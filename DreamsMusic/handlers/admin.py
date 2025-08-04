from pyrogram import Client, filters

@Client.on_message(filters.command(["pause", "resume", "stop", "skip", "end", "restart"]))
async def admin_handler(client, message):
    await message.reply_text(f"{message.command[0].capitalize()} command executed.")
