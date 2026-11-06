# Watchtower Night Report — 2026-11-06
**Cycle:** Night | **Generated:** 2026-11-06 03:11 UTC
**Sources checked:** 21/21 | **KEV additions (30 days):** 12

---

## 🔴 CRITICAL

### 📰 Apple Safari/iOS Pointer Authentication Bypass
**Product:** Apple Safari, iOS, iPadOS | **CVE:** CVE-2024-27834 | **CVSS:** 5.5 | **Threat score:** 10/10 | **Popularity:** 7.0/10 (2/7 newsrooms, 3/5 trending lists)

The flaw was recently added to CISA's KEV list following reports of active exploitation by Russia-linked hackers. It is used as part of exploit chains delivered via watering hole attacks to deploy info-stealing malware. Apple has released patches for Safari 17.5 and corresponding iOS/iPadOS versions.

**Why it matters:** Users of older iOS and macOS versions are exposed to targeted malware infections that can steal sensitive data.

**Signals:** CISA KEV since 2026-11-04 · EPSS 0.01 · SSVC exploitation: active · trending: CVE Crowd, Intruder cvemon, Vulmon trends · registries: CISA KEV 2026-11-04

**Mitigation:**
- Update iOS, iPadOS, and macOS to the latest available versions
- Keep Safari updated to version 17.5 or newer

**Covered by:** The Hacker News — 2026-11-05 Hackers Exploit Patched Apple Flaw to Deliver Info-Stealing Malware, CISA Says | SecurityWeek — 2026-11-05 Russia-Linked Hackers Hit iOS, Android Devices With Exploit Chains via Watering Holes

---

### 🔄 GitLab RCE (CVE-2026-97229)
**Product:** GitLab CE/EE | **CVE:** CVE-2026-97229 | **CVSS:** 10 | **Threat score:** 10/10 (was 10) | **Popularity:** 5.4/10 (3/7 newsrooms, 0/5 trending lists)

**Since 2026-10-30:** nuclei template appeared

This critical flaw affects multiple versions of GitLab CE/EE (19.2 through 19.4). It is actively exploited in the wild and listed in CISA KEV. A nuclei template is now available for detection.

**Why it matters:** Unauthenticated attackers can gain full control over the GitLab server, compromising source code and CI/CD pipelines.

**Signals:** CISA KEV since 2026-10-29 · EPSS 0.65 · SSVC exploitation: active · nuclei template · registries: CISA KEV 2026-10-29

**Mitigation:**
- Update to versions 19.2.8, 19.3.5, or 19.4.2
- Use the available nuclei template to scan for vulnerability

**Covered by:** The Hacker News — 2026-10-30 CISA Adds Actively Exploited GitLab RCE and Cisco Firewall DoS Flaws to KEV | BleepingComputer — 2026-11-02 Over 1,000 GitLab servers vulnerable to ongoing RCE attacks | SecurityWeek — 2026-10-30 Max-Severity GitLab Vulnerability Exploited Against Alpine Linux

---

### 📰 Zyxel GS1900 Stack Buffer Overflow
**Product:** Zyxel GS1900 Series Switches | **CVE:** CVE-2026-7273 | **CVSS:** 8.8 | **Threat score:** 9/10 | **Popularity:** 6.3/10 (2/7 newsrooms, 2/5 trending lists)

The vulnerability is actively exploited in the wild and was recently added to CISA KEV. It allows remote root command execution via crafted HTTP requests. Zyxel has released patches to address the flaw.

**Why it matters:** Network administrators using GS1900 switches are exposed to full device compromise by attackers on the local network.

**Signals:** CISA KEV since 2026-09-21 · EPSS 0.03 · SSVC exploitation: active · trending: CVE Crowd, Vulmon trends

**Mitigation:**
- Update firmware to the latest version
- Restrict management interface access to trusted IPs

**Covered by:** The Hacker News — 2026-11-05 Zyxel GS1900 Patch Fails to Block Zero-Day Exploit Allowing Root Command Execution | BleepingComputer — 2026-11-04 Zyxel fixes zero-day exploited to hack nearly 1,000 network switches

---

### 🔄 Android GhostMap Vulnerabilities
**Product:** Google Android | **CVE:** CVE-2026-58876, CVE-2026-58868, CVE-2026-58882, CVE-2026-58936 | **CVSS:** 9.8 | **Threat score:** 9/10 (was 8) | **Popularity:** 6.3/10 (3/7 newsrooms, 1/5 trending lists)

**Since 2026-11-05:** CVSS assigned: 9.8; public PoC appeared

The GhostMap set includes use-after-free and heap buffer overflow vulnerabilities (CVE-2026-58876, CVE-2026-58868, CVE-2026-58936) and an integer overflow leading to DoS (CVE-2026-58882). A public PoC has emerged for the heap buffer overflow, and reports indicate Russia-linked hackers are using exploit chains via watering holes. Some flaws can trigger persistent boot loops.

**Why it matters:** Android users are exposed to zero-click remote code execution or device bricking, granting attackers full system control.

**Signals:** EPSS 0.00 · SSVC exploitation: none · trending: Vulmon trends

**Mitigation:**
- Apply the latest Android security updates
- Avoid visiting untrusted websites to mitigate watering hole attacks
- Monitor for unusual device behavior or boot loops

**Covered by:** BleepingComputer — 2026-11-05 GhostMap Android flaw lets malicious app trigger persistent boot loop | SecurityWeek — 2026-11-05 Russia-Linked Hackers Hit iOS, Android Devices With Exploit Chains via Watering Holes

---

## 🟠 HIGH

### 🔄 Linux Kernel TCP Use-After-Free
**Product:** Linux Kernel TCP Stack | **CVE:** CVE-2026-98432 | **CVSS:** 9.8 | **Threat score:** 7/10 (was 7) | **Popularity:** 7.0/10 (2/7 newsrooms, 3/5 trending lists)

**Since 2026-10-30:** new newsroom reports

The flaw involves a use-after-free condition during SYN request processing. Recent reports indicate this specific vulnerability was among those successfully targeted by AI-generated exploit pipelines to achieve root access.

**Why it matters:** Remote or local attackers may be able to crash the system or execute arbitrary code with kernel privileges.

**Signals:** EPSS 0.01 · trending: CVE Crowd, Vulmon trends, securityvulnerability.io trending · registries: oss-security mailing list

**Mitigation:**
- Update Linux kernels to the latest stable release
- Implement network-level filtering to reduce exposure of TCP stacks

**Covered by:** The Hacker News — 2026-11-05 OpenAI AI Pipeline Generates 948 Linux Root Escalation Exploits in 30-Hour Run | SecurityWeek — 2026-11-05 AI Agents Got Root on Linux via 948 Kernel Flaws in OpenAI Research

---

### 🔄 Zyxel GS1900 Out-of-Bounds Write
**Product:** Zyxel GS1900 Series Switches | **CVE:** CVE-2026-107441 | **CVSS:** 8.8 | **Threat score:** 7/10 (was 7) | **Popularity:** 7.0/10 (3/7 newsrooms, 2/5 trending lists)

**Since 2026-11-05:** new newsroom reports

Recent reports indicate that previous patches failed to block a zero-day exploit targeting this flaw. Attackers can achieve root command execution via crafted HTTP requests. Updated firmware is required to fully mitigate the risk.

**Why it matters:** Users who believed they were patched may still be vulnerable to root-level compromise.

**Signals:** EPSS 0.00 · SSVC exploitation: none · trending: CVE Crowd, Vulmon trends

**Mitigation:**
- Apply the latest firmware updates immediately
- Disable unused management services

**Covered by:** The Hacker News — 2026-11-05 Zyxel GS1900 Patch Fails to Block Zero-Day Exploit Allowing Root Command Execution | SecurityWeek — 2026-11-05 Zyxel Switch Hacks Blamed on Patched Flaw Actually Exploited a Zero-Day

---

### 📰 Linux Kernel Root Escalation Flaws (OpenAI Research)
**Product:** Linux Kernel | **CVE:** CVE-2026-43499, CVE-2026-74580, CVE-2026-98260, CVE-2026-31695 | **CVSS:** 8.8 | **Threat score:** 7/10 | **Popularity:** 6.3/10 (2/7 newsrooms, 2/5 trending lists)

These flaws span various kernel components including rtmutex, vhost, POSIX timers, and virt_wifi. Some of these vulnerabilities have public PoCs or are categorized as having total technical impact. They were highlighted in recent reports regarding OpenAI's ability to generate large volumes of root escalation exploits.

**Why it matters:** Local attackers or compromised processes could leverage these flaws to gain full root privileges on the host system.

**Signals:** EPSS 0.01 · SSVC exploitation: poc · public PoC · trending: Vulmon trends, securityvulnerability.io trending

**Mitigation:**
- Update Linux kernels to the latest stable release
- Apply vendor-specific security patches for kernel components

**Covered by:** The Hacker News — 2026-11-05 OpenAI AI Pipeline Generates 948 Linux Root Escalation Exploits in 30-Hour Run | SecurityWeek — 2026-11-05 AI Agents Got Root on Linux via 948 Kernel Flaws in OpenAI Research

---

## 🟡 MEDIUM

### 📰 Debian/Ubuntu APT Hard Link RCE
**Product:** APT (Advanced Package Tool) | **CVE:** CVE-2026-109518 | **CVSS:** 7.7 | **Threat score:** 6/10 | **Popularity:** 6.3/10 (1/7 newsrooms, 3/5 trending lists)

The flaw involves the reuse of hard links during package installation. An attacker capable of manipulating HTTP traffic (e.g., via a malicious mirror or proxy) can swap verified packages for malicious ones. Patches have been released by Debian and Ubuntu.

**Why it matters:** Linux users on these distributions are vulnerable if they use untrusted mirrors or are subject to MitM attacks, leading to full system takeover.

**Signals:** EPSS 0.01 · SSVC exploitation: none · trending: CVE Crowd, Vulmon trends, securityvulnerability.io trending · registries: oss-security mailing list

**Mitigation:**
- Update APT packages via the official security repositories
- Use HTTPS for package mirrors

**Covered by:** The Hacker News — 2026-11-04 Debian and Ubuntu APT Flaw Lets MitM Attackers Swap Verified Packages and Run Code as Root

---

### 📰 SonicWall GMS End-of-Life Vulnerabilities
**Product:** SonicWall Global Management System (GMS) | **CVE:** CVE-2026-109593, CVE-2026-109594 | **CVSS:** 9.1 | **Threat score:** 5/10 | **Popularity:** 6.3/10 (3/7 newsrooms, 1/5 trending lists)

CVE-2026-109593 allows unauthenticated attackers to read internal files, while CVE-2026-109594 allows authenticated users to modify the database. SonicWall has declined to patch these vulnerabilities because the software is end-of-life. Users are urged to migrate to supported platforms.

**Why it matters:** Organizations still running GMS 9.5.2 or earlier face permanent exposure to sensitive data theft and database manipulation.

**Signals:** EPSS 0.01 · SSVC exploitation: none · trending: Vulmon trends

**Mitigation:**
- Migrate from GMS to a supported management platform
- Isolate the GMS server from the general network

**Covered by:** The Hacker News — 2026-11-04 SonicWall Won't Patch EoL GMS Flaws That Could Expose Files, Alter Database Records | BleepingComputer — 2026-11-04 SonicWall warns of unpatched flaws in end-of-life GMS software | SecurityWeek — 2026-11-05 Cisco, WatchGuard Release Patches; SonicWall Won’t Fix GMS Flaws

---

## 📋 Noted

- **CVE-2026-9198** (IBM Langflow OSS): Unauthenticated RCE via auto-login bypass and code validation.
- **CVE-2025-43529** (Apple Safari/iOS/iPadOS): Use-after-free in web content processing leading to arbitrary code execution.
- **CVE-2026-46300** (Linux Kernel): Memory corruption in skbuff coalescing allowing potential root escalation.
- **CVE-2026-63030** (WordPress): REST API route confusion and SQL injection leading to RCE.
- **CVE-2026-93674** (IBM Langflow OSS): Remote code execution due to improper neutralization of OS commands.
- **CVE-2026-7873** (IBM Langflow OSS): Authenticated code injection via the code validation endpoint.
- **CVE-2026-10134** (IBM Langflow OSS): Unauthenticated RCE via PythonCodeStructuredTool in public flows.
- **CVE-2026-110264** (GitLab): Unauthenticated RCE via integer overflow during regular expression compilation.
- **CVE-2026-110193** (IBM Langflow OSS): Authenticated RCE via Agentic Assistant component code generation.
- **CVE-2026-104339** (IBM Langflow OSS): Remote code execution via improper OS command neutralization.
- **CVE-2026-83844** (Microsoft Paint): Out-of-bounds read allowing remote code execution over a network.
- **CVE-2026-118331** (Google Chrome): Use-after-free in FileAPI allowing RCE outside the sandbox.
- **CVE-2026-118344** (Google Chrome): Use-after-free in Layout allowing RCE inside the sandbox.
- **CVE-2026-118348** (Google Chrome): Integer overflow in Skia allowing RCE outside the sandbox.
- **CVE-2026-106378** (Google Chrome): Sandbox privilege escalation on macOS allowing RCE outside the sandbox.
- **CVE-2026-110192** (IBM Langflow OSS): Authenticated information disclosure due to insufficiently protected credentials.
- **CVE-2026-102703** (Xen Hypervisor): Arbitrary read/write across VMs via grant copy validation errors.
- **CVE-2026-123158** (OpenSSH): Password authentication bypass on Linux systems using musl libc without PAM.
- **CVE-2021-33044** (Dahua IP Cameras/Devices): Identity authentication bypass during the login process.
- **CVE-2021-33045** (Dahua IP Cameras/Devices): Identity authentication bypass during the login process.
- **CVE-2025-54236** (Adobe Commerce): Improper input validation leading to session takeover.
- **CVE-2025-8088** (WinRAR): Path traversal allowing arbitrary code execution via malicious archives.
- **CVE-2026-42208** (BerriAI litellm): Unauthenticated SQL injection in Proxy API key verification.
- **CVE-2026-102764** (BeyondTrust Remote Support): Improper origin validation allowing unauthenticated file operations and RCE.
- **CVE-2026-110447** (Collabora Online CODE Server): OS command injection in proxy.php leading to remote code execution.
- **CVE-2025-14174** (Google Chrome): Out-of-bounds memory access in ANGLE on macOS.
- **CVE-2026-48356** (Adobe Commerce): Unrestricted upload of dangerous file types leading to RCE.
- **CVE-2021-38003** (Google Chrome): Heap corruption in V8 allowing remote code execution.
- **CVE-2026-86950** (Apple iOS/iPadOS/macOS): Out-of-bounds write in CoreGraphics leading to arbitrary code execution.
- **CVE-2026-102489** (Zammad): Session hijack vulnerability leading to remote code execution.

## Index

Every CVE of today's findings; later digests check it so they do not repeat themselves.

| CVE | Finding | Score | First seen |
|---|---|---|---|
| CVE-2024-27834 | Apple Safari/iOS Pointer Authentication Bypass | 10 | 2026-11-06 |
| CVE-2026-97229 | GitLab RCE (CVE-2026-97229) | 10 | 2026-10-30 |
| CVE-2026-7273 | Zyxel GS1900 Stack Buffer Overflow | 9 | 2026-11-06 |
| CVE-2026-58876 | Android GhostMap Vulnerabilities | 9 | 2026-11-05 |
| CVE-2026-58868 | Android GhostMap Vulnerabilities | 9 | 2026-11-05 |
| CVE-2026-58882 | Android GhostMap Vulnerabilities | 9 | 2026-11-05 |
| CVE-2026-58936 | Android GhostMap Vulnerabilities | 9 | 2026-11-05 |
| CVE-2026-98432 | Linux Kernel TCP Use-After-Free | 7 | 2026-10-30 |
| CVE-2026-107441 | Zyxel GS1900 Out-of-Bounds Write | 7 | 2026-11-05 |
| CVE-2026-43499 | Linux Kernel Root Escalation Flaws (OpenAI Research) | 7 | 2026-11-06 |
| CVE-2026-74580 | Linux Kernel Root Escalation Flaws (OpenAI Research) | 7 | 2026-11-06 |
| CVE-2026-98260 | Linux Kernel Root Escalation Flaws (OpenAI Research) | 7 | 2026-11-06 |
| CVE-2026-31695 | Linux Kernel Root Escalation Flaws (OpenAI Research) | 7 | 2026-11-06 |
| CVE-2026-109518 | Debian/Ubuntu APT Hard Link RCE | 6 | 2026-11-06 |
| CVE-2026-109593 | SonicWall GMS End-of-Life Vulnerabilities | 5 | 2026-11-06 |
| CVE-2026-109594 | SonicWall GMS End-of-Life Vulnerabilities | 5 | 2026-11-06 |

## Source Coverage

| Source | Type | Status | Items |
|---|---|---|---|
| The Hacker News | news | ✅ | 115 |
| BleepingComputer | news | ✅ | 64 |
| SecurityWeek | news | ✅ | 99 |
| Krebs on Security | news | ✅ | 3 |
| Schneier on Security | news | ✅ | 5 |
| Rapid7 blog | news | ✅ | 9 |
| Cloudflare security blog | news | ✅ | 7 |
| CVE Crowd | buzz | ✅ | 23 |
| CVE Crowd | buzz | ✅ | 23 |
| ZoomEye | buzz | ✅ | 5 |
| securityvulnerability.io trending | buzz | ✅ | 18 |
| Intruder cvemon | buzz | ✅ | 9 |
| Vulmon trends | buzz | ✅ | 26 |
| FediSecFeeds | signal | ✅ | 142 |
| 0xMarcio trending public PoCs | signal | ✅ | 44 |
| CISA KEV | feed | ✅ | 12 |
| CERT/CC vulnerability notes | feed | ✅ | 4 |
| GitHub Security Lab advisories | feed | ✅ | 0 |
| Full Disclosure mailing list | feed | ✅ | 15 |
| oss-security mailing list | feed | ✅ | 127 |
| OpenCVE latest | feed | ✅ | 21 |
