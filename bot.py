from pyrogram import filters, Client
import os
import ftplib


FTP_HOST = "130.185.79.172"
FTP_USER = "pz14205"
FTP_PASS = "12345678"
# connect to the FTP server
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
# force UTF-8 encoding
ftp.encoding = "utf-8"

def chdir(dir): 
    if directory_exists(dir) is False: # (or negate, whatever you prefer for readability)
        ftp.mkd(dir)
    ftp.cwd(dir)

# Check if directory exists (in current location)
def directory_exists(dir):
    filelist = []
    ftp.retrlines('LIST',filelist.append)
    for f in filelist:
        if f.split()[-1] == dir and f.upper().startswith('D'):
            return True
    return False

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
    
    

@bot.on_message(filters.private & filters.regex(pattern=".*ftp.*"))
async def gettttttttt(c: Client, m: Message):
    await m.reply_text('لطفا کمی صبر کنید ...')
    pattern_link = re.compile(r'^\/ftp_(.*)')
    matches_link = pattern_link.search(str(m.text))
    namepath = matches_link.group(1)
    # Checks
    if (not m.reply_to_message) or (not m.reply_to_message.media) or (not get_file_attr(m.reply_to_message)):
        return await m.reply_text("Reply to any document/video/audio to rename it!", quote=True)
    # Proceed
    dl_loc = "./dl/" + str(cmd.from_user.id) + "/"
    if not os.path.isdir(dl_loc):
    	os.makedirs(dl_loc)
    the_media = await bot.download_media(
        message=cmd,
        file_name=dl_loc
    )
    print (the_media)
    print('----------------')
    print (m)
    print('----------------')
    print (c)
    #chdir("./domains/pz14205.parspack.net/public_html/"+namepath)
    #filename = the_media
    #with open(filename, "rb") as file:
        # use FTP's STOR command to upload the file
        #ftp.storbinary(f"STOR ./domains/pz14205.parspack.net/public_html/"+namepath, file)

   
print ('im alive')
bot.run()
