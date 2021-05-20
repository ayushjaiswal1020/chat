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



@asst.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def on_new_mssg(event):
    incoming = event.raw_text
    who = event.sender_id
    if is_blacklisted(who):
        return
    # doesn't reply to that user anymore
    if incoming.startswith("/"):
        pass
    elif who == 997822204:
        return
    else:
        xx = await event.forward_to(997822204)
        udB.set(str(xx.id), str(who))


bot.run()
