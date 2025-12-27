import asyncio
import random
import logging
from aiogram import Router
from config import VERIFY_TIMEOUT
from aiogram.types import ChatMemberUpdated, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.enums import ChatMemberStatus

from services.restrict import restrict

router = Router()

pending = {}

EMOJIS = ["🔥", "🍕", "🐶", "🚀", "🎯", "🍀", "⭐"]

@router.chat_member()
async def on_chat_member_update(event: ChatMemberUpdated):
    old = event.old_chat_member.status
    new = event.new_chat_member.status
    chat_type = event.chat.type
    
    logging.info(f"Bot mode: {'FULL' if event.chat.type=='supergroup' else 'LIMITED'}")

    if new in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR):
        logging.info("Admin joined → bypass")
        return

    if chat_type != "supergroup":
        logging.info("Normal group detected → limited mode")
        return

    if old in (ChatMemberStatus.LEFT, ChatMemberStatus.KICKED) and new == ChatMemberStatus.MEMBER:
        user = event.new_chat_member.user
        chat_id = event.chat.id

        logging.info(f"New user joined (gatekeeper): {user.id}")

        await restrict(event.bot, chat_id, user.id)

        correct = random.choice(EMOJIS)
        wrong = random.sample([e for e in EMOJIS if e != correct], 2)
        options = wrong + [correct]
        random.shuffle(options)

        kb = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=e,
                        callback_data=f"verify:{user.id}:{e}"
                    ) for e in options
                ]
            ]
        )

        msg = await event.bot.send_message(
            chat_id,
            (
                f"👋 Welcome {user.mention_html()}!\n\n"
                f"Click the **{correct}** emoji to verify you're human."
            ),
            reply_markup=kb,
            parse_mode="HTML",
        )

        pending[(chat_id, user.id)] = {
            "message_id": msg.message_id,
            "answer": correct,
        }

        asyncio.create_task(
            verification_timeout(event.bot, chat_id, user.id, timeout=VERIFY_TIMEOUT)
        )

        logging.info(f"Verification timeout started for {user.id}")


async def verification_timeout(bot, chat_id: int, user_id: int, timeout: int = 60):
    await asyncio.sleep(timeout)

    key = (chat_id, user_id)
    data = pending.get(key)
    if not data:
        return

    logging.info(f"Verification timeout → kick {user_id}")

    try:
        await bot.ban_chat_member(chat_id, user_id)
        await bot.unban_chat_member(chat_id, user_id)
    except:
        pass

    try:
        await bot.delete_message(chat_id, data["message_id"])
    except:
        pass

    del pending[key]
