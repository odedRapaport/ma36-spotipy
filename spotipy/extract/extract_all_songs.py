from music.music_manager import MusicManager
from extract.reader import JsonReader
from os import listdir


def extract_all_songs(music_manager: MusicManager):
    songs_path = JsonReader("configuration.json").read().get('extract_music').get('path')
    tracks_json_format = [JsonReader(songs_path+"\\"+file.title()).read() for file in listdir(songs_path)]
    for track in tracks_json_format:
        music_manager.add_track(track)
    return music_manager
