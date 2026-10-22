from __future__ import annotations
import random
from pathlib import Path


class ProxyRotator:
    def __init__(self, pool_path: str | None):
        self._proxies: list[str] = []
        if pool_path:
            p = Path(pool_path)
            if p.exists():
                self._proxies = [ln.strip() for ln in p.read_text().splitlines() if ln.strip()]

    def pick(self) -> str | None:
        return random.choice(self._proxies) if self._proxies else None

    def __len__(self) -> int:
        return len(self._proxies)