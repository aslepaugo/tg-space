import os
from dotenv import load_dotenv


load_dotenv()

SPACE_X_LAUNCH_ALL = 'https://api.spacexdata.com/v4/launches'
SPACE_X_LAUNCH_LATEST = 'https://api.spacexdata.com/v5/launches/latest'

NASA_APOD_API = 'https://api.nasa.gov/planetary/apod'
NASA_EPIC_API = 'https://api.nasa.gov/EPIC/api/natural/images'
NASA_EPIC_ARCHIVE_API = 'https://api.nasa.gov/EPIC/archive/natural'
MAX_EPIC_PIC_COUNT = 5
NASA_PIC_COUNT = 5

NASA_API_KEY = os.getenv("NASA_API_KEY")
