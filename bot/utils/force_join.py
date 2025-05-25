from pyrogram.errors import UserNotParticipant
from pyrogram.types import Message
from bot.config.env import LOGGER_ID

async def check_force_join(client, message: Message):
    try:
        member = await client.get_chat_member(LOGGER_ID, message.from_user.id)
        return False
    except UserNotParticipant:
        await message.reply(f"Please join our updates channel first: https://t.me/c/{str(LOGGER_ID)[4:]}/")
        return True
