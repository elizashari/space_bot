import os
import requests
from urllib.parse import urlsplit, unquote


def download_image(file_path, url, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(file_path, "wb") as file:
        file.write(response.content)

