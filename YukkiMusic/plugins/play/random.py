import random
import os
import random
import requests
import asyncio
import re
from cgi import print_arguments
from pyrogram import Client, filters
from config import BANNED_USERS
from strings import get_command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from datetime import datetime
from sys import version_info
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import app
from YukkiMusic import settingsApp
from strings import get_command
from strings.filters import command

    
disable = []

flex = {}
chat_watcher_group = 3
         
         
@app.on_message(filters.command("تعطيل غنيلي", [".", ""]) & filters.group)
async def deslink(client, message):      
       a = await app.get_chat_member(message.chat.id, message.from_user.id)
       if message.chat.id in disable:
         return

       if not a.can_manage_chat:
         await message.reply_text("**- هذا الأمر يخص المشرفين بس !**")
        
       if a.can_manage_chat:
         disable.append(message.chat.id)
         await message.reply_text(f"- ابشر عيني {message.from_user.mention}\n**- تم تعطيل امر غنيلي**") 
         
         
@app.on_message(filters.command("تفعيل غنيلي", [".", ""]) & filters.group)
async def enablelink(client, message):      
       a = await app.get_chat_member(message.chat.id, message.from_user.id)
       if message.chat.id not in disable:
         return

       if not a.can_manage_chat:
         await message.reply_text("**- هذا الأمر يخص المشرفين بس !**")
        
       if a.can_manage_chat:
         disable.remove(message.chat.id)
         await message.reply_text(f"- ابشر عيني {message.from_user.mention}\n**- تم تفعيل امر غنيلي**")         
         
@app.on_message(filters.regex("^غنيلي$") & filters.group & ~filters.edited)
async def musicme(client, message):
       if message.chat.id in disable:
         return await message.reply_text("**- تم تعطيل امر غنيلي من قبل المشرفين**")
       if message.chat.id not in disable:
         rl = random.randint(2,277)
         url = f"https://t.me/vvooi4/{rl}"
         await message.reply_voice(url,caption="-› [• 𝐁𝙧𝙪𝙙 •](t.me/zzsvv)")
         


disable_A = []

flex = {}
chat_watcher_group = 3
         
         
@app.on_message(filters.command("تعطيل الافتارات", [".", ""]) & filters.group)
async def avtarB(client, message):      
       a = await app.get_chat_member(message.chat.id, message.from_user.id)
       if message.chat.id in disable_A:
         return

       if not a.can_manage_chat:
         await message.reply_text("**- هذا الأمر يخص المشرفين بس !**")
        
       if a.can_manage_chat:
         disable_A.append(message.chat.id)
         await message.reply_text(f"- ابشر عيني {message.from_user.mention}\n**- تم تعطيل اوامر الافتارات**") 
         
         
@app.on_message(filters.command("تفعيل الافتارات", [".", ""]) & filters.group)
async def AvtarT(client, message):      
       a = await app.get_chat_member(message.chat.id, message.from_user.id)
       if message.chat.id not in disable_A:
         return

       if not a.can_manage_chat:
         await message.reply_text("**- هذا الأمر يخص المشرفين بس !**")
        
       if a.can_manage_chat:
         disable_A.remove(message.chat.id)
         await message.reply_text(f"- ابشر عيني {message.from_user.mention}\n**- تم تفعيل اوامر الافتارات**")         
         
@app.on_message(filters.regex("^افتار بنات$") & filters.group & ~filters.edited)
async def ava(client, message):
       if message.chat.id in disable_A:
         return await message.reply_text("**- تم تعطيل امر افتار بنات من قبل المشرفين\n- للتفعيل اكتب تفعيل الافتارات**")
       if message.chat.id not in disable_A:
         rl = random.randint(3,289)
         url = f"https://t.me/vvooi2/{rl}"
         await message.reply_photo(url,caption="-› [• 𝐁𝙧𝙪𝙙 •](t.me/zzsvv)")
         
@app.on_message(filters.regex("^افتارات بنات$") & filters.group & ~filters.edited)
async def ava(client, message):
       if message.chat.id in disable_A:
         return await message.reply_text("**- تم تعطيل امر افتارات بنات من قبل المشرفين\n- للتفعيل اكتب تفعيل الافتارات**")
       if message.chat.id not in disable_A:
         rl = random.randint(3,289)
         url = f"https://t.me/vvooi2/{rl}"
         await message.reply_photo(url,caption="-› [• 𝐁𝙧𝙪𝙙 •](t.me/zzsvv)")
         
         
@app.on_message(filters.regex("^افتار ولد$") & filters.group & ~filters.edited)
async def ava(client, message):
       if message.chat.id in disable_A:
         return await message.reply_text("**- تم تعطيل امر افتار ولد من قبل المشرفين\n- للتفعيل اكتب تفعيل الافتارات**")
       if message.chat.id not in disable_A:
         rl = random.randint(3,117)
         url = f"https://t.me/vvooi5/{rl}"
         await message.reply_photo(url,caption="-› [• 𝐁𝙧𝙪𝙙 •](t.me/zzsvv)")
         
@app.on_message(filters.regex("^افتارات شباب$") & filters.group & ~filters.edited)
async def ava(client, message):
       if message.chat.id in disable_A:
         return await message.reply_text("**- تم تعطيل امر افتارات ولد من قبل المشرفين\n- للتفعيل اكتب تفعيل الافتارات**")
       if message.chat.id not in disable_A:
         rl = random.randint(3,589)
         url = f"https://t.me/vvooi5/{rl}"
         await message.reply_photo(url,caption="-› [• 𝐁𝙧𝙪𝙙 •](t.me/zzsvv)")
         
@app.on_message(filters.regex("^افتارات مكس$") & filters.group & ~filters.edited)
async def ava(client, message):
       if message.chat.id in disable_A:
         return await message.reply_text("**- تم تعطيل امر افتارات مكس من قبل المشرفين**")
       if message.chat.id not in disable_A:
         rl = random.randint(2,235)
         url = f"https://t.me/vvooi3/{rl}"
         await message.reply_photo(url,caption="-› [• 𝐁𝙧𝙪𝙙 •](t.me/zzsvv)")
         



disable_G = []

flex = {}
chat_watcher_group = 3



@app.on_message(filters.command("تعطيل الاقتباسات", [".", ""]) & filters.group)
async def aqtbas(client, message):      
       a = await app.get_chat_member(message.chat.id, message.from_user.id)
       if message.chat.id in disable_G:
         return

       if not a.can_manage_chat:
         await message.reply_text("**- هذا الأمر يخص المشرفين بس !**")
        
       if a.can_manage_chat:
         disable_G.append(message.chat.id)
         await message.reply_text(f"- ابشر عيني {message.from_user.mention}\n**- تم تعطيل الاقتباسات**") 
         
         
@app.on_message(filters.command("تفعيل الاقتباسات", [".", ""]) & filters.group)
async def aqty(client, message):      
       a = await app.get_chat_member(message.chat.id, message.from_user.id)
       if message.chat.id not in disable_G:
         return

       if not a.can_manage_chat:
         await message.reply_text("**- هذا الأمر يخص المشرفين بس !**")
        
       if a.can_manage_chat:
         disable_G.remove(message.chat.id)
         await message.reply_text(f"- ابشر عيني {message.from_user.mention}\n**- تم تفعيل الاقتباسات**")         
         
@app.on_message(filters.regex("^اقتباسات$") & ~filters.edited)
async def qw2(client,message):
       if message.chat.id in disable_G:
         return await message.reply_text("**- تم تعطيل امر الاقتباسات من قبل المشرفين**")
       if message.chat.id not in disable_G:
         rl = random.randint(1824,3267)
         url = requests.get(f"https://t.me/JuuuT/{rl}").text
         caption = re.findall(r'<meta property="og:description" content="(.*)">',str(url))
         await message.reply_text("-›" + str(caption[0]))





disable_h = []

flex = {}
chat_watcher_group = 3
         
         
@app.on_message(filters.command("تعطيل الشعر", [".", ""]) & filters.group)
async def hy1(client, message):      
       a = await app.get_chat_member(message.chat.id, message.from_user.id)
       if message.chat.id in disable_h:
         return

       if not a.can_manage_chat:
         await message.reply_text("**- هذا الأمر يخص المشرفين بس !**")
        
       if a.can_manage_chat:
         disable_h.append(message.chat.id)
         await message.reply_text(f"- ابشر عيني {message.from_user.mention}\n**- تم تعطيل امر شعر**") 
         
         
@app.on_message(filters.command("تفعيل الشعر", [".", ""]) & filters.group)
async def hy(client, message):      
       a = await app.get_chat_member(message.chat.id, message.from_user.id)
       if message.chat.id not in disable_h:
         return

       if not a.can_manage_chat:
         await message.reply_text("**- هذا الأمر يخص المشرفين بس !**")
        
       if a.can_manage_chat:
         disable_h.remove(message.chat.id)
         await message.reply_text(f"- ابشر عيني {message.from_user.mention}\n**- تم تفعيل امر شعر**") 



@app.on_message(filters.regex("^شعر$") & filters.group & ~filters.edited)
async def hyder(client, message):
       if message.chat.id in disable_h:
         return await message.reply_text("**- تم تعطيل امر الشعر من قبل المشرفين\n- للتفعيل اكتب تفعيل الشعر**")
       if message.chat.id not in disable_h:
         rl = random.randint(3,303)
         url = f"https://t.me/vvooi1/{rl}"
         await message.reply_voice(url,caption="-› [• 𝐁𝙧𝙪𝙙 •](t.me/zzsvv)")


@app.on_message(filters.regex("^ش$") & filters.group & ~filters.edited)
async def hyder1(client, message):
       if message.chat.id in disable_h:
         return await message.reply_text("**- تم تعطيل امر الشعر من قبل المشرفين\n- للتفعيل اكتب تفعيل الشعر**")
       if message.chat.id not in disable_h:
         rl = random.randint(3,303)
         url = f"https://t.me/vvooi1/{rl}"
         await message.reply_voice(url,caption="-› [• 𝐁𝙧𝙪𝙙 •](t.me/zzsvv)")
