import argparse
import requests
import settings

from files_helper import save_image
from pathlib import Path


def fetch_spacex_images(launch_id='latest'):
    response = requests.get(f"{settings.SPACEX_LAUNCH_API}/{launch_id}")
    response.raise_for_status()
    image_urls = response.json()['links']['flickr']['original']
    outpath = Path.cwd() / 'images'
    Path(outpath).mkdir(exist_ok=True)
    for picrure_number, picture_url in enumerate(image_urls):
        picture_name = f'spacex_{picrure_number}.jpg'
        save_image(picture_url, outpath / picture_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Upload SpaceX Images')
    parser.add_argument('-lid', '--launchID', help='Launch ID from SpaceX program', default='latest')
    args = parser.parse_args()
    fetch_spacex_images(args.launchID)
