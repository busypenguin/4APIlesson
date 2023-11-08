import requests
from utils import download_image, find_format
from pathlib import Path
from environs import Env


def fetch_nasa_last_launch():
    images_number = 30
    response = requests.get('https://api.nasa.gov/planetary/apod/api_key={nasa_api_key}&count={images_number}'.format(nasa_api_key=nasa_api_key, images_number=images_number))
    response.raise_for_status()
    launches = response.json()
    for launch in launches:
        if find_format(launch['url']) == '.jpg':
            download_image(launch['url'], 'images/')


if __name__ == '__main__':
    env = Env()
    env.read_env()
    nasa_api_key = env.str('NASA_API_KEY')
    Path("images").mkdir(parents=True, exist_ok=True)
    fetch_nasa_last_launch()
