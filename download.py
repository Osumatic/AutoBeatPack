"""
AutoBeatPack - Automatic parallel download of osu! beatmap packs from the official source.
"""

import asyncio
from os import path

import aiohttp
import aiohttp.client_exceptions

from lib.config import get_config
from lib.disk import OpenModes, make_folders, save_list
from lib.downloader import download_batch
from lib.error import FAILED_TEXT, ConfigError, DownloadError
from lib.packtypes import PACK_TYPES
from lib.pretty import pprint, time
from lib.urls import make_all_urls, split_list


def start():
    """Run AutoBeatPack"""
    pprint("==== AutoBeatPack by Saltssaumure ====\n")

    config_filename = "config.ini"
    succeed_text = f"\nAll complete - {time()}"

    try:
        abs_here = path.dirname(__file__)
        abs_url_folder = path.join(abs_here, "url")
        packs_range, batch_size, abs_download_folder, pack_category, pack_mode = get_config(
            config_filename, abs_here
        )

        make_folders(abs_url_folder, abs_download_folder)

        all_urls = make_all_urls(packs_range, pack_category, pack_mode)
        abs_url_category_folder = path.join(abs_url_folder, PACK_TYPES[pack_category]["title"])
        save_list(abs_url_category_folder, "urls.txt", all_urls, mode=OpenModes.OVERWRITE)

        all_urls_split = split_list(all_urls, batch_size)
        for idx, batch_urls in enumerate(all_urls_split):
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
    except DownloadError as exc:
        pprint(FAILED_TEXT.format(
            time=time(),
            msg=f"Download failed. {exc}"
        ))
    except FileNotFoundError as exc:
        pprint(FAILED_TEXT.format(
            time=time(),
            msg=f"File not found. {exc}"
        ))
    except ConfigError as exc:
        pprint(FAILED_TEXT.format(
            time=time(),
            msg=f"Invalid config, {exc}"
        ))


if __name__ == "__main__":
    start()
