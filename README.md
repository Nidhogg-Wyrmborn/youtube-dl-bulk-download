# youtube-dl bulk download 

IMPORTANT: if you download a video with subtitles, KEEP THE .ASS FILES, if you delete them the video won't have subtitles anymore
i will find a way to fix this but for now DO NOT DELETE THEM

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

# something to note about crunchyroll and possibly other sites

if you try to download a video that requires premium or equivalent it will throw an error and be unable to continue

# Distributions of this script

if you want to have a particular feature added to this script create an issue and i will add the feature as soon as i am able to
this is the same with EXEs if you want to have an executable create an issue and i will do my best