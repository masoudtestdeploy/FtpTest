from pyrogram import filters, Client
import pyrogram
import os
import ftplib
import re
import time 
import math 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

FTP_HOST = "130.185.79.172"
FTP_USER = "pz14205"
FTP_PASS = "12345678"
# connect to the FTP server
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
# force UTF-8 encoding
ftp.encoding = "utf-8"

def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + " days, ") if days else "") + \
        ((str(hours) + " hrs, ") if hours else "") + \
        ((str(minutes) + " min, ") if minutes else "") + \
        ((str(seconds) + " sec, ") if seconds else "") + \
        ((str(milliseconds) + " millisec, ") if milliseconds else "")
    return tmp[:-2]


def checkftp(text):
    ftp.cwd('./domains/pz14205.parspack.net/public_html/')
    files = []
    try:
        files = ftp.nlst()
    except ftplib.error_perm as resp:
        if str(resp) == "550 No files found":
            print ("No files in this directory")
        else:
            raise

    """for f in files:
        print (f)"""
    
    if text in files:
        #print ('|--------------------------------|')
        return "exist"
        #print ('|--------------------------------|')
    else:
        ftp.mkd(text)
        #print ('|--------------------------------|')
        return "make" 
        #print ('|--------------------------------|')


api_id = 2669389
api_hash = "59f112100d19186dc03cd93fb7f2904a"
bot_token = "5178142737:AAHRe5OeU6FdDYiZG2LqjEfr04rj_EVhKUM"

bot = Client(
    "withrap2",
    api_id=api_id, 
    api_hash=api_hash,
    bot_token=bot_token

)

PROGRESS_BAR = """\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗂️ : {1} | {2}
┣⪼ ⏳️ : {0}%
┣⪼ 🚀 : {3}/s
┣⪼ ⏱️ : {4}
╰━━━━━━━━━━━━━━━➣ """

async def progress_for_pyrogram(current, total, ud_type, message, start):

    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        # if round(current / total * 100, 0) % 5 == 0:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "{0}{1}".format(
            ''.join(["█" for i in range(math.floor(percentage / 5))]),
            ''.join(["░" for i in range(20 - math.floor(percentage / 5))]))
            
        tmp = progress + PROGRESS_BAR.format( 
            round(percentage, 2),
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            # elapsed_time if elapsed_time != '' else "0 s",
            estimated_total_time if estimated_total_time != '' else "0 s"
        )
        try:
            await message.edit(
                text="{}\n\n{}".format(ud_type, tmp),               
                reply_markup=InlineKeyboardMarkup( [[
                    InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="cancel")
                    ]]
                )
            )
        except:
            pass
        
@bot.on_message(filters.command("start"))
async def start_command(bot, message):
    await bot.send_message(message.chat.id , "سلام \n شروع مجدد : /start")
    
    

@bot.on_message(filters.private & (filters.document | filters.video | filters.photo | filters.audio))
async def gettttttttt(bots, message):
    
    media = message.document or message.video or message.audio or message.photo
    # text
    text = ""
    if not message.photo:
        text = "--**🗃️ Fɪʟᴇ Dᴇᴛᴀɪʟs:**--\n\n"
        text += f"📂 ** Fɪʟᴇ ɴᴀᴍᴇ :** `{media.file_name}`\n\n" if media.file_name else ""
        text += f"🍃 **Mɪᴍᴇ Tʏᴘᴇ:** __{media.mime_type}__\n\n" if media.mime_type else ""
        #text += f"📦 **Fɪʟᴇ ꜱɪᴢᴇ :** __{humanbytes(media.file_size)}__\n\n" if media.file_size else ""
        if not message.document:
            text += f"🎞 **Dᴜʀᴀᴛɪᴏɴ:** __{TimeFormatter(media.duration * 1000)}__\n\n" if media.duration else ""
            if message.audio:
                
                text += f"🎵 **Tɪᴛʟᴇ:** __{media.title}__\n\n" if media.title else ""
                text += f"🎙 **Pᴇʀғᴏʀᴍᴇʀ:** __{media.performer}__\n\n" if media.performer else ""
                

    text += f"**✏ Cᴀᴘᴛɪᴏɴ:** __{message.caption}__\n\n" if message.caption else ""
    #text += f"**🍁--Uᴘʟᴏᴀᴅᴇᴅ Bʏ :--** [{message.from_user.first_name}](tg://user?id={message.from_user.id}) \n\n"
    names = media.file_name
    await message.reply_text(text)
    
    # Proceed
    path = message.caption
    checkftp(path)
    ##if res == "exist":

    #chdir("./domains/pz14205.parspack.net/public_html/"+path)
    dl_loc = "./dl/" + str(message.from_user.id) + "/"
    if not os.path.isdir(dl_loc):
        os.makedirs(dl_loc)
    
    
    ms = await message.reply_text("𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳...")
    c_time = time.time()
    #file = message.message.reply_to_message
    the_media = await bot.download_media(
        message = message,
        file_name=dl_loc,
        progress=progress_for_pyrogram,
        progress_args=( "𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳....",  ms, c_time   )
    )
    #print (the_media)
    print('----------------')
    
    
    #filename = the_media
    print(f"{path}\n\n---------\n\n{the_media}\n\n---\n\n{names}")
    try:
        with open(the_media, "rb") as file:
            ftp.storbinary(f"STOR ./{path}/{names}", file)
            await message.reply_text(f"UPLOAD COPLETE \n\nhttps://s2.kenzodl.xyz/{path}/{names}")
    except : 
        await message.reply_text(f"ERROR UPLOAD COPLETE")
        
    ftp.quit()
    print ("ftp ok")
    

print ('im alive')
bot.run()
