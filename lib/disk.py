"""
Disky actions
"""

import os.path as path
import pathlib
from enum import Enum

from lib.packtypes import PACK_TYPES


class OpenModes(Enum):
    """Modes for opening files"""
    WRITE_BYTE = "xb"
    OVERWRITE_BYTE = "wb"
    APPEND_BYTE = "ab"
    READ_BYTE = "rb"
    WRITE = "x"
    OVERWRITE = "w"
    APPEND = "a"
    READ = "r"


def make_folders(abs_url_folder: str, abs_download_folder: str):
    """Make URL and download folders"""
    pathlib.Path(abs_download_folder).mkdir(parents=True, exist_ok=True)
    for category_info in PACK_TYPES.values():
        category_title = category_info["title"]
        pathlib.Path(abs_url_folder, category_title).mkdir(parents=True, exist_ok=True)


def save_list(abs_folder: str, filename: str, items: list, mode: OpenModes):
    """Save list to file (overwriting)"""
    abs_path = path.join(abs_folder, filename)
    with open(abs_path, mode=mode.value, encoding="utf-8") as file:
        for item in items:
            file.write(item + "\n")
