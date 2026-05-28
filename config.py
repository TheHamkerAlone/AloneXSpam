import logging
from os import getenv
from telethon import TelegramClient, events
from AltBots.data import ALTRON
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

# VALUES REQUIRED FOR XBOTS
API_ID = int(getenv("API_ID", 18136872))
API_HASH = getenv("API_HASH", "312d861b78efcd1b02183b2ab52a83a4")
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="8458947967").split()))
for x in ALTRON:
    if x not in SUDO_USERS:
        SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="8458947967"))
if OWNER_ID not in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)

# ------------- CLIENTS -------------

BOT_TOKENS = [
    getenv("BOT_TOKEN", "8808672991:AAHiJOCiUsU-NuOC0x4Zn8wdaw3JcgB6oBM"),
    getenv("BOT_TOKEN2", "8342189109:AAG6Oa8hiiYZgF3tUVnYY483toIF_xhd47c"),
    getenv("BOT_TOKEN3", "8614627276:AAGVqWSTx9AYum4oLeXj4BhNCAaIgZ8hRgY"),
    getenv("BOT_TOKEN4", "8991144749:AAHkyr5QN-O0W1q2LJDevOlOFvoyKESxpYQ"),
    getenv("BOT_TOKEN5", "8890147072:AAGtRgG9iBBLOsoWkXwt0qw8Ujzbdat9-U0"),
    getenv("BOT_TOKEN6"),
    getenv("BOT_TOKEN7"),
    getenv("BOT_TOKEN8"),
    getenv("BOT_TOKEN9"),
    getenv("BOT_TOKEN10"),
]

clients = []
for i, token in enumerate(BOT_TOKENS, start=1):
    if token:
        try:
            client = TelegramClient(f"X{i}", API_ID, API_HASH).start(bot_token=token)
            clients.append(client)
        except Exception as e:
            print(f"Failed to start client X{i}: {e}")

# Maintain backward compatibility for modules
X1 = clients[0] if len(clients) > 0 else None
X2 = clients[1] if len(clients) > 1 else None
X3 = clients[2] if len(clients) > 2 else None
X4 = clients[3] if len(clients) > 3 else None
X5 = clients[4] if len(clients) > 4 else None
X6 = clients[5] if len(clients) > 5 else None
X7 = clients[6] if len(clients) > 6 else None
X8 = clients[7] if len(clients) > 7 else None
X9 = clients[8] if len(clients) > 8 else None
X10 = clients[9] if len(clients) > 9 else None

def on_cmd(pattern, **kwargs):
    def decorator(func):
        for client in clients:
            client.add_event_handler(func, events.NewMessage(incoming=True, pattern=r"\%s" % CMD_HNDLR + pattern, **kwargs))
        return func
    return decorator

def on_msg(**kwargs):
    def decorator(func):
        for client in clients:
            client.add_event_handler(func, events.NewMessage(incoming=True, **kwargs))
        return func
    return decorator

def on_cb(pattern=None, **kwargs):
    def decorator(func):
        for client in clients:
            client.add_event_handler(func, events.CallbackQuery(pattern=pattern, **kwargs))
        return func
    return decorator
