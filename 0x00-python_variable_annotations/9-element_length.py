#!/usr/bin/env python3  
""" Basic annotations - task 9 """

from typing import List, Union, Tuple,Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a list of tuples, where the first element is a string and the second is an int """
    return [(i, len(i)) for i in lst]
