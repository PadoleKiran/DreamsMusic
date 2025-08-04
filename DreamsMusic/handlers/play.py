from pyrogram import Client, filters

@Client.on_message(filters.command("play"))
async def play_handler(client, message):
    await message.reply_text("Playing requested song...")
