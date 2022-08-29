# youtube-dl bulk download 

This is a custom script i put together to allow people to bulk download videos from any media

the main idea is that it runs through each video unless it fails in which case it tries again
if there is a keyboard interrupt (Control+C) then it will cancel the current download and/or quit

if there is an error with a video link, go to the youtube-dl git repo

https://github.com/ytdl-org/youtube-dl

FYI: if you are downloading from crunchyroll and the link is something like

https://beta.crunchyroll.com/...

change it to

https://crunchyroll.com/...

because crunchyroll beta seems to throw "unsupported link" errors

if you want to have this as an executable create and issue requesting as such and i will create a release with the executable as soon as i am able to