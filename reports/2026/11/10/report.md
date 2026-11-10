# Watchtower Night Report — 2026-11-10
**Cycle:** Night | **Generated:** 2026-11-10 03:08 UTC
**Sources checked:** 21/21 | **KEV additions (30 days):** 13

---

## 🔴 CRITICAL

### 📰 SignalWire FreeSWITCH RCE (CVE-2026-116779)
**Product:** SignalWire FreeSWITCH | **CVE:** CVE-2026-116779 | **CVSS:** 9.8 | **Threat score:** 10/10 | **Popularity:** 5.4/10 (0/7 newsrooms, 3/5 trending lists)

The flaw exists in the sofia_presence_handle_sip_i_message function, which incorrectly parses the 'To' user field. By selecting the api chat protocol, an attacker can reach switch_api_execute(). It is currently being actively exploited and was added to CISA KEV on 2026-11-09.

**Why it matters:** Administrators of telecom stacks using FreeSWITCH are exposed to full system compromise via unauthenticated remote command execution.

**Signals:** CISA KEV since 2026-11-09 · EPSS 0.01 · SSVC exploitation: active · trending: CVE Crowd, Intruder cvemon, Vulmon trends · registries: CISA KEV 2026-11-09

**Mitigation:**
- Update FreeSWITCH to version 1.11.3 or later
- Restrict SIP MESSAGE traffic to trusted peers

---

### 🔄 OpenSSH 'SSHole' Auth Bypass (CVE-2026-123158)
**Product:** OpenSSH on Linux (musl libc) | **CVE:** CVE-2026-123158 | **CVSS:** 8.1 | **Threat score:** 9/10 (was 8) | **Popularity:** 8.1/10 (3/7 newsrooms, 4/5 trending lists)

**Since 2026-11-07:** added to CISA KEV 2026-11-09; SSVC exploitation poc -> active

The vulnerability allows any password between 256 and 1024 characters to succeed under specific configurations. It has been upgraded from PoC to active exploitation and was added to CISA KEV on 2026-11-09. A patch is available in version 10.6p2.

**Why it matters:** Users of Alpine Linux and other musl-based distributions without PAM are vulnerable to complete unauthorized remote access.

**Signals:** CISA KEV since 2026-11-09 · EPSS 0.01 · SSVC exploitation: active · public PoC · trending: CVE Crowd, Intruder cvemon, Vulmon trends, securityvulnerability.io trending · registries: CISA KEV 2026-11-09, OpenCVE latest

**Mitigation:**
- Update OpenSSH to 10.6p2 or later
- Enable PAM if supported by the distribution

**Covered by:** BleepingComputer — 2026-11-09 Hackers exploit SSHole OpenSSH flaw to breach Linux systems | SecurityWeek — 2026-11-09 Hackers Exploiting ‘SSHole’ Authentication Bypass in OpenSSH

---

## 🟠 HIGH

### 📰 Plex Media Server 'Plex2Shell' (CVE-2026-96654)
**Product:** Plex Media Server | **CVE:** CVE-2026-96654 | **CVSS:** 6.5 | **Threat score:** 8/10 | **Popularity:** 5.4/10 (2/7 newsrooms, 1/5 trending lists)

The 'searchOne' parameter is not correctly neutralized, enabling the injection of malicious URLs. It is being actively exploited in the wild, specifically targeting QNAP NAS devices. Fixed in version 1.43.3.10861.

**Why it matters:** Plex users, particularly those hosting on NAS devices, risk remote exploitation and potential lateral movement within their home networks.

**Signals:** CISA KEV since 2026-10-20 · EPSS 0.02 · SSVC exploitation: active · trending: ZoomEye

**Mitigation:**
- Update Plex Media Server to 1.43.3.10861 or later
- Restrict external access to the Plex web interface

**Covered by:** BleepingComputer — 2026-11-06 QNAP says hackers breaching NAS devices in Plex2Shell attacks | SecurityWeek — 2026-11-09 Plex2Shell Exploited Against QNAP NAS Users

---

### 🔄 Microsoft Paint RCE (CVE-2026-83844)
**Product:** Microsoft Paint | **CVE:** CVE-2026-83844 | **CVSS:** 7 | **Threat score:** 7/10 (was 5) | **Popularity:** 6.3/10 (1/7 newsrooms, 3/5 trending lists)

**Since 2026-11-07:** public PoC appeared

A public PoC has now appeared for this vulnerability. While a fix exists, reports indicate it may not be delivered automatically via standard Windows Updates.

**Why it matters:** Users opening malicious image files in Paint could have their systems compromised.

**Signals:** EPSS 0.00 · SSVC exploitation: none · public PoC · trending: CVE Crowd, Vulmon trends, securityvulnerability.io trending

**Mitigation:**
- Manually check for and install the latest Windows cumulative updates
- Avoid opening untrusted image files

**Covered by:** The Hacker News — 2026-11-06 Microsoft Paint RCE Fix Now Available, but Windows Update Won't Deliver It

---

## 📋 Noted

- **CVE-2026-9198** (IBM Langflow OSS): Unauthenticated RCE via auto-login bypass and code validation.
- **CVE-2025-43529** (Apple Safari/iOS/iPadOS): Use-after-free in web content processing leading to arbitrary code execution.
- **CVE-2026-46300** (Linux Kernel): Memory corruption in skbuff coalescing allowing potential root escalation.
- **CVE-2026-96652** (Plex Media Server): SSRF via the /player/timeline endpoint.
- **CVE-2026-96655** (Plex Media Server): Authenticated SSRF via the transcode universal path parameter.
- **CVE-2026-63030** (WordPress): REST API route confusion and SQL injection leading to RCE.
- **CVE-2026-96656** (Plex Media Server): Arbitrary file write by admin users leading to code execution.
- **CVE-2026-123218** (IBM Aspera Faspex): Authorization bypass allowing users to gain administrative privileges.
- **CVE-2026-102895** (GPUStack): Authentication bypass via trusted loopback source granting admin access.
- **CVE-2016-6210** (OpenSSH): Timing difference in password hashing allowing remote user enumeration.
- **CVE-2026-110264** (GitLab): Integer overflow in regular expression compilation leading to unauthenticated RCE.
- **CVE-2026-110193** (IBM Langflow OSS): Authenticated RCE via Agentic Assistant component code generation.
- **CVE-2026-104339** (IBM Langflow OSS): Remote code execution due to improper neutralization of OS commands.
- **CVE-2026-114432** (Contact Form 7): Unauthenticated arbitrary file upload leading to RCE on specific configurations.
- **CVE-2026-118331** (Google Chrome): Use-after-free in FileAPI allowing RCE outside the sandbox.
- **CVE-2026-118344** (Google Chrome): Use-after-free in Layout allowing RCE inside the sandbox.
- **CVE-2026-118348** (Google Chrome): Integer overflow in Skia allowing RCE outside the sandbox.
- **CVE-2026-110963** (Userplace): Unauthenticated privilege escalation via AJAX action and nonce exposure.
- **CVE-2026-110192** (IBM Langflow OSS): Information disclosure of sensitive credentials to authenticated attackers.
- **CVE-2021-33044** (Dahua Devices): Identity authentication bypass during the login process.
- **CVE-2021-33045** (Dahua Devices): Identity authentication bypass via malicious data packets during login.
- **CVE-2025-31324** (SAP NetWeaver): Unauthenticated upload of malicious binaries via Visual Composer Metadata Uploader.
- **CVE-2025-8088** (WinRAR): Path traversal in archive processing leading to arbitrary code execution.
- **CVE-2026-102764** (BeyondTrust Remote Support): Improper origin validation allowing unauthenticated file operations.
- **CVE-2025-14174** (Google Chrome): Out of bounds memory access in ANGLE on macOS.
- **CVE-2026-102489** (Zammad): Session hijack vulnerability leading to remote code execution.
- **CVE-2026-48356** (Adobe Commerce): Unrestricted upload of dangerous file types leading to RCE.
- **CVE-2021-38003** (Google Chrome): Heap corruption in V8 engine via crafted HTML pages.
- **CVE-2026-86950** (Apple iOS/macOS): Out-of-bounds write in CoreGraphics leading to arbitrary code execution.
- **CVE-2026-18577** (N-able N-central): Authentication bypass and account takeover due to an incomplete patch.

## Index

Every CVE of today's findings; later digests check it so they do not repeat themselves.

| CVE | Finding | Score | First seen |
|---|---|---|---|
| CVE-2026-116779 | SignalWire FreeSWITCH RCE (CVE-2026-116779) | 10 | 2026-11-10 |
| CVE-2026-123158 | OpenSSH 'SSHole' Auth Bypass (CVE-2026-123158) | 9 | 2026-11-07 |
| CVE-2026-96654 | Plex Media Server 'Plex2Shell' (CVE-2026-96654) | 8 | 2026-11-10 |
| CVE-2026-83844 | Microsoft Paint RCE (CVE-2026-83844) | 7 | 2026-11-07 |

## Source Coverage

| Source | Type | Status | Items |
|---|---|---|---|
| The Hacker News | news | ✅ | 124 |
| BleepingComputer | news | ✅ | 89 |
| SecurityWeek | news | ✅ | 99 |
| Krebs on Security | news | ✅ | 2 |
| Schneier on Security | news | ✅ | 5 |
| Rapid7 blog | news | ✅ | 8 |
| Cloudflare security blog | news | ✅ | 6 |
| CVE Crowd | buzz | ✅ | 25 |
| CVE Crowd | buzz | ✅ | 25 |
| ZoomEye | buzz | ✅ | 5 |
| securityvulnerability.io trending | buzz | ✅ | 18 |
| Intruder cvemon | buzz | ✅ | 11 |
| Vulmon trends | buzz | ✅ | 26 |
| FediSecFeeds | signal | ✅ | 10 |
| 0xMarcio trending public PoCs | signal | ✅ | 43 |
| CISA KEV | feed | ✅ | 13 |
| CERT/CC vulnerability notes | feed | ✅ | 4 |
| GitHub Security Lab advisories | feed | ✅ | 0 |
| Full Disclosure mailing list | feed | ✅ | 15 |
| oss-security mailing list | feed | ✅ | 108 |
| OpenCVE latest | feed | ✅ | 20 |
