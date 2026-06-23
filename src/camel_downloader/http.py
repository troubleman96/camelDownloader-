from pathlib import Path
from urllib.parse import urlparse

import requests
from rich.console import Console
from rich.progress import (
    BarColumn, DownloadColumn, Progress,
    TextColumn, TimeRemainingColumn, TransferSpeedColumn,
)

from .utils import ensure_output_dir

console = Console()


def download_http(url: str, output_dir: Path, filename: str | None = None) -> bool:
    console.print(f"\n[bold cyan]⬇  HTTP Download[/] → [dim]{url}[/]")

    try:
        with requests.get(url, stream=True, timeout=30, allow_redirects=True) as r:
            r.raise_for_status()

            if not filename:
                cd = r.headers.get("content-disposition", "")
                if "filename=" in cd:
                    filename = cd.split("filename=")[-1].strip('" ')
                else:
                    filename = Path(urlparse(url).path).name or "download"

            ensure_output_dir(output_dir)
            dest = output_dir / filename
            total = int(r.headers.get("content-length", 0))

            with Progress(
                TextColumn("[bold blue]{task.fields[filename]}"),
                BarColumn(),
                DownloadColumn(),
                TransferSpeedColumn(),
                TimeRemainingColumn(),
                console=console,
            ) as progress:
                task = progress.add_task("download", filename=filename, total=total or None)
                with open(dest, "wb") as f:
                    for chunk in r.iter_content(chunk_size=1024 * 64):
                        f.write(chunk)
                        progress.advance(task, len(chunk))

        console.print(f"[green]✓ Saved:[/] {dest}")
        return True

    except requests.RequestException as e:
        console.print(f"[red]✗ HTTP error:[/] {e}")
        return False
