import telegram
from additional_settings import telegram_bot_token, chat_id
import os
import argparse
import random
import time


images = os.walk('images/')
bot = telegram.Bot(token=telegram_bot_token)
parser = argparse.ArgumentParser()
parser.add_argument("--sec", help="Перерыв между отправкой картинок в секунду", type=int)
args = parser.parse_args()
sec = args.sec
if sec is None:
    sec = 14400
while True:
    for image in images:
        path = image[0]
        for pic in image[2]:
            bot.send_photo(chat_id, photo=open(str(path+pic), 'rb'))
            time.sleep(sec)
        random.shuffle(image)
