from pyrogram import Client, filters

@Client.on_message(filters.command(["ping", "help"]))
async def extra_handler(client, message):
    if message.text == "/ping":
        await message.reply("🏓 Pong!")
    else:
        await message.reply("/play /pause /resume /stop /skip /auth /unauth /stats /queue /song /loop /speed /seek /broadcast etc.")
