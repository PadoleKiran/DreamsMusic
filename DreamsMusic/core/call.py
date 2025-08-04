<<<<<<< HEAD
from pytgcalls import PyTgCalls
from pyrogram import Client
from DreamsMusic.config import API_ID, API_HASH, BOT_TOKEN

client = Client("DreamsMusic", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
pytgcalls = PyTgCalls(client)

async def start_streaming():
    await pytgcalls.start()
=======
from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.input_stream import InputStream, AudioPiped
from DreamsMusic import app
from DreamsMusic.utils.logger import LOGGER


class DreamsPlayer:
    def __init__(self, client: Client):
        self.client = client
        self.call = PyTgCalls(client)

        @self.call.on_stream_end()
        async def on_stream_end(_, update: Update):
            LOGGER.info(f"Stream ended in chat: {update.chat_id}")
            # Add logic to handle end of stream

    async def start(self):
        await self.call.start()
        LOGGER.info("DreamsPlayer call started")

    async def join_and_play(self, chat_id: int, audio_url: str):
        await self.call.join_group_call(
            chat_id,
            InputStream(
                AudioPiped(audio_url)
            ),
        )
        LOGGER.info(f"Joined group call in {chat_id} with {audio_url}")

    async def leave(self, chat_id: int):
        await self.call.leave_group_call(chat_id)
        LOGGER.info(f"Left group call in {chat_id}")
>>>>>>> 6f44fcf168a5bb46336301c0e48b584e74efcfc4
