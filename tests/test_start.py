"""Test module to check the functionality of the start command."""

import unittest
from unittest.mock import MagicMock

from telegram import Update
from telegram.ext import CallbackContext

from telegram_modules.start_cmd import start_command


class TestStartCommand(unittest.TestCase):
    def test_start_command(self):
        update = MagicMock(Update)
        context = MagicMock(CallbackContext)
        start_command(update, context)
        update.message.reply_text.assert_called_with("Hello! Welcome to the bot.")


if __name__ == "__main__":
    unittest.main()
