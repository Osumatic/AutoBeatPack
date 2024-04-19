"""
AutoBeatPack - Automatic parallel download of osu! beatmap packs from the official source.
"""

import asyncio
from os import path

import aiohttp
import aiohttp.client_exceptions

from lib.config import get_config
from lib.downloader import download_batch
from lib.error import DownloadError, FAILED_TEXT
from lib.lists import make_all_urls, split_list
from lib.pretty import pprint, time


def start():
    """Run AutoBeatPack"""
    pprint("==== AutoBeatPack by Saltssaumure ====\n")

    config_filename = "config.ini"
    succeed_text = f"\nAll complete - {time()}"

    try:
        abs_here = path.dirname(__file__)
        first, last, batch_size, abs_download_folder, pack_category, pack_mode = get_config(
            config_filename, abs_here
        )

        all_urls = split_list(make_all_urls(first, last, pack_category, pack_mode), batch_size)
        for idx, batch_urls in enumerate(all_urls):
            asyncio.run(download_batch(idx+1, batch_urls, abs_download_folder))

        pprint(succeed_text)
    except KeyboardInterrupt:
        pprint(FAILED_TEXT.format(
            time=time(),
            msg="User cancelled."
        ))
    except TimeoutError as exc:
        pprint(FAILED_TEXT.format(
            time=time(),
            msg=f"Connection timed out. {exc}"
        ))
    except aiohttp.client_exceptions.ClientConnectorError as exc:
        pprint(FAILED_TEXT.format(
            time=time(),
            msg=f"Can't connect. {exc}"
        ))
    except FileNotFoundError as exc:
        pprint(FAILED_TEXT.format(
            time=time(),
            msg=f"Invalid {config_filename}. {exc}"
        ))
    except DownloadError as exc:
        pprint(FAILED_TEXT.format(
            time=time(),
            msg="Download failed: {exc}"
        ))


if __name__ == "__main__":
    start()
