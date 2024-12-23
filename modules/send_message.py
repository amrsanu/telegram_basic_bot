from telegram.ext import (
    CallbackContext,
)
from config import user_chat_ids


async def send_updates(context: CallbackContext):
    print(f"Users: {user_chat_ids}")
    for user in user_chat_ids:
        chat_id = user["chat_id"]
        await context.bot.send_message(
            chat_id=chat_id, text="Hello, this is a periodic update!"
        )
