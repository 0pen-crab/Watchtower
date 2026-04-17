# Watchtower Night Report — 2026-04-17
**Cycle:** Night | **Generated:** 2026-04-17 22:00 UTC (2026-04-17T22:00:00Z)
**Sources checked:** 27/30 | **CISA KEV total:** ~1,280 | **New KEV additions:** 3

---

## 🔴 CRITICAL

### CVE-2026-33032 — nginx-ui MCP Authentication Bypass Enables Full Nginx Server Takeover (CVSS 9.8)
**Product:** nginx-ui (open-source Nginx management tool) | **CVE:** CVE-2026-33032 | **Status:** Active Exploitation

📰 News — Threat Score: **9**

An unprotected `/mcp_message` endpoint in nginx-ui's Model Context Protocol (MCP) integration allows unauthenticated attackers to establish SSE connections, obtain session IDs, and invoke all 12 MCP tools — including 7 destructive ones — without any authentication. Attackers can read/exfiltrate nginx configs, inject malicious server blocks, and trigger automatic nginx reloads for full server takeover. Pluto Security AI discovered the flaw on March 14; a partial fix shipped in v2.3.4 (March 15) with v2.3.6 recommended. Approximately 2,600 vulnerable instances are publicly exposed, concentrated in China, US, Indonesia, Germany, and Hong Kong.

**Timeline:** Discovered 2026-03-14 → Fix v2.3.4 2026-03-15 → Fix v2.3.6 following week → Active exploitation confirmed April 2026.

**Why it matters:** nginx-ui has 11,000+ GitHub stars and 430,000+ Docker pulls. Any organization using it for nginx management with MCP enabled is fully exposed. The MCP attack vector is novel — this is the first major actively exploited vulnerability specifically targeting an AI protocol endpoint in production infrastructure.

**Discovered by:** Pluto Security AI

**Mitigation:**
- Upgrade nginx-ui to v2.3.6 or later immediately
- If MCP is not needed, disable it entirely
- Block external access to `/mcp_message` endpoint at the network level
- Audit nginx configurations for unauthorized server blocks or injected directives
- Check for indicators of compromise: unexpected config changes, unauthorized reloads

**Discovery:** on-time — exploitation reported by THN/BleepingComputer on April 15, same cycle as our detection.

**Sources:** [The Hacker News](https://thehackernews.com) | [BleepingComputer](https://www.bleepingcomputer.com) | [SecurityWeek](https://www.securityweek.com)

---

## 🟠 HIGH

### CVE-2026-34197 — Apache ActiveMQ Jolokia API Remote Code Execution Added to CISA KEV (CVSS 8.8)
**Product:** Apache ActiveMQ Classic | **CVE:** CVE-2026-34197 | **CVSS:** 8.8 | **First reported:** 2026-04-17

📰 News — Threat Score: **8**

A 13-year-old improper input validation flaw in ActiveMQ's Jolokia JMX-HTTP bridge allows authenticated attackers to invoke operations with crafted discovery URIs that trigger remote Spring XML context loading, enabling arbitrary code execution. Added to CISA KEV on April 17, 2026, with confirmed active exploitation. The age of this vulnerability means enormous numbers of legacy deployments remain unpatched.

**Mitigation:**
- Patch Apache ActiveMQ immediately per vendor advisory
- Restrict access to the Jolokia endpoint (typically `/api/jolokia/`)
- Monitor for unusual Jolokia API calls, especially those referencing external URIs

**Discovery:** on-time

**Sources:** [The Hacker News](https://thehackernews.com) | [OpenCVE](https://app.opencve.io)

---

### Microsoft April 2026 Patch Tuesday — CVE-2026-33824 Windows IKE Unauthenticated RCE (CVSS 9.8), SharePoint Zero-Day in KEV
**Product:** Microsoft Windows, SharePoint | **CVE:** CVE-2026-33824, CVE-2026-32201 | **CVSS:** 9.8 / 6.5 | **First reported:** 2026-04-14

📰 News — Threat Score: **8**

Microsoft's second-largest Patch Tuesday ever addresses 169 vulnerabilities (8 Critical). The headline is CVE-2026-33824, an unauthenticated RCE in Windows Internet Key Exchange (IKE) v2 service (CVSS 9.8) — any Windows server with IPsec/VPN exposed can be compromised via specially crafted packets with no user interaction. Separately, CVE-2026-32201 (SharePoint spoofing, CVSS 6.5) is actively exploited in the wild and added to CISA KEV with a remediation deadline of April 28.

**Mitigation:**
- Apply April 2026 cumulative updates immediately, prioritizing IKE-exposed systems
- If IPsec VPN cannot be patched immediately, restrict IKE traffic to known peers
- Patch SharePoint instances per CISA KEV deadline of April 28

**Discovery:** on-time

**Sources:** [Krebs on Security](https://krebsonsecurity.com) | [Rapid7](https://rapid7.com) | [The Hacker News](https://thehackernews.com)

---

### 🔄 CVE-2026-39987 UPDATE — Marimo RCE Now Weaponized: NKAbuse Malware Deployed from Hugging Face Spaces
**Product:** Marimo Python notebook | **CVE:** CVE-2026-39987 | **CVSS:** 9.3 | **First reported:** 2026-04-14

🔄 Update — Threat Score: **8** (was 7) | Previous score: 7

Material change: exploitation occurred within 10 hours of disclosure. Attackers are now deploying NKAbuse malware variants hosted on Hugging Face Spaces via the unauthenticated WebSocket terminal vulnerability. The AI/ML supply chain angle — using Hugging Face as malware hosting infrastructure — represents a significant escalation beyond the initial RCE finding.

**Mitigation:**
- Upgrade Marimo to v0.20.5+ immediately
- Audit any Marimo instances for unauthorized WebSocket connections
- Block outbound connections to suspicious Hugging Face Spaces endpoints
- Scan for NKAbuse IoCs on hosts running Marimo

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com) | [The Hacker News](https://thehackernews.com)

---

### CVE-2026-27681 — SAP Business Planning and Consolidation SQL Injection (CVSS 9.9)
**Product:** SAP Business Planning and Consolidation (BPC), SAP Business Warehouse | **CVE:** CVE-2026-27681 | **CVSS:** 9.9 | **First reported:** 2026-04-15

📰 News — Threat Score: **7**

Low-privileged users can upload files containing arbitrary SQL statements for execution against SAP data stores, enabling complete data theft and corruption. While requiring authentication, the low privilege threshold and CVSS 9.9 make this extremely dangerous in any SAP environment. Part of the April 2026 Patch Tuesday cycle across multiple vendors.

**Mitigation:**
- Apply SAP Security Note immediately
- Restrict file upload permissions in BPC/BW environments
- Monitor for anomalous SQL execution patterns in SAP logs

**Discovery:** on-time

**Sources:** [The Hacker News](https://thehackernews.com) | [SecurityWeek](https://www.securityweek.com)

---

### Cisco ISE and Webex Services — Four Critical Flaws Enable User Impersonation and RCE (CVSS 9.8–9.9)
**Product:** Cisco Identity Services Engine, Webex Services | **CVE:** CVE-2026-20184, CVE-2026-20147, CVE-2026-20180, CVE-2026-20186 | **CVSS:** 9.8–9.9 | **First reported:** 2026-04-16

📰 News — Threat Score: **7**

Four critical vulnerabilities across Cisco ISE and Webex: CVE-2026-20184 (CVSS 9.8) is an improper certificate validation in Webex SSO enabling user impersonation; CVE-2026-20147 (CVSS 9.9) is an insufficient input validation in ISE/ISE-PIC; CVE-2026-20180 and CVE-2026-20186 (both CVSS 9.9) are additional critical flaws. Some require valid admin credentials, reducing the immediate blast radius, but ISE is a core network access control platform — compromise means lateral movement across the enterprise.

**Mitigation:**
- Apply Cisco patches for ISE and Webex per advisory
- Review ISE admin accounts for unauthorized access
- Monitor Webex SSO logs for impersonation attempts

**Discovery:** on-time

**Sources:** [The Hacker News](https://thehackernews.com) | [SecurityWeek](https://www.securityweek.com)

---

### WordPress EssentialPlugin Supply Chain Attack — 30+ Plugins Backdoored, Ethereum C2
**Product:** WordPress (EssentialPlugin suite — 30+ plugins) | **CVE:** Not yet assigned | **First reported:** 2026-04-15

📰 News — Threat Score: **7**

A dormant backdoor planted in August 2025 after the EssentialPlugin suite was acquired in a six-figure deal has been activated, pushing malware via plugin updates. The backdoor fetches spam links, redirects, and fake pages from a C2 server, injects code into wp-config.php, and uses Ethereum-based address resolution for C2 evasion. Malicious content is displayed exclusively to Googlebot, making it invisible to site admins. WordPress.org has closed affected plugins and pushed forced updates, but wp-config.php requires manual cleanup.

**Mitigation:**
- Check if any EssentialPlugin products are installed and update/remove immediately
- Manually inspect wp-config.php for injected code
- Search for 'wp-comments-posts.php' and other suspicious files
- Check for additional compromised files beyond known indicators

**Discovery:** on-time

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com)

---

## 🟡 MEDIUM

### CVE-2025-0520 — ShowDoc Unrestricted File Upload RCE Under Active Exploitation (CVSS 9.4)
**Product:** ShowDoc (document management) | **CVE:** CVE-2025-0520 | **Published:** 2026-04-14

📰 News — Threat Score: **6**

An unrestricted file upload vulnerability in ShowDoc allows unauthenticated attackers to upload and execute arbitrary PHP files, achieving remote code execution. Originally assigned in 2025 (CNVD-2020-26585), exploitation is now confirmed on unpatched servers. ShowDoc is a popular open-source documentation platform; however, its deployment footprint is smaller than enterprise targets.

**Mitigation:** Upgrade ShowDoc immediately or restrict public access to upload endpoints.

**Sources:** [The Hacker News](https://thehackernews.com)

---

### 🔄 CVE-2026-33825 UPDATE — Microsoft Defender "BlueHammer" Privilege Escalation — Public PoC and Zero-Day Status Confirmed
**Product:** Microsoft Defender for Endpoint | **CVE:** CVE-2026-33825 | **Published:** 2026-04-14

🔄 Update — Threat Score: **6** (was noted) | Previous score: 3

Previously noted in our April 7 report as "BlueHammer." Now assigned CVE-2026-33825 (CVSS 7.8), with a public exploit on GitHub since April 3. Exploits the Defender update process through Volume Shadow Copy abuse to escalate from low-privileged user to SYSTEM. Requires local access, limiting the immediate remote attack surface, but any post-exploitation scenario benefits massively.

**Mitigation:** Apply April 2026 Patch Tuesday updates. Monitor for Volume Shadow Copy abuse patterns.

**Sources:** [Krebs on Security](https://krebsonsecurity.com) | [The Hacker News](https://thehackernews.com)

---

### CVE-2026-40176, CVE-2026-40261 — PHP Composer Command Injection via Malicious Repository Configs (CVSS 8.8)
**Product:** Composer (PHP package manager) | **CVE:** CVE-2026-40176, CVE-2026-40261 | **Published:** 2026-04-15

📰 News — Threat Score: **5**

Two command injection vulnerabilities in Composer's Perforce VCS driver allow arbitrary command execution via crafted `composer.json` files — even if Perforce is not installed. CVE-2026-40261 (CVSS 8.8) exploits inadequate shell metacharacter escaping in source references. Fixed in Composer 2.9.6 and 2.2.27. Packagist.org disabled Perforce source metadata publication on April 10 as a proactive mitigation.

**Mitigation:** Update Composer to 2.9.6+. Inspect composer.json files from untrusted sources before running.

**Sources:** [The Hacker News](https://thehackernews.com)

---

## 📋 Noted / Monitoring

**ZionSiphon OT Malware** — ICS/SCADA malware targeting water treatment and desalination facilities via Modbus/DNP3/S7comm. Currently non-functional due to a code bug in encryption logic, but represents a serious future OT threat once fixed. USB-based propagation targeting air-gapped systems.

**CVE-2025-60710 — Windows Task Host Privilege Escalation** — Added to CISA KEV on April 13. Local privilege escalation via link following in Windows 11 and Server 2025. Patched November 2025, now confirmed actively exploited. Requires local access.

**CVE-2026-34222 — Open WebUI Access Control** — Broken access control in Open WebUI < v0.8.11 disclosed via Full Disclosure. AI platform vulnerability.

**CVE-2026-27664 — Siemens SICAM A8000** — Multiple vulnerabilities in industrial control equipment (CP-8050/CP-8031). Fixed in V26.10. ICS/OT context.

**ATHR Vishing Platform** — New AI-powered voice phishing platform using AI voice agents for automated credential harvesting at scale.

**100+ Malicious Chrome Extensions** — Discovered stealing OAuth2 Bearer tokens, deploying backdoors, and conducting ad fraud. Removed from Chrome Web Store.

**MCP Design Flaw Research** — SecurityWeek reports on a "by design" flaw in Anthropic's Model Context Protocol allowing unsanitized commands to execute silently across AI environments. Research-stage, no CVE.

**CVE-2026-40901 — DataEase RCE** — Authenticated RCE via deserialization in legacy Velocity/Commons Collections libraries (CVSS 9.0). Niche deployment.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | BleepingComputer, The Hacker News, SecurityWeek, Schneier, Krebs | ✅ |
| CISA / US Gov | CISA KEV (API), CISA advisories, CERT/CC (kb.cert.org) | ⚠️ CISA main site 403 |
| Vendor advisories | Microsoft (MSRC), Cisco, Fortinet, Cloudflare, Rapid7 | ✅ |
| CVE databases | NVD, OpenCVE (app.opencve.io), CVE.org | ✅ |
| Research / OSINT | GitHub CVE search, 0xMarcio/cve, Full Disclosure, Google Project Zero, GitHub Security Lab | ✅ |
| Supply chain | PacketStorm (→packetstorm.news), Schneier | ✅ |
| Threat intel | AttackerKB, Fortinet, dbugs.ptsecurity.com | ⚠️ AttackerKB 403 |
| Regional | CERT-UA, Habr/TomHunter, Teletype/CyberOK | ✅ (no new content) |
| Bug bounty | HackerOne, Bugcrowd | ⚠️ JS-only / 404 |

**Errors:**
- `cisa.gov` — 403 Forbidden (checked via API/KEV catalog and news outlets instead)
- `cisa.gov/known-exploited-vulnerabilities-catalog` — 403 Forbidden
- `attackerkb.com` — 403 Forbidden
- `hackerone.com/hacktivity` — JS-required, no content
- `bugcrowd.com/disclosures` — 404 Not Found
- `cve.org` — JS-required, no content

**CISA KEV:** ~1,280 total entries — new additions include CVE-2026-34197 (Apache ActiveMQ), CVE-2026-32201 (SharePoint), CVE-2025-60710 (Windows Task Host)

---

*Watchtower vulnerability-researcher | Cycle: 2026-04-17/night | Next: 2026-04-18/night*
