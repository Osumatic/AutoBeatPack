"""
AutoBeatPack - Automatic parallel download of osu! beatmap packs from the official source.
"""

import asyncio

import aiohttp
import aiohttp.client_exceptions

from lib.lists import make_all_urls, split_list
from lib.pretty import pprint, time
from lib.config import get_config
from lib.download import download_batch


def start():
    """Run AutoBeatPack"""
    pprint("==== AutoBeatPack by Saltssaumure ====\n")
    try:
        first, last, batch_size, abs_download_folder = get_config()

        all_urls = split_list(make_all_urls(first, last), batch_size)
        for idx, batch_urls in enumerate(all_urls):
            asyncio.run(download_batch(idx+1, batch_urls, abs_download_folder))

        pprint(f"\nAll complete - {time()}")
    except KeyboardInterrupt:
        pprint(f"\nDownload(s) cancelled - {time()}")
    except TimeoutError as e:
        pprint(f"\nDownload(s) cancelled - {time()}: Connection timed out. {e}")
    except aiohttp.client_exceptions.ClientConnectorError as e:
        pprint(f"\nDownload(s) cancelled - {time()}: Can't connect. {e}")
    except ValueError:
        pprint("\nInvalid config.txt value(s), see README for help.")


if __name__ == "__main__":
    start()
