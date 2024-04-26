"""
Beatmap download url utils
"""

import os.path as path

from ossapi import Ossapi

from lib.packtypes import PACK_TYPES
from lib.disk import save_list, OpenModes

__all__ = ["get_osu_id", "split_list", "make_all_urls"]


def get_osu_id():
    """Get osu! API client ID and secret"""
    with open("api_keys.txt", "r", encoding="utf-8") as file:
        osu_id = file.readline().strip()
        secret = file.readline().strip()
    return osu_id, secret


def split_list(biglist, maxlen):
    """Turn big list into list of smaller lists"""
    for first_pos in range(0, len(biglist), maxlen):
        yield biglist[first_pos:first_pos + maxlen]


def make_all_urls(packs_range: range, abs_url_folder: str, pack_category: str, pack_mode: str):
    """Make list of URLs given an inclusive range"""
    client_id, client_secret = get_osu_id()

    api = Ossapi(client_id, client_secret)
    beatmappacks = api.beatmap_packs(type=pack_category)

    urls = []
    for pack in beatmappacks.beatmap_packs:
        wanted_info = PACK_TYPES[pack_category]
        if pack_mode:
            wanted_prefix = wanted_info["prefix"] + wanted_info["subtypes"][pack_mode]["prefix"]
        else:
            wanted_prefix = wanted_info["prefix"]

        pack_prefix = "".join([char for char in pack.tag if char.isalpha()])
        pack_num = pack.tag.removeprefix(pack_prefix)

        if pack_prefix != wanted_prefix:
            continue

        if int(pack_num) in packs_range:
            urls.append(pack.url)

    return urls
