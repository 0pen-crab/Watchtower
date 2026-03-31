# Vulnerability Intelligence Report — 2026-03-31 (Night Cycle)

---

## 📰 CVE-2026-21643 — FortiClient EMS SQL Injection Under Active Exploitation

**Threat Score:** 8
**Affected Technology:** Fortinet FortiClient EMS 7.4.4
**CVE:** CVE-2026-21643
**CVSS:** 9.1

### Summary
A critical SQL injection vulnerability in Fortinet's FortiClient Endpoint Management Server (EMS) version 7.4.4 allows unauthenticated attackers to execute arbitrary SQL commands via maliciously crafted HTTP requests targeting the web GUI's "Site" header. Threat intelligence firm Defused confirmed active exploitation began approximately 4 days ago (around March 26). Shodan shows close to 1,000 publicly exposed FortiClient EMS instances, while Shadowserver tracks over 2,000 exposed web interfaces globally — primarily in the US and Europe. Fortinet has not yet updated their advisory to flag in-the-wild exploitation, though a patch is available in version 7.4.5+.

### Why It Matters
FortiClient EMS is a centralized endpoint management platform deployed in enterprise environments — compromise turns the management server into a pivot point giving attackers the same access paths as administrators. Fortinet vulnerabilities are frequently exploited in ransomware and cyber-espionage campaigns; CISA has flagged 24 Fortinet CVEs as actively exploited, 13 in ransomware attacks.

### Discovery
**First seen at:** bleepingcomputer.com
**How found:** BleepingComputer article citing Defused threat intelligence confirming first exploitation. Cross-referenced with HelpNetSecurity, CSO Online, and CyberSecurityNews.

### Sources
- https://www.bleepingcomputer.com/news/security/critical-fortinet-forticlient-ems-flaw-now-exploited-in-attacks/
- https://www.helpnetsecurity.com/2026/03/30/forticlient-ems-cve-2026-21643-reported-exploitation/
- https://www.csoonline.com/article/4152117/fortinet-hit-by-another-exploited-cybersecurity-flaw.html
- https://fortiguard.fortinet.com/psirt/FG-IR-25-1142

---

## 🔄 Update: CVE-2026-3055 — Citrix NetScaler SAML Memory Overread Added to CISA KEV, Active Exploitation Confirmed

**Previous Threat Score:** 7 → **Updated Threat Score:** 9
**CVE:** CVE-2026-3055

### What Changed
CISA added CVE-2026-3055 to the Known Exploited Vulnerabilities catalog on March 30 with a remediation deadline of April 2 — a 3-day deadline indicating critical urgency. Active exploitation in the wild is now confirmed by multiple sources including Rapid7, who published a detailed technical analysis. The Hacker News weekly recap leads with this as the top threat. The vulnerability allows attackers to leak application memory from NetScaler appliances configured as SAML Identity Providers, potentially exposing authenticated administrative session IDs that enable full appliance takeover. A public PoC exploit is now available on GitHub.

### Sources
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://www.rapid7.com/blog/post/etr-cve-2026-3055-citrix-netscaler-adc-and-netscaler-gateway-out-of-bounds-read/
- https://www.bleepingcomputer.com/news/security/critical-citrix-netscaler-memory-flaw-actively-exploited-in-attacks/
- https://thehackernews.com/2026/03/weekly-recap-telecom-sleeper-cells-llm.html
- https://github.com/0xBlackash/CVE-2026-3055

---

## 🔄 Update: CVE-2025-53521 — F5 BIG-IP Reclassified from DoS to Critical RCE, Webshells Deployed in Wild

**Previous Threat Score:** 7 → **Updated Threat Score:** 9
**CVE:** CVE-2025-53521

### What Changed
F5 has reclassified CVE-2025-53521 from a high-severity denial-of-service vulnerability to a critical-severity remote code execution flaw in BIG-IP APM. Attackers are actively exploiting it to deploy webshells on unpatched devices. This represents a significant escalation from the initial assessment when it was added to CISA KEV on March 27 — the impact has gone from service disruption to full code execution and persistent access.

### Sources
- https://www.bleepingcomputer.com/news/security/hackers-now-exploit-critical-f5-big-ip-flaw-in-attacks-patch-now/
- https://www.securityweek.com/f5-big-ip-dos-flaw-upgraded-to-critical-rce-now-exploited-in-the-wild/

---

## 🔄 Update: DarkSword iOS Exploit Kit — Russian APT Star Blizzard (FSB) Now Adopted

**Previous Threat Score:** 8 → **Updated Threat Score:** 9
**CVE:** CVE-2026-20700, CVE-2025-43529, CVE-2025-14174, CVE-2025-31277, CVE-2025-43510, CVE-2025-43520

### What Changed
SecurityWeek reports that Star Blizzard (FSB-linked, also known as SEABORGIUM/Callisto Group), a state-sponsored Russian APT, has adopted the DarkSword iOS exploit kit for its campaigns. Previously attributed only to UNC6353 (Russia-linked) targeting Ukraine, the kit is now being used by Star Blizzard to target government, higher education, financial, and legal entities as well as think tanks globally. This significantly expands the threat scope from a targeted Ukraine operation to broader Western intelligence-collection operations.

### Sources
- https://www.securityweek.com/russian-apt-star-blizzard-adopts-darksword-ios-exploit-kit/

---

## 📋 Noted

- **CVE-2026-0766** — OpenWebUI: Remote code execution vulnerability with PoC on GitHub (ZDI-published). AI tool with growing deployment but limited enterprise exposure currently.
- **CVE-2026-26111** — Windows RRAS: Integer overflow RCE patched in March 2026 Patch Tuesday. A GitHub researcher claims successful exploitation on fully patched systems, suggesting incomplete patching — unconfirmed, monitoring.

---

## 📡 Source Coverage

**Sources checked:** 30/30
**Sources with findings:** 8

| Status | Source | Notes |
|--------|--------|-------|
| ✅ | bleepingcomputer.com | FortiClient EMS exploitation, Citrix, F5, RoadK1ll |
| ✅ | thehackernews.com | Weekly recap, Citrix exploitation lead |
| ✅ | cisa.gov/kev | CVE-2026-3055 added March 30 |
| ✅ | cisa.gov | Same as KEV catalog |
| ✅ | securityweek.com | Star Blizzard DarkSword, CareCloud, Citrix, F5 |
| ✅ | github.com/search?q=CVE | CVE-2026-26111 patch bypass claim, CVE-2026-3055 PoC |
| ✅ | schneier.com | Apple camera indicators — nothing in scope |
| ✅ | krebsonsecurity.com | TeamPCP, botnets, Stryker — all previously covered |
| ✅ | rapid7.com | CVE-2026-3055 technical analysis, BPFDoor report |
| ✅ | attackerkb.com | CVE-2026-20127 deep analysis (already covered) |
| ✅ | fortinet.com/blog/threat-research | Iran cyber fallout — nothing net-new |
| ✅ | securitylab.github.com | Minor CVEs — Sylius, Chromium, Spree |
| ✅ | seclists.org/fulldisclosure | 26 March messages — no critical new disclosures |
| ✅ | packetstormsecurity.com | 41 exploits last 7 days — covered via other sources |
| ✅ | opencve.io | Platform operational |
| ✅ | nvd.nist.gov | No additional critical CVEs beyond other sources |
| ❌ | cve.mitre.org | Content extraction failed |
| ❌ | cve.org | Content extraction failed |
| ✅ | googleprojectzero.blogspot.com | Research posts — no new vulns |
| ✅ | blog.cloudflare.com/tag/security | Client-side security, Pingora (covered) |
| ✅ | msrc.microsoft.com/blog | Minimal content extracted — no new advisories |
| ⚠️ | hackerone.com/hacktivity | JS-rendered, no content extracted |
| ❌ | bugcrowd.com/disclosures | 404 Not Found |
| ✅ | kb.cert.org/vuls | No new VU notes in scope |
| ✅ | avleonov.com | March Linux Patch Wednesday analysis |
| ✅ | github.com/0xMarcio/cve | Top PoCs tracked — all previously reported |
| ✅ | dbugs.ptsecurity.com | Operational — no specific new findings |
| ✅ | habr.com/ru/companies/tomhunter/articles | Feb CVE roundup — retrospective |
| ✅ | teletype.in/@cyberok | Dec/Jan roundups — retrospective |
| ⚠️ | cert.gov.ua | Page loaded, JS-rendered, no extractable content |
