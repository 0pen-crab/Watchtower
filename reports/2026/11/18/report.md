# Watchtower Night Report — 2026-11-18
**Cycle:** Night | **Generated:** 2026-11-18 03:10 UTC
**Sources checked:** 21/21 | **KEV additions (30 days):** 14

---

## 🔴 CRITICAL

### 🔄 ConnectWise ScreenConnect Guest-to-Host Execution
**Product:** ConnectWise ScreenConnect Client | **CVE:** CVE-2026-84869 | **CVSS:** 9.9 | **Threat score:** 9/10 (was 9) | **Popularity:** 7.0/10 (3/7 newsrooms, 2/5 trending lists)

**Since 2026-11-13:** new newsroom reports

The vulnerability enables a guest to execute files on the host machine without authorization. Recent reports indicate active campaigns by actors like SCKit targeting unpatched systems. The flaw is currently listed in CISA KEV.

**Why it matters:** Managed Service Providers (MSPs) and their clients are exposed; attackers can gain full control of the host system during a support session.

**Signals:** CISA KEV since 2026-09-11 · EPSS 0.01 · SSVC exploitation: active · trending: CVE Crowd, Vulmon trends

**Mitigation:**
- Update ScreenConnect clients to the latest version
- Restrict remote session permissions
- Monitor for unauthorized file transfers during sessions

**Covered by:** The Hacker News — 2026-11-17 ConnectWise Warns ScreenConnect Attacks Continue as SCKit Targets Unpatched Systems | SecurityWeek — 2026-11-17 MSP ScreenConnect Servers Targeted in Month-Long Campaign

---

## 🟠 HIGH

### 🔄 Apache Axis 1.x Remote Code Execution
**Product:** Apache Axis 1.x (EOL) | **CVE:** CVE-2026-90436 | **CVSS:** 9.8 | **Threat score:** 8/10 (was 8) | **Popularity:** 6.3/10 (2/7 newsrooms, 2/5 trending lists)

**Since 2026-11-17:** public PoC appeared

A public PoC is now available. Rapid7 has detected active exploitation against Atlassian Confluence Data Center and N-able N-central. The product is end-of-life (EOL).

**Why it matters:** Organizations using legacy Axis 1.x integrations are vulnerable to unauthenticated RCE via specially crafted SOAP requests.

**Signals:** EPSS 0.01 · SSVC exploitation: none · public PoC · trending: CVE Crowd, Vulmon trends

**Mitigation:**
- Migrate from Apache Axis 1.x to a supported framework
- Implement WAF rules to block malicious SOAP <Fault> elements
- Audit classpath for dangerous classes

**Covered by:** The Hacker News — 2026-11-13 Hackers Exploit N-central Flaws to Infect 21 Servers, Including 19 Running Hotfix 2 | Rapid7 blog — 2026-11-16 Rapid7 Detected Exploitation of CVE-2026-90436 against Atlassian Confluence Data Center, N-able N-central also Exploited

---

### 📰 Oracle Java 'Java4Shell' RCE
**Product:** Oracle Java SE / GraalVM | **CVE:** CVE-2026-114938 | **CVSS:** 8.1 | **Threat score:** 7/10 | **Popularity:** 7.0/10 (3/7 newsrooms, 2/5 trending lists)

Known as 'Java4Shell', this flaw allows an unauthenticated attacker with network access to compromise the system. A public PoC exists, though exploitation is described as difficult. Oracle has released patches for affected versions of Java SE and GraalVM.

**Why it matters:** Administrators of major Java applications are exposed to potential full system compromise via network protocols.

**Signals:** SSVC exploitation: none · public PoC · trending: CVE Crowd, securityvulnerability.io trending · registries: oss-security mailing list

**Mitigation:**
- Apply the latest Oracle Critical Patch Update (CPU)
- Restrict network access to Java-based services
- Update GraalVM distributions

**Covered by:** The Hacker News — 2026-11-17 Oracle to Patch 11 Java Flaws Today as Critical OpenJDK RCE (CVE-2026-114938) Report Emerges | BleepingComputer — 2026-11-17 Critical Java4Shell flaw allows RCE attacks on major Java applications | Rapid7 blog — 2026-11-17 CVE-2026-114938: Reported Critical Pre-authentication Remote Code Execution in Java 17

---

## 🟡 MEDIUM

### 📰 Linux Kernel Socket Lookup Flaw
**Product:** Linux Kernel | **CVE:** CVE-2026-99288 | **CVSS:** 5.9 | **Threat score:** 4/10 | **Popularity:** 5.4/10 (0/7 newsrooms, 3/5 trending lists)

The flaw occurs during lockless TCP established ehash lookups where memory may be reused before an RCU reader finishes. A public PoC is available, but the impact is limited to partial system stability or memory issues.

**Why it matters:** Linux server administrators are exposed to potential kernel instability or local crashes.

**Signals:** EPSS 0.00 · SSVC exploitation: none · public PoC · trending: CVE Crowd, Vulmon trends, securityvulnerability.io trending · registries: oss-security mailing list

**Mitigation:**
- Update the Linux kernel to the latest stable version
- Monitor system logs for unexpected kernel panics

---

## 📋 Noted

- **CVE-2023-2868** (Barracuda Email Security Gateway): Remote command injection via unsanitized .tar files allows root access.
- **CVE-2026-2441** (Google Chrome): Use-after-free in CSS allows remote code execution inside a sandbox.
- **CVE-2024-1086** (Linux Kernel): Use-after-free in netfilter nf_tables allows local privilege escalation.
- **CVE-2026-96656** (Plex Media Server): Arbitrary file write allows admin users to execute code on load.
- **CVE-2025-43529** (Apple Safari/iOS/iPadOS): Use-after-free in web content processing allows arbitrary code execution.
- **CVE-2026-46300** (Linux Kernel): Shared-frag marker loss in skbuff allows local root escalation.
- **CVE-2026-5281** (Google Chrome): Use-after-free in Dawn allows remote code execution via compromised renderer.
- **CVE-2026-96652** (Plex Media Server): SSRF via /player/timeline allows forcing POST requests to arbitrary destinations.
- **CVE-2026-96655** (Plex Media Server): SSRF via transcode path allows authenticated users to request arbitrary addresses.
- **CVE-2026-87491** (Google Chrome): Out-of-bounds write in V8 allows remote code execution inside a sandbox.
- **CVE-2026-3910** (Google Chrome): V8 implementation flaw allows remote code execution inside a sandbox.
- **CVE-2026-11645** (Google Chrome): Out-of-bounds read/write in V8 allows remote code execution inside a sandbox.
- **CVE-2026-3909** (Google Chrome): Out-of-bounds write in Skia allows remote memory access via crafted HTML.
- **CVE-2026-85046** (Google Chrome): Type confusion in V8 allows remote code execution inside a sandbox.
- **CVE-2026-111793** (Openwave Webtop Media Transcoder): Insufficient file type restrictions allow authenticated users to convert unintended documents.
- **CVE-2026-23918** (Apache HTTP Server): Double free in HTTP/2 protocol may allow unauthenticated remote code execution.
- **CVE-2026-126187** (React): Unauthenticated remote code execution in React Server Components via crafted payloads.
- **CVE-2026-111760** (Git): Recursive clones can be exploited to execute code via symbolic link overwrites.
- **CVE-2026-113961** (Apple HomeView/iOS/iPadOS): Authorization issue allows remote attackers to join iMessage groups and receive messages.
- **CVE-2024-36350** (AMD EPYC Processors): Transient execution vulnerability allows leakage of privileged information from previous stores.
- **CVE-2024-36357** (AMD EPYC Processors): Transient execution vulnerability allows leakage of sensitive information from L1D cache.
- **CVE-2026-113960** (Apple HomeView/iOS/iPadOS): Privacy flaw allows users added to iMessage groups to access previous messages.
- **CVE-2026-118331** (Google Chrome): Use-after-free in FileAPI allows remote code execution outside the sandbox.
- **CVE-2026-118344** (Google Chrome): Use-after-free in Layout allows remote code execution inside the sandbox.
- **CVE-2026-118348** (Google Chrome): Integer overflow in Skia allows remote code execution outside the sandbox.
- **CVE-2026-0004** (AMD EPYC Processors): Transient execution vulnerability allows leakage of sensitive information from L1D cache.
- **CVE-2026-102703** (Xen Hypervisor): Incorrect re-validation of grant copy data allows arbitrary read/write across VMs.
- **CVE-2026-102704** (Xen Hypervisor): Incorrect re-validation of grant copy data allows arbitrary read/write across VMs.
- **CVE-2026-129271** (N-able N-central): Local privilege escalation in Patch Management Engine via attacker-controlled metadata.
- **CVE-2026-129272** (N-able N-central): Authentication bypass via predictable appliance passcode allows remote impersonation.

## Index

Every CVE of today's findings; later digests check it so they do not repeat themselves.

| CVE | Finding | Score | First seen |
|---|---|---|---|
| CVE-2026-84869 | ConnectWise ScreenConnect Guest-to-Host Execution | 9 | 2026-11-13 |
| CVE-2026-90436 | Apache Axis 1.x Remote Code Execution | 8 | 2026-11-17 |
| CVE-2026-114938 | Oracle Java 'Java4Shell' RCE | 7 | 2026-11-18 |
| CVE-2026-99288 | Linux Kernel Socket Lookup Flaw | 4 | 2026-11-18 |

## Source Coverage

| Source | Type | Status | Items |
|---|---|---|---|
| The Hacker News | news | ✅ | 116 |
| BleepingComputer | news | ✅ | 121 |
| SecurityWeek | news | ✅ | 112 |
| Krebs on Security | news | ✅ | 3 |
| Schneier on Security | news | ✅ | 9 |
| Rapid7 blog | news | ✅ | 12 |
| Cloudflare security blog | news | ✅ | 4 |
| CVE Crowd | buzz | ✅ | 18 |
| CVE Crowd | buzz | ✅ | 18 |
| ZoomEye | buzz | ✅ | 5 |
| securityvulnerability.io trending | buzz | ✅ | 18 |
| Intruder cvemon | buzz | ✅ | 10 |
| Vulmon trends | buzz | ✅ | 26 |
| FediSecFeeds | signal | ✅ | 21 |
| 0xMarcio trending public PoCs | signal | ✅ | 45 |
| CISA KEV | feed | ✅ | 14 |
| CERT/CC vulnerability notes | feed | ✅ | 7 |
| GitHub Security Lab advisories | feed | ✅ | 0 |
| Full Disclosure mailing list | feed | ✅ | 15 |
| oss-security mailing list | feed | ✅ | 130 |
| OpenCVE latest | feed | ✅ | 20 |
