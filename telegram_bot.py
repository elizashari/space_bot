import os
from dotenv import load_dotenv
import time
import argparse
import telegram


def main():
    load_dotenv()
    telegam_token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TG_CHAT_ID"]
    bot = telegram.Bot(token=telegam_token)
    parser = argparse.ArgumentParser(description="Программа высылает фото в чат с указанной задержкой")
    parser.add_argument("--delay", help="Задержка", default=14400)
    args = parser.parse_args()
    posting_period = args.delay
    while True:
        for root, dirs, files in os.walk("images"):
            for filename in files:
                image_path = os.path.join(root, filename)
                with open(image_path, "rb") as file:
                    photo = file.read()
                    bot.send_photo(chat_id=chat_id, photo=photo)
                time.sleep(float(posting_period))

if __name__ == "__main__":
    main()

