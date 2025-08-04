from DreamsMusic import config
from pyrogram import Client, idle
from DreamsMusic.core.call import start_streaming

app = Client(
    "DreamsMusic",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
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
