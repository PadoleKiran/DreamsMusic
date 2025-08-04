<<<<<<< HEAD
from DreamsMusic import config
from pyrogram import Client, idle
from DreamsMusic.core.call import start_streaming
=======
from pyrogram import Client
from DreamsMusic import config
from DreamsMusic.utils.logger import LOGGER
from DreamsMusic.core.call import DreamsPlayer

from DreamsMusic.handlers import (
    start,
    play,
    admin,
    auth,
    extra,
    broadcast,
    stats
)
>>>>>>> 6f44fcf168a5bb46336301c0e48b584e74efcfc4

app = Client(
    "DreamsMusic",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
<<<<<<< HEAD
    bot_token=config.BOT_TOKEN
)

async def main():
    await app.start()
    await start_streaming()
    print("DreamsMusic Bot Started.")
    await idle()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
=======
    bot_token=config.BOT_TOKEN,
    plugins={"root": "DreamsMusic/handlers"},
)

Dreams = DreamsPlayer(app)

if __name__ == "__main__":
    LOGGER.info("Starting DreamsMusic Bot...")
    app.start()
    Dreams.start()
    LOGGER.info("DreamsMusic Bot Started Successfully.")
    app.idle()
>>>>>>> 6f44fcf168a5bb46336301c0e48b584e74efcfc4
