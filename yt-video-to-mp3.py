# %%
# Download Youtube video as webm file
from pytube import YouTube
import subprocess
import os
from pathlib import Path


def convert_video_to_audio_ffmpeg(video_file, output_ext="mp3"):
    """Converts video to audio directly using `ffmpeg` command
    with the help of subprocess module"""
    filename, ext = os.path.splitext(video_file)
    subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)


with open('yt-video-links.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
        yt = YouTube(line)
        print(yt.title)
        stream = yt.streams.get_by_itag(251)
        stream.download()
        print("Download completed..")

# %%
# Convert webm files to mp3
for file in os.listdir("."):
    if file.endswith(".webm"):
        print(file)
        convert_video_to_audio_ffmpeg(file)
        print("Conversion to mp3 completed..")
