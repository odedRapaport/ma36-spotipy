from exceptions.user_exceptions import *
from extract.reader import config_read


class User:
    def __init__(self, username, is_premium):
        self.username = username
        self.is_premium = is_premium
        self.playlists = {}

    def add_playlist(self, playlist_name: str, songs_list: list):
        user_config = config_read().get('users')
        if not self.is_premium and (len(self.playlists) >= user_config.get("not_premium_playlists_restrict") or len(
                songs_list) > user_config.get("not_premium_songs_per_playlist_restrict")):
            NotPremiumUserRestrictedException
        else:
            if playlist_name in self.playlists.keys():
                raise PlaylistIsAlreadyExistException
            else:
                self.playlists[playlist_name] = songs_list
