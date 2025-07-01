from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiohttp import web
import os
import asyncio
import logging
from config import API_ID, API_HASH, BOT_TOKEN, SOURCE_CHANNEL, TARGET_CHANNEL, AUTOFILTER_BOT_USERNAME, HOW_TO_DOWNLOAD_URL

logging.basicConfig(level=logging.INFO)

# Pyrogram bot
app = Client("PosterBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ✅ Message Handler for Source Channel
@app.on_message(filters.chat(SOURCE_CHANNEL) & (filters.document | filters.video))
async def handle_file(client, message):
    try:
        file_name = message.document.file_name if message.document else message.video.file_name
        title = os.path.splitext(file_name)[0]

        caption = f"🎬 **{title}**\n\n📥 Click below to get the file."

        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("📥 Get File", url=f"https://t.me/{AUTOFILTER_BOT_USERNAME}?start={title.replace(' ', '%20')}")
            ],
            [
                InlineKeyboardButton("❓ How to Download", url=HOW_TO_DOWNLOAD_URL)
            ]
        ])

        await client.send_message(
            chat_id=TARGET_CHANNEL,
            text=caption,
            reply_markup=keyboard
        )
        logging.info(f"✅ Posted to target: {title}")

    except Exception as e:
        logging.error(f"❌ Error: {e}")


# 🌐 Keep-Alive Web Server (for Render/Koyeb)
async def handle_web(request):
    return web.Response(text="✅ Bot is Alive!")

async def start_web():
    app = web.Application()
    app.router.add_get("/", handle_web)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()
    print("🌐 Keep-alive server running on http://0.0.0.0:8080")


# 🏁 Run Both Bot + Web Server
async def main():
    await asyncio.gather(
        app.start(),
        start_web()
    )

if __name__ == "__main__":
    asyncio.run(main())
