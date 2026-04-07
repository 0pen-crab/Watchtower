# Watchtower Report — 2026-03-10 (Night)

---

## 📰 Microsoft March 2026 Patch Tuesday — 2 Public Zero-Days, 8 Critical Flaws

**Threat Score:** 8/10
**CVE:** CVE-2026-26127, CVE-2026-21262
**CVSS:** 8.8

Microsoft patched 84 vulnerabilities: 8 Critical, 76 Important. Two publicly disclosed zero-days: CVE-2026-26127 (.NET DoS, CVSS 7.5) and CVE-2026-21262 (SQL Server EoP, CVSS 8.8). 46 privilege escalation flaws, 18 RCE, 10 info disclosure. Highest CVSS is a critical RCE in Microsoft Devices.

**Sources:** bleepingcomputer.com, thehackernews.com

---

## 📰 KadNap Botnet Infects 14,000+ Edge Devices via Kademlia DHT Protocol

**Threat Score:** 8/10

Black Lotus Labs (Lumen) discovered KadNap, a botnet primarily targeting ASUS routers using a custom Kademlia DHT protocol to conceal C2 infrastructure within a peer-to-peer system. 14,000+ infected devices, 60% in the US. Compromised devices serve as proxies for malicious traffic, resilient to traditional network monitoring and takedown.

**Sources:** thehackernews.com, bleepingcomputer.com

---

## 📰 APT28 Deploys BEARDSHELL and COVENANT for Long-Term Ukraine Military Surveillance

**Threat Score:** 8/10

ESET disclosed that APT28 (Fancy Bear / GRU Unit 26165) has been using BEARDSHELL and a customized variant of the open-source Covenant C2 framework, along with SLIMAGENT (keylogger/screenshot/clipboard stealer), for long-term espionage against Ukrainian military personnel since April 2024.

**Sources:** thehackernews.com, bleepingcomputer.com

---

## 📰 FortiGate NGFW Devices Exploited to Steal Service Account Credentials

**Threat Score:** 8/10

SentinelOne reported a campaign exploiting FortiGate Next-Gen Firewalls to extract configuration files containing AD/LDAP service account credentials and network topology. Targets include healthcare, government, and MSP environments. Attackers leverage recently disclosed vulnerabilities or weak credentials.

**Sources:** thehackernews.com

---

## 📰 CISA Flags Ivanti EPM Flaw as Actively Exploited

**Threat Score:** 7/10

CISA added a recently patched high-severity Ivanti Endpoint Manager vulnerability to KEV, confirming active exploitation. Federal agencies ordered to patch within three weeks.

**Sources:** bleepingcomputer.com

---

## 📰 HPE Aruba AOS-CX Critical Flaw Allows Unauthenticated Admin Password Reset

**Threat Score:** 7/10

HPE patched multiple vulnerabilities in Aruba Networking AOS-CX including critical authentication bypass and code execution flaws that allow unauthenticated admin password resets on affected switches.

**Sources:** bleepingcomputer.com

---

## 📰 BlackSanta EDR Killer Targets HR Departments

**Threat Score:** 7/10

A Russian-speaking threat actor has been targeting HR departments for over a year with malware delivering BlackSanta, a new EDR killer designed to disable endpoint security products before deploying final payloads.

**Sources:** bleepingcomputer.com

---

## 📰 A0Backdoor Deployed via Microsoft Teams Phishing

**Threat Score:** 7/10

Attackers contact employees at financial and healthcare organizations via Microsoft Teams, trick them into granting Quick Assist remote access, then deploy the new A0Backdoor malware. Combines social engineering with living-off-the-land tools.

**Sources:** bleepingcomputer.com

---

## 📰 Russian Signal/WhatsApp Account Hijacking Campaign

**Threat Score:** 7/10

Dutch government warned of Russian state-sponsored phishing campaign targeting government officials, military personnel, and journalists to hijack Signal and WhatsApp accounts. Aims to access sensitive communications.

**Sources:** bleepingcomputer.com

---

## 📋 Noted

- Zombie ZIP evasion technique helps conceal payloads in compressed files to bypass AV/EDR.
- Ericsson US disclosed breach of 15,000+ employee/customer records after service provider compromise.

---

## 📡 Source Coverage: 35/35 checked, 4 with findings
