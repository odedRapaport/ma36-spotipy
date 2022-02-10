from extract.extract_all_songs import extract_all_songs
from search.search_methods import *
from users.user import User
from users.artist_user import ArtistUser

music_manager = MusicManager()
music_manager = extract_all_songs(music_manager)
user = User("oded", False)
artist_user = ArtistUser("Joji")
print(get_all_artists(user, music_manager))
print(get_albums_by_artist(artist_user, music_manager, '3MZsBdqDrRTJihTHQrO6Dq'))
print(get_top_songs_by_artist(user, music_manager, '3MZsBdqDrRTJihTHQrO6Dq'))
print(get_songs_by_album(artist_user, music_manager, '0d2EBNZtasKFZOtbhBibjD'))
