import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
VERIFY_TIMEOUT = int(os.getenv("VERIFY_TIMEOUT", "60"))

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is required")
