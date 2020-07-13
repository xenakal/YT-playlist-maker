# YT-playlist-maker

Create a Youtube playlist (no account needed) from a file containing the search terms for each video of the playlist. 

## How to use 

A file such as [songs.txt](https://github.com/xenakal/YT-playlist-maker/blob/master/songs.txt) must be created. Each line of the file will be used as a search term once (in youtube). The first result of each search is added to the playlist. Run: 

>```python3 create_yt_playlist.py [path]```, 

where [path] is the optional path to the file containing the songs. If unspecified, the script will use a file called *songs.txt* in the current directory.  


## Requirements

Requires [youtube-search](https://github.com/joetats/youtube_search) (```pip install youtube-search```). 

