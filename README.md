# camelDownloader 🐫

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![yt-dlp](https://img.shields.io/badge/powered%20by-yt--dlp-FF0000.svg)](https://github.com/yt-dlp/yt-dlp)

**camelDownloader** is a production-ready, high-performance YouTube downloader designed for simplicity and reliability. It provides a clean CLI interface to download videos in any resolution (up to 4K) or extract high-quality audio with ease.

---

## ✨ Key Features

- 📺 **All Resolutions Support**: Choose from 360p up to 2160p (4K).
- 🎵 **Smart Audio Extraction**: One-click MP3 conversion at 192kbps.
- 🚀 **No Quality Loss**: Uses smart merging (MP4/MKV) without forced re-encoding.
- 🛠️ **Built for Stability**: 10x auto-retry on network failures and geographic bypass support.
- 📊 **Clean Progress UI**: Real-time download speed, ETA, and file size tracking.
- 📁 **Organized Downloads**: Automatically saves to `~/Downloads/camelDownloader`.

---

## 📋 Prerequisites

Before installing, ensure you have the following requirements:

1. **Python 3.8+**
2. **FFmpeg**: Required for merging video/audio streams and audio extraction.
   - **Ubuntu/Debian**: `sudo apt install ffmpeg`
   - **macOS**: `brew install ffmpeg`
   - **Termux**: `pkg install ffmpeg`
   - **Windows**: [Download from ffmpeg.org](https://ffmpeg.org/download.html)

---

## 🚀 Installation

### via PyPI (Recommended)

```bash
pip install camelDownloader
```

### from Source

```bash
git clone https://github.com/troubleman96/camel-Downloader.git
cd camel-Downloader
pip install .
```

---

## 🎮 Usage

Simply run the command from any terminal:

```bash
camel
```

Follow the interactive prompts:
1. Paste your **YouTube URL**.
2. Select your desired **Quality** (1-7).
3. Sit back and relax! 🐫

---

## 🛠️ Project Structure

```text
camel-Downloader/
├── src/
│   └── camel_downloader/
│       ├── __init__.py
│       └── main.py          # Core logic & CLI
├── pyproject.toml           # Build system & dependencies
├── README.md                # Project documentation
└── setup.py                 # Package shim
```

---

## 🤝 Contributing

This is an open-source project. Feel free to:
- Open issues for bugs or feature requests.
- Submit Pull Requests to improve the code or documentation.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
