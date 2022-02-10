from extract.extract_all_songs import extract_all_songs
from search.search_methods import *
from users.users_manager import login


music_manager = MusicManager()
music_manager = extract_all_songs(music_manager)
user = login("oded")
artist_user = login("Joji")
print(get_all_artists(not artist_user.is_premium, music_manager))
print(get_albums_by_artist(not artist_user.is_premium, music_manager, '3MZsBdqDrRTJihTHQrO6Dq'))
print(get_top_songs_by_artist(not user.is_premium, music_manager, '3MZsBdqDrRTJihTHQrO6Dq'))
print(get_songs_by_album(not artist_user.is_premium, music_manager, '0d2EBNZtasKFZOtbhBibjD'))
