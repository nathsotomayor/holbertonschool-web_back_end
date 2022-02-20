#!/usr/bin/env python3
"""
Module for 1. Async Comprehensions.
0x02. Python - Async Comprehension
Holberton Web Stack programming Spec ― Back-end
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension.
    """
    return [number async for number in async_generator()]
