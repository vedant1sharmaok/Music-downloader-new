from pyrogram import filters
from pyrogram.types import Message
from bot.config.env import LOGGER_ID
from bot.utils.force_join import check_force_join

def start_handler(app):
    @app.on_message(filters.command("start"))
    async def start(client, message: Message):
        if await check_force_join(client, message):
            return
        await message.reply("Welcome to the Music Bot!")
