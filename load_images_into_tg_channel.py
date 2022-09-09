import argparse
import os
import random
import settings
import telegram
import time


def get_images():
    images = []
    for _, _, files in os.walk('./images/'):
        for file in files:
            images.append(file)
    random.shuffle(images)
    return images


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Load space photos and images to Telegram Channel')
    parser.add_argument('--hours', help='Delay for the script in hours', type=int)
    parser.add_argument('--photo', help='Photo name from/images to publish', type=str)
    parser.add_argument('--infinite', help='Run infinitely with delay in --hours', type=bool)
    args = parser.parse_args()
    delay_seconds = 4 * 3600 if args.hours is None else args.hours * 3600
    bot = telegram.Bot(token=settings.TG_BOT_TOKEN)

    if args.photo:
        bot.send_document(chat_id=settings.CHAT_ID, document=open(f'./images/{args.photo}', 'rb'))
    elif not args.infinite:
        bot.send_document(chat_id=settings.CHAT_ID, document=open(f'./images/{get_images()[0]}', 'rb'))

    while True and args.infinite:
        for image in get_images():
            image_size = os.path.getsize(f'./images/{image}')
            if image_size > settings.IMAGE_SIZE_LIMIT:
                continue
            bot.send_document(chat_id=settings.CHAT_ID, document=open(f'./images/{image}', 'rb'))
            time.sleep(delay_seconds)
