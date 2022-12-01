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
    await message.reply_photo(
        photo="https://telegra.ph/file/04a69ce280b397914d5f7.jpg",
        caption=f"""𝒘𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 𝒕𝒉𝒆 𝑨 𝑷 𝑹 𝑰 𝑳 𝒎𝒖𝒔𝒊𝒄 𝒔𝒐𝒖𝒓𝒄𝒆, 𝒇𝒐𝒍𝒍𝒐𝒘 𝒕𝒉𝒆 𝒃𝒐𝒕 𝒖𝒑𝒅𝒂𝒕𝒆𝒔 𝒃𝒚 𝒑𝒓𝒆𝒔𝒔𝒊𝒏𝒈 𝒕𝒉𝒆 𝒄𝒉𝒂𝒏𝒏𝒆𝒍 𝒃𝒖𝒕𝒕𝒐𝒏, 𝒌𝒊𝒏𝒅𝒍𝒚""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("𝑨 𝑯 𝑴 𝑬 𝑫", url=f"https://t.me/ccbee",
                ),
                InlineKeyboardButton(f"𝑨 𝑷 𝑹 𝑰 𝑳", url=f"https://t.me/sspaa",
                ),
            ],
            [
                InlineKeyboardButton("‹ أضفني لمجموعتك ›", url=f"https://t.me/AprilMubot?startgroup=true",
                ),
                ]
            ]
        ),
    )
