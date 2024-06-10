#!/usr/bin/env python3
"""task4"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """task_wait_n"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    tasks = asyncio.as_completed(tasks)
    delays = [await task for task in tasks]
    return delays
