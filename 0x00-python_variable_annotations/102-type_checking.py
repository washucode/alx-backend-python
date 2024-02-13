#!/usr/bin/env python3

""" validate code"""


from typing import Sequence, Union, Any, List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Returns a list of tuples,
    where the first element is a string
    and the second is an int
    """
    return [(i, i * factor) for i in lst]
