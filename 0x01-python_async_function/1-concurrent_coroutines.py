#!/usr/bin/env python3
""" multiple coroutines at the same time with async """
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """perform multiple coroutines at the same time with async"""
    delaysArray = []
    for _ in range(n):
        delaysArray.append(asyncio.create_task(wait_random(max_delay)))
    return sorted(await asyncio.gather(*delaysArray))
