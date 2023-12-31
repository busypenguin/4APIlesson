# Автоматическая загрузка картинок космоса 

Проект создан для автоматизации скачивания картинок из космоса 

### Как установить

Создайте файл .env и запишите туда переменные окружения (NASA_API_KEY, TELEGRAM_BOT_TOKEN, TG_CHAT_ID) и их значения.

NASA_API_KEY можно получить на сайте [NASA](https://api.nasa.gov/).
TELEGRAM_BOT_TOKEN вы получаете после создания телеграм-бота.
TG_CHAT_ID это путь к вашей группе в телеграме.

Например:

```NASA_API_KEY = XtF68J5HnvuAOrOuXaFH0lHJlwztVndKkf```

Дальше можете скачать картинки в папку images, взапустив файлы fetch_spacex_images.py, fetch_nasa_images.py, fetch_nasa_epic_images.py. Обратите внимание, что запустить файлы можно написав в терминале:

```python3 fetch_nasa_images.py```

Но для файла fetch_spacex_images.py, можно указать id полёта:

```python3 fetch_spacex_images.py 5eb87d42ffd86e000604b384```

Затем можно запустить  файл telegram_bot.py, указав промежуток времени между загрузкой фотографий в секундах(по умолчанию промежуток равен 4 часа)

```python3 telegram_bot.py 60```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).