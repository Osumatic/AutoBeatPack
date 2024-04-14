# https://packs.ppy.sh/S1084%20-%20Beatmap%20Pack%20%231084.7z

import os
from urllib import parse
import asyncio
import aiohttp
from datetime import datetime

def time():
    return datetime.now().strftime('%H:%M::%S')

def pprint(var):
    if not(isinstance(var, list)):
        print(var)
    else:
        for item in var:
            print(item)

def divideChunks(urls, chunkSize): 
    for i in range(0, len(urls), chunkSize):  
        yield urls[i:i + chunkSize]

def makeAllUrls(start, end):
    urls = [f"https://packs.ppy.sh/S{cur}%20-%20Beatmap%20Pack%20%23{cur}.7z" for cur in range(start, end+1)]
    return urls
    
async def size(num):
    for unit in ["b", "KB", "MB"]:
        if num < 1024:
            return f"{num:.3f}{unit}" 
        else:
            num /= 1024

async def download(filename, response, overwrite):
    expectedSize = int(response.headers["Content-Length"])
    mode = "wb" if overwrite else "xb"
    with open(filename, mode=mode) as file:
        filesize = 0
        oldProgress = 0
        # Get and write chunks of 1024 bytes
        # Print progress every 1%
        chunkSize = 1024
        increment = 10
        while True:
            chunk = await response.content.read(chunkSize)
            if not chunk:
                break
            file.write(chunk)
            filesize += chunkSize
            percent = filesize * 100 / expectedSize
            progress = int(percent / increment)
            if progress > oldProgress:
                oldProgress = progress
                print(f"  {filename} - {percent:.0f}%")
    pprint(f"  Downloaded {filename}!")

async def downloadFromUrl(url):
    filename = os.path.basename(parse.unquote(parse.urlparse(url).path))

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            try:
                filesize = os.path.getsize(filename)
                expectedSize = int(response.headers["Content-Length"])

                pStarting = f"  Starting {filename} {await size(expectedSize)}"
                pSkipped = f"  Skipped {filename}"
                pRedownload = f"  Redownload {filename} (local: {await size(filesize)}, server: {await size(expectedSize)})? y/n"

                if filesize == expectedSize:
                    pprint(pSkipped + " (match)")
                elif filesize == 0:
                    pprint(pStarting)
                    await download(filename, response, overwrite=True)
                else:
                    if input(pRedownload + "\t").lower() == "y":
                        pprint(pStarting)
                        await download(filename, response, overwrite=True)
                    else:
                        print(pSkipped + " (manual)")
            except OSError as e:
                # File doesn't exist
                pprint(pStarting)
                await download(filename, response, overwrite=False)
            except Exception as e:
                print(f"  Error {filename}: {e}")

async def downloadFromUrls(batch, urls):
    pprint(f"Batch {batch} - {time()}")
    tasks = [downloadFromUrl(url) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        start, end, chunkSize = 1084, 1411, 3
        folder = os.path.dirname(os.path.abspath(__file__))
        allUrls = divideChunks(makeAllUrls(start, end), chunkSize)
        # allUrls = [["https://getsamplefiles.com/download/txt/sample-1.txt", "https://getsamplefiles.com/download/txt/sample-2.txt"],["https://getsamplefiles.com/download/txt/sample-3.txt"]]

        pprint(f"Downloading {start} to {end}, in groups of {chunkSize}, to {folder}")
        for i, urls in enumerate(allUrls):
            asyncio.run(downloadFromUrls(i+1, urls))
        pprint(f"All complete - {time()}")
    except KeyboardInterrupt:
        pprint(f"Download(s) cancelled - {time()}")