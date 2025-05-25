from pyrogram import filters
from pyrogram.types import Message

def settings_handler(app):
    @app.on_message(filters.command("settings"))
    async def settings(client, message: Message):
        await message.reply("Settings: Choose your preferred options below.")

1. Format
2. Quality
3. Language (coming soon)")
