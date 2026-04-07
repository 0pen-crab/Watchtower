# 🔐 Vulnerability Intelligence Report
**Date:** 2026-03-20 | **Cycle:** Night | **Generated:** 02:00 EEST

---

## 🚨 Critical Update: APT28 (GRU) Confirmed Exploiting Zimbra CVE-2025-66376 Against Ukraine
**Threat Score: 10/10 | UPDATE to 2026-03-18 finding**

| Field | Detail |
|---|---|
| **CVE** | CVE-2025-66376 |
| **CVSS** | High (NVD pending) |
| **Affected** | Synacor Zimbra Collaboration Suite (ZCS) Classic UI — all versions prior to patched build |
| **Status** | CISA KEV (added 2026-03-18, due 2026-04-01) |

**What's new:** SecurityWeek and multiple sources confirmed today that Russian APT28 (Fancy Bear, GRU military intelligence unit 26165) is **actively exploiting** CVE-2025-66376 in targeted campaigns against Ukrainian government entities. Previously only "exploited in wild" by unknown actors; now confirmed as Russian state military intelligence.

**Mechanism:** Attackers embed malicious CSS `@import` directives in HTML emails. When the victim opens the email in Zimbra Classic UI with browser rendering, the imported CSS triggers inline script execution — no additional user interaction required beyond opening the email. Session tokens are stolen, enabling full account compromise.

**Action:** If on any unpatched Zimbra ZCS version, patch is P0 emergency. APT28 has repeatedly pivoted from initial email compromise to lateral movement, data exfiltration, and destructive operations in Ukrainian government environments.

---

## 🔴 Top Findings

### 1. Citrix NetScaler CVE-2025-5777 — Mass Exploitation: 500+ Honeypot Hits in 24h
**Threat Score: 9/10**

| Field | Detail |
|---|---|
| **CVE** | CVE-2025-5777 |
| **Also Targeted** | CVE-2023-4966 ("Citrix Bleed") |
| **CVSS** | Critical (NVD) |
| **Affected** | Citrix NetScaler ADC / Gateway — unpatched instances |
| **CISA KEV** | CVE-2025-5777 added June 2025 |

Defused Cyber recorded **500+ exploit attempts** against their Citrix honeypot on March 16, 2026, targeting both CVE-2025-5777 (newer flaw) and the still-prevalent CVE-2023-4966 (Citrix Bleed). Security researchers note that surges in old-vulnerability exploitation often precede zero-day disclosure for the same product family.

**Urgency:** This is active mass scanning. Organizations still running unpatched NetScaler must treat this as P0. Check `https://support.citrix.com/` for latest builds for your platform.

---

### 2. DarkSword iOS Exploit Kit — 6 CVEs, 3 Zero-Days, UNC6353/Russia Targeting Ukraine
**Threat Score: 9/10**

| Field | Detail |
|---|---|
| **CVEs** | CVE-2026-20700, CVE-2025-43529, CVE-2025-14174 (zero-days) + CVE-2025-31277, CVE-2025-43510, CVE-2025-43520 |
| **Affected** | iOS 18.4–18.7 / iPadOS equivalents |
| **Fully Patched In** | iOS 18.7.3 / iOS 26.2 (or later) |
| **Threat Actors** | UNC6353 (suspected Russia/GRU), commercial surveillance vendors |

Google GTIG, iVerify, and Lookout jointly disclosed **DarkSword**, a full-chain iOS exploit kit in active use since November 2025. The second commercial iOS 0-day kit discovered this month (after Coruna). Three CVEs were exploited as zero-days before Apple patched them:

- **CVE-2026-20700** — dyld Pointer Authentication Code (PAC) bypass
- **CVE-2025-43529** — JavaScriptCore memory corruption
- **CVE-2025-14174** — ANGLE memory corruption

The kit achieves complete device takeover with **no user interaction** (zero-click via compromised websites hosting malicious iFrame + JS fingerprinting). Russian UNC6353 deploys both DarkSword and Coruna against Ukrainian users by injecting the JavaScript framework into compromised websites. The kit targets credentials, crypto wallets, and personal data with "hit-and-run" exfiltration within seconds.

**Action:** Ensure all iOS/iPadOS devices are on ≥18.7.3 or the iOS 26.x branch ≥26.2. Review web browsing policies; consider iVerify mobile threat detection for high-risk users.

---

### 3. The Gentlemen RaaS — CVE-2024-55591 FortiOS Auth Bypass; 14,700 Devices in Operational Database
**Threat Score: 9/10**

| Field | Detail |
|---|---|
| **CVE** | CVE-2024-55591 |
| **CVSS** | 9.8 Critical |
| **Affected** | FortiOS / FortiProxy — all versions vulnerable to auth bypass |
| **Active Since** | July/August 2025 |

Group-IB published a detailed report on **"The Gentlemen"**, a ~20-member RaaS operation born from a payment dispute on the RAMP cybercrime forum. Primary TTPs:

- **Initial access:** CVE-2024-55591 (critical FortiOS/FortiProxy authentication bypass)
- **Operational database:** ~14,700 already-exploited FortiGate devices globally
- **Ready-to-attack pool:** 969 validated brute-forced FortiGate VPN credentials
- **Defense evasion:** BYOVD (Bring Your Own Vulnerable Driver) to kill security processes at kernel level
- **Impact:** 94 organizations attacked since emergence

CVE-2024-55591 has been mass-exploited since January 2025. Any internet-facing FortiGate running a vulnerable FortiOS version should be considered actively compromised unless patched. Audit for indicators of initial access (unexpected admin accounts, suspicious super_admin configurations).

---

### 4. BMC FootPrints ITSM — Pre-Auth RCE via 4-CVE Chain (First Public Disclosure)
**Threat Score: 8/10**

| Field | Detail |
|---|---|
| **CVEs** | CVE-2025-71257, CVE-2025-71258, CVE-2025-71259, CVE-2025-71260 |
| **CVSS** | Critical (chain result) |
| **Affected** | BMC FootPrints ITSM — all versions prior to September 2025 patch |
| **Patched** | September 2025 (but first public disclosure today) |

Attack chain (unauthenticated remote → RCE):
1. **CVE-2025-71257** (Auth bypass) → extracts guest `SEC_TOKEN` from `/aspnetconfig` password reset endpoint
2. **CVE-2025-71260** (Java deserialization) → `__VIEWSTATE` parameter accepts untrusted data; exploit via AspectJWeaver gadget chain
3. Gadget chain writes arbitrary file to Tomcat webroot → **full RCE as Tomcat service user**
4. **CVE-2025-71258, CVE-2025-71259** (SSRF x2) → internal data leak using stolen SEC_TOKEN

The fix shipped in September 2025, but ITSM platforms are notoriously deprioritized for patching. Operators of internet-facing or intranet-accessible BMC FootPrints instances should verify their version and apply the patch immediately — a public PoC is effectively available through the detailed write-up.

---

### 5. 'PolyShell' — Unauthenticated RCE/XSS on Magento/Adobe Commerce (No Production Patch)
**Threat Score: 8/10**

| Field | Detail |
|---|---|
| **CVE** | Not yet assigned |
| **CVSS** | ~9.1 Critical (researcher estimate) |
| **Affected** | Magento 2 / Adobe Commerce all versions ≤ 2.4.8 |
| **Fix Available** | Only in 2.4.9 alpha2 (NOT in production release) |

Sansec researchers disclosed **PolyShell**: an unauthenticated attacker uploads a polyglot file (simultaneously valid image and PHP script) via the Magento REST API cart custom option endpoint. On most hosting configurations this yields **direct RCE**; on hardened configs it enables stored XSS or session hijacking.

**Critical gap:** Adobe has not released a production patch. The fix only exists in 2.4.9 alpha2.

**Interim mitigations:**
- Block web access to `pub/media/custom_options/` (NGINX/Apache config)
- Audit for existing backdoors in that directory
- Monitor for unexpected PHP files in media directories
- Consider WAF rules blocking `DOCUMENT_ROOT` path in REST requests

Exploit method already circulating among threat actors.

---

### 6. CVE-2026-22557 — Ubiquiti UniFi CVSS 10.0 Path Traversal Enables Unauthenticated Account Takeover
**Threat Score: 7/10**

| Field | Detail |
|---|---|
| **CVE** | CVE-2026-22557 |
| **CVSS** | 10.0 Critical (max) |
| **Affected** | UniFi Network Application ≤ 10.1.85 |
| **Fixed In** | 10.1.89 / 10.2.97 / 9.0.118 |

Maximum-severity unauthenticated path traversal in Ubiquiti UniFi Network Application. Network-adjacent attacker with no privileges and no user interaction required can access files on the underlying server and manipulate them to **take over user accounts**. A second authenticated flaw enables NoSQL injection for privilege escalation.

Relevance: GRU's MooBot botnet previously weaponized Ubiquiti EdgeOS routers for infrastructure (FBI disruption Feb 2024). Russian APT actors have repeatedly abused misconfigured Ubiquiti hardware for proxying and C2. Update to patched version immediately, especially any internet-exposed UniFi controllers.

---

### 7. CursorJack — Proofpoint PoC: One-Click Arbitrary Command Execution via Cursor IDE MCP Deep Link
**Threat Score: 7/10**

| Field | Detail |
|---|---|
| **CVE** | Not yet assigned |
| **Affected** | Cursor IDE (all versions supporting MCP deep links) |
| **PoC** | Public (Proofpoint GitHub) |

Proofpoint disclosed **CursorJack**: attackers abuse the `cursor://` URL protocol handler and MCP deep link support. A target developer who clicks a malicious link and accepts the install prompt:
- Executes **arbitrary local commands** (via `command` field in mcp.json), or
- Installs a **malicious remote MCP server** (full AI context hijacking)

No complex exploitation needed; social engineering via chat, email, or malicious website suffices. Proofpoint published a working PoC on GitHub. This attack surface is new and growing rapidly as AI-assisted development tooling (Cursor, Windsurf, Claude Code, etc.) expands MCP server usage.

**Action for developer security teams:** Audit MCP server allowlists, disable external deep link acceptance, and educate developers not to click unsolicited `cursor://` links.

---

### 8. CVE-2026-22733 — Spring Security Authentication Bypass via CloudFoundry Actuator Path (CVSS 8.2)
**Threat Score: 7/10**

| Field | Detail |
|---|---|
| **CVE** | CVE-2026-22733 |
| **CVSS** | 8.2 High |
| **Affected** | Spring Security 4.0.0–4.0.3, 3.5.0–3.5.11, 3.4.0–3.4.14, 3.3.0–3.3.17, 2.7.0–2.7.31 |
| **Published** | 2026-03-19 |

Spring Boot applications using Actuator can be bypassed when an application endpoint requiring authentication is declared under the CloudFoundry Actuator path. This allows unauthenticated access to secured endpoints. Affects five major Spring Security release lines spanning approximately 8 years of versions.

**Fix versions:** ≥4.0.4, ≥3.5.12, ≥3.4.15, ≥3.3.18, ≥2.7.32. Any Spring Boot application exposing Actuator and running a vulnerable Spring Security version should be patched. Extremely wide enterprise Java exposure.

---

## 📌 Noted (Awareness)

| Item | CVE(s) | Source |
|---|---|---|
| SnappyClient C2 Framework via HijackLoader — crypto theft focus, AMSI bypass + Heaven's Gate | — | THN |
| ClickFix AutoHotKey backdoor via compromised Pakistani government site | — | THN |
| PEGA Infinity: Weak brute-force (CVE-2025-62181) + IDOR (CVE-2025-9559) — medium severity, SEC Consult disclosure | CVE-2025-62181, CVE-2025-9559 | seclists.org |
| Microsoft Teams phishing surge — IT impersonation + Quick Assist remote access | — | Rapid7 |
| Iran cyber infrastructure buildup post-strikes — no large-scale attack yet, elevated regional activity | — | Fortinet |

---

## 📊 Source Coverage

- **Total sources:** 31 configured
- **Checked this cycle:** 28
- **Sources with new findings:** 10
- **Unreachable:** nvd.nist.gov (redirect), group-ib.com (403), securityweek.com article (403)
- **Degraded (partial):** packetstormsecurity.com, msrc.microsoft.com, kb.cert.org, cve.org, dbugs.ptsecurity.com, cert.gov.ua, attackerkb.com, rapid7.com/threat-intel

---

*Watchtower Vulnerability Intelligence | Auto-generated | 2026-03-20 02:00 EEST*
