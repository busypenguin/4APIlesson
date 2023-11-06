import requests
import argparse
from additional_settings import download_image
from pathlib import Path


def fetch_spacex_last_launch():
    payload = {'?': '/'}
    response = requests.get('https://api.spacexdata.com/v5/launches/{}'.format(flight_id), params=payload)
    response.raise_for_status()
    flights = response.json()
    if flight_id != '':
        flights_combination = []
        flights_combination.append(flights)
        flights = flights_combination
    for flight in flights:
        picture = flight['links']['patch']['large']
        download_image(picture, 'images/')


def main():
    Path("images").mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Программа скачивает картинки с сайта spacex'
    )
    parser.add_argument("--flight_id", help="ID запуска", default='')
    args = parser.parse_args()
    flight_id = args.flight_id
    main()
