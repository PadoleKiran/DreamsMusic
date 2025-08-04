from pytgcalls import PyTgCalls
from pyrogram import Client
from DreamsMusic.config import API_ID, API_HASH, BOT_TOKEN

client = Client("DreamsMusic", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
pytgcalls = PyTgCalls(client)

async def start_streaming():
    await pytgcalls.start()
