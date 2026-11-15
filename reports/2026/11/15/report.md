# Watchtower Night Report — 2026-11-15
**Cycle:** Night | **Generated:** 2026-11-15 03:13 UTC
**Sources checked:** 21/21 | **KEV additions (30 days):** 15

---

## 🔴 CRITICAL

### 🔄 PHP 'PHP2Shell' RCE
**Product:** PHP | **CVE:** CVE-2026-109618, CVE-2026-109619 | **CVSS:** 9.2 | **Threat score:** 10/10 (was 10) | **Popularity:** 6.3/10 (2/7 newsrooms, 2/5 trending lists)

**Since 2026-10-30:** new newsroom reports

The flaws involve OOM corruption and stale global state that can be leveraged to execute arbitrary code. These vulnerabilities are actively exploited in the wild and listed in CISA KEV. Patches have been released to address these memory handling issues.

**Why it matters:** Administrators of PHP-based web applications are exposed; an attacker can gain full remote control over the server.

**Signals:** CISA KEV since 2026-10-26 · EPSS 1.00 · SSVC exploitation: active · public PoC · trending: Vulmon trends, ZoomEye · registries: OpenCVE latest

**Mitigation:**
- Update PHP to the latest patched version
- Implement a Web Application Firewall (WAF) to detect common RCE patterns

**Covered by:** The Hacker News — 2026-11-13 Hackers Exploit PHP2Shell Flaws in Check Point Gateways to Deploy TSGA Backdoor and Wipe ESXi Files | BleepingComputer — 2026-11-13 Check Point gateways hacked via PHP2Shell to deploy VMware ESXi wiper

---

### 📰 UnrealIRCd Command Injection
**Product:** UnrealIRCd | **CVE:** CVE-2026-114713 | **CVSS:** 8.6 | **Threat score:** 10/10 | **Popularity:** 6.3/10 (1/7 newsrooms, 3/5 trending lists)

The vulnerability exists in the labeled-response module of UnrealIRCd versions before 6.2.7.1. It is currently being actively exploited in the wild and is listed in CISA KEV. A patch has been released to address the escaping issue.

**Why it matters:** Administrators of IRC networks with multiple linked servers are exposed. An attacker can execute commands with full server authority, potentially compromising the entire network.

**Signals:** CISA KEV since 2026-11-13 · EPSS 0.01 · SSVC exploitation: active · trending: CVE Crowd, Intruder cvemon, Vulmon trends · registries: CISA KEV 2026-11-13

**Mitigation:**
- Update UnrealIRCd to version 6.2.7.1 or later
- Audit server-to-server communication logs for unusual command patterns

**Covered by:** The Hacker News — 2026-11-14 Attackers Exploit UnrealIRCd Flaw That Enables Server-Level Command Injection

---

### 📰 Check Point Quantum 'PHP2Shell' LPE
**Product:** Check Point Quantum Security Gateway / Management | **CVE:** CVE-2026-123039 | **CVSS:** 7.8 | **Threat score:** 9/10 | **Popularity:** 7.6/10 (3/7 newsrooms, 3/5 trending lists)

The Gaia OS DynamicCLI daemon listens on a world-writable local socket without authentication. This flaw is being used in active campaigns to deploy the TSGA backdoor and wipe ESXi files. It is listed in CISA KEV as of November 13.

**Why it matters:** Attackers who have gained initial access to the gateway can escalate to root and move laterally into the virtualized infrastructure.

**Signals:** CISA KEV since 2026-11-13 · EPSS 0.02 · SSVC exploitation: active · trending: CVE Crowd, Intruder cvemon, Vulmon trends · registries: CISA KEV 2026-11-13

**Mitigation:**
- Apply the vendor security update immediately
- Monitor for unauthorized access to /tmp/dynamic_socket

**Covered by:** The Hacker News — 2026-11-13 Hackers Exploit PHP2Shell Flaws in Check Point Gateways to Deploy TSGA Backdoor and Wipe ESXi Files | BleepingComputer — 2026-11-13 Check Point gateways hacked via PHP2Shell to deploy VMware ESXi wiper | SecurityWeek — 2026-11-13 PHP2Shell Exploited in Destructive Check Point Gateway Attacks

---

### 🔄 N-able N-central '4EverAble2Shell' Account Takeover
**Product:** N-able N-central | **CVE:** CVE-2026-18556, CVE-2026-18577 | **CVSS:** 8.2 | **Threat score:** 9/10 (was 9) | **Popularity:** 5.4/10 (3/7 newsrooms, 0/5 trending lists)

**Since 2026-11-11:** new newsroom reports

The flaws involve an alternate authentication path and a subsequent incomplete patch. Both are actively exploited in the wild and listed in CISA KEV. Recent reports indicate exploitation occurring immediately following PoC publication.

**Why it matters:** Organizations using N-central for remote management are at high risk. An attacker gains full administrative control over the management console, enabling wide-scale deployment of malware to managed endpoints.

**Signals:** CISA KEV since 2026-08-04 · EPSS 0.44 · SSVC exploitation: active

**Mitigation:**
- Update N-central to the latest patched version (beyond 2026.3.1)
- Review administrative account logs for unauthorized access
- Implement multi-factor authentication where available

**Covered by:** SecurityWeek — 2026-11-13 Hackers Exploit New N-central Zero-Day Hours After PoC Publication

---

### 🔄 Barracuda ESG/ADC Root Access Chain
**Product:** Barracuda Email Security Gateway / Load Balancer ADC | **CVE:** CVE-2026-116606, CVE-2026-111560 | **CVSS:** 9.3 | **Threat score:** 9/10 (was 9) | **Popularity:** 5.4/10 (3/7 newsrooms, 0/5 trending lists)

**Since 2026-11-05:** new newsroom reports

The chain involves an authentication bypass in the configuration-import function and a command injection via the timezone field. Both vulnerabilities are actively exploited in the wild. CISA has added both to the KEV catalog.

**Why it matters:** Attackers can achieve full system compromise (root) on critical perimeter security appliances.

**Signals:** CISA KEV since 2026-11-10 · EPSS 0.11 · SSVC exploitation: active · registries: CISA KEV 2026-11-10

**Mitigation:**
- Update Barracuda ESG to version 9.4.0.030 or later
- Apply latest firmware updates for Barracuda ADC

**Covered by:** SecurityWeek — 2026-11-11 Recently Patched Barracuda Vulnerabilities Exploited in Attacks

---

### 🔄 SonicWall SonicOS SSL-VPN MFA Bypass
**Product:** SonicWall SonicOS | **CVE:** CVE-2026-19868 | **CVSS:** 7.5 | **Threat score:** 9/10 (was 9) | **Popularity:** 5.4/10 (3/7 newsrooms, 0/5 trending lists)

**Since 2026-11-07:** new newsroom reports

The vulnerability allows users with valid credentials for an alternate method to bypass SAML controls. This effectively neutralizes MFA protections for the SSL-VPN service. Active exploitation has been reported and it is listed in CISA KEV.

**Why it matters:** Attackers with stolen passwords can bypass MFA to gain unauthorized access to corporate networks via VPN.

**Signals:** CISA KEV since 2026-11-06 · EPSS 0.01 · SSVC exploitation: active · registries: CISA KEV 2026-11-06

**Mitigation:**
- Apply the latest SonicOS security patches
- Monitor VPN logs for unusual authentication patterns

**Covered by:** The Hacker News — 2026-11-09 CISA Flags SonicWall SonicOS MFA Bypass Flaw Amid Reports of Possible Exploitation | SecurityWeek — 2026-11-07 SonicWall Patches Exploited SonicOS Vulnerability That Weakens VPN Logins

---

## 🟠 HIGH

### 🔄 Apache HTTP Server mod_http2 RCE
**Product:** Apache HTTP Server | **CVE:** CVE-2026-119618 | **CVSS:** 8.1 | **Threat score:** 8/10 (was 8) | **Popularity:** 7.0/10 (3/7 newsrooms, 2/5 trending lists)

**Since 2026-11-13:** CVSS assigned: 8.1

The issue stems from improper synchronization in the assign_headers() function. A CVSS score of 8.1 has been assigned following reports from Anthropic and Google. Patches are available for versions 2.4.55 through 2.4.70.

**Why it matters:** Unauthenticated remote attackers can potentially execute arbitrary code on the web server.

**Signals:** EPSS 0.01 · SSVC exploitation: none · trending: Vulmon trends, securityvulnerability.io trending · registries: OpenCVE latest, oss-security mailing list

**Mitigation:**
- Update Apache HTTP Server to version 2.4.71 or later
- Disable mod_http2 if not strictly required

**Covered by:** The Hacker News — 2026-11-12 Critical Apache HTTP/2 Flaw Could Let Unauthenticated Attackers Execute Code Remotely | BleepingComputer — 2026-11-12 Apache HTTP Server patches critical HTTP/2 remote code execution flaw | SecurityWeek — 2026-11-12 Apache Patches Critical HTTP Server RCE Found by Anthropic, Google

---

### 🔄 Plex Media Server 'Plex2Shell' URL Injection
**Product:** Plex Media Server | **CVE:** CVE-2026-96654 | **CVSS:** 6.5 | **Threat score:** 8/10 (was 8) | **Popularity:** 5.4/10 (2/7 newsrooms, 1/5 trending lists)

**Since 2026-11-10:** EPSS 0.019 -> 0.127

The flaw exists in versions before 1.43.3.10861 due to improper neutralization of 'searchOne' values. It is actively exploited, specifically targeting users running Plex on QNAP NAS devices. The EPSS score has recently increased significantly.

**Why it matters:** Users exposing Plex servers to the internet, particularly on NAS hardware, are vulnerable. Attackers can leverage this to execute unauthorized functions and potentially pivot into the host system.

**Signals:** CISA KEV since 2026-10-20 · EPSS 0.13 · SSVC exploitation: active · trending: ZoomEye

**Mitigation:**
- Update Plex Media Server to version 1.43.3.10861 or later
- Restrict Plex server access to trusted networks via firewall

**Covered by:** BleepingComputer — 2026-11-06 QNAP says hackers breaching NAS devices in Plex2Shell attacks | SecurityWeek — 2026-11-09 Plex2Shell Exploited Against QNAP NAS Users

---

### 📰 Red Hat Quay Registry Signing-Key Takeover
**Product:** Red Hat Quay | **CVE:** CVE-2026-123710 | **CVSS:** 9.8 | **Threat score:** 8/10 | **Popularity:** 5.4/10 (2/7 newsrooms, 1/5 trending lists)

A flaw in the service key rotation endpoint allows unauthenticated clients to install their own signing keys. This enables the attacker to sign registry tokens that are accepted for any repository. The vulnerability allows both reading and overwriting private images.

**Why it matters:** Organizations using Red Hat Quay for private image storage are exposed to complete registry compromise and supply chain attacks via image replacement.

**Signals:** EPSS 0.01 · SSVC exploitation: none · trending: CVE Crowd

**Mitigation:**
- Update Red Hat Quay to the latest patched version
- Audit registry signing keys for unauthorized entries

**Covered by:** The Hacker News — 2026-11-12 Critical Red Hat Quay Flaw Lets Attackers Read and Overwrite All Private Container Images in a Registry | SecurityWeek — 2026-11-12 Critical Red Hat Quay Vulnerability Could Expose Private Container Images

---

## 🟡 MEDIUM

### 📰 PostgreSQL Type Confusion RCE
**Product:** PostgreSQL | **CVE:** CVE-2026-6460 | **CVSS:** 8.8 | **Threat score:** 6/10 | **Popularity:** 6.3/10 (1/7 newsrooms, 3/5 trending lists)

The flaw stems from inadequate tracking of typed values in the data dictionary and PL/pgSQL variables. An attacker can trigger this via ALTER ... SET DATA TYPE or specific DDL sequences. Patches have been released as part of a larger security update.

**Why it matters:** Database users with permissions to create or alter objects can escalate privileges to the operating system user running the database. This allows for full host compromise from within the DB.

**Signals:** EPSS 0.01 · SSVC exploitation: none · trending: Intruder cvemon, Vulmon trends, securityvulnerability.io trending

**Mitigation:**
- Apply the latest PostgreSQL security patches
- Restrict DDL permissions (ALTER/CREATE) to trusted administrators

**Covered by:** The Hacker News — 2026-11-13 PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE

---

### 📰 Next.js Middleware Authorization Bypass
**Product:** vercel next.js | **CVE:** CVE-2025-29927 | **CVSS:** 9.1 | **Threat score:** 6/10 | **Popularity:** 5.4/10 (0/7 newsrooms, 3/5 trending lists)

The vulnerability exists in versions 1.11.4 through 15.2.3 when authorization is handled in the middleware layer. Attackers can bypass these checks to access protected resources. Patches have been released for all affected major versions.

**Why it matters:** Developers relying on Next.js middleware for access control may inadvertently expose private data or administrative functions to unauthenticated users.

**Signals:** EPSS 0.99 · SSVC exploitation: none · trending: CVE Crowd, Intruder cvemon, Vulmon trends

**Mitigation:**
- Update Next.js to versions 12.3.5, 13.5.9, 14.2.25, or 15.2.3
- Block external requests containing the x-middleware-subrequest header

---

### 🔄 Citrix NetScaler Memory Overflow
**Product:** Citrix NetScaler ADC / Gateway | **CVE:** CVE-2026-120868 | **CVSS:** 9.3 | **Threat score:** 6/10 (was 6) | **Popularity:** 5.4/10 (2/7 newsrooms, 1/5 trending lists)

**Since 2026-11-13:** new newsroom reports

The flaw occurs during the processing of network packets. While it can lead to a crash (DoS), the potential for unpredictable behavior suggests further risk. Citrix has released patches as part of a larger security update.

**Why it matters:** Attackers can disrupt network availability or potentially trigger unstable system states on critical gateway infrastructure.

**Signals:** EPSS 0.00 · trending: Vulmon trends

**Mitigation:**
- Update NetScaler ADC and Gateway to the latest patched versions

**Covered by:** SecurityWeek — 2026-11-13 Citrix Patches 10 Critical NetScaler Vulnerabilities

---

## 📋 Noted

- **CVE-2026-104935** (Ivanti Connect Secure): Authentication bypass allowing remote command execution.
- **CVE-2023-2868** (Barracuda Email Security Gateway): Remote command injection via unsanitized .tar files.
- **CVE-2026-2441** (Google Chrome): Use-after-free in CSS allowing sandboxed code execution.
- **CVE-2026-9198** (IBM Langflow OSS): Unauthenticated RCE via auto-login bypass and code validation.
- **CVE-2025-43529** (Apple Safari/iOS/iPadOS): Use-after-free in web content processing leading to code execution.
- **CVE-2026-96656** (Plex Media Server): Arbitrary file write allowing execution of .so files.
- **CVE-2026-46300** (Linux Kernel): Memory corruption in skbuff coalescing leading to root escalation.
- **CVE-2026-5281** (Google Chrome): Use-after-free in Dawn allowing sandboxed code execution.
- **CVE-2026-96652** (Plex Media Server): SSRF via the /player/timeline endpoint.
- **CVE-2026-96655** (Plex Media Server): Authenticated SSRF via the transcode universal path.
- **CVE-2026-87491** (Google Chrome): Out-of-bounds write in V8 allowing sandboxed code execution.
- **CVE-2026-3910** (Google Chrome): V8 implementation flaw allowing sandboxed code execution.
- **CVE-2026-11645** (Google Chrome): Out-of-bounds read/write in V8 allowing sandboxed code execution.
- **CVE-2026-3909** (Google Chrome): Out-of-bounds write in Skia allowing memory access.
- **CVE-2026-85046** (Google Chrome): Type confusion in V8 allowing sandboxed code execution.
- **CVE-2026-111793** (Openwave Webtop Media Transcoder): Bypass of file type restrictions for document conversion.
- **CVE-2016-6210** (OpenSSH): Timing difference in sshd allowing remote user enumeration.
- **CVE-2026-23918** (Apache HTTP Server): Double free in HTTP/2 protocol potentially leading to RCE.
- **CVE-2026-58115** (Siemens SIMATIC IoT2050): Missing authentication on Node-RED interface allowing RCE.
- **CVE-2026-110193** (IBM Langflow OSS): Authenticated RCE via Agentic Assistant code generation.
- **CVE-2026-104339** (IBM Langflow OSS): Remote code execution due to improper OS command neutralization.
- **CVE-2026-113961** (Apple HomeView/iOS/iPadOS): Authorization issue allowing unauthorized joining of iMessage groups.
- **CVE-2026-116331** (PostgreSQL): Type confusion in aggregate optimization allowing arbitrary code execution.
- **CVE-2024-36350** (AMD EPYC Processors): Transient execution vulnerability allowing privileged data leakage.
- **CVE-2024-36357** (AMD EPYC Processors): Transient execution vulnerability allowing L1D cache data leakage.
- **CVE-2026-113960** (Apple HomeView/iOS/iPadOS): Privacy flaw allowing access to iMessage history before joining a group.
- **CVE-2026-118331** (Google Chrome): Use-after-free in FileAPI allowing code execution outside the sandbox.
- **CVE-2026-118344** (Google Chrome): Use-after-free in Layout allowing sandboxed code execution.
- **CVE-2026-118348** (Google Chrome): Integer overflow in Skia allowing code execution outside the sandbox.
- **CVE-2026-107412** (Citrix NetScaler ADC/Gateway): Memory overflow vulnerabilities leading to Denial of Service.

## Index

Every CVE of today's findings; later digests check it so they do not repeat themselves.

| CVE | Finding | Score | First seen |
|---|---|---|---|
| CVE-2026-109618 | PHP 'PHP2Shell' RCE | 10 | 2026-10-30 |
| CVE-2026-109619 | PHP 'PHP2Shell' RCE | 10 | 2026-10-30 |
| CVE-2026-114713 | UnrealIRCd Command Injection | 10 | 2026-11-15 |
| CVE-2026-123039 | Check Point Quantum 'PHP2Shell' LPE | 9 | 2026-11-15 |
| CVE-2026-18556 | N-able N-central '4EverAble2Shell' Account Takeover | 9 | 2026-11-11 |
| CVE-2026-18577 | N-able N-central '4EverAble2Shell' Account Takeover | 9 | 2026-11-11 |
| CVE-2026-116606 | Barracuda ESG/ADC Root Access Chain | 9 | 2026-11-05 |
| CVE-2026-111560 | Barracuda ESG/ADC Root Access Chain | 9 | 2026-11-05 |
| CVE-2026-19868 | SonicWall SonicOS SSL-VPN MFA Bypass | 9 | 2026-11-07 |
| CVE-2026-119618 | Apache HTTP Server mod_http2 RCE | 8 | 2026-11-13 |
| CVE-2026-96654 | Plex Media Server 'Plex2Shell' URL Injection | 8 | 2026-11-10 |
| CVE-2026-123710 | Red Hat Quay Registry Signing-Key Takeover | 8 | 2026-11-15 |
| CVE-2026-6460 | PostgreSQL Type Confusion RCE | 6 | 2026-11-15 |
| CVE-2025-29927 | Next.js Middleware Authorization Bypass | 6 | 2026-11-15 |
| CVE-2026-120868 | Citrix NetScaler Memory Overflow | 6 | 2026-11-13 |

## Source Coverage

| Source | Type | Status | Items |
|---|---|---|---|
| The Hacker News | news | ✅ | 123 |
| BleepingComputer | news | ✅ | 115 |
| SecurityWeek | news | ✅ | 107 |
| Krebs on Security | news | ✅ | 4 |
| Schneier on Security | news | ✅ | 7 |
| Rapid7 blog | news | ✅ | 9 |
| Cloudflare security blog | news | ✅ | 5 |
| CVE Crowd | buzz | ✅ | 17 |
| CVE Crowd | buzz | ✅ | 17 |
| ZoomEye | buzz | ✅ | 5 |
| securityvulnerability.io trending | buzz | ✅ | 18 |
| Intruder cvemon | buzz | ✅ | 10 |
| Vulmon trends | buzz | ✅ | 26 |
| FediSecFeeds | signal | ✅ | 49 |
| 0xMarcio trending public PoCs | signal | ✅ | 44 |
| CISA KEV | feed | ✅ | 15 |
| CERT/CC vulnerability notes | feed | ✅ | 8 |
| GitHub Security Lab advisories | feed | ✅ | 0 |
| Full Disclosure mailing list | feed | ✅ | 15 |
| oss-security mailing list | feed | ✅ | 120 |
| OpenCVE latest | feed | ✅ | 20 |
