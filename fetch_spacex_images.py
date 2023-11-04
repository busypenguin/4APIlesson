import requests
import argparse
from additional_settings import download_image
from pathlib import Path


def fetch_spacex_last_launch():
    parser = argparse.ArgumentParser(
        description='Программа скачивает картинки с сайта spacex'
    )
    parser.add_argument("--id", help="ID запуска", default='')
    args = parser.parse_args()
    id = args.id
    response = requests.get('https://api.spacexdata.com/v5/launches/{}'.format(id))
    response.raise_for_status()
    flight_data_json = response.json()
    if id != '':
        list_with_dict = []
        list_with_dict.append(flight_data_json)
        flight_data_json = list_with_dict
    for data in flight_data_json:
        pic = data['links']['patch']['large']
        download_image(pic, 'images/')


def main():
    Path("images").mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
