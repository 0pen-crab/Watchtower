# Vulnerability Report — 2026-02-28 (Night Cycle)

## Executive Summary

Six findings and five noted items from scanning 72 of 90 sources (18 unreachable due to platform restrictions on X/Twitter, Telegram, Discord, and geo-restricted sites). Key highlights include a massive Chinese espionage campaign disrupted by Google/Mandiant, a critical VoIP phone vulnerability with a public Metasploit module, a supply chain attack via npm, and an escalation in North Korean threat actor operations.

---

## Findings

### 1. UNC2814 GRIDTIDE: Chinese Espionage Campaign Abusing Google Sheets API (Threat Score: 9/10)

Google's Threat Intelligence Group, Mandiant, and partners disrupted a global espionage campaign attributed to Chinese threat actor UNC2814. The campaign deployed a novel C-based backdoor called GRIDTIDE that abuses the Google Sheets API for evasive command-and-control operations. Active since at least 2023, it impacted 53 organizations across 42 countries, targeting telecommunications and government networks. GRIDTIDE authenticates using a hardcoded private key and supports command execution, file upload/download via spreadsheet cells. Google terminated all associated cloud projects, sinkholed domains, and revoked API access.

**Source:** BleepingComputer, Google Cloud Blog

---

### 2. CVE-2026-2329: Critical Unauthenticated RCE in Grandstream GXP1600 VoIP Phones (Threat Score: 8/10)

Rapid7 Labs discovered a critical unauthenticated stack-based buffer overflow (CVSSv4 9.3) in Grandstream GXP1600 series VoIP phones. The vulnerability exists in the web-based API service and affects all six models in the series (GXP1610/1615/1620/1625/1628/1630) in default configuration. A Metasploit exploit module achieving root-level RCE has been published, along with a post-exploitation module for credential extraction. Firmware version 1.0.7.81 remediates the issue.

**Source:** Rapid7 Blog

---

### 3. Malicious npm Package "ambar-src" Deploys Multi-Platform Malware (Threat Score: 7/10)

Tenable Research investigated the malicious npm package "ambar-src" which accumulated approximately 50,000 downloads before removal. The package typosquats the legitimate "ember-source" package and exploits npm's preinstall script hooks to execute malicious code during installation without any explicit import. It deploys OS-specific open-source malware variants targeting Windows, Linux, and macOS developers.

**Source:** Tenable Blog

---

### 4. Lazarus Group Collaborating with Medusa Ransomware (Threat Score: 8/10)

Symantec/Broadcom reports that North Korea's Lazarus Group has begun collaborating with Medusa ransomware operators. This represents a significant evolution in the state-sponsored group's tactics, expanding from traditional espionage and cryptocurrency theft into ransomware-as-a-service partnerships, potentially increasing the sophistication and reach of Medusa ransomware operations.

**Source:** Symantec/Broadcom Security Blog

---

### 5. [UPDATE] CISA Warns RESURGE Malware Persists on Ivanti Devices Post-Patch — CVE-2025-0282 (Threat Score: 8/10, Previous: 7/10)

CISA published a new advisory warning that RESURGE malware variants can remain dormant on Ivanti Connect Secure devices even after patching CVE-2025-0282. Organizations are advised to perform factory resets rather than relying solely on patches, and to conduct thorough forensic analysis of potentially compromised devices.

**Source:** BleepingComputer, CISA

---

### 6. CVE-2025-15467: Critical OpenSSL Vulnerability in Fortinet Products (Threat Score: 6/10)

Fortinet published a critical-severity PSIRT advisory (FG-IR-26-076) for CVE-2025-15467, an OpenSSL vulnerability involving maliciously crafted AEAD parameters in CMS AuthEnvelopedData message parsing. The vulnerability affects FortiAP, FortiClientWindows, and FortiNAC-F across multiple versions.

**Source:** FortiGuard PSIRT

---

## Noted Items

| Product | CVE | Summary |
|---------|-----|---------|
| FortiOS | CVE-2025-55018 | Medium-severity HTTP request smuggling vulnerability |
| Firefox/Thunderbird | — | MFSA 2026-13 through 2026-17 security updates released Feb 24 |
| intra-mart Accel Platform | — | JVN#80500630: Untrusted data deserialization in IM-LogicDesigner |
| Fujitsu BIOS Driver | — | JVNVU#96854657: Out-of-bounds write in fbiosdrv.sys |
| Arkanix Stealer | — | Kaspersky analysis of new C++/Python MaaS information stealer |

---

## Dedup Exclusions

The following were seen in sources but excluded as already reported:
- CVE-2026-20127 — Cisco Catalyst SD-WAN (reported 2026-02-25)
- CVE-2026-1731 — BeyondTrust RS/PRA (reported 2026-02-16)
- CVE-2026-25108 — Soliton FileZen (reported 2026-02-13)

---

## Source Coverage

- **Total sources:** 90
- **Checked:** 72
- **With findings:** 14
- **Unreachable (18):** x.com (all accounts), t.me, discord.gg, owasp.org/slack, 0day.today, threatpost.com, vulndb.cyberriskanalytics.com, cnvd.org.cn, cert.gov.ua, securityfocus.com, opencve.io, strobes.co, cybersecuritydispatch.com, dbugs.ptsecurity.com, habr.com, teletype.in, acsc.gov.au
- **Degraded (1):** reddit.com (content not rendering)
