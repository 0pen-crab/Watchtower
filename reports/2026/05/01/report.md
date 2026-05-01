# Watchtower Night Report — 2026-05-01
**Cycle:** Night | **Generated:** 2026-05-01 00:30 UTC (2026-05-01T00:30:00Z)
**Sources checked:** 22/30 | **CISA KEV total:** unreachable (cisa.gov 403) | **New KEV additions:** CVE-2024-1708 (ConnectWise ScreenConnect) and CVE-2026-32202 (Windows Shell) added 2026-04-29 — relayed via THN/SecurityWeek

---

## 🔴 CRITICAL

### CVE-2026-4670 / CVE-2026-5174 — Progress MOVEit Automation Pre-Auth Authentication Bypass (CVSS 9.8) and Privilege Escalation (CVSS 7.7)
**Product:** Progress MOVEit Automation 2024.0.0, 2025.0.0, 2025.1.0 branches | **CVE:** CVE-2026-4670, CVE-2026-5174 | **Status:** Patched, no confirmed in-the-wild exploitation yet

Airbus Seclab discovered two flaws in Progress MOVEit Automation, the workflow/scheduler companion to MOVEit Transfer. CVE-2026-4670 is an authentication-bypass-by-primary-weakness condition that lets an unauthenticated remote attacker reach administrative functionality of the Automation server (CVSS 9.8). CVE-2026-5174 (CVSS 7.7) is a chained improper-input-validation flaw that escalates an authenticated low-privilege user to administrator. Together they constitute pre-auth-to-admin on any internet-reachable Automation deployment. No public PoC and no confirmed in-the-wild activity at time of writing, but Progress's 2026-04-30 advisory and Airbus's parallel write-up provide enough technical detail for fast weaponisation.

**Timeline:** Q1 2026: Airbus Seclab discovers and reports → 2026-04-30: Progress publishes advisory + patches across all supported branches; CVE numbers assigned; OpenCVE indexes both entries.

**Why it matters:** The 2023 Cl0p mass-exploitation of MOVEit Transfer (CVE-2023-34362) compromised 2,700+ organisations and remains the most expensive single supply-chain ransomware event on record. Automation runs in many of the same enterprise environments as Transfer and frequently shares the same DMZ — and ransomware crews specifically tracked Progress for follow-on bugs after 2023. Treat this as the kind of advisory Cl0p, FIN11, or a successor crew will weaponise within days. Patch every internet-facing MOVEit Automation node before that happens.

**Discovered by:** Airbus Seclab (responsible disclosure to Progress).

**Mitigation:**
- Upgrade MOVEit Automation to the fixed releases for 2024.0.x / 2025.0.x / 2025.1.x branches per Progress's 2026-04-30 advisory.
- Until patched, restrict inbound access to the Automation web/API endpoints to known-good source IPs only, and disable any internet-exposed Automation listeners.
- Rotate Automation operator credentials and any tokens stored in workflow definitions on previously-exposed instances; assume credential disclosure if pre-patch internet exposure is confirmed.
- Bring MOVEit Transfer + Automation into the same patch SLA window — Progress vulnerabilities have historically been chained.

**Sources:** [OpenCVE — CVE-2026-4670](https://app.opencve.io/cve/CVE-2026-4670) | [OpenCVE — CVE-2026-5174](https://app.opencve.io/cve/CVE-2026-5174) | [Positive Technologies dbugs roll-up](https://dbugs.ptsecurity.com)

---

### Google Gemini CLI Headless-Mode Pre-Sandbox RCE (CVSS 10.0)
**Product:** `@google/gemini-cli` < 0.39.1 (and < 0.40.0-preview.3) and `google-github-actions/run-gemini-cli` < 0.1.22 | **CVE:** None assigned (vendor advisory, GHSA pending) | **Status:** Patched, no confirmed in-the-wild exploitation, but trivially attackable via untrusted PRs

Google's Gemini CLI implicitly trusted the contents of the working directory's `.gemini/` folder when running in headless / non-interactive mode (the `run-gemini-cli` GitHub Action and any unattended invocation of the CLI). An attacker could plant a malicious `.gemini/settings.json` containing custom MCP-server definitions or shell-out commands; on next agent startup the CLI parsed and executed those settings *before* sandbox initialisation, yielding code execution on the runner with whatever privileges Gemini had. The realistic attack pattern is a malicious pull-request that drops `.gemini/settings.json` into the repo, then the CI workflow runs `run-gemini-cli` against that PR's commit and executes the attacker's commands on the GitHub Actions runner — with access to `GITHUB_TOKEN` and any secrets the workflow exposes. Google patched 2026-04-30 by requiring explicit folder-trust (`GEMINI_TRUST_WORKSPACE: 'true'` or interactive consent) before reading workspace `.gemini/` configs.

**Timeline:** 2026-04-30: Novee Security reports flaw → same day: Google ships `@google/gemini-cli` 0.39.1 / 0.40.0-preview.3 and `run-gemini-cli` 0.1.22 → The Hacker News + Schneier coverage on 2026-04-30 evening.

**Why it matters:** This is the second AI-coding-agent config-file weaponisation pattern in 48 hours (after Mini Shai-Hulud writing `.claude/settings.json` for SessionStart persistence — see today's Update). Any organisation that runs Gemini CLI in CI/CD against external PRs — common for OSS triage and "summarise this PR" automations — is one unpatched runner away from a worker-secret leak. The CVSS 10 score reflects unauthenticated → arbitrary code execution with no preconditions beyond being able to submit a PR. AI-agent config files are the new `.github/workflows/`: code that runs implicitly when the right wrapper opens it. Treat them as such.

**Discovered by:** Novee Security (responsible disclosure to Google).

**Mitigation:**
- Upgrade `@google/gemini-cli` to ≥ 0.39.1 (or ≥ 0.40.0-preview.3) and `google-github-actions/run-gemini-cli` to ≥ 0.1.22 immediately.
- For workflows that run Gemini against untrusted PR commits, do **not** set `GEMINI_TRUST_WORKSPACE: 'true'`; review the upstream guidance for safe untrusted-input handling.
- Audit all GitHub Actions workflows that invoke `run-gemini-cli` (or any agent CLI) on `pull_request` triggers — confirm they don't grant `secrets`, `id-token: write`, or write tokens to runs against external contributors.
- Add CI guardrails: refuse PRs that introduce new `.gemini/`, `.claude/`, `.cursor/`, or `.copilot/` config files without a maintainer code review.
- Discovery research path: cross-reference of npm registry for `@google/*` security advisories with The Hacker News' AI-pipeline tag yielded the GHSA + advisory text within the same hour as publication — same approach worked for the Mini Shai-Hulud bun-runtime detection.

**Sources:** [The Hacker News — Google Fixes CVSS 10 Gemini CLI CI RCE](https://thehackernews.com/2026/04/google-fixes-cvss-10-gemini-cli-ci-rce.html) | [Schneier on Security — Mythos / AI implications coverage](https://www.schneier.com/blog/archives/2026/04/) | [GitHub release — google-github-actions/run-gemini-cli 0.1.22](https://github.com/google-github-actions/run-gemini-cli/releases/tag/v0.1.22)

---

## 🟠 HIGH

### CVE-2026-41940 cPanel & WHM Authentication Bypass — UPDATE: Public PoC + IOC Scanner Now in the Wild (Threat score 10, previously 10)
**Product:** cPanel & WHM (all currently supported branches) + WP Squared 11.136.1 | **CVE:** CVE-2026-41940 | **Threat score:** 10 (unchanged, still maximum) | **First reported:** 2026-04-29

A material-detail change on yesterday's CRITICAL: in the 24 hours since the cPanel advisory, multiple weaponised PoCs and an IOC scanner have appeared on GitHub (AndreiG6/CVE-2026-41940 + ≥1 other repo updated within the past hour as of report time). Several of these are not just session-validation/scanner code but functional one-shot session-injection exploits — the bar to exploit drops from "watchTowr-level analysis" to "clone repo, point at IP, send request." Combined with yesterday's confirmed pre-disclosure in-the-wild use, defenders should now assume opportunistic mass scanning of TCP/2083 + 2087 from commodity infrastructure within hours, not days.

**Why this is an update vs. yesterday's CRITICAL:** the trigger is "technical detail newly published" — a working public exploit now exists where yesterday's coverage referenced only watchTowr's vendor-coordinated write-up. Threat score stays pegged at 10 because urgency cannot meaningfully go higher; the change is an operational signal to defenders that any unpatched pre-2026-04-29 cPanel instance is now reachable by anyone with a botnet.

**Mitigation (incremental over yesterday's):**
- If you have not patched: assume the box is breached. Patch, then rotate all credentials and contacted-shell SSH keys on every account, and replay traffic logs for session-store anomalies.
- Run the public IOC scanner (or your own equivalent) over inbound HTTP logs on 2083/2087 for `Authorization: Basic` headers containing `\r` or `\n` byte values.
- Brief the SOC: this is a "cron-job-grade" exploit now, not a researcher-grade one; expect detection volume to spike.

**Sources:** [GitHub — AndreiG6/CVE-2026-41940 IOC scanner (updated within last hour)](https://github.com/AndreiG6/CVE-2026-41940) | [BleepingComputer — cPanel CVE-2026-41940 PoC available](https://www.bleepingcomputer.com) | [Yesterday's Watchtower CRITICAL entry](../30/report.md)

---

### Mini Shai-Hulud — UPDATE: Campaign Expands to PyPI via PyTorch Lightning 2.6.2 / 2.6.3 (Threat score 9, previously 8)
**Product:** PyPI package `pytorch-lightning` versions 2.6.2 and 2.6.3 (in addition to yesterday's SAP CAP npm packages) | **CVE:** None assigned | **Threat score:** 9 (previously 8) | **First reported:** 2026-04-29

Yesterday's TeamPCP-attributed Mini Shai-Hulud worm — covered as a npm-only SAP CAP supply-chain compromise — extended into the Python ecosystem on 2026-04-30 with trojanised PyTorch Lightning releases 2.6.2 and 2.6.3 published to PyPI. The attack chain is conceptually identical (a hidden `_runtime/start.py` downloads the Bun JavaScript runtime, then executes an 11 MB obfuscated `router_runtime.js` payload that harvests local creds, GitHub/PyPI tokens, CI secrets, and cloud keys), but with two important changes: (1) execution is automatic on `import lightning` rather than gated behind a `preinstall` hook, so any developer or CI runner that even imports the module is compromised; (2) malicious commits to victim repos use a hardcoded git author identity impersonating Anthropic's Claude Code, which both improves the worm's blend-in (looks like AI-assisted commits) and is an early example of attribution-laundering against AI coding agents. PyPI quarantined both versions; downgrade to 2.6.1.

**Why this is an update vs. yesterday's CRITICAL:** the trigger is "affected product scope expanded" — the worm has crossed from JavaScript to Python and from `npm install` to `import` time, both of which materially widen blast radius. Threat score moves from 8 → 9 because the Python ecosystem expansion likely pulls in a much larger fraction of corporate ML pipelines than the SAP CAP packages did.

**Mitigation (incremental):**
- Pin away from `pytorch-lightning==2.6.2` and `==2.6.3`; verify nothing in your `requirements.txt` / `pyproject.toml` / Poetry / uv lockfiles still resolves to those.
- Treat any CI runner or developer machine that executed `import lightning` between 2026-04-30 publication and PyPI quarantine as compromised. Rotate every PyPI token, GitHub token, GitHub Actions secret, and cloud creds reachable from that host.
- Search GitHub for malicious commits whose `author.name` impersonates "Claude Code" or "Anthropic" but were not generated by your real Claude Code agents — high signal for compromised credentials.
- Continue all yesterday's mitigations: search for `.claude/settings.json` and `.vscode/tasks.json` plant artifacts; treat AI-agent config dirs as code that runs implicitly.

**Sources:** [The Hacker News — PyTorch Lightning Compromised in PyPI Supply Chain](https://thehackernews.com/2026/04/pytorch-lightning-compromised-in-pypi.html) | [Socket — pytorch-lightning 2.6.2/2.6.3 analysis](https://socket.dev) | [Aikido / OX Security / StepSecurity correlated reports](https://www.aikido.dev/blog/mini-shai-hulud-has-appeared) | [Yesterday's Watchtower CRITICAL entry](../30/report.md)

---

### SonicWall SonicOS Vulnerability Roll-Up — Eight CVEs Including Access-Control Bypass on Management API (CVSS up to 8.0)
**Product:** SonicWall NSA / TZ / NSv firewall appliances — 33 product variants | **CVE:** CVE-2026-0204 (CVSS 8.0), CVE-2026-0205 (6.8), CVE-2026-0206 (4.9), CVE-2026-0399, 0400, 0401, 0402, 3439 (each 4.9) | **CVSS:** 4.9–8.0 | **First reported:** 2026-04-30

SonicWall published a coordinated batch of eight SonicOS advisories on 2026-04-30. The headline issue is CVE-2026-0204: an access-control mechanism flaw exposing certain management functions under specific conditions (CVSS 8.0). CVE-2026-0205 is a path traversal (CVSS 6.8) granting access to restricted management services. The remaining six (CVE-2026-0206, 0399, 0400, 0401, 0402, 3439) are post-authentication denial-of-service crashes in the SonicOS API endpoints — stack-based buffer overflows, format-string bug, NULL deref, OOB read, and a certificate-handling buffer overflow. None are pre-auth RCE, but the access-control + path-traversal pair is a plausible chain that gets an unauthenticated network-adjacent attacker to data-exposing management endpoints.

**Mitigation:**
- Apply the vendor's combined SonicOS firmware update covering all eight CVEs; SonicWall's advisory page lists per-platform fixed builds.
- Continue restricting management-plane access (HTTPS UI, SSH) to known administrator IPs only — none of these flaws should be reachable from the internet on a hardened deployment.
- Hunt for crashes / unexpected reboots correlating with malformed HTTPS POSTs to SonicOS API endpoints in the past 30 days; the DoS issues have been silently exploitable since at least the affected firmware ship date.

**Sources:** [OpenCVE — SonicWall April 2026 batch](https://app.opencve.io/cve/?vendor=sonicwall&date=2026-04) | [SecurityWeek — SonicWall firewall flaws coverage](https://www.securityweek.com)

---

## 🟡 MEDIUM

### CVE-2026-32202 Windows Shell — UPDATE: Added to CISA KEV Catalog (Threat score 8, unchanged)
**Product:** Windows Shell (all currently supported) | **CVE:** CVE-2026-32202 | **Threat score:** 8 (unchanged) | **First reported:** 2026-04-28

CISA added CVE-2026-32202 to the KEV catalog on 2026-04-29 (relayed via The Hacker News; cisa.gov continues to return 403 to direct fetches). This codifies the Microsoft + Akamai 2026-04-27 confirmation of APT28 in-the-wild use as a federal patching mandate (BOD 22-01: federal agencies must patch within 21 days). For private-sector defenders, KEV listing primarily lifts the bug's priority in third-party scanner risk scoring and triggers compliance-driven patch SLAs.

**Why this is an update vs. yesterday's coverage:** the trigger is "KEV addition." Threat score stays at 8 — KEV listing is a defensive-urgency signal but does not change the underlying technical risk we already escalated yesterday.

**Mitigation:** continue the patch + SMB-egress hunt outlined in the 2026-04-29 entry; ensure the patch is queued in the federal-mandated 21-day window if you carry that obligation.

**Sources:** [The Hacker News — KEV addition coverage](https://thehackernews.com) | [Yesterday's Watchtower update](../29/report.md)

---

## 📋 Noted / Monitoring

**CVE-2026-31431 (Linux kernel "Copy Fail" `algif_aead` LPE)** — Out-of-remote-services scope, but PoC count exploded today: ≥6 distinct GitHub repos updated within the past hour (Python, C variants, detection rule sets). Still LPE only, but every Linux server / CI runner / jump host since kernel 4.14 (2017) is in scope. Schedule a kernel-update window for jump hosts, container hosts, and shared CI runners. Patched in 5.10.254+, 5.15.204+, 6.1.170+, 6.6.137+.

**CVE-2024-1708 (ConnectWise ScreenConnect path traversal, CVSS 8.4)** — Newly added to CISA KEV 2026-04-29. Old (2024) bug, but KEV listing implies fresh active-exploitation evidence; if you still operate ScreenConnect on-prem, confirm the 2024 patch is applied and check access logs for traversal attempts. Will not promote to a full Update — we never covered the original 2024 advisory and this is a routine federal-mandate signal, not a new technical development.

**CVE-2026-5403 / CVE-2026-5405 / CVE-2026-5656 (Wireshark 4.6.x / 4.4.x batch)** — DoS / memory-corruption flaws in SBC codec, RDP dissector, and profile-import path. CVSS 7.0–7.8; Wireshark is an analyst tool not internet-facing infra, but worth a routine update on SOC analyst workstations.

**CVE-2026-7551 (HKUDS OpenHarness, CVSS 8.8)** — RCE via malicious slash commands in the agent loop — yet another AI-agent CLI joining nginx-ui, mcp-atlassian, and chatgpt-mcp-server in the unauth-RCE-via-AI-tooling pattern. Niche deploy footprint right now.

**CVE-2026-7510 (OWASP DefectDojo ≤ 2.55.4, CVSS 6.3)** — Authorization bypass; many security teams self-host DefectDojo for AppSec triage — schedule the patch on internal AppSec tooling.

**CVE-2026-7505 (nextlevelbuilder GoClaw / GoClaw Lite ≤ 3.8.5, CVSS 7.3)** — Authorization flaw in a niche workflow plugin — naming overlap with OpenClaw is incidental (different vendor/product). Mention for OpenClaw-watching teams to avoid confusion.

**CVE-2026-7246 (Pallets Click, CVSS 7.2)** — Vulnerability in the widely used Python CLI library — review what your in-house tooling exposes.

**CVE-2026-41882 (JetBrains IntelliJ IDEA, CVSS 7.4)** — Developer-IDE issue; client-only, but worth a note in the AI-IDE / developer-tool security thread alongside Gemini CLI and Mini Shai-Hulud.

**CVE-2026-7503 (Code-projects For Plugin 4.1.2cu.5137, CVSS 8.8)** — Buffer overflow in wireless config function; niche IoT/router population.

**CVE-2026-7506 (SourceCodester Hotel Management System 1.0, CVSS 7.3)** — SQL injection; very niche, mention for completeness.

**CVE-2026-22726 (CloudFoundry route services bypass, CVSS 5.0)** — Routing bypass, lower severity, worth tracking on enterprise PaaS deployments.

**Sandhills Medical ransomware (170,000 records)** — Inc Ransom group, disclosed nearly a year after the breach. Healthcare credential-recovery pattern; useful incident-response reference.

**Checkmarx GitHub data leak** — Data exfiltrated 2026-03-30, malicious code published one week later. Still developing; if confirmed as a distinct supply-chain vector against AppSec vendor tooling, will promote next cycle.

**Anthropic Claude "Mythos" — 271 zero-days in Firefox 150** — AI-driven vulnerability discovery announcement (Schneier, 2026-04-29). No specific CVE list yet, but if the bug count is even half-true, expect a Mozilla advisory wave. Browser scope, lower defensive urgency for our perimeter, but track for AI-vulnscan trend.

**Bluekit phishing-as-a-service (40+ templates, AI campaign generator)** — Net-new commodity phishing kit observed in the wild 2026-04-30; brief the SOC's anti-phishing detection team.

**Brazilian "Huge Networks" anti-DDoS firm running DDoS attacks** — Krebs investigation 2026-04-30 — Python scripts target TP-Link routers via CVE-2023-1389; noted for CVE-2023-1389 trend signal and as an example of compromised security-vendor infrastructure.

**Cloudflare IPsec post-quantum (ML-KEM) general availability** — Not a vuln, but informational for crypto-migration planners; interoperability tested against Cisco and Fortinet.

**Romanian swatting-ring leader sentenced (4 years federal)** — Operational/judicial item, no defensive action.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (403) |
| Vendor advisories | rapid7.com, fortinet.com/blog/threat-research, msrc.microsoft.com/blog | ✅ / ⚠️ / ⚠️ |
| Research / OSINT | schneier.com, krebsonsecurity.com, googleprojectzero.blogspot.com, securitylab.github.com | ✅ / ✅ / ⚠️ / ⚠️ |
| CVE feeds | opencve.io, nvd.nist.gov, cve.org, cve.mitre.org, kb.cert.org/vuls | ✅ / ✅ / ❌ / ❌ / ⚠️ |
| GitHub / PoC | github.com/search, github.com/0xMarcio/cve | ✅ |
| Disclosure programs | hackerone.com/hacktivity, bugcrowd.com/disclosures, seclists.org/fulldisclosure | ❌ / ❌ / ✅ |
| Russian-language | dbugs.ptsecurity.com, avleonov.com, habr.com/ru/companies/tomhunter, teletype.in/@cyberok | ✅ / ⚠️ / ⚠️ / ⚠️ |
| Other | attackerkb.com, packetstormsecurity.com, blog.cloudflare.com/tag/security, cert.gov.ua | ❌ / ⚠️ / ✅ / ❌ |

**Errors:** cisa.gov + KEV (403), attackerkb.com (403), bugcrowd.com/disclosures (404), hackerone.com/hacktivity (JS-only, empty), cve.org (JS-only, empty), cve.mitre.org (redirects to cve.org, JS-only), cert.gov.ua (no content returned)
**Degraded (returned content but no recent / relevant data):** fortinet.com/blog/threat-research (latest 2026-04-17), securitylab.github.com (latest 2026-04-24), googleprojectzero.blogspot.com → projectzero.google (latest March 2026), packetstorm.news (homepage only), msrc.microsoft.com/blog (navigation only), avleonov.com (latest 2026-04-22), habr.com/ru/companies/tomhunter (latest March 2026), teletype.in/@cyberok (latest February 2026), kb.cert.org/vuls (latest 2026-04-23)
**CISA KEV:** 2 new additions confirmed via THN — CVE-2024-1708 (ConnectWise ScreenConnect) and CVE-2026-32202 (Windows Shell, covered as Update above) added 2026-04-29.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-01/night | Next: 2026-05-02/night*
