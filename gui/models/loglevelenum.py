"""
module docstring
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import enum


class LogLevelEnum(enum.Enum):
    """
    log levels
    """

    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    FATAL = 4
