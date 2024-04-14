"""
Utils for reading config.txt
"""

import configparser
import os

from lib.pretty import ind, pprint, q

__all__ = ["try_user", "get_config"]


def try_user(config, user):
    """Recursively receives user input until valid config name entered."""
    try:
        config[user]  # pylint: disable=pointless-statement
        return user
    except KeyError:
        user = input(f"{q(user)} not found, try again:\t")
        return try_user(config, user)


def get_config():
    """Returns config values from config.txt"""
    raw_config = configparser.ConfigParser()
    raw_config.read("config.txt")
    user = "DEFAULT"
    if input("Use DEFAULT config? y/n\t").lower() != "y":
        user = input("Enter config name:\t")
        user = try_user(raw_config, user)
    config_user = raw_config[user]

    cf_first, cf_last, cf_batch_size = [
        config_user.getint("FirstPack"),
        config_user.getint("LastPack"),
        config_user.getint("BatchSize")
    ]
    cf_download_folder = os.path.join(os.path.dirname(__file__), config_user["DownloadFolder"])

    pprint(ind(f"Beatmap packs:   {cf_first} to {cf_last}"))
    pprint(ind(f"Batch size:      {cf_batch_size}"))
    pprint(ind(f"Download folder: {cf_download_folder}"""))
    input("Enter to begin, Ctrl+C to cancel.\n")

    return cf_first, cf_last, cf_batch_size, cf_download_folder
