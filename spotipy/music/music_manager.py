from music.artist import Artist
from music.album import Album
from music.song import Song


class MusicManager:
    def __init__(self):
        self.artists = []

    def add_track(self, track: dict):
        track = track.get('track')
        song = Song(track.get('id'), track.get('name'), track.get('popularity'))
        album = Album(track.get('album').get('id'), track.get('album').get('name'), [song])
        for artist in track.get('artists'):
            if not self.contains_artist(artist.get('id')):
                self.artists.append(Artist(artist.get('id'), artist.get('name'), [album]))
            else:
                self.add_track_to_artist(artist.get('id'), album)

    def contains_artist(self, id: str):
        for artist in self.artists:
            if artist.id == id:
                return True
        return False

    def add_track_to_artist(self, artist_id: str, album: Album):
        for artist in self.artists:
            if artist.id == artist_id:
                if artist.contains_album(album.id):
                    artist.add_song(album.id, album.songs[0])
                else:
                    artist.add_album(album)
