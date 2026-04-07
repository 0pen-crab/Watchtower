# Vulnerability Intelligence Report — 2026-02-26 Night

## Critical Findings

### 🔴 CVE-2026-20127 — Cisco SD-WAN Controller Authentication Bypass (CVSS 10.0)
**Threat Score: 10/10 | Exploited in the Wild Since 2023**

A critical authentication bypass vulnerability in the Cisco Catalyst SD-WAN Controller has been disclosed and added to the CISA Known Exploited Vulnerabilities catalog. The flaw has been exploited as a zero-day since at least 2023. CISA issued Emergency Directive 26-03 requiring all federal civilian agencies to remediate immediately. This is being treated with the highest urgency given the widespread deployment of Cisco SD-WAN infrastructure across government and enterprise networks.

- **Source:** BleepingComputer, CISA
- **Status:** Active exploitation confirmed, Emergency Directive issued
- **Action:** Patch immediately per Cisco advisory

---

### 🔴 UNC2814 GRIDTIDE — Chinese Espionage via Google Sheets C2 (53 Orgs, 42 Countries)
**Threat Score: 9/10**

Google Threat Intelligence Group and Mandiant disrupted a global espionage campaign attributed to Chinese state-sponsored threat actor UNC2814. The campaign deployed a novel C-based backdoor called GRIDTIDE that abuses Google Sheets API for command-and-control, making detection extremely difficult as C2 traffic blends with legitimate Google API calls. The campaign has impacted 53 confirmed organizations in 42 countries, with suspected infections in 20 more. Primary targets include telecommunications providers and government agencies.

GRIDTIDE supports command execution, file upload/download, and uses URL-safe base64 encoding to evade web monitoring. Google has sinkholed all known C2 infrastructure and revoked API access.

- **Source:** BleepingComputer, Google Cloud Blog
- **IOCs:** Available in Google's report

---

### 🟠 Zyxel Critical RCE in Consumer Routers — 12+ Models, Some Unpatchable
**Threat Score: 8/10**

Zyxel warned of a critical remote code execution flaw affecting over a dozen consumer router models. Some end-of-life devices will not receive patches, leaving users permanently exposed. Given Zyxel routers' history of exploitation by botnets (Mirai variants), this is a high-priority issue for ISPs and home networks.

- **Source:** BleepingComputer

---

### 🟠 SolarWinds Serv-U — Four New Critical Vulnerabilities Patched
**Threat Score: 8/10**

SolarWinds released patches for four new critical vulnerabilities in Serv-U file transfer software. This follows the actively exploited CVE-2025-40538 (added to CISA KEV). Given Serv-U's history as a target for state-sponsored actors (particularly Chinese APTs), organizations should patch urgently.

- **Source:** SecurityWeek

---

## High-Priority Findings

### 🟡 US Sanctions Russian Exploit Broker Operation Zero
**Threat Score: 7/10**

The US Treasury sanctioned Operation Zero (St. Petersburg, Russia), its owner Sergey Zelenyuk, and five associated entities under the Protecting American Intellectual Property Act — the first use of this law. The action followed the conviction of Peter Williams, a former L3Harris/Trenchant executive who sold 8 stolen zero-day exploits to Operation Zero for $1.3M in cryptocurrency. Williams received 87 months in prison.

Operation Zero openly offers millions in bounties for exploits targeting US-built software and claims to sell exclusively to Russian government clients.

- **Source:** BleepingComputer, US Treasury

---

### 🟡 Fake Next.js Job Interview Campaign — Developer Machines Targeted
**Threat Score: 7/10**

Microsoft Defender team documented a coordinated supply chain campaign using malicious Next.js repositories disguised as job interview coding tests. Three infection vectors: VS Code `folderOpen` triggers, trojanized `npm run dev`, and backend startup module exfiltrating `process.env`. Stage 2 includes persistent C2 polling and file exfiltration. Multiple repositories across Bitbucket sharing infrastructure.

- **Source:** BleepingComputer, Microsoft Security Blog

---

## Updates

### 🔄 Lazarus Group + Medusa Ransomware Collaboration Confirmed
**Threat Score: 8/10 (↑ from 7)**

Symantec/Broadcom published a detailed technical analysis confirming that the North Korean Lazarus Group is actively collaborating with Medusa ransomware operators, particularly targeting US healthcare organizations. This represents a significant escalation from the initial reporting.

- **Source:** security.com (Symantec/Broadcom)

---

## Noted

| CVE | Product | Note |
|-----|---------|------|
| CVE-2022-20775 | Cisco SD-WAN | Legacy path traversal added to CISA KEV alongside CVE-2026-20127 |
| CVE-2026-2441 | Chromium | RCE exploited in the wild per Linux Patch Wednesday analysis |
| CVE-2026-21509 | Microsoft Office | RCE trending in Positive Technologies February digest |
| — | AI Training Data | Schneier highlighted trivial poisoning of AI training data via personal websites |

---

*Generated: 2026-02-26T11:06 EET | Cycle: night | Sources checked: 85/90*
