# %%
import sys
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


# %%
while True:
    folder = input("Input a Folder: ")
    if Path(folder).is_dir() == False:
        print(f"Input a valid Folder")
    if Path(folder).is_dir() == True and not "".__eq__(folder):
        print(f"Input folder is '{folder}'")
        our_folder = Path(folder)
        break

# %%
for file in our_folder.iterdir():
    f = Path(file)
    print(f)

    convert_video_to_audio_ffmpeg(f)
