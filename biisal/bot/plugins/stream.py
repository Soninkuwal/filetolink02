#(c) Adarsh-Goel
#(c) @biisal
import os
import asyncio
from asyncio import TimeoutError
from biisal.bot import StreamBot
from biisal.utils.database import Database
from biisal.utils.human_readable import humanbytes
from biisal.vars import Var
from urllib.parse import quote_plus
from pyrogram import filters, Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
#from utils_bot import get_shortlink

from biisal.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)


MY_PASS = os.environ.get("MY_PASS", None)
pass_dict = {}
pass_db = Database(Var.DATABASE_URL, "ag_passwords")

msg_text = """<b>YOUR LINK GENERATED ! 😉

‣ 𝙁𝙄𝙇𝙀 𝙉𝘼𝙈𝙀 💫 : <i>{}</i>

‣ 𝙁𝙄𝙇𝙀 𝙎𝙄𝙕𝙀 🤔 : {}

🔻 <a href="{}">𝗙𝗔𝗦𝗧 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗</a>
🔺 <a href="{}">𝗪𝗔𝗧𝗖𝗛 𝗢𝗡𝗟𝗜𝗡𝗘</a>

🔥 <a href="{}">𝗢𝗣𝗘𝗡 𝗜𝗡 𝗠𝗫 𝗣𝗟𝗔𝗬𝗘𝗥</a>
📽️ <a href="{}">𝗢𝗣𝗘𝗡 𝗜𝗡 𝗣𝗟𝗔𝗬𝗜𝗧 𝗣𝗟𝗔𝗬𝗘𝗥</a>

╔══════════════════╗
 [📌 JOIN MOVIE GROUP 🎭 ] 
   👇👇👇👇👇👇👇👇👇
<a href=https://t.me/SONICKUWALMOVIESWEBSERIES>JOIN MOVIE 🎥 GROUP</a>

 [📌 JOIN UPDATE CHANNEL ⚡]
👇👇👇👇👇👇👇👇
<a href=https://t.me/SONICKUWALUPDATEKANHA>JOIN UPDATED CHANNEL</a>
╚══════════════════╝

NOTES: 🌝 THIS FILE LINK ✅ NEVER DELETE ! 😃

‣ JOIN  <a href="https://t.me/SONICKUWALSSCBOT"> ⭐ TELEGRAM CHANNEL ⭐</a></b> 🤡"""

# Example usage in reply_markup
reply_markup = InlineKeyboardMarkup(
    [
        [  # Middle buttons
            InlineKeyboardButton("WATCH ONLINE 🔺", url="stream_link_placeholder"),
            InlineKeyboardButton("FAST DOWNLOAD 🔻", url="download_link_placeholder"),
        ],
        [  # MX Player and PlayIt Player buttons in the middle
            InlineKeyboardButton("OPEN IN MX PLAYER 🎥", url="mx_player_link_placeholder"),
            InlineKeyboardButton("OPEN IN PLAYIT PLAYER 📽️", url="playit_player_link_placeholder"),
        ],
        [  # Bottom buttons
            InlineKeyboardButton("JOIN MOVIE GROUP 🎭", url="https://t.me/SONICKUWALMOVIESWEBSERIES"),
            InlineKeyboardButton("JOIN UPDATE CHANNEL ⚡", url="https://t.me/SONICKUWALUPDATEKANHA"),
        ]
    ]
)




@StreamBot.on_message((filters.private) & (filters.document | filters.video | filters.audio | filters.photo) , group=4)
async def private_receive_handler(c: Client, m: Message):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await c.send_message(
            Var.BIN_CHANNEL,
            f"New User Joined! : \n\n Name : [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started Your Bot!!"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await c.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await c.send_message(
                    chat_id=m.chat.id,
                    text="You are banned!\n\n  **Cᴏɴᴛᴀᴄᴛ Support [Support](https://t.me/SONICKUWALSSCBOT) They Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**",
                    
                    disable_web_page_preview=True
                )
                return 
        except UserNotParticipant:
            await c.send_photo(
                chat_id=m.chat.id,
                photo="https://graph.org/file/95a9fc09cc310c0c8cd6f.jpg",
                caption=""""<b>Hᴇʏ ᴛʜᴇʀᴇ!\n\nPʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ ! 😊\n\nDᴜᴇ ᴛᴏ sᴇʀᴠᴇʀ ᴏᴠᴇʀʟᴏᴀᴅ, ᴏɴʟʏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ !</b>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jᴏɪɴ ɴᴏᴡ 🚩", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
            return
        except Exception as e:
            await m.reply_text(e)
            await c.send_message(
                chat_id=m.chat.id,
                text="**Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ. Cᴏɴᴛᴀᴄᴛ ᴍʏ Support** [Support](https://telegram.me/SONICKUWALSSCBOT)",
                
                disable_web_page_preview=True)
            return
    ban_chk = await db.is_banned(int(m.from_user.id))
    if ban_chk == True:
        return await m.reply(Var.BAN_ALERT)
try:
    log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
    stream_link = f"{Var.URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
    online_link = f"{Var.URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
    mx_player_link = f"intent://{Var.URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}#Intent;package=com.mxtech.videoplayer.ad;end;"
    playit_player_link = f"intent://{Var.URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}#Intent;package=com.playit.videoplayer;end;"

    await log_msg.reply_text(
        text=f"**RᴇQᴜᴇꜱᴛᴇᴅ ʙʏ :** [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n**Uꜱᴇʀ ɪᴅ :** `{m.from_user.id}`\n**Stream ʟɪɴᴋ :** {stream_link}",
        disable_web_page_preview=True,
        quote=True
    )
    await m.reply_text(
        text=msg_text.format(get_name(log_msg), humanbytes(get_media_file_size(m)), online_link, stream_link),
        quote=True,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("WATCH ONLINE 🔺", url=stream_link),  # Stream Link
                InlineKeyboardButton('FAST DOWNLOAD 🔻', url=online_link)  # Download Link
            ],
            [
                InlineKeyboardButton("OPEN IN MX PLAYER 🎥", url=mx_player_link),  # MX Player Link
                InlineKeyboardButton("OPEN IN PLAYIT PLAYER 📽️", url=playit_player_link)  # PlayIt Player Link
            ]
        ])
    )
except Exception as e:
    print(f"Error: {e}")
     

except FloodWait as e:
    wait_time = e.x
    user_name = m.from_user.first_name
    user_id = m.from_user.id

    # Log the FloodWait
    print(f"FloodWait triggered. Sleeping for {wait_time} seconds.")

    # Pause execution for the required duration
    await asyncio.sleep(wait_time)

    # Notify admins in BIN_CHANNEL
    await c.send_message(
        chat_id=Var.BIN_CHANNEL,
        text=(
            f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {wait_time}s from "
            f"[{user_name}](tg://user?id={user_id})\n\n"
            f"**𝚄𝚜𝚎𝚛 𝙸𝙳 :** `{user_id}`"
        ),
        disable_web_page_preview=True
 )



@StreamBot.on_message(filters.channel & ~filters.group & (filters.document | filters.video | filters.photo)  & ~filters.forwarded, group=-1)
async def channel_receive_handler(bot, broadcast):
    if int(broadcast.chat.id) in Var.BAN_CHNL:
        print("chat trying to get straming link is found in BAN_CHNL,so im not going to give stram link")
        return
    ban_chk = await db.is_banned(int(broadcast.chat.id))
    if (int(broadcast.chat.id) in Var.BANNED_CHANNELS) or (ban_chk == True):
        await bot.leave_chat(broadcast.chat.id)
        return
try:
    log_msg = await broadcast.forward(chat_id=Var.BIN_CHANNEL)
    stream_link = f"{Var.URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
    online_link = f"{Var.URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
    mx_player_link = f"intent://{Var.URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}#Intent;package=com.mxtech.videoplayer.ad;end;"
    playit_player_link = f"intent://{Var.URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}#Intent;package=com.playit.videoplayer;end;"

    await log_msg.reply_text(
        text=f"**Channel Name:** `{broadcast.chat.title}`\n**CHANNEL ID:** `{broadcast.chat.id}`\n**Rᴇǫᴜᴇsᴛ ᴜʀʟ:** {stream_link}",
        quote=True
    )
    await bot.edit_message_reply_markup(
        chat_id=broadcast.chat.id,
        message_id=broadcast.id,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("WATCH ONLINE 🔺", url=stream_link),
                    InlineKeyboardButton("FAST DOWNLOAD 🔻", url=online_link)
                ],
                [
                    InlineKeyboardButton("OPEN IN MX PLAYER 🎥", url=mx_player_link),
                    InlineKeyboardButton("OPEN IN PLAYIT PLAYER 📽️", url=playit_player_link)
                ]
            ]
        )
    )
except Exception as e:
    print(f"Error: {e}")
     
    except FloodWait as w:
        print(f"Sleeping for {str(w.x)}s")
        await asyncio.sleep(w.x)
        await bot.send_message(chat_id=Var.BIN_CHANNEL,
                            text=f"GOT FLOODWAIT OF {str(w.x)}s FROM {broadcast.chat.title}\n\n**CHANNEL ID:** `{str(broadcast.chat.id)}`",
                            disable_web_page_preview=True)
    except Exception as e:
        await bot.send_message(chat_id=Var.BIN_CHANNEL, text=f"**#ERROR_TRACKEBACK:** `{e}`", disable_web_page_preview=True)
        print(f"Cᴀɴ'ᴛ Eᴅɪᴛ Bʀᴏᴀᴅᴄᴀsᴛ Mᴇssᴀɢᴇ!\nEʀʀᴏʀ:  **Give me edit permission in updates and bin Channel!{e}**")

