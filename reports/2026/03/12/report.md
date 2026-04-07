# Threat Intelligence Report — 2026-03-12 Night Cycle

## Executive Summary

The night cycle surfaces **8 findings** (7 news, 1 critical update) and **4 noted items**. The Stryker wiper incident escalates to threat score 10 as operational impact becomes clearer — 5,000+ workers sent home in Ireland alone, personal devices wiped, and US headquarters declared a building emergency. A second n8n RCE (CVE-2025-68613) joins the CISA KEV, marking two actively exploited n8n flaws in two weeks. Two Microsoft Office Preview Pane RCEs (CVE-2026-26113, CVE-2026-26110) are particularly dangerous — zero-click via email preview. ICS Patch Tuesday brings critical fixes across Siemens, Schneider, Moxa, and Mitsubishi Electric.

---

## 🔴 Critical Findings (Threat Score ≥ 8)

### Stryker Wiper Attack — Operational Devastation Confirmed [UPDATE: 8→10]

The Iran-linked Handala hacktivist group's wiper attack against medical technology giant Stryker (NYSE: SYK, $25B revenue) has proven catastrophic. New reporting from Krebs on Security reveals:

- **5,000+ workers sent home** from Stryker's Cork, Ireland headquarters (its largest hub outside the US)
- Personal devices with Microsoft Outlook installed were remotely wiped
- Login pages on surviving devices display the Handala logo
- Stryker's Michigan headquarters voicemail states a "building emergency"
- Staff communicating via WhatsApp as all networked systems are down
- Handala claims to have wiped **200,000+ systems, servers, and mobile devices** across 79 countries

**Attribution:** Palo Alto Networks links Handala to Iran's Ministry of Intelligence and Security (MOIS) via the Void Manticore threat actor. The attack is claimed retaliation for the Feb. 28 missile strike on an Iranian school.

**CISO Action:** If your organization uses Stryker medical devices or services, assume supply chain disruption. Review any network connections to Stryker infrastructure. This demonstrates that state-linked wiper capabilities can cripple a Fortune 500 company globally within hours.

---

### n8n CVE-2025-68613 — Second Actively Exploited RCE Added to CISA KEV [Score: 9]

CISA added CVE-2025-68613 to the Known Exploited Vulnerabilities catalog on March 11, 2026. This is a **separate vulnerability** from CVE-2026-21858 (reported March 7), making it the second actively exploited n8n RCE in two weeks. The flaw resides in n8n's workflow expression evaluation system, allowing improper control of dynamically-managed code resources leading to remote code execution.

- **CVSS:** 9.8
- **CISA Deadline:** March 25, 2026
- **Ransomware Use:** Unknown

**CISO Action:** Patch immediately. If running n8n, audit for both CVE-2025-68613 and CVE-2026-21858. The repeated exploitation of n8n suggests threat actors are actively targeting workflow automation platforms.

---

### CVE-2026-26113 & CVE-2026-26110: Microsoft Office Preview Pane RCE [Score: 8]

Two critical remote code execution flaws in Microsoft Office can be triggered **by simply viewing a malicious message in the Preview Pane**. No additional user interaction required beyond receiving and previewing an email.

- **CVE-2026-26113** — CVSS 8.8
- **CVE-2026-26110** — CVSS 8.8
- Part of the March 2026 Patch Tuesday (84 total fixes)

**CISO Action:** Prioritize these patches for all Office deployments. Consider disabling Preview Pane in Outlook as an interim mitigation across the enterprise. These are prime candidates for targeted spear-phishing.

---

### ICS Patch Tuesday: Siemens, Schneider Electric, Moxa, Mitsubishi Electric [Score: 8]

March 2026 ICS Patch Tuesday brings critical and high-severity advisories from all four major industrial control system vendors. Given the escalating Iran-linked cyber activity and Fortinet's warning about rising regional threats post-strikes, organizations with OT environments should treat these patches as urgent.

**CISO Action:** Coordinate with OT teams for emergency patching windows. Cross-reference with CISA ED 26-03 (Cisco SD-WAN) for any overlapping infrastructure exposure.

---

## 🟡 High Findings (Threat Score 7)

### Michelin Data Breach — Oracle EBS Exploited, 300GB Leaked [Score: 7]

Cybercriminals exploited Oracle E-Business Suite to breach tire giant Michelin, exfiltrating over 300GB of corporate data now being leaked. Demonstrates continued targeting of ERP systems as high-value attack surfaces.

### Zombie ZIP Technique — New AV/EDR Evasion Method [Score: 7]

A newly disclosed technique creates specially crafted compressed files that conceal payloads to evade AV and EDR detection. Security teams should update detection rules and test current tooling against this technique.

### Fortinet, Ivanti, and Intel Multi-Vendor Patch Advisory [Score: 7]

High-severity patches from three major vendors addressing code execution, privilege escalation, and authentication bypass flaws. Given active exploitation campaigns against FortiGate and Ivanti products, patch immediately.

### CVE-2026-21440: AdonisJS Bodyparser Arbitrary File Write [Score: 7]

Critical path traversal in the popular Node.js framework's bodyparser allows unauthenticated arbitrary file writing. Public PoC and writeup available. Any application built on AdonisJS with file upload functionality is potentially vulnerable.

---

## 📝 Noted Items

| Item | Summary |
|------|---------|
| Meta Platforms | Disabled 150K+ accounts linked to Southeast Asian scam centers; 21 arrests in Thailand |
| Bell Ambulance | Data breach impacted 238K individuals — SSN and driver license numbers exposed |
| Wekan CVE-2026-30844 | SSRF and unauthorized data manipulation disclosed by GitHub Security Lab |
| AFFINE | Access control bypass vulnerability disclosed by GitHub Security Lab |

---

## Source Coverage

| Metric | Value |
|--------|-------|
| Total Sources | 30 |
| Checked | 30 |
| With Findings | 14 |
| Unreachable | 0 |
| Degraded | bugcrowd.com, cert.gov.ua |

---

*Generated: 2026-03-12T07:30 UTC+2 — Night Cycle*
