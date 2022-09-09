import argparse
import os
import random
import settings
import telegram
import time


parser = argparse.ArgumentParser(description='Load space photos and images to Telegram Channel')
parser.add_argument('--hours', help='Delay for the script in hours', type=int)
args = parser.parse_args()
delay_seconds = 4 * 3600 if args.hours is None else args.hours * 3600
bot = telegram.Bot(token=settings.TG_BOT_TOKEN)

delay_seconds = 10  # debug

while True:
    images = []
    for _, _, files in os.walk('./images/'):
        for file in files:
            images.append(file)
    random.shuffle(images)

    for image in images:
        image_size = os.path.getsize(f'./images/{image}')
        if image_size > settings.IMAGE_SIZE_LIMIT:
            continue
        bot.send_document(chat_id=settings.CHAT_ID, document=open(f'./images/{image}', 'rb'))
        time.sleep(delay_seconds)
