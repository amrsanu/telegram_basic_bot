from telegram import Update
from telegram.ext import CallbackContext


async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("This is a help message.")
