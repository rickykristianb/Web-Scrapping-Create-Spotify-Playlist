from spotipy.oauth2 import SpotifyOAuth
import spotipy
import os
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_ID = os.getenv('SPOTIFY_ID')
SPOTIFY_SECRET = os.getenv('SPOTIFY_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')


class Spotify():

    def __init__(self):
        self.scope_modify = "playlist-modify-private"

    def authorization(self):
        spotify = SpotifyOAuth(
            client_id=SPOTIFY_ID,
            client_secret=SPOTIFY_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=self.scope_modify
        )
        spotify.get_access_token()
        auth_code = spotify.get_authorization_code()
        return auth_code

    def create_playlist(self, charts: list, year, date):
        sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=SPOTIFY_ID,
                client_secret=SPOTIFY_SECRET,
                redirect_uri=REDIRECT_URI,
                scope=self.scope_modify)
        )
        playlist = sp.user_playlist_create(
            user=sp.current_user()["id"],
            name=f"Billboard Top 100 on {date}",
            public=False,
            collaborative=False,
            description="TESTING DESCRIPTION"
        )
        position = 1
        songs_uri = []
        for track in charts:
            print(position, track, year)
            try:
                song = sp.search(q=f"track:{track} year:{year}", type="track")
                song_uri = str(song["tracks"]["items"][0]["uri"]).split(":")[2]
                songs_uri.append(song_uri)
                position += 1
            except IndexError:
                print(IndexError)
        print(songs_uri)
        sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uri)
