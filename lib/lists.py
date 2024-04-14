"""
Functions for working with lists
"""

from urllib.parse import quote

__all__ = ["split_list", "make_all_urls"]


def split_list(biglist, maxlen):
    """Turn big list into list of smaller lists"""
    for first_pos in range(0, len(biglist), maxlen):
        yield biglist[first_pos:first_pos + maxlen]


def make_all_urls(first_num, last_num):
    """Make list of URLs given an inclusive range"""
    urls = []
    for num in range(first_num, last_num+1):
        filename = f"S{num} - Beatmap Pack #{num}.7z"
        urls.append(f"https://packs.ppy.sh/{quote(filename)}")
    return urls
