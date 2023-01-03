import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
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
    await client.send_dice(message.chat.id, "عيونها")
@app.on_message(command("بالناقص"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "منك! 🙂")
@app.on_message(command("بحبك"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "بس انا صغيرة!")
@app.on_message(command("احمد"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "ده مطوري")
@app.on_message(command("باي"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "الله معك")
@app.on_message(command("مرحبا"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "مرحبتين")
@app.on_message(command("دوم"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "تسلم/ي")
@app.on_message(command("صباحو"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "ورد")
@app.on_message(command("صلاح"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "ده صحبي")
@app.on_message(command("لجين"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "دي بنتي")
@app.on_message(command("ابو سليمان"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "ده حبيبي")
@app.on_message(command("ايمن"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "طنبخة")
@app.on_message(command("هاي"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "هايات")
@app.on_message(command("بولنغ"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "🎲")
@app.on_message(command("كيفكم"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "بخير وانت")
@app.on_message(command("رنا"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "دي عمري")
