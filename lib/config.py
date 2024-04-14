"""
Reading config.txt utils
"""

import configparser
from os import path

from lib.pretty import ind, pprint, q

__all__ = ["try_user", "get_config"]


def try_user(config, profile):
    """Recursively receives user input until valid config name entered."""
    try:
        config[profile]  # pylint: disable=pointless-statement
        return profile
    except KeyError:
        profile = input(f"{q(profile)} not found, try again:\t")
        return try_user(config, profile)


def get_config():
    """Returns config values from config.txt"""
    raw_config = configparser.ConfigParser()
    raw_config.read("config.ini")
    profile = "DEFAULT"
    if input("Use DEFAULT config? y/n\t").lower() != "y":
        profile = input("Config profile name:\t")
        profile = try_user(raw_config, profile)
    config_user = raw_config[profile]

    cf_first, cf_last, cf_batch_size = [
        config_user.getint("FirstPack"),
        config_user.getint("LastPack"),
        config_user.getint("BatchSize")
    ]
    cf_abs_download_folder = path.join(
        path.dirname(path.dirname(__file__)),
        config_user["DownloadFolder"]
    )

    pprint(ind(f"Beatmap packs:   {cf_first} to {cf_last}"))
    pprint(ind(f"Batch size:      {cf_batch_size}"))
    pprint(ind(f"Download folder: {cf_abs_download_folder}"""))
    input("Enter to begin, Ctrl+C to cancel.\n")

    return cf_first, cf_last, cf_batch_size, cf_abs_download_folder
