import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
content = response.text

soup = BeautifulSoup(content, "html.parser")
movie_list = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
movies = movie_list[::-1]
with open("movie-list.txt",  "w", encoding="utf=8") as file:
    for movie in movies:
        file.write(f"{movie}\n")