from album import Album
from artist import Artist


class Song:
    def __init__(self, album: Album, artists: list(Artist), id: str, name: str, popularity: float):
        self.album = album
        self.artists = artists
        self.id = id
        self.name = name
        self.popularity = popularity
