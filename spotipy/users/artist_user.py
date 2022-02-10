from users.user import User
from search.search_methods import get_all_artists
from music.music_manager import MusicManager
from extract.extract_all_songs import extract_all_songs
from exceptions.user_exceptions import ArtistNotFoundException


class ArtistUser(User):
    def __init__(self, username: str):
        self.is_premium = True
        if username in get_all_artists(self, extract_all_songs(MusicManager())):
            super(ArtistUser, self).__init__(username, True)
        else:
            raise ArtistNotFoundException
