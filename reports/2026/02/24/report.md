# Vulnerability Intelligence Report — 2026-02-24 Night Cycle

**Generated:** 2026-02-24T02:00:00+02:00
**Cycle:** night
**Sources checked:** 91/91
**New findings:** 8 | **Noted:** 10

---

## 🔴 Critical Findings

### 1. CVE-2026-1603 — Ivanti Endpoint Manager Authentication Bypass
- **CVSS:** 8.6 (Ivanti) / 7.5 (NVD)
- **Product:** Ivanti Endpoint Manager (EPM) < 2024 SU5
- **Type:** Authentication Bypass → Credential Exposure
- **Exploitation:** No public exploitation confirmed yet; Horizon3.ai published Rapid Response test
- **Impact:** Remote unauthenticated attacker can access stored credential data. Given EPM's elevated privileges across managed endpoints, credential exposure enables lateral movement and broad compromise.
- **Action:** Patch to 2024 SU5 immediately. Audit credential stores. Monitor for follow-on access.
- **Sources:** Horizon3.ai, NVD

### 2. AI-Augmented FortiGate Campaign — 600+ Firewalls Compromised
- **Threat Actor:** Russian-speaking, financially motivated, low-to-medium skill
- **Type:** Mass exploitation using commercial gen AI tools
- **Scope:** 600+ FortiGate devices across 55+ countries (South Asia, Latin America, West Africa, Northern Europe, Southeast Asia)
- **Method:** Automated scanning for exposed admin interfaces + weak auth. Stole full device configs including passwords and network architecture. Moved into Active Directory and targeted backup systems.
- **AI Usage:** Attack planning, script automation, operational checklists, credential extraction tools — all AI-generated. Code worked for standard paths but failed in edge cases.
- **Significance:** First major documented campaign of a low-skill actor achieving high-volume results via commercial AI. Preparation for possible ransomware follow-on.
- **Action:** Audit FortiGate admin exposure. Rotate credentials. Check for unauthorized config exports.
- **Source:** Amazon threat intelligence (published Feb 20), The Record

### 3. Dell CVE-2026-22769 — Grimbolt Malware Evolution (UPDATE)
- **CVSS:** 10.0
- **Product:** Dell RecoverPoint for Virtual Machines
- **What's New:** Google/Mandiant confirmed UNC6201 (overlaps Silk Typhoon/UNC5221) has replaced Brickstorm with **Grimbolt** — a more advanced, harder-to-detect successor. Dell released patch Feb 23.
- **Impact:** <12 confirmed orgs, but "full scale unknown." Actor likely still active in unpatched/unremediated environments. 18+ months of access since mid-2024.
- **Action:** Patch immediately. Hunt for Grimbolt indicators in any environment previously targeted by Brickstorm.
- **Sources:** CyberScoop, Google GTIG, Mandiant

---

## 🟠 High Findings

### 4. GIMP Multiple RCE Vulnerabilities (CVE-2026-2044, 2045, 2047, 2048)
- **CVSS:** 7.8 each
- **Products:** GIMP (all platforms)
- **Type:** File parsing vulnerabilities — OOB write (XWD), heap buffer overflow (ICNS), uninitialized memory (PGM)
- **Vector:** Crafted image files trigger code execution when opened
- **Action:** Update GIMP. Ubuntu USN-8057-1 covers 24.04, 22.04, 20.04, 18.04, 16.04.
- **Sources:** ZDI-26-118 through ZDI-26-121, Ubuntu

### 5. Advantest Semiconductor Supplier — Ransomware Attack
- **Target:** Advantest Corporation (Tokyo, Japan) — $6.4B revenue, leading semiconductor test equipment manufacturer
- **Date:** Feb 19, 2026
- **Impact:** Multiple company systems affected. Critical supplier to ML, 5G, autonomous vehicle chip production.
- **Significance:** Supply chain risk to global semiconductor manufacturing.
- **Source:** The Record

### 6. France FICOBA National Bank Database Breach
- **Target:** French National Bank Accounts File (FICOBA) — 80M+ individuals
- **Impact:** 1.2M accounts of 300M+ queried. Attacker impersonated civil servant using stolen credentials.
- **Data Exposed:** Account numbers, names, addresses, some tax IDs. No account balances or transactions.
- **Source:** The Record, DGFiP

### 7. Phobos Ransomware Affiliate Arrested in Poland
- **Event:** Polish Central Bureau for Combating Cybercrime arrested 47-year-old affiliate
- **Context:** Part of Europol's "Phobos Aetor" operation. Phobos claimed 1,000+ victims globally, $16M+ in extortion.
- **Seized:** Computer, multiple phones, credentials, credit card numbers, IP addresses for attack servers.
- **Source:** CyberScoop, CBZC Poland

### 8. Air Côte d'Ivoire Ransomware (INC Gang)
- **Target:** Air Côte d'Ivoire (partially owned by Air France)
- **Date:** Feb 8, 2026 attack; confirmed Feb 21
- **Impact:** 208GB data stolen by INC ransomware gang. Business continuity plans activated.
- **Source:** The Record

---

## 📝 Noted (Lower severity / context updates)

| # | Item | Details |
|---|------|---------|
| 1 | Docker Desktop MCP Server (ZDI-26-123) | Cleartext credential storage, CVSS 5.5, beta only, no CVE assigned |
| 2 | CVE-2026-2490 — RustDesk Client | Info disclosure via link following, CVSS 5.5 |
| 3 | CVE-2026-2492 — TensorFlow HDF5 | Local privilege escalation, CVSS 7.0 |
| 4 | CVE-2025-62676 — FortiClient VPN LPE | Link following LPE, CVSS 7.8 |
| 5 | Dassault eDrawings (CVE-2026-1334, 1335) | EPRT file parsing RCE, CVSS 7.8 |
| 6 | AD Dynamic Objects stealthy evasion | Tenable research — self-destructing AD objects bypass forensics |
| 7 | Kubernetes Ingress NGINX retirement | Datadog Labs advisory on migration urgency |
| 8 | Trail of Bits: Perplexity Comet prompt injection | Gmail data exfiltration via AI assistant manipulation |
| 9 | Trend Micro: OpenClaw agentic AI research | Security analysis of agentic AI paradigm risks |
| 10 | MongoDB MongoBleed (CVE-2025-14847) | Info disclosure, in-the-wild exploitation per avleonov |

---

## Source Coverage

**Total sources in SOURCES.md:** 91
**Checked:** 91
**Returned useful data:** 72
**Blocked/errored:** 19 (Cloudflare blocks, 404s, JS-rendered only, auth walls)
**Dedup gate:** All findings cross-referenced against 30-day report history. Items already covered (BeyondTrust CVE-2026-1731, Chrome CVE-2026-2441, Grandstream CVE-2026-2329, OpenSSL CVE-2025-15467, etc.) excluded from findings.
