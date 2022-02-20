#!/usr/bin/env python3
"""
Module for 2. Run time for four parallel comprehensions.
0x02. Python - Async Comprehension
Holberton Web Stack programming Spec ― Back-end
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes `async_comprehension` four times in parallel.
    """
    start = time.perf_counter()
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*tasks)
    end = time.perf_counter()
    return end - start
