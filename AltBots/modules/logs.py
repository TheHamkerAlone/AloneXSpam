from config import on_cmd, clients, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from telethon import events
import os

@on_cmd(r"logs(?: |$)(.*)")
async def logs(legend):
    if legend.sender_id == OWNER_ID:
        # On VPS, we can try to send the nohup.out or a specific log file if it exists
        log_file = "bot.log" # Assume we might be logging to bot.log
        if os.path.exists(log_file):
            try:
                if clients:
                    await clients[0].send_file(legend.chat_id, log_file, caption=f"⚡ **XBOTS LOGS (VPS)** ⚡")
            except Exception as e:
                await legend.reply(f"An Exception Occured!\n\n**ERROR:** {str(e)}")
        else:
            await legend.reply("» ɴᴏ ʟᴏɢ ꜰɪʟᴇ ꜰᴏᴜɴᴅ ᴏɴ ᴠᴘꜱ.")

    elif legend.sender_id in SUDO_USERS:
        await legend.reply("» ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")
