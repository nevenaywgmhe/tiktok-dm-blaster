import asyncio
import random


class RateLimiter:
    """Jittered delay between DM sends to avoid detection."""

    def __init__(self, base_delay: float, jitter: float):
        self.base = base_delay
        self.jitter = jitter
        self._lock = asyncio.Lock()

    async def wait(self) -> None:
        async with self._lock:
            delay = self.base + random.uniform(0, self.jitter)
            await asyncio.sleep(delay)