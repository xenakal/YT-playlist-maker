"""
Script to create an untitled youtube playlist (without a linked account) from a file. Each line of the file must contain the search terms associated to a video. 
The file must be called "songs.txt" and be located in the same folder as this script. 
"""

# base of the url to create a playlist
playlist_url = "https://www.youtube.com/watch_videos?video_ids="

# handle input arguments
import argparse
parser = argparse.ArgumentParser(description='Make a youtube playlist containing a video for each line of the input file')
## path 
parser.add_argument('-p', '--path', default="./songs.txt", help="path to file containing the songs")
## open browser 
parser.add_argument('-b', '--use_browser', default=0, help="set to 1 to open playlist in default browser")
args = parser.parse_args()

# get names/artists of songs 
names_file = open(args.path, 'r')
songs_name = names_file.readlines()
names_file.close()
vids_number = len([song for song in songs_name if not song[0]=="#"])
tenth = vids_number/10

# search yt for video and append its ID to the playlist url
import sys
from youtubesearchpython import searchYoutube
print(f"Creating a playlist from the file %s" % args.path)
number_completed = 0
sys.stdout.write("[%s]" % (" " * 10))
sys.stdout.flush()
sys.stdout.write("\b" * 11)  # return to start of line, after '['

for song_name in songs_name:
    if not song_name[0] == "#":
        vid_id = searchYoutube(song_name, offset=1, mode="dict", max_results=1).result()["search_result"][0]["id"]
        playlist_url += vid_id + ","
        number_completed += 1
        while number_completed > tenth:
           number_completed -= tenth
           sys.stdout.write("-")
           sys.stdout.flush()

sys.stdout.write("-\n")
sys.stdout.flush()
playlist_url = playlist_url[:-1]
 
# output resulting url 
print(f"Playlist URL: \n \t %s" % playlist_url)

# open the playlist in default browser
if args.use_browser=="1" or args.use_browser=="T" or args.use_browser=="True" or args.use_browser=="t" or args.use_browser=="true":
    import webbrowser
    webbrowser.open(playlist_url)

