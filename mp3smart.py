import yt_dlp

# Works for both single video and playlist
url = "https://youtu.be/HIVx-Nxm1No?si=1VXVEf4kepvsQA9C"

# Detect playlist vs single video
is_playlist = "list=" in url

ydl_opts = {
    'format': 'bestaudio/best',
    'ffmpeg_location': r"C:\ffmpeg\bin",
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    # Use playlist numbering if it's a playlist, otherwise just title
    'outtmpl': '%(playlist_index)s - %(title)s.%(ext)s' if is_playlist else '%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
