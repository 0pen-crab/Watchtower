# Vulnerability Report — 2026-03-07 (Night Cycle)

## Key Findings

### 1. 🔥 CVE-2026-21858 + CVE-2025-68613: n8n Full Chain — Unauthenticated RCE (CVSS 10.0)
**Affected:** n8n workflow automation (≤1.65.0 for AFR, ≥0.211.0 for sandbox bypass)
**Summary:** Public PoC exploit chains CVE-2026-21858 (Content-Type confusion → arbitrary file read) with CVE-2025-68613 (expression injection → sandbox bypass → RCE) for unauthenticated remote code execution on n8n instances. The exploit was AI-automated within 9 hours of disclosure. LeakIX shows publicly exposed vulnerable instances. Fixed in 1.121.0/1.120.4+.
**PoC:** https://github.com/Chocapikk/CVE-2026-21858 (222 stars)
**First seen:** github.com/0xMarcio/cve

### 2. 🔥 CVE-2026-1731: BeyondTrust RS/PRA Command Injection (Critical)
**Affected:** BeyondTrust Remote Support and Privileged Remote Access
**Summary:** Critical command injection in the same endpoint as previously exploited CVE-2024-12356. Rapid7 reproduced the vulnerability. While no known exploitation in the wild yet, the similarity to CVE-2024-12356 (which was a zero-day) makes this extremely high risk. Patch: BT26-02.
**First seen:** attackerkb.com

### 3. 🔥 CVE-2026-22200: osTicket Arbitrary File Read + RCE via CNEXT
**Affected:** osTicket
**Summary:** Horizon3.ai released a PoC exploiting PHP filters in osTicket's mPDF library for file exfiltration, chained to RCE via CVE-2024-2961 (CNEXT). Fully automated exploit available.
**PoC:** https://github.com/horizon3ai/CVE-2026-22200
**First seen:** github.com/0xMarcio/cve

### 4. 📰 MuddyWater (Seedworm) Targets U.S. Bank, Airport, Software Company with Dindoor Backdoor
**Affected:** U.S. critical infrastructure (banks, airports, non-profits, defense software)
**Summary:** Broadcom/Symantec discovered Iranian state-sponsored MuddyWater embedded in networks of U.S. companies including banks and airports, deploying new Dindoor backdoor (Deno-based) and Fakeset Python backdoor. Activity intensified after U.S.-Israeli strikes on Iran. Data exfiltration attempts via Rclone to Wasabi cloud storage observed.
**First seen:** thehackernews.com, security.com

### 5. 📰 FBI Investigating Breach of Surveillance and Wiretap Systems
**Summary:** FBI confirmed a breach affecting systems managing surveillance and wiretap warrants. Possibly connected to earlier Salt Typhoon campaign. The breach has been addressed per FBI statement but scope remains unclear.
**First seen:** bleepingcomputer.com

### 6. 📰 CVE-2026-24061: Telnet RCE via Malformed USER Variable
**Affected:** Telnet servers
**Summary:** SafeBreach Labs released a PoC for RCE through malformed USER environment variable exploitation in Telnet servers. Public exploit actively accumulating attention (197 stars).
**PoC:** https://github.com/SafeBreach-Labs/CVE-2026-24061
**First seen:** github.com/0xMarcio/cve

### 7. 📰 CVE-2026-23745: node-tar Arbitrary File Overwrite
**Affected:** node-tar (<7.5.3)
**Summary:** PoC for arbitrary file overwrite vulnerability in node-tar, a widely-used npm package for handling tar archives. Could affect many downstream packages.
**PoC:** https://github.com/Jvr2022/CVE-2026-23745
**First seen:** github.com/0xMarcio/cve

### 8. 📰 GitHub Security Lab Discloses Zammad IDOR and SQLi
**Affected:** Zammad
**Summary:** Multiple vulnerabilities disclosed in Zammad including IDOR (GHSL-2026-049) leading to access control violations and SQL injection (GHSL-2026-047) allowing sensitive information leakage. Published March 6, 2026.
**First seen:** securitylab.github.com

### 9. 📰 CISA Emergency Directive 26-03: Cisco SD-WAN
**Affected:** Cisco Catalyst SD-WAN
**Summary:** CISA issued Emergency Directive 26-03 requiring federal agencies to inventory SD-WAN systems, apply mitigations, and assess for compromise based on CVE-2026-20127 and CVE-2022-20775. This is an escalation of the previously reported CVE-2026-20127 issue.
**First seen:** cisa.gov

## Noted (Lower Priority)

- **CVE-2026-30844 / CVE-2026-30843**: SSRF and unauthorized data manipulation in Wekan (GHSL advisories)
- **GHSL-2026-040**: Access Control Bypass in AFFiNE (published 2026-03-06)
- **Cisco ASA/FMC/FTD**: 48 vulnerabilities patched in bulk advisory cycle
- **Fake Claude Code install guides**: ClickFix variant pushing infostealers
- **Google report**: Half of 2025's 90 exploited zero-days targeted enterprise products
- **Fortinet**: Cyber fallout analysis post-Iran strikes; regional cyber activity rising
- **EncystPHP**: Weaponized web shell exploiting CVE-2025-64328 in FreePBX
