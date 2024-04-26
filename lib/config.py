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
        profile = input(f"{q(profile)} not found:\t\t")
        return try_user(config, profile)


def get_config(config_filename, abs_here):
    """Returns config values from config.txt"""
    raw_config = configparser.ConfigParser()
    if not path.exists(config_filename):
        raise FileNotFoundError("file not found.")
    raw_config.read(config_filename)
    if len(raw_config.sections()) == 0:
        raise ValueError("file missing profiles.")

    profile = "DEFAULT"
    if input(f"Use {q(profile)} profile? [Y/n]\t").lower() == "n":
        profile = input("Config profile name:\t\t")
        profile = try_user(raw_config, profile)
    config_user = raw_config[profile]

    cf_first, cf_last, cf_batch_size = [
        config_user.getint("FirstPack"),
        config_user.getint("LastPack"),
        config_user.getint("BatchSize"),
    ]
    cf_abs_download_folder = path.join(abs_here, config_user["DownloadFolder"])
    cf_pack_category = config_user["PackCategory"].lower()
    cf_pack_mode = config_user["PackMode"].lower() if cf_pack_category == "standard" else None

    pprint(ind(f"Beatmap packs:   {cf_first} to {cf_last}"))
    pprint(ind(f"Batch size:      {cf_batch_size}"))
    pprint(ind(f"Download folder: {cf_abs_download_folder}"""))
    pprint(ind(f"Pack category:   {cf_pack_category}"))
    pprint(ind(f"Pack mode:       {cf_pack_mode}"))
    input("Enter to begin, Ctrl+C to cancel.\n")

    return cf_first, cf_last, cf_batch_size, cf_abs_download_folder, cf_pack_category, cf_pack_mode
