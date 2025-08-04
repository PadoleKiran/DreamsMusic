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

app = Client(
    "DreamsMusic",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
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
