from exceptions.user_exceptions import *
from extract.reader import JsonReader
import logging


class User:
    def __init__(self, username, is_premium):
        self.username = username
        self.is_premium = is_premium
        self.playlists = {}
        logging.basicConfig(filename=JsonReader("configuration.json").read().get('logging').get("logs_file_name"),
                            format='%(asctime)s - %(levelname)s - %(message)s', filemode='a', level=logging.DEBUG)
        logging.debug(f"create new user {username}")

    def add_playlist(self, playlist_name: str, songs_list: list):
        user_config = JsonReader("configuration.json").read().get('users')
        if not self.is_premium and (len(self.playlists) >= user_config.get("not_premium_playlists_restrict") or len(songs_list) > user_config.get("not_premium_songs_per_playlist_restrict")):
            NotPremiumUserRestrictedException
        else:
            if playlist_name in self.playlists.keys():
                raise PlaylistIsAlreadyExistException
            else:
                self.playlists[playlist_name] = songs_list
