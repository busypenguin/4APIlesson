import requests
from urllib.parse import urlsplit
import os
from environs import Env


env = Env()
env.read_env()
nasa_api_key = env.str('NASA_API_KEY')
telegram_bot_token = env.str('TELEGRAM_BOT_TOKEN')
tg_chat_id = env.str('TG_CHAT_ID')


def download_image(url, folder_path):
    filename = url.split("/")[-1]
    response = requests.get(url)
    response.raise_for_status()
    with open(f'{folder_path}{filename}', "wb") as file:
        file.write(response.content)


def find_format(url):
    path_of_url = urlsplit(url)
    part_of_path_of_url = os.path.split(path_of_url[2])
    shorten_url = os.path.splitext(part_of_path_of_url[1])
    format_of_url = shorten_url[1]
    return format_of_url
