import os
import requests
import urllib


def save_image(source_url, destination, params=None):
    response = requests.get(source_url, params=params)
    response.raise_for_status()

    with open(destination, "wb") as file:
        file.write(response.content)


def get_extension_by_url(url):
    path = urllib.parse.urlsplit(url).path
    extension = os.path.splitext(path)[1]
    return extension
