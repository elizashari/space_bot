import requests
import os
import argparse
from download_image import download_image


def fetch_spacex_last_launch(spacex_launch_id):
    response_spacex = requests.get(f"https://api.spacexdata.com/v5/launches/{spacex_launch_id}")
    response_spacex.raise_for_status()
    links = response_spacex.json()["links"]["flickr"]["original"]
    for link_number, link in enumerate(links):
        filename = f"spacex_{link_number}.jpeg"
        file_path = os.path.join(dir_name, filename)
        download_image(file_path, link)


def main():
    dir_name = "images"
    os.makedirs(dir_name, exist_ok=True)
    parser = argparse.ArgumentParser(
        description="Программа скачивает фото Spacex по указанному ID запуска"
    )
    parser.add_argument("id", help="ID запуска")
    args = parser.parse_args()
    spacex_launch_id = args.id
    fetch_spacex_last_launch(spacex_launch_id)
    

if __name__ == "__main__":
    main()
