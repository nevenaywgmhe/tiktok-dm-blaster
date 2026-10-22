from __future__ import annotations
import httpx


class AccountChecker:
    """Verify session cookies are still valid before blasting."""

    CHECK_URL = "https://www.tiktok.com/passport/web/account/info/"

    def __init__(self, session_id: str, user_agent: str):
        self.session_id = session_id
        self.ua = user_agent

    async def is_alive(self) -> bool:
        async with httpx.AsyncClient(headers={"User-Agent": self.ua}) as c:
            r = await c.get(self.CHECK_URL, cookies={"sessionid": self.session_id})
            if r.status_code != 200:
                return False
            data = r.json()
            return data.get("data", {}).get("user_id") is not None