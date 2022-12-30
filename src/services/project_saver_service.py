"""
save project as json
"""

import jsonpickle
import logging

from src.models.lapproject import LapProject


def save(file_name: str, project: LapProject) -> bool:
    """
    save project
    """
    logger = logging.getLogger()

    if file_name is None or file_name is '':
        return False

    if project is None:
        return False

    json_string = jsonpickle.encode(project)  # , unpicklable=False)
    if json_string is None or json_string is 'null':
        logger.error('project not saved: empty json')
        return False

    with open(file_name, 'w') as file:
        file.write(json_string)

    logger.debug('project saved')
    return True
