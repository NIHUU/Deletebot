#@Aadhi000 #AVR #neo

import asyncio
import os
import math
import time
import requests
from pyrogram import Client, filters

#=====================================================
BOT_START_TIME = time.time()
#=====================================================

@Client.on_message(filters.command("ping"))
async def ping(_, message):
    start_t = time.time()  
    avr = await message.reply_text("•••")  
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    uptime = time.strftime("%Hh | %Mm | %Ss", time.gmtime(time.time() - BOT_START_TIME))   
    await avr.edit(f"-𝙲𝚄𝚁𝚁𝙴𝙽𝚃 𝙱𝙾𝚃 𝚂𝚃𝙰𝚃𝚄𝚂-\n\n‹› 𝙿𝙾𝙽𝙶! : {time_taken_s:.3f} ms\n‹› 𝙱𝙾𝚃 𝚄𝙿𝚃𝙸𝙼𝙴 : {uptime}")
    await asyncio.sleep(10)
    await avr.delete()
