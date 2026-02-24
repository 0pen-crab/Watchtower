# Vulnerability Intelligence Report — 2026-02-24 Morning

**Generated:** 2026-02-24T08:00:00+02:00
**Cycle:** morning
**Sources checked:** 90/90

---

## 🔴 CRITICAL Findings

### 1. CVE-2026-21858 + CVE-2025-68613 — n8n "Ni8mare" Unauthenticated RCE Chain (CVSS 10.0)
- **Product:** n8n workflow automation platform
- **Impact:** Unauthenticated arbitrary file read (CVE-2026-21858) chained with expression injection sandbox bypass (CVE-2025-68613) for full RCE
- **Affected:** n8n <= 1.65.0 (AFR) / >= 0.211.0 (RCE)
- **Fixed:** 1.121.0 (AFR) / 1.120.4+ (RCE)
- **PoC:** Public exploit by Chocapikk (222 stars, automated Python script). AI-automated exploit development ~9h post-disclosure.
- **Attack chain:** Content-Type confusion → read /proc/self/environ → read config + SQLite DB → forge admin JWT → expression injection → sandbox bypass → RCE
- **Exposure:** Publicly accessible n8n instances found via LeakIX
- **Source:** github.com/Chocapikk/CVE-2026-21858, Cyera research
- **Priority:** PATCH IMMEDIATELY — public exploit, unauthenticated, internet-facing

### 2. CVE-2026-24061 — GNU inetutils telnetd Unauthenticated RCE
- **Product:** GNU inetutils telnetd (telnet server)
- **Impact:** Remote root shell without authentication via malformed USER environment variable
- **Affected:** GNU inetutils telnetd (bug present for 11 years)
- **PoC:** Public exploit by SafeBreach Labs (195 stars) + batch scanning tool
- **Source:** github.com/SafeBreach-Labs/CVE-2026-24061, Full Disclosure mailing list
- **Priority:** CRITICAL — trivial exploit, affects any exposed telnet server

### 3. CVE-2026-22200 — osTicket Arbitrary File Read + CNEXT RCE
- **Product:** osTicket helpdesk system
- **Impact:** PHP filter abuse via mPDF library for arbitrary file exfiltration, chainable to RCE via CVE-2024-2961 (CNEXT/glibc iconv)
- **PoC:** Public exploit by Horizon3.ai with full toolchain (file read, CNEXT payload gen, user enumeration, access link forging)
- **Source:** github.com/horizon3ai/CVE-2026-22200, Horizon3.ai blog
- **Priority:** CRITICAL — full exploit chain published

---

## 🟠 HIGH Findings

### 4. CVE-2026-21440 — AdonisJS Bodyparser Path Traversal → Arbitrary File Write
- **Product:** @adonisjs/bodyparser (Node.js)
- **Impact:** Critical path traversal allowing arbitrary file writing on the server
- **PoC:** Public writeup and PoC (27 stars)
- **Source:** github.com/k0nnect/cve-2026-21440-writeup-poc

### 5. CVE-2026-23745 — node-tar Arbitrary File Overwrite
- **Product:** node-tar (npm package)
- **Affected:** Versions < 7.5.3
- **Impact:** Arbitrary file overwrite via crafted tar archive
- **PoC:** Public (19 stars)
- **Source:** github.com/Jvr2022/CVE-2026-23745

### 6. ShinyHunters SSO Vishing Campaign — 100+ Organizations Targeted
- **Type:** Active threat campaign
- **Impact:** ShinyHunters extortion gang targeting SSO accounts at Okta, Microsoft Entra, and Google via sophisticated voice phishing. Compromised SSO provides access to all connected enterprise SaaS.
- **Victims:** Optimizely (confirmed breach Feb 11), Canada Goose, Panera Bread, Betterment, SoundCloud, PornHub, Figure, Match Group
- **TTPs:** Call impersonating IT support → phishing page mimicking login portal → real-time MFA relay → SSO takeover → data exfiltration from connected apps → extortion
- **Source:** BleepingComputer, silentpush.com
- **Priority:** HIGH — active campaign, over 100 targets

### 7. CVE-2025-41717 — Phoenix Contact TC Router Command Injection
- **Product:** Phoenix Contact TC Router 5004T-5G EU and others (TC ROUTER 3002T-3G, 2002T-3G)
- **Impact:** Authenticated command injection (High)
- **Fixed:** FW 1.06.23 / 3.08.8
- **Source:** Full Disclosure (CyberDanube Security Research)

### 8. CVE-2026-24070 / CVE-2026-24071 — Native Instruments Native Access macOS LPE (UNPATCHED)
- **Product:** Native Instruments Native Access (macOS), verified up to v3.22.0
- **Impact:** Local privilege escalation via DYLIB injection in privileged helper
- **Status:** UNPATCHED — vendor unresponsive to multiple contact attempts
- **Source:** SEC Consult Vulnerability Lab via Full Disclosure

### 9. February Linux Patch Wednesday — 632 Vulnerabilities
- **Overview:** Linux vendors addressed 632 CVEs in February, including 305 in Linux Kernel
- **In-the-wild exploitation confirmed:**
  - CVE-2026-2441 (Chrome/Chromium RCE) — *previously reported*
  - CVE-2025-14847 (MongoDB MongoBleed) — *previously reported*
- **Notable new public exploits (56 total):**
  - CVE-2026-24747: PyTorch RCE
  - CVE-2026-24049: Wheel RCE
  - CVE-2026-25916: Roundcube SFB
  - CVE-2025-15467, CVE-2025-69421, CVE-2025-11187: OpenSSL RCE variants
  - CVE-2025-12762, CVE-2025-13780: pgAdmin RCE
  - CVE-2026-21721: Grafana EoP
  - CVE-2024-21545: Proxmox VE AFR
- **Source:** avleonov.com (Vulristics report)

---

## 🟡 MEDIUM Findings

### 10. Android Mental Health Apps — 1,575 Vulnerabilities Across 10 Apps
- **Impact:** 14.7M installs affected. 54 high-severity, 538 medium-severity issues. One app had 85+ medium/high vulns. Exposed therapy data, session transcripts, mood logs, medication schedules.
- **Issues:** Intent hijacking, insecure local storage, hardcoded API keys, weak session token generation, no root detection
- **Source:** Oversecured research via BleepingComputer

### 11. CVE-2026-21509 — Microsoft Office RCE (Trending)
- **Product:** Microsoft Office
- **Impact:** Remote code execution — trending vulnerability per Positive Technologies
- **Source:** avleonov.com, PT Security

### 12. CVE-2026-20805 — Desktop Window Manager Information Disclosure (Trending)
- **Product:** Windows Desktop Window Manager
- **Impact:** Information disclosure — trending vulnerability
- **Source:** avleonov.com, PT Security

---

## 📋 Noted (Previously Reported / Updates)

| Item | Status |
|------|--------|
| CVE-2026-2441 (Chrome zero-day) | Confirmed ITW exploitation in Linux context |
| CVE-2026-1731 (BeyondTrust RS/PRA RCE) | Detailed Rapid7 analysis published on AttackerKB — same endpoint as CVE-2024-12356 |
| CVE-2025-14847 (MongoBleed) | Confirmed ITW exploitation in Linux context |
| CVE-2025-15467 (OpenSSL RCE) | Now confirmed with Linux public exploit |
| ShinyHunters campaign | Expanding — Optimizely is latest confirmed victim |

---

## Source Coverage

| Category | Checked | Accessible | Notes |
|----------|---------|------------|-------|
| Vuln databases (NVD, CVE.org, OSV, VulDB, OpenCVE, etc.) | 12/12 | 9 | cvedetails/vulners blocked by Cloudflare |
| CISA/CERT (CISA, CERT-EU, CERT-UA, CERT/CC) | 5/5 | 5 | |
| Vendor blogs (MS, Google, AWS, Atlassian, RedHat, Fortinet, etc.) | 10/10 | 10 | |
| Security news (Bleeping, THN, Krebs, HelpNet, SecurityWeek, DarkReading, etc.) | 10/10 | 10 | |
| Research blogs (Talos, Unit42, P0, CrowdStrike, Rapid7, Qualys, etc.) | 10/10 | 10 | |
| Reddit (netsec, blueteamsec, cybersec, RE, bugbounty) | 5/5 | 5 | |
| Full Disclosure / mailing lists | 2/2 | 2 | |
| GitHub (CVE repos, advisory DB, nuclei templates, trending) | 5/5 | 5 | |
| Bug bounty platforms (HackerOne, Bugcrowd) | 2/2 | 1 | Bugcrowd 404 |
| Exploit DBs (ExploitDB, PacketStorm, 0day.today, AttackerKB) | 4/4 | 3 | 0day.today hijacked |
| Twitter/X accounts (13 researchers/orgs) | 13/13 | 0 | Nitter proxies down; X requires auth |
| Russian/intl sources (Habr, CyberOK, avleonov, PT Security) | 4/4 | 4 | |
| Other (Schneier, tldrsec, risky.biz, SANS, etc.) | 8/8 | 7 | cybersecuritydispatch stale |
| **TOTAL** | **90/90** | **71** | 19 inaccessible (auth walls, Cloudflare, nitter down) |
