# Vulnerability Intelligence Report — 2026-03-17 / Night

**Cycle:** Night (2026-03-17 00:00 UTC)
**Generated:** 2026-03-17T02:00:00+02:00 (Athens)
**Previous report:** 2026-03-12/night (5-day gap — overnight backlog scan)

---

## 📰 Wing FTP Server Path Disclosure Added to CISA KEV — Actively Chained for RCE

**Threat Score:** 7
**Affected Technology:** Wing FTP Server (v7.4.3 and earlier)
**CVE:** CVE-2025-47813
**CVSS:** 5.3 (Medium — standalone; critical in RCE chain context)

### Summary
CVE-2025-47813, an information disclosure flaw in Wing FTP Server that leaks the full local installation path via an oversized UID cookie error message, was added to the CISA KEV catalog on March 16, 2026 after CISA confirmed attackers are actively chaining it with the critical RCE bug CVE-2025-47812 to achieve full remote code execution. The developer patched both in May 2025 (v7.4.4), but unpatched servers remain exposed — and the CVE-2025-47812 RCE exploit was already being exploited one day after its technical details dropped publicly. Wing FTP Server is used by 10,000+ organizations including the US Air Force, Sony, Airbus, Reuters, and Sephora. A public PoC for CVE-2025-47813 was published by discoverer Julien Ahrens in June 2025. BOD 22-01 agencies have two weeks to patch; all organizations should treat this as urgent.

### Why It Matters
FTP servers are often deployed on internet-facing infrastructure and overlooked in patch cycles. The combined CVE-2025-47812 + CVE-2025-47813 chain provides unauthenticated RCE — a full takeover primitive — and confirmed exploitation in the wild makes this immediately actionable.

### Discovery
**First seen at:** bleepingcomputer.com
**How found:** BleepingComputer homepage featured article + cross-referenced with CISA KEV catalog addition dated 2026-03-16.

### Sources
- https://www.bleepingcomputer.com/news/security/cisa-flags-wing-ftp-server-flaw-as-actively-exploited-in-attacks/
- https://nvd.nist.gov/vuln/detail/CVE-2025-47813
- https://www.cisa.gov/news-events/alerts/2026/03/16/cisa-adds-one-known-exploited-vulnerability-catalog

---

## 📰 Two Chrome Zero-Days (Skia + V8) Added to CISA KEV — Targeted Exploitation Confirmed

**Threat Score:** 9
**Affected Technology:** Google Chrome (all platforms)
**CVE:** CVE-2026-3909 (Skia heap corruption), CVE-2026-3910 (V8 type confusion)
**CVSS:** Not yet published

### Summary
Google patched two actively exploited Chrome zero-days — CVE-2026-3909, a heap corruption in the Skia graphics engine, and CVE-2026-3910, a type confusion in the V8 JavaScript engine — both added to the CISA KEV catalog on March 13, 2026, indicating confirmed nation-state targeted exploitation. No public PoC exists, but Google's advisory acknowledged exploitation "in the wild" prior to patch release, consistent with prior Chrome zero-day patterns where exploitation was observed weeks before discovery by Google's Threat Analysis Group. Patches were pushed via Chrome stable channel updates; users and organizations running auto-update should verify version ≥124.x.

### Why It Matters
Browser zero-days on CISA KEV are among the highest-signal indicators of active nation-state operations. Enterprise endpoints running unmanaged or stale Chrome versions — especially in environments without forced update policies — are directly exposed. Both Skia and V8 bugs historically enable renderer exploitation that can be chained with sandbox escapes.

### Discovery
**First seen at:** thehackernews.com
**How found:** THN homepage and cross-referenced CISA KEV catalog entries dated 2026-03-13.

### Sources
- https://thehackernews.com/
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog

---

## 📰 GlassWorm ForceMemo — Mass Force-Push Supply Chain Attack Compromises Hundreds of Python Repos

**Threat Score:** 8
**Affected Technology:** Python/PyPI ecosystem (GitHub-hosted repositories)
**CVE:** Not assigned
**CVSS:** N/A

### Summary
A new GlassWorm campaign offshoot dubbed ForceMemo has been actively compromising hundreds of Python GitHub repositories since March 8, 2026 by leveraging stolen GitHub OAuth tokens (exfiltrated by GlassWorm from developer systems via malicious VS Code/Cursor extensions) to silently rebase and force-push obfuscated cryptocurrency-stealing and data-exfiltration payloads into files named setup.py, main.py, and app.py — preserving original commit metadata to evade detection, making `pip install` or cloning the repo a full infection vector. The payload skips Russian-locale systems and retrieves dynamic C2 instructions via a Solana wallet memo field (operational since November 2025); the Aikido-linked wave already compromised 151+ repos using invisible Unicode character obfuscation. Affected projects include Django apps, ML research code, Streamlit dashboards, and published PyPI packages.

### Why It Matters
Supply chain attacks via GitHub token compromise are exceptionally hard to detect at the enterprise boundary — the malicious code appears as a legitimate commit from a known developer. Any CI/CD pipeline that installs Python dependencies from GitHub source (rather than verified PyPI hashes) is a direct infection path.

### Discovery
**First seen at:** thehackernews.com
**How found:** THN article (Mar 16) on GlassWorm ForceMemo; corroborated by StepSecurity and Aikido Security research; SecurityWeek confirmed additional repository counts.

### Sources
- https://thehackernews.com/2026/03/glassworm-attack-uses-stolen-github.html
- https://www.stepsecurity.io/blog/forcememo-hundreds-of-github-python-repos-compromised-via-account-takeover-and-force-push

---

## 📰 CVE-2025-33073 — NTLM Reflection SMB Exploit at 658 GitHub Stars

**Threat Score:** 7
**Affected Technology:** Windows Active Directory / SMB / NTLM
**CVE:** CVE-2025-33073
**CVSS:** Not yet published

### Summary
A high-traction public exploit for CVE-2025-33073, an NTLM reflection vulnerability in Windows SMB, has accumulated 658 GitHub stars in the 0xMarcio/cve tracker — indicating rapid community interest and likely real-world adoption — enabling attackers with network-layer access to capture NTLM authentication hashes and relay them for lateral movement, privilege escalation, or domain compromise in Active Directory environments. No patch status confirmed from the current scan; organizations should evaluate SMB signing enforcement and NTLM relay mitigations as immediate compensating controls. The exploit popularity suggests mass scanning and opportunistic exploitation is underway or imminent.

### Why It Matters
NTLM relay and reflection attacks remain the most reliable lateral movement primitive in Windows enterprise networks. With 658 stars, this exploit is firmly in the toolbox of pentesters and threat actors alike — expect it in ransomware pre-encryption reconnaissance playbooks.

### Discovery
**First seen at:** github.com/0xMarcio/cve
**How found:** GitHub 0xMarcio/cve tracker identified as 658-star repo; identified during nightly scan of high-traction exploit repositories.

### Sources
- https://github.com/mverschu/CVE-2025-33073
- https://github.com/0xMarcio/cve

---

## 📰 Rocket.Chat Authentication Bypass — CVE-2026-28514 and CVE-2026-30833

**Threat Score:** 7
**Affected Technology:** Rocket.Chat (self-hosted instances)
**CVE:** CVE-2026-28514, CVE-2026-30833
**CVSS:** Not yet published

### Summary
GitHub Security Lab published a coordinated disclosure for two authentication bypass vulnerabilities in Rocket.Chat — CVE-2026-28514 and CVE-2026-30833 — that chain to allow unauthenticated attackers to bypass login controls and gain unauthorized access to the open-source collaboration platform, which is widely deployed as a self-hosted Slack alternative in enterprises, government agencies, and critical infrastructure organizations. The advisory was published with full technical details by researchers Man Yue Mo and Peter Stöckli at GHSL; patch version and due date are not yet confirmed from current scan. Organizations running self-hosted Rocket.Chat instances should treat this as an urgent patch priority and consider disabling public registration as a temporary mitigation.

### Why It Matters
Authentication bypass in a widely deployed collaboration platform is an immediate threat to organizational communications security — attackers gaining access can exfiltrate sensitive conversations, pivot to internal systems via integrations, and harvest credentials shared in chat.

### Discovery
**First seen at:** securitylab.github.com
**How found:** GitHub Security Lab homepage listing of recent advisories; cross-referenced with available CVE records.

### Sources
- https://securitylab.github.com/
- https://securitylab.github.com/advisories/

---

## 📰 DRILLAPP — Laundry Bear Deploys Edge-Abusing Backdoor Against Ukrainian Targets

**Threat Score:** 6
**Affected Technology:** Microsoft Edge (headless debugging API — LOLBAS technique)
**CVE:** Not assigned
**CVSS:** N/A

### Summary
Russian threat actor Laundry Bear (UAC-0190 / Void Blizzard) has been running a campaign since February 2026 deploying the DRILLAPP JavaScript backdoor against Ukrainian judicial and charity organizations, using LNK lures (Starlink installation and Come Back Alive charity themes) that launch Microsoft Edge in headless mode with disabled security settings (--no-sandbox, --disable-web-security) to silently capture webcam, microphone, screen, and local file system data — exfiltrating over WebSocket to a C2 resolved via Pastefy dead-drop — representing a living-off-the-land browser abuse technique with no malicious binary on disk. The campaign shares infrastructure overlaps with PLUGGYAPE, a prior Laundry Bear tool that abused Signal for C2, confirming the group's preference for trusted applications as operational cover.

### Why It Matters
While currently targeting Ukrainian entities, Laundry Bear's LOLBAS browser-abuse technique is platform-agnostic and infrastructure-independent — any organization with Edge deployed could face similar campaigns using localized social engineering lures. The no-binary-on-disk approach evades most EDR detection.

### Discovery
**First seen at:** thehackernews.com
**How found:** THN article (Mar 16) based on S2 Grupo LAB52 threat intelligence report.

### Sources
- https://thehackernews.com/2026/03/drillapp-backdoor-targets-ukraine.html
- https://lab52.io/blog/drillapp-new-backdoor-targeting-ukrainian-entities-with-possible-links-to-laundry-bear/

---

## 🔄 Update: Stryker Wiper Attack — Confirmed Tens of Thousands of Devices Destroyed, No Malware Used

**Previous Threat Score:** 10 → **Updated Threat Score:** 10
**CVE:** Not applicable

### What Changed
The Handala wiper attack against Stryker (first reported 2026-03-11, updated 2026-03-12) is now confirmed to have destroyed data on **tens of thousands of endpoint devices** — significantly more than the initial "5,000 workers sent home" estimate — and forensic analysis has concluded the attackers achieved mass destruction **without deploying any malware binary**, instead relying entirely on legitimate Windows admin tooling and living-off-the-land techniques to wipe device data at scale. This "no malware needed" revelation fundamentally changes the forensic and detection picture: there is no dropper, no payload, no signature to hunt. The attack represents a new tier of destructive capability achievable through supply chain access to legitimate enterprise management tools. Irish authorities confirmed cross-border impact on Stryker's European operations.

### Sources
- https://www.bleepingcomputer.com/ (featured: "Stryker attack wiped tens of thousands of devices, no malware needed")
- https://krebsonsecurity.com/

---

## 📋 Noted

- **CVE-2026-3909 / CVE-2026-3910** — Google Chrome: See full findings above; additional context — exploitation assessed as nation-state targeted, not mass exploitation yet; update to score 9+ if mass scanning detected.
- **CVE-2025-55182** — Meta React Server Components / Next.js: Critical pre-auth RCE (CVSS unscored) in React Server Components 19.x; added to CISA KEV Dec 5, 2025; China-nexus groups (per AWS Threat Intel) are actively exploiting in ongoing campaigns — 1,356+ GitHub stars on PoC repos; pre-dates our 30-day window but ongoing exploitation wave warrants monitoring.
- **CVE-2026-4224** — Expat XML library: C stack overflow when parsing deeply nested XML content model definitions; no PoC, widely embedded in software stacks including Python, Firefox, and Apache; no KEV.
- **CVE-2026-21440** — AdonisJS bodyparser: Path traversal enabling arbitrary file write (previously reported 2026-02-24, ts=7); now at 27 GitHub stars on two PoC repos — no confirmed exploitation yet.
- **CVE-2026-24061** — GNU inetutils-telnetd: Remote authentication bypass (CISA KEV); new PoC batch scanning tool released within last 24 hours; previously reported 2026-03-07/night, but PoC proliferation continues.
- **CVE-2025-10010** — CryptoPro Secure Disk for BitLocker: Multiple vulnerabilities disclosed via Full Disclosure (Mar 12); niche enterprise product, low mass-exploitation risk.
- **Cohesity TranZman Migration Appliance** — 5 CVEs including command injection, LPE, unsigned patches, and weak crypto; disclosed via Full Disclosure (Mar 12); affects enterprise data management/migration appliance.
- **Alipay DeepLink+JSBridge** — 17 vulns, 6 CVEs, CVSS 9.3 attack chain enabling silent GPS exfiltration via DeepLink and JSBridge abuse; disclosed via Full Disclosure (Mar 12); primarily affects mobile Alipay super-app but JSBridge patterns transferable to other mobile platforms.
- **CVE-2026-25177** — Active Directory SPN Unicode Collision: Scanner released targeting detection of exploitation on Domain Controllers; no CVE details confirmed from scan — monitoring.
- **CVE-2026-29000** — Unknown product: Two fresh PoC repos appeared in last 24 hours; no description available from scan — requires follow-up.
- **Apple iOS 15.8.7 / iOS 16.7.15** — Apple: Security updates released March 11 for legacy iOS versions; likely patch for previously disclosed vulnerabilities.
- **Storm-2561** — Microsoft threat actor: Active credential theft campaign targeting VPN users via phishing infrastructure; no CVE, social engineering vector.
- **Oracle EBS breach follow-up** — Four Fortune 500 companies (Broadcom, Bechtel, Estée Lauder, Abbott) confirmed as victims of the March 2026 Oracle E-Business Suite breach but have not issued public statements; attack scope expanding.
- **AppsFlyer Web SDK** — Mobile analytics: Web SDK hijacked to distribute crypto-stealing JavaScript code; supply chain compromise affecting downstream mobile app analytics integrations.
- **CL-STA-1087** — Chinese APT: Targeting Southeast Asian military networks; intelligence collection focus, no exploited CVE reported.
- **CVE-2026-26119** — Windows Admin Center: Vulnerability disclosed Mar 16; insufficient detail from scan for scoring — monitoring.

---

## 📡 Source Coverage

**Sources checked:** 30/30
**Sources with findings:** 12

| Status | Source | Notes |
|--------|--------|-------|
| ✅ | bleepingcomputer.com | Wing FTP, Stryker update, AppsFlyer, Exchange outage |
| ✅ | thehackernews.com | GlassWorm/ForceMemo, Chrome 0-days, DRILLAPP |
| ✅ | cisa.gov/known-exploited-vulnerabilities-catalog | CVE-2025-47813, CVE-2026-3909/3910 additions confirmed |
| ✅ | cisa.gov | Same domain — covered |
| ✅ | securityweek.com | Oracle EBS update, GlassWorm context, CL-STA-1087 |
| ✅ | github.com/search?q=CVE | CVE-2025-33073 (658★), CVE-2026-2441 PoC, mass CVE-2026-24061 scanners |
| ✅ | schneier.com | No in-scope findings |
| ✅ | krebsonsecurity.com | Stryker wiper no-malware revelation |
| ✅ | rapid7.com | Cisco SD-WAN context, WordPress stealer context |
| ✅ | attackerkb.com | CVE-2026-20127 deep-dive published |
| ✅ | fortinet.com/blog/threat-research | Iran cyber retaliation risk, EncystPHP FreePBX |
| ✅ | securitylab.github.com | Rocket.Chat CVE-2026-28514/30833, Zammad IDOR (in dedup) |
| ✅ | seclists.org/fulldisclosure | 7 March 2026 posts: Alipay, Cohesity, CryptoPro, Apple iOS, AppLocker bypass |
| ⚠️ | packetstormsecurity.com | Returned ToS redirect page — stats only, no article listing |
| ✅ | opencve.io | CVE-2026-4224 (Expat), CVE-2026-20841 (Notepad), CVE-2026-26119 |
| ✅ | nvd.nist.gov | CVE-2025-55182 (React RCE KEV), CVE-2026-24061 context |
| ⚠️ | cve.mitre.org | Redirected to cve.org search — empty result rendering |
| ⚠️ | cve.org | Minimal page content — search results not rendering |
| ✅ | googleprojectzero.blogspot.com | No new in-scope findings |
| ✅ | blog.cloudflare.com/tag/security | No in-scope vulnerability findings |
| ⚠️ | msrc.microsoft.com/blog | Minimal content returned — blocked/JS-required |
| ❌ | hackerone.com/hacktivity | Requires authentication — no public content accessible |
| ❌ | bugcrowd.com/disclosures | 404 — page appears removed/restructured |
| ⚠️ | kb.cert.org/vuls | Minimal page content — search form only, no listing |
| ✅ | avleonov.com | CVE-2026-21519/21533 (Feb Patch Tuesday, in dedup) — no new findings |
| ✅ | github.com/0xMarcio/cve | CVE-2025-55182 (1356★), CVE-2025-33073 (658★), CVE-2026-21858 (in dedup) |
| ⚠️ | dbugs.ptsecurity.com | Minimal content — footer-only rendering |
| ✅ | habr.com/ru/companies/tomhunter/articles | Most recent: Feb 2026 roundup — no March content |
| ✅ | teletype.in/@cyberok | Most recent: Dec/Jan top-vuln roundup — no March content |
| ❌ | cert.gov.ua | Empty response body |
