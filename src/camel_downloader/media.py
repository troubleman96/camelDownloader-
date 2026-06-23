import subprocess
from pathlib import Path

from rich.console import Console

from .utils import format_duration

console = Console()

QUALITY_MAP = {
    '1': 'bestvideo[height<=360]+bestaudio/best[height<=360]',
    '2': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
    '3': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
    '4': 'bestvideo[height<=1440]+bestaudio/best[height<=1440]',
    '5': 'bestvideo[height<=2160]+bestaudio/best[height<=2160]',
    '6': 'bestvideo+bestaudio/best',
    '7': 'bestaudio/best',
}

QUALITY_LABELS = {
    '1': '360p  (SD)',
    '2': '720p  (HD)',
    '3': '1080p (Full HD)',
    '4': '1440p (2K)',
    '5': '2160p (4K)',
    '6': 'Best Available',
    '7': 'Audio Only (MP3)',
}

_last_pct = -1


def check_ffmpeg() -> bool:
    try:
        subprocess.run(
            ['ffmpeg', '-version'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        console.print("[red]✗ ffmpeg not installed.[/]")
        console.print("  Ubuntu/Debian: [dim]sudo apt install ffmpeg[/]")
        console.print("  Termux:        [dim]pkg install ffmpeg[/]")
        console.print("  macOS:         [dim]brew install ffmpeg[/]")
        return False


def _progress_hook(d: dict) -> None:
    global _last_pct  # noqa: PLW0603
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A').strip()
        speed = d.get('_speed_str', 'N/A').strip()
        eta = d.get('_eta_str', 'N/A').strip()
        downloaded = d.get('downloaded_bytes', 0)
        total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)

        try:
            pct = float(percent.replace('%', ''))
            if int(pct) == _last_pct:
                return
            _last_pct = int(pct)
        except Exception:
            pass

        if total:
            from .utils import fmt_bytes
            size_info = f"{fmt_bytes(downloaded)}/{fmt_bytes(total)}"
        else:
            from .utils import fmt_bytes
            size_info = fmt_bytes(downloaded)

        print(f"\r⬇️  {percent} | {size_info} | Speed: {speed} | ETA: {eta}   ", end='', flush=True)

    elif d['status'] == 'finished':
        _last_pct = -1
        print("\n🔄 Merging video and audio streams...")

    elif d['status'] == 'error':
        print("\n❌ Download error occurred")


def download_media(url: str, output_dir: Path, quality_choice: str = '6') -> bool:
    try:
        import yt_dlp
    except ImportError:
        console.print("[red]✗ yt-dlp not installed.[/] Run: [dim]pip install yt-dlp[/]")
        return False

    if not check_ffmpeg():
        return False

    ydl_opts = {
        'format': QUALITY_MAP.get(quality_choice, QUALITY_MAP['6']),
        'outtmpl': str(output_dir / '%(title)s.%(ext)s'),
        'restrictfilenames': False,
        'windowsfilenames': False,
        'merge_output_format': 'mp4',
        'geo_bypass': True,
        'nocheckcertificate': True,
        'retries': 10,
        'fragment_retries': 10,
        'socket_timeout': 30,
        'quiet': False,
        'no_warnings': False,
        'verbose': False,
        'age_limit': None,
        'progress_hooks': [_progress_hook],
    }

    if quality_choice == '7':
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
        ydl_opts.pop('merge_output_format', None)

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            console.print("\n🔍 Fetching info...")
            console.print("─" * 60)

            try:
                info = ydl.extract_info(url, download=False)
            except yt_dlp.utils.DownloadError as e:
                console.print(f"[red]✗ Cannot access video:[/] {e}")
                return False

            title = info.get('title', 'Unknown')
            uploader = info.get('uploader', 'Unknown')
            duration = info.get('duration', 0)
            view_count = info.get('view_count', 0)

            console.print(f"📹 [bold]{title}[/]")
            console.print(f"👤 {uploader}")
            console.print(f"⏱️  {format_duration(duration)}")
            if view_count:
                console.print(f"👁️  {view_count:,} views")

            if info.get('formats'):
                heights = sorted(
                    {f['height'] for f in info['formats'] if f.get('height')},
                    reverse=True,
                )
                if heights:
                    console.print(f"📊 Resolutions: {', '.join(f'{h}p' for h in heights)}")

            console.print("─" * 60)
            console.print(f"\n✅ Quality: [cyan]{QUALITY_LABELS.get(quality_choice, 'Best')}[/]")
            console.print("⬇️  Starting download...\n")

            ydl.download([url])

        console.print("\n" + "═" * 60)
        console.print("[green]✅ DOWNLOAD COMPLETE![/]")
        console.print("═" * 60)
        console.print(f"📁 [dim]{output_dir}[/]")
        console.print("═" * 60)
        return True

    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️  Download cancelled (Ctrl+C)[/]")
        return False

    except yt_dlp.utils.DownloadError as e:
        console.print(f"\n[red]✗ Download error:[/] {e}")
        console.print("💡 Try: [dim]pip install -U yt-dlp[/]")
        return False

    except PermissionError:
        console.print(f"\n[red]✗ Permission denied:[/] {output_dir}")
        return False

    except OSError as e:
        console.print(f"\n[red]✗ System error:[/] {e}")
        return False
