# Watchtower Night Report — 2026-04-18
**Cycle:** Night | **Generated:** 2026-04-18 06:00 UTC (2026-04-18T06:00:00Z)
**Sources checked:** 28/35 | **CISA KEV total:** N/A (403) | **New KEV additions:** N/A

---

## 🔴 CRITICAL

No critical findings today.

---

## 🟠 HIGH

### 🔄 Microsoft Defender Zero-Day Trilogy — RedSun + UnDefend Join BlueHammer in Active Exploitation (CVSS N/A)
**Product:** Microsoft Windows Defender | **CVE:** CVE-2026-33825 (BlueHammer); RedSun and UnDefend not yet assigned | **Status:** Active Exploitation | **Previous Score:** 6

Two additional Microsoft Defender zero-days — "RedSun" (local privilege escalation to SYSTEM) and "UnDefend" (blocks definition updates) — are now confirmed actively exploited alongside the previously reported BlueHammer. All three were disclosed by researcher "Chaotic Eclipse" within two weeks. RedSun exploits Defender's cloud protection file-rewrite behavior via oplocks and directory junctions to overwrite system files and achieve SYSTEM privileges. UnDefend can be triggered by standard users. Only BlueHammer has been patched (April 2026 Patch Tuesday); RedSun and UnDefend remain unpatched zero-days.

**Timeline:** BlueHammer patched April 8 → RedSun PoC published ~April 10 → Huntress Labs confirms hands-on-keyboard exploitation of all three by April 17.

**Why it matters:** Every Windows endpoint running Defender is potentially affected. Attackers chaining RedSun (SYSTEM access) with UnDefend (disable definitions) get persistent elevated access with neutered AV — a devastating combination for post-exploitation. Two of three remain unpatched.

**Discovered by:** Chaotic Eclipse (independent researcher); exploitation confirmed by Huntress Labs

**Mitigation:**
- Apply April 2026 Patch Tuesday updates immediately (patches BlueHammer only)
- Monitor for unauthorized QEMU/VM installations and suspicious scheduled tasks named 'TPMProfiler'
- Enable ASR rules to restrict file overwrites in system directories
- Consider supplementary EDR until Microsoft patches RedSun/UnDefend
- Monitor registry key HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU for ClickFix-style activity

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/microsoft/new-microsoft-defender-redsun-zero-day-poc-grants-system-privileges/) | [BleepingComputer](https://www.bleepingcomputer.com/news/security/recently-leaked-windows-zero-days-now-exploited-in-attacks/) | [The Hacker News](https://thehackernews.com)

---

### 📰 Oracle WebLogic Server CVE-2026-21962 — Unauthenticated RCE via HTTP (CVSS 10.0)
**Product:** Oracle HTTP Server / Oracle WebLogic Server Proxy Plug-in | **CVE:** CVE-2026-21962 | **CVSS:** 10.0 | **First reported:** 2026-04-18

An easily exploitable vulnerability in the Oracle WebLogic Server Proxy Plug-in allows unauthenticated attackers with network access via HTTP to achieve complete system compromise, including unauthorized access to and modification of all accessible data. No user interaction required. The flaw was published to NVD with CVSS 10.0 base score.

**Why it matters:** Oracle WebLogic is ubiquitous in enterprise environments, often directly exposed to the internet as application server infrastructure. A CVSS 10.0 unauthenticated network-accessible RCE is the worst-case scenario. Patch immediately once Oracle CPU is available.

**Discovered by:** Oracle (via Critical Patch Update)

**Mitigation:**
- Apply Oracle Critical Patch Update as soon as available
- Restrict network access to WebLogic administration ports
- Place WebLogic behind WAF with request inspection enabled
- Audit internet-facing Oracle deployments immediately

**Sources:** [OpenCVE](https://app.opencve.io/cve/CVE-2026-21962)

---

### 📰 Cursor AI Vulnerability Chain — Prompt Injection + Sandbox Bypass = Developer Machine Shell Access
**Product:** Cursor AI (AI development tool) | **CVE:** Not yet assigned | **CVSS:** N/A | **First reported:** 2026-04-17

An indirect prompt injection vulnerability in Cursor AI can be chained with a sandbox bypass and Cursor's remote tunnel feature to obtain shell access on developer machines. The attack chain allows an attacker to escalate from untrusted input (e.g., a malicious code comment or documentation) to arbitrary command execution on the developer's host system. This is particularly dangerous given Cursor's widespread adoption among software developers.

**Why it matters:** Developer machines are high-value targets with access to source code, credentials, and CI/CD pipelines. AI coding assistants that can be weaponized via prompt injection represent an emerging attack surface. This is the second major AI code tool vulnerability after CursorJack (reported March 20).

**Mitigation:**
- Update Cursor to latest version
- Disable remote tunnel feature if not needed
- Review untrusted repositories before opening in AI-enabled editors
- Implement network segmentation for developer workstations

**Sources:** [SecurityWeek](https://www.securityweek.com/cursor-ai-vulnerability-exposed-developer-devices/)

---

### 📰 Payouts King Ransomware — QEMU VM Evasion Bypasses All Host Endpoint Security
**Product:** Windows endpoints (via SonicWall VPN, SolarWinds WHD initial access) | **CVE:** CVE-2025-26399 (SolarWinds WHD, initial access vector) | **CVSS:** N/A | **First reported:** 2026-04-17

Payouts King ransomware operators deploy hidden QEMU virtual machines running Alpine Linux with SYSTEM privileges via scheduled tasks disguised as 'TPMProfiler'. Virtual disk files are disguised as databases and DLLs, with reverse SSH tunnels providing covert access. Since host-based security solutions cannot scan inside VMs, this technique effectively bypasses all endpoint detection. Initial access is primarily through exposed SonicWall VPNs and SolarWinds Web Help Desk (CVE-2025-26399). Post-exploitation includes VSS shadow copies for NTDS.dit credential extraction.

**Why it matters:** This technique renders host-based EDR blind. The campaign (tracked as STAC4713) is linked to GOLD ENCOUNTER, with possible former BlackBasta affiliates involved. SonicWall VPNs are widely deployed across enterprise perimeters. The combination of VPN initial access + EDR bypass + credential harvesting is a full kill chain.

**Discovered by:** Huntress Labs (STAC4713 tracking)

**Mitigation:**
- Monitor for unauthorized QEMU installations on endpoints
- Detect SYSTEM-privileged scheduled tasks with unusual names
- Block outbound SSH on non-standard ports at firewall level
- Patch SonicWall VPN and SolarWinds WHD immediately
- Monitor for TPMProfiler scheduled task creation

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/payouts-king-ransomware-uses-qemu-vms-to-bypass-endpoint-security/)

---

## 🟡 MEDIUM

### 📰 Cloudflare Wrangler CVE-2026-0933 — CI/CD Command Injection via --commit-hash (CVSS 9.9)
**Product:** Cloudflare Wrangler (Pages deploy CLI) | **CVE:** CVE-2026-0933 | **Published:** 2026-04-18

A command injection flaw in Cloudflare Wrangler's `pages deploy` command where the `--commit-hash` parameter lacks proper validation. In CI/CD environments where this parameter derives from untrusted sources (e.g., PR titles, branch names), attackers can inject arbitrary shell commands. CVSS 9.9 reflects the potential for supply chain compromise through CI/CD pipelines.

**Mitigation:** Update Wrangler to latest version; sanitize all inputs to `--commit-hash` in CI/CD pipelines; audit existing pipeline configurations.

**Sources:** [OpenCVE](https://app.opencve.io/cve/CVE-2026-0933)

---

### 📰 ClickFix Phishing Campaign Impersonating Claude AI Installer
**Product:** Anthropic Claude (impersonated) | **CVE:** Not yet assigned | **Published:** 2026-04-16

Rapid7 Labs identified a ClickFix-style phishing campaign using a fake Claude AI installer (claude.msixbundle) that delivers staged malware via mshta + PowerShell. The attack chain includes AMSI bypass, layered obfuscation, XOR-encrypted shellcode, and process injection via NtCreateThreadEx. The campaign targets developers and AI users in the EU and US. IOCs include domains oakenfjrod[.]ru and download-version[.]1-5-8[.]com.

**Mitigation:** Block IOC domains at perimeter; monitor RunMRU registry key for ClickFix patterns; warn users about unofficial Claude installer downloads; only download Claude from official Anthropic channels.

**Sources:** [Rapid7](https://rapid7.com/blog/post/ve-clickfix-phishing-campaign-fake-claude-installer)

---

### 📰 FastGPT CVE-2026-40351 — NoSQL Injection Authentication Bypass (CVSS 9.8)
**Product:** Labring FastGPT (AI platform) | **CVE:** CVE-2026-40351 | **Published:** 2026-04-18

A TypeScript type assertion without runtime validation in FastGPT allows MongoDB query operators in login credentials, bypassing authentication for administrator accounts. CVSS 9.8 unauthenticated. FastGPT is an open-source AI knowledge base platform with growing enterprise adoption.

**Mitigation:** Update FastGPT to patched version; implement input validation on authentication endpoints; add rate limiting on login attempts.

**Sources:** [dbugs.ptsecurity.com](https://dbugs.ptsecurity.com)

---

### 📰 xrdp CVE-2026-32105 — Missing MAC Signature Verification Enables MITM on RDP (CVSS 9.3)
**Product:** Neutrinolabs xrdp | **CVE:** CVE-2026-32105 | **Published:** 2026-04-18

The xrdp remote desktop server silently ignores MAC signatures in classic RDP mode, permitting man-in-the-middle modification of encrypted traffic. Attackers on the network path can intercept and modify RDP sessions without detection. xrdp is widely deployed on Linux servers for remote desktop access.

**Mitigation:** Update xrdp to patched version; use TLS-encrypted RDP connections; deploy network-level protections (VPN/ZTNA) for remote desktop access.

**Sources:** [dbugs.ptsecurity.com](https://dbugs.ptsecurity.com)

---

## 📋 Noted / Monitoring

**Dolibarr CVE-2026-23500 (CVSS 9.4)** — OS command injection in Dolibarr ERP/CRM via unsanitized configuration constants in shell exec() calls. Requires admin access, reducing practical risk.

**Anviz CVE-2026-35546 (CVSS 9.8)** — Unauthenticated firmware upload on Anviz CX2 Lite & CX7 physical access control devices. Niche product but critical impact.

**OpenViking CVE-2026-40525 (CVSS 9.1)** — Volcengine OpenViking authentication bypass when API key is unset. Exposes bot control to unauthenticated access.

**Nexcorium Mirai Variant** — FortiGuard reports new Mirai variant targeting TBK DVRs via CVE-2024-3721 and CVE-2017-17215. Multi-architecture DDoS botnet with brute-force capabilities.

**SAIL Image Library CVE-2026-40492/40493/40494 (CVSS 9.8)** — Heap buffer overflows in PSD, TGA, and XWD codecs of HappySeaFox SAIL library. RCE via crafted image files.

**ChurchCRM CVE-2026-40484 (CVSS 9.1)** — Backup restore webshell upload. Niche product.

**McGraw Hill Breach** — ShinyHunters exfiltrated 13.5M accounts (100GB) from Salesforce environment. Contact data exposed; spear-phishing risk for students/educators.

**ZionSiphon ICS/OT Malware UPDATE** — SecurityWeek now reporting dedicated coverage of ZionSiphon targeting water treatment facilities (was noted 04/17). Monitoring for wider targeting beyond Israeli facilities.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | BleepingComputer, The Hacker News, SecurityWeek, Schneier, Krebs | ✅ |
| CISA / US Gov | cisa.gov, CISA KEV | ❌ (403 Forbidden) |
| Vendor advisories | Rapid7, Fortinet, Cloudflare, MSRC, Oracle | ✅ / ⚠️ |
| Research / OSINT | GitHub CVE search, 0xMarcio/cve, dbugs.ptsecurity, seclists.org, NVD | ✅ |
| Supply chain | GitHub Security Lab, PacketStorm | ✅ / ⚠️ |
| Threat intel | OpenCVE, CERT/CC, avleonov.com | ✅ |
| Regional | CERT-UA, Habr/TomHunter, Cyberok | ⚠️ / ❌ |

**Errors:**
- cisa.gov / CISA KEV: 403 Forbidden (persistent)
- attackerkb.com: 403 Forbidden (persistent)
- bugcrowd.com/disclosures: 404 Not Found (persistent)
- hackerone.com/hacktivity: Requires JavaScript
- cve.org / cve.mitre.org: Requires JavaScript
- SecurityWeek article pages: 403 on direct article access
- Oracle security alerts: 403 Forbidden
- MSRC blog: Redirect, content not accessible

**CISA KEV:** Unable to access directly (403); no new KEV additions identified from secondary sources beyond ActiveMQ CVE-2026-34197 (already reported 04/17).

---

*Watchtower vulnerability-researcher | Cycle: 2026-04-18/night | Next: 2026-04-19/night*
