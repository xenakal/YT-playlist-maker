"""
Script to create an untitled youtube playlist (without a linked account) from a file. Each line of the file must contain the search terms associated to a video. 
The file must be called "songs.txt" and be located in the same folder as this script. 
"""

# base of the url to create a playlist
playlist_url = "https://www.youtube.com/watch_videos?video_ids="

# get names/artists of songs 
filepath = "./songs.txt"
names_file = open(filepath, 'r')
songs_name = names_file.readlines()
names_file.close()

# search yt for video and append its ID to the playlist url
from youtubesearchpython import searchYoutube
for song_name in songs_name:
    vid_id = searchYoutube(song_name, offset=1, mode="dict", max_results=1).result()["search_result"][0]["id"]
    playlist_url += vid_id + ","
playlist_url = playlist_url[:-1]
 
# open the playlist in default browser
import webbrowser
webbrowser.open(playlist_url)


