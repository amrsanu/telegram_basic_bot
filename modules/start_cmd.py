from telegram import Update
from telegram.ext import CallbackContext


async def start_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! Welcome to the bot.")
