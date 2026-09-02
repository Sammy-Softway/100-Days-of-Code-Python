import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
movies_website_html = response.text

soup = BeautifulSoup(movies_website_html, 'html.parser')
# print(soup.prettify())

target = soup.find(name='h3', class_='title')
# print(target.text)

all_movies = soup.find_all(name='h3', class_='title')
# movies_list = []
# for each_movie in all_movies:
#     movie_title = each_movie.get_text()
#     movies_list.append(movie_title)

# list and for loop simplified
movies_list = [movie.getText() for movie in all_movies]

with open('./movies.txt', 'w', encoding='utf-8') as file:
    #for movie in movie_list[::-1]: This creates a shallow copy of the list in reverse order. It uses more memory
    for each_movie in reversed(movies_list):
        file.write(each_movie + '\n')