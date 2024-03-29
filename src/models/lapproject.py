"""
lap project (files)
"""

from src.utils.decorators import jsonpickle_decorators


class LapProject:
    """
    lap project
    """

    def __init__(self) -> None:
        self.main_file = ''
        self.geom_file = ''
        self.wells_event = ''
        self.wells_history = ''
        self.fluid_props = ''
        self.reservoir_props = ''

        self.grid = ''
        self.geo_maps = ''
        self.boundary = ''

        self.results_folder = ''

    # @jsonpickle_decorators.remove_unused_from_dict(['main_file'])
    # @jsonpickle_decorators.remove_unused_from_dict
    def __getstate__(self):
        state = self.__dict__.copy()
        del state['main_file']
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
