from strings.filters import command
from pyrogram import filters, Client
from YukkiMusic import app
from typing import Union
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message, CallbackQuery)


@app.on_message(command(["سورس ليز","السورس","سورس"])
    & filters.group
    & ~filters.edited
)
async def ahmad(client: Client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/94f1316d4fc5546bb9c4c.jpg",
        caption=f"""𝒘𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 𝒕𝒉𝒆 [liz](https://t.me/zzsvv) 𝒎𝒖𝒔𝒊𝒄 𝒔𝒐𝒖𝒓𝒄𝒆, 𝒇𝒐𝒍𝒍𝒐𝒘 𝒕𝒉𝒆 𝒃𝒐𝒕 𝒖𝒑𝒅𝒂𝒕𝒆𝒔 𝒃𝒚 𝒑𝒓𝒆𝒔𝒔𝒊𝒏𝒈 𝒕𝒉𝒆 𝒄𝒉𝒂𝒏𝒏𝒆𝒍 𝒃𝒖𝒕𝒕𝒐𝒏, 𝒌𝒊𝒏𝒅𝒍𝒚""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("‹ ضيفني لكروبك ›", url=f"https://t.me/ZXXCAQPBOT?startgroup=true",
                ),
            ],
            [
                InlineKeyboardButton("‹ حول السورس ›", callback_data=f"eslam"),
            ],
            ]
        ),
    )
@app.on_callback_query(filters.regex("eslam"))
async def eslam(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""- معلومات حول بوت ليز اتبع الازرار .""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "- مطور السورس .", url=f"https://t.me/AAAQQQ"),
                    InlineKeyboardButton(
                        "- قناة السورس .", url=f"https://t.me/zzSvv"),
                ],[
                    InlineKeyboardButton(
                        "المساعد", url=f"https://t.me/zzTaa"),
                ],[ 
                    InlineKeyboardButton(
                        "اغلاق", callback_data="close"),
                    InlineKeyboardButton(
                        "رجوع", callback_data="back1"),
               ],
          ]
        ),
    )
@app.on_callback_query(filters.regex("back1"))
async def back1(_, query: CallbackQuery):
   await query.edit_message_text("""𝒘𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 𝒕𝒉𝒆 [liz](https://t.me/zzSvv) 𝒎𝒖𝒔𝒊𝒄 𝒔𝒐𝒖𝒓𝒄𝒆, 𝒇𝒐𝒍𝒍𝒐𝒘 𝒕𝒉𝒆 𝒃𝒐𝒕 𝒖𝒑𝒅𝒂𝒕𝒆𝒔 𝒃𝒚 𝒑𝒓𝒆𝒔𝒔𝒊𝒏𝒈 𝒕𝒉𝒆 𝒄𝒉𝒂𝒏𝒏𝒆𝒍 𝒃𝒖𝒕𝒕𝒐𝒏, 𝒌𝒊𝒏𝒅𝒍𝒚""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("‹ ضيفني لكروبك ›", url=f"https://t.me/ZXXCAQPBOT?startgroup=true",
                ),
            ],
            [
                InlineKeyboardButton("‹ حول السورس ›", callback_data=f"eslam"),
            ],
            ]
        ),
    )
