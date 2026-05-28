import asyncio
from random import choice
from telethon import errors
from config import on_cmd, on_msg, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from AltBots.data import RAID, REPLYRAID, ALTRON, MRAID, SRAID, CRAID

REPLY_RAID = []

@on_cmd(r"raid(?: |$)(.*)")
async def raid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)
        uid = None

        if len(xraid) == 3:
            try:
                entity = await e.client.get_entity(xraid[2])
                uid = entity.id
            except Exception:
                await e.reply("» ᴄᴀɴ'ᴛ ꜰɪɴᴅ ᴜꜱᴇʀ.")
                return

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            uid = a.sender_id
            entity = await e.client.get_entity(uid)

        if not uid:
             await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐑𝐚𝐢𝐝\n  » {hl}raid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}raid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
             return

        try:
            if uid in ALTRON:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀʟᴛʀᴏɴ'ꜱ ᴏᴡɴᴇʀ.")
            elif uid == OWNER_ID:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ.")
            elif uid in SUDO_USERS:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ.")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(RAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        except errors.FloodWaitError as f:
            await asyncio.sleep(f.seconds)
        except (IndexError, ValueError):
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐑𝐚𝐢𝐝\n  » {hl}raid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}raid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(f"Error in raid: {e}")

@on_msg()
async def _(event):
    global REPLY_RAID
    check = f"{event.sender_id}_{event.chat_id}"
    if check in REPLY_RAID:
        try:
            await asyncio.sleep(0.1)
            await event.client.send_message(
                entity=event.chat_id,
                message="""{}""".format(choice(REPLYRAID)),
                reply_to=event.message.id,
            )
        except errors.FloodWaitError as f:
            await asyncio.sleep(f.seconds)
        except Exception:
            pass

@on_cmd(r"rraid(?: |$)(.*)")
async def rraid(e):
    if e.sender_id in SUDO_USERS:
        mkrr = e.text.split(" ", 1)
        entity = None
        if len(mkrr) == 2:
            try:
                entity = await e.client.get_entity(mkrr[1])
            except Exception:
                await e.reply("» ᴄᴀɴ'ᴛ ꜰɪɴᴅ ᴜꜱᴇʀ.")
                return

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            try:
                entity = await e.client.get_entity(a.sender_id)
            except Exception:
                await e.reply("» ᴄᴀɴ'ᴛ ꜰɪɴᴅ ᴜꜱᴇʀ.")
                return

        if not entity:
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  » {hl}rraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}rraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
            return

        try:
            user_id = entity.id
            if user_id in ALTRON:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀʟᴛʀᴏɴ'ꜱ ᴏᴡɴᴇʀ.")
            elif user_id == OWNER_ID:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ.")
            elif user_id in SUDO_USERS:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ.")
            else:
                global REPLY_RAID
                check = f"{user_id}_{e.chat_id}"
                if check not in REPLY_RAID:
                    REPLY_RAID.append(check)
                await e.reply("» ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ !! ✅")
        except Exception as e:
            print(f"Error in rraid: {e}")

@on_cmd(r"drraid(?: |$)(.*)")
async def drraid(e):
    if e.sender_id in SUDO_USERS:
        text = e.text.split(" ", 1)
        entity = None

        if len(text) == 2:
            try:
                entity = await e.client.get_entity(text[1])
            except Exception:
                await e.reply("» ᴄᴀɴ'ᴛ ꜰɪɴᴅ ᴜꜱᴇʀ.")
                return
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            try:
                entity = await e.client.get_entity(a.sender_id)
            except Exception:
                await e.reply("» ᴄᴀɴ'ᴛ ꜰɪɴᴅ ᴜꜱᴇʀ.")
                return

        if not entity:
             await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐃𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  » {hl}drraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}drraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
             return

        try:
            check = f"{entity.id}_{e.chat_id}"
            global REPLY_RAID
            if check in REPLY_RAID:
                REPLY_RAID.remove(check)
            await e.reply("» ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ !! ✅")
        except Exception as e:
            print(f"Error in drraid: {e}")

@on_cmd(r"mraid(?: |$)(.*)")
async def mraid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)
        uid = None
        if len(xraid) == 3:
            try:
                entity = await e.client.get_entity(xraid[2])
                uid = entity.id
            except: pass
        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            uid = a.sender_id
            entity = await e.client.get_entity(uid)

        if uid:
            try:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(MRAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
            except errors.FloodWaitError as f:
                await asyncio.sleep(f.seconds)
            except Exception as ex:
                print(ex)

@on_cmd(r"sraid(?: |$)(.*)")
async def sraid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)
        uid = None
        if len(xraid) == 3:
            try:
                entity = await e.client.get_entity(xraid[2])
                uid = entity.id
            except: pass
        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            uid = a.sender_id
            entity = await e.client.get_entity(uid)

        if uid:
            try:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(SRAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
            except errors.FloodWaitError as f:
                await asyncio.sleep(f.seconds)
            except Exception as ex:
                print(ex)

@on_cmd(r"craid(?: |$)(.*)")
async def craid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)
        uid = None
        if len(xraid) == 3:
            try:
                entity = await e.client.get_entity(xraid[2])
                uid = entity.id
            except: pass
        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            uid = a.sender_id
            entity = await e.client.get_entity(uid)

        if uid:
            try:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(CRAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
            except errors.FloodWaitError as f:
                await asyncio.sleep(f.seconds)
            except Exception as ex:
                print(ex)
