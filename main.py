from pathlib import Path
from fetch_spacex_images import fetch_spacex_images
from fetch_nasa_apod_images import fetch_nasa_apod_images
from fetch_nasa_epic_images import fetch_nasa_epic_images


if __name__ == "__main__":
    Path("./images").mkdir(exist_ok=True)
    fetch_spacex_images()
    fetch_nasa_epic_images()
    fetch_nasa_apod_images()
