import glob
import asyncio
import logging
import importlib.util
import urllib3

from pathlib import Path
from config import clients


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def load_plugins(plugin_name):
    path = Path(f"AltBots/modules/{plugin_name}.py")
    try:
        spec = importlib.util.spec_from_file_location(f"AltBots.modules.{plugin_name}", path)
        load = importlib.util.module_from_spec(spec)
        load.logger = logging.getLogger(plugin_name)
        spec.loader.exec_module(load)
        import sys
        sys.modules["AltBots.modules." + plugin_name] = load
        print("Altron has Imported " + plugin_name)
    except Exception as e:
        print(f"Failed to load plugin {plugin_name}: {e}")


async def main():
    files = glob.glob("AltBots/modules/*.py")
    for name in files:
        plugin_name = Path(name).stem
        load_plugins(plugin_name)

    if not clients:
        print("No clients started. Please check your BOT_TOKENs.")
        return

    print("\n𝐗𝐁𝐨𝐭𝐬 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ⚡\nMy Master ---> @ALONE_WAS_BOT")

    # Run all clients until disconnected
    await asyncio.gather(*(client.run_until_disconnected() for client in clients))


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
