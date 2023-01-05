import asyncio
from pyrogram.types import Message
from pyrogram import Client, filters
from strings.filters import command, other_filters
from pyrogram.errors import UserAlreadyParticipant
from strings.decorators import authorized_users_only
from strings.callsmusic import client as user


@Client.on_message(
    command(["تعالا", "/assistant","انضم","خش","ادخل"]) & ~filters.private & ~filters.bot
)
@authorized_users_only
async def join_chat(c: Client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    try:
        invite_link = await m.chat.export_invite_link()
        if "+" in invite_link:
            link_hash = (invite_link.replace("+", "")).split("t.me/")[1]
            await user.join_chat(f"https://t.me/joinchat/{link_hash}")
        await m.chat.promote_member(
            (await user.get_me()).id,
            can_manage_voice_chats=True
        )
        return await user.send_message(chat_id, "🦦 تم انضمام الحساب المساعد")
    except UserAlreadyParticipant:
        admin = await m.chat.get_member((await user.get_me()).id)
        if not admin.can_manage_voice_chats:
            await m.chat.promote_member(
                (await user.get_me()).id,
                can_manage_voice_chats=True
            )
            return await user.send_message(chat_id, "🦦 موجود من زمان")
        return await user.send_message(chat_id, "🦦 موجود من زمان​")
