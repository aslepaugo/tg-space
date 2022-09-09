import requests
import settings

from files_helper import save_image, get_extension_by_url


def fetch_nasa_apod_images():
    payload = {
        "api_key": settings.NASA_API_KEY,
        "count": settings.NASA_PIC_COUNT
    }
    response = requests.get(settings.NASA_APOD_API, params=payload)
    response.raise_for_status()
    for record_number, record in enumerate(response.json()):
        picture_url = record['url']
        picture_extension = get_extension_by_url(picture_url)
        save_image(picture_url, f"./images/nasa_apod_{record_number}{picture_extension}")


if __name__ == "__main__":
    fetch_nasa_apod_images()
