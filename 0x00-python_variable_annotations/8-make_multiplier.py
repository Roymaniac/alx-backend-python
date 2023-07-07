#!/usr/bin/env python3

'''
Write a type-annotated function make_multiplier that takes a float multiplier
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    returns a function that multiplies a float by multiplier.
    '''
    def multiply(x: float) -> float:
        '''
        multipy the multiplier
        '''
        return float(x * multiplier)
    return multiply
