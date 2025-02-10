#!/usr/bin/env python3
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
   
    def fun(num: float):
        return num * multiplier
    return fun
