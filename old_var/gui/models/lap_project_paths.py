"""

"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json


class LapProjectPaths:
    """
    LapProjectPaths
    """

    def __init__(self, directory: str):
        """

        args:
            dr - directory
        """

        self.__main_proj_file = 'proj.ql'
        self.__dr = directory
        self.__grid_file = ''
        self.__boundary_file = ''
        self.__wells_file = ''
        self.__fracts_file = ''
        # self.__satur_fields = []
        # self.__press_fields = []
        # self.__version = None
        self.__current_version = "0.1"
        self.__press_folder = 'press'
        self.__satur_folder = 'satur'

    def save_project(self):
        """
        save project to file
        """
        data = self.__to_dict()
        with open(os.path.join(self.__dr, self.__main_proj_file), 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def read_project(self):
        """
        read project
        """
        pass

    def __to_dict(self):
        data = {}
        data['project'] = []
        data['project'].append({
            'intro': 'QT LAPPY PROJECT',
            'version': self.__current_version,
            'grid': self.__grid_file,
            'boundary': self.__boundary_file,
            'wells': self.__wells_file,
            'fracts': self.__fracts_file,
            'pressures': self.__press_folder,
            'saturations': self.__satur_folder
        })

        return data
