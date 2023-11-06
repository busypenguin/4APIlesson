import requests
import datetime
from additional_settings import download_image, nasa_api_key
from pathlib import Path


def fetch_nasa_epic_launch():
    payload = {'?': '/'}
    response = requests.get('https://api.nasa.gov/EPIC/api/natural?api_key={nasa_api_key}'.format(nasa_api_key=nasa_api_key), params=payload)
    response.raise_for_status()
    earth_images = response.json()
    epic_example = 'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png?api_key={nasa_api_key}'
    for image_number, data in enumerate(earth_images):
        date = earth_images[image_number]['date']
        date = datetime.datetime.fromisoformat(date)
        date = date.strftime("%Y/%m/%d")
        url = epic_example.format(date=date, image=earth_images[image_number]['image'], nasa_api_key=nasa_api_key)
        download_image(url, 'images/')


def main():
    Path("images").mkdir(parents=True, exist_ok=True)
    fetch_nasa_epic_launch()


if __name__ == '__main__':
    main()
