import sys
from config import on_cmd, clients, OWNER_ID, SUDO_USERS, CMD_HNDLR as hl

from os import execl
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
