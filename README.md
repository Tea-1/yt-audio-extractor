# yt-audio-extractor
Takes either a yt url or search and downloads a video or audio file

# Installation Instructions
YOU MUST HAVE FFMPEG INSTALLED FOR THIS TO RUN
requirements: 
FFmpeg
Python3+

To install FFmpeg:

go to this site: 
  https://ffmpeg.org/download.html
  
click on gyan.dev
scroll down to "Releases" 
download ffmpeg-release-full.7z or ffmpeg-release-essentials.zip
if you download the 7z file, make sure you have 7zip installed: https://www.7-zip.org/

go under bin files and copy all the .exe files
navigate to your C: drive and make a file called ffmpeg
open up windows search and type in path, press enter
click "Environment Variables"
under "User variables" find "path", select it and press 'edit'
click "new", and enter in the path to the folder you just made (should be C:\ffmpeg)
click ok
double check it's working by opening up cmd and typing ffmpeg, some stuff should show up

To run the program, double click the .py file
Either enter a youtube url or search for a video
Enter what file format, m4a is much higher quality and thus is the default (press enter for default)
Enter bitrate, default 192 is fine (press enter for default)

Your audio file will be saved to the local directory of the python script.
