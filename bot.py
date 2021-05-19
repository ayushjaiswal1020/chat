from os import environ
import aiohttp
from pyrogram import Client, filters

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
API_KEY = environ.get('API_KEY', 'c3398d623ffc9ab6de497e37d6938e280ed7a474')

bot = Client('gplink bot',
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


from datetime import datetime
from os import environ
import aiohttp
from pyrogram import Client, filters


@bot.on_message(filters.command('ping') & filters.private)

async def _(event):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await message.reply(
        event.chat_id,
        f"**Pong!!**\n `{ms}ms`",
    )


bot.run()
