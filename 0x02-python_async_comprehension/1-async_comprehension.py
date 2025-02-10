#!/usr/bin/env python3
import asyncio
import random
async_g = __import__('0-async_generator').async_generator
from typing import List

async def async_comprehension() -> List[float]:
    "collects 10 random numbers using async comprehensing over async_generator"
    return await asyncio.shield([i async for i in async_g()])
