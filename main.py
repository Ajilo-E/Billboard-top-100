import requests

from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"
date = input("What year would you like to travel to in YYYY-MM-DD:")
response = requests.get(URL + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all(name='h3', class_="a-no-trucate")
song_names = [song.getText().strip("\t\n") for song in song_names_spans]
print(song_names)

song = song_names[::-1]
with open("songs.txt", mode="w")as file:
    for playlist in song:
        file.write(f"{playlist}\n")
