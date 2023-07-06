#!/usr/bin/env python3

'''
Write a type-annotated function to_kv.
'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float])-> Tuple[str, float]:
    '''
    returns a tuple with both values in it
    '''
    value = (k,v**2)
    return value
