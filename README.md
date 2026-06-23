# camelDownloader 🐫

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![yt-dlp](https://img.shields.io/badge/powered%20by-yt--dlp-FF0000.svg)](https://github.com/yt-dlp/yt-dlp)

**camelDownloader** is a free, open-source YouTube downloader that runs entirely in your terminal. No browser extensions, no ads, no limits. Download any YouTube video in any quality — from 360p all the way up to 4K — or extract audio as MP3. Works on Linux, macOS, Android (Termux), and Windows.

---

## Table of Contents

1. [What It Does](#-what-it-does)
2. [Key Features](#-key-features)
3. [How It Works](#-how-it-works)
4. [Prerequisites](#-prerequisites)
5. [Installation](#-installation)
   - [Linux (Ubuntu / Debian)](#linux-ubuntu--debian)
   - [macOS](#macos)
   - [Android (Termux)](#android-termux)
   - [Windows](#windows)
   - [From Source (All Platforms)](#from-source-all-platforms)
6. [Usage](#-usage)
7. [Quality Options](#-quality-options)
8. [Where Do Downloads Go?](#-where-do-downloads-go)
9. [Troubleshooting](#-troubleshooting)
10. [Project Structure](#-project-structure)
11. [Contributing](#-contributing)
12. [License](#-license)

---

## 🎯 What It Does

You give it a YouTube URL. It downloads the video (or audio) to your device in whatever quality you choose. That's it.

```
camel-downloader

🔗 Enter YouTube URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
👉 Your choice (1-7): 2

✅ DOWNLOAD COMPLETE!
📁 Location: ~/Downloads/camelDownloader
```

---

## ✨ Key Features

- 📺 **All Resolutions** — 360p, 720p, 1080p, 1440p (2K), and 2160p (4K)
- 🎵 **MP3 Audio Extraction** — download sound only at 192kbps
- 🚀 **No Quality Loss** — merges video and audio without re-encoding
- 🛠️ **Reliable** — auto-retries 10 times on network failures, bypasses geo-restrictions
- 📊 **Live Progress** — shows download speed, percentage, ETA, and file size in real time
- 📁 **Organized** — files are saved to a dedicated `camelDownloader` folder
- 🤖 **True CLI** — one global command (`camel-downloader`) works from any terminal window, anywhere on your system
- 📱 **Android Support** — works on Android via Termux, saves to your public Downloads folder
- 🆓 **Free & Open Source** — MIT licensed, no accounts, no subscriptions

---

## ⚙️ How It Works

camelDownloader is built on top of [yt-dlp](https://github.com/yt-dlp/yt-dlp), the most powerful YouTube downloading library available. Here is what happens when you run it:

1. You paste a YouTube URL and pick a quality.
2. yt-dlp fetches the video metadata (title, duration, available resolutions).
3. It downloads the video stream and audio stream separately (YouTube stores them apart for HD content).
4. FFmpeg merges them into a single MP4 file on your device.
5. The file is saved to your Downloads folder.

---

## 📋 Prerequisites

Before installing camelDownloader, you need two things:

### 1. Python 3.8 or higher

Check if you have it:
```bash
python3 --version
```

If not installed:

| Platform | How to install Python |
|---|---|
| Ubuntu / Debian | `sudo apt install python3` |
| macOS | `brew install python` or [python.org](https://www.python.org/downloads/) |
| Android (Termux) | `pkg install python` |
| Windows | [python.org/downloads](https://www.python.org/downloads/) — check "Add to PATH" during install |

### 2. FFmpeg

FFmpeg is used to merge the video and audio streams into one file. Without it, HD downloads will have no sound.

| Platform | How to install FFmpeg |
|---|---|
| Ubuntu / Debian | `sudo apt install ffmpeg` |
| macOS | `brew install ffmpeg` |
| Android (Termux) | `pkg install ffmpeg` |
| Windows | [ffmpeg.org/download](https://ffmpeg.org/download.html) — add to PATH after installing |

---

## 🚀 Installation

### Linux (Ubuntu / Debian)

```bash
# Step 1 — Install prerequisites
sudo apt update
sudo apt install python3 python3-pip ffmpeg -y

# Step 2 — Install camelDownloader
pip install camelDownloader

# Step 3 — Make the command available globally (run once)
mkdir -p ~/.local/bin
ln -sf $(which camel-downloader) ~/.local/bin/camel-downloader
```

> If `camel-downloader` is still not found after Step 3, add this line to your `~/.bashrc` file:
> ```bash
> export PATH="$HOME/.local/bin:$PATH"
> ```
> Then run `source ~/.bashrc` to apply it.

**Verify the install:**
```bash
camel-downloader
```

---

### macOS

```bash
# Step 1 — Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Step 2 — Install prerequisites
brew install python ffmpeg

# Step 3 — Install camelDownloader
pip3 install camelDownloader
```

**Verify the install:**
```bash
camel-downloader
```

---

### Android (Termux)

Termux is a free Android terminal app. It lets you run Linux commands directly on your phone — no root required.

**Step 1 — Install Termux**

Download Termux from **F-Droid** (the Play Store version is outdated and broken):

👉 [https://f-droid.org/en/packages/com.termux/](https://f-droid.org/en/packages/com.termux/)

**Step 2 — Open Termux and run these commands**

```bash
# Update Termux packages
pkg update && pkg upgrade -y

# Install Python and FFmpeg
pkg install python ffmpeg -y

# Install camelDownloader
pip install camelDownloader
```

**Step 3 — Grant storage access (one-time)**

This lets your downloads appear in Android's file manager (Files app, Downloads folder):

```bash
termux-setup-storage
```

Tap **Allow** when Android asks for permission.

**Verify the install:**
```bash
camel-downloader
```

---

### Windows

**Step 1 — Install Python**

Download from [python.org/downloads](https://www.python.org/downloads/).
During installation, **check the box that says "Add Python to PATH"**.

**Step 2 — Install FFmpeg**

1. Download FFmpeg from [ffmpeg.org/download](https://ffmpeg.org/download.html)
2. Extract the zip file
3. Copy the path to the `bin` folder inside (e.g. `C:\ffmpeg\bin`)
4. Add it to your system PATH:
   - Search "Environment Variables" in the Start menu
   - Click "Environment Variables"
   - Under "System variables", find `Path`, click Edit
   - Click New and paste the path to ffmpeg's `bin` folder
   - Click OK on all windows

**Step 3 — Open Command Prompt and install**

```bash
pip install camelDownloader
```

**Verify the install:**
```bash
camel-downloader
```

---

### From Source (All Platforms)

Use this if you want to run the latest development code or contribute to the project.

```bash
# Clone the repository
git clone https://github.com/troubleman96/camelDownloader-.git
cd camelDownloader-

# Install in editable mode (changes to source take effect immediately)
pip install -e .
```

---

## 🎮 Usage

Run the command from any terminal:

```bash
camel-downloader
```

`camel` also works as a shorter alias:

```bash
camel
```

You will see this screen:

```
════════════════════════════════════════════════════════════
                 camelDownloader 🐫
           Production YouTube Downloader
     Handles ANY video type, length, and quality
════════════════════════════════════════════════════════════

🔗 Enter YouTube URL:
```

**Step 1** — Paste your YouTube link and press Enter.

```
🔍 Fetching video information...
────────────────────────────────────────────────────────────
📹 Title: Never Gonna Give You Up
👤 Uploader: Rick Astley
⏱️  Duration: 3:33
👁️  Views: 1,500,000,000
📊 Available resolutions: 1080p, 720p, 480p, 360p, 240p, 144p
────────────────────────────────────────────────────────────
```

**Step 2** — Choose your quality:

```
📊 SELECT QUALITY:
────────────────────────────────────────────────────────────
1) 360p  - SD       (Small file, fast download)
2) 720p  - HD       (Balanced quality and size)
3) 1080p - Full HD  (High quality, larger file)
4) 1440p - 2K       (Very high quality)
5) 2160p - 4K       (Maximum quality, huge file)
6) Best  - Auto     (Let YouTube decide best quality)
7) Audio - MP3      (Sound only, ~3MB per minute)
────────────────────────────────────────────────────────────

👉 Your choice (1-7):
```

**Step 3** — Wait for the download to finish:

```
⬇️  78.3% | 45.2MB/57.8MB | Speed: 3.2MiB/s | ETA: 4s
🔄 Merging video and audio streams (this may take a moment)...

════════════════════════════════════════════════════════════
✅ DOWNLOAD COMPLETE!
════════════════════════════════════════════════════════════
📁 Location: ~/Downloads/camelDownloader
📄 Filename: Never Gonna Give You Up
════════════════════════════════════════════════════════════
```

---

## 📊 Quality Options

| Option | Label | Best For | Approx. File Size (10 min video) |
|--------|-------|----------|----------------------------------|
| 1 | 360p SD | Slow internet, saving data | ~50 MB |
| 2 | 720p HD | Most use cases, good balance | ~150 MB |
| 3 | 1080p Full HD | Desktop viewing, archiving | ~300 MB |
| 4 | 1440p 2K | Large monitors, high quality | ~600 MB |
| 5 | 2160p 4K | 4K displays, video editing | ~1.5 GB |
| 6 | Best Auto | Maximum quality available | Varies |
| 7 | Audio MP3 | Music, podcasts, audio only | ~25 MB |

> File sizes are estimates. Actual sizes depend on the video content and YouTube's encoding.

---

## 📁 Where Do Downloads Go?

Files are saved automatically — you don't need to choose a folder.

| Platform | Download Location |
|---|---|
| Linux | `~/Downloads/camelDownloader/` |
| macOS | `~/Downloads/camelDownloader/` |
| Android (Termux) | `~/storage/downloads/camelDownloader/` → visible in your Android **Downloads** folder |
| Windows | `C:\Users\YourName\Downloads\camelDownloader\` |

On Android, after downloading, open your **Files** app and go to **Downloads → camelDownloader** to find your file.

---

## 🛠️ Troubleshooting

### `camel-downloader: command not found`

The command is not in your PATH. Fix it:

```bash
# Linux / macOS
mkdir -p ~/.local/bin
ln -sf $(which camel-downloader) ~/.local/bin/camel-downloader
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

On Android (Termux), this should not happen after a successful `pip install`. Try closing and reopening Termux, then run `camel-downloader` again.

---

### `ffmpeg not installed` error

Install FFmpeg for your platform (see [Prerequisites](#-prerequisites) above).

---

### `termux-setup-storage` aborted or failed (Android)

This is a known Termux bug. Try again:

```bash
termux-setup-storage
```

Make sure to tap **Allow** when Android shows the permission popup. If it keeps failing, your downloads will still work — they just save to Termux's internal folder (`~/downloads/`) instead of the public Downloads folder.

---

### Download fails or gives a 403 error

yt-dlp may be outdated. Update it:

```bash
pip install -U yt-dlp
```

---

### Video says it's age-restricted or private

Age-restricted videos require YouTube login cookies. This is an advanced use case — open an issue on GitHub and we can help.

---

### Disk full or permission error

Check that you have enough storage space on your device. On Android, make sure `termux-setup-storage` has been run and storage permission was granted.

---

## 🗂️ Project Structure

```
camel-downloader/
├── src/
│   └── camel_downloader/
│       ├── __init__.py       # Package marker
│       └── main.py           # All core logic and CLI entry point
├── pyproject.toml            # Build config, dependencies, CLI entry points
├── setup.py                  # Minimal setuptools shim
└── README.md                 # This file
```

### How the CLI command is registered

The `camel-downloader` command is defined in `pyproject.toml`:

```toml
[project.scripts]
camel-downloader = "camel_downloader.main:main"
camel            = "camel_downloader.main:main"
```

When pip installs the package it automatically generates an executable script at
`<env>/bin/camel-downloader` that calls the `main()` function in `main.py`.
No manual scripting needed — pip handles it all.

---

## 🤝 Contributing

This project is open source and contributions are welcome.

**Ways to contribute:**
- Report bugs by [opening an issue](https://github.com/troubleman96/camelDownloader-/issues)
- Suggest new features via issues
- Submit a Pull Request with improvements

**To contribute code:**

```bash
# Fork the repo on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/camelDownloader-.git
cd camelDownloader-

# Install in editable mode so your changes take effect immediately
pip install -e .

# Create a branch for your change
git checkout -b my-feature

# Make your changes, then commit and push
git add .
git commit -m "describe your change"
git push origin my-feature
```

Then open a Pull Request on GitHub.

---

## 📜 License

Distributed under the **MIT License** — free to use, modify, and distribute for any purpose.
