# My Space Telegram channel publishing support

## Be ready with your channel and telegram bot registration

I assume that you already have your channel and telegram bot.

But if you not, it's not a problem.

How to register your bot and setup you channel is described [here](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/)

If you'd like to use NASA pictures you should gain your API key [here](https://api.nasa.gov)
## Prepare scripts and settings

1. Create `.env` file to store environment variables:

```bash
NASA_API_KEY = 'YOUR_NASA_API_KEY'
TG_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
```

2. Prepare and fill [settings](./settings.py) with the following parameters:

```bash
MAX_NASA_EPIC_PIC_COUNT = {IDENTIFY MAXIMUM NASA EPIC PHOTOS TO LOAD}
MAX_NASA_APOD_PIC_COUNT = {IDENTIFY MAXIMUM NASA A PICTURE OF A DAY PHOTOS TO LOAD}

CHAT_ID = '@your_channel'
```

3. It's highly recommended to create virtual environment 

```bash
python -m venv venv
```

Activate your virtual environment:

```bash
. ./venv/bin/activate
# for Windows
# . ./venv/Scripts/activate
```

4. Install dependencies from requirements.txt

```bash
pip install -r requirements.txt
```

5. You are ready to go with scripts.

Scripts:

Scripts for images download use folder images to store photos. 

You can add your own photos there.


### fetch_spacex_images.py

To get photos for specific launch of SpaceX you can put it ID as a parameter

```bash
python fetch_spacex_images.py -lid 5eb87d42ffd86e000604b384
```

To get latest launch image run without any parameter

```bash
python fetch_spacex_images.py
```

### fetch_nasa_apod_images.py

To get pictire of a day from NASA

```bash
python fetch_nasa_apod_images.py
```

### fetch_nasa_epic_images.py

To get EPIC picture from NASA

```bash
python fetch_nasa_epic_images.py
```

### download_from_all_sources.py

Script to use all 3 available sources 

```bash
python download_from_all_sources.py
```

### load_images_into_tg_channel.py

Script periodicall uploads photos from `images` directory into Telegram Channel.

`--hours` is used to identify how often photos should be uploaded (default 4 hours)
`--photo` is used to upload 1 specific photo from `images` folder
`--infinite` is used to run infinitely with delay defined in `--hours` (default 4 hours)

```bash
python load_images_into_tg_channel.py --infinite True --hours 6
```

```bash
python load_images_into_tg_channel.py --photo spacex_4.jpg
```
