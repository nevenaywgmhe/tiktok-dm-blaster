import asyncio
import random


async def human_delay(min_s: float = 2.0, max_s: float = 8.0) -> None:
    await asyncio.sleep(random.uniform(min_s, max_s))


def typing_speed_for(text: str) -> float:
    """Approximate typing time in seconds for a message."""
    return len(text) / random.uniform(8.0, 14.0)