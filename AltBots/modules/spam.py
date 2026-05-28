# © @ALONE_WAS_BOT
import asyncio

from AltBots.data import GROUP, PORMS
from config import on_cmd, SUDO_USERS, CMD_HNDLR as hl

from random import choice
from telethon import functions, types, errors


async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=smex.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass


@on_cmd(r"spam(?: |$)(.*)")
async def spam(event):
    if event.sender_id in SUDO_USERS:
        altron = event.text.split(" ", 2)
        mk = await event.get_reply_message()

        try:
            if len(altron) == 3:
                message = altron[2]
                for _ in range(int(altron[1])):
                    if event.reply_to_msg_id:
                        await mk.reply(message)
                    else:
                        await event.client.send_message(event.chat_id, message)
                    await asyncio.sleep(0.3)
            elif event.reply_to_msg_id and mk.media:
                for _ in range(int(altron[1])):
                    mk = await event.client.send_file(event.chat_id, mk, caption=mk.text)
                    await gifspam(event, mk) 
                    await asyncio.sleep(0.3)
            elif event.reply_to_msg_id and mk.text:
                message = mk.text
                for _ in range(int(altron[1])):
                    await event.client.send_message(event.chat_id, message)
                    await asyncio.sleep(0.3)
            else:
                await event.reply(f"😈 **Usage:**\n  » {hl}spam 13 Altron\n  » {hl}spam 13 <ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ>\n\n**To do spam with replying to a user:**\n  » {hl}spam 13 Altron <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>")

        except errors.FloodWaitError as f:
            await asyncio.sleep(f.seconds)
        except (IndexError, ValueError):
            await event.reply(f"😈 **Usage:**\n  » {hl}spam 13 Altron\n  » {hl}spam 13 <ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ>\n\n**To do spam with replying to a user:**\n  » {hl}spam 13 Altron <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>")
        except Exception as e:
            print(f"Error in spam: {e}")


@on_cmd(r"pspam(?: |$)(.*)")
async def pspam(event):
    if event.sender_id in SUDO_USERS:
        if event.chat_id in GROUP:
            await event.reply("» ꜱᴏʀʀʏ, ᴛʜɪꜱ ɪꜱ ᴀʟᴛʀᴏɴ ᴘʀᴏᴛᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘ.")
        else:
            try:
                counter = int(event.text.split(" ", 2)[1])
                porrn = choice(PORMS)
                for _ in range(counter):
                    alt = await event.client.send_file(event.chat_id, porrn)
                    await gifspam(event, alt) 
                    await asyncio.sleep(0.3)
            except errors.FloodWaitError as f:
                await asyncio.sleep(f.seconds)
            except (IndexError, ValueError):
                await event.reply(f"🔞 **Usage:**  {hl}pspam 13")
            except Exception as e:
                print(f"Error in pspam: {e}")


@on_cmd(r"hang(?: |$)(.*)")
async def hang(e):
    if e.sender_id in SUDO_USERS:
        if e.chat_id in GROUP:
            await e.reply("» ꜱᴏʀʀʏ, ᴛʜɪꜱ ɪꜱ ᴀʟᴛʀᴏɴ ᴘʀᴏᴛᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘ.")
        else:
            try:
                counter = int(e.text.split(" ", 2)[1])
                hang_msg = "😈" + "꙰" * 500 + "😈"
                for _ in range(counter):
                    await e.respond(hang_msg)
                    await asyncio.sleep(0.5)
            except errors.FloodWaitError as f:
                await asyncio.sleep(f.seconds)
            except (IndexError, ValueError):
                await e.reply(f"😈 **Usage:** {hl}hang 10")
            except Exception as e:
                print(f"Error in hang: {e}")
