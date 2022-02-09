from users.user import User
from music.music_manager import MusicManager


def get_all_artists(music_manager: MusicManager):
    return [artist.name for artist in music_manager.artists]

