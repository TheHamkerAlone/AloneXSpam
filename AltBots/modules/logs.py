import asyncio
try:
    import heroku3
except ImportError:
    heroku3 = None

from config import on_cmd, clients, SUDO_USERS, OWNER_ID, HEROKU_API_KEY, HEROKU_APP_NAME, CMD_HNDLR as hl

from datetime import datetime


@on_cmd(r"logs(?: |$)(.*)")
async def logs(legend):
    if legend.sender_id == OWNER_ID:
        if not heroku3:
            await legend.reply("» `heroku3` ʟɪʙʀᴀʀʏ ɪꜱ ᴍɪꜱꜱɪɴɢ !!")
            return

        if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
            await legend.reply(
                "First Set These Vars In Heroku :  `HEROKU_API_KEY` And `HEROKU_APP_NAME`.",
            )
            return

        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            app = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            await legend.reply(
                "Make Sure Your Heroku API Key & App Name Are Configured Correctly In Heroku."
            )
            return

        try:
            logs = app.get_log()
        except Exception as e:
            await legend.reply(f"**HEROKU ERROR:** `{e}`")
            return

        start = datetime.now()
        fetch = await legend.reply(f"__Fetching Logs...__")
    
        with open("AltLogs.txt", "w") as logfile:
            logfile.write("⚡ XBOTS ⚡ [ Bot Logs ]\n\n" + logs)

        end = datetime.now()
        ms = (end-start).seconds
        await asyncio.sleep(1)

        try:
            if clients:
                await clients[0].send_file(legend.chat_id, "AltLogs.txt", caption=f"⚡ **XBOTS LOGS** ⚡\n  » **ᴛɪᴍᴇ ᴛᴀᴋᴇɴ:** `{ms} ꜱᴇᴄᴏɴᴅꜱ`")
            await fetch.delete()
        except Exception as e:
            await fetch.edit(f"An Exception Occured!\n\n**ERROR:** {str(e)}")

    elif legend.sender_id in SUDO_USERS:
        await legend.reply("» ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")
