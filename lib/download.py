"""
Parallel download utils
"""

import asyncio
import os
from urllib import parse

import aiohttp

from lib.pretty import ind, pprint, q, size, time

__all__ = ["download_batch", "download_decision", "download_file"]


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


async def download_decision(url, abs_download_folder):
    """Decide whether to download file from url based on local file contents."""
    filename = os.path.basename(parse.unquote(parse.urlparse(url).path))
    abs_filename = os.path.join(abs_download_folder, filename)
    if not os.path.exists(abs_download_folder):
        os.makedirs(abs_download_folder)

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            try:
                expected_size = int(response.headers["Content-Length"])

                p_starting = ind(f'Starting {q(filename)} (server: {await size(expected_size)})')
                p_skipped = ind(f'Skipped {q(filename)}')

                filesize = os.path.getsize(abs_filename)

                p_redownload = ind(
                    f'''Redownload {q(filename)}? y/n
    (local:  {await size(filesize)})
    (server: {await size(expected_size)})\t''')

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
                pprint(p_starting)
                await download_file(abs_filename, response, overwrite=False)


async def download_batch(batch, urls, abs_download_folder):
    """Download files in current batch in parallel"""
    pprint(f"Batch {batch} - {time()}")
    tasks = [download_decision(url, abs_download_folder) for url in urls]
    await asyncio.gather(*tasks)
