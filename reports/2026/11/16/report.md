# Watchtower Night Report — 2026-11-16
**Cycle:** Night | **Generated:** 2026-11-16 03:06 UTC
**Sources checked:** 21/21 | **KEV additions (30 days):** 15

---

## 🟠 HIGH

### 🔄 Apache HTTP Server mod_http2 RCE
**Product:** Apache HTTP Server | **CVE:** CVE-2026-119618 | **CVSS:** 8.1 | **Threat score:** 8/10 (was 8) | **Popularity:** 7.6/10 (3/7 newsrooms, 3/5 trending lists)

**Since 2026-11-13:** public PoC appeared

The vulnerability is caused by improper synchronization in assign_headers(), affecting Apache HTTP Server 2.4.55 through 2.4.70 and mod_h2 2.0.8 through 2.0.42. A public PoC has now appeared, increasing the risk of exploitation. Patches are available from the Apache Software Foundation.

**Why it matters:** Unauthenticated remote attackers can execute arbitrary code on servers running the affected mod_http2 module.

**Signals:** EPSS 0.02 · SSVC exploitation: none · public PoC · trending: CVE Crowd, Vulmon trends, securityvulnerability.io trending · registries: oss-security mailing list

**Mitigation:**
- Update Apache HTTP Server to version 2.4.71 or later
- Update mod_h2 to version 2.0.43 or later

**Covered by:** The Hacker News — 2026-11-12 Critical Apache HTTP/2 Flaw Could Let Unauthenticated Attackers Execute Code Remotely | BleepingComputer — 2026-11-12 Apache HTTP Server patches critical HTTP/2 remote code execution flaw | SecurityWeek — 2026-11-12 Apache Patches Critical HTTP Server RCE Found by Anthropic, Google

---

## 📋 Noted

- **CVE-2026-104935** (Ivanti Connect Secure): Authentication bypass allowing remote command execution.
- **CVE-2023-2868** (Barracuda Email Security Gateway): Remote command injection via unsanitized .tar files.
- **CVE-2026-111497** (Google Brotli): Out-of-bounds write in the decoder allowing remote code execution.
- **CVE-2026-2441** (Google Chrome): Use-after-free in CSS allowing remote code execution in a sandbox.
- **CVE-2026-9198** (IBM Langflow OSS): Unauthenticated RCE via auto-login bypass and code validation.
- **CVE-2025-43529** (Apple Safari/iOS/iPadOS): Use-after-free in web content processing allowing arbitrary code execution.
- **CVE-2026-96656** (Plex Media Server): Arbitrary file write allowing execution of files on load.
- **CVE-2026-46300** (Linux Kernel): Memory corruption in skbuff coalescing leading to potential root escalation.
- **CVE-2026-5281** (Google Chrome): Use-after-free in Dawn allowing code execution via compromised renderer.
- **CVE-2026-96652** (Plex Media Server): SSRF via the /player/timeline endpoint.
- **CVE-2026-96655** (Plex Media Server): Vulnerability associated with the Plex2Shell attack chain.
- **CVE-2026-87491** (Google Chrome): Out-of-bounds write in V8 allowing remote code execution in a sandbox.
- **CVE-2026-3910** (Google Chrome): V8 implementation flaw allowing remote code execution in a sandbox.
- **CVE-2026-11645** (Google Chrome): Out-of-bounds read/write in V8 allowing remote code execution in a sandbox.
- **CVE-2026-3909** (Google Chrome): Out-of-bounds write in Skia allowing remote memory access.
- **CVE-2026-85046** (Google Chrome): Type confusion in V8 allowing remote code execution in a sandbox.
- **CVE-2026-111793** (Openwave Webtop Media Transcoder): Failure to enforce file type restrictions for document conversion.
- **CVE-2026-23918** (Apache HTTP Server): Double free in HTTP/2 protocol allowing potential remote code execution.
- **CVE-2026-58115** (Siemens SIMATIC IoT2050): Missing authentication on Node-RED interface allowing remote command execution.
- **CVE-2026-110193** (IBM Langflow OSS): Authenticated RCE via Agentic Assistant code generation.
- **CVE-2026-104339** (IBM Langflow OSS): Remote code execution due to improper neutralization of OS commands.
- **CVE-2026-113961** (Apple HomeView/iOS/iPadOS): Authorization issue allowing unauthorized joining of iMessage group chats.
- **CVE-2024-36350** (AMD EPYC Processors): Transient execution vulnerability allowing leakage of privileged information.
- **CVE-2024-36357** (AMD EPYC Processors): Transient execution vulnerability allowing L1D cache data leakage.
- **CVE-2026-113960** (Apple HomeView/iOS/iPadOS): Privacy flaw allowing access to iMessage history before joining a group.
- **CVE-2026-118331** (Google Chrome): Use-after-free in FileAPI allowing remote code execution outside the sandbox.
- **CVE-2026-118344** (Google Chrome): Use-after-free in Layout allowing remote code execution in a sandbox.
- **CVE-2026-118348** (Google Chrome): Integer overflow in Skia allowing remote code execution outside the sandbox.
- **CVE-2026-110192** (IBM Langflow OSS): Insufficiently protected credentials allowing sensitive information disclosure.
- **CVE-2026-0004** (AMD EPYC Processors): Transient execution vulnerability allowing L1D cache data leakage.

## Index

Every CVE of today's findings; later digests check it so they do not repeat themselves.

| CVE | Finding | Score | First seen |
|---|---|---|---|
| CVE-2026-119618 | Apache HTTP Server mod_http2 RCE | 8 | 2026-11-13 |

## Source Coverage

| Source | Type | Status | Items |
|---|---|---|---|
| The Hacker News | news | ✅ | 121 |
| BleepingComputer | news | ✅ | 114 |
| SecurityWeek | news | ✅ | 108 |
| Krebs on Security | news | ✅ | 3 |
| Schneier on Security | news | ✅ | 7 |
| Rapid7 blog | news | ✅ | 9 |
| Cloudflare security blog | news | ✅ | 5 |
| CVE Crowd | buzz | ✅ | 16 |
| CVE Crowd | buzz | ✅ | 16 |
| ZoomEye | buzz | ✅ | 5 |
| securityvulnerability.io trending | buzz | ✅ | 18 |
| Intruder cvemon | buzz | ✅ | 10 |
| Vulmon trends | buzz | ✅ | 26 |
| FediSecFeeds | signal | ✅ | 58 |
| 0xMarcio trending public PoCs | signal | ✅ | 44 |
| CISA KEV | feed | ✅ | 15 |
| CERT/CC vulnerability notes | feed | ✅ | 8 |
| GitHub Security Lab advisories | feed | ✅ | 0 |
| Full Disclosure mailing list | feed | ✅ | 15 |
| oss-security mailing list | feed | ✅ | 122 |
| OpenCVE latest | feed | ✅ | 20 |
