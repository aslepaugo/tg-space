import argparse
import requests
import settings

from files_helper import save_image


def fetch_spacex_images(launch_id=None):
    if launch_id is None:
        response = requests.get(f"{settings.SPACEX_LAUNCH_API}/latest")
    else:
        response = requests.get(f"{settings.SPACEX_LAUNCH_API}/{launch_id}")
    response.raise_for_status()
    image_urls = response.json()['links']['flickr']['original']
    for picrure_number, picture_url in enumerate(image_urls):
        save_image(picture_url, f"./images/spacex_{picrure_number}.jpg")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Upload SpaceX Images')
    parser.add_argument('-lid', '--launchID', help='Launch ID from SpaceX program')
    args = parser.parse_args()
    fetch_spacex_images(args.launchID)
