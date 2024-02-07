# %%
# Pytube for youtube
from pytube import Search
from pytube import YouTube

video_path = input("Enter youtube video link: ")
yt = YouTube(video_path)
yt.title

# %%
# Filter streams by adaptive
# yt.streams.filter(adaptive=True)

# %%
# Filter streams by audio
# yt.streams.filter(only_audio=True)

# %%
# Download video or audio by itag
stream = yt.streams.get_by_itag(251)
stream.download()

# %%
# Search for videos
# s = Search('Python Tutorial')
# len(s.results)
# s.results
