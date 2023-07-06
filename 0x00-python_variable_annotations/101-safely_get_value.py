#!/usr/bin/env python3
'''
Given the parameters and the return values, add type annotations to the function
Hint: look into TypeVar
'''

from typing import Any, Mapping, TypeVar, Union

T=TypeVar("T")
NoneType = TypeVar("NoneType", bound=None)

def safely_get_value(dct: Mapping, key: Any, default: Union[T, NoneType])-> Union[Any, T]:
    '''
    fill the right annotation type
    '''
    if key in dct:
        return dct[key]
    else:
        return default


annotations = safely_get_value.__annotations__
print("Here's what the mappings should look like")
for k, v in annotations.items():
    print( ("{}: {}".format(k, v)))
