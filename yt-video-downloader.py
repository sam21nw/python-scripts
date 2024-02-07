# %%
# Download Youtube video as mp4 file
from pytube import YouTube
from pytube import Playlist
# import subprocess
# import os
# from pathlib import Path


# def convert_video_to_audio_ffmpeg(video_file, output_ext="mp3"):
#     """Converts video to audio directly using `ffmpeg` command
#     with the help of subprocess module"""
#     filename, ext = os.path.splitext(video_file)
#     subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"],
#                     stdout=subprocess.DEVNULL,
#                     stderr=subprocess.STDOUT)

# p = Playlist(
# 'https://www.youtube.com/watch?v=qZ6TJc5bSKU&list=PLp_fYzTMUTz4a1kmkWqxBgB63t2MNfI7f')

# for url in p.video_urls[1:5]:
#     print(url)

# for video in p.videos[-1:]:
#     print(f'Downloading: {video.title}')
#     video.streams.get_by_itag(22).download()

# Download one video from a playlist
with open('yt-video-links.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
        yt = YouTube(line)
        print(yt.title)
        stream = yt.streams.get_by_itag(22)
        stream.download()

# %%
# Convert webm files to mp3
# for file in os.listdir("."):
#     if file.endswith(".webm"):
#         print(file)
#         convert_video_to_audio_ffmpeg(file)
