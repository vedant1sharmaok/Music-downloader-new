from pyrogram import filters
from pyrogram.types import Message

def settings_handler(app):
@Client.on_message(filters.command("settings"))
async def settings_handler(client, message):
    await message.reply(
        "Settings:\n\n"
        "1. Preferred Format (Audio/Video)\n"
        "2. Quality Selection\n"
        "3. Language (coming soon)"
    )
)
