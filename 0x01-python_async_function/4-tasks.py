#!/usr/bin/env python3
wait_r = __import__('0-basic_async_syntax').wait_random
import asyncio
import random
from typing import List
task_wait_r = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) ->List[float]:

    """uses wait_random to compile a list af delay times"""
    myList = []
    for i in range(n):
        task = task_wait_r(await wait_r(max_delay))
        result = await task
        myList.append(result)

    return myList

