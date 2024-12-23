import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Heroku Details
# https://anant1212-bot-658ea6576886.herokuapp.com/
# https://git.heroku.com/anant1212-bot.git

# Access environment variables
URL = os.getenv("BOT_LINK")
TOKEN = os.getenv("TELEGRAM_TOKEN")

user_chat_ids = []
