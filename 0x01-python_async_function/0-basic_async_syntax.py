#!/usr/bin/env python3
"""async function"""
import asyncio
import random


async def wait_random(max_delay = 10):
    """async function"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
