from extract.extract_all_songs import extract_all_songs
from music.music_manager import MusicManager
from search.search_methods import get_all_artists
from extract.reader import JsonReader, config_read
from users.artist_user import ArtistUser
from users.user import User
from exceptions.user_exceptions import ArtistNotFoundException, UserNotFoundException
import logging

all_artists = get_all_artists(False, extract_all_songs(MusicManager()))
users_file_path = config_read().get('users').get("users_file_path")


def login(username: str):
    users = JsonReader(users_file_path).read()
    for user in users.values():
        if user.get('username') == username:
            logging.basicConfig(filename=config_read().get('logging').get("logs_file_name"),
                                format='%(asctime)s - %(levelname)s - %(message)s', filemode='a', level=logging.DEBUG)
            try:
                user = ArtistUser(user.get('username'))
                logging.info(f"artist {username} made login")
                return user
            except ArtistNotFoundException:
                user = User(user.get('username'), user.get('is_premium'))
                logging.info(f"{username} made login")
                return user
    raise UserNotFoundException
