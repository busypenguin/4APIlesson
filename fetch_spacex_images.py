import requests
import argparse
from additional_settings import download_images
from pathlib import Path


def fetch_spacex_last_launch():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", help="ID запуска")
    args = parser.parse_args()
    id = args.id
    if id is None:
        id = ''
    response = requests.get('https://api.spacexdata.com/v5/launches/{}'.format(id))
    response.raise_for_status()
    data_json = response.json()
    if id != '':
        list_with_dict = []
        list_with_dict.append(data_json)
        data_json = list_with_dict
    for data in data_json:
        pic = data['links']['patch']['large']
        download_images(pic, 'images/')


Path("images").mkdir(parents=True, exist_ok=True)
fetch_spacex_last_launch()
