from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonXMusic import app


start_txt = """
✦ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ !

̶꯭꯭⎯̶꯭̽❝꯭꯭💗꯭꯭꯭꯭᭄꯭꯭꯭🇹‌𝗵𝗮𝗻𝘂🇽‌𝗺𝘂𝘀𝗶𝗰🤍꯭᪳𝆺̶꯭𝅥⎯̶̶꯭̽

❅ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ˹ʙᴜɢ ✘ ϻʊsɪx ˼ ʙᴏᴛ ʀᴇᴘᴏ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/BTS_network_op"),
          InlineKeyboardButton("update", url="https://t.me/aboutBtschinna"),
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/9e170bd102c6198c4cfb9.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
