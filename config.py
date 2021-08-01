from os import getenv

from dotenv import load_dotenv

load_dotenv()

bot_token = getenv("BOT_TOKEN", "session")
ARQ_API_KEY = "XQYJAL-HTSZIK-YALWDS-TJPWMO-ARQ" 
api_id = getenv("API_ID", "api_id") 
api_hash = getenv("API_HASH", "api_hash")
LANGUAGE = "en"
ARQ_API_BASE_URL = "https://thearq.tech"
