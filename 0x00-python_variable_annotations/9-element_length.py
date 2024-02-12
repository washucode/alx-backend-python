#!/usr/bin/env python3  
""" Basic annotations - task 9 """

from typing import List, Union, Tuple


def element_length(lst: List[Union[str, List[Union[int, float]]]]) -> List[Tuple[str, int]]:
    """ Returns a list of tuples, where the first element is a string and the second is an int """
    return [(i, len(i)) for i in lst]
