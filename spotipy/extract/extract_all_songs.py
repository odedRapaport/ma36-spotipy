from music.music_manager import MusicManager
from extract.reader import JsonReader
import json
from os import listdir


def extract_all_songs(music_manager: MusicManager):
    songs_path = ""
    with open("configuration.json") as config_file:
        songs_path = json.load(config_file).get('extract_music').get('path')
    tracks_json_format = [JsonReader(songs_path+"\\"+file.title()).read() for file in listdir(songs_path)]
    for track in tracks_json_format:
        music_manager.add_track(track)
    return music_manager
