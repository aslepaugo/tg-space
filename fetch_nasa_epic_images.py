from datetime import datetime
import requests
import settings

from files_helper import save_image
from pathlib import Path


def fetch_nasa_epic_images():
    payload = {
        "api_key": settings.NASA_API_KEY
    }
    response = requests.get(settings.NASA_EPIC_API, params=payload)
    response.raise_for_status()
    outpath = Path.cwd() / 'images'
    Path(outpath).mkdir(exist_ok=True)
    for record_number, record in enumerate(response.json()):
        image_name = record['image']
        image_date = record['date']
        image_date = datetime.fromisoformat(image_date)
        image_url = f"{settings.NASA_EPIC_ARCHIVE_API}/{image_date.year}/{image_date.month:02d}/{image_date.day:02d}/png/{image_name}.png"
        picture_name = f'nasa_epic_{record_number}.png'
        save_image(image_url, outpath / picture_name, params=payload)
        if record_number == settings.MAX_NASA_EPIC_PIC_COUNT - 1:
            break


if __name__ == "__main__":
    fetch_nasa_epic_images()
