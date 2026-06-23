# camelDownloader — Windows Setup

## Requirements
- Windows 10 (updated) or Windows 11
- Python 3.8 or higher
- FFmpeg
- Internet connection

---

## Step 1 — Install Python and FFmpeg

Open **Command Prompt as Administrator** and run:

```powershell
winget install Python.Python.3 -e
winget install Gyan.FFmpeg -e
```

`winget` comes pre-installed on Windows 10 (updated) and Windows 11. Restart your terminal after this step.

**No winget?** Install manually:
- Python: https://python.org/downloads — check **"Add Python to PATH"** during install
- FFmpeg: https://ffmpeg.org/download.html → extract zip → add the `bin` folder to your system PATH

---

## Step 2 — Install camelDownloader

Open **Command Prompt** (regular, not admin) and run:

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
C:\Users\YourName\Downloads\camelDownloader\
```

---

## Torrent / Magnet Support (optional)

```bash
pip install libtorrent
```

If pip install fails, try the wheel from https://github.com/arvidn/libtorrent/releases.

---

## Update to Latest Version

```bash
pip install -U camelDownloader
```

---

## Troubleshooting

**`camel` is not recognized**
Python's Scripts folder is not on PATH. Add it:
1. Search "Environment Variables" in Start
2. Edit the `Path` system variable
3. Add: `C:\Users\YourName\AppData\Local\Programs\Python\Python3xx\Scripts\`

**`ffmpeg` is not recognized**
FFmpeg's `bin` folder is not on PATH. Add `C:\ffmpeg\bin` to your system PATH (same steps as above).

**Download fails / 403 error**
```bash
pip install -U yt-dlp
```

**No audio in downloaded video**
FFmpeg is not installed or not on PATH. Reinstall using winget:
```bash
winget install Gyan.FFmpeg -e
```
