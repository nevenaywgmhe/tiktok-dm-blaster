# Security Policy

## Supported versions
Only `main` receives security fixes.

## Reporting
Email the maintainers privately (see GitHub profile) — do not open a public
issue for anything that could be weaponized.

## What we care about
- Session cookie leakage (never commit `.env`, `*.session`, or `targets.local.txt`)
- Proxy credential exposure in logs
- Dependency CVEs (`pip-audit` runs weekly in CI)

## Out of scope
- TikTok's own anti-spam / detection systems
- Account bans resulting from misuse of this tool
</Parameter>