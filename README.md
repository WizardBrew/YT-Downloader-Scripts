# YT-Downloader-Scripts
Video - Audio Playlists all 


Download a complete build of FFmpeg

Go to the official FFmpeg site or a trusted distributor (like gyan.dev or [BtbN builds on GitHub]).

Choose a full release build, not a “minimal” one, since minimal builds often exclude filters.

Extract properly

Unzip the archive into a folder (e.g., C:\ffmpeg).

Inside, you should see bin, doc, and other directories. The bin folder must contain ffmpeg.exe and all the DLLs.

Update your PATH (optional but recommended)

Add C:\ffmpeg\bin to your system PATH so you can run ffmpeg from any command prompt.

Check for missing DLLs

If avfilter-11.dll is missing in the bin folder, your build is incomplete. Re-download a full build.

Never try to download random DLLs from the internet — they can be unsafe. Always get them bundled with the official FFmpeg build.
