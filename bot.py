from os import environ
import aiohttp
from pyrogram import Client, filters


from datetime import datetime


from telethon import Button, events
from telethon.utils import get_display_name

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')

bot = Client('Chatcat bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)

@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
await message.reply(
              f"**Hey there {message.chat.first_name}, this is Assistant of MJBhai!**\n\n"
              "You can contact my boss using this bot!! \n\n Send your Message, I will Deliver it to my Boss.")

bot.run()
