"""
lap project (files)
"""

from typing import List
from src.utils.decorators import jsonpickle_decorators


class LapProject:
    """
    lap project
    """

    def __init__(self) -> None:
        self.main_file = ''
        self.geom_file = ''
        self.wells_event_file = ''
        self.wells_history_file = ''
        self.fluid_props_file = ''
        self.reservoir_props_file = ''

        self.grid_file = ''
        self.geo_maps_file = '' # file with files for each map 
        self.boundary_file = ''

        self.results_folder = ''

    # @jsonpickle_decorators.remove_unused_from_dict(['main_file'])
    # @jsonpickle_decorators.remove_unused_from_dict
    def __getstate__(self):
        state = self.__dict__.copy()
        del state['main_file']
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
