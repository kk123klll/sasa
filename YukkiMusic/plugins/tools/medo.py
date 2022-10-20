from strings.filters import command
from pyrogram import filters, Client
from YukkiMusic import app
from typing import Union
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)


@app.on_message(command(["سورس","السورس","المطور","مطور"])
    & filters.group
    & ~filters.edited
)
@app.on_message(command(["سورس","السورس","المطور","مطور"])
    & filters.channel
    & ~filters.edited
)
async def ahmad(client: Client, message: Message):
    await message.reply_video(
        video="https://telegra.ph/file/0506fadf1547e11548b5c.mp4",
        caption=f"""**‹ Welcome to the Music Source ›**""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("‹ المطور ›", url=f"https://t.me/aaaqqq",
                ),
                InlineKeyboardButton(f"‹ السورس ›", url=f"https://t.me/zzzzx1",
                ),
            ],
            [
                InlineKeyboardButton("‹ أضفني لمجموعتك ›", url=f"https://t.me/ZXXCAQPBOT?startgroup=true",
                ),
                InlineKeyboardButton("‹ قناة البوت ›", url=f"https://t.me/zzzzx1",),
                ]
            ]
        ),
    )
