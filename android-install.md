# camelDownloader — Android (Termux) Setup

## Requirements
- Android 7.0 or higher
- Termux (from F-Droid — NOT the Play Store version)
- ~100 MB free storage

---

## Step 1 — Install Termux

Download from **F-Droid** (the Play Store version is outdated and broken):

👉 https://f-droid.org/en/packages/com.termux/

Install the APK. Allow "Install from unknown sources" when prompted.

---

## Step 2 — Install everything (one command)

Open Termux and paste this:

```bash
pkg update -y && pkg upgrade -y && pkg install python ffmpeg openssl aria2 -y && pip install camelDownloader
```

This installs Python, FFmpeg, OpenSSL, aria2 (for torrent/magnet support), and camelDownloader in one go.

---


## Step 3 — Grant storage access (one time only)

```bash
termux-setup-storage
```

Tap **Allow** when Android asks for permission. This makes your downloads appear in the Android **Files app → Downloads** folder.

---

## Step 4 — Run it

```bash
camel
```

Paste any link at the prompt and press Enter. It auto-detects the type:

- **YouTube / TikTok / Twitter / Instagram / Vimeo** → shows quality menu (1–7)
- **Direct file link** → downloads immediately
- **Magnet links & .torrent files** → downloads via aria2c (installed in Step 2)

---

## Quality Options (media links)

| # | Quality | Good For |
|---|---------|----------|
| 1 | 360p SD | Slow data, quick preview |
| 2 | 720p HD | Best balance (recommended) |
| 3 | 1080p Full HD | High quality |
| 4 | 1440p 2K | Very high quality |
| 5 | 2160p 4K | Maximum (large file) |
| 6 | Best Auto | Let it decide |
| 7 | Audio MP3 | Music / podcasts only |

---

## Where Downloads Go

After running `termux-setup-storage`:

```
~/storage/downloads/camelDownloader/
```

Open the **Files** app on Android → **Downloads → camelDownloader** to find your files.

If `termux-setup-storage` failed, files go to:

```
~/downloads/camelDownloader/
```

---

## Update to Latest Version

```bash
pip install -U camelDownloader
```

---

## Troubleshooting

**`camel: command not found`**
Close and reopen Termux, then try again.

**`termux-setup-storage` popup never appears**
Go to Android Settings → Apps → Termux → Permissions → Files and Media → Allow.

**Download fails / 403 error**
Update yt-dlp:
```bash
pip install -U yt-dlp
```

**No audio in downloaded video**
FFmpeg is missing or broken. Reinstall:
```bash
pkg install ffmpeg
```
