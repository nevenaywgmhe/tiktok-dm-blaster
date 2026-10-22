import asyncio
from pathlib import Path

from core.config_loader import BlasterConfig
from core.engine import BlasterEngine


def test_engine_dry_run(tmp_path: Path):
    targets = tmp_path / "targets.txt"
    targets.write_text("@alice\n@bob\n")
    msg = tmp_path / "msg.txt"
    msg.write_text("hi $username")

    cfg = BlasterConfig(threads=2, delay=0.01, jitter=0.0)
    engine = BlasterEngine(cfg=cfg, dry_run=True)
    engine.load_targets(targets)
    engine.load_message(msg)
    engine.run()

    assert engine.stats.sent == 2
    assert engine.stats.failed == 0