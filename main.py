import asyncio
import logging
from aiogram import Bot, Dispatcher
from routers import join, verify, service_cleanup

from config import BOT_TOKEN
from routers import join, verify

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logging.getLogger("aiogram").setLevel(logging.WARNING)
logging.getLogger("aiogram.event").setLevel(logging.WARNING)
logging.getLogger("aiogram.dispatcher").setLevel(logging.WARNING)
logging.getLogger("aiogram.client").setLevel(logging.WARNING)

async def main():
    logging.info("Starting Gatekeeper Bot...")

    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(join.router)
    dp.include_router(verify.router)
    dp.include_router(service_cleanup.router)

    logging.info("Bot started. Waiting for updates...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
