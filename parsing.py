import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
web_content = response.text
web_soup = BeautifulSoup(web_content, "html.parser")
movie_titles = web_soup.find_all(name="h3", class_="title")
movie_text_content = ""
for movie in movie_titles:
    movie_text_content = movie.get_text() + "\n" + movie_text_content
with open("movie.txt", "w", encoding="utf-8") as text_file:
    text_file.write(movie_text_content)

