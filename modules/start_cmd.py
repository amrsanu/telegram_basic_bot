from telegram import Update
from telegram.ext import CallbackContext

from modules.message_handler import COMMANDS
from config import user_chat_ids


async def start_command(update: Update, context: CallbackContext) -> None:
    user_chat_ids.append(
        {
            "chat_id": update.effective_chat.id,
            "context": context,
        }
    )

    message = "Hello! Welcome to the bot.\nAvailable commands:\n" + "\n".join(
        [f"/{cmd} - {desc}" for cmd, desc in COMMANDS.items()]
    )
    await update.message.reply_text(message)
