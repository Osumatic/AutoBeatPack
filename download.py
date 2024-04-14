"""
AutoBeatPack - Automatic parallel download of osu! beatmap packs from the official source.
"""

import asyncio

import aiohttp
import aiohttp.client_exceptions

from lib.lists import make_all_urls, split_list
from lib.pretty import pprint, time
from lib.config import get_config
from lib.downloader import download_batch


def start():
    """Run AutoBeatPack"""
    pprint("==== AutoBeatPack by Saltssaumure ====\n")

    config_filename = "config.ini"
    succeed_text = f"\nAll complete - {time()}"
    failed_text = f"\nStopped - {time()}"
    try:

        first, last, batch_size, abs_download_folder = get_config(config_filename)

        all_urls = split_list(make_all_urls(first, last), batch_size)
        for idx, batch_urls in enumerate(all_urls):
            asyncio.run(download_batch(idx+1, batch_urls, abs_download_folder))

        pprint(succeed_text)
    except KeyboardInterrupt:
        pprint(f"{failed_text}: User cancelled.")
    except TimeoutError as err:
        pprint(f"{failed_text}: Connection timed out. {err}")
    except aiohttp.client_exceptions.ClientConnectorError as err:
        pprint(f"{failed_text}: Can't connect. {err}")
    except (FileNotFoundError, ValueError) as err:
        pprint(f"{failed_text}: Invalid {config_filename} - {err}")


if __name__ == "__main__":
    start()
