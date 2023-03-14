import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from typing import Union
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup)
from pyrogram.types import Message, VoiceChatStarted, VoiceChatEnded
from YukkiMusic import app

@app.on_message(filters.voice_chat_started)
async def babloo(client: Client, message: Message): 
      Startt = "- بدأت المحادثة الصوتية ."
      await message.reply_text(Startt)

@app.on_message(filters.voice_chat_ended)
async def bablo(client: Client, message: Message): 
      Enddd = "- تم انهاء المحادثه الصوتية ."
      await message.reply_text(Enddd)
@app.on_message(filters.voice_chat_members_invited)
async def fuckoff(client, message):
           text = f"🗯 | قام -> {message.from_user.mention}\n"
           x = 0
           for user in message.voice_chat_members_invited.users:
             try:
               text += f"🗯 | بدعوة -> {user.mention} \n🗯 | إلى المحادثه الصوتية"
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text}")
           except:
             pass

def get_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            "contact",
            "dice",
            "poll",
            "location",
            "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj
              
@app.on_message(command("قناتي"))
async def throw_dice(client, message: Message): 
    await message.reply_text("@zzsvv")
@app.on_message(command(["مظزلتغىونلىتتت"])
    & filters.group
    & ~filters.edited
)
async def ahmad(client: Client, message: Message):
    await message.reply_video(
        video="https://te.legra.ph/file/dbcf6af7538952498c41c.mp4",
        caption=f"""- فرررررررطت ضحك قمنقلععع 😂""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("‹ ضيفني لكروبك ›", url=f"t.me/ZXXCAQPBOT?startgroup=true",
                ),
            ],
            [
                InlineKeyboardButton("‹ دخول البوت ›", url=f"t.me/ZXXCAQPBOT"),
            ],
            ]
        ),
    )
