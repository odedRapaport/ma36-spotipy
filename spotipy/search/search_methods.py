from music.music_manager import MusicManager
from music.song import Song
from extract.reader import JsonReader


def get_all_artists(music_manager: MusicManager):
    return [artist.name for artist in music_manager.artists]


def get_albums_by_artist(music_manager: MusicManager, artist_id: str):
    for artist in music_manager.artists:
        if artist.id == artist_id:
            return [album.name for album in artist.albums]


def get_top_songs_by_artist(music_manager: MusicManager, artist_id: str):
    restricted_songs_number = JsonReader("configuration.json").read().get('extract_music').get('path')
    for artist in music_manager.artists:
        if artist.id == artist_id:
            all_songs = artist.get_all_songs().sort(key=compare_by_popularity)
            if len(all_songs) >= restricted_songs_number:
                return all_songs
            else:
                return all_songs[:restricted_songs_number]


def compare_by_popularity(song: Song):
    return song.popularity
