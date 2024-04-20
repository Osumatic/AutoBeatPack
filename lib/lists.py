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


def make_url(num, pack_category, pack_subtype=None):
    "Make URL given beatpack number"
    pack_info = pack_types[pack_category]

    match pack_category:
        case "standard":
            pack_subinfo = pack_info["subtypes"][pack_subtype]
            for num_range, pack_rangeinfo in pack_subinfo["ranges"].items():
                if num in num_range:
                    break

            filename = pack_info["template"].format(
                prefix=pack_info["prefix"],
                suffix=pack_subinfo["suffix"],
                num=num,
                mode=pack_rangeinfo["mode"],  # pylint: disable=undefined-loop-variable
                ext=pack_rangeinfo["ext"]  # pylint: disable=undefined-loop-variable
            )
        case "featured artist":
            filename = pack_info["template"].format(
                prefix=pack_info["prefix"],
                num=num,
                artist=pack_info["artists"][num-1]
            )
        case "tournament":
            pass
        case "loved":
            pass
        case "spotlights":
            pass
        case "theme":
            pass
        case "artist/album":
            pass
        case _:
            raise ValueError(f"Invalid pack category {pack_category}")

    return f"https://packs.ppy.sh/{parse.quote(filename)}"


def make_all_urls(first_num, last_num, pack_category, pack_mode=None):
    """Make list of URLs given an inclusive range"""
    urls = []
    for num in range(first_num, last_num+1):
        urls.append(make_url(num, pack_category, pack_mode))
    return urls
