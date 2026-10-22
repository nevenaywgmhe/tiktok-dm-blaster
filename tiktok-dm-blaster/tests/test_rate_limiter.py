import asyncio
import pytest

from handlers.rate_limiter import RateLimiter


@pytest.mark.asyncio
async def test_rate_limiter_respects_base():
    limiter = RateLimiter(base_delay=0.05, jitter=0.0)
    start = asyncio.get_event_loop().time()
    await limiter.wait()
    elapsed = asyncio.get_event_loop().time() - start
    assert elapsed >= 0.04


@pytest.mark.asyncio
async def test_rate_limiter_serializes():
    limiter = RateLimiter(base_delay=0.02, jitter=0.0)
    order: list[int] = []

    async def worker(i: int):
        await limiter.wait()
        order.append(i)

    await asyncio.gather(*(worker(i) for i in range(3)))
    assert order == [0, 1, 2]