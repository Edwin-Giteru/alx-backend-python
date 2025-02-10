#!/usr/bin/env python3
wait_r = __import__('0-basic_async_syntax').wait_random
import asyncio
import random
from typing import List

async def wait_n(n: int, max_delay: int) ->List[float]:
    delay = [await wait_r(max_delay) for i in range(n)]
    return delay
    

