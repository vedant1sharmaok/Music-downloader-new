from pyrogram import filters
from pyrogram.types import Message
from bot.config.env import OWNER_ID

def admin_handler(app):
    @app.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
    async def broadcast(client, message: Message):
        await message.reply("Broadcast feature coming soon!")

    @app.on_message(filters.command("stats") & filters.user(OWNER_ID))
    async def stats(client, message: Message):
        await message.reply("Stats feature coming soon!")
