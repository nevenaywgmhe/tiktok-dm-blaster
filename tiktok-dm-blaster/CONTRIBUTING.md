# Contributing to tiktok-dm-blaster

Thanks for helping out! A few ground rules:

## Scope
- `core/` — engine + config loading. Keep it framework-free.
- `handlers/` — one feature per module (sender, limiter, proxy, checker).
- `models/` — pure dataclasses, no I/O.
- `utils/` — stateless helpers only.
- `tests/` — pytest, one module per handler.

## Local dev
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest -q
```

## PRs
- Keep diffs small and focused.
- Add tests for new handlers.
- Do not commit real session cookies or target lists.

## Ethics
This tool is for educational research into rate-limiting and anti-spam systems.
Do not use it against accounts you don't own or to harass users.