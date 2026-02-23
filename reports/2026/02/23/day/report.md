# Watchtower Daily Report — 2026-02-23 (Day Cycle)

## Executive Summary

Two significant new threats emerged today: a sophisticated npm supply chain worm campaign targeting AI coding assistants (SANDWORM_MODE), and a fresh MuddyWater APT campaign deploying four new malware families against MENA targets. A new AI-assisted info-stealer (Arkanix) was also analyzed. All previously tracked high-severity items (BeyondTrust CVE-2026-1731, MS Patch Tuesday zero-days, OpenSSL) remain active with no status changes since the morning cycle.

---

## New Findings

### 1. SANDWORM_MODE — npm Supply Chain Worm Targets AI Coding Assistants
- **Threat Score:** 9/10
- **CVE:** None assigned
- **Affected Technology:** npm ecosystem, AI coding assistants (Claude Code, Cursor, VS Code Continue, Windsurf, Claude Desktop)
- **Source:** [The Hacker News](https://thehackernews.com/2026/02/malicious-npm-packages-harvest-crypto.html) / Socket.dev
- **Date:** February 23, 2026

**Summary:** Socket identified 19 malicious npm packages in an active supply chain worm campaign codenamed SANDWORM_MODE, a new wave of the Shai-Hulud family. Key capabilities include:

- **Credential harvesting:** npm/GitHub tokens, CI/CD secrets, API keys, cryptocurrency wallet keys
- **MCP server injection:** Deploys malicious Model Context Protocol servers into AI coding assistants (Claude Code, Cursor, VS Code Continue, Windsurf) with embedded prompt injection to exfiltrate SSH keys, AWS credentials, .env files, and .npmrc tokens
- **LLM API key theft:** Targets 9 providers (Anthropic, OpenAI, Google, Mistral, Cohere, etc.)
- **Worm propagation:** Abuses stolen npm/GitHub identities to self-propagate; weaponized GitHub Action steals CI/CD secrets
- **Kill switch:** Home directory wiper if access to GitHub/npm is lost (currently disabled)
- **Polymorphic engine:** Uses local Ollama/DeepSeek Coder for code mutation to evade detection (currently disabled)
- **48-hour activation delay** with per-machine jitter

Malicious packages include typosquats: `claud-code`, `cloude-code`, `opencraw`, `veim`, `rimarf`, `yarsg`, `suport-color`, and others published by aliases `official334` and `javaorg`.

**Action Required:** Organizations should audit npm dependencies for these packages, rotate all npm/GitHub tokens and CI secrets, and review MCP server configurations in AI coding tools.

---

### 2. MuddyWater Operation Olalampo — New Iranian APT Campaign Against MENA
- **Threat Score:** 8/10
- **CVE:** None assigned
- **Affected Technology:** Windows systems across MENA organizations (energy, marine services)
- **Source:** [The Hacker News](https://thehackernews.com/2026/02/muddywater-targets-mena-organizations.html) / Group-IB
- **Date:** February 23, 2026

**Summary:** Iranian APT MuddyWater (Earth Vetala / Mango Sandstorm) launched Operation Olalampo targeting MENA organizations since January 26, 2026, deploying four new malware families:

- **GhostFetch:** First-stage downloader with anti-VM/anti-debug checks, in-memory payload execution
- **GhostBackDoor:** Second-stage backdoor with interactive shell, file read/write
- **HTTP_VIP:** Native downloader deploying AnyDesk; new variant adds clipboard capture and beacon control
- **CHAR:** Rust backdoor controlled via Telegram bot ("Olalampo" / "stager_51_bot") — shows signs of AI-assisted development

Attack chains use malicious Office documents with macro lures (flight tickets, energy company themes). CHAR shares code structure with BlackBeard/Archer RAT. Group also exploiting public-facing server vulnerabilities for initial access.

---

### 3. Arkanix Stealer — AI-Developed Info-Stealer Experiment
- **Threat Score:** 6/10
- **CVE:** None assigned
- **Affected Technology:** Windows systems, 22+ browsers, crypto wallets, VPN clients
- **Source:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/arkanix-stealer-pops-up-as-short-lived-ai-info-stealer-experiment/) / Kaspersky
- **Date:** February 22, 2026

**Summary:** Kaspersky analyzed Arkanix Stealer, an info-stealer promoted on dark web forums since October 2025 and shut down after just 2 months. Evidence of LLM-assisted development. Two tiers: Python-based basic and C++ premium (VMProtect, AV evasion, wallet injection). Capabilities include browser data theft (22+ browsers), OAuth2 token extraction, Discord/Telegram credential theft, crypto wallet targeting, and a ChromElevator tool to bypass Google's App-Bound Encryption. The premium tier adds HVNC, RDP theft, and gaming platform credential theft. Significance lies in demonstrating how AI accelerates malware development cycles.

---

## Continuing Threats (No Status Change)

| Threat | Score | Status |
|--------|-------|--------|
| BeyondTrust CVE-2026-1731 | 10 | Active ransomware exploitation |
| MS Patch Tuesday 6 zero-days | 9 | Active exploitation |
| OpenSSL CVE-2025-15467 (CVSS 9.8) | 8 | Patch available |
| AI-assisted FortiGate campaign | 8 | 600+ devices compromised |
| CISA KEV (RoundCube, Dell, Chrome) | 8 | Due dates approaching |
| Starkiller PhaaS | 8 | Active service |
| Kimwolf I2P disruption | 7 | Ongoing |
| PromptSpy Android malware | 7 | Active |
| Grandstream CVE-2026-2329 | 7 | Unpatched in many deployments |

## Noted Items

| Item | Detail |
|------|--------|
| Romanian hacker guilty plea | Catalin Dragomir admitted selling access to Oregon state government network (SecurityWeek, Feb 23) |
| Winos 4.0 Taiwan campaigns | Fortinet reports massive ValleyRat campaigns via phishing/DLL sideloading (Feb 20) |

---

## Source Coverage

| Metric | Value |
|--------|-------|
| Total sources | 90 |
| Checked this cycle | 32 |
| With new findings | 5 |
| Unreachable | 0 |
| Degraded | darkreading.com (Cloudflare block), reddit.com/r/netsec (no content rendered) |

### Sources Checked
✅ BleepingComputer ✅ The Hacker News ✅ Krebs on Security ✅ SecurityWeek ✅ CISA KEV ✅ Schneier on Security ✅ Fortinet Threat Research ✅ Cisco Talos ✅ ESET WeLiveSecurity ✅ Cloudflare Blog ✅ HackerOne Blog ✅ GitHub Security Lab ✅ AWS Security Blog ✅ Red Hat Security ✅ Atlassian Security ✅ AttackerKB ✅ Google Security Blog ✅ MSRC Blog ✅ Qualys Blog ✅ Unit 42 ✅ Help Net Security ✅ Packet Storm ✅ Exploit-DB ✅ Full Disclosure ✅ seclists.org
⚠️ Dark Reading (403/Cloudflare) ⚠️ Reddit r/netsec (no content)
❌ CISA Alerts page (404 — federal funding lapse)
ℹ️ NVD, CVE.org, MITRE, VulDB, OSV, CNVD, EUVD, Google Project Zero, vulndb.cyberriskanalytics — not checked (web search unavailable; no new CVE IDs surfaced from news sources)
