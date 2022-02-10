from users.user import User
from search.search_methods import get_all_artists
from music.music_manager import MusicManager
from extract.extract_all_songs import extract_all_songs
from exceptions.user_exceptions import ArtistNotFoundException


all_artists = get_all_artists(False, extract_all_songs(MusicManager()))


class ArtistUser(User):
    def __init__(self, username: str):
        if username in all_artists:
            super(ArtistUser, self).__init__(username, True)
        else:
            raise ArtistNotFoundException

    def get_albums(self):
        for artist in all_artists:
            if artist.name == self.username:
                return artist.albums
