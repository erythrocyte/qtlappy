"""
"""

import os
import typing
import jsonpickle
from src.models.lapproject import LapProject
from src.utils.helpers import dir_helper


def remove_projects_in_dir(dir: str) -> None:
    projects = dir_helper.get_files_in_dir_pattern(dir, '.lap')

    if not projects:
        return

    for project in projects:
        remove_project_files(project)


def remove_project_files(project_main_file: str) -> None:
    """
    """

    if project_main_file is None or project_main_file is '':
        return

    with open(project_main_file, 'r') as file:
        json_string = file.read()

    project = typing.cast(LapProject, jsonpickle.decode(json_string))

    os.remove(project.boundary)
    os.remove(project.contours_file)
    os.remove(project.fluid_props)
    __remove_model_geo_maps(project.geo_maps)
    os.remove(project.grid)
    os.remove(project.reservoir_props)
    os.remove(project.wells_event)
    os.remove(project.wells_geom)
    os.remove(project.wells_history)
    __remove_results(project.results_folder)

    os.remove(project_main_file)


def __remove_model_geo_maps(geo_maps_file: str):
    """
    """

    pass


def __remove_results(results: str):
    """
    """

    pass
