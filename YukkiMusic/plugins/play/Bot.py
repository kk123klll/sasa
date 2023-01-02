import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")

IMG_BOT1 = getenv("IMG_BOT1")

OWNER = getenv("OWNER")

OWNER_NAME = getenv("OWNER_NAME")

NAME_BOT = getenv("NAME_BOT")


def get_file_id(msg: Message):

    if msg.media:

        for message_type in (

            "photo",

            "animation",

            "audio",

            "document",

            "video",

            "video_note",

            "voice",

            # "contact",

            # "dice",

            # "poll",

            # "location",

            # "venue",

            "sticker",

        ):

            obj = getattr(msg, message_type)

            if obj:

                setattr(obj, "message_type", message_type)

                return obj

@app.on_message(
    command(["بوت"])
    & filters.group
    & ~filters.edited
)

async def khalid(client: Client, message: Message):

    usr = await client.get_users(ID_BOT1)

    name = usr.first_name

    async for photo in client.iter_profile_photos(ID_BOT1, limit=1):

                    await message.reply_photo(photo.file_id,       caption=f"اسمي {NAME_BOT} عمري .", 

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        f"{OWNER_NAME}", url=f"https://t.me/{OWNER}") 

                ],[

                    InlineKeyboardButton(

                        "- اضافة الى مجموعة .", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),

                ],

            ]

        ),

    )
