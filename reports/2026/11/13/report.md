# Watchtower Night Report — 2026-11-13
**Cycle:** Night | **Generated:** 2026-11-13 03:15 UTC
**Sources checked:** 21/21 | **KEV additions (30 days):** 13

---

## 🔴 CRITICAL

### 🔄 N-able N-central '4EverAble2Shell' Account Takeover
**Product:** N-able N-central | **CVE:** CVE-2026-18556, CVE-2026-18577 | **CVSS:** 8.2 | **Threat score:** 9/10 (was 9) | **Popularity:** 5.4/10 (3/7 newsrooms, 0/5 trending lists)

**Since 2026-11-11:** EPSS 0.079 -> 0.439

These flaws, including an incomplete patch for the initial vulnerability, enable full administrative access. The EPSS score has surged to 0.439 following reports of active exploitation. N-able has released security hotfixes to address the zero-days.

**Why it matters:** MSP administrators are exposed; an attacker gains total control over the N-central management console and managed endpoints.

**Signals:** CISA KEV since 2026-08-04 · EPSS 0.44 · SSVC exploitation: active

**Mitigation:**
- Apply latest security hotfixes immediately
- Audit administrative account logs for unauthorized access
- Restrict N-central console access to trusted IPs

**Covered by:** BleepingComputer — 2026-11-12 New N-able "4EverAble2Shell" zero-day exploited hours after PoC released | SecurityWeek — 2026-11-12 Hackers Target N-central Zero-Days as N-able Rushes Patches

---

### 📰 ConnectWise ScreenConnect Guest-to-Host Execution
**Product:** ConnectWise ScreenConnect Client | **CVE:** CVE-2026-84869 | **CVSS:** 9.9 | **Threat score:** 9/10 | **Popularity:** 5.4/10 (3/7 newsrooms, 0/5 trending lists)

The vulnerability is being leveraged by 'SCKit' malware to turn support sessions into attack paths. It allows files to be executed on the host without authorization or confirmation. The flaw is currently listed in CISA KEV.

**Why it matters:** Organizations using ScreenConnect for remote support are exposed to worm-like malware that can breach MSPs and their clients.

**Signals:** CISA KEV since 2026-09-11 · EPSS 0.01 · SSVC exploitation: active

**Mitigation:**
- Update ScreenConnect client to the latest patched version
- Monitor for unauthorized file transfers during remote sessions
- Implement strict application whitelisting on endpoints

**Covered by:** The Hacker News — 2026-11-12 SCKit Malware Turns ScreenConnect Support Sessions Into Potential MSP Attack Paths | BleepingComputer — 2026-11-12 New worm-like 'SCKit' malware targets MSPs in ScreenConnect attacks | SecurityWeek — 2026-11-12 Hackers Deploy Malware in Fresh ScreenConnect Campaign

---

## 🟠 HIGH

### 📰 Apache HTTP Server mod_http2 RCE
**Product:** Apache HTTP Server (mod_http2) | **CVE:** CVE-2026-119618 | **CVSS:** Not specified | **Threat score:** 8/10 | **Popularity:** 7.0/10 (3/7 newsrooms, 2/5 trending lists)

The flaw exists in the assign_headers() function due to improper synchronization during concurrent execution. A public PoC is available, and the vulnerability affects versions 2.4.55 through 2.4.70. Patches have been released to address the synchronization issue.

**Why it matters:** Unauthenticated remote attackers can execute arbitrary code on widely deployed web servers.

**Signals:** EPSS 0.00 · public PoC · trending: CVE Crowd, Vulmon trends · registries: oss-security mailing list

**Mitigation:**
- Update Apache HTTP Server to version 2.4.71 or later
- Disable mod_http2 if not required for business operations

**Covered by:** The Hacker News — 2026-11-12 Critical Apache HTTP/2 Flaw Could Let Unauthenticated Attackers Execute Code Remotely | BleepingComputer — 2026-11-12 Apache HTTP Server patches critical HTTP/2 remote code execution flaw | SecurityWeek — 2026-11-12 Apache Patches Critical HTTP Server RCE Found by Anthropic, Google

---

### 📰 Cisco BroadWorks XML External Entity (XXE)
**Product:** Cisco BroadWorks | **CVE:** CVE-2026-20320 | **CVSS:** 7.5 | **Threat score:** 8/10 | **Popularity:** 6.3/10 (3/7 newsrooms, 1/5 trending lists)

The vulnerability is caused by the default resolution of external entities in the OCI XML Parser. It has been added to CISA KEV as it is being actively exploited in the wild. Cisco has provided patches for affected systems.

**Why it matters:** Attackers can steal sensitive system configuration information from telecommunications infrastructure.

**Signals:** CISA KEV since 2026-11-10 · EPSS 0.01 · SSVC exploitation: active · trending: Intruder cvemon · registries: CISA KEV 2026-11-10

**Mitigation:**
- Apply the official Cisco security updates for BroadWorks
- Restrict access to the OCI-P service to trusted networks

**Covered by:** The Hacker News — 2026-11-11 Cisco BroadWorks and Openwave Flaws Actively Exploited Despite Available Patches | BleepingComputer — 2026-11-11 CISA flags Cisco BroadWorks flaw as actively exploited in attacks | SecurityWeek — 2026-11-11 Threat Actors Exploit Openwave, Cisco BroadWorks Vulnerabilities

---

## 🟡 MEDIUM

### 📰 Citrix NetScaler Memory Overflow
**Product:** Citrix NetScaler ADC and Gateway | **CVE:** CVE-2026-120868 | **CVSS:** 9.3 | **Threat score:** 6/10 | **Popularity:** 6.3/10 (2/7 newsrooms, 2/5 trending lists)

The vulnerability resides in the packet processing engine. While it has a critical CVSS score, there is currently no public PoC or confirmed exploitation. Citrix has released patches for this and other related flaws.

**Why it matters:** Organizations using NetScaler for load balancing or gateway services are exposed to potential service outages.

**Signals:** trending: CVE Crowd, Vulmon trends

**Mitigation:**
- Apply the latest Citrix NetScaler security updates
- Monitor system logs for unexpected reboots or crashes
- Implement DDoS protection to mitigate packet-based attacks

**Covered by:** The Hacker News — 2026-11-12 Citrix Patches 12 NetScaler and Secure Access Client Flaws, Including Authentication Bypass | SecurityWeek — 2026-11-11 Citrix, Ivanti Patch Critical and High-Severity Vulnerabilities

---

### 📰 MongoDB Server Pre-Auth Remote Code Execution
**Product:** MongoDB Server | **CVE:** CVE-2026-118383 | **CVSS:** 9 | **Threat score:** 6/10 | **Popularity:** 5.4/10 (1/7 newsrooms, 2/5 trending lists)

The flaw occurs when a newly elected replica set primary completes catch-up. It can be triggered by unauthenticated requests. The vulnerability affects replica set members, including shard and config servers.

**Why it matters:** Administrators of MongoDB clusters are exposed; an unauthenticated remote attacker could crash the database or execute code.

**Signals:** EPSS 0.01 · trending: CVE Crowd, Vulmon trends

**Mitigation:**
- Update MongoDB Server to the latest patched version
- Restrict network access to MongoDB ports using firewalls
- Ensure replica set members are isolated from public internet

**Covered by:** The Hacker News — 2026-11-12 Critical Pre-Auth MongoDB Flaw (CVE-2026-118383) Can Crash Lagging Servers on Failover

---

### 📰 Zoom Workplace Privilege Escalation
**Product:** Zoom Workplace for Windows | **CVE:** CVE-2026-108186, CVE-2026-108187 | **CVSS:** 9.6 | **Threat score:** 6/10 | **Popularity:** 5.4/10 (2/7 newsrooms, 1/5 trending lists)

The flaws stem from improper input validation and origin validation errors. Zoom has released security patches to address these issues. There are currently no public PoCs or reports of active exploitation.

**Why it matters:** Windows users running Zoom Workplace are exposed to remote attackers who could gain elevated system privileges.

**Signals:** EPSS 0.00 · SSVC exploitation: none · trending: Vulmon trends

**Mitigation:**
- Update Zoom Workplace for Windows to the latest version
- Restrict unnecessary network access to Zoom application ports

**Covered by:** The Hacker News — 2026-11-11 Critical Zoom Workplace Flaw Could Allow Unauthenticated Remote Privilege Escalation | SecurityWeek — 2026-11-11 Asus, Zoom Release Security Patches

---

## 📋 Noted

- **CVE-2026-104935** (Ivanti Connect Secure): Authentication bypass allowing remote command execution.
- **CVE-2023-2868** (Barracuda Email Security Gateway): Remote command injection via unsanitized .tar files.
- **CVE-2026-111497** (Google Brotli): Out-of-bounds write in the decoder allowing remote code execution.
- **CVE-2026-2441** (Google Chrome): Use-after-free in CSS allowing sandboxed remote code execution.
- **CVE-2026-9198** (IBM Langflow OSS): Unauthenticated remote code execution via auto-login bypass.
- **CVE-2025-43529** (Apple Safari/iOS/iPadOS): Use-after-free in web content processing leading to code execution.
- **CVE-2026-46300** (Linux Kernel): Memory corruption in skbuff coalescing leading to potential privilege escalation.
- **CVE-2026-5281** (Google Chrome): Use-after-free in Dawn allowing code execution from a compromised renderer.
- **CVE-2026-96652** (Plex Media Server): SSRF via the /player/timeline endpoint.
- **CVE-2026-96655** (Plex Media Server): Authenticated SSRF via the transcode universal path.
- **CVE-2026-63030** (WordPress): REST API route confusion and SQL injection leading to remote code execution.
- **CVE-2026-87491** (Google Chrome): Out-of-bounds write in V8 allowing sandboxed remote code execution.
- **CVE-2026-3910** (Google Chrome): V8 implementation flaw allowing sandboxed remote code execution.
- **CVE-2026-11645** (Google Chrome): Out-of-bounds read/write in V8 allowing sandboxed remote code execution.
- **CVE-2026-3909** (Google Chrome): Out-of-bounds write in Skia allowing remote memory access.
- **CVE-2026-85046** (Google Chrome): Type confusion in V8 allowing sandboxed remote code execution.
- **CVE-2026-96656** (Plex Media Server): Arbitrary file write allowing potential code execution on load.
- **CVE-2026-111793** (Openwave Webtop Media Transcoder): Failure to enforce file type restrictions during conversion.
- **CVE-2016-6210** (OpenSSH): Timing difference in password hashing allowing remote user enumeration.
- **CVE-2026-23918** (Apache HTTP Server): Double free in HTTP/2 protocol leading to possible remote code execution.
- **CVE-2026-126187** (React): Unauthenticated remote code execution in React Server Components.
- **CVE-2026-58115** (Siemens SIMATIC IoT2050): Missing authentication on Node-RED interface allowing remote command execution.
- **CVE-2026-110193** (IBM Langflow OSS): Authenticated remote code execution via Agentic Assistant.
- **CVE-2026-104339** (IBM Langflow OSS): Remote code execution due to improper neutralization of OS commands.
- **CVE-2026-113961** (Apple HomeView/iOS/iPadOS): Authorization issue allowing unauthorized joining of iMessage group chats.
- **CVE-2024-36350** (AMD EPYC Processors): Transient execution vulnerability allowing privileged information leakage.
- **CVE-2026-123710** (Red Hat Quay): Unauthenticated registry signing-key takeover allowing image replacement.
- **CVE-2024-36357** (AMD EPYC Processors): Transient execution vulnerability allowing L1D cache data leakage.
- **CVE-2026-118331** (Google Chrome): Use-after-free in FileAPI allowing remote code execution outside the sandbox.
- **CVE-2026-118344** (Google Chrome): Use-after-free in Layout allowing sandboxed remote code execution.

## Index

Every CVE of today's findings; later digests check it so they do not repeat themselves.

| CVE | Finding | Score | First seen |
|---|---|---|---|
| CVE-2026-18556 | N-able N-central '4EverAble2Shell' Account Takeover | 9 | 2026-11-11 |
| CVE-2026-18577 | N-able N-central '4EverAble2Shell' Account Takeover | 9 | 2026-11-11 |
| CVE-2026-84869 | ConnectWise ScreenConnect Guest-to-Host Execution | 9 | 2026-11-13 |
| CVE-2026-119618 | Apache HTTP Server mod_http2 RCE | 8 | 2026-11-13 |
| CVE-2026-20320 | Cisco BroadWorks XML External Entity (XXE) | 8 | 2026-11-13 |
| CVE-2026-120868 | Citrix NetScaler Memory Overflow | 6 | 2026-11-13 |
| CVE-2026-118383 | MongoDB Server Pre-Auth Remote Code Execution | 6 | 2026-11-13 |
| CVE-2026-108186 | Zoom Workplace Privilege Escalation | 6 | 2026-11-13 |
| CVE-2026-108187 | Zoom Workplace Privilege Escalation | 6 | 2026-11-13 |

## Source Coverage

| Source | Type | Status | Items |
|---|---|---|---|
| The Hacker News | news | ✅ | 127 |
| BleepingComputer | news | ✅ | 118 |
| SecurityWeek | news | ✅ | 104 |
| Krebs on Security | news | ✅ | 4 |
| Schneier on Security | news | ✅ | 5 |
| Rapid7 blog | news | ✅ | 9 |
| Cloudflare security blog | news | ✅ | 4 |
| CVE Crowd | buzz | ✅ | 20 |
| CVE Crowd | buzz | ✅ | 20 |
| ZoomEye | buzz | ✅ | 5 |
| securityvulnerability.io trending | buzz | ✅ | 18 |
| Intruder cvemon | buzz | ✅ | 10 |
| Vulmon trends | buzz | ✅ | 26 |
| FediSecFeeds | signal | ✅ | 16 |
| 0xMarcio trending public PoCs | signal | ✅ | 43 |
| CISA KEV | feed | ✅ | 13 |
| CERT/CC vulnerability notes | feed | ✅ | 8 |
| GitHub Security Lab advisories | feed | ✅ | 0 |
| Full Disclosure mailing list | feed | ✅ | 15 |
| oss-security mailing list | feed | ✅ | 114 |
| OpenCVE latest | feed | ✅ | 20 |
