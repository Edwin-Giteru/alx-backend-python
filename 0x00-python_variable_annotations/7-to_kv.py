#!/usr/bin/env python3
from typing import Tuple

def to_kv(k: str ,v: int | float) -> Tuple[str, float]:
    return k, v **2
