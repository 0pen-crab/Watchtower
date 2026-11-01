# Watchtower Night Report — 2026-10-30
**Cycle:** Night | **Generated:** 2026-10-31 13:29 UTC
**Sources checked:** 21/21 | **KEV additions (30 days):** 18
**Baseline:** first digest of the new pipeline — everything popular in the last 14 days; later digests report only new CVEs and updates.

---

## 🔴 CRITICAL

### 📰 PHP 'PHP2Shell' RCE
**Product:** PHP | **CVE:** CVE-2026-109618, CVE-2026-109619 | **CVSS:** 9.2 | **Threat score:** 10/10 | **Popularity:** 9.7/10 (6/7 newsrooms, 5/5 trending lists)

The flaws involve OOM corruption using longjmp() and improper resets of global state pointing to request memory. Both are actively exploited in the wild, including attacks against network appliances. Emergency patches have been released to address these issues.

**Why it matters:** Almost any server running PHP is potentially exposed, granting attackers full system compromise.

**Signals:** CISA KEV since 2026-10-26 · EPSS 1.00 · SSVC exploitation: active · public PoC · nuclei template · trending: CVE Crowd, Intruder cvemon, Vulmon trends, ZoomEye, securityvulnerability.io trending · registries: CERT/CC vulnerability notes 2026-10-22, CISA KEV 2026-10-26, Full Disclosure mailing list 2026-10-29, oss-security mailing list

**Mitigation:**
- Update PHP to the latest patched version immediately
- Monitor for unusual child process spawning from web servers
- Implement strict memory limits in php.ini

**Covered by:** The Hacker News — 2027-12-31 PHP2Shell: Two Unpatched Critical PHP RCE Flaws (CVSS 9.2) Trigger Emergency Security Alert | SecurityWeek — 2026-10-30 PHP2Shell Attacks Root Palo Alto Firewalls but Fail Against WordPress | Krebs on Security — 2026-10-23 Widespread PHP Flaw May Cause Many Site Outages Today | Schneier on Security — 2026-10-20 New Serious PHP Vulnerabilities Released and Patched | Rapid7 blog — 2026-10-21 CVE-2026-109618 and CVE-2026-109619: Critical Unauthenticated Remote Code Execution in PHP | Cloudflare security blog — 2026-10-27 Introducing the Cloudflare PHP Capture the Flag challenge

---

### 📰 Cisco Catalyst SD-WAN Manager Authentication Bypass
**Product:** Cisco Catalyst SD-WAN | **CVE:** CVE-2026-20127 | **CVSS:** 10 | **Threat score:** 10/10 | **Popularity:** 6.3/10 (3/7 newsrooms, 1/5 trending lists)

The flaw exists in the peering authentication mechanism of vSmart, vManage, and vBond controllers. It is actively exploited in the wild by actors linked to Volt Typhoon's 'Silent Train' network. Attackers have used this access to deploy custom KeyDrift malware designed to steal encryption keys.

**Why it matters:** Organizations using Cisco SD-WAN are exposed to total system takeover and theft of sensitive cryptographic material.

**Signals:** CISA KEV since 2026-02-25 · EPSS 0.89 · SSVC exploitation: active · trending: Vulmon trends

**Mitigation:**
- Apply the official Cisco security patches immediately
- Audit SD-WAN controller logs for unauthorized administrative access
- Rotate encryption keys if compromise is suspected

**Covered by:** The Hacker News — 2026-10-29 Hackers Exploited Cisco SD-WAN Flaw to Plant Malware Built to Steal Encryption Keys | BleepingComputer — 2026-10-29 Hackers exploit Cisco SD-WAN flaw to deploy custom KeyDrift malware | SecurityWeek — 2026-10-29 Cisco SD-WAN Zero-Day Exploitation Tied to Volt Typhoon’s ‘Silent Train’ Network

---

### 📰 Google Brotli 'Node2Shell' OOB Write
**Product:** Google Brotli Decoder | **CVE:** CVE-2026-111497 | **CVSS:** 9.2 | **Threat score:** 9/10 | **Popularity:** 7.6/10 (3/7 newsrooms, 3/5 trending lists)

The flaw exists in versions 1.0.3 through 1.2.0 across all platforms. It is actively exploited and affects numerous downstream implementations including Node.js, Python packages, and Microsoft products. Patches are available in versions 1.0.10 and 1.1.1.

**Why it matters:** Widespread use of Brotli for compression means many web servers and applications are vulnerable to remote takeover.

**Signals:** CISA KEV since 2026-10-27 · EPSS 0.83 · SSVC exploitation: active · public PoC · nuclei template · trending: CVE Crowd, Vulmon trends, securityvulnerability.io trending · registries: CISA KEV 2026-10-27, oss-security mailing list

**Mitigation:**
- Update Brotli libraries to version 1.0.10 or 1.1.1
- Update Node.js and Python environments using Brotli
- Filter or sanitize untrusted compressed input

**Covered by:** The Hacker News — 2026-10-28 Adobe Commerce PolyShell Attacks Breach Hundreds of Stores as Brotli Exploit Traffic Emerges | SecurityWeek — 2026-10-28 CISA Warns of Node2Shell Exploitation as Honeypots Log Attack Attempts | Rapid7 blog — 2026-10-26 CVE-2026-111497: Critical out-of-bounds write in the Node.js Brotli decoder

---

### 📰 GitLab RCE (CVE-2026-97229)
**Product:** GitLab CE/EE | **CVE:** CVE-2026-97229 | **CVSS:** 10 | **Threat score:** 9/10 | **Popularity:** 7.0/10 (2/7 newsrooms, 3/5 trending lists)

The vulnerability affects multiple versions of GitLab CE/EE (19.2, 19.3, and 19.4). It is listed in CISA KEV as being actively exploited. Patches have been released for all affected versions.

**Why it matters:** Attackers can gain full control of the GitLab server, potentially accessing all hosted source code and CI/CD secrets.

**Signals:** CISA KEV since 2026-10-29 · EPSS 0.27 · SSVC exploitation: active · trending: CVE Crowd, Intruder cvemon, Vulmon trends · registries: CISA KEV 2026-10-29

**Mitigation:**
- Update GitLab to 19.2.8, 19.3.5, or 19.4.2
- Restrict access to CI/CD configuration interfaces
- Audit CI/CD logs for suspicious regular expression patterns

**Covered by:** The Hacker News — 2026-10-30 CISA Adds Actively Exploited GitLab RCE and Cisco Firewall DoS Flaws to KEV | SecurityWeek — 2026-10-30 Max-Severity GitLab Vulnerability Exploited Against Alpine Linux

---

### 📰 Arista VeloCloud Orchestrator SQL Injection
**Product:** Arista VeloCloud Orchestrator (VCO) | **CVE:** CVE-2026-114625 | **CVSS:** 9.9 | **Threat score:** 9/10 | **Popularity:** 5.4/10 (2/7 newsrooms, 1/5 trending lists)

The vulnerability enables an attacker to access privileged internal functionality and compromise the VCO host. It has been added to CISA KEV as it is actively exploited in attacks. A patch is available from Arista.

**Why it matters:** Administrators of on-prem VeloCloud Orchestrators face potential total compromise of the orchestrator and all managed data.

**Signals:** CISA KEV since 2026-10-23 · EPSS 0.01 · SSVC exploitation: active · trending: securityvulnerability.io trending · registries: CISA KEV 2026-10-23

**Mitigation:**
- Update VCO on-prem to the latest patched version
- Restrict access to the VCO management interface
- Review operator account activity for unauthorized privilege escalation

**Covered by:** The Hacker News — 2026-10-26 CISA Flags Two Actively Exploited Critical Flaws in Collabora Online and Arista VeloCloud | SecurityWeek — 2026-10-23 Attackers Exploit Third Arista VCO Zero-Day in Four Months

---

### 📰 Oracle PeopleSoft Enterprise PeopleTools RCE
**Product:** Oracle PeopleSoft Enterprise PeopleTools | **CVE:** CVE-2026-35273 | **CVSS:** 9.8 | **Threat score:** 9/10 | **Popularity:** 5.4/10 (2/7 newsrooms, 1/5 trending lists)

This vulnerability is easily exploitable over HTTP and has been linked to campaigns by the ShinyHunters group. It is part of a chain of flaws used in recent attacks and is listed in CISA KEV. Oracle has released patches as part of the October CPU.

**Why it matters:** Enterprises running PeopleSoft versions 8.61 and 8.62 are vulnerable to complete server compromise.

**Signals:** CISA KEV since 2026-06-12 · EPSS 0.97 · SSVC exploitation: active · trending: Vulmon trends

**Mitigation:**
- Apply the October 2026 Oracle Critical Patch Update (CPU)
- Implement network-level access controls to restrict HTTP access to PeopleTools

**Covered by:** The Hacker News — 2026-10-28 ShinyHunters-Exploited Oracle PeopleSoft Zero-Day Turns Out to Be Three Chained Flaws | SecurityWeek — 2026-10-22 Oracle Patches Over 1,200 Vulnerabilities With October 2026 CPU

---

## 🟠 HIGH

### 📰 Cisco ASA/FTD VPN DoS
**Product:** Cisco Secure Firewall (ASA/FTD) | **CVE:** CVE-2026-76418 | **CVSS:** 8.6 | **Threat score:** 8/10 | **Popularity:** 7.0/10 (2/7 newsrooms, 3/5 trending lists)

The flaw is triggered when secondary authentication is configured on a tunnel group. It is currently being exploited in the wild to cause unexpected device reloads. Cisco has released software updates to resolve the issue.

**Why it matters:** Attackers can repeatedly crash corporate VPN gateways, causing total loss of remote access for employees.

**Signals:** CISA KEV since 2026-10-29 · EPSS 0.01 · SSVC exploitation: active · trending: CVE Crowd, Intruder cvemon, Vulmon trends · registries: CISA KEV 2026-10-29

**Mitigation:**
- Apply the latest Cisco ASA and FTD software updates
- Review SSL VPN tunnel group authentication configurations
- Monitor for repeated device reloads in system logs

**Covered by:** The Hacker News — 2026-10-29 Cisco Patches Actively Exploited ASA and FTD VPN Flaw That Can Crash Firewalls | SecurityWeek — 2026-10-29 Attackers Exploit Second Cisco Firewall VPN Zero-Day Since August

---

### 📰 Drupal Commerce Core Authorization Bypass
**Product:** Drupal Commerce Core | **CVE:** CVE-2026-118539 | **CVSS:** Not specified | **Threat score:** 8/10 | **Popularity:** 6.3/10 (3/7 newsrooms, 1/5 trending lists)

The flaw affects multiple versions of Commerce Core (up to 2.41 and 3.3.13). It is currently being actively exploited against online stores. Drupal has issued a security advisory (SA-CONTRIB-2026-254) and a patch.

**Why it matters:** Online store owners using Drupal Commerce may have sensitive data exposed or administrative functions accessed by unauthorized users.

**Signals:** EPSS 0.00 · trending: CVE Crowd

**Mitigation:**
- Update Drupal Commerce Core to the latest patched version
- Review web server logs for patterns of forceful browsing/directory traversal

**Covered by:** The Hacker News — 2026-10-30 Hackers Actively Exploit Highly Critical Drupal Commerce Core Authorization Bypass Flaw | BleepingComputer — 2026-10-30 Drupal warns of critical Commerce Core flaw exploited in attacks | SecurityWeek — 2026-10-30 Drupal Commerce Core Vulnerability Exploited Against Online Stores

---

### 📰 Oracle E-Business Suite RCE (CVE-2026-101767)
**Product:** Oracle Application Object Library | **CVE:** CVE-2026-101767 | **CVSS:** 9.8 | **Threat score:** 8/10 | **Popularity:** 5.4/10 (2/7 newsrooms, 1/5 trending lists)

This critical vulnerability exists in versions 12.2.3 through 12.2.15 of the Oracle E-Business Suite Core component. While no public PoC is listed, news reports indicate that attackers have already begun probing for this flaw. Oracle released a patch as part of the October 2026 Critical Patch Update.

**Why it matters:** Organizations running affected Oracle EBS instances are exposed to full system compromise by unauthenticated network attackers.

**Signals:** EPSS 0.01 · SSVC exploitation: none · trending: Vulmon trends

**Mitigation:**
- Apply the October 2026 Oracle CPU
- Restrict HTTP access to E-Business Suite interfaces
- Monitor web logs for unusual probing patterns

**Covered by:** The Hacker News — 2026-10-28 Hackers Target Critical Oracle E-Business Suite RCE Flaw Days After Security Patch | SecurityWeek — 2026-10-28 Hackers Start Probing Fresh Oracle EBS Vulnerability

---

### 📰 Linux Kernel TCP Use-After-Free
**Product:** Linux Kernel (ipv4) | **CVE:** CVE-2026-98432 | **CVSS:** 9.8 | **Threat score:** 7/10 | **Popularity:** 7.0/10 (1/7 newsrooms, 4/5 trending lists)

The issue stems from the transfer of ownership of ireq_opt without proper copying, leading to a race condition. A public PoC exists, and it affects major distributions like Ubuntu and Red Hat. The fix involves freeing options after an RCU grace period.

**Why it matters:** A remote attacker could potentially crash the system or achieve privilege escalation via a specially crafted TCP sequence.

**Signals:** EPSS 0.00 · public PoC · trending: CVE Crowd, Intruder cvemon, Vulmon trends, securityvulnerability.io trending · registries: oss-security mailing list

**Mitigation:**
- Update the Linux kernel to the latest stable version
- Apply distribution-specific security patches for the TCP stack
- Use firewall rules to limit SYN flood exposure

**Covered by:** The Hacker News — 2026-10-29 Linux Kernel TCP Flaw With 9.8 CVSS Score Affects Ubuntu, Red Hat and Other Distributions

---

## 🟡 MEDIUM

### 📰 TianoCore EDK2 Pre-boot RCE
**Product:** TianoCore EDK2 (UEFI) | **CVE:** CVE-2026-97631 | **CVSS:** 9.5 | **Threat score:** 6/10 | **Popularity:** 5.4/10 (1/7 newsrooms, 2/5 trending lists)

The vulnerability involves out-of-bounds writes in the BIOS when handling network booting. It can potentially execute code before Secure Boot is fully established on network-booting servers. No public PoC is currently available.

**Why it matters:** Servers configured for PXE/network booting are vulnerable to low-level persistence and pre-OS compromise.

**Signals:** EPSS 0.01 · trending: Vulmon trends, securityvulnerability.io trending · registries: oss-security mailing list

**Mitigation:**
- Update UEFI/BIOS firmware to the latest vendor-provided version
- Disable PXE booting if not strictly required for operations

**Covered by:** The Hacker News — 2026-10-28 Critical 16-Year-Old UEFI Flaw Can Run Code Before Secure Boot on Network-Booting Servers

---

### 📰 VMware ESX Insufficient Logging
**Product:** VMware ESX / Cloud Foundation | **CVE:** CVE-2026-41709 | **CVSS:** 2.7 | **Threat score:** 5/10 | **Popularity:** 6.3/10 (2/7 newsrooms, 2/5 trending lists)

While the CVSS is low, this vulnerability has been added to CISA KEV because it is used by China-linked actors. It serves as a stealth mechanism to hide other malicious activities within the hypervisor. A patch is available.

**Why it matters:** Organizations with compromised administrative credentials may not detect malicious hypervisor-level changes.

**Signals:** CISA KEV since 2026-10-28 · EPSS 0.01 · SSVC exploitation: active · trending: CVE Crowd, Vulmon trends · registries: CISA KEV 2026-10-28

**Mitigation:**
- Apply VMware ESXi security updates
- Implement strict multi-factor authentication for all ESX administrative accounts

**Covered by:** The Hacker News — 2026-10-29 China-Linked Hackers Exploited VMware ESX Zero-Day to Reduce Audit Trail Visibility | SecurityWeek — 2026-10-29 Chinese Hackers Quietly Used Low-Severity ESXi Logging Flaw as Zero-Day

---

### 📰 TeamViewer Remote Control Buffer Overflow (CVE-2026-111585)
**Product:** TeamViewer Full Client / Portable | **CVE:** CVE-2026-111585 | **CVSS:** 8.8 | **Threat score:** 4/10 | **Popularity:** 5.4/10 (2/7 newsrooms, 1/5 trending lists)

The flaw affects TeamViewer clients prior to version 15.83 during the processing of remote-control screen data. Exploitation is client-side and requires a user to connect to a malicious or compromised host. It can result in a denial of service or arbitrary code execution with the privileges of the viewer process.

**Why it matters:** Support technicians or users connecting to untrusted remote machines could have their own local systems compromised.

**Signals:** EPSS 0.00 · trending: CVE Crowd

**Mitigation:**
- Update TeamViewer clients to version 15.83 or later
- Avoid establishing remote sessions with untrusted or unverified hosts

**Covered by:** The Hacker News — 2026-10-30 TeamViewer Flaw Lets Remote Computers Attack Users Who Connect to Control Them | SecurityWeek — 2026-10-30 TeamViewer Flaw Could Let Malicious Hosts Take Over Support Technicians’ Machines

---

## 📋 Noted

- **CVE-2026-88771** (Citrix NetScaler ADC/Gateway): Unauthenticated remote code execution via improper input validation.
- **CVE-2026-48356** (Adobe Commerce): Arbitrary code execution via unrestricted file upload requiring user interaction.
- **CVE-2026-86950** (Apple iOS/iPadOS/macOS): Arbitrary code execution via an out-of-bounds write issue.
- **CVE-2026-46300** (Linux Kernel): Vulnerability in skbuff coalescing that breaks shared-frag marker invariants.
- **CVE-2026-63030** (WordPress): Remote code execution via REST API route confusion and SQL injection.
- **CVE-2026-96654** (Plex Media Server): URL injection allowing attackers to call other plugin functions.
- **CVE-2026-110936** (Siemens Software Center): Local privilege escalation via DLL hijacking from an uncontrolled search path.
- **CVE-2026-111357** (Ivanti Connect Secure): Privilege escalation to root via mishandled DSCache configuration data.
- **CVE-2026-111862** (Rank Math SEO PRO): Supply-chain compromise delivering a self-restoring backdoor.
- **CVE-2025-65200** (LocalStack): Arbitrary code execution via crafted content in the cloudformation deploy endpoint.
- **CVE-2026-80097** (Microsoft Authenticator (Android)): Local privilege escalation allowing apps to steal work account tokens.
- **CVE-2026-113470** (Mozilla Firefox/Thunderbird): Cryptographic issue in security block-lists and allow-lists.
- **CVE-2026-86990** (Apple iOS/iPadOS/macOS): Unauthorized camera access by malicious applications.
- **CVE-2026-65339** (Apple iOS/iPadOS/macOS): Logic issue allowing applications to leak sensitive user information.
- **CVE-2026-86987** (Apple iOS/iPadOS): Remote access to sensitive user data via authorization bypass.
- **CVE-2021-33044** (Dahua IP Cameras/Devices): Identity authentication bypass during the login process.
- **CVE-2021-33045** (Dahua IP Cameras/Devices): Identity authentication bypass during the login process.
- **CVE-2025-54236** (Adobe Commerce): Improper input validation leading to session takeover.
- **CVE-2026-42208** (LiteLLM): Unauthenticated SQL injection in Proxy API key verification.
- **CVE-2026-88772** (Citrix NetScaler ADC/Gateway): Memory overflow leading to remote code execution or denial of service.
- **CVE-2026-110447** (Collabora Online (CODE Server)): Remote code execution via OS command injection in proxy.php.
- **CVE-2026-102764** (BeyondTrust Remote Support): Unauthenticated file upload to RCE via improper origin validation.
- **CVE-2026-88779** (NetScaler ADC/Gateway): Memory overflow leading to denial of service.
- **CVE-2026-68820** (Microsoft Windows 10): Local privilege escalation via use-after-free in WinSock driver.
- **CVE-2024-39717** (Versa Director): Malicious file upload via the Change Favicon option for admins.
- **CVE-2026-75650** (Adobe Commerce): Arbitrary code execution via template engine injection.
- **CVE-2026-96652** (Plex Media Server): Server-side request forgery via the player timeline endpoint.
- **CVE-2026-96656** (Plex Media Server): Arbitrary file write allowing execution of malicious .so files.
- **CVE-2026-16812** (Arista VeloCloud Orchestrator): Remote OS command injection in on-prem installations.
- **CVE-2026-96655** (Plex Media Server): Authenticated server-side request forgery via transcode path parameters.

## Index

Every CVE of today's findings; later digests check it so they do not repeat themselves.

| CVE | Finding | Score | First seen |
|---|---|---|---|
| CVE-2026-109618 | PHP 'PHP2Shell' RCE | 10 | 2026-10-30 |
| CVE-2026-109619 | PHP 'PHP2Shell' RCE | 10 | 2026-10-30 |
| CVE-2026-20127 | Cisco Catalyst SD-WAN Manager Authentication Bypass | 10 | 2026-10-30 |
| CVE-2026-111497 | Google Brotli 'Node2Shell' OOB Write | 9 | 2026-10-30 |
| CVE-2026-97229 | GitLab RCE (CVE-2026-97229) | 9 | 2026-10-30 |
| CVE-2026-114625 | Arista VeloCloud Orchestrator SQL Injection | 9 | 2026-10-30 |
| CVE-2026-35273 | Oracle PeopleSoft Enterprise PeopleTools RCE | 9 | 2026-10-30 |
| CVE-2026-76418 | Cisco ASA/FTD VPN DoS | 8 | 2026-10-30 |
| CVE-2026-118539 | Drupal Commerce Core Authorization Bypass | 8 | 2026-10-30 |
| CVE-2026-101767 | Oracle E-Business Suite RCE (CVE-2026-101767) | 8 | 2026-10-30 |
| CVE-2026-98432 | Linux Kernel TCP Use-After-Free | 7 | 2026-10-30 |
| CVE-2026-97631 | TianoCore EDK2 Pre-boot RCE | 6 | 2026-10-30 |
| CVE-2026-41709 | VMware ESX Insufficient Logging | 5 | 2026-10-30 |
| CVE-2026-111585 | TeamViewer Remote Control Buffer Overflow (CVE-2026-111585) | 4 | 2026-10-30 |

## Source Coverage

| Source | Type | Status | Items |
|---|---|---|---|
| The Hacker News | news | ✅ | 112 |
| BleepingComputer | news | ✅ | 15 |
| SecurityWeek | news | ✅ | 103 |
| Krebs on Security | news | ✅ | 2 |
| Schneier on Security | news | ✅ | 10 |
| Rapid7 blog | news | ✅ | 11 |
| Cloudflare security blog | news | ✅ | 9 |
| CVE Crowd | buzz | ✅ | 30 |
| CVE Crowd | buzz | ✅ | 30 |
| ZoomEye | buzz | ✅ | 5 |
| securityvulnerability.io trending | buzz | ✅ | 18 |
| Intruder cvemon | buzz | ✅ | 9 |
| Vulmon trends | buzz | ✅ | 26 |
| FediSecFeeds | signal | ✅ | 117 |
| 0xMarcio trending public PoCs | signal | ✅ | 50 |
| CISA KEV | feed | ✅ | 18 |
| CERT/CC vulnerability notes | feed | ✅ | 4 |
| GitHub Security Lab advisories | feed | ✅ | 5 |
| Full Disclosure mailing list | feed | ✅ | 15 |
| oss-security mailing list | feed | ✅ | 130 |
| OpenCVE latest | feed | ✅ | 21 |
