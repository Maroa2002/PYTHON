import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "html.parser")
movies = soup.find_all(name="h3")

number_list = []
name_list = []

for movie in movies:
    number = movie.getText().split(")")[0]
    number_list.append(number)
    name = movie.getText().split()[1]
    name_list.append(name)


print(number_list)
print(name_list)

with open("movies.txt", mode="w") as movies:
    pass


