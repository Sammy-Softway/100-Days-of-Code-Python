import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME")
SCOPE = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=SCOPE,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="https://example.com",
        show_dialog=True,
        cache_path="token.txt",
        username=SPOTIFY_USERNAME,
    )
)

user_id = sp.current_user()["id"]
# print(user_id)

user_date_choice = input("Which date do you want to travel to? (YYYY-MM-DD): ")

URL = f"https://appbrewery.github.io/bakeboard-hot-100/{user_date_choice}"

response = requests.get(URL)
web_html = response.text

soup = BeautifulSoup(web_html, 'html.parser')
# target = soup.find('h3', class_='chart-entry__title')
# print(target)

music_title_list = [song.getText() for song in soup.find_all('h3', class_='chart-entry__title')]
# print(music_title_list)

song_uris = []

year = user_date_choice.split("-")[0]

for song in music_title_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{user_date_choice} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)