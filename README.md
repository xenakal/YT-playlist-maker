# YT-playlist-maker

Create a Youtube playlist (no account needed) from a file containing the search terms for each video of the playlist. 

## How to use 

A file such as [songs.txt](https://github.com/xenakal/YT-playlist-maker/blob/master/songs.txt) must be created. Each line of the file will be used as a search term once (in youtube). The first result of each search is added to the playlist. Usage: 

>```python3 create_yt_playlist.py [-h] [-p PATH] [-b USE_BROWSER]```, 

where [path] is the optional path to the file containing the songs, and USE_BROWSER opens the playlist in the default browser if set to 1. If unspecified, the script will use a file called *songs.txt* in the current directory, not opening the playlist.  


## Requirements

Requires [youtube-search](https://github.com/joetats/youtube_search) (```pip install youtube-search```). 

