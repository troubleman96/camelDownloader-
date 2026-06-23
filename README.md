# camelDownloader 🐫

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![yt-dlp](https://img.shields.io/badge/powered%20by-yt--dlp-FF0000.svg)](https://github.com/yt-dlp/yt-dlp)

**camelDownloader** is a production-ready YouTube downloader with a global CLI — run `camel-downloader` from any terminal, on any platform, without activating a virtual environment.

---

## ✨ Key Features

- 📺 **All Resolutions**: 360p, 720p, 1080p, 1440p, 4K — your choice.
- 🎵 **Audio Extraction**: One-click MP3 conversion at 192kbps.
- 🚀 **No Quality Loss**: Smart MP4/MKV merging with no forced re-encoding.
- 🛠️ **Built for Stability**: 10x auto-retry on network failures, geo-bypass support.
- 📊 **Live Progress**: Real-time speed, ETA, and file size in the terminal.
- 📁 **Organized Saves**: Downloads go to `~/Downloads/camelDownloader` (or Android's public Downloads on Termux).
- 🤖 **Global CLI**: One command — `camel-downloader` — works from anywhere after install.

---

## 📋 Prerequisites

1. **Python 3.8+**
2. **FFmpeg** — required for merging video and audio streams.

| Platform       | Install command                                    |
|----------------|----------------------------------------------------|
| Ubuntu / Debian | `sudo apt install ffmpeg`                         |
| macOS          | `brew install ffmpeg`                              |
| Termux         | `pkg install ffmpeg`                               |
| Windows        | [ffmpeg.org/download](https://ffmpeg.org/download.html) |

---

## 🚀 Installation

### Ubuntu / Debian / macOS

```bash
pip install camelDownloader
```

Make the command available globally (only needed once):

```bash
mkdir -p ~/.local/bin
ln -sf $(which camel-downloader) ~/.local/bin/camel-downloader
```

> `~/.local/bin` is already in `$PATH` on most Linux/macOS systems. If not, add
> `export PATH="$HOME/.local/bin:$PATH"` to your `~/.bashrc` or `~/.zshrc`.

### Termux (Android)

```bash
# 1. Install system dependencies
pkg update && pkg install python ffmpeg

# 2. Install the package
pip install camelDownloader

# 3. (One-time) Grant storage access so files appear in Android's file manager
termux-setup-storage
```

Downloads will be saved to `~/storage/downloads/camelDownloader` (Android's public Downloads folder).

### From Source

```bash
git clone https://github.com/troubleman96/camel-Downloader.git
cd camel-Downloader
pip install .
```

---

## 🎮 Usage

```bash
camel-downloader
```

`camel` works as a short alias too.

Follow the interactive prompts:

```
🔗 Enter YouTube URL: https://www.youtube.com/watch?v=...

📊 SELECT QUALITY:
1) 360p  - SD       (Small file, fast download)
2) 720p  - HD       (Balanced quality and size)
3) 1080p - Full HD  (High quality, larger file)
4) 1440p - 2K       (Very high quality)
5) 2160p - 4K       (Maximum quality, huge file)
6) Best  - Auto     (Let YouTube decide best quality)
7) Audio - MP3      (Sound only, ~3MB per minute)

👉 Your choice (1-7):
```

---

## ⚙️ How the CLI Works

The `camel-downloader` command is registered as a Python **entry point** in `pyproject.toml`:

```toml
[project.scripts]
camel-downloader = "camel_downloader.main:main"
camel            = "camel_downloader.main:main"
```

When pip installs the package it generates a real executable script at
`<env>/bin/camel-downloader` that calls `main()` directly — no manual script needed.
Symlinking that file into `~/.local/bin` (which is in `$PATH`) makes it reachable
from any terminal without activating a virtual environment.

---

## 🛠️ Project Structure

```
camel-downloader/
├── src/
│   └── camel_downloader/
│       ├── __init__.py
│       └── main.py          # Core logic & CLI entry point
├── pyproject.toml           # Build config, dependencies & CLI entry points
├── setup.py                 # Minimal setuptools shim
└── README.md
```

---

## 🤝 Contributing

Open issues for bugs or feature requests, or submit a Pull Request.

---

## 📜 License

Distributed under the MIT License.
