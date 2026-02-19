import yt_dlp

url = "https://youtu.be/HIVx-Nxm1No?si=z6XXWmKTbEZUGFOy"

ydl_opts = {
    'format': 'bestaudio/best',             # get best audio stream
    'outtmpl': '%(playlist_index)s - %(title)s.%(ext)s',
    'ffmpeg_location': r"C:\ffmpeg\bin",    # path to ffmpeg
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',            # convert to mp3
        'preferredquality': '192',          # bitrate (kbps)
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
