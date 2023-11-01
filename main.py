import requests
from pathlib import Path
from urllib.parse import urlsplit
import os
import datetime
from environs import Env


env = Env()
env.read_env()


def download_images(url, folder_path):
    filename = url.split("/")[-1]
    response = requests.get(url)
    response.raise_for_status()

    with open(folder_path+filename, "wb") as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    response = requests.get('https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384')
    data_json = response.json()["links"]["flickr"]["original"]
    for pic in data_json:
        download_images(pic, 'images/')


def find_format(url):
    path_of_url = urlsplit(url)
    a = os.path.split(path_of_url[2])
    b = os.path.splitext(a[1])
    c = b[1]
    return c


def fetch_nasa_last_launch():
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}&count=30'.format(nasa_api_key=nasa_api_key))
    data_json = response.json()
    for el in data_json:
        if find_format(el["url"]) == ".jpg":
            download_images(el['url'], 'images/')


def fetch_nasa_Earth_launch():
    response = requests.get('https://api.nasa.gov/EPIC/api/natural?api_key={nasa_api_key}'.format(nasa_api_key=nasa_api_key))
    data_json = response.json()
    epic_example = 'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png?api_key={nasa_api_key}'
    for el, data in enumerate(data_json):
        date = data_json[el]['date']
        date = datetime.datetime.fromisoformat(date)
        date = date.strftime("%Y/%m/%d")
        url = epic_example.format(date=date, image=data_json[el]['image'], nasa_api_key=nasa_api_key)
        download_images(url, 'images/')


if __name__ == '__main__':
    nasa_api_key = env.str('NASA_API_KEY')
    Path("images").mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch()
    fetch_nasa_last_launch()
    fetch_nasa_Earth_launch()
