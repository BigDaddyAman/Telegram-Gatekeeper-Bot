# Telegram Gatekeeper Bot

A Telegram bot that verifies new users when they join a group and
automatically removes unverified users after a timeout.

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/kbVNI2?referralCode=nIQTyp&utm_medium=integration&utm_source=template&utm_campaign=generic)

---

## ✨ Features

- 🛡️ Restricts new users on join (supergroups)
- 😀 Emoji-based human verification
- ⏱️ Auto-kicks users who fail to verify in time
- 👮 Admins are automatically bypassed
- 🧹 Cleans up join / leave / kick service messages
- 🔄 Automatically detects group type (supergroup vs normal group)

---

## ℹ️ Group Type Behavior

Telegram has different capabilities for normal groups and supergroups.
This bot automatically detects the group type and adjusts its behavior.

- ✅ **Supergroup** → Full gatekeeper protection (verification, timeout, cleanup)
- ⚠️ **Normal group** → Limited mode (no user restrictions)

To enable full protection, convert your group into a supergroup:
- Make the group public (set a username), or
- Let Telegram auto-upgrade it automatically

## 🚀 Deploy on Railway

Click the button below to deploy instantly:

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/kbVNI2?referralCode=nIQTyp&utm_medium=integration&utm_source=template&utm_campaign=generic)

### Required Environment Variables

| Variable | Description |
|--------|------------|
| BOT_TOKEN | Telegram bot token from @BotFather |
| VERIFY_TIMEOUT | Seconds before kicking unverified users (default: 60) |

---

## 🤖 Bot Setup

1. Create a bot using **@BotFather**
2. Copy the bot token
3. Deploy this project on Railway
4. Set the BOT_TOKEN environment variable
5. Add the bot to your Telegram group as **admin**
6. Grant permissions:
   - Restrict users
   - Ban users
   - Delete messages

---

## 🧪 How It Works

1. User joins the group
2. Bot restricts the user
3. Emoji verification message is sent
4. User clicks the correct emoji
5. Restrictions are removed
6. If the user does nothing → bot kicks them after the timeout

---

## 🛠️ Local Development (Optional)

```bash
pip install -r requirements.txt
export BOT_TOKEN=your_token_here
python main.py
```

---

## 📜 License

MIT License
