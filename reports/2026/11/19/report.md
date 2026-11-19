# Watchtower Night Report — 2026-11-19
**Cycle:** Night | **Generated:** 2026-11-19 03:08 UTC
**Sources checked:** 20/21 | **KEV additions (30 days):** 18

---

## 🔴 CRITICAL

### 🔄 Apache Axis 1.x RCE
**Product:** Apache Axis 1.x (EOL) | **CVE:** CVE-2026-90436 | **CVSS:** 9.8 | **Threat score:** 9/10 (was 8) | **Popularity:** 7.0/10 (2/7 newsrooms, 3/5 trending lists)

**Since 2026-11-17:** added to CISA KEV 2026-11-18

The vulnerability is triggered by deserializing an inbound SOAP fault containing a crafted exceptionName element. It has been added to CISA KEV as of 2026-11-18. Exploitation has been detected in the wild against Atlassian Confluence Data Center and N-able N-central.

**Why it matters:** Legacy systems using this EOL library are vulnerable to full system compromise via unauthenticated network requests.

**Signals:** CISA KEV since 2026-11-18 · EPSS 0.01 · SSVC exploitation: none · trending: CVE Crowd, Intruder cvemon, Vulmon trends · registries: CISA KEV 2026-11-18

**Mitigation:**
- Migrate from the EOL Apache Axis 1.x to a supported framework
- Implement strict WAF rules to filter SOAP <Fault> elements

**Covered by:** The Hacker News — 2026-11-13 Hackers Exploit N-central Flaws to Infect 21 Servers, Including 19 Running Hotfix 2 | Rapid7 blog — 2026-11-16 Rapid7 Detected Exploitation of CVE-2026-90436 against Atlassian Confluence Data Center, N-able N-central also Exploited

---

### 📰 Perforce Puppet Enterprise RCE
**Product:** Perforce Puppet Enterprise | **CVE:** CVE-2026-115731 | **CVSS:** 9.4 | **Threat score:** 9/10 | **Popularity:** 5.4/10 (2/7 newsrooms, 1/5 trending lists)

The flaw occurs when the server processes untrusted data in a PUT request. Attackers with a CA-signed agent certificate can execute code as the service user. If autosigning is enabled without strong verification, unauthenticated attackers can obtain the necessary certificate.

**Why it matters:** Enterprise management servers are exposed; an attacker gains full control over the Puppet Server.

**Signals:** CISA KEV since 2026-11-17 · EPSS 0.01 · SSVC exploitation: active · trending: CVE Crowd · registries: CISA KEV 2026-11-17

**Mitigation:**
- Update to the latest patched version of Puppet Enterprise
- Disable CA autosigning or implement strong verification for agent certificates

**Covered by:** The Hacker News — 2026-11-18 Hackers Exploiting Critical Puppet RCE Flaw Affecting Enterprise Management Servers | SecurityWeek — 2026-11-18 Critical Perforce Puppet RCE Exploited in Attacks

---

### 📰 Apache Roller RCE
**Product:** Apache Roller | **CVE:** CVE-2026-129448, CVE-2026-82384 | **CVSS:** 9.8 | **Threat score:** 9/10 | **Popularity:** 5.4/10 (2/7 newsrooms, 1/5 trending lists)

The vulnerability allows attackers to execute arbitrary code by sending specially crafted vendor extension types to the XML-RPC endpoint before authentication occurs. While initially reported for version 6.1.5, it affects versions 4.0.0 through 6.1.4 as well. Reports indicate the flaw is currently being actively exploited in the wild.

**Why it matters:** Administrators of Apache Roller instances are exposed to full system compromise by unauthenticated remote attackers.

**Signals:** EPSS 0.02 · SSVC exploitation: none · public PoC · trending: CVE Crowd · registries: oss-security mailing list

**Mitigation:**
- Upgrade to Apache Roller 6.1.6 or later
- Disable the XML-RPC endpoint if not required

**Covered by:** The Hacker News — 2026-11-18 Critical Apache Roller RCE Flaw Under Active Exploitation, No Authentication Required | BleepingComputer — 2026-11-18 Apache warns of Roller RCE vulnerability exploited in attacks

---

## 🟠 HIGH

### 🔄 Oracle Java 'Java4Shell' RCE
**Product:** Oracle Java SE / GraalVM | **CVE:** CVE-2026-114938 | **CVSS:** 8.1 | **Threat score:** 7/10 (was 7) | **Popularity:** 9.0/10 (4/7 newsrooms, 5/5 trending lists)

**Since 2026-11-18:** new newsroom reports

The flaw allows unauthenticated attackers with network access to compromise the system via multiple protocols. Recent reports highlight that this affects major enterprise applications including Jira, Jenkins, and Keycloak. CISA has urged immediate patching.

**Why it matters:** A vast array of enterprise Java-based applications are potentially vulnerable to remote takeover.

**Signals:** EPSS 0.01 · SSVC exploitation: none · trending: CVE Crowd, Intruder cvemon, Vulmon trends, ZoomEye, securityvulnerability.io trending · registries: oss-security mailing list

**Mitigation:**
- Apply the latest Oracle Critical Patch Update (CPU)
- Restrict network access to affected Java-based application servers

**Covered by:** The Hacker News — 2026-11-18 Java4Shell Flaw (CVE-2026-114938) Enables Pre-Auth RCE in Jira, Jenkins, Keycloak and More | SecurityWeek — 2026-11-18 Java4Shell Vulnerability Puts Enterprise Applications at Risk of Takeover

---

### 📰 NGINX HTTP/2 RCE and DoS
**Product:** F5 NGINX Open Source and Plus | **CVE:** CVE-2026-123007, CVE-2026-123633 | **CVSS:** 8.1 | **Threat score:** 7/10 | **Popularity:** 7.6/10 (2/7 newsrooms, 4/5 trending lists)

CVE-2026-123007 involves an integer underflow in flow control, while CVE-2026-123633 involves a use-after-free when worker connections are low. Both can lead to RCE if ASLR is disabled or bypassed, otherwise resulting in a denial-of-service. Public PoCs are available.

**Why it matters:** Widely deployed web servers using HTTP/2 are at risk of crashing or remote takeover.

**Signals:** SSVC exploitation: none · public PoC · trending: CVE Crowd, Intruder cvemon, ZoomEye, securityvulnerability.io trending · registries: oss-security mailing list

**Mitigation:**
- Update NGINX to the latest patched version
- Disable HTTP/2 if not required for business operations

**Covered by:** The Hacker News — 2026-11-19 10-Year-Old NGINX HTTP/2 Flaw Lets Unauthenticated Attackers Execute Code on Servers | Rapid7 blog — 2026-11-18 CVE-2026-123007: Critical NGINX HTTP/2 Integer Underflow Leads to RCE (FIXED)

---

## 📋 Noted

- **CVE-2023-2868** (Barracuda Email Security Gateway): Remote command injection via unsanitized .tar files allows root access.
- **CVE-2026-2441** (Google Chrome): Use-after-free in CSS allows remote code execution inside a sandbox.
- **CVE-2026-96656** (Plex Media Server): Arbitrary file write allows admin users to execute code on load.
- **CVE-2025-43529** (Apple Safari/iOS/iPadOS): Use-after-free in web content processing allows arbitrary code execution.
- **CVE-2026-40217** (BerriAI LiteLLM): Remote code execution via bytecode rewriting at a specific URI.
- **CVE-2026-46300** (Linux Kernel): A shared-frag marker issue in skbuff can lead to root escalation.
- **CVE-2026-5281** (Google Chrome): Use-after-free in Dawn allows code execution if the renderer is compromised.
- **CVE-2026-96652** (Plex Media Server): SSRF via the /player/timeline endpoint allows forced POST requests.
- **CVE-2026-96655** (Plex Media Server): Authenticated SSRF via the transcode universal path parameter.
- **CVE-2026-90817** (Vanderbilt University REDCap): Unauthenticated remote code execution via survey routing and data import logic.
- **CVE-2026-87491** (Google Chrome): Out-of-bounds write in V8 allows remote code execution inside a sandbox.
- **CVE-2026-3910** (Google Chrome): V8 implementation flaw allows remote code execution inside a sandbox.
- **CVE-2026-11645** (Google Chrome): Out-of-bounds read and write in V8 allows remote code execution inside a sandbox.
- **CVE-2026-3909** (Google Chrome): Out-of-bounds write in Skia allows remote memory access via crafted HTML.
- **CVE-2026-85046** (Google Chrome): Type confusion in V8 allows remote code execution inside a sandbox.
- **CVE-2026-125350** (Google Chrome): Use-after-free in XML allows remote code execution inside a sandbox.
- **CVE-2026-111793** (Openwave Webtop Media Transcoder): Failure to enforce file type restrictions allows conversion of unintended documents.
- **CVE-2026-23918** (Apache HTTP Server): Double free in HTTP/2 protocol can lead to remote code execution.
- **CVE-2026-115732** (Perforce Puppet Enterprise): Certificate name authorization bypass allows node impersonation and RCE.
- **CVE-2026-111760** (git): Recursive clones can be exploited for RCE via symbolic link overwrites.
- **CVE-2026-129275** (N-able N-central): Missing authentication in repositoryItemGet discloses customer automation policies.
- **CVE-2026-129280** (N-able N-central): Missing authentication in SOAP operations allows cross-customer data access.
- **CVE-2026-129274** (N-able N-central): Missing authentication in RemoteExecutionTaskSubmit allows task result forgery.
- **CVE-2026-129273** (N-able N-central): Syslog configuration injection allows authenticated admins to execute root commands.
- **CVE-2026-129279** (N-able N-central): Password reset response discrepancy allows username enumeration.
- **CVE-2026-129272** (N-able N-central): Predictable appliance passcodes allow authentication bypass and impersonation.
- **CVE-2026-129276** (N-able N-central): Missing authentication in AssetDiscoSimplifiedInfoSubmit allows agent data overwrite.
- **CVE-2026-129277** (N-able N-central): Missing authentication in MaintActionGet allows reading and cancelling maintenance actions.
- **CVE-2026-129278** (N-able N-central): Missing authentication in remoteControlMSPAStartEndTimeSubmit allows audit log tampering.
- **CVE-2026-113961** (Apple HomeView/iOS/iPadOS): Authorization issue allows attackers to join iMessage group chats.

## Index

Every CVE of today's findings; later digests check it so they do not repeat themselves.

| CVE | Finding | Score | First seen |
|---|---|---|---|
| CVE-2026-90436 | Apache Axis 1.x RCE | 9 | 2026-11-17 |
| CVE-2026-115731 | Perforce Puppet Enterprise RCE | 9 | 2026-11-19 |
| CVE-2026-129448 | Apache Roller RCE | 9 | 2026-11-19 |
| CVE-2026-82384 | Apache Roller RCE | 9 | 2026-11-19 |
| CVE-2026-114938 | Oracle Java 'Java4Shell' RCE | 7 | 2026-11-18 |
| CVE-2026-123007 | NGINX HTTP/2 RCE and DoS | 7 | 2026-11-19 |
| CVE-2026-123633 | NGINX HTTP/2 RCE and DoS | 7 | 2026-11-19 |

## Source Coverage

| Source | Type | Status | Items |
|---|---|---|---|
| The Hacker News | news | ✅ | 117 |
| BleepingComputer | news | ✅ | 119 |
| SecurityWeek | news | ✅ | 112 |
| Krebs on Security | news | ✅ | 4 |
| Schneier on Security | news | ✅ | 10 |
| Rapid7 blog | news | ✅ | 12 |
| Cloudflare security blog | news | ❌ | 3 |
| CVE Crowd | buzz | ✅ | 35 |
| CVE Crowd | buzz | ✅ | 35 |
| ZoomEye | buzz | ✅ | 5 |
| securityvulnerability.io trending | buzz | ✅ | 18 |
| Intruder cvemon | buzz | ✅ | 10 |
| Vulmon trends | buzz | ✅ | 26 |
| FediSecFeeds | signal | ✅ | 28 |
| 0xMarcio trending public PoCs | signal | ✅ | 45 |
| CISA KEV | feed | ✅ | 18 |
| CERT/CC vulnerability notes | feed | ✅ | 7 |
| GitHub Security Lab advisories | feed | ✅ | 0 |
| Full Disclosure mailing list | feed | ✅ | 15 |
| oss-security mailing list | feed | ✅ | 120 |
| OpenCVE latest | feed | ✅ | 20 |
