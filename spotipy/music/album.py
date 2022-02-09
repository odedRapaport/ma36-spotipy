from music.song import Song


class Album:
    def __init__(self, id: str, name: str, songs: list):
        self.id = id
        self.name = name
        self.songs = songs

    def add_song(self, song: Song):
        self.songs.append(song)
