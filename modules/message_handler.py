from telegram import (
    Update,
    InlineQueryResultArticle,
    InputTextMessageContent,
)
from telegram.ext import (
    CallbackContext,
)
from uuid import uuid4

# Define command suggestions and autocompletions
COMMANDS = {
    "start": "Begin interacting with the bot",
    "help": "Get help information",
    "tokens": "List of tokens to track, separated by space",
    "options": "List all available commands",
}


async def options(update: Update, context: CallbackContext):
    message = "Available commands:\n" + "\n".join(
        [f"/{cmd} - {desc}" for cmd, desc in COMMANDS.items()]
    )
    await update.message.reply_text(message)


async def message_handler(update: Update, context: CallbackContext):
    user_input = update.message.text
    suggestions = [cmd for cmd in COMMANDS if cmd.startswith(user_input.strip("/"))]
    if suggestions:
        suggestion_message = "Did you mean:\n" + "\n".join(
            [f"/{cmd}" for cmd in suggestions]
        )
        await update.message.reply_text(suggestion_message)


async def inline_query(update: Update, context: CallbackContext):
    query = update.inline_query.query
    print("calling inline query")
    if query.startswith("/"):
        results = [
            InlineQueryResultArticle(
                id=str(uuid4()),
                title=f"/{cmd}",
                input_message_content=InputTextMessageContent(f"/{cmd}"),
                description=desc,
            )
            for cmd, desc in COMMANDS.items()
            if cmd.startswith(query[1:])
        ]
        await update.inline_query.answer(results, cache_time=0)
