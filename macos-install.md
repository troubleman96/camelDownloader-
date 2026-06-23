# camelDownloader — macOS Setup

## Requirements
- macOS 11 (Big Sur) or higher
- Homebrew (recommended)
- Python 3.8 or higher
- FFmpeg

---

## Step 1 — Install Homebrew (skip if already installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Homebrew is a free package manager for macOS. It makes installing Python and FFmpeg simple.

---

## Step 2 — Install Python and FFmpeg

```bash
brew install python ffmpeg
```

---

## Step 3 — Install camelDownloader

```bash
pip3 install camelDownloader
```

---

## Step 4 — Run it

```bash
camel
```

Paste any link at the prompt and press Enter. It auto-detects the type:

- **YouTube / TikTok / Twitter / Vimeo / 1000+ sites** → shows quality menu (1–7)
- **Direct file link** (.zip, .mp4, .pdf, etc.) → downloads immediately
- **Magnet link or .torrent** → torrent download (requires libtorrent — see below)

---

## Quality Options (media links)

| # | Quality | Good For |
|---|---------|----------|
| 1 | 360p SD | Slow internet |
| 2 | 720p HD | Best balance (recommended) |
| 3 | 1080p Full HD | High quality |
| 4 | 1440p 2K | Very high quality |
| 5 | 2160p 4K | Maximum (large file) |
| 6 | Best Auto | Let it decide |
| 7 | Audio MP3 | Music / podcasts only |

---

## Where Downloads Go

```
~/Downloads/camelDownloader/
```

---

## Torrent / Magnet Support (optional)

```bash
pip3 install libtorrent
```

---

## Update to Latest Version

```bash
pip3 install -U camelDownloader
```

---

## Troubleshooting

**`camel: command not found`**

Add pip's bin directory to PATH:

```bash
echo 'export PATH="$HOME/Library/Python/3.x/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

Replace `3.x` with your Python version (e.g. `3.12`).

**`ffmpeg not installed` error**

```bash
brew install ffmpeg
```

**Download fails / 403 error**

```bash
pip3 install -U yt-dlp
```

**`libtorrent not installed` when using magnets**

```bash
pip3 install libtorrent
```

**No audio in downloaded video**

FFmpeg is missing or not on PATH. Reinstall:

```bash
brew install ffmpeg
```
