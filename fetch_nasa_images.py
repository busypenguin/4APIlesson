import requests
from additional_settings import download_image, find_format, nasa_api_key
from pathlib import Path


def fetch_nasa_last_launch():
    payload = {'?': '/'}
    number_of_images = 30
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}&count={number_of_images}'.format(
                                            nasa_api_key=nasa_api_key, number_of_images=number_of_images), params=payload)
    response.raise_for_status()
    flights = response.json()
    for flight in flights:
        if find_format(flight['url']) == '.jpg':
            download_image(flight['url'], 'images/')


def main():
    Path("images").mkdir(parents=True, exist_ok=True)
    fetch_nasa_last_launch()


if __name__ == '__main__':
    main()
