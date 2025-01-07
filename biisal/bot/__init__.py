from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import pyromod.listen
from ..vars import Var
from os import getcwd


# Initialize Bot Client
StreamBot = Client(
    name="Web Streamer",
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS
)

multi_clients = {}
work_loads = {}

async def generate_reply(log_msg, m):
    try:
        stream_link = f"{Var.URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        online_link = f"{Var.URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"

        # Validate the URLs
        if not (stream_link.startswith("http://") or stream_link.startswith("https://")):
            raise ValueError(f"Invalid stream link: {stream_link}")
        if not (online_link.startswith("http://") or online_link.startswith("https://")):
            raise ValueError(f"Invalid online link: {online_link}")

        # Properly format the text
        msg_text = "**Name:** {}\n**Size:** {}\n**Stream:** {}\n**Download:** {}"
        msg_body = msg_text.format(
            get_name(log_msg),
            humanbytes(get_media_file_size(m)),
            online_link,
            stream_link
        )

        # Send Reply with Buttons
        await m.reply_text(
            text=msg_body,
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("WATCH ONLINE 🔺", url=stream_link),
                     InlineKeyboardButton("FAST DOWNLOAD 🔻", url=online_link)]
                ]
            )
        )
    except ValueError as ve:
        # Log invalid URLs for debugging
        print(f"URL Error: {ve}")
        await m.reply_text("An error occurred while generating the link. Please try again later.")
    except Exception as e:
        # Catch other unexpected errors
        print(f"Error: {e}")
        await m.reply_text("An unexpected error occurred. Please try again later.")
