import os
from pathlib import Path


def fmt_bytes(num: float) -> str:
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if num < 1024:
            return f"{num:.1f} {unit}"
        num /= 1024
    return f"{num:.1f} PB"


def format_duration(seconds) -> str:
    if not seconds:
        return "Unknown"
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"


def ensure_output_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def get_download_dir(subfolder: str = "camelDownloader") -> Path:
    is_termux = "TERMUX_VERSION" in os.environ or os.path.exists("/data/data/com.termux")
    if is_termux:
        if os.path.exists(os.path.expanduser("~/storage/downloads")):
            base = Path(os.path.expanduser("~/storage/downloads"))
        elif os.path.exists("/sdcard/Download"):
            base = Path("/sdcard/Download")
        elif os.path.exists("/storage/emulated/0/Download"):
            base = Path("/storage/emulated/0/Download")
        else:
            print("⚠️  Downloads going to a hidden folder.")
            print("💡 Fix: Run `termux-setup-storage` in Termux and tap Allow.")
            base = Path(os.path.expanduser("~/downloads"))
    else:
        base = Path.home() / "Downloads"

    path = base / subfolder
    ensure_output_dir(path)
    return path
