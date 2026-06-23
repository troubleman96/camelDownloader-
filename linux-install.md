# camelDownloader — Linux (Ubuntu / Debian) Setup

## Requirements
- Ubuntu 20.04+ or any Debian-based distro
- Python 3.8 or higher
- FFmpeg
- pip

---

## Step 1 — Install prerequisites

```bash
sudo apt update
sudo apt install python3 python3-pip ffmpeg -y
```

**Optional — torrent & magnet link support:**

```bash
sudo apt install python3-libtorrent -y
```

---

## Step 2 — Install camelDownloader

```bash
pip install camelDownloader
```

---

## Step 3 — Run it

```bash
camel
```

Paste any link at the prompt and press Enter. It auto-detects the type:

- **YouTube / TikTok / Twitter / Vimeo / 1000+ sites** → shows quality menu (1–7)
- **Direct file link** (.zip, .mp4, .pdf, etc.) → downloads immediately
- **Magnet link or .torrent** → torrent download (requires python3-libtorrent)

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

## Update to Latest Version

```bash
pip install -U camelDownloader
```

---

## Troubleshooting

**`camel: command not found`**

pip installs scripts to `~/.local/bin` which may not be on PATH. Fix it:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

**`ffmpeg not installed` error**

```bash
sudo apt install ffmpeg
```

**Download fails / 403 error**

```bash
pip install -U yt-dlp
```

**`libtorrent not installed` when using magnets**

```bash
sudo apt install python3-libtorrent
```

**No audio in downloaded video**

FFmpeg is missing. Install it:

```bash
sudo apt install ffmpeg
```
