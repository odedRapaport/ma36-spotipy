from music.music_manager import MusicManager
from music.song import Song
from exceptions.search_exceptions import ArtistNotFoundException, AlbumNotFoundException
from extract.reader import config_read
from collections.abc import Iterable


def decorator_by_user_type(func):
    def inner(*args):
        func_result = func(*args)
        if isinstance(func_result, Iterable):
            search_result_restrict = config_read().get('users').get(
                "not_premium_search_result_restrict")
            if (args[0]) and len(func_result) > search_result_restrict:
                return func_result[:search_result_restrict]
            else:
                return func_result
        else:
            return func_result

    return inner


@decorator_by_user_type
def get_all_artists(is_restrict: bool, music_manager: MusicManager):
    return [artist.name for artist in music_manager.artists]


@decorator_by_user_type
def get_albums_by_artist(is_restrict: bool, music_manager: MusicManager, artist_id: str):
    for artist in music_manager.artists:
        if artist.id == artist_id:
            return [album.name for album in artist.albums]
    raise ArtistNotFoundException


@decorator_by_user_type
def get_top_songs_by_artist(is_restrict: bool, music_manager: MusicManager, artist_id: str):
    restricted_top_songs_number = config_read().get('search').get(
        'top_songs_to_search_number')
    for artist in music_manager.artists:
        if artist.id == artist_id:
            all_songs = artist.get_all_songs()
            all_songs.sort(key=compare_by_popularity)
            if len(all_songs) >= restricted_top_songs_number:
                return all_songs
            else:
                return [song.name for song in all_songs[:restricted_top_songs_number]]
    raise ArtistNotFoundException


@decorator_by_user_type
def get_songs_by_album(is_restrict: bool, music_manager: MusicManager, album_id: str):
    songs = []
    for artist in music_manager.artists:
        for album in artist.albums:
            if album.id == album_id:
                for song in album.songs:
                    if song not in songs:
                        songs.append(song)
    if len(songs) > 0:
        return [song.name for song in songs]
    raise AlbumNotFoundException


def compare_by_popularity(song: Song):
    return song.popularity
