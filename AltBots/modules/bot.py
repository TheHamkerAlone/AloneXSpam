import sys
try:
    import heroku3
except ImportError:
    heroku3 = None

from config import on_cmd, clients, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl

from os import execl, getenv
from datetime import datetime


@on_cmd(r"ping(?: |$)(.*)")
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        altron = await e.reply(f"» __ᴀʟᴏɴᴇ__")
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await altron.edit(f"__🤖 ᴘɪɴɢ__\n» `{mp} ᴍꜱ`")


@on_cmd(r"reboot(?: |$)(.*)")
async def restart(e):
    if e.sender_id in SUDO_USERS:
        await e.reply(f"`ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
        for client in clients:
            try:
                await client.disconnect()
            except Exception:
                pass

        execl(sys.executable, sys.executable, *sys.argv)


@on_cmd(r"sudo(?: |$)(.*)")
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        if not heroku3:
            await event.reply("» `heroku3` ʟɪʙʀᴀʀʏ ɪꜱ ᴍɪꜱꜱɪɴɢ !!")
            return

        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default="")

        ok = await event.reply(f"» __ᴀᴅᴅɪɴɢ ᴜꜱᴇʀ ᴀꜱ ꜱᴜᴅᴏ...__")
        target = ""
        if HEROKU_APP_NAME is not None:
            try:
                app = Heroku.app(HEROKU_APP_NAME)
            except Exception as e:
                await ok.edit(f"**HEROKU ERROR:** `{e}`")
                return
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ !!")
            return

        if str(target) in sudousers:
            await ok.edit(f"ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ !!")
        else:
            if len(sudousers) > 0:
                newsudo = f"{sudousers} {target}"
            else:
                newsudo = f"{target}"
            await ok.edit(f"» **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ**: `{target}`\n» `ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
            heroku_var["SUDO_USERS"] = newsudo    
    
    elif event.sender_id in SUDO_USERS:
        await event.reply("» ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")
