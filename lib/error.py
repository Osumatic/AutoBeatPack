"""
Error message utils
"""


class DownloadError(Exception):
    """Custom exception for download errors"""


FAILED_TEXT = "\nStopped - {time}: {msg}"
