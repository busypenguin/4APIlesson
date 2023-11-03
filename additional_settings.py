import requests
from pathlib import Path
from urllib.parse import urlsplit
import os
from environs import Env


env = Env()
env.read_env()
nasa_api_key = env.str('NASA_API_KEY')
telegram_bot_token = env.str('TELEGRAM_BOT_TOKEN')
chat_id = env.str('CHAT_ID')
Path("images").mkdir(parents=True, exist_ok=True)


def download_images(url, folder_path):
    filename = url.split("/")[-1]
    response = requests.get(url)
    response.raise_for_status()
    with open(folder_path+filename, "wb") as file:
        file.write(response.content)


def find_format(url):
    path_of_url = urlsplit(url)
    a = os.path.split(path_of_url[2])
    b = os.path.splitext(a[1])
    c = b[1]
    return c
