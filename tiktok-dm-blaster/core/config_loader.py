from __future__ import annotations
import tomli
from pathlib import Path
from pydantic import BaseModel, Field


class BlasterConfig(BaseModel):
    threads: int = Field(default=3, ge=1, le=20)
    delay: float = Field(default=6.5, ge=1.0)
    jitter: float = Field(default=2.0, ge=0.0)
    retries: int = 3
    proxy_pool: str | None = None
    session_cookie_env: str = "TT_SESSIONID"
    user_agent: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) TikTok/33.7.4"


def load_config(path: Path) -> BlasterConfig:
    if not path.exists():
        return BlasterConfig()
    with path.open("rb") as fh:
        raw = tomli.load(fh)
    return BlasterConfig(**raw.get("blaster", {}))