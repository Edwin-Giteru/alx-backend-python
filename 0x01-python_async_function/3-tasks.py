#!/usr/bin/env python3
wait_r = __import__('0-basic_async_syntax').wait_random
import asyncio

def task_wait_random(max_delay: int) ->asyncio.Task:
    return asyncio.create_task(wait_r(max_delay))
