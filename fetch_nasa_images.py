import requests
from additional_settings import download_images, find_format, nasa_api_key
from pathlib import Path


def fetch_nasa_last_launch():
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}&count=30'.format(nasa_api_key=nasa_api_key))
    data_json = response.json()
    for el in data_json:
        if find_format(el['url']) == '.jpg':
            download_images(el['url'], 'images/')


Path("images").mkdir(parents=True, exist_ok=True)
fetch_nasa_last_launch()
