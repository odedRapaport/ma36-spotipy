from music.music_manager import MusicManager
from extract.extract_all_songs import extract_all_songs


music_manager = MusicManager()
music_manager = extract_all_songs(music_manager)
print()