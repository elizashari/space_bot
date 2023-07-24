import requests
import os
import datetime
from dotenv import load_dotenv
from download_image import download_image


def get_epic(nasa_token):
    payload = {"api_key": nasa_token}
    url = "https://epic.gsfc.nasa.gov/api/natural"
    response = requests.get(url, params=payload)
    response.raise_for_status()
    epic_response = response.json()
    for number, image in enumerate(epic_response):
        filename = f"nasa_epic_{number}.png"
        file_path = os.path.join(dir_name, filename)
        image_name = image["image"]
        image_date = image["date"]
        image_datetime = datetime.datetime.fromisoformat(image_date)
        formatted_image_date = image_datetime.strftime("%Y/%m/%d")
        epic_url = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_image_date}/png/{image_name}.png"
        download_image(file_path, epic_url, params=payload)


def main():
    load_dotenv()
    dir_name = "images"
    os.makedirs(dir_name, exist_ok=True)
    nasa_token = os.getenv("NASA_TOKEN")
    get_epic(nasa_token)


if __name__ == "__main__":
 main()
