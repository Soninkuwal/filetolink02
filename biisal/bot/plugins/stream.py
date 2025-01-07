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


@StreamBot.on_message((filters.private) & (filters.document | filters.video | filters.audio | filters.photo), group=4)
async def private_receive_handler(c: Client, m: Message):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await c.send_message(
            Var.BIN_CHANNEL,
            f"New User Joined! : \n\nName : [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started Your Bot!!"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await c.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await c.send_message(
                    chat_id=m.chat.id,
                    text="You are banned!\n\n  **Contact Support [Support](https://t.me/SONICKUWALSSCBOT). They will help you.**",
                    disable_web_page_preview=True
                )
                return 
        except UserNotParticipant:
            await c.send_photo(
                chat_id=m.chat.id,
                photo="https://graph.org/file/95a9fc09cc310c0c8cd6f.jpg",
                caption="""<b>Hey there!\n\nPlease join our updates channel to use me! 😊\n\nDue to server overload, only our channel subscribers can use this bot!</b>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Now 🚩", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
            )
            return
        except Exception as e:
            await m.reply_text(e)
            await c.send_message(
                chat_id=m.chat.id,
                text="**Something went wrong. Contact my Support** [Support](https://telegram.me/SONICKUWALSSCBOT)",
                disable_web_page_preview=True
            )
            return
    ban_chk = await db.is_banned(int(m.from_user.id))
    if ban_chk:
        return await m.reply(Var.BAN_ALERT)
    try:
        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = f"{Var.URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        online_link = f"{Var.URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"

        await log_msg.reply_text(
            text=f"**Requested by:** [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n**User ID:** `{m.from_user.id}`\n**Stream Link:** {stream_link}",
            disable_web_page_preview=True,
            quote=True
        )
        await m.reply_text(
            text=msg_text.format(get_name(log_msg), humanbytes(get_media_file_size(m)), online_link, stream_link),
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("WATCH ONLINE 🔺", url=stream_link),
                        InlineKeyboardButton("FAST DOWNLOAD 🔻", url=online_link)
                    ],
                    [
                        InlineKeyboardButton("MX Player 🔹", url=f"intent://{stream_link}#Intent;package=com.mxtech.videoplayer.ad;end"),
                        InlineKeyboardButton("PlayIt Player 🔸", url=f"intent://{stream_link}#Intent;package=com.playit.videoplayer;end")
                    ]
                ]
            )
        )
    except FloodWait as e:
        print(f"Sleeping for {str(e.x)}s")
        await asyncio.sleep(e.x)
        await c.send_message(
            chat_id=Var.BIN_CHANNEL,
            text=f"Got FloodWait of {str(e.x)}s from [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**User ID:** `{str(m.from_user.id)}`",
            disable_web_page_preview=True
)


@StreamBot.on_message(filters.channel & ~filters.group & (filters.document | filters.video | filters.photo) & ~filters.forwarded, group=-1)
async def channel_receive_handler(bot, broadcast):
    if int(broadcast.chat.id) in Var.BAN_CHNL:
        print("Chat trying to get streaming link is found in BAN_CHNL, so not providing stream link")
        return
    ban_chk = await db.is_banned(int(broadcast.chat.id))
    if (int(broadcast.chat.id) in Var.BANNED_CHANNELS) or (ban_chk == True):
        await bot.leave_chat(broadcast.chat.id)
        return
    try:
        log_msg = await broadcast.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = f"{Var.URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        online_link = f"{Var.URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        await log_msg.reply_text(
            text=f"**Channel Name:** `{broadcast.chat.title}`\n**CHANNEL ID:** `{broadcast.chat.id}`\n**Requested URL:** {stream_link}",
            quote=True
        )
        await bot.edit_message_reply_markup(
            chat_id=broadcast.chat.id,
            message_id=broadcast.id,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("WATCH ONLINE 🔺", url=stream_link),
                     InlineKeyboardButton("FAST DOWNLOAD 🔻", url=online_link)],
                    [InlineKeyboardButton("MX Player 🔹", url=f"intent://{stream_link}#Intent;package=com.mxtech.videoplayer.ad;end"),
                     InlineKeyboardButton("PlayIt Player 🔸", url=f"intent://{stream_link}#Intent;package=com.playit.videoplayer;end")]
                ]
            )
        )
    except FloodWait as w:
        print(f"Sleeping for {str(w.x)}s")
        await asyncio.sleep(w.x)
        await bot.send_message(
            chat_id=Var.BIN_CHANNEL,
            text=f"GOT FLOODWAIT OF {str(w.x)}s FROM {broadcast.chat.title}\n\n**CHANNEL ID:** `{str(broadcast.chat.id)}`",
            disable_web_page_preview=True
        )
    except Exception as e:
        await bot.send_message(
            chat_id=Var.BIN_CHANNEL,
            text=f"**#ERROR_TRACEBACK:** `{e}`",
            disable_web_page_preview=True
        )
        print(f"Can't edit broadcast message!\nError: **Give me edit permission in updates and bin Channel! {e}**")
     
