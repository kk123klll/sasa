import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["المطور","المبرمج"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users()
    name = usr.first_name
    async for photo in client.iter_profile_photos(5946704196, limit=1):
                    await message.reply_photo(photo.file_id,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{OWNER}"),
                ],
            ]
        ),
    )
