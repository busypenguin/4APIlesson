import telegram
from additional_settings import telegram_bot_token, tg_chat_id
import os
import argparse
import random
import time


def main():
    images = os.walk('images/')
    bot = telegram.Bot(token=telegram_bot_token)
    parser = argparse.ArgumentParser(
        description='Отрправляет картинки через бота в группу'
    )
    parser.add_argument("--sec", help="Перерыв между отправкой картинок в секунду", type=int, default=14400)
    args = parser.parse_args()
    sec = args.sec
    while True:
        for image in images:
            path = image[0]
            for pic in image[2]:
                with open(f"{path}{pic}", 'rb') as photo:
                    bot.send_photo(tg_chat_id,  photo)
                    time.sleep(sec)
            random.shuffle(image)


if __name__ == '__main__':
    main()
