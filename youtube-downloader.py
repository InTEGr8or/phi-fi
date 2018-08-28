from pytube import YouTube
from pytube import Playlist
pl = Playlist('https://www.youtube.com/playlist?list=PLYL1oPw_Wlb_7o_Y2KIIcOWmYqzaQPh4a')
pl.download_all("./youtube")
# pl.populate_video_urls()
# for video in pl.video_urls:

#     print(video.title().lower())
