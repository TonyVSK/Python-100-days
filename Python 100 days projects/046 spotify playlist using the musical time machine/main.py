from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from keys import clientId, clientSecret
import requests
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

#========================================================================================================================
# Spotipy configurations

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id = clientId,
        client_secret = clientSecret,
        redirect_uri="http://example.com",
        cache_path="token.txt",
        username="Walskiko"

    )
)
user_id = sp.current_user()["id"]


#========================================================================================================================
# Scraping html configurations
URL = "https://www.billboard.com/charts/hot-100/"
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

year = date[0]+date[1]+date[2]+date[3]

response = requests.get(URL + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names]

print(song_names)


#========================================================================================================================
# using spotipy to search artist songs by scraping html list of musics

spotify_uris=[]

for music in song_names:
    spotify_search = sp.search(q=f"track:{music}")
    try:
        song_uri = spotify_search['tracks']['items'][0]['uri']
        spotify_uris.append(song_uri)
    except IndexError:
        print(f'No song {music}')
    else:
        pass


playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard Top Tracks", public=False, description=f"Tracks number 1 in {year}")

try:
    for i in range(0, len(spotify_uris), 100):
        sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist['id'], tracks=spotify_uris[i:i+100])
    print(f"All songs added to playlist {year} Billboard Top Tracks.")
except spotipy.exceptions.SpotifyException:
    print(f"An error occurred: {spotipy.exceptions.SpotifyException}")
