from album import Album


class Artist:
    def __init__(self, id: str, name: str, albums: list(Album)):
        self.id = id
        self.name = name
        self.albums = albums
