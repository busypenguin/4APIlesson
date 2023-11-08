import telegram
from environs import Env
import os
import argparse
import random
import time


def main():
    env = Env()
    env.read_env()
    telegram_bot_token = env.str('TELEGRAM_BOT_TOKEN')
    tg_chat_id = env.str('TG_CHAT_ID')
    images = os.walk('images/')
    bot = telegram.Bot(token=telegram_bot_token)
    parser = argparse.ArgumentParser(
        description='Отрправляет картинки через бота в группу'
    )
    parser.add_argument("--sec", help="Перерыв между отправкой картинок в секунду", type=int, default=14400)
    args = parser.parse_args()
    sec = args.sec
    while True:
        for image_urls in images:
            path = image_urls[0]
            for pic in image_urls[2]:
                with open(f"{path}{pic}", 'rb') as photo:
                    bot.send_photo(tg_chat_id,  photo)
                    time.sleep(sec)
            random.shuffle(image_urls)


if __name__ == '__main__':
    main()
