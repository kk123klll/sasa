from strings.filters import command
from pyrogram import filters, Client
from YukkiMusic import app
from typing import Union
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)


@app.on_message(command(["سورس","السورس","المطور","المبرمج"])
    & filters.group
    & ~filters.edited
)
@app.on_message(command(["سورس","السورس","المطور","المبرمج"])
    & filters.channel
    & ~filters.edited
)
async def ahmad(client: Client, message: Message):
    await message.reply_video(
        video="https://telegra.ph/file/148226fc83f4112ac89d2.mp4",
        caption=f"""**‹ Welcome to the Music Source ›**""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("‹ المطور ›", url=f"https://t.me/ku_kx",
                ),
                InlineKeyboardButton(f"‹ السورس ›", url=f"https://t.me/YaFaSoR",
                ),
            ],
            [
                InlineKeyboardButton("‹ أضفني لمجموعتك ›", url=f"https://t.me/YaFaMuBot?startgroup=true",
                ),
                InlineKeyboardButton("‹ قناة البوت ›", url=f"https://t.me/ssAee",),
                ]
            ]
        ),
    )
