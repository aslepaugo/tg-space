import settings
import telegram

bot = telegram.Bot(token=settings.TG_BOT_TOKEN)
bot.send_message(chat_id=settings.CHAT_ID, text="I'm sorry Dave I'm afraid I can't do that.")
