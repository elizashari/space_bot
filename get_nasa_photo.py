import os
import requests
from urllib.parse import urlparse
from download_image import download_image
from dotenv import load_dotenv


def get_file_extension(url):
    url = "https://api.nasa.gov/planetary/apod"
    parsed_url = urlparse(url)
    extention = os.path.splitext(parsed_url.path)
    return extention


def get_nasa_image(nasa_token):
    nasa_images = []
    payload = {
        "api_key": nasa_token
    }
    url = "https://api.nasa.gov/planetary/apod"
    nasa_response = requests.get(url, params=payload)
    nasa_response.raise_for_status()
    links = nasa_response.json()
    for number, image in enumerate(links):
        if image["media_type"] == "video":
            continue
        nasa_photo_url = image['url']
        parse = urlparse(nasa_photo_url)
        parse_path = parse.path
        extension = get_file_extension(parse_path)
        filename = f"nasa_apod_{number}{extension}"
        file_path = os.path.join(dir_name, filename)
        download_image(file_path, nasa_photo_url)


def main():
    load_dotenv()
    dir_name = "images"
    os.makedirs(dir_name, exist_ok=True)
    nasa_token = os.getenv("NASA_TOKEN")
    get_nasa_image(nasa_token)



if __name__ == "__main__":
     main()

