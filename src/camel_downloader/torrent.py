import shutil
import subprocess
import tempfile
import time
from pathlib import Path

import requests
from rich.console import Console
from rich.progress import (
    BarColumn, DownloadColumn, Progress,
    TextColumn, TimeRemainingColumn, TransferSpeedColumn,
)

from .utils import ensure_output_dir, fmt_bytes

console = Console()


def download_torrent(source: str, output_dir: Path, seed_after: bool = False) -> bool:
    ensure_output_dir(output_dir)

    try:
        import libtorrent as lt
        return _download_libtorrent(source, output_dir, seed_after, lt)
    except ImportError:
        pass

    if shutil.which("aria2c"):
        return _download_aria2(source, output_dir)

    console.print("[red]✗ No torrent backend found.[/]")
    console.print("\n[bold]Install one of the following:[/]")
    console.print("  Android/Termux: [dim]pkg install aria2[/]")
    console.print("  Ubuntu/Debian:  [dim]sudo apt install python3-libtorrent[/]")
    console.print("  macOS:          [dim]brew install aria2[/]")
    console.print("  Windows:        [dim]winget install aria2[/]  [bold]or[/]  [dim]pip install libtorrent[/]")
    return False


# ── aria2c backend ────────────────────────────────────────────

def _download_aria2(source: str, output_dir: Path) -> bool:
    console.print("\n[bold yellow]🧲  Torrent Download[/] [dim](via aria2c)[/]")
    console.print(f"[bold]Save:[/]  {output_dir}\n")

    cmd = [
        "aria2c",
        "--dir", str(output_dir),
        "--seed-time=0",          # don't seed after finish
        "--max-connection-per-server=4",
        "--split=4",
        "--console-log-level=warn",
        "--summary-interval=3",
        source,
    ]

    try:
        result = subprocess.run(cmd, check=True)
        console.print(f"\n[green]✓ Download complete:[/] {output_dir}")
        return result.returncode == 0

    except subprocess.CalledProcessError as e:
        console.print(f"[red]✗ aria2c error (exit {e.returncode})[/]")
        return False
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️  Download cancelled (Ctrl+C).[/]")
        return False


# ── libtorrent backend ────────────────────────────────────────

def _download_libtorrent(source: str, output_dir: Path, seed_after: bool, lt) -> bool:
    console.print("\n[bold yellow]🧲  Torrent Download[/]")

    ses = lt.session()
    ses.listen_on(6881, 6891)
    ses.add_dht_router("router.bittorrent.com", 6881)
    ses.add_dht_router("router.utorrent.com", 6881)
    ses.add_dht_router("dht.transmissionbt.com", 6881)
    ses.start_dht()
    ses.start_lsd()
    ses.start_upnp()
    ses.start_natpmp()

    params = {
        "save_path": str(output_dir),
        "storage_mode": lt.storage_mode_t.storage_mode_sparse,
    }

    handle = None

    if source.startswith("magnet:"):
        console.print("[dim]Adding magnet link…[/]")
        handle = lt.add_magnet_uri(ses, source, params)
        console.print("[dim]Fetching torrent metadata via DHT…[/]")
        with console.status("[yellow]Waiting for peers/metadata…[/]", spinner="dots"):
            start = time.time()
            while not handle.has_metadata():
                time.sleep(0.5)
                if time.time() - start > 60:
                    console.print("[red]✗ Metadata timeout. Check magnet link or internet.[/]")
                    return False

    elif source.endswith(".torrent"):
        torrent_path = source
        if source.startswith("http"):
            console.print("[dim]Downloading .torrent file…[/]")
            try:
                r = requests.get(source, timeout=20)
                r.raise_for_status()
                with tempfile.NamedTemporaryFile(suffix=".torrent", delete=False) as tf:
                    tf.write(r.content)
                    torrent_path = tf.name
            except requests.RequestException as e:
                console.print(f"[red]✗ Failed to fetch .torrent file:[/] {e}")
                return False

        info = lt.torrent_info(torrent_path)
        params["ti"] = info
        handle = ses.add_torrent(params)

    else:
        console.print("[red]✗ Not a valid torrent source.[/]")
        return False

    info = handle.get_torrent_info()
    name = info.name() if info else "Unknown"
    size = info.total_size() if info else 0

    console.print(f"[bold]Name:[/]  [cyan]{name}[/]")
    if size:
        console.print(f"[bold]Size:[/]  {fmt_bytes(size)}")
    console.print(f"[bold]Save:[/]  {output_dir}\n")

    try:
        with Progress(
            TextColumn("[bold yellow]{task.fields[name]}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            DownloadColumn(),
            TransferSpeedColumn(),
            TimeRemainingColumn(),
            TextColumn("[dim]↑{task.fields[up]} peers:{task.fields[peers]}[/]"),
            console=console,
            refresh_per_second=2,
        ) as progress:
            task = progress.add_task(
                "torrent",
                name=name[:40],
                total=size or 1,
                up="0B/s",
                peers=0,
            )
            while True:
                s = handle.status()
                progress.update(
                    task,
                    completed=s.total_done,
                    up=fmt_bytes(s.upload_rate) + "/s",
                    peers=s.num_peers,
                )
                if s.is_seeding or s.state == lt.torrent_status.seeding:
                    progress.update(task, completed=size or s.total_done)
                    break
                time.sleep(1)

        console.print(f"[green]✓ Torrent complete:[/] {output_dir / name}")
        if not seed_after:
            ses.remove_torrent(handle)
        return True

    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️  Download paused (Ctrl+C). Partial files saved.[/]")
        return False
