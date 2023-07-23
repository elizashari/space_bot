# Телеграм-Бот
С помощью этого проекта вы сможете скачать фото с сайта Nasa, Spacex или высылать фото из директории в Telegram канал.

### Как установить
Зарегистрируйтесь на сайте [Nasa](https://api.nasa.gov/) и получите персональный токен, далее поместите ваш токен в файл .env под названием NASA_TOKEN

Получите ID запуска Spacex для дальнейшего использования в запуске скрипта.

Получите токен своего телеграм-бота. 

Вместе с ID своего телеграм чата положите эти данные в файл .env , Токен под названием TELEGRAM_TOKEN, а ID чата
под названием TG_CHAT_ID.

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Как запустить
Чтобы запустить код используйте консольную команду python3, указав нужный вам скрипт и нужные ему аргументы:
Скачивание фото дня с Nasa:
```
python3 get_nasa_photo.py
```
Скачивание фото со Spacex:
```
python3 fetch_spacex_images.py 
```
Скачивание фото EPIC:
```
python3 get_epic_photo.py
```
Отправка фото в Телеграм:
```
python3 telegram_bot.py 
```

### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
