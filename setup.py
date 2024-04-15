"""
Create executable in dist folder using py2exe
"""

from distutils.core import setup  # pylint: disable=deprecated-module
from glob import glob  # pylint: disable=unused-import

import py2exe  # type: ignore # pylint: disable=unused-import, import-error

# data_files = [("Microsoft.VC90.CRT", glob(
#     r'C:\Program Files\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\*.*'))]

setup(
    # data_files=data_files,
    console=["download.py"]
)
