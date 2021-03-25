import youtube_dl
import time
import urllib.request
import re

search = input("Search: ")
audio = str(input("Audio type (m4a, mp3, mp4, webm): "))
bitrate = str(input("Bitrate (default = 192): "))

if audio == '':
	audio = 'm4a'
if bitrate == '':
	bitrate = '192'

def search__(text):
	text = text.replace(' ', '+')
	html = urllib.request.urlopen(f"https://youtube.com/results?search_query={text}")
	videos = re.findall(r"watch\?v=(\S{11})", html.read().decode())
	vid_id = videos[0]
	url = f"https://www.youtube.com/watch?v={vid_id}"
	return url

if 'youtube'in search:
	url = search

else:
	url = search__(search)
	print(f"URL = {url}")

start_time = time.time()

opts = {
	'format': 'bestaudio/best',
	'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': audio,
        'preferredquality': bitrate,
    }],
}

with youtube_dl.YoutubeDL(opts) as ydl:
	info = ydl.extract_info(url, download=False) 
	video_title = info.get('title', None)
	ydl.download([url])

elapsed_time =  time.time() - start_time

print(f"Downloaded {video_title} in {elapsed_time} seconds.")
