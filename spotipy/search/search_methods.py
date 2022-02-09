from music.music_manager import MusicManager
from music.song import Song
from exceptions.search_exceptions import ArtistNotFoundException, AlbumNotFoundException
from extract.reader import JsonReader


def get_all_artists(music_manager: MusicManager):
    return [artist.name for artist in music_manager.artists]


def get_albums_by_artist(music_manager: MusicManager, artist_id: str):
    for artist in music_manager.artists:
        if artist.id == artist_id:
            return [album.name for album in artist.albums]
    raise ArtistNotFoundException


def get_top_songs_by_artist(music_manager: MusicManager, artist_id: str):
    restricted_top_songs_number = JsonReader("configuration.json").read().get('search').get('top_songs_to_search_number')
    for artist in music_manager.artists:
        if artist.id == artist_id:
            all_songs = artist.get_all_songs()
            all_songs.sort(key=compare_by_popularity)
            if len(all_songs) >= restricted_top_songs_number:
                return all_songs
            else:
                return [song.name for song in all_songs[:restricted_top_songs_number]]
    raise ArtistNotFoundException


def get_songs_by_album(music_manager: MusicManager, album_id: str):
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
