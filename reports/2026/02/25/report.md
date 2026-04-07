# Watchtower Report — 2026-02-25 Night Cycle

**Generated:** 2026-02-25T02:00:00+02:00
**Cycle:** night
**Sources checked:** 91/91

---

## 🔴 CRITICAL — CVE-2026-25108: Soliton FileZen OS Command Injection (CISA KEV)

**CVSS:** 8.8 | **Status:** Actively exploited (added to CISA KEV 2026-02-24)

Soliton FileZen, a file-sharing appliance widely used in Japan and APAC, contains an OS command injection vulnerability. When the Antivirus Check Option is enabled, an authenticated user can send a specially crafted HTTP request to execute arbitrary OS commands on the underlying system. CISA added this to the KEV catalog on February 24, indicating confirmed in-the-wild exploitation. Organizations using FileZen should patch immediately or disable the antivirus check feature as a temporary mitigation.

**Action:** Patch immediately. CISA remediation deadline applies.
**Sources:** CISA KEV, OpenCVE, SecurityWeek

---

## 🔴 CRITICAL — Reynolds Ransomware: BYOVD-Based EDR Killer

**Severity:** Critical | **Status:** Active campaigns

A new ransomware strain dubbed "Reynolds" embeds a bring-your-own-vulnerable-driver (BYOVD) component to disable endpoint detection and response (EDR) security tools before encrypting victim systems. The ransomware deploys a signed but vulnerable Windows driver to gain kernel-level access, terminates security processes, and then proceeds with file encryption. This technique follows the trend seen in other ransomware families but Reynolds' integrated approach makes it particularly dangerous—the BYOVD payload is embedded directly in the ransomware binary rather than delivered as a separate tool.

**Action:** Monitor for vulnerable driver loading, enforce driver blocklists, ensure tamper protection is enabled on EDR.
**Sources:** The Hacker News

---

## 🟠 HIGH — Andariel (DPRK) Deploys Three New RATs: StarshellRAT, JelusRAT, GopherRAT

**Attribution:** Andariel / Reconnaissance General Bureau 3rd Bureau (DPRK)
**Targets:** European public/legal sector, South Korean ERP software

WithSecure identified and attributed a breach of a European customer in the public/legal sector to the Andariel group with high confidence. The investigation revealed three previously undocumented remote access trojans: **StarshellRAT**, **JelusRAT**, and **GopherRAT**. The threat actor accessed documents relating to anti-money laundering (aligned with DPRK's known money laundering to evade international sanctions). A second attack targeted a South Korean ERP vendor—the same vendor Andariel had previously targeted in 2017 and 2024. The group also used PrintSpoofer, PetitPotato for privilege escalation, and BYOVD techniques to kill AV/EDR products.

**Action:** Hunt for IOCs from WithSecure's report. Monitor for BYOVD activity and lateral movement patterns.
**Sources:** WithSecure Labs

---

## 🟠 HIGH — Diesel Vortex Phishing Campaign Targets US/European Freight & Logistics

**Severity:** High | **Status:** Active

A financially motivated threat group dubbed "Diesel Vortex" is conducting credential-stealing phishing attacks against freight and logistics operators in the United States and Europe. The campaign uses 52 domains mimicking legitimate logistics platforms and freight brokerages. Given the supply chain nature of the targets, compromised credentials could enable further downstream attacks including business email compromise, cargo theft coordination, and supply chain fraud.

**Action:** Alert logistics sector partners, block IOC domains, strengthen email authentication.
**Sources:** Bleeping Computer

---

## 🟠 HIGH — SSHStalker Botnet: IRC C2 Targeting Linux via Legacy Kernel Exploits

**Severity:** High | **Status:** Active

A new botnet dubbed "SSHStalker" uses IRC-based command and control to coordinate compromised Linux systems. The botnet propagates by exploiting legacy kernel vulnerabilities and brute-forcing SSH credentials. Once installed, it provides persistent backdoor access and can be commanded to launch DDoS attacks or mine cryptocurrency. The use of IRC C2 is a deliberate choice to evade modern detection systems tuned for HTTP/HTTPS-based C2 channels.

**Action:** Patch Linux kernels, enforce SSH key-based auth, monitor for IRC traffic on unexpected ports.
**Sources:** The Hacker News

---

## 🟠 HIGH — CVE-2025-14905: Red Hat 389-ds-base Heap Buffer Overflow (RCE)

**CVSS:** 7.2 | **Product:** 389 Directory Server (Red Hat)

A heap buffer overflow vulnerability exists in the `schema_attr_enum_callback` function within `schema.c` of 389-ds-base. The code incorrectly calculates buffer size by summing alias string lengths without accounting for additional formatting characters. When a large number of aliases are processed, this leads to a heap overflow that can be triggered remotely, potentially enabling denial of service or remote code execution.

**Action:** Apply Red Hat security updates for 389-ds-base and RHDS.
**Sources:** OpenCVE, Red Hat

---

## 🟠 HIGH — Keenadu Firmware Backdoor Infects Android Tablets via Signed OTA Updates

**Severity:** High | **Status:** Active in the wild

A firmware-level backdoor dubbed "Keenadu" is being distributed through signed OTA (over-the-air) updates to Android tablets. The backdoor is embedded in the system partition and survives factory resets. It provides persistent remote access, can exfiltrate data, and install additional payloads. The use of legitimately signed OTA mechanisms makes this particularly insidious as it bypasses standard Android security verification.

**Action:** Verify OTA update chain integrity, monitor for anomalous system-level processes on Android devices.
**Sources:** The Hacker News

---

## 🟡 MEDIUM — 1Campaign: Cybercrime Platform Enabling Persistent Malicious Google Ads

**Severity:** Medium | **Impact:** Broad

A newly identified cybercrime-as-a-service platform called "1Campaign" is enabling threat actors to run malicious Google Ads campaigns that evade detection and remain online for extended periods. The service provides cloaking infrastructure, fingerprinting of security researchers, and automated ad rotation. This explains the persistence of many malvertising campaigns that have been difficult to take down.

**Action:** Implement DNS-based ad blocking, educate users on malvertising risks, report malicious ads through Google's abuse channels.
**Sources:** Bleeping Computer

---

## 🟡 MEDIUM — CarGurus Data Breach: 12.4M Records Published by ShinyHunters

**Severity:** Medium (data breach) | **Attribution:** ShinyHunters

The ShinyHunters extortion group published personal information from over 12 million records allegedly stolen from CarGurus, a major U.S. digital auto platform. The leaked data reportedly includes names, email addresses, phone numbers, and partial address information from buyer and seller accounts. This follows the group's recent claims against Odido and Wynn Resorts, indicating an active and aggressive extortion campaign.

**Action:** Monitor for credential stuffing using CarGurus data, alert affected users.
**Sources:** Bleeping Computer

---

## 🟡 MEDIUM — Wynn Resorts Employee Data Breach (ShinyHunters)

**Severity:** Medium (data breach) | **Attribution:** ShinyHunters

Wynn Resorts confirmed that a threat actor stole employee data from its systems after the company was listed on ShinyHunters' data leak site. The breach affects employee personal information. This is part of ShinyHunters' broader extortion campaign alongside CarGurus and Odido.

**Action:** Employee identity monitoring, credential rotation for affected personnel.
**Sources:** Bleeping Computer

---

## 🟡 MEDIUM — Active Directory Dynamic Objects: Stealthy Attack Technique (Tenable Research)

**Severity:** Medium | **Type:** Technique/Research

Tenable published research demonstrating how Active Directory's "dynamic objects" feature can be abused by attackers for stealthy persistence. Dynamic objects automatically self-destruct without leaving tombstones, which means they bypass standard forensic analysis. Attackers can use them to create temporary machine accounts that self-delete, pollute ACLs with orphan SIDs, and establish cloud persistence through stale Entra ID users—all while leaving no forensic evidence.

**Action:** Implement real-time monitoring for objects with `entryTTL` or `msDS-Entry-Time-To-Die` attributes. Correlate with orphan SID detection.
**Sources:** Tenable Blog

---

## 🟡 MEDIUM — FBI FLASH: ATM Jackpotting via Ploutus Malware ($20M Stolen in 2025)

**Severity:** Medium | **Type:** Advisory

The FBI issued a FLASH alert regarding ATM jackpotting attacks using Ploutus malware, which exploits XFS (Extensions for Financial Services) software. The advisory notes that $20M was stolen through this technique in 2025 and provides prevention guidance. Ploutus has been active since 2013 but continues to evolve and remains effective against ATMs running older software.

**Action:** Update ATM software, implement physical security controls, monitor for XFS manipulation.
**Sources:** SC World, FBI

---

## 🟡 MEDIUM — Phobos Ransomware Affiliate Arrested in Poland

**Severity:** Medium | **Type:** Law enforcement action

Polish authorities arrested an alleged affiliate of the Phobos ransomware operation. Phobos has been one of the more accessible ransomware-as-a-service platforms, targeting small and medium businesses. The arrest demonstrates continued international cooperation in ransomware enforcement.

**Action:** No immediate technical action. Monitor for potential Phobos infrastructure changes.
**Sources:** CyberScoop

---

## 🟡 MEDIUM — ToxicSkills: 1,467 Malicious Payloads Found in AI Agent Skills (Snyk Research)

**Severity:** Medium | **Type:** Supply chain research

Snyk's research on AI agent skills supply chain found prompt injection in 36% of analyzed skills and identified 1,467 malicious payloads in a study of agent skills. The research specifically examined the ClawHub ecosystem and found widespread credential leaks (280+ leaky skills exposing API keys and PII). This highlights the growing attack surface in AI agent ecosystems where skills/tools are shared and consumed with minimal security review.

**Action:** Audit AI agent skill configurations, scan for credential exposure in skill definitions.
**Sources:** Snyk Blog

---

## ℹ️ INFORMATIONAL

- **Salt Typhoon threats "still very much ongoing"** — FBI confirmed at CyberTalks 2026 that Chinese APT Salt Typhoon continues targeting US telecom infrastructure (CyberScoop)
- **Cisco warns MCP (Model Context Protocol) is "woefully insecure"** — described as the "SolarWinds of AI" risk (Cybersecurity Dive)
- **CrowdStrike report:** Threat groups moving at record speeds with AI assistance, increasingly abusing legitimate tools (Cybersecurity Dive)
- **Kubernetes Ingress NGINX retirement warning** — Datadog Security Labs flagged migration urgency (Datadog)
- **Advantest (chip-testing manufacturer)** deployed incident response protocols following a cybersecurity incident (Infosecurity Magazine)

---

## Dedup Notes

The following items from today's scan were already covered in prior reports and excluded:
- CVE-2026-2441 (Chrome zero-day) — reported 2026-02-17
- CVE-2026-1731 (BeyondTrust RCE) — reported 2026-02-10
- SANDWORM_MODE npm — reported 2026-02-24
- FortiGate 600+ AI-assisted attacks — reported 2026-02-21
- MuddyWater Olalampo — reported 2026-02-24
- ShinyHunters SSO vishing — reported 2026-02-21
- Lazarus/Medusa ransomware — reported 2026-02-24
- CVE-2026-21858 (n8n) — reported 2026-02-24
- CVE-2026-22200 (osTicket) — reported 2026-02-24
- CVE-2026-24061 (GNU telnetd) — reported 2026-02-24
- Dell RecoverPoint CVE-2026-22769 — reported 2026-02-17
- ClickFix campaigns — reported 2026-02-14
- OpenClaw security issues — reported 2026-02-21
- Anthropic distillation accusations — reported 2026-02-24
- Roundcube KEV — reported 2026-02-14
- Password manager vault theft research — reported 2026-02-17
