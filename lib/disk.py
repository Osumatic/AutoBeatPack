"""
Disky actions
"""

import pathlib
from lib.packtypes import PACK_TYPES


def make_folders(abs_url_folder, abs_download_folder):
    """Make folders"""
    pathlib.Path(abs_download_folder).mkdir(parents=True, exist_ok=True)
    for category_info in PACK_TYPES.values():
        category_title = category_info["title"]
        pathlib.Path(abs_url_folder, category_title).mkdir(parents=True, exist_ok=True)
