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
      Startt = "- صعدوا نسمع أغاني 🥲"
      await message.reply_text(Startt)

@app.on_message(filters.voice_chat_ended)
async def bablo(client: Client, message: Message): 
      Enddd = "- أصلاً مليت 🙂"
      await message.reply_text(Enddd)

      
@app.on_message(command("ايما"))
async def throw_dice(client, message: Message): 
    await message.reply_text("عيونها")
@app.on_message(command("ايدي"))
async def throw_dice(client, message: Message): 
    await message.reply_text(f"ايدي الكروب :```{message.chat.id}```")
@app.on_message(command("بالناقص"))
async def throw_dice(client, message: Message): 
    await message.reply_text("منك! 🙂")
@app.on_message(command("بحبك"))
async def throw_dice(client, message: Message): 
    await message.reply_text("بس انا صغيرة!")
@app.on_message(command("هههه"))
async def throw_dice(client, message: Message): 
    await message.reply_text("تؤبرني هالضحكة 🫂🤍")
@app.on_message(command("باي"))
async def throw_dice(client, message: Message): 
    await message.reply_text("الله معك 🤝")
@app.on_message(command("مرحبا"))
async def throw_dice(client, message: Message): 
    await message.reply_text("مرحبتين 🤝")
@app.on_message(command("دوم"))
async def throw_dice(client, message: Message): 
    await message.reply_text("تسلم/ي")
@app.on_message(command("صباحو"))
async def throw_dice(client, message: Message): 
    await message.reply_text("ورد 💞")
@app.on_message(command("هلو"))
async def throw_dice(client, message: Message): 
    await message.reply_text("هلوات 🙁")
@app.on_message(command("ازيك"))
async def throw_dice(client, message: Message): 
    await message.reply_text("بخير وانت/ي ؟")
@app.on_message(command("🤣🤣"))
async def throw_dice(client, message: Message): 
    await message.reply_text("مستفز 🙂")
@app.on_message(command("🥲🥲"))
async def throw_dice(client, message: Message): 
    await message.reply_text("دخيلو الكيوت 🥲")
@app.on_message(command("هاي"))
async def throw_dice(client, message: Message): 
    await message.reply_text("هايات 🙃")
@app.on_message(command("بولنغ"))
async def throw_dice(client, message: Message): 
    await message.reply("🎲")
@app.on_message(command("كيفكم"))
async def throw_dice(client, message: Message): 
    await message.reply_text("بخير وانت ؟")
@app.on_message(command("محمد"))
async def throw_dice(client, message: Message): 
    await message.reply_text("عليه أفضل الصلاة والسلام")
@app.on_message(command("خاص"))
async def throw_dice(client, message: Message): 
    await message.reply_text("واللهي يبتاع الخاص قلبي تعب وعقلي تعب وأي ياي ياي .")
@app.on_message(command("تصبحو ع خير"))
async def throw_dice(client, message: Message): 
    await message.reply_text("وانت بخير يا نور عيوني .")
@app.on_message(command("ايمااا"))
async def throw_dice(client, message: Message): 
    await message.reply_text("قليل ذوق لا تعيط!!")
@app.on_message(command("بتحبيني"))
async def throw_dice(client, message: Message): 
    await message.reply_text("طبعا بحبك لك ابرنييي 🤍🫂")
@app.on_message(command("🙂🙂"))
async def throw_dice(client, message: Message): 
    await message.reply_text("الغزال منكد؟")
@app.on_message(command("😍😍"))
async def throw_dice(client, message: Message): 
    await message.reply_text("حبيت؟")
@app.on_message(command("تفه"))
async def throw_dice(client, message: Message): 
    await message.reply_text("قلة ذوق ترا ؟")
@app.on_message(command("تفو"))
async def throw_dice(client, message: Message): 
    await message.reply_text("قليل ادب 🙂.")

@app.on_message(command(["غنيلي"])
    & filters.group
    & ~filters.edited
)
async def ahmad(client: Client, message: Message):
    await message.reply_voice(
        voice="https://t.me/sspaa/177",
        caption=f"""- Voice : JRO7I 🎙.
- Jo!N : @sspaa 📡.""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("‹ ضيفني لكروبك ›", url=f"https://t.me/AprilMubot?startgroup=true",
                ),
            ]
        ),
    )
