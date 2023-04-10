"""

module caption: project cloner
date: 10.04.2023
author: erythrocyte
description: ---

"""

import os
import shutil

from src.models.lapmodel import LapModel


def clone_project(new_path: str, new_name: str, model: LapModel):
    """
    Clone project files

    Args:
        new_path (str): new directory for project
        new_name (str): new name for cloned project
        model (LapModel): _description_
    """
    if not model:
        return

    if not model.project:
        return

    if not new_path or new_path == '':
        return

    if not new_name:
        return

    if new_name == '':
        new_name = model.name + "_copy"

    if not os.path.exists(new_path):
        os.mkdir(new_path)

    nn = os.path.join(new_path, model.project.main_file)
    shutil.copyfile(model.project.main_file, nn)
    os.rename(nn, new_name)