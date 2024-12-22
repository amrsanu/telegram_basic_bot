"""Main script to run the bot."""

from telegram.ext import Application, CommandHandler

import config
from modules import start_cmd, help_cmd


def main():
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(config.TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start_cmd.start_command))
    application.add_handler(CommandHandler("help", help_cmd.help_command))

    # Start the Bot
    application.run_polling()


if __name__ == "__main__":
    main()
