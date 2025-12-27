from aiogram import Router
from aiogram.types import CallbackQuery

from services.restrict import unrestrict
from routers.join import pending
from routers.service_cleanup import join_messages

router = Router()

@router.callback_query(lambda c: c.data.startswith("verify:"))
async def verify_user(call: CallbackQuery):
    _, user_id, emoji = call.data.split(":")
    user_id = int(user_id)
    chat_id = call.message.chat.id

    if call.from_user.id != user_id:
        await call.answer("This button is not for you.", show_alert=True)
        return

    key = (chat_id, user_id)
    data = pending.get(key)

    if not data:
        await call.answer("Verification expired.", show_alert=True)
        return

    if emoji != data["answer"]:
        await call.answer("❌ Wrong emoji. Try again.", show_alert=True)
        return

    del pending[key]

    await call.answer("✅ Verified! You can now chat.")
    await unrestrict(call.bot, chat_id, user_id)

    try:
        await call.message.delete()
    except:
        pass

    join_msg = join_messages.pop(chat_id, None)
    if join_msg:
        try:
            await call.bot.delete_message(chat_id, join_msg)
        except:
            pass
