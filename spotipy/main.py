from extract.reader import JsonReader


song = JsonReader("C:\spotipy_songs\song_1bFSitBqVkOrZ5geYAHEKX.json").read()
print(song)