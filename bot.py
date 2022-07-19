from pyrogram import filters, Client
import os

api_id = 2669389
api_hash = "59f112100d19186dc03cd93fb7f2904a"
bot_token = "5178142737:AAHRe5OeU6FdDYiZG2LqjEfr04rj_EVhKUM"

bot = Client(
    "withrap2",
    api_id=api_id, 
    api_hash=api_hash,
    bot_token=bot_token

)


@bot.on_message(filters.command("start"))
async def start_command(bot, message):
    await bot.send_message(message.chat.id , "سلام \n شروع مجدد : /start")
    
    
    
@bot.on_message((filters.document | filters.video | filters.photo) & filters.private)
async def VidWatermarkAdder(bot, cmd):
    dl_loc = Config.DOWN_PATH + "/WatermarkAdder/" + str(cmd.from_user.id) + "/"
      if not os.path.isdir(dl_loc):
          os.makedirs(dl_loc)
    the_media = await bot.download_media(
        message=cmd,
        file_name=dl_loc
		)

