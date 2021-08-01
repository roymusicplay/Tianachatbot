import os

from heroku3 import from_key
from pyrogram import Client
from pyromod import listen

api_id = int(os.environ.get("API_ID", 0))
api_hash = os.environ.get("API_HASH", None)
bot_token = os.environ.get("BOT_TOKEN", None)
ARQ_API_KEY = "XQYJAL-HTSZIK-YALWDS-TJPWMO-ARQ" 
LANGUAGE = "en"
ARQ_API_BASE_URL = "https://thearq.tech"

bot = Client(":memory:",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)
