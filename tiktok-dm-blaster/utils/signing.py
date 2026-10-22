import hashlib
import time
import secrets


def make_tt_signature() -> str:
    """Generate a plausible msToken/X-Bogus-style signature stub.

    Real TikTok signing requires JS reverse-engineering; this stub
    produces a deterministic-per-second token for local testing.
    """
    ts = int(time.time())
    nonce = secrets.token_hex(8)
    digest = hashlib.sha256(f"{ts}:{nonce}".encode()).hexdigest()
    return f"{ts}_{digest[:32]}"