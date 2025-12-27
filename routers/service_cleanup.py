from aiogram import Router
from aiogram.types import Message

router = Router()

join_messages = {}  

@router.message()
async def capture_service_messages(msg: Message):
    if msg.new_chat_members:
        join_messages[msg.chat.id] = msg.message_id

    elif msg.left_chat_member:
        join_messages[msg.chat.id] = msg.message_id
