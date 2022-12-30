"""
decorators
"""

import functools
from typing import List


def remove_unused_from_dict(prop_names: List[str]):
    def decorator(function):
        # @functools.wraps(function)
        def wrapper():
            func_result = function()

            if prop_names is None:
                print('prop names is empty')
                return func_result

            for prop_name in prop_names:
                del func_result[prop_name]
            return func_result
        
        return wrapper
    
    return decorator



