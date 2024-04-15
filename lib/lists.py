"""
List utils
"""

from urllib import parse

from lib.types import pack_types

__all__ = ["split_list", "make_all_urls"]


def split_list(biglist, maxlen):
    """Turn big list into list of smaller lists"""
    for first_pos in range(0, len(biglist), maxlen):
        yield biglist[first_pos:first_pos + maxlen]


def make_url(num):
    "Make URL given beatpack number"
    pack_type = "standard"
    pack_subtype = "osu!"

    pack_info = pack_types[pack_type]
    pack_subinfo = pack_info["subtypes"][pack_subtype]
    for num_range, pack_rangeinfo in pack_subinfo["ranges"].items():
        if num in num_range:
            break

    filename = pack_info["template"].format(
        prefix=pack_info["prefix"],
        suffix=pack_subinfo["suffix"],
        num=num,
        mode=pack_rangeinfo["mode"],
        ext=pack_rangeinfo["ext"]
    )

    return f"https://packs.ppy.sh/{parse.quote(filename)}"


def make_all_urls(first_num, last_num):
    """Make list of URLs given an inclusive range"""
    urls = []
    for num in range(first_num, last_num+1):
        urls.append(make_url(num))
    return urls
