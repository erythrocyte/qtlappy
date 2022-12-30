"""
"""

import os
import logging
from typing import List
from src.models.lapmodel import LapModel
from src.models.lapproject import LapProject
from src.services import project_saver_service


def create(projects: List[LapModel], name: str, project_path: str) -> LapModel:
    item = LapModel()
    item.id = __valid_id(projects)
    item.name = name if name != '' else f'Project{item.id+1}'
    item.project = LapProject()
    project_file_name = os.path.join(project_path, f'{name}.lap')
    item.project.main_file = project_file_name
    status = project_saver_service.save(project_file_name, item.project)

    if not status:
        return None

    logger = logging.getLogger()
    logger.info(f'Model \'{item.name}\' created')

    return item


def check_project_folder(project_folder: str) -> bool:
    """
    """

    pass


def __valid_id(projects: List[LapModel]) -> int:
    if not projects:
        return 0

    return max(p.id for p in projects)+1
