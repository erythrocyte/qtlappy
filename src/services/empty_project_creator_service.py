"""
"""

from typing import List
from src.models.lapproject import LapProject


def create(projects: List[LapProject], name: str = '') -> LapProject:
    item = LapProject()
    item.id = __valid_id(projects)
    item.name = name if name != '' else f'Project{item.id+1}'

    return item


def __valid_id(projects: List[LapProject]) -> int:
    if not projects:
        return 0

    return max(p.id for p in projects)+1
