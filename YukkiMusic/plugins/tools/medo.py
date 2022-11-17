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
        photo="https://telegra.ph//file/af1a88818924a8508a096.jpg",
        caption=f"""𝒘𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 𝒕𝒉𝒆 𝒄𝒐𝒇𝒇𝒆𝒆 𝒎𝒖𝒔𝒊𝒄 𝒔𝒐𝒖𝒓𝒄𝒆, 𝒇𝒐𝒍𝒍𝒐𝒘 𝒕𝒉𝒆 𝒃𝒐𝒕 𝒖𝒑𝒅𝒂𝒕𝒆𝒔 𝒃𝒚 𝒑𝒓𝒆𝒔𝒔𝒊𝒏𝒈 𝒕𝒉𝒆 𝒄𝒉𝒂𝒏𝒏𝒆𝒍 𝒃𝒖𝒕𝒕𝒐𝒏, 𝒌𝒊𝒏𝒅𝒍𝒚""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ᗩᕼᗰᗩᗪ 🇨🇦", url=f"https://t.me/sspaa",
                ),
                InlineKeyboardButton(f"˹ 𝐶𝑜𝑓𝑓𝑒𝑒 ‌☕", url=f"https://t.me/ssaee",
                ),
            ],
            [
                InlineKeyboardButton("‹ أضفني لمجموعتك ›", url=f"https://t.me/CoffeMusic3bot?startgroup=true",
                ),
                ]
            ]
        ),
    )
