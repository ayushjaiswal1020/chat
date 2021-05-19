from datetime import datetime
from os import environ
import aiohttp
from pyrogram import Client, filters


@bot.on_message(filters.command('ping') & filters.private)

async def _(event):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await asst.send_message(
        event.chat_id,
        f"**Pong!!**\n `{ms}ms`",
    )
