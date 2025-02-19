#!/usr/bin/env python3

wait_n = __import__('1-concurrent_coroutines').wait_n
import random
import asyncio
import time

def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()

    asyncio.gather(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time -start_time

    return total_time / n
