import requests
import datetime
from utils import download_image
from pathlib import Path
from environs import Env


def fetch_nasa_epic_launch(nasa_api_key):
    payload = {'api_key': nasa_api_key}
    response = requests.get('https://api.nasa.gov/EPIC/api/natural', params=payload)
    response.raise_for_status()
    earth_images = response.json()
    epic_example = 'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png'
    for image_number in earth_images:
        date = earth_images[image_number]['date']
        date = datetime.datetime.fromisoformat(date)
        date = date.strftime("%Y/%m/%d")
        url = epic_example.format(date=date, image=earth_images[image_number]['image'])
        download_image(url, 'images/', payload)


if __name__ == '__main__':
    env = Env()
    env.read_env()
    nasa_api_key = env.str('NASA_API_KEY')
    Path("images").mkdir(parents=True, exist_ok=True)
    fetch_nasa_epic_launch(nasa_api_key)
