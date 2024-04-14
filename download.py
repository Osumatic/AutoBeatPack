"""
AutoBeatPack
"""

import asyncio
import os

from urllib import parse

import aiohttp

import aiohttp.client_exceptions
from lib.pretty import pprint, q, time, size, ind
from lib.lists import split_list, make_all_urls


async def download_file(abs_filename, response, overwrite):
    """Download file and report progress"""
    expected_size = int(response.headers["Content-Length"])
    mode = "wb" if overwrite else "xb"
    filename = os.path.basename(abs_filename)

    with open(abs_filename, mode=mode) as file:
        filesize = 0
        old_prog = 0
        # Get and write chunks of 1024 bytes
        # Print progress every 1%
        chunk_size = 1024
        increment = 10
        while True:
            chunk = await response.content.read(chunk_size)
            if not chunk:
                break
            file.write(chunk)
            filesize += chunk_size
            percent = filesize * 100 / expected_size
            new_prog = int(percent / increment)
            if new_prog > old_prog:
                old_prog = new_prog
                pprint(ind(f"{q(filename)} - {percent:.0f}%"))

    pprint(f"Downloaded {q(filename)}!")


async def download_decision(url):
    """Decide whether to download file from url based on local file contents."""
    filename = os.path.basename(parse.unquote(parse.urlparse(url).path))
    abs_filename = os.path.join(os.path.dirname(__file__), "beatpacks", filename)

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            try:
                expected_size = int(response.headers["Content-Length"])

                p_starting = ind(f'Starting {q(filename)} (server: {await size(expected_size)})')
                p_skipped = ind(f'Skipped {q(filename)}')

                filesize = os.path.getsize(abs_filename)

                p_redownload = ind(
                    f'''Redownload {q(filename)}?
    (local:  {await size(filesize)})
    (server: {await size(expected_size)})
    y/n\t'''
                )

                if filesize == expected_size:
                    pprint(p_skipped + " (match)")
                elif filesize == 0:
                    pprint(p_starting)
                    await download_file(abs_filename, response, overwrite=True)
                else:
                    if input(p_redownload + "\t").lower() == "y":
                        pprint(p_starting)
                        await download_file(abs_filename, response, overwrite=True)
                    else:
                        pprint(p_skipped + " (manual)")
            except OSError:
                # File doesn't exist
                pprint(p_starting)
                await download_file(abs_filename, response, overwrite=False)


async def download_batch(batch, urls):
    """Download files in current batch in parallel"""
    pprint(f"Batch {batch} - {time()}")
    tasks = [download_decision(url) for url in urls]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    try:
        start, end, batch_size = 1230, 1411, 3
        folder = os.path.dirname(os.path.abspath(__file__))
        all_urls = split_list(make_all_urls(start, end), batch_size)

        pprint(
            f"Downloading {start} to {end}, in groups of {batch_size}, to {folder}")
        for idx, batch_urls in enumerate(all_urls):
            asyncio.run(download_batch(idx+1, batch_urls))
        pprint(f"All complete - {time()}")
    except KeyboardInterrupt:
        pprint(f"Download(s) cancelled - {time()}")
    except TimeoutError as e:
        pprint(f"Download(s) cancelled - {time()}: Connection timed out. {e}")
    except aiohttp.client_exceptions.ClientConnectorError as e:
        pprint(f"Download(s) cancelled - {time()}: Can't connect. {e}")
    # except Exception as e:  # pylint: disable=broad-except
    #     pprint(f"Stopped due to error - {time()}: {e}")
