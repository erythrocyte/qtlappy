"""
directory work helper
"""

import os
from typing import List


def get_files_in_dir(dir: str) -> List[str]:
    """
    """

    return os.listdir(dir)


def get_files_in_dir_pattern(dir: str, pattern: str) -> List[str]:
    """
    """

    files = get_files_in_dir(dir)
    return [file for file in files if pattern in file]


def dir_contains_files(dir: str) -> bool:
    """
    """

    files = get_files_in_dir(dir)
    return not files and len(files) > 0


def dir_contains_files_pattern(dir: str, pattern: str) -> bool:
    """
    """

    files = get_files_in_dir(dir)
    return any(pattern in file for file in files)
