import os, logging, requests
from dotenv import load_dotenv 
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler


load_dotenv()
readwise_token = os.getenv('READWISE_TOKEN')  # or however you're storing your token
telegram_token = os.getenv('TELEGRAM_TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    requests.post(
        url="https://readwise.io/api/v3/save/",
        headers={"Authorization": f"Token {readwise_token}"},
        json={
            "url": "https://yourapp.com#document1",
            "html": f"<p>{update.message.text}</p>",
        }
        )


if __name__ == '__main__':
    application = ApplicationBuilder().token(telegram_token).build()
    
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    
    application.run_polling()
#response = requests.post(
#        url="https://readwise.io/api/v3/save/",
#        headers={"Authorization": f"Token {readwise_token}"}, verify=False,
#        json={
#            "url": "https://yourapp.com#document1",
#            "html": "<p>Your document content here</p>",
#        }
#)
#
