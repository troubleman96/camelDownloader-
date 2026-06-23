#!/usr/bin/env python3
"""
camelDownloader 🐫
General Purpose Downloader — HTTP, YouTube/media, Torrents
"""

import sys

from rich.console import Console

from .detect import detect_link_type
from .http import download_http
from .media import QUALITY_LABELS, download_media
from .torrent import download_torrent
from .utils import get_download_dir

console = Console()

BANNER = """
════════════════════════════════════════════════════════════
                 camelDownloader 🐫
              General Purpose Downloader
   Handles YouTube, HTTP files, Torrents & 1000+ sites
════════════════════════════════════════════════════════════
"""

TYPE_LABELS = {
    "media":          "🎬  Media / YouTube / TikTok / Twitter…",
    "http":           "🌐  Direct HTTP download",
    "torrent_magnet": "🧲  Magnet link",
    "torrent_file":   "📦  Torrent file",
}


def ask_quality() -> str:
    console.print("\n[bold]📊 SELECT QUALITY:[/]")
    console.print("─" * 40)
    for key, label in QUALITY_LABELS.items():
        console.print(f"  {key})  {label}")
    console.print("─" * 40)

    while True:
        choice = input("\n👉 Your choice (1-7): ").strip()
        if choice in QUALITY_LABELS:
            return choice
        console.print("[red]Invalid choice — enter a number from 1 to 7.[/]")


def main():
    print(BANNER)

    output_dir = get_download_dir()

    while True:
        try:
            url = input("🔗 Paste your link (or 'q' to quit): ").strip()
        except (KeyboardInterrupt, EOFError):
            console.print("\n\n👋 Goodbye!")
            sys.exit(0)

        if url.lower() in ("q", "quit", "exit"):
            console.print("\n👋 Goodbye!")
            sys.exit(0)

        if not url:
            console.print("[yellow]No link entered. Try again.[/]")
            continue

        link_type = detect_link_type(url)
        console.print(f"\n✅ Detected: [cyan]{TYPE_LABELS.get(link_type, link_type)}[/]")

        if link_type == "media":
            quality = ask_quality()
            download_media(url, output_dir, quality_choice=quality)

        elif link_type == "http":
            download_http(url, output_dir)

        elif link_type in ("torrent_magnet", "torrent_file"):
            download_torrent(url, output_dir)

        else:
            console.print(f"[red]✗ Unknown link type: {link_type}[/]")
            continue

        console.print()
        another = input("⬇️  Download another? (y/n): ").strip().lower()
        if another != "y":
            console.print("\n👋 Goodbye!")
            sys.exit(0)

        print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n\n👋 Goodbye!")
        sys.exit(0)
