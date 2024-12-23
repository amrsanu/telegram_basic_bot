from telegram import Update
from telegram.ext import CallbackContext


async def token_command(update: Update, context: CallbackContext) -> None:
    tokens = update.message.text.split(" ")[1:]
    token_details = []
    if tokens:
        for token in tokens:
            token_details.append(f"Name: {token} Details: This is {token} token.")
    else:
        token_details.append("No tokens provided.")

    await update.message.reply_text("\n".join(token_details))
