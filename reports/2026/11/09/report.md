# Watchtower Night Report — 2026-11-09
**Cycle:** Night | **Generated:** 2026-11-09 03:04 UTC
**Sources checked:** 21/21 | **KEV additions (30 days):** 11

---

## 🔴 CRITICAL

### 🔄 WordPress Core RCE (CVE-2026-119977)
**Product:** WordPress Core | **CVE:** CVE-2026-119977 | **CVSS:** 8.1 | **Threat score:** 10/10 (was 10) | **Popularity:** 7.0/10 (2/7 newsrooms, 3/5 trending lists)

**Since 2026-11-05:** public PoC appeared

The vulnerability exists in versions 4.7 through 7.1.3 during the upgrade window. A public PoC has now appeared, confirming the ease of exploitation. CISA has added this to KEV as it is being actively exploited in the wild.

**Why it matters:** Administrators of outdated WordPress sites are exposed to total server takeover by unauthenticated remote attackers.

**Signals:** CISA KEV since 2026-11-03 · EPSS 0.01 · SSVC exploitation: active · public PoC · trending: Intruder cvemon, Vulmon trends, securityvulnerability.io trending · registries: CISA KEV 2026-11-03

**Mitigation:**
- Update WordPress Core to version 7.1.4 or later
- Monitor server logs for unusual activity in staging paths during updates

**Covered by:** The Hacker News — 2026-11-06 Installing the Fix for an Exploited WordPress Flaw Can Expose Some Sites One Last Time | BleepingComputer — 2026-11-04 CISA flags WordPress RCE flaw as actively exploited in attacks

---

## 📋 Noted

- **CVE-2026-9198** (IBM Langflow OSS): Unauthenticated RCE via auto-login bypass and code validation.
- **CVE-2025-43529** (Apple Safari/iOS/iPadOS): Use-after-free in web content processing leading to arbitrary code execution.
- **CVE-2026-46300** (Linux Kernel): Kernel vulnerability in skbuff coalescing allowing root escalation.
- **CVE-2026-63030** (WordPress): REST API route confusion and SQL injection leading to RCE.
- **CVE-2026-96654** (Plex Media Server): URL injection allowing attackers to call other plugin functions.
- **CVE-2016-6210** (OpenSSH): Timing difference in password hashing allowing remote user enumeration.
- **CVE-2026-110264** (GitLab): Integer overflow in regular expression compilation leading to unauthenticated RCE.
- **CVE-2026-110193** (IBM Langflow OSS): Authenticated RCE via Agentic Assistant component code generation.
- **CVE-2026-104339** (IBM Langflow OSS): Remote code execution due to improper neutralization of OS commands.
- **CVE-2026-109469** (Microsoft Entra Device Registration): Authorization bypass allowing network-based privilege elevation.
- **CVE-2026-118331** (Google Chrome): Use-after-free in FileAPI allowing RCE outside the sandbox.
- **CVE-2026-118344** (Google Chrome): Use-after-free in Layout allowing RCE inside the sandbox.
- **CVE-2026-118348** (Google Chrome): Integer overflow in Skia allowing RCE outside the sandbox.
- **CVE-2026-110192** (IBM Langflow OSS): Insufficiently protected credentials allowing authenticated information disclosure.
- **CVE-2026-102703** (Xen Hypervisor): Arbitrary read/write via grant copy allowing VM-to-VM memory access.
- **CVE-2026-15266** (IBM Concert): Unsafe command execution allowing arbitrary system commands on the host.
- **CVE-2021-33044** (Dahua IP Cameras/Devices): Identity authentication bypass via malicious data packets.
- **CVE-2021-33045** (Dahua IP Cameras/Devices): Identity authentication bypass via malicious data packets.
- **CVE-2025-54236** (Adobe Commerce): Improper input validation leading to session takeover.
- **CVE-2025-8088** (WinRAR): Path traversal vulnerability allowing arbitrary code execution via malicious archives.
- **CVE-2026-102764** (BeyondTrust Remote Support): Improper origin validation allowing unauthenticated file upload and RCE.
- **CVE-2025-14174** (Google Chrome): Out of bounds memory access in ANGLE on macOS.
- **CVE-2026-102489** (Zammad): Session hijack vulnerability leading to remote code execution.
- **CVE-2026-48356** (Adobe Commerce): Unrestricted upload of dangerous file types leading to RCE.
- **CVE-2021-38003** (Google Chrome): Heap corruption in V8 engine via crafted HTML pages.
- **CVE-2026-86950** (Apple iOS/iPadOS/macOS): Out-of-bounds write in CoreGraphics leading to arbitrary code execution.
- **CVE-2026-96652** (Plex Media Server): SSRF via the /player/timeline endpoint.
- **CVE-2026-102490** (Zammad): Local privilege escalation to root via insecure service process ownership.
- **CVE-2026-96655** (Plex Media Server): Authenticated SSRF via the transcode universal path parameter.
- **CVE-2026-68820** (Microsoft Windows 10): Use-after-free in WinSock driver allowing local privilege elevation.

## Index

Every CVE of today's findings; later digests check it so they do not repeat themselves.

| CVE | Finding | Score | First seen |
|---|---|---|---|
| CVE-2026-119977 | WordPress Core RCE (CVE-2026-119977) | 10 | 2026-11-05 |

## Source Coverage

| Source | Type | Status | Items |
|---|---|---|---|
| The Hacker News | news | ✅ | 114 |
| BleepingComputer | news | ✅ | 77 |
| SecurityWeek | news | ✅ | 101 |
| Krebs on Security | news | ✅ | 2 |
| Schneier on Security | news | ✅ | 6 |
| Rapid7 blog | news | ✅ | 9 |
| Cloudflare security blog | news | ✅ | 7 |
| CVE Crowd | buzz | ✅ | 16 |
| CVE Crowd | buzz | ✅ | 16 |
| ZoomEye | buzz | ✅ | 5 |
| securityvulnerability.io trending | buzz | ✅ | 18 |
| Intruder cvemon | buzz | ✅ | 11 |
| Vulmon trends | buzz | ✅ | 26 |
| FediSecFeeds | signal | ✅ | 45 |
| 0xMarcio trending public PoCs | signal | ✅ | 43 |
| CISA KEV | feed | ✅ | 11 |
| CERT/CC vulnerability notes | feed | ✅ | 4 |
| GitHub Security Lab advisories | feed | ✅ | 0 |
| Full Disclosure mailing list | feed | ✅ | 15 |
| oss-security mailing list | feed | ✅ | 116 |
| OpenCVE latest | feed | ✅ | 20 |
