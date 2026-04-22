# Watchtower Night Report — 2026-04-22
**Cycle:** Night | **Generated:** 2026-04-22 06:00 UTC (2026-04-22T06:00:00Z)
**Sources checked:** 21/31 | **CISA KEV total:** 8 new additions | **New KEV additions:** 8

---

## 🟠 HIGH

### CISA Adds 8 Exploited Flaws to KEV — Quest KACE CVSS 10.0, PaperCut, TeamCity, Cisco SD-WAN (CVSS 10.0)
**Product:** Quest KACE, PaperCut NG/MF, JetBrains TeamCity, Cisco Catalyst SD-WAN Manager, Kentico, Zimbra | **CVE:** CVE-2025-32975, CVE-2023-27351, CVE-2024-27199, CVE-2026-20133 | **Status:** Active Exploitation | KEV

CISA added 8 vulnerabilities to the Known Exploited Vulnerabilities catalog with federal patch deadlines of April 24 to early May 2026. The most critical is Quest KACE Systems Management Appliance (CVE-2025-32975, CVSS 10.0), an enterprise asset management platform deployed across large organizations. Also included: PaperCut NG/MF authentication bypass (CVE-2023-27351, CVSS 8.2), JetBrains TeamCity path traversal (CVE-2024-27199, CVSS 7.3), and a new Cisco Catalyst SD-WAN Manager information disclosure flaw (CVE-2026-20133) caused by insufficient file system access restrictions — distinct from CVE-2026-20127 reported March 23.

**Why it matters:** Quest KACE manages software inventory and deployment across enterprise fleets. A CVSS 10.0 with confirmed exploitation means any organization running KACE needs to patch immediately. The Cisco SD-WAN addition is the fourth SD-WAN CVE confirmed exploited in 2026, signaling sustained adversary interest in SD-WAN infrastructure.

**Mitigation:**
- Patch Quest KACE to latest version immediately
- Verify PaperCut NG/MF, TeamCity, and SD-WAN Manager are on current patch levels
- Check Kentico and Zimbra deployments for available updates
- Review CISA KEV catalog for full list and deadlines

**Sources:** [The Hacker News](https://thehackernews.com) | [BleepingComputer](https://www.bleepingcomputer.com) | [SecurityWeek](https://www.securityweek.com)

---

### Progress MOVEit WAF and LoadMaster — RCE, OS Command Injection, and WAF Bypass
**Product:** Progress MOVEit WAF, Progress LoadMaster | **CVE:** Not yet assigned | **CVSS:** Not yet scored | **First reported:** 2026-04-21

Progress Software patched multiple critical vulnerabilities in MOVEit WAF and LoadMaster load balancer. The flaws enable remote code execution, OS command injection, and WAF detection bypass. Given MOVEit Transfer's history as a mass exploitation target (Cl0p campaign 2023), any vulnerability in the MOVEit ecosystem warrants immediate attention. No public exploitation reported yet, but the combination of RCE + WAF bypass in a product designed to protect web applications is particularly concerning.

**Mitigation:**
- Apply Progress security patches for MOVEit WAF and LoadMaster immediately
- Review WAF rules for bypass indicators
- Monitor Progress advisory portal for CVE assignments and detailed technical guidance

**Sources:** [SecurityWeek](https://www.securityweek.com)

---

## 🟡 MEDIUM

### Firefox 150 / ESR 140.10 Patches 34+ Vulnerabilities Including Critical DOM Security Bypass (CVE-2026-6771, CVSS 9.8)
**Product:** Mozilla Firefox, Thunderbird | **CVE:** CVE-2026-6771, CVE-2026-6761, CVE-2026-6746, CVE-2026-6747, CVE-2026-6754 | **Published:** 2026-04-21

Mozilla released Firefox 150, ESR 140.10, and ESR 115.35 addressing 34+ vulnerabilities. The most severe is CVE-2026-6771 (CVSS 9.8), a DOM Security component mitigation bypass. Nine high-severity flaws include use-after-free bugs in DOM (CVE-2026-6746), WebRTC (CVE-2026-6747), and JavaScript engine (CVE-2026-6754), plus a networking privilege escalation (CVE-2026-6761, CVSS 8.8). Multiple memory safety bugs "showed evidence of memory corruption" per Mozilla's advisory.

**Mitigation:** Update Firefox to 150, ESR to 140.10 or 115.35. Update Thunderbird to matching ESR release.

**Sources:** [Mozilla Security Advisories](https://www.mozilla.org/en-US/security/advisories/) | [PT Security](https://dbugs.ptsecurity.com)

---

### 🔄 Apache ActiveMQ CVE-2026-34197 — 6,400 Exposed Servers Quantified, Exploitation Scope Confirmed
**Product:** Apache ActiveMQ | **CVE:** CVE-2026-34197 | **CVSS:** 8.6 | **First reported:** 2026-04-17

The Shadowserver Foundation confirmed over 6,400 Apache ActiveMQ instances remain exposed and vulnerable, with the majority in Asia (2,925), North America (1,409), and Europe (1,334). CISA reaffirmed active exploitation. Horizon3 researcher Naveen Sunkavally published detection guidance: examine broker logs for suspicious VM transport connections with "brokerConfig=xbean:http://" parameters. The 13-year-old code injection flaw was patched in ActiveMQ Classic 5.19.4 and 6.2.3 on March 30.

**Mitigation:** Patch to ActiveMQ Classic 5.19.4+ or 6.2.3+. Audit logs for VM transport abuse. Remove unnecessary internet exposure.

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com) | [Shadowserver Foundation](https://www.shadowserver.org)

---

### Terrarium CVE-2026-5752 — AI Code Sandbox Escape to Root via JavaScript Prototype Chain (Vendor Unresponsive)
**Product:** Terrarium (Cohere AI sandbox platform) | **CVE:** CVE-2026-5752 | **Published:** 2026-04-21

CERT/CC published VU#414811 after vendor coordination with Cohere failed. Terrarium's Pyodide WebAssembly sandbox can be escaped by traversing the JavaScript prototype chain from the mock document object up to `Object.prototype`, reaching the function constructor, and executing arbitrary Node.js code with root privileges. Attackers gain access to environment variables, internal services, and potentially escape the container. No patch available.

**Mitigation:** Disable user code submission if possible. Network-segment Terrarium containers. Deploy WAF and monitor container activity for anomalous behavior.

**Sources:** [CERT/CC VU#414811](https://kb.cert.org/vuls/id/414811)

---

## 📋 Noted / Monitoring

**Lotus Data Wiper (Venezuela)** — Previously undocumented wiper malware used against Venezuelan energy and utility organizations in late 2025. Kaspersky analysis published April 21. Geopolitically motivated; no remote exploitation vector relevant to general enterprise environments.

**Radware Alteon CVE-2026-5754** — Reflected XSS in `/protected/login` ReturnTo parameter on Alteon load balancers. Patch expected in v34.5.7.0 (March 31 target unclear if shipped). Low severity for enterprise environments with proper network segmentation.

**FreePBX CVE-2026-40520 (CVSS 7.2)** — GraphQL mutation input fields passed directly to shell exec() in the FreePBX API module. Requires authentication to exploit. Patch status unknown.

**Tekton Pipeline CVE-2026-40938 (CVSS 7.5)** — Argument injection via Git revision parameter enables arbitrary binary execution. Affects CI/CD pipelines using Tekton for trusted resource verification.

**Perforce P4 Server Exposure** — Over 1,500 unsecured Perforce instances discovered allowing file reads including sensitive data from major organizations. Misconfiguration issue, not a CVE.

**The Gentlemen RaaS / SystemBC** — 1,570+ victims tracked via compromised C2 panel. RC4-encrypted SOCKS5 tunneling. 320+ claimed victims since July 2025. Ransomware operations intelligence, not a specific exploitable vulnerability.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | BleepingComputer, The Hacker News, SecurityWeek, Krebs on Security, Schneier | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/kev | ❌ 403 (used THN/BleepingComputer for KEV data) |
| Vendor advisories | Fortinet, Rapid7, Microsoft MSRC, Cloudflare, Mozilla | ✅ / ⚠️ |
| CVE databases | NVD, OpenCVE, dbugs.ptsecurity.com | ✅ / ⚠️ |
| Research / OSINT | GitHub CVE search, 0xMarcio/cve, seclists.org/fulldisclosure, CERT/CC, avleonov.com | ✅ |
| Supply chain | packetstorm.news, GitHub Security Lab | ✅ / ⚠️ |
| Threat intel | habr.com/tomhunter, teletype.in/@cyberok | ✅ (no new content) |
| Other | AttackerKB, HackerOne, Bugcrowd, cve.org, cve.mitre.org, cert.gov.ua | ❌ (JS-only / 403 / 404) |

**Errors:** cisa.gov (403), cisa.gov/kev (403), attackerkb.com (403), hackerone.com/hacktivity (JS-only), cve.org (JS-only), bugcrowd.com/disclosures (404), cve.mitre.org (redirects to cve.org), cert.gov.ua (unreachable), packetstormsecurity.com (redirect, content inaccessible), msrc.microsoft.com/blog (redirect, content inaccessible)
**CISA KEV:** 8 new additions announced April 21 — Quest KACE CVSS 10.0, PaperCut, TeamCity, Cisco SD-WAN, Kentico, Zimbra confirmed exploited with April-May federal deadlines.

---

*Watchtower vulnerability-researcher | Cycle: 2026-04-22/night | Next: 2026-04-23/night*
