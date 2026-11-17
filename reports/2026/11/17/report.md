# Watchtower Night Report — 2026-11-17
**Cycle:** Night | **Generated:** 2026-11-17 03:10 UTC
**Sources checked:** 21/21 | **KEV additions (30 days):** 14

---

## 🔴 CRITICAL

### 🔄 UnrealIRCd Command Injection
**Product:** UnrealIRCd | **CVE:** CVE-2026-114713 | **CVSS:** 8.6 | **Threat score:** 10/10 (was 10) | **Popularity:** 7.6/10 (2/7 newsrooms, 4/5 trending lists)

**Since 2026-11-15:** new newsroom reports

The labeled-response module fails to escape tags when echoing replies. This allows an attacker on a network with linked servers to execute commands with server authority. Recent reports confirm this vulnerability is being exploited in active attacks.

**Why it matters:** Administrators of UnrealIRCd servers are exposed; an attacker can gain full control over the server infrastructure.

**Signals:** CISA KEV since 2026-11-13 · EPSS 0.01 · SSVC exploitation: active · trending: CVE Crowd, Intruder cvemon, Vulmon trends, securityvulnerability.io trending · registries: CISA KEV 2026-11-13

**Mitigation:**
- Update UnrealIRCd to version 6.2.7.1 or later
- Review server logs for unauthorized server-to-server commands

**Covered by:** SecurityWeek — 2026-11-16 Recent UnrealIRCd Vulnerability Exploited in Attacks

---

## 🟠 HIGH

### 📰 Apache Axis 1.x Remote Code Execution
**Product:** Apache Axis 1.x | **CVE:** CVE-2026-90436 | **CVSS:** 9.8 | **Threat score:** 8/10 | **Popularity:** 5.4/10 (2/7 newsrooms, 1/5 trending lists)

The deserialization of inbound SOAP faults allows an attacker to load and instantiate arbitrary classes on the classpath. Rapid7 has detected active exploitation of this flaw against Atlassian Confluence Data Center and N-able N-central. The product is end-of-life (EOL).

**Why it matters:** Organizations using legacy Apache Axis 1.x or affected third-party software are exposed to full remote system compromise.

**Signals:** EPSS 0.01 · SSVC exploitation: none · trending: CVE Crowd

**Mitigation:**
- Migrate from Apache Axis 1.x to a supported framework
- Disable SOAP endpoints if not required
- Implement strict WAF rules to block malicious SOAP <Fault> elements

**Covered by:** The Hacker News — 2026-11-13 Hackers Exploit N-central Flaws to Infect 21 Servers, Including 19 Running Hotfix 2 | Rapid7 blog — 2026-11-16 Rapid7 Detected Exploitation of CVE-2026-90436 against Atlassian Confluence Data Center, N-able N-central also Exploited

---

### 🔄 Linux Kernel NoisyTCP Use-After-Free
**Product:** Linux Kernel | **CVE:** CVE-2026-98432 | **CVSS:** 9.8 | **Threat score:** 7/10 (was 7) | **Popularity:** 7.0/10 (3/7 newsrooms, 2/5 trending lists)

**Since 2026-10-30:** new newsroom reports

The NoisyTCP vulnerability involves a use-after-free condition in the IPv4 TCP stack during SYN processing. While previously noted for privilege escalation, new reports indicate it can be used to crash Linux servers remotely. A fix has been merged into the kernel.

**Why it matters:** Administrators of Linux servers are exposed to remote denial-of-service attacks and potential local privilege escalation.

**Signals:** EPSS 0.01 · trending: CVE Crowd, Vulmon trends

**Mitigation:**
- Update the Linux kernel to a patched version
- Restrict unnecessary TCP traffic via firewall rules

**Covered by:** BleepingComputer — 2026-11-16 New NoisyTCP vulnerability lets attackers crash Linux servers

---

## 📋 Noted

- **CVE-2023-2868** (Barracuda Email Security Gateway): Remote command injection via unsanitized .tar files allows root access.
- **CVE-2026-111497** (Google Brotli): An out-of-bounds write in the decoder can lead to remote code execution.
- **CVE-2026-2441** (Google Chrome): A use-after-free vulnerability in CSS allows remote code execution inside a sandbox.
- **CVE-2025-43529** (Apple Safari/iOS/iPadOS): A use-after-free issue in web content processing may lead to arbitrary code execution.
- **CVE-2026-96656** (Plex Media Server): An arbitrary file write vulnerability allows admin users to execute code on load.
- **CVE-2026-46300** (Linux Kernel): A failure to preserve shared-frag markers during coalescing can lead to root escalation.
- **CVE-2026-5281** (Google Chrome): A use-after-free in Dawn allows a compromised renderer process to execute arbitrary code.
- **CVE-2026-96652** (Plex Media Server): A server-side request forgery (SSRF) vulnerability exists via the /player/timeline endpoint.
- **CVE-2026-96655** (Plex Media Server): An authenticated user can trigger SSRF via the transcode universal path parameter.
- **CVE-2026-87491** (Google Chrome): An out-of-bounds write in V8 allows remote code execution inside a sandbox.
- **CVE-2026-3910** (Google Chrome): An implementation flaw in V8 allows remote code execution inside a sandbox.
- **CVE-2026-116779** (SignalWire FreeSWITCH): Improper handling of SIP MESSAGE requests allows remote execution of API commands.
- **CVE-2026-11645** (Google Chrome): Out-of-bounds read and write in V8 allows remote code execution inside a sandbox.
- **CVE-2026-3909** (Google Chrome): An out-of-bounds write in Skia allows remote memory access via crafted HTML.
- **CVE-2026-85046** (Google Chrome): Type confusion in V8 allows remote code execution inside a sandbox.
- **CVE-2026-111793** (Openwave Webtop Media Transcoder): Failure to enforce file type restrictions allows authenticated users to convert unintended documents.
- **CVE-2026-23918** (Apache HTTP Server): A double free vulnerability in the HTTP/2 protocol may lead to remote code execution.
- **CVE-2026-126187** (React): Unauthenticated remote code execution is possible in React Server Components via crafted payloads.
- **CVE-2026-58115** (Siemens SIMATIC IoT2050): Missing authentication on the Node-RED HTTP interface allows remote system command execution.
- **CVE-2026-113961** (Apple HomeView/iOS/iPadOS): An authorization issue allows a remote attacker to join iMessage group chats and receive messages.
- **CVE-2024-36350** (AMD EPYC Processors): A transient execution vulnerability may allow the leakage of privileged information.
- **CVE-2024-36357** (AMD EPYC Processors): A transient execution vulnerability may allow sensitive information leakage from the L1D cache.
- **CVE-2026-113960** (Apple HomeView/iOS/iPadOS): A vulnerability allows users added to an iMessage group to access messages sent before they joined.
- **CVE-2026-118331** (Google Chrome): A use-after-free in FileAPI allows remote code execution outside the sandbox.
- **CVE-2026-118344** (Google Chrome): A use-after-free in Layout allows remote code execution inside the sandbox.
- **CVE-2026-118348** (Google Chrome): An integer overflow in Skia allows remote code execution outside the sandbox.
- **CVE-2026-0004** (AMD EPYC Processors): A transient execution vulnerability allows local attackers to infer data in the L1D cache.
- **CVE-2026-99288** (Linux Kernel): Failure to reject unhashed sockets during established lookups can lead to memory issues.
- **CVE-2026-102703** (Xen Hypervisor): Incorrect re-validation of internal data allows arbitrary read/write via grant copy.
- **CVE-2026-102704** (Xen Hypervisor): Incorrect re-validation of internal data allows arbitrary read/write via grant copy.

## Index

Every CVE of today's findings; later digests check it so they do not repeat themselves.

| CVE | Finding | Score | First seen |
|---|---|---|---|
| CVE-2026-114713 | UnrealIRCd Command Injection | 10 | 2026-11-15 |
| CVE-2026-90436 | Apache Axis 1.x Remote Code Execution | 8 | 2026-11-17 |
| CVE-2026-98432 | Linux Kernel NoisyTCP Use-After-Free | 7 | 2026-10-30 |

## Source Coverage

| Source | Type | Status | Items |
|---|---|---|---|
| The Hacker News | news | ✅ | 120 |
| BleepingComputer | news | ✅ | 118 |
| SecurityWeek | news | ✅ | 109 |
| Krebs on Security | news | ✅ | 4 |
| Schneier on Security | news | ✅ | 8 |
| Rapid7 blog | news | ✅ | 10 |
| Cloudflare security blog | news | ✅ | 4 |
| CVE Crowd | buzz | ✅ | 21 |
| CVE Crowd | buzz | ✅ | 21 |
| ZoomEye | buzz | ✅ | 5 |
| securityvulnerability.io trending | buzz | ✅ | 18 |
| Intruder cvemon | buzz | ✅ | 10 |
| Vulmon trends | buzz | ✅ | 26 |
| FediSecFeeds | signal | ✅ | 46 |
| 0xMarcio trending public PoCs | signal | ✅ | 44 |
| CISA KEV | feed | ✅ | 14 |
| CERT/CC vulnerability notes | feed | ✅ | 8 |
| GitHub Security Lab advisories | feed | ✅ | 0 |
| Full Disclosure mailing list | feed | ✅ | 15 |
| oss-security mailing list | feed | ✅ | 134 |
| OpenCVE latest | feed | ✅ | 20 |
