# camelDownloader 🐫

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyPI version](https://img.shields.io/pypi/v/camelDownloader.svg)](https://pypi.org/project/camelDownloader/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![yt-dlp](https://img.shields.io/badge/powered%20by-yt--dlp-FF0000.svg)](https://github.com/yt-dlp/yt-dlp)

**camelDownloader** is a free, open-source general purpose downloader that runs entirely in your terminal. One command. Paste any link. It auto-detects whether it's a YouTube video, a direct file, a TikTok, a magnet link, or a torrent — and downloads it.

Works on Linux, macOS, Android (Termux), and Windows.

---

## What It Handles

| Link Type | Examples |
|---|---|
| 🎬 YouTube & 1000+ sites | YouTube, TikTok, Twitter/X, Instagram, Vimeo, SoundCloud, Twitch… |
| 🌐 Direct HTTP/HTTPS | `.zip`, `.mp4`, `.pdf`, any direct file link |
| 🧲 Magnet links | `magnet:?xt=urn:btih:...` |
| 📦 Torrent files | `.torrent` URL or local file path |

---

## Quick Demo

```
camel

════════════════════════════════════════════════════════════
                 camelDownloader 🐫
              General Purpose Downloader
   Handles YouTube, HTTP files, Torrents & 1000+ sites
════════════════════════════════════════════════════════════

🔗 Paste your link (or 'q' to quit): https://youtube.com/watch?v=dQw4w9WgXcQ

✅ Detected: 🎬  Media / YouTube / TikTok / Twitter…

📊 SELECT QUALITY:
────────────────────────────────────────
  1)  360p  (SD)
  2)  720p  (HD)
  ...
👉 Your choice (1-7): 2

📹 Never Gonna Give You Up
👤 Rick Astley  ⏱️ 3:33  👁️ 1,500,000,000 views
⬇️  100% | 45.2MB/45.2MB | Speed: 3.2MiB/s | ETA: 0s
✅ DOWNLOAD COMPLETE!
📁 ~/Downloads/camelDownloader
```

---

## Installation

### Linux (Ubuntu / Debian)

```bash
# Prerequisites
sudo apt update
sudo apt install python3 python3-pip ffmpeg -y

# Optional: torrent/magnet support
sudo apt install python3-libtorrent -y

# Install
pip install camelDownloader
```

### macOS

```bash
brew install python ffmpeg
pip3 install camelDownloader
```

### Android (Termux)

```bash
# Update and install prerequisites
pkg update -y && pkg upgrade -y
pkg install python ffmpeg openssl -y

# Grant storage access (one-time — tap Allow when prompted)
termux-setup-storage

# Install
pip install camelDownloader
```

### Windows

```powershell
# Install Python and FFmpeg via winget (run as admin)
winget install Python.Python.3 -e
winget install Gyan.FFmpeg -e

# Then install in Command Prompt
pip install camelDownloader
```

### From Source

```bash
git clone https://github.com/troubleman96/camelDownloader-.git
cd camelDownloader-
pip install -e .
```

---

## Usage

Run the command from any terminal:

```bash
camel
```

You will be prompted to paste a link. The app auto-detects the type and routes it:

- **YouTube / TikTok / Twitter / Vimeo / etc.** → shows quality menu (1–7), then downloads
- **Direct file URL** → downloads immediately with progress bar
- **Magnet link or .torrent** → connects to DHT, fetches metadata, downloads

Type `q` at the link prompt to quit.

---

## Quality Options (media links only)

| # | Quality | Best For | ~Size (10 min) |
|---|---------|----------|----------------|
| 1 | 360p SD | Slow internet, mobile data | ~50 MB |
| 2 | 720p HD | Most use cases | ~150 MB |
| 3 | 1080p Full HD | Desktop viewing | ~300 MB |
| 4 | 1440p 2K | Large screens | ~600 MB |
| 5 | 2160p 4K | 4K displays, editing | ~1.5 GB |
| 6 | Best Auto | Maximum available | Varies |
| 7 | Audio MP3 | Music, podcasts | ~25 MB |

---

## Where Downloads Go

| Platform | Location |
|---|---|
| Linux | `~/Downloads/camelDownloader/` |
| macOS | `~/Downloads/camelDownloader/` |
| Android (Termux) | `~/storage/downloads/camelDownloader/` → Android **Downloads** folder |
| Windows | `C:\Users\YourName\Downloads\camelDownloader\` |

---

## Troubleshooting

### `camel: command not found`

```bash
# Linux / macOS
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

On Termux, close and reopen the app then try again.

### `ffmpeg not installed`

```bash
# Ubuntu/Debian
sudo apt install ffmpeg
# macOS
brew install ffmpeg
# Termux
pkg install ffmpeg
# Windows
winget install Gyan.FFmpeg -e
```

### `libtorrent not installed` (torrent/magnet only)

```bash
# Ubuntu/Debian
sudo apt install python3-libtorrent
# pip (if apt version not available)
pip install libtorrent
```

### Download fails / 403 error

Update yt-dlp — YouTube changes its API frequently:

```bash
pip install -U yt-dlp
```

### `termux-setup-storage` failed (Android)

Run it again and tap **Allow** when prompted. If the popup never appears, go to Android Settings → Apps → Termux → Permissions → Files and Media → Allow.

---

## Project Structure

```
src/camel_downloader/
├── main.py      # entry point — banner, prompt, routing
├── detect.py    # classifies any URL (media / http / torrent)
├── http.py      # direct HTTP/HTTPS file downloads
├── media.py     # yt-dlp backend (YouTube, TikTok, 1000+ sites)
├── torrent.py   # magnet links & .torrent files (libtorrent)
└── utils.py     # shared helpers (fmt_bytes, get_download_dir…)
```

---

## Contributing

```bash
# Fork on GitHub, then:
git clone https://github.com/YOUR_USERNAME/camelDownloader-.git
cd camelDownloader-
pip install -e .
git checkout -b my-feature
# make your changes...
git add . && git commit -m "describe your change"
git push origin my-feature
# open a Pull Request on GitHub
```

Bug reports and feature requests → [open an issue](https://github.com/troubleman96/camelDownloader-/issues).

---

## License

Distributed under the **MIT License** — free to use, modify, and distribute for any purpose.
