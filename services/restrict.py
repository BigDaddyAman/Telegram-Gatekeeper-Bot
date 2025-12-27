from aiogram import Bot
from aiogram.types import ChatPermissions

READ_ONLY = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False,
    can_send_polls=False,
    can_send_other_messages=False,
)

FULL = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_send_other_messages=True,
)

async def restrict(bot: Bot, chat_id: int, user_id: int):
    try:
        await bot.restrict_chat_member(chat_id, user_id, READ_ONLY)
    except Exception:
        pass

async def unrestrict(bot: Bot, chat_id: int, user_id: int):
    try:
        await bot.restrict_chat_member(chat_id, user_id, FULL)
    except Exception:
        pass
