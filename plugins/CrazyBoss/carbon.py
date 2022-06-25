from pyrogram import filters
from aiohttp import ClientSession
from pyrogram import Client as bot
from plugins.CrazyBoss.function import make_carbon
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
aiohttpsession = ClientSession()

C = "ʜᴇʏ 👋 {} ʏᴏᴜʀ ᴄᴀʀʙᴏɴ ɪs ʀᴇᴀᴅʏ 🤤"
F = InlineKeyboardMarkup(
[[
     InlineKeyboardButton("🔖 sᴜᴘᴘᴏʀᴛ 🕊️", url="https://t.me/NL_BOTxCHAT")
]]
)




@bot.on_message(filters.command("carbon"))
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴄᴀʀʙᴏɴ."
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴄᴀʀʙᴏɴ."
        )
    user_id = message.from_user.id
    m = await message.reply_text("ᴘʀᴏᴄᴇssɪɴɢ...")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("ᴜᴘʟᴏᴀᴅɪɴɢ..")
    await message.reply_photo(
        photo=carbon,
        caption=C.format(message.from_user.mention),
        reply_markup=F)
    await m.delete()
    carbon.close()
