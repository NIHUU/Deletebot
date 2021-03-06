import re
from pyrogram import filters, Client
from pyrogram.errors.exceptions.bad_request_400 import ChannelInvalid, UsernameInvalid, UsernameNotModified
from info import ADMINS, LOG_CHANNEL, FILE_STORE_CHANNEL, PUBLIC_FILE_STORE
from database.ia_filterdb import unpack_new_file_id
from utils import temp
import re
import os
import json
import base64
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

async def allowed(_, __, message):
    if PUBLIC_FILE_STORE:
        return True
    if message.from_user and message.from_user.id in ADMINS:
        return True
    return False

@Client.on_message(filters.command(['link', 'plink']) & filters.create(allowed))
async def gen_link_s(bot, message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply('ππ΄πΏπ»π ππΎ π° πΌπ΄πππ°πΆπ΄ πΎπ π° π΅πΈπ»π΄. πΈ ππΈπ»π» πΆπΈππ΄ ππΎπ π° ππ·π°ππ°π±π»π΄ πΏπ΄ππΌπ°π½π΄π½π π»πΈπ½πΊ')
    file_type = replied.media
    if file_type not in ["video", 'audio', 'document']:
        return await message.reply("ππ΄πΏπ»π ππΎ π° πππΏπΏπΎπππ΄π³ πΌπ΄π³πΈπ°")
    if message.has_protected_content and message.chat.id not in ADMINS:
        return await message.reply("πΎπΊ π±ππΎ")
    file_id, ref = unpack_new_file_id((getattr(replied, file_type)).file_id)
    string = 'filep_' if message.text.lower().strip() == "/plink" else 'file_'
    string += file_id
    outstr = base64.urlsafe_b64encode(string.encode("ascii")).decode().strip("=")
    await message.reply(f"<b>βͺΌ π·π΄ππ΄ πΈπ ππΎππ π»πΈπ½πΊ:</b>\n\nhttps://t.me/{temp.U_NAME}?start={outstr}")
    
   
