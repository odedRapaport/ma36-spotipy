from music.album import Album
from music.song import Song


class Artist:
    def __init__(self, id: str, name: str, albums: list):
        self.id = id
        self.name = name
        self.albums = albums

    def add_album(self, album: Album):
        self.albums.append(album)

    def add_song(self, album_id, song: Song):
        for album in self.albums:
            if album.id == album_id:
                album.add_song(song)

    def contains_album(self, id: str):
        for album in self.albums:
            if album.id == id:
                return True
        return False
