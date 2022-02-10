from consolemenu import *
from consolemenu.items import *

from extract.extract_all_songs import extract_all_songs
from users.user import User
from users.users_manager import login
from search.search_methods import *
from exceptions.user_exceptions import UserNotFoundException


def run():
    login_to_spotipy()


def login_to_spotipy():
    username = str(input("enter your username:"))
    try:
        user = login(username)
        console_menu(user)
    except UserNotFoundException:
        print("username does not exist, please try again")
        login_to_spotipy()


def console_menu(user: User):
    music_manager = extract_all_songs(MusicManager())
    menu = ConsoleMenu("spotipy menu")
    menu.append_item(
        FunctionItem(text="print_all_artists", function=print_all_artists, args=[not user.is_premium, music_manager]))
    menu.append_item(FunctionItem(text="print_albums_by_artist", function=print_albums_by_artist,
                                  args=[not user.is_premium, music_manager]))
    menu.append_item(FunctionItem(text="print_top_songs_by_artist", function=print_top_songs_by_artist,
                                  args=[not user.is_premium, music_manager]))
    menu.append_item(FunctionItem(text="print_songs_by_album", function=print_songs_by_album,
                                  args=[not user.is_premium, music_manager]))
    menu.show()


def print_all_artists(is_restrict: bool, music_manager: MusicManager):
    print(get_all_artists(is_restrict, music_manager))


def print_albums_by_artist(is_restrict: bool, music_manager: MusicManager):
    artist_id = str(input("enter artist id:"))
    print(get_albums_by_artist(is_restrict, music_manager, artist_id))


def print_top_songs_by_artist(is_restrict: bool, music_manager: MusicManager):
    artist_id = str(input("enter artist id:"))
    print(get_top_songs_by_artist(is_restrict, music_manager, artist_id))


def print_songs_by_album(is_restrict: bool, music_manager: MusicManager):
    album_id = str(input("enter album id:"))
    print(get_songs_by_album(is_restrict, music_manager, album_id))
