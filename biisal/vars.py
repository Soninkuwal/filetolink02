# (c) adarsh-goel (c) @biisal
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()
bot_name = "KANHA FILES TO LINK 🖇️ BOT"
kanha_channel = "https://t.me/Sonickuwalupdate"
kanha_grp = "https://t.me/SONICKUWALMOVIE"

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '20945078'))
    API_HASH = str(getenv('API_HASH', '93f6b8ce4bb0ab61b4c7e42187f2aa64'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , '6785205860:AAGjdRAPWKS-k0yGf5SLMqvw8xnbdYY09ME'))
    name = str(getenv('name', 'kanha_file2link_bot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002049098708'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', '-1002049098708'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = [int(x) for x in os.environ.get("OWNER_ID", "1664376941").split()]
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'kanhaiyalalmeenakuwal'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "https://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://filetostream:MtaWgRRLBqd2qC2a@filetostream.fpwbtsy.mongodb.net/?retryWrites=true&w=majority&appName=filetostream'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'Sonickuwalupdate')) 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "-1002049098708")).split()))   
    BAN_ALERT = str(getenv('BAN_ALERT' , '<b>ʏᴏᴜʀ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.Pʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ @Sonickuwalupdate ᴛᴏ ʀᴇsᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇ!!</b>'))
