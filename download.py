"""
AutoBeatPack
"""

import asyncio
import os
from datetime import datetime
from urllib import parse

import aiohttp


def time():
    """Current time in HH:MM::SS format"""
    return datetime.now().strftime("%H:%M::%S")


def pprint(var):
    """Pretty printer for lists"""
    if not isinstance(var, list):
        print(var)
    else:
        for item in var:
            print(item)


def split_list(biglist, maxlen):
    """Turn big list into list of smaller lists"""
    for first_pos in range(0, len(biglist), maxlen):
        yield biglist[first_pos:first_pos + maxlen]


def make_all_urls(first_num, last_num):
    """Make list of URLs given an inclusive range"""
    urls = []
    for num in range(first_num, last_num+1):
        urls.append(parse.quote_plus(f"https//packs.ppy.sh/S{num} - Beatmap Pack #{num}.7z"))
    return urls


async def size(num):
    """Formats byte size into readable units"""
    for unit in ["b", "KB", "MB"]:
        if num < 1024:
            return f"{num:.3f}{unit}"
        num /= 1024


async def download_file(filename, response, overwrite):
    """Download file and report progress"""
    expected_size = int(response.headers["Content-Length"])
    mode = "wb" if overwrite else "xb"
    with open(filename, mode=mode) as file:
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
                print(f"  {filename} - {percent:.0f}%")
    pprint(f"  Downloaded {filename}!")


async def download_decision(url):
    """Decide whether to download file from url based on local file contents."""
    filename = os.path.basename(parse.unquote(parse.urlparse(url).path))

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            try:
                filesize = os.path.getsize(filename)
                expected_size = int(response.headers["Content-Length"])

                p_starting = f"  Starting {filename} {await size(expected_size)}"
                p_skipped = f"  Skipped {filename}"
                p_redownload = f"""  Redownload {filename}?
                      (local:  {await size(filesize)}
                      (server: {await size(expected_size)})
                    y/n"""

                if filesize == expected_size:
                    pprint(p_skipped + " (match)")
                elif filesize == 0:
                    pprint(p_starting)
                    await download_file(filename, response, overwrite=True)
                else:
                    if input(p_redownload + "\t").lower() == "y":
                        pprint(p_starting)
                        await download_file(filename, response, overwrite=True)
                    else:
                        pprint(p_skipped + " (manual)")
            except OSError:
                # File doesn't exist
                pprint(p_starting)
                await download_file(filename, response, overwrite=False)


async def download_batch(batch, urls):
    """Download files in current batch in parallel"""
    pprint(f"Batch {batch} - {time()}")
    tasks = [download_decision(url) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        start, end, batch_size = 1084, 1411, 3
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
    except Exception as e:  # pylint: disable=broad-except
        pprint(f"Stopped due to error - {time()}: {e}")
