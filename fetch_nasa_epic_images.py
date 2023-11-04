import requests
import datetime
from additional_settings import download_image, nasa_api_key
from pathlib import Path


def fetch_nasa_epic_launch():
    response = requests.get('https://api.nasa.gov/EPIC/api/natural?api_key={nasa_api_key}'.format(nasa_api_key=nasa_api_key))
    response.raise_for_status()
    data_on_Earth_images_json = response.json()
    epic_example = 'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png?api_key={nasa_api_key}'
    epic_example.raise_for_status()
    for el, data in enumerate(data_on_Earth_images_json):
        date = data_on_Earth_images_json[el]['date']
        date = datetime.datetime.fromisoformat(date)
        date = date.strftime("%Y/%m/%d")
        url = epic_example.format(date=date, image=data_on_Earth_images_json[el]['image'], nasa_api_key=nasa_api_key)
        download_image(url, 'images/')


def main():
    Path("images").mkdir(parents=True, exist_ok=True)
    fetch_nasa_epic_launch()


if __name__ == '__main__':
    main()
