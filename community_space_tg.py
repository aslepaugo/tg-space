import settings
import telegram

bot = telegram.Bot(token=settings.TG_BOT_TOKEN)
bot.send_document(chat_id=settings.CHAT_ID, document=open('./images/spacex_0.jpg', 'rb'))
