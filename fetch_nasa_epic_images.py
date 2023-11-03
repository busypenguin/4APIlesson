import requests
import datetime
from additional_settings import download_images, nasa_api_key
from pathlib import Path


def fetch_nasa_epic_launch():
    response = requests.get('https://api.nasa.gov/EPIC/api/natural?api_key={nasa_api_key}'.format(nasa_api_key=nasa_api_key))
    data_json = response.json()
    epic_example = 'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png?api_key={nasa_api_key}'
    for el, data in enumerate(data_json):
        date = data_json[el]['date']
        date = datetime.datetime.fromisoformat(date)
        date = date.strftime("%Y/%m/%d")
        url = epic_example.format(date=date, image=data_json[el]['image'], nasa_api_key=nasa_api_key)
        download_images(url, 'images/')


Path("images").mkdir(parents=True, exist_ok=True)
fetch_nasa_epic_launch()
