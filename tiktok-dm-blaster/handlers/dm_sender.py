from __future__ import annotations
import os
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

from core.config_loader import BlasterConfig
from utils.signing import make_tt_signature


class DMSender:
    BASE = "https://www.tiktok.com/api/im/message/send/"

    def __init__(self, cfg: BlasterConfig, dry_run: bool = False):
        self.cfg = cfg
        self.dry_run = dry_run
        self._client = httpx.AsyncClient(
            timeout=15.0,
            headers={"User-Agent": cfg.user_agent, "Referer": "https://www.tiktok.com/messages"},
        )
        self._session = os.getenv(cfg.session_cookie_env, "")

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=2, max=20))
    async def send_dm(self, username: str, message: str) -> bool:
        if self.dry_run:
            return True
        payload = {
            "to_user": username,
            "msg": message,
            "ts": make_tt_signature(),
        }
        cookies = {"sessionid": self._session} if self._session else {}
        r = await self._client.post(self.BASE, json=payload, cookies=cookies)
        return r.status_code == 200 and r.json().get("status_code") == 0

    async def close(self) -> None:
        await self._client.aclose()