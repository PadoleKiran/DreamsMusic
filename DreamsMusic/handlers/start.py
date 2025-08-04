from pyrogram import Client, filters

@Client.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply_text("DreamsMusic is alive! Send /help to see commands.")
