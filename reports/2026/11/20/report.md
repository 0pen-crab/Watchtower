# Watchtower Night Report — 2026-11-20
**Cycle:** Night | **Generated:** 2026-11-20 03:12 UTC
**Sources checked:** 20/21 | **KEV additions (30 days):** 17

---

## 🔴 CRITICAL

### 📰 Vanderbilt REDCap RCE
**Product:** Vanderbilt University REDCap | **CVE:** CVE-2026-90817 | **CVSS:** 9.8 | **Threat score:** 10/10 | **Popularity:** 5.4/10 (1/7 newsrooms, 2/5 trending lists)

The flaw allows attackers to manipulate HTTP requests to access unintended controller routes and supply crafted file-path parameters. It is currently listed in CISA KEV as being actively exploited by ransomware and cryptomining campaigns. A patch is available from the vendor.

**Why it matters:** Organizations using REDCap for research data management are exposed to full server compromise by unauthenticated remote attackers.

**Signals:** CISA KEV since 2026-11-18 · EPSS 0.25 · SSVC exploitation: active · trending: Intruder cvemon, Vulmon trends · registries: CISA KEV 2026-11-18

**Mitigation:**
- Update REDCap to the latest patched version
- Restrict public access to survey endpoints where possible

**Covered by:** The Hacker News — 2026-11-19 CISA Warns of 4 Exploited Flaws Linked to Ransomware, Cryptomining, and LLMjacking Attacks

---

### 🔄 Apache Axis 1.x RCE
**Product:** Apache Axis 1.x (EOL) | **CVE:** CVE-2026-90436 | **CVSS:** 9.8 | **Threat score:** 9/10 (was 9) | **Popularity:** 7.0/10 (3/7 newsrooms, 2/5 trending lists)

**Since 2026-11-17:** SSVC exploitation none -> active

The vulnerability occurs when Axis loads a named class from a SOAP Fault detail element. This can lead to RCE if a suitable class exists on the application's classpath. It is now confirmed as actively exploited and listed in CISA KEV.

**Why it matters:** Users of the end-of-life Axis 1.x are exposed to full system compromise by unauthenticated remote attackers.

**Signals:** CISA KEV since 2026-11-18 · EPSS 0.02 · SSVC exploitation: active · trending: Intruder cvemon, Vulmon trends · registries: CISA KEV 2026-11-18

**Mitigation:**
- Migrate to a supported SOAP framework
- Implement strict network filtering for SOAP traffic
- Remove unnecessary classes from the application classpath

**Covered by:** The Hacker News — 2026-11-19 CISA Warns of 4 Exploited Flaws Linked to Ransomware, Cryptomining, and LLMjacking Attacks | SecurityWeek — 2026-11-19 Critical Apache Roller, Axis Vulnerabilities Exploited in Attacks

---

### 📰 VMware vCenter Authentication Bypass
**Product:** VMware vCenter / Telco Cloud | **CVE:** CVE-2026-123890, CVE-2026-59309 | **CVSS:** 9.8 | **Threat score:** 9/10 | **Popularity:** 7.0/10 (4/7 newsrooms, 1/5 trending lists)

The flaw was exploited as a zero-day by Chinese APT groups starting in September. It affects multiple versions of vCenter, Telco Cloud Platform, and Telco Cloud Infrastructure. VMware has released security updates to address the issue.

**Why it matters:** Attackers with network access can bypass authentication to gain administrative control over the virtualization infrastructure.

**Signals:** SSVC exploitation: none · trending: CVE Crowd

**Mitigation:**
- Apply VMware patches for vCenter 8.0, 9.0, and 9.1
- Update Telco Cloud Platform to the latest fixed versions
- Restrict network access to vCenter management interfaces

**Covered by:** The Hacker News — 2026-11-19 Critical VMware vCenter Zero-Day Flaw Lets Network Attackers Bypass Authentication | BleepingComputer — 2026-11-19 VMware patches vCenter zero-day exploited in attacks since September | SecurityWeek — 2026-11-19 Newly Patched VMware vCenter Flaw Exploited as Zero-Day by Chinese APT | Rapid7 blog — 2026-11-19 CVE-2026-123890: Critical Authentication Bypass in VMware vCenter

---

### 🔄 Apache Roller RCE
**Product:** Apache Roller | **CVE:** CVE-2026-129448, CVE-2026-82384 | **CVSS:** 9.8 | **Threat score:** 9/10 (was 9) | **Popularity:** 6.3/10 (3/7 newsrooms, 1/5 trending lists)

**Since 2026-11-19:** new newsroom reports

Recent reports confirm this vulnerability is being actively exploited in the wild. The issue affects versions 4.0.0 through 6.1.5, where vendor extension types are deserialized before authentication. Users must upgrade to version 6.1.6 or later.

**Why it matters:** Unauthenticated remote attackers can execute arbitrary code on servers running affected versions of Apache Roller.

**Signals:** EPSS 0.01 · SSVC exploitation: none · trending: Vulmon trends · registries: oss-security mailing list

**Mitigation:**
- Upgrade to Apache Roller 6.1.6 or later
- Disable the XML-RPC feature if not required

**Covered by:** SecurityWeek — 2026-11-19 Critical Apache Roller, Axis Vulnerabilities Exploited in Attacks

---

## 🟠 HIGH

### 🔄 Oracle Java 'Java4Shell' RCE
**Product:** Oracle Java SE and GraalVM | **CVE:** CVE-2026-114938 | **CVSS:** 8.1 | **Threat score:** 8/10 (was 7) | **Popularity:** 9.0/10 (4/7 newsrooms, 5/5 trending lists)

**Since 2026-11-18:** new newsroom reports

The flaw allows an unauthenticated attacker with network access to compromise the system. Recent reports indicate that exploitation attempts have begun in the wild. Oracle has released security updates for affected versions.

**Why it matters:** Organizations running vulnerable Oracle Java or GraalVM environments are now facing active exploitation attempts.

**Signals:** EPSS 0.01 · SSVC exploitation: none · trending: CVE Crowd, Intruder cvemon, Vulmon trends, ZoomEye, securityvulnerability.io trending · registries: oss-security mailing list

**Mitigation:**
- Apply the latest Oracle Java SE and GraalVM security updates
- Restrict network access to affected compiler components

**Covered by:** SecurityWeek — 2026-11-19 Java4Shell Exploitation Attempts Begin as Vendors Rush Out Advisories

---

### 📰 PHP Session RCEs
**Product:** PHP | **CVE:** CVE-2026-115560, CVE-2026-126714 | **CVSS:** 9.2 | **Threat score:** 8/10 | **Popularity:** 7.6/10 (3/7 newsrooms, 3/5 trending lists)

CVE-2026-115560 involves a serializer mismatch during multipart uploads, while CVE-2026-126714 involves partially overwritten session files. Both allow an attacker to inject data that is later unserialized as objects. Public PoCs exist for the serializer mismatch.

**Why it matters:** Attackers can achieve RCE on PHP servers by manipulating session data via file uploads.

**Signals:** SSVC exploitation: none · public PoC · trending: CVE Crowd, Vulmon trends, securityvulnerability.io trending

**Mitigation:**
- Update PHP to the latest patched version
- Disable session.upload_progress if not required

**Covered by:** The Hacker News — 2026-11-19 phpAfterShell Explained: How Hackers Could Turn a PHP Session Flaw Into Code Execution | BleepingComputer — 2026-11-19 PHP security updates fix 18 flaws, including critical RCE bugs | SecurityWeek — 2026-11-19 PHP Patches Seven Critical RCE Vulnerabilities

---

### 🔄 NGINX HTTP/2 RCE and DoS (NGINX2Root)
**Product:** F5 NGINX Open Source and Plus | **CVE:** CVE-2026-123007, CVE-2026-123633 | **CVSS:** 8.1 | **Threat score:** 7/10 (was 7) | **Popularity:** 9.0/10 (4/7 newsrooms, 5/5 trending lists)

**Since 2026-11-19:** new newsroom reports

The flaws allow remote attackers to crash worker processes or execute code if ASLR is disabled. Public PoC exploits are now available. F5 has released patches to address these issues.

**Why it matters:** Administrators of NGINX servers using HTTP/2 are exposed to potential server hijacking or denial-of-service attacks.

**Signals:** EPSS 0.06 · SSVC exploitation: none · public PoC · trending: CVE Crowd, Intruder cvemon, Vulmon trends, ZoomEye, securityvulnerability.io trending · registries: oss-security mailing list

**Mitigation:**
- Update NGINX to the latest patched version
- Enable ASLR on host systems to hinder RCE
- Disable HTTP/2 if not strictly required

**Covered by:** BleepingComputer — 2026-11-19 Critical NGINX ‘NGINX2Root’ bugs let attackers hijack servers | SecurityWeek — 2026-11-19 F5 Patches Critical NGINX2Root Flaws as PoC Exploits Go Public

---

## 🟡 MEDIUM

### 📰 NGINX Multiple RCE/DoS Flaws (NGINX2Root)
**Product:** F5 NGINX Open Source and Plus | **CVE:** CVE-2026-123634, CVE-2026-121810, CVE-2026-113425 | **CVSS:** 8.1 | **Threat score:** 6/10 | **Popularity:** 7.6/10 (3/7 newsrooms, 3/5 trending lists)

These vulnerabilities can be triggered by specially crafted requests to the resolver, HTTP/3 traffic, or mail proxy traffic. Like other NGINX2Root flaws, RCE is possible if ASLR is bypassed or disabled. Patches have been issued by F5.

**Why it matters:** Users of NGINX as a proxy, mail server, or HTTP/3 provider are at risk of remote crashes or code execution.

**Signals:** EPSS 0.02 · SSVC exploitation: none · trending: CVE Crowd, Intruder cvemon, Vulmon trends

**Mitigation:**
- Update NGINX to the latest patched version
- Enable ASLR on host systems
- Review proxy and SSI configurations

**Covered by:** The Hacker News — 2026-11-19 10-Year-Old NGINX HTTP/2 Flaw Lets Unauthenticated Attackers Execute Code on Servers | BleepingComputer — 2026-11-19 Critical NGINX ‘NGINX2Root’ bugs let attackers hijack servers | SecurityWeek — 2026-11-19 F5 Patches Critical NGINX2Root Flaws as PoC Exploits Go Public

---

## 📋 Noted

- **CVE-2023-2868** (Barracuda Email Security Gateway): Remote command injection via unsanitized .tar files allows root access.
- **CVE-2026-111497** (Google Brotli): An out-of-bounds write in the decoder can lead to remote code execution.
- **CVE-2026-40217** (BerriAI LiteLLM): Remote code execution is possible via bytecode rewriting at a specific URI.
- **CVE-2026-2441** (Google Chrome): A use-after-free vulnerability in CSS allows remote code execution inside a sandbox.
- **CVE-2026-96656** (Plex Media Server): Arbitrary file write allows admin users to execute code on load.
- **CVE-2026-5281** (Google Chrome): A use-after-free in Dawn allows a compromised renderer to execute code.
- **CVE-2026-96652** (Plex Media Server): SSRF via the /player/timeline endpoint allows forced POST requests.
- **CVE-2026-96655** (Plex Media Server): Authenticated users can perform SSRF via the transcode universal path.
- **CVE-2026-87491** (Google Chrome): An out-of-bounds write in V8 allows remote code execution inside a sandbox.
- **CVE-2026-3910** (Google Chrome): An implementation flaw in V8 allows remote code execution inside a sandbox.
- **CVE-2026-11645** (Google Chrome): Out-of-bounds read and write in V8 allows remote code execution inside a sandbox.
- **CVE-2026-3909** (Google Chrome): An out-of-bounds write in Skia allows remote memory access via crafted HTML.
- **CVE-2024-10441** (Synology BeeStation OS / DSM): Improper output encoding in the system plugin daemon allows remote code execution.
- **CVE-2026-85046** (Google Chrome): Type confusion in V8 allows remote code execution inside a sandbox.
- **CVE-2026-125350** (Google Chrome): A use-after-free in the XML component allows remote code execution inside a sandbox.
- **CVE-2026-111793** (Openwave Webtop Media Transcoder): Lack of file type restriction allows authenticated users to convert unintended documents.
- **CVE-2026-23918** (Apache HTTP Server): A double free in the HTTP/2 protocol may lead to remote code execution.
- **CVE-2026-129274** (N-able N-central): Missing authentication in ServerMMS2 allows forgery of remote execution task results.
- **CVE-2026-129280** (N-able N-central): Missing authentication in SOAP operations allows cross-customer data access and modification.
- **CVE-2026-129275** (N-able N-central): Unauthenticated access to repositoryItemGet allows downloading customer automation policies.
- **CVE-2026-113961** (Apple iOS / iPadOS / macOS): An authorization issue allows remote attackers to join iMessage group chats.
- **CVE-2026-116331** (PostgreSQL): Type confusion in aggregate optimization allows an object creator to execute arbitrary code.
- **CVE-2026-129272** (N-able N-central): Predictable appliance passcodes allow authentication bypass and appliance impersonation.
- **CVE-2026-129279** (N-able N-central): Password reset response discrepancies allow for username enumeration.
- **CVE-2026-129273** (N-able N-central): Syslog configuration injection allows authenticated admins to execute root commands.
- **CVE-2024-36350** (AMD EPYC Processors): A transient execution vulnerability may allow leakage of privileged information.
- **CVE-2026-129276** (N-able N-central): Missing authentication in AssetDiscoSimplifiedInfoSubmit allows overwriting agent asset data.
- **CVE-2026-129277** (N-able N-central): Unauthenticated access to MaintActionGet allows reading and cancelling maintenance actions.
- **CVE-2026-129278** (N-able N-central): Missing authentication allows tampering with Take Control tasks and audit logs.
- **CVE-2026-129281** (N-able N-central): Incorrect authorization allows view-only users to set device execution configurations.

## Index

Every CVE of today's findings; later digests check it so they do not repeat themselves.

| CVE | Finding | Score | First seen |
|---|---|---|---|
| CVE-2026-90817 | Vanderbilt REDCap RCE | 10 | 2026-11-20 |
| CVE-2026-90436 | Apache Axis 1.x RCE | 9 | 2026-11-17 |
| CVE-2026-123890 | VMware vCenter Authentication Bypass | 9 | 2026-11-20 |
| CVE-2026-59309 | VMware vCenter Authentication Bypass | 9 | 2026-11-20 |
| CVE-2026-129448 | Apache Roller RCE | 9 | 2026-11-19 |
| CVE-2026-82384 | Apache Roller RCE | 9 | 2026-11-19 |
| CVE-2026-114938 | Oracle Java 'Java4Shell' RCE | 8 | 2026-11-18 |
| CVE-2026-115560 | PHP Session RCEs | 8 | 2026-11-20 |
| CVE-2026-126714 | PHP Session RCEs | 8 | 2026-11-20 |
| CVE-2026-123007 | NGINX HTTP/2 RCE and DoS (NGINX2Root) | 7 | 2026-11-19 |
| CVE-2026-123633 | NGINX HTTP/2 RCE and DoS (NGINX2Root) | 7 | 2026-11-19 |
| CVE-2026-123634 | NGINX Multiple RCE/DoS Flaws (NGINX2Root) | 6 | 2026-11-20 |
| CVE-2026-121810 | NGINX Multiple RCE/DoS Flaws (NGINX2Root) | 6 | 2026-11-20 |
| CVE-2026-113425 | NGINX Multiple RCE/DoS Flaws (NGINX2Root) | 6 | 2026-11-20 |

## Source Coverage

| Source | Type | Status | Items |
|---|---|---|---|
| The Hacker News | news | ✅ | 118 |
| BleepingComputer | news | ✅ | 121 |
| SecurityWeek | news | ✅ | 115 |
| Krebs on Security | news | ✅ | 3 |
| Schneier on Security | news | ✅ | 8 |
| Rapid7 blog | news | ✅ | 14 |
| Cloudflare security blog | news | ❌ | 2 |
| CVE Crowd | buzz | ✅ | 36 |
| CVE Crowd | buzz | ✅ | 36 |
| ZoomEye | buzz | ✅ | 5 |
| securityvulnerability.io trending | buzz | ✅ | 18 |
| Intruder cvemon | buzz | ✅ | 11 |
| Vulmon trends | buzz | ✅ | 26 |
| FediSecFeeds | signal | ✅ | 40 |
| 0xMarcio trending public PoCs | signal | ✅ | 48 |
| CISA KEV | feed | ✅ | 17 |
| CERT/CC vulnerability notes | feed | ✅ | 7 |
| GitHub Security Lab advisories | feed | ✅ | 0 |
| Full Disclosure mailing list | feed | ✅ | 15 |
| oss-security mailing list | feed | ✅ | 115 |
| OpenCVE latest | feed | ✅ | 20 |
