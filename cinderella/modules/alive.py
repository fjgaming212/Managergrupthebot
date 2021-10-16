import re
import os

from telethon import events, Button
from telethon import version as tlhver
from innexiaBot.events import register
from innexiaBot import telethn as tbot

PHOTO = "https://telegra.ph/file/0fa4ac715b5cf0c76dc27.jpg"

@register(pattern=("/alive"))
async def awake(event):
  ken = event.sender.first_name
  SKYZU = "🍁 Holla I'm Gen Manager ! \n\n"
  SKYZU += "🍁 I'm Working Properly \n\n"
  SKYZU += "🍁 My Master : [Lord](https://t.me/FJ_GAMING) \n\n"
  SKYZU += f"🍁 Telethon Version : {tlhver} \n\n"
  SKYZU += f"🍁 Pyrogram Version : 1.5 \n\n"
  SKYZU += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/Yagura_Managerbot?start=help"), Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/Gen_Project_Support")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=SKYZU,  buttons=BUTTON)
