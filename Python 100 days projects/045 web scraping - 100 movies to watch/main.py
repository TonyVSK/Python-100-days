import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)
yc_web_page = response.text

soup= BeautifulSoup(yc_web_page, "html.parser")

linking = soup.find_all(name="h3", class_="title")
print(linking)

movie_titles = [movie.getText() for movie in linking]
print(movie_titles)

with open ("./movies.txt", "w") as file:
    for item in movie_titles:
        file.write(f"{item}\n")
