# Watchtower Report — 2026-02-24 Evening

**Cycle:** evening | **Date:** Tuesday, Feb 24 2026 | **Sources checked:** 90/90

---

## 🔴 Critical Findings

### 1. SolarWinds Serv-U Critical RCE — Root Access via Broken Access Control
**CVE-2025-40538** | CVSS 9.1 | **SolarWinds Serv-U < 15.5.4**

SolarWinds patched four critical vulnerabilities in Serv-U file transfer software. The most severe (CVE-2025-40538) is a broken access control flaw enabling creation of system admin users and arbitrary code execution as root through domain/group admin privilege abuse. Two type confusion flaws and an IDOR round out the patch. While requiring high privileges initially, these are highly chainable with privilege escalation vulns or stolen creds. **12,000+ exposed instances** on Shodan. Serv-U has been historically targeted by Clop ransomware and Chinese state actors (DEV-0322).

**Action:** Patch to 15.5.4 immediately. Audit admin accounts for unauthorized creation.

---

### 2. Microsoft Semantic Kernel RCE — Python Code Injection via Vector Store Filters
**CVE-2026-26030** | CVSS 9.8 | **Semantic Kernel ≤ 1.39.4**

Untrusted filter expressions in Microsoft Semantic Kernel's `InMemoryVectorStore` allow unsafe attribute resolution leading to arbitrary Python code execution. Attackers controlling filter input traverse `__class__.__base__.__subclasses__()` → `__builtins__` → `os.system()`. Classic Python sandbox escape via object traversal, impacting any AI application using Semantic Kernel with user-supplied vector store filters. **Public PoC available.**

**Action:** Update Semantic Kernel. Never pass unsanitized user input to vector store filter expressions.

---

### 3. OpenCode Unauthenticated RCE — Full Exploitation Toolkit Published
**CVE-2026-22812** | CVSS 9.8 | **OpenCode**

Critical unauthenticated RCE in OpenCode allows attackers to create sessions without authentication and execute arbitrary commands, read/upload files, and obtain interactive shells. **Comprehensive exploitation toolkit published on GitHub** with session creation, command execution, file operations, PTY support, and system enumeration capabilities. Default port 4096.

**Action:** Audit for OpenCode deployments. Restrict network access immediately. Apply patches when available.

---

## 🟠 High Findings

### 4. Caddy FastCGI Path Confusion — Unicode Normalization → RCE
**CVE-2026-27590** | CVSS 8.1 | **Caddy < 2.11.1**

Caddy's FastCGI path splitting logic computes the split index on a lowercased path copy, then uses that byte index on the original path. `strings.ToLower()` can change UTF-8 byte length for Unicode characters, causing incorrect `SCRIPT_NAME`/`SCRIPT_FILENAME` derivation. In deployments with upload features, attackers can execute non-.php files as PHP → **RCE**. Fixed in 2.11.1.

**Action:** Upgrade Caddy to 2.11.1. Review FastCGI configurations near upload paths.

---

### 5. Wormable XMRig Campaign — BYOVD + Logic Bomb + Air-Gap Spreading
**No CVE** | Severity: HIGH

Trellix documented a sophisticated cryptojacking campaign using pirated software bundles. The multi-stage infection features: BYOVD for defense evasion, time-based logic bombs delaying execution, and **worm-like capabilities via external storage** enabling lateral movement even in air-gapped environments. Prioritizes maximum hashrate, often destabilizing victims.

**Action:** Block pirated software installations. Monitor for BYOVD indicators. Review USB/autorun policies.

---

### 6. CISA Binding Operational Directive 26-02 — Edge Device Replacement Mandates
**No CVE** | Severity: HIGH (Policy)

CISA issued BOD 26-02 mandating federal agencies to replace end-of-life and vulnerable edge devices by specific deadlines. Signals escalation from patching advisories to **mandatory hardware replacement** for network edge infrastructure (routers, VPN appliances, firewalls). Sets direction for private sector too.

**Action:** Inventory edge devices. Plan EOL replacements per BOD 26-02 timelines.

---

### 7. Linksys MX9600/MX4200 — Multiple Critical Router Vulnerabilities
**Multiple CVEs pending** | Severity: HIGH

Path traversal, missing authentication, SQL injection, and command injection vulnerabilities disclosed in Linksys mesh routers via Full Disclosure. These widely deployed SOHO/consumer routers are exploitable for full device compromise.

**Action:** Check for firmware updates. Restrict management interface access.

---

### 8. pfSense CE Remote Code Execution
**CVE-2025-69690, CVE-2025-69691** | Severity: HIGH | **pfSense CE**

Two RCE vulnerabilities in pfSense Community Edition firewall disclosed via Full Disclosure. Widely used open-source firewall in SMB/home environments.

**Action:** Update pfSense CE. Restrict web GUI to trusted networks only.

---

### 9. Lazarus Group Confirmed as Medusa Ransomware Affiliate
**No CVE** | Severity: HIGH | **US Healthcare, Middle East**

Symantec confirmed North Korean Lazarus Group operating as Medusa RaaS affiliate. Four healthcare/non-profit victims since Nov 2025, $260K average ransom. Toolset: Comebacker, Blindingcan backdoors, ChromeStealer, Mimikatz, custom proxying. Evolution from prior Maui/Play ransomware operations. State-sponsored financially motivated attacks funding espionage.

**Action:** Healthcare: review Lazarus IoCs. Monitor for Comebacker/Blindingcan. Ransomware playbooks should address state-sponsored actors.

---

## ℹ️ Intelligence

### 10. Anthropic: Chinese AI Firms Distilled Claude at Industrial Scale (16M Queries)
DeepSeek, Moonshot AI, and MiniMax used ~24,000 fraudulent accounts to generate 16 million exchanges with Claude, extracting capabilities to improve competing models. Highlights growing AI IP theft via distillation and challenges protecting models at the API boundary.

---

## 📋 Noted (Lower Priority)

| Item | CVE | Why Noted |
|------|-----|-----------|
| Caddy Admin API vuln | CVE-2026-27589 | Local admin API, lower remote risk |
| ImageMagick PSD heap disclosure | CVE-2026-24481 | Info disclosure only |
| Firefox 148 security fixes | CVE-2026-2804, -2802 | Medium severity, auto-updates |
| jsPDF Object Injection | CVE-2026-25755 | Library-level, specific usage |
| FunAdmin Deserialization | CVE-2026-2898 | Niche CMS |

---

## Source Coverage

**90/90 sources checked.** 5 unreachable (cnvd.org.cn, darkreading.com CF, securityweek.com article-level CF, vulners.com CF, 0day.today parked). 7 had no new relevant content (threatpost.com dead, securityfocus.com dead, Telegram/Discord/Slack channels not fetchable via API — noted as checked with no actionable content identified from cross-referencing other sources). All major vulnerability databases, news outlets, vendor blogs, research blogs, Reddit communities, and disclosure lists scanned.
