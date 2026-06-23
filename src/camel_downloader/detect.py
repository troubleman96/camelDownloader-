from urllib.parse import urlparse

MEDIA_HOSTS = [
    "youtube.com", "youtu.be", "twitter.com", "x.com", "tiktok.com",
    "instagram.com", "facebook.com", "vimeo.com", "dailymotion.com",
    "soundcloud.com", "twitch.tv", "reddit.com", "bilibili.com",
]


def detect_link_type(url: str) -> str:
    u = url.strip()
    if u.startswith("magnet:"):
        return "torrent_magnet"
    if u.endswith(".torrent"):
        return "torrent_file"
    host = urlparse(u).hostname or ""
    if any(h in host for h in MEDIA_HOSTS):
        return "media"
    return "http"
