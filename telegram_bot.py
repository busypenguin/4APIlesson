import telegram
from additional_settings import telegram_bot_token


bot = telegram.Bot(token=telegram_bot_token)


# bot.send_message(chat_id='@The_best_pictures_of_space', text="I did it!")



bot.send_photo('@The_best_pictures_of_space', photo=open('images/KsiuGQL4_o.png', 'rb'))

