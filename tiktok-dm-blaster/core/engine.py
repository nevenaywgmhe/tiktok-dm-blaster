from __future__ import annotations
import asyncio
import random
from dataclasses import dataclass, field
from pathlib import Path

from core.config_loader import BlasterConfig
from handlers.dm_sender import DMSender
from handlers.rate_limiter import RateLimiter
from utils.logger import setup_logger


@dataclass
class BlastStats:
    sent: int = 0
    failed: int = 0
    skipped: int = 0


@dataclass
class BlasterEngine:
    cfg: BlasterConfig
    dry_run: bool = False
    stats: BlastStats = field(default_factory=BlastStats)

    def __post_init__(self):
        self.log = setup_logger("engine")
        self._targets: list[str] = []
        self._message: str = ""
        self._limiter = RateLimiter(self.cfg.delay, self.cfg.jitter)

    def load_targets(self, path: Path) -> None:
        self._targets = [ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]
        self.log.info("loaded %s targets", len(self._targets))

    def load_message(self, path: Path) -> None:
        self._message = path.read_text(encoding="utf-8").strip()

    async def _blast_one(self, sender: DMSender, user: str) -> None:
        await self._limiter.wait()
        try:
            ok = await sender.send_dm(user, self._message)
            if ok:
                self.stats.sent += 1
            else:
                self.stats.failed += 1
        except Exception as exc:  # noqa: BLE001
            self.log.error("send failed for %s: %s", user, exc)
            self.stats.failed += 1

    async def _run_async(self) -> None:
        sender = DMSender(self.cfg, dry_run=self.dry_run)
        sem = asyncio.Semaphore(self.cfg.threads)

        async def worker(user: str):
            async with sem:
                await self._blast_one(sender, user)

        await asyncio.gather(*(worker(u) for u in self._targets))
        await sender.close()

    def run(self) -> None:
        asyncio.run(self._run_async())

    def shutdown(self) -> None:
        self.log.info("shutdown requested")