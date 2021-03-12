import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.esquire.com/entertainment/movies/g226/best-movies-ever-0609/")
films_page = response.text

soup = BeautifulSoup(films_page,"html.parser")

titles = soup.find_all(name="span", class_="listicle-slide-hed-text")
esquire_greatest_movies = []

with open("100films.txt", "w") as films:
    films.write("Esquire Entertainments 100 Greatest Movies\n")
    rank = 0
    for movie in titles:
        rank += 1
        movie = movie.getText()
        esquire_greatest_movies.append(f"{rank}: {movie}")
        films.write(f"{rank}: {movie}\n")

    print(esquire_greatest_movies)

