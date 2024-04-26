"""
Reading config.txt utils
"""

import configparser
from os import path

from lib.error import ConfigError
from lib.pretty import ind, pprint, q
from lib.packtypes import PACK_TYPES

__all__ = ["try_user", "get_config"]


def try_user(config: configparser.ConfigParser, profile: str):
    """Recursively receives user input until valid config name entered."""
    try:
        config[profile]  # pylint: disable=pointless-statement
        return profile
    except KeyError:
        profile = input(f"{q(profile)} not found:\t\t")
        return try_user(config, profile)


def get_config(config_filename: str, abs_here: str):
    """Returns config values from config.txt"""
    raw_config = configparser.ConfigParser()
    if not path.exists(config_filename):
        raise FileNotFoundError("file not found.")
    raw_config.read(config_filename)
    if len(raw_config.sections()) == 0:
        raise ConfigError("file missing profiles.")

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
    cf_range = range(cf_first, cf_last + 1)
    cf_abs_download_folder = path.join(abs_here, config_user["DownloadFolder"])
    cf_pack_category = config_user["PackCategory"].lower()
    cf_pack_mode = config_user["PackMode"].lower() if cf_pack_category == "standard" else None

    if cf_first < 1 or cf_last < 1:
        raise ConfigError("pack numbers must be positive.")
    if cf_first > cf_last:
        raise ConfigError("first pack cannot be greater than last pack.")
    if cf_batch_size < 1:
        raise ConfigError("batch size must be positive.")
    if cf_pack_category not in PACK_TYPES:
        raise ConfigError("invalid pack category.")
    if cf_pack_mode and cf_pack_mode not in PACK_TYPES[cf_pack_category]["subtypes"]:
        raise ConfigError("invalid pack mode.")

    pprint(ind(f"Beatmap packs:    {cf_first} to {cf_last} ({len(cf_range)} packs)"))
    pprint(ind(f"Batch size:       {cf_batch_size} pack per batch"))
    pprint(ind(f"Download folder:  {cf_abs_download_folder}"""))
    pprint(ind(f"Pack category:    {PACK_TYPES[cf_pack_category]['title']}"))
    pprint(ind(f"Pack mode:        {cf_pack_mode}"))
    input("Enter to begin, Ctrl+C to cancel.\n")

    return cf_range, cf_batch_size, cf_abs_download_folder, cf_pack_category, cf_pack_mode
