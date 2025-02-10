#!/usr/bin/env python3

async_c = __import__('1-async_comprehension').async_comprehension
import asyncio
import time

async def measure_runtime() -> float:
    "measures the runtime"
    start_time = time.time()
    batch = asyncio.gather(async_c(), async_c(), async_c(), async_c())
    end_time = time.time()
    return end_time - start_time

