#!/usr/bin/env python3
from typing import Tuple

def sum_mixed_list(mxd_lst: Tuple[int, float]) -> float:
    sum = 0
    for num in mxd_lst:
        sum += num
    return sum
