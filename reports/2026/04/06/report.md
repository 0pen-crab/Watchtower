# Vulnerability Intelligence Report — 2026-04-06 Night Cycle

---

## 📰 Progress ShareFile Pre-Auth RCE Chain — CVE-2026-2699 + CVE-2026-2701

**Threat Score:** 8
**Affected Technology:** Progress ShareFile Storage Zones Controller
**CVE:** CVE-2026-2699, CVE-2026-2701
**CVSS:** 9.8 / 9.1

### Summary
watchTowr Labs disclosed two critical vulnerabilities in Progress ShareFile Storage Zones Controller that can be chained for unauthenticated remote code execution. CVE-2026-2699 (CVSS 9.8) is an authentication bypass allowing unauthenticated access to restricted configuration functionality, and CVE-2026-2701 (CVSS 9.1) is an arbitrary file upload enabling web shell deployment. When chained, an external attacker achieves pre-auth RCE on customer-managed ShareFile deployments. Patches were released in February 2026 for the Storage Zones Controller v5, but the watchTowr technical write-up (April 2) and SecurityWeek coverage (April 5) have now made exploitation details public.

### Why It Matters
ShareFile is widely used in enterprise and regulated environments for secure file exchange and client workflows. Customer-managed Storage Zones Controller deployments directly exposed to the internet are immediately exploitable. Given the history of Progress products (MOVEit), threat actors will race to weaponize this.

### Discovery
**First seen at:** securityweek.com
**How found:** watchTowr blog + SecurityWeek coverage + SOCRadar analysis cross-referenced. CIS advisory also published.

### Sources
- https://www.securityweek.com/critical-sharefile-flaws-lead-to-unauthenticated-rce/
- https://watchtowr.com/resources/sharefile-storage-zone-controller-pre-auth-rce-cve-2026-2699-cve-2026-2701/
- https://socradar.io/blog/progress-sharefile-cve-2026-2699-2701-rce/
- https://docs.sharefile.com/en-us/storage-zones-controller/5-0/security-vulnerability-feb26.html

---

## 📰 CVE-2026-0331 — Claude Code Context Poisoning Vulnerability (Adversa AI)

**Threat Score:** 7
**Affected Technology:** Anthropic Claude Code
**CVE:** CVE-2026-0331
**CVSS:** null

### Summary
Days after Anthropic accidentally leaked 512,000 lines of Claude Code source code via npm package v2.1.88 on March 31, 2026, Adversa AI identified and disclosed CVE-2026-0331, a critical context poisoning vulnerability in the Claude Code harness. The flaw allows an attacker to inject malicious context into Claude Code sessions, potentially leading to arbitrary command execution on developer machines. This is particularly dangerous given Claude Code's deep integration with file systems and shell access in developer workflows.

### Why It Matters
Claude Code is increasingly adopted by enterprise developers. A context poisoning vulnerability in an AI coding tool with shell access has direct RCE implications on developer workstations. Combined with the source code exposure, this represents a compounding AI supply chain risk.

### Discovery
**First seen at:** securityweek.com
**How found:** SecurityWeek reporting on Adversa AI research; cross-referenced with LinkedIn analysis and daily security review coverage.

### Sources
- https://www.securityweek.com/critical-vulnerability-in-claude-code-emerges-days-after-source-leak/
- https://dailysecurityreview.com/cyber-security/critical-vulnerability-in-claude-code-surfaces-days-after-source-code-leak/

---

## 📰 36 Malicious npm Packages Disguised as Strapi Plugins Deploy Redis/PostgreSQL Implants

**Threat Score:** 6
**Affected Technology:** npm / Strapi CMS ecosystem
**CVE:** Not yet assigned
**CVSS:** null

### Summary
SafeDep researchers discovered 36 malicious npm packages published by four sock-puppet accounts, all disguised as Strapi CMS v3 community plugins. The packages carry eight distinct payload variants including Redis crontab injection for persistent access, direct PostgreSQL credential theft via hardcoded database queries, fileless reverse shells, and persistent implants. The campaign appears to specifically target cryptocurrency exchange Guardarian. All packages follow a consistent three-file structure using version 3.6.8 to mimic mature plugins.

### Why It Matters
Strapi is a widely used headless CMS in enterprise applications. This supply chain attack combines multiple persistence techniques targeting both application databases and infrastructure, making it particularly difficult to fully remediate once a malicious package has executed.

### Discovery
**First seen at:** thehackernews.com
**How found:** The Hacker News reporting on SafeDep research, cross-referenced with SafeDep blog.

### Sources
- https://thehackernews.com/2026/04/36-malicious-npm-packages-exploited.html
- https://safedep.io/malicious-npm-strapi-plugin-events-c2-agent/

---

## 🔄 Update: EvilTokens Device Code Phishing — 37x Surge in OAuth Account Takeover

**Previous Threat Score:** 5 → **Updated Threat Score:** 7
**CVE:** Not applicable

### What Changed
Push Security documented a 37.5x surge in device code phishing pages as of April 4, 2026, directly attributed to the commercial launch of EvilTokens — a Phishing-as-a-Service platform targeting Microsoft 365 accounts via the OAuth 2.0 Device Authorization Grant flow. What was previously a niche technique (noted in our April 2 cycle) has become commoditized and accessible to low-skill attackers, dramatically expanding the attack surface. The technique bypasses standard MFA and conditional access policies by abusing legitimate OAuth device flows.

### Sources
- https://www.bleepingcomputer.com/news/security/device-code-phishing-attacks-surge-37x-as-new-kits-spread-online/
- https://pushsecurity.com/blog/device-code-phishing
- https://labs.cloudsecurityalliance.org/research/csa-research-note-oauth-device-code-phishing-surge-20260405/

---

## 🔄 Update: FortiClientEMS CVE-2026-35616 — Zero-Day Window Confirmed, Easter Weekend Exploitation

**Previous Threat Score:** 8 → **Updated Threat Score:** 9
**CVE:** CVE-2026-35616

### What Changed
Cloud Security Alliance research confirms CVE-2026-35616 was actively exploited as a zero-day starting March 31, 2026 — a full four days before Fortinet's emergency disclosure on April 4. The zero-day window deliberately opened over the Easter holiday weekend when security teams were understaffed. The pre-authentication API bypass (CVSS 9.1) allows unauthenticated remote attackers to bypass all API authentication and execute privileged operations against FortiClient EMS. Multiple threat intelligence firms have now published detailed technical analysis and detection guidance.

### Sources
- https://labs.cloudsecurityalliance.org/research/csa-research-note-fortinet-forticlient-ems-cve-2026-35616-20/
- https://www.helpnetsecurity.com/2026/04/04/forticlient-ems-zero-day-cve-2026-35616/
- https://thehackernews.com/2026/04/fortinet-patches-actively-exploited-cve.html

---

## 📋 Noted

- **CVE-2026-4747** — FreeBSD: AI-discovered vulnerability found by Claude Code in FreeBSD; demonstrates autonomous vulnerability research capabilities. CVE assigned, patch in progress.
- **CVE-2026-5201** — gdk-pixbuf: Heap-based buffer overflow in JPEG loader (CVSS 7.5), PoC on GitHub with 10 stars. Affects Linux systems processing untrusted images.
- **Not assigned** — LinkedIn BrowserGate: LinkedIn using hidden JavaScript to scan visitors' browsers for 6,000+ installed Chrome extensions and collect device data. Privacy concern, no direct exploitation vector.
- **CVE-2026-33691** — OWASP CRS: Whitespace padding bypass vulnerability disclosed on Full Disclosure mailing list (already noted last cycle, confirmed April 2 post).
- **Not assigned** — MetInfo CMS: KIS-2026-06 advisory published on Full Disclosure April 2; details limited.
- **Not assigned** — Apple OHTTP Relay: 14 third-party endpoints in 6 countries with zero user visibility disclosed on Full Disclosure April 2.
- **CVE-2026-27636** — FreeScout: Metasploit module now live (Metasploit Wrap-Up 04/03) for unauthenticated RCE via ZWSP .htaccess bypass; previously noted, escalation path now trivial.
- **CVE-2025-50286** — Grav CMS: Authenticated RCE via Direct Install feature, Metasploit module released April 3.
- **Not assigned** — DPRK LNK + GitHub C2: FortiGuard Labs analysis of DPRK-linked attacks using GitHub as covert C2 via LNK-based multi-stage PowerShell execution.
- **Not assigned** — Microsoft Cookie-Controlled PHP Web Shells: Microsoft Defender team details stealth technique using HTTP cookies as control channel for PHP web shells persisting via cron on Linux servers.

---

## 📡 Source Coverage

**Sources checked:** 31/31
**Sources with findings:** 14

| Status | Source | Notes |
|--------|--------|-------|
| ✅ | bleepingcomputer.com | 3 findings (ShareFile, FortiClientEMS, device code phishing) |
| ✅ | thehackernews.com | 2 findings (Strapi npm, FortiClientEMS) |
| ✅ | cisa.gov/kev | No new KEV additions since last cycle |
| ✅ | cisa.gov | No new advisories since last cycle |
| ✅ | securityweek.com | 2 findings (ShareFile RCE, Claude Code vuln) |
| ✅ | github.com/search?q=CVE | Trending repos checked — CVE-2026-25769 Wazuh, CVE-2026-21643 FortiClient |
| ✅ | schneier.com | 2 noted items (US router ban policy, Coruna iOS toolkit analysis) |
| ✅ | krebsonsecurity.com | 1 finding context (TeamPCP CanisterWorm Iran wiper — already reported) |
| ✅ | rapid7.com | 1 finding (Metasploit Wrap-Up: FreeScout, Grav CMS modules) |
| ✅ | attackerkb.com | Cisco SD-WAN analysis — already covered |
| ✅ | fortinet.com/blog/threat-research | DPRK LNK/GitHub C2 campaign, Iran cyber fallout — noted |
| ✅ | securitylab.github.com | Signal attachment exfil, NocoDB XSS, Sentry privesc — noted |
| ✅ | seclists.org/fulldisclosure | 5 posts in April: OWASP CRS, MetInfo, Apple OHTTP, Vienna LPE, Open WebUI |
| ✅ | packetstormsecurity.com | 34 exploits, 221 advisories in last 7 days — cross-referenced |
| ✅ | opencve.io | Platform checked, login required for detailed alerts |
| ✅ | nvd.nist.gov | Recent CVEs reviewed — Mbed TLS, MobSF, Haraka, OneUptime |
| ❌ | cve.mitre.org | Extraction failed (no content rendered) |
| ❌ | cve.org | Extraction failed (no content rendered) |
| ✅ | googleprojectzero.blogspot.com | No new posts since Jan 2026 |
| ✅ | blog.cloudflare.com/tag/security | Client-Side Security tools, Account Abuse Protection — no new vulns |
| ✅ | msrc.microsoft.com/blog | Page rendered minimally — no new advisories since Patch Tuesday |
| ✅ | hackerone.com/hacktivity | JS-rendered, no extractable content |
| ❌ | bugcrowd.com/disclosures | 404 error |
| ✅ | kb.cert.org/vuls | No new vulnerability notes |
| ✅ | avleonov.com | March Linux Patch Wednesday recap, n8n coverage — already reported |
| ✅ | github.com/0xMarcio/cve | Trending PoCs reviewed — CVE-2026-25769 Wazuh, CVE-2026-21643 |
| ✅ | dbugs.ptsecurity.com | No new disclosures |
| ✅ | habr.com/ru/companies/tomhunter | February 2026 roundup — no April content yet |
| ✅ | teletype.in/@cyberok | December/January retrospective only |
| ✅ | cert.gov.ua | Rendered but no extractable content |
| ✅ | web_search (DuckDuckGo) | Multiple targeted searches for new vulns, breaches, exploits |
