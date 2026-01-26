import os
import logging
from logging.handlers import RotatingFileHandler

# --- API & BOT TOKENS ---
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8583460812:AAEyTMW-JYP3_JIQSGsh3thPhMAoh2ZxArY")
API_ID = int(os.environ.get("API_ID", "32460404"))
API_HASH = os.environ.get("API_HASH", "410d526521ae7dcc474e0f4246788560")

# --- DATABASE & OWNER ---
OWNER_ID = int(os.environ.get("OWNER_ID", "5569039254"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://sonukumarkushvaha1_db_user:6w9MVqKN8wjNlqqS@cluster0.2eu5lot.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")

# --- CHANNELS (Set to None if not using) ---
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003626737474"))
FORCE_SUB_CHANNEL = None 
FORCE_SUB_LINK = os.environ.get("FORCE_SUB_LINK", "")

# --- SETTINGS ---
FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600"))
PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# --- ADMINS LOGIC ---
try:
    ADMINS = [6848088376, OWNER_ID]
    admin_env = os.environ.get("ADMINS", "6848088376")
    for x in admin_env.split():
        if int(x) not in ADMINS:
            ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# --- CUSTOMIZATION ---
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
PROTECT_CONTENT = os.environ.get('PROTECT_CONTENT', "False").lower() == "true"
DISABLE_CHANNEL_BUTTON = os.environ.get('DISABLE_CHANNEL_BUTTON', "True").lower() == "true"

# --- MESSAGES (Import Errors को रोकने के लिए ये सब यहाँ होने चाहिए) ---
START_MSG = os.environ.get("START_MESSAGE", "Hello {mention}\n\nI Can Store Private Files In Specified Channel.")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You Need To Join My Channel To Use Me.</b>") # यह लाइन वापस जोड़ दी गई है
BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !"

# --- LOGGING ---
LOG_FILE_NAME = "filesharingbot.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ]
)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
