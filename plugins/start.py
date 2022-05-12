import traceback
import logging
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.types import User, Message
import os
import requests
import time
from pyrogram.errors import UserNotParticipant
import wget
import time
import math
import json
import string
import random
import traceback
import asyncio
import datetime
import aiofiles
from random import choice 
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, InputTextMessageContent
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid, UserNotParticipant, UserBannedInChannel
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid
from telegraph import upload_file
from youtube_search import YoutubeSearch
import requests
from pytube import YouTube
import youtube_dl
#IMPORT
import traceback
import logging
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.types import User, Message
import os
import requests
import time

from io import BytesIO
from traceback import format_exc
import aiohttp



force_subchannel = "GishanKrishka1_Cloud"

BROADCAST_AS_COPY = "True"

OWNER = "ImGishan"

START_IMG = "https://telegra.ph/file/490a71ad194e4d6ea95f0.jpg"

FORCESUB_TEXT = "**❌ Access Denied ❌**\n\n🌷You Must Join My Update Channel...🌷\n♻️Join it & Try Again.♻️"

FORCESUB_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton('༒❣️☢️╣IrØή❂mคŇ╠☢️❣️༒', url=f"https://t.me/{force_subchannel}")
                 ],
                 [
                 InlineKeyboardButton('◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』', url=f"https://t.me/{OWNER}")
                 ],
                 [
                 InlineKeyboardButton(text="♻️ Reload ♻️",callback_data="ref")
                 ]]
                  )


START_STRING =f"""
Hi , Welcome to ◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』's Pm Bot.
Use Help Button For More....
 By [◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』](https://t.me/{OWNER})
"""


START_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』', url=f"https://t.me/{OWNER}")
                 ],
                 [
                 InlineKeyboardButton(text="🌴 ʜᴇʟᴘ 🌴",callback_data="cmds")
                 ],
                 [
                 InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴜʀ ɢʀᴏᴜᴘ ➕", url="https://t.me/imgishan_Bot?startgroup=true")
                 ]]
                  )

HELP_BUTTONS = InlineKeyboardMarkup([[              
                 InlineKeyboardButton(text="🌻 ᴛᴇʟᴇɢʀᴀᴘʜ 🌻",callback_data="tgm")
                 ],
                 [
                 InlineKeyboardButton(text="🌻 ʟᴏɢᴏ 🌻",callback_data="logoc")
                 ],
                 [
                 InlineKeyboardButton(text="🌻 sᴏɴɢ 🌻",callback_data="songg")
                 ],
                 [
                 InlineKeyboardButton(text="🌻 ᴘɪᴄ ᴍᴇ 🌻",callback_data="pichel")
                 ],
                 [
                 InlineKeyboardButton(text="🌻 ǫʀ ɢᴇɴᴇʀᴀᴛᴏʀ 🌻",callback_data="qrg")
                 ],
                 [
                 InlineKeyboardButton(text="🍃 ʙᴀᴄᴋ 🍃",callback_data="bamk")            
                 ]]
                  )

GHELP_BUTTONS = InlineKeyboardMarkup([[              
                 InlineKeyboardButton(text="🌻 ᴛᴇʟᴇɢʀᴀᴘʜ 🌻",callback_data="htgm")
                 ],
                 [
                 InlineKeyboardButton(text="🌻 ʟᴏɢᴏ 🌻",callback_data="hlogoc")
                 ],
                 [
                 InlineKeyboardButton(text="🌻 sᴏɴɢ 🌻",callback_data="songg")
                 ],
                 [
                 InlineKeyboardButton(text="🌻 ᴘɪᴄ ᴍᴇ 🌻",callback_data="pichel")
                 ],
                 [
                 InlineKeyboardButton(text="🌻 ǫʀ ɢᴇɴᴇʀᴀᴛᴏʀ 🌻",callback_data="hqrg")
                 ],
                 [
                 InlineKeyboardButton(text="🍃 ʙᴀᴄᴋ 🍃",callback_data="hbamk")            
                 ]]
                  )

PICMEH_BUTTONS = InlineKeyboardMarkup([[              
                 InlineKeyboardButton(text="🌻 ᴛᴇʟᴇɢʀᴀᴘʜ 🌻",callback_data="ptgm")
                 ],
                 [
                 InlineKeyboardButton(text="🌻 ʟᴏɢᴏ 🌻",callback_data="plogoc")
                 ],
                 [
                 InlineKeyboardButton(text="🌻 sᴏɴɢ 🌻",callback_data="pongg")
                 ],
                 [
                 InlineKeyboardButton(text="🌻 ǫʀ ɢᴇɴᴇʀᴀᴛᴏʀ 🌻",callback_data="pqrg")
                 ],
                 [
                 InlineKeyboardButton(text="🍃 ʙᴀᴄᴋ 🍃",callback_data="picme")            
                 ]]
                  )
HHHELP_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="🍃 ʙᴀᴄᴋ 🍃",callback_data="hhbak")            
                 ]]
                  ) 
PICMEB_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="🍃 ʙᴀᴄᴋ 🍃",callback_data="ppbak")            
                 ]]
                  ) 
                 
BOT_USERNAME = "**@ImGishan_Bot**"
PM_TXT_ATT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"
PM_MED_ATT = "<b>Message from:</b> {} \n<b>Name:</b> {}"

TELEGRAPH = """
🍄Help for Telegraph Link Gen🍄
Available commands
✘ Send Eny Photo  - create Telegraph link
"""
PIC_HELP = """
🍄Help for Pic Me🍄
Available commands
✘ /picme - Cappture Ur Profrile Pic 
✘ /addchannel {Ur Channel Id} - Send Pic Me post To Channel or group
"""

LOGO_STRING = """
🍄Help for logo make🍄
Available commands
✘ /logo {text} - create simple random logos
✘ /logohq {text} - create simple random HQ logos
✘ /write{text} - create Note
"""
SONG_STRING = """
🍄Help for song download🍄
Available commands
✘ /song {song name} - Download a song simply.
✘ /song {youtube link} - Download song using youtube link
"""

QR_STRING = """🍄Help for QR Generator🍄
Available commands
✘ /qr {text} - Generate Qr simply.
"""

HELP_STRING = """
⚊❮❮❮❮ ｢  Still Wonder How I Work ? 」❯❯❯❯⚊
✘ Commands Available-
/song {song name}
/logo {text}
/logohq {text}
/write {text}
/qr {text}
Add Onother Features Soon
"""

BACK_BUTTON = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="🍃 ʙᴀᴄᴋ 🍃",callback_data="bamk")
                 ]]
                  )

HELPB_BUTTON = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="ʜᴇʟᴘ⁉️",callback_data="hcmds")
                 ]]
                  )


USER_DETAILS = "<b>PM FROM:</b>\nName: {} {}\nId: {}\nUname: @{}\nScam: {}\nRestricted: {}\nStatus: {}\nDc Id: {}"



picmebtns = InlineKeyboardMarkup([[
               InlineKeyboardButton("🌻 ᴘɪᴄ ᴍᴇ 🌻", callback_data="picme")
               ]]

             )
@Client.on_message(filters.sticker & filters.private)
async def help_me(bot, message):
    file_id = "CAADBQADEwUAAmjn4Vez7jrL1Cu2AAEC"
    await bot.send_sticker(message.chat.id, file_id)
    
@Client.on_message(filters.private & filters.command(["start"]))
async def help_me(bot, message):
    USER = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('USER', url=f"https://t.me/{message.from_user.username}")
                 ]]
                  )
    info = await bot.get_users(user_ids=message.from_user.id)
    USER_DETAILS = f"[{message.from_user.mention}](tg://user?id={message.from_user.id}) [`{message.from_user.id}`] Started Ur Bot.\n\n**PM FROM: `{info.first_name}`**\n**LastName: `{info.last_name}`**\n**Scam: `{info.is_scam}`**\n**Restricted: `{info.is_restricted}`**\n**Status:`{info.status}`**\n**Dc Id: `{info.dc_id}`**"
    await bot.send_message(-1001581011760, text=USER_DETAILS, reply_markup=USER)
    if force_subchannel:
        try:
            user = await bot.get_chat_member(force_subchannel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("Yourt Banned")
                return 
        except UserNotParticipant:
            text = FORCESUB_TEXT
            reply_markup = FORCESUB_BUTTONS
            await message.reply_text(
            text=text,
            reply_markup=reply_markup
            ) 
            return
    file_id = "CAADBQAD7AQAAgQ66VdlsI69XmFUkwI"
    await bot.send_sticker(message.chat.id, file_id)
    text = START_STRING
    reply_markup = START_BUTTON 
    text = START_STRING
    reply_markup = START_BUTTON   
    await message.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )
            
@Client.on_message(filters.command(["help", "help@ImGishan_Bot"]))  
async def tgm(bot, update):
    reply_markup = InlineKeyboardMarkup([[
                   InlineKeyboardButton(text="ʜᴇʟᴘ⁉️",callback_data="hcmds")
                   ]]
                   )
    await update.reply_text(
    text=f"Hi {update.from_user.mention}\n\n**» press the button below to read the explanation and see the list of available commands !**\n\n__⚡️ Powered by ⚡️__[◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』](t.me/imgishan)",
    reply_markup=reply_markup,
    disable_web_page_preview=True
    )  

