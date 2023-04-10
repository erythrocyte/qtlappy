"""
project remover
10.12.2022
by erythrocyte
"""

import os
import typing
import jsonpickle
from src.models.lapproject import LapProject
from src.utils.helpers import dir_helper, file_helper


def remove_projects_in_dir(dir: str) -> None:
    projects = dir_helper.get_files_in_dir_pattern(dir, '.lap')

    if not projects:
        return

    for project in projects:
        remove_project_files(os.path.join(dir,project))


def remove_project_files(project_main_file: str) -> None:
    """
    """

    if project_main_file is None or project_main_file is '':
        return

    with open(project_main_file, 'r') as file:
        json_string = file.read()

    project = typing.cast(LapProject, jsonpickle.decode(json_string))

    
    file_helper.delete_file_if_exists(project.boundary_file)
    file_helper.delete_file_if_exists(project.geom_file)
    file_helper.delete_file_if_exists(project.fluid_props_file)
    __remove_model_geo_maps(project.geo_maps_file)
    file_helper.delete_file_if_exists(project.grid_file)
    file_helper.delete_file_if_exists(project.reservoir_props_file)
    file_helper.delete_file_if_exists(project.wells_event_file)
    file_helper.delete_file_if_exists(project.wells_history_file)
    __remove_results(project.results_folder)

    file_helper.delete_file_if_exists(project_main_file)


def __remove_model_geo_maps(geo_maps_file: str):
    """
    """

    pass


def __remove_results(results: str):
    """
    """

    pass
