#!/usr.bin/env python3
import asyncio
import random
from typing import Iterator

async def async_generator() -> Iterator[float]:
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0,10)
