import requests
import settings

from files_helper import save_image, get_extension_by_url
from pathlib import Path


def fetch_nasa_apod_images():
    payload = {
        "api_key": settings.NASA_API_KEY,
        "count": settings.MAX_NASA_APOD_PIC_COUNT
    }
    response = requests.get(settings.NASA_APOD_API, params=payload)
    response.raise_for_status()
    outpath = Path.cwd() / 'images'
    Path(outpath).mkdir(exist_ok=True)
    for record_number, record in enumerate(response.json()):
        picture_url = record['url']
        picture_extension = get_extension_by_url(picture_url)
        picture_name = f'nasa_apod_{record_number}{picture_extension}'
        save_image(picture_url, outpath / picture_name)


if __name__ == "__main__":
    fetch_nasa_apod_images()
