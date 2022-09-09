import os
from dotenv import load_dotenv


load_dotenv()

SPACEX_LAUNCH_API = 'https://api.spacexdata.com/v5/launches'

NASA_APOD_API = 'https://api.nasa.gov/planetary/apod'
NASA_EPIC_API = 'https://api.nasa.gov/EPIC/api/natural/images'
NASA_EPIC_ARCHIVE_API = 'https://api.nasa.gov/EPIC/archive/natural'
MAX_EPIC_PIC_COUNT = 2
NASA_PIC_COUNT = 2

NASA_API_KEY = os.getenv("NASA_API_KEY")

TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
CHAT_ID = '@dvmn_space_community_test'
