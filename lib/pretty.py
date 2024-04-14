"""Utility functions for pretty printing and string formatting"""

from datetime import datetime as _datetime

__all__ = ["q", "pprint", "time", "size", "indent"]


def q(string):
    """Adds quotes around string"""
    return f'"{string}"'


def time():
    """Current time in HH:MM::SS format"""
    return _datetime.now().strftime("%H:%M::%S")


def indent(string, spaces=2):
    """Indent string by number of spaces"""
    return f"{' ' * spaces}{string}"


async def size(num):
    """Formats byte size into readable units"""
    for unit in ["b", "KB", "MB"]:
        if num < 1024:
            return f"{num:.3f}{unit}"
        num /= 1024


def pprint(var):
    """Pretty printer for lists"""
    if not isinstance(var, list):
        print(var)
    else:
        for item in var:
            print(item)
