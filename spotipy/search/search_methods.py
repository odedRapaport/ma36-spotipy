from music.music_manager import MusicManager


def get_all_artists(music_manager: MusicManager):
    return [artist.name for artist in music_manager.artists]


def get_albums_by_artist(music_manager: MusicManager, artist_id: str):
    for artist in music_manager.artists:
        if artist.id == artist_id:
            return [album.name for album in artist.albums]
