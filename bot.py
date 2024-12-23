"""Main script to run the bot."""

import time
from telegram.ext import (
    Application,
    InlineQueryHandler,
    CommandHandler,
    MessageHandler,
    filters,
    JobQueue,
)

from modules import (
    start_cmd,
    help_cmd,
    tokens_cmd,
    message_handler,
    send_message,
)
import config


def main():
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(config.TOKEN).build()

    job_queue = application.job_queue
    job_queue.run_repeating(send_message.send_updates, interval=10, first=10)

    # Register handlers
    application.add_handler(CommandHandler("start", start_cmd.start_command))
    application.add_handler(CommandHandler("help", help_cmd.help_command))
    application.add_handler(CommandHandler("tokens", tokens_cmd.token_command))
    application.add_handler(CommandHandler("options", message_handler.options))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler.message_handler)
    )
    application.add_handler(InlineQueryHandler(message_handler.inline_query))
    # Start the Bot
    application.run_polling()


if __name__ == "__main__":
    main()
