from exceptions.user_exceptions import PlaylistIsAlreadyExistException


class User:
    def __init__(self, username):
        self.username = username
        self.playlists = {}

    def add_playlist(self, playlist_name: str, songs_list: list):
        if playlist_name in self.playlists.keys():
            raise PlaylistIsAlreadyExistException
        else:
            self.playlists[playlist_name] = songs_list
