from bs4 import BeautifulSoup
import requests

URL = "https://www.billboard.com/charts/hot-100/"
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(URL + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names]

print(song_names)