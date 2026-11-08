# Watchtower Night Report — 2026-11-08
**Cycle:** Night | **Generated:** 2026-11-08 03:05 UTC
**Sources checked:** 21/21 | **KEV additions (30 days):** 13

---

## 🟠 HIGH

### 🔄 Android 'GhostMap' Denial of Service
**Product:** Google Android | **CVE:** CVE-2026-58882 | **CVSS:** 7.5 | **Threat score:** 7/10 (was 9) | **Popularity:** 5.4/10 (3/7 newsrooms, 0/5 trending lists)

**Since 2026-11-05:** CVSS assigned: 7.5

The vulnerability is triggered via WapPushOverSms.java without requiring user interaction. A CVSS score of 7.5 has been assigned since the last report. It can result in persistent boot loops or system crashes.

**Why it matters:** Android users are exposed to 'SMS of Death' attacks that can remotely crash devices. This allows attackers to disable mobile endpoints without any user action.

**Signals:** EPSS 0.00 · SSVC exploitation: none

**Mitigation:**
- Install the November 2026 Android security update
- Restrict untrusted SMS sources where possible

**Covered by:** The Hacker News — 2026-11-04 Google Issues Patches for Critical Android Flaw That Could Allow RCE Without User Interaction | BleepingComputer — 2026-11-05 GhostMap Android flaw lets malicious app trigger persistent boot loop | SecurityWeek — 2026-11-05 Russia-Linked Hackers Hit iOS, Android Devices With Exploit Chains via Watering Holes

---

## 📋 Noted

- **CVE-2026-9198** (IBM Langflow OSS): Unauthenticated RCE via auto-login bypass and code validation.
- **CVE-2025-43529** (Apple Safari/iOS/iPadOS): Use-after-free in web content processing leading to arbitrary code execution.
- **CVE-2026-46300** (Linux Kernel): Kernel vulnerability in skbuff coalescing allowing root escalation.
- **CVE-2026-63030** (WordPress): REST API route confusion and SQL injection leading to RCE.
- **CVE-2026-96654** (Plex Media Server): URL injection allowing attackers to call other plugin functions.
- **CVE-2026-110264** (GitLab): Integer overflow in regular expression compilation leading to unauthenticated RCE.
- **CVE-2026-99999** (Linux Kernel): IPv4 checksum validation flaw that can corrupt network headers.
- **CVE-2026-110193** (IBM Langflow OSS): Authenticated RCE via Agentic Assistant component code generation.
- **CVE-2026-104339** (IBM Langflow OSS): RCE due to improper neutralization of OS command elements.
- **CVE-2026-109469** (Microsoft Entra Device Registration): Authorization bypass allowing network-based privilege elevation.
- **CVE-2026-118331** (Google Chrome): Use-after-free in FileAPI allowing RCE outside the sandbox.
- **CVE-2026-118344** (Google Chrome): Use-after-free in Layout allowing RCE inside the sandbox.
- **CVE-2026-118348** (Google Chrome): Integer overflow in Skia allowing RCE outside the sandbox.
- **CVE-2026-110192** (IBM Langflow OSS): Insufficiently protected credentials allowing sensitive information disclosure.
- **CVE-2021-33044** (Dahua IP Cameras/Devices): Identity authentication bypass during the login process.
- **CVE-2021-33045** (Dahua IP Cameras/Devices): Identity authentication bypass during the login process.
- **CVE-2025-54236** (Adobe Commerce): Improper input validation leading to session takeover.
- **CVE-2025-8088** (WinRAR): Path traversal vulnerability allowing arbitrary code execution via malicious archives.
- **CVE-2026-102764** (BeyondTrust Remote Support): Improper origin validation allowing unauthenticated file upload and RCE.
- **CVE-2021-30860** (Apple iOS/macOS): Integer overflow in PDF processing leading to arbitrary code execution.
- **CVE-2026-110447** (Collabora Online CODE Server): OS command injection in proxy.php leading to RCE.
- **CVE-2025-14174** (Google Chrome): Out of bounds memory access in ANGLE on macOS.
- **CVE-2026-102489** (Zammad): Session hijack vulnerability leading to RCE as the zammad user.
- **CVE-2026-48356** (Adobe Commerce): Unrestricted upload of dangerous file types leading to RCE.
- **CVE-2021-38003** (Google Chrome): Heap corruption in V8 engine via crafted HTML pages.
- **CVE-2026-86950** (Apple iOS/iPadOS/macOS): Out-of-bounds write in CoreGraphics leading to arbitrary code execution.
- **CVE-2026-96652** (Plex Media Server): SSRF via the /player/timeline endpoint.
- **CVE-2026-102490** (Zammad): Local privilege escalation to root via insecure service process execution.
- **CVE-2026-96655** (Plex Media Server): Authenticated SSRF via the transcode universal path parameter.
- **CVE-2026-68820** (Microsoft Windows 10): Use-after-free in WinSock driver allowing local privilege elevation.

## Index

Every CVE of today's findings; later digests check it so they do not repeat themselves.

| CVE | Finding | Score | First seen |
|---|---|---|---|
| CVE-2026-58882 | Android 'GhostMap' Denial of Service | 7 | 2026-11-05 |

## Source Coverage

| Source | Type | Status | Items |
|---|---|---|---|
| The Hacker News | news | ✅ | 121 |
| BleepingComputer | news | ✅ | 76 |
| SecurityWeek | news | ✅ | 101 |
| Krebs on Security | news | ✅ | 2 |
| Schneier on Security | news | ✅ | 7 |
| Rapid7 blog | news | ✅ | 9 |
| Cloudflare security blog | news | ✅ | 8 |
| CVE Crowd | buzz | ✅ | 20 |
| CVE Crowd | buzz | ✅ | 20 |
| ZoomEye | buzz | ✅ | 5 |
| securityvulnerability.io trending | buzz | ✅ | 18 |
| Intruder cvemon | buzz | ✅ | 11 |
| Vulmon trends | buzz | ✅ | 26 |
| FediSecFeeds | signal | ✅ | 46 |
| 0xMarcio trending public PoCs | signal | ✅ | 43 |
| CISA KEV | feed | ✅ | 13 |
| CERT/CC vulnerability notes | feed | ✅ | 4 |
| GitHub Security Lab advisories | feed | ✅ | 0 |
| Full Disclosure mailing list | feed | ✅ | 15 |
| oss-security mailing list | feed | ✅ | 122 |
| OpenCVE latest | feed | ✅ | 20 |
