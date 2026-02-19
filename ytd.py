import yt_dlp

url = "https://www.youtube.com/playlist?list=PL3SWvPT2o0y-sytMGUdlbJX07_EtVtx4w"

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'merge_output_format': 'mp4',
    'outtmpl': '%(playlist_index)s - %(title)s.%(ext)s',
    'ffmpeg_location': r"C:\ffmpeg\bin"   # <-- change to your actual ffmpeg path
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
