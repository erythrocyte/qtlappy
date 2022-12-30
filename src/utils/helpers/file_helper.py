"""
"""

import os


def delete_file_if_exists(file_path: str):
    """
    """

    try:
        os.remove(file_path)
    except OSError:
        pass
