import sys
import argparse
from pathlib import Path

from core.engine import BlasterEngine
from core.config_loader import load_config
from utils.logger import setup_logger


def parse_args():
    p = argparse.ArgumentParser(prog="tiktok-dm-blaster")
    p.add_argument("--config", default="config/settings.toml")
    p.add_argument("--targets", required=True, help="path to targets file")
    p.add_argument("--message", required=True, help="message template path")
    p.add_argument("--dry-run", action="store_true")
    return p.parse_args()


def main():
    args = parse_args()
    log = setup_logger("blaster")
    cfg = load_config(Path(args.config))
    log.info("loaded config: %s threads, %s delay", cfg.threads, cfg.delay)

    engine = BlasterEngine(cfg=cfg, dry_run=args.dry_run)
    engine.load_targets(Path(args.targets))
    engine.load_message(Path(args.message))

    try:
        engine.run()
    except KeyboardInterrupt:
        log.warning("interrupted by user")
        engine.shutdown()
        sys.exit(130)

    log.info("done: %s sent, %s failed", engine.stats.sent, engine.stats.failed)


if __name__ == "__main__":
    main()