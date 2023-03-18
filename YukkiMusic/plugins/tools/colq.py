import asyncio
from pyrogram import filters, Client
from YukkiMusic import app
from YukkiMusic.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError)
from YukkiMusic.core.call import Yukki
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped

@app.on_message(filters.regex("^مين صاعد$|^مين بالاتصال$|^مين في الكول$"))
async def strcall(client, message):
    assistant = await group_assistant(Yukki,message.chat.id)
    try:
        await assistant.join_group_call(message.chat.id, AudioPiped("./assets/mody.mp3"), stream_type=StreamType().pulse_stream)
        text="الاعضاء المتواجدين في الاتصال:⇊\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut=f"◉{participant.volume}◉ ♡ يتحدث ◉"
            else:
                mut="◎ ♪ ساكت ◎"
            user = await client.get_users(participant.user_id)
            print(participant.user_id)
            k +=1
            text +=f"{k}➲{user.mention}{mut}\n"
        text += f"\nعددهم : {len(participants)}\n✓"    
        await message.reply(f"{text}")
        await asyncio.sleep(5)
        await assistant.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"عمري الاتصال مش مفتوح اصلااا\n✗")
    except AlreadyJoinedError:
        text="الاعضاء المتواجدين في الاتصال: ⇊\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut=f"◉{participant.volume}◉ ♡ يتحدث ◉"
            else:
                mut="◎ ♪ ساكت ◎"
            user = await client.get_users(participant.user_id)
            print(participant.user_id)
            k +=1
            text +=f"{k}➲{user.mention}{mut}\n"
        text += f"\nعددهم : {len(participants)}\n✓"
        await message.reply(f"{text}")
    except TelegramServerError:
        await message.reply(f"ارسل الامر تاني في مشكله في سيرفر التلجرام\n✗")
