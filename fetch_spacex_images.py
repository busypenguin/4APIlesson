import requests
import argparse
from utils import download_image
from pathlib import Path


def fetch_spacex_last_launch():
    payload = {}
    response = requests.get('https://api.spacexdata.com/v5/launches/{}'.format(launch_id))
    response.raise_for_status()
    launches = response.json()
    for launch in launches:
        picture = launch['links']['patch']['large']
        download_image(picture, 'images/', payload)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Программа скачивает картинки с сайта spacex'
    )
    parser.add_argument("--launch_id", help="ID запуска", default='5eb87d42ffd86e000604b384')
    args = parser.parse_args()
    launch_id = args.launch_id
    Path("images").mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch()
