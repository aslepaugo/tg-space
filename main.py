import datetime
import os
import requests
import settings
import urllib

from pathlib import Path


def get_extension_by_url(url):
    path = urllib.parse.urlsplit(url).path
    extension = os.path.splitext(path)[1]
    return extension


def save_picture(source_url, destination, params=None):
    response = requests.get(source_url, params=params)
    response.raise_for_status()

    with open(destination, "wb") as file:
        file.write(response.content)


def fetch_nasa_pictures():
    payload = {
        "api_key": settings.NASA_API_KEY,
        "count": settings.NASA_PIC_COUNT
    }
    response = requests.get(settings.NASA_APOD_API, params=payload)
    response.raise_for_status()
    for record_number, record in enumerate(response.json()):
        picture_url = record['url']
        picture_extension = get_extension_by_url(picture_url)
        save_picture(picture_url, f"./images/nasa_apod_{record_number}{picture_extension}")


def fetch_nasa_epic_pictures():
    payload = {
        "api_key": settings.NASA_API_KEY
    }
    response = requests.get(settings.NASA_EPIC_API, params=payload)
    response.raise_for_status()

    for record_number, record in enumerate(response.json()):
        image_name = record['image']
        image_date = record['date']
        image_date = datetime.datetime.fromisoformat(image_date)
        image_url = f"{settings.NASA_EPIC_ARCHIVE_API}/{image_date.year}/{image_date.month:02d}/{image_date.day:02d}/png/{image_name}.png"
        save_picture(image_url, f"./images/nasa_epic_{record_number}.png", params=payload)
        if record_number == settings.MAX_EPIC_PIC_COUNT - 1:
            break


def fetch_spacex_last_launch():
    response = requests.get(settings.SPACE_X_LAUNCH_LATEST)
    response.raise_for_status()
    picture_urls = response.json()['links']['flickr']['original']

    for picrure_number, picture_url in enumerate(picture_urls):
        save_picture(picture_url, f"./images/spacex_{picrure_number}.jpg")


if __name__ == "__main__":
    Path("./images").mkdir(exist_ok=True)
    fetch_spacex_last_launch()
    fetch_nasa_pictures()
    fetch_nasa_epic_pictures()
