#!/usr/bin/env python3

""" Duck-typed annotations"""


from typing import Sequence, Union, Any, List, Tuple


def safely_get_value(dct: dict, key: Any,
                     default: Union[Any, None]) -> Union[Any, None]:
    """ Duck-typed annotations """
    if key in dct:
        return dct[key]
    else:
        return default
