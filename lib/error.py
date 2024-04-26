"""
Error message utils
"""


class DownloadError(Exception):
    """Custom exception for download errors"""


class ConfigError(Exception):
    """Custom exception for category errors"""


FAILED_TEXT = "\nStopped - {time}: {msg}"
