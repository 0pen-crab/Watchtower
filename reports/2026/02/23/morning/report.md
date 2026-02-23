# Watchtower Morning Report — Monday, February 23, 2026

**Cycle:** Morning | **Date:** 2026-02-23 | **Analyst:** Watchtower AI

---

## 🔴 CRITICAL — Active Exploitation

### 1. BeyondTrust RS/PRA Command Injection (CVE-2026-1731) — Now in Ransomware Campaigns
- **CVSS:** 9.9 | **CISA KEV:** Yes (added 2026-02-13, due 2026-02-16) | **Ransomware:** Confirmed
- **What:** Unauthenticated OS command injection in BeyondTrust Remote Support and Privileged Remote Access via the `thin-scc-wrapper` WebSocket endpoint. Same endpoint as CVE-2024-12356. Attacker-controlled `remoteVersion` parameter lacked numeric validation, allowing shell command injection.
- **Update (this week):** CISA updated KEV to flag active ransomware exploitation. Unit 42 published detailed analysis showing exploitation for web shells (VShell), backdoors, C2, lateral movement, and data exfiltration across financial services, legal, tech, education, healthcare in US, France, Germany, Australia, Canada.
- **Rapid7 analysis:** Full technical deep-dive published on AttackerKB confirming trivial exploitability. Patch adds numeric-only validation on `remoteVersion`.
- **Action:** Patch immediately. If unpatched past 2026-02-16 deadline, assume compromise and investigate.

### 2. Microsoft Patch Tuesday — 6 Zero-Days Under Active Exploitation
- **CVE-2026-21510** — Windows Shell security feature bypass (click-to-exploit, all Windows versions)
- **CVE-2026-21513** — MSHTML security bypass
- **CVE-2026-21514** — Microsoft Word security bypass
- **CVE-2026-21533** — Windows RDS local privilege escalation to SYSTEM
- **CVE-2026-21519** — DWM elevation of privilege (second consecutive month for DWM zero-day)
- **CVE-2026-21525** — Windows Remote Access Connection Manager DoS (VPN disruption)
- **Action:** Apply February Patch Tuesday updates urgently. CVE-2026-21510 is especially dangerous — single click, no consent dialog, all Windows.

### 3. Dell RecoverPoint for VMs — Hard-Coded Credentials (CVE-2026-22769)
- **CISA KEV:** Yes (added 2026-02-18, **due 2026-02-21** — already overdue)
- **What:** Hard-coded credentials allow unauthenticated remote root access and persistence.
- **Action:** Patch or isolate immediately. CISA deadline has passed.

### 4. Google Chromium CSS Use-After-Free (CVE-2026-2441)
- **CISA KEV:** Yes (added 2026-02-17, due 2026-03-10)
- **What:** Heap corruption via crafted HTML. Affects Chrome, Edge, Opera, all Chromium-based browsers.
- **Action:** Update all Chromium browsers.

---

## 🟠 HIGH — Significant Vulnerabilities & Threats

### 5. RoundCube Webmail — Two Vulnerabilities Added to CISA KEV
- **CVE-2025-68461** — XSS via SVG animate tag
- **CVE-2025-49113** — Deserialization RCE (authenticated)
- Both added to KEV on 2026-02-20, due 2026-03-13.
- **Context:** RoundCube remains a high-value target for espionage groups.

### 6. Grandstream GXP1600 VoIP Phones — Root RCE (CVE-2026-2329)
- **CVSS:** Critical | **Auth required:** No
- **What:** Remote unauthenticated root access enabling silent eavesdropping on calls.
- **Action:** Patch or segment VoIP infrastructure. No workaround available.

### 7. AI-Assisted Hacker Compromises 600+ FortiGate Firewalls in 55 Countries
- **Source:** Amazon Threat Intelligence
- **What:** Russian-speaking, financially motivated actor used commercial GenAI tools to automate a campaign exploiting exposed management ports and weak credentials (not FortiGate vulns). 600+ devices compromised across 55 countries in 5 weeks (Jan 11 – Feb 18, 2026).
- **Key insight:** AI enabled an unsophisticated actor to operate at scale. No vulnerability exploitation — purely credential stuffing + exposed management interfaces.
- **Action:** Audit FortiGate management port exposure, enforce MFA, rotate credentials.

### 8. Ivanti Zero-Day Exploitation Traced Back to July 2025
- Exploitation surging. Attackers delivering shells, conducting recon, downloading malware.
- **Action:** Review Ivanti patching status and check for indicators of compromise.

---

## 🟡 NOTABLE — Malware, Breaches & Emerging Threats

### 9. PromptSpy — First Android Malware Using Generative AI at Runtime
- Uses Google Gemini to analyze screen elements and generate step-by-step persistence instructions, adapting to any device/layout/OS version.
- Captures lockscreen data, blocks uninstall, screenshots, screen recording.
- **Significance:** First known malware leveraging LLMs operationally at runtime. Expect rapid copycats.

### 10. Starkiller — Advanced Phishing-as-a-Service with Real-Time MFA Bypass
- Dynamically loads real login pages via headless Chrome in Docker containers.
- Acts as MITM reverse proxy, capturing credentials + session tokens in real-time.
- Defeats MFA by relaying full auth flow. Includes keylogger, cookie theft, geo-tracking, Telegram alerts, campaign analytics.
- **Significance:** Dramatically lowers barrier for MFA-bypass phishing.

### 11. Arkanix Stealer — AI-Developed Info-Stealer
- Short-lived AI-assisted experiment promoted on dark web forums (late 2025).
- Another data point in the AI-assisted malware development trend.

### 12. Predator Spyware — iOS SpringBoard Hooking
- Intellexa's Predator now hooks iOS SpringBoard to hide mic/camera recording indicators while secretly streaming feeds.
- **Action:** High-value targets should review MDM and device integrity monitoring.

### 13. Cline CLI 2.3.0 Supply Chain Attack
- Compromised npm publish token used to inject `openclaw@latest` installation via postinstall script.
- Package downloaded by developers worldwide before detection.
- **Significance:** Ongoing trend of npm/PyPI supply chain compromises.

### 14. Kimwolf Botnet Swamps I2P Anonymity Network
- 700,000 botnet nodes accidentally disrupted I2P in a Sybil attack while trying to use it for C2 fallback.
- I2P network significantly degraded since Feb 3.

### 15. SLSH (Scattered Lapsus ShinyHunters) Extortion Escalation
- Combining data theft with executive harassment, swatting, DDoS, media notification.
- Recent victims across SaaS, financial services. Figure (blockchain lender) breach: 1M records leaked.
- Unit 221B advises: never pay, never engage beyond "we're not paying."

---

## 📊 Breach Tracker

| Organization | Type | Impact |
|---|---|---|
| French Bank Registry (FICOBA) | Unauthorized access | 1.2M bank accounts exposed |
| PayPal | Software error | SSNs exposed for ~6 months |
| Figure (blockchain lender) | ShinyHunters breach | ~1M user records, 2GB data leaked |
| Advantest (Japan) | Ransomware | Customer/employee data potentially stolen |
| UMMC (Mississippi) | Ransomware | All clinics closed statewide |

---

## 📈 Trends & Analysis

### AI in Offense is Accelerating
Three distinct manifestations this week:
1. **AI-assisted campaigns at scale** (FortiGate — AI compensating for low skill)
2. **AI-generated malware** (Arkanix Stealer, PromptSpy using Gemini at runtime)
3. **AI vulnerability research** (AISLE found 12/12 OpenSSL zero-days including CVE-2025-15467, CVSS 9.8)

### AI in Defense — AISLE OpenSSL Discovery
- AI system found all 12 OpenSSL zero-days in January 2026 release, including bugs present since 1998.
- Proposed accepted patches for 5 of 12. This is historically unprecedented concentration from a single research entity.
- **Schneier's take:** "AI vulnerability finding is changing cybersecurity, faster than expected."

### CISA KEV Activity (Last 7 Days)
- 11 new entries since Feb 12, including BeyondTrust (ransomware-confirmed), RoundCube (2), Dell, Chromium, TeamT5, SolarWinds WHD, Notepad++, Zimbra, GitLab, MS Config Manager.
- Notable: TeamT5 ThreatSonar Anti-Ransomware product itself has an exploited file upload vuln (CVE-2024-7694).

---

## 🎯 Recommended Priority Actions

1. **BeyondTrust RS/PRA** — Patch CVE-2026-1731 NOW. Assume compromise if unpatched.
2. **Microsoft February patches** — Deploy immediately, especially CVE-2026-21510 (Windows Shell bypass).
3. **Dell RecoverPoint** — CVE-2026-22769 deadline passed. Patch or isolate.
4. **FortiGate management ports** — Audit exposure, enforce MFA, check for unauthorized access.
5. **Chromium browsers** — Update for CVE-2026-2441.
6. **RoundCube** — Patch both KEV vulnerabilities.
7. **Grandstream VoIP** — Patch CVE-2026-2329 or segment.
8. **Ivanti** — Review patch status and hunt for compromise indicators.

---

*Sources: BleepingComputer, The Hacker News, Krebs on Security, SecurityWeek, CISA KEV, AttackerKB, Schneier on Security, Fortinet FortiGuard Labs, Cloudflare, Help Net Security, Packet Storm*
