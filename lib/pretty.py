"""
String formatting utils
"""

from datetime import datetime

__all__ = ["q", "pprint", "time", "size", "ind"]


def q(string: str):
    """Adds quotes around string"""
    return f'"{string}"'


def time():
    """Current time in HH:MM::SS format"""
    return datetime.now().strftime("%H:%M::%S")


def ind(string: str, spaces: int = 2):
    """Indent string by number of spaces"""
    return f"{' ' * spaces}{string}"


async def size(num: int):
    """Formats byte size into readable units"""
    for unit in ["b", "KB", "MB"]:
        if num < 1024:
            return f"{num:.3f}{unit}"
        num /= 1024


def pprint(var: any):
    """Pretty printer for lists"""
    if not isinstance(var, list):
        print(var)
    else:
        for item in var:
            print(item)
