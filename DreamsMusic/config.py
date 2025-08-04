import os
<<<<<<< HEAD

API_ID = int(os.getenv("API_ID", "12345"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "your_mongo_uri")
STRING_SESSION = os.getenv("STRING_SESSION", "")
=======
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URI = os.getenv("MONGO_URI", "")
OWNER_ID = int(os.getenv("OWNER_ID", ""))
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", ""))
STRING_SESSION = os.getenv("STRING_SESSION", None)
>>>>>>> 6f44fcf168a5bb46336301c0e48b584e74efcfc4
