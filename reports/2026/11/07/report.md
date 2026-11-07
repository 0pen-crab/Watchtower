# Watchtower Night Report — 2026-11-07
**Cycle:** Night | **Generated:** 2026-11-07 03:09 UTC
**Sources checked:** 21/21 | **KEV additions (30 days):** 13

---

## 🔴 CRITICAL

### 🔄 WordPress Core RCE (CVE-2026-119977)
**Product:** WordPress Foundation WordPress | **CVE:** CVE-2026-119977 | **CVSS:** 8.1 | **Threat score:** 10/10 (was 10) | **Popularity:** 7.6/10 (2/7 newsrooms, 4/5 trending lists)

**Since 2026-11-05:** new newsroom reports

The vulnerability exists in versions 4.7 through 7.1.3 during the upgrade window. Attackers can target web-accessible staging paths to execute arbitrary code on the server. Recent reports indicate that applying the fix may briefly expose some sites to the flaw one last time.

**Why it matters:** Administrators of outdated WordPress sites are exposed to full server compromise by unauthenticated remote attackers.

**Signals:** CISA KEV since 2026-11-03 · EPSS 0.01 · SSVC exploitation: active · trending: CVE Crowd, Intruder cvemon, Vulmon trends, securityvulnerability.io trending · registries: CISA KEV 2026-11-03

**Mitigation:**
- Update WordPress Core to the latest version
- Monitor server logs for unusual activity in staging paths

**Covered by:** The Hacker News — 2026-11-06 Installing the Fix for an Exploited WordPress Flaw Can Expose Some Sites One Last Time

---

### 🔄 GitLab RCE (CVE-2026-97229)
**Product:** GitLab GitLab | **CVE:** CVE-2026-97229 | **CVSS:** 10 | **Threat score:** 10/10 (was 10) | **Popularity:** 6.3/10 (3/7 newsrooms, 1/5 trending lists)

**Since 2026-10-30:** public PoC appeared

The flaw affects multiple versions of GitLab CE/EE due to insufficient validation in CI/CD configurations. It is actively exploited and listed in CISA KEV. A public PoC has now appeared, increasing the risk of widespread attacks.

**Why it matters:** Unauthenticated attackers can gain full control over GitLab servers, potentially accessing source code and CI/CD secrets.

**Signals:** CISA KEV since 2026-10-29 · EPSS 0.65 · SSVC exploitation: active · public PoC · nuclei template · trending: CVE Crowd · registries: CISA KEV 2026-10-29

**Mitigation:**
- Update to versions 19.2.8, 19.3.5, or 19.4.2
- Restrict access to CI/CD configuration interfaces

**Covered by:** The Hacker News — 2026-10-30 CISA Adds Actively Exploited GitLab RCE and Cisco Firewall DoS Flaws to KEV | BleepingComputer — 2026-11-02 Over 1,000 GitLab servers vulnerable to ongoing RCE attacks | SecurityWeek — 2026-10-30 Max-Severity GitLab Vulnerability Exploited Against Alpine Linux

---

### 📰 SonicWall SonicOS SSL-VPN MFA Bypass
**Product:** SonicWall SonicOS SSLVPN | **CVE:** CVE-2026-19868 | **CVSS:** 7.5 | **Threat score:** 9/10 | **Popularity:** 5.4/10 (1/7 newsrooms, 2/5 trending lists)

The vulnerability stems from improper authentication enforcement in the SSLVPN service. It is currently being exploited in active attacks and was added to CISA KEV on 2026-11-06. A patch is available to address the bypass.

**Why it matters:** Organizations using SonicWall SSL-VPN with SAML are exposed to unauthorized access by attackers who can bypass MFA requirements.

**Signals:** CISA KEV since 2026-11-06 · SSVC exploitation: active · trending: CVE Crowd, Intruder cvemon · registries: CISA KEV 2026-11-06

**Mitigation:**
- Apply the latest SonicOS firmware updates
- Monitor SSL-VPN logs for unusual authentication patterns
- Review SAML configuration and access logs

**Covered by:** BleepingComputer — 2026-11-06 SonicWall warns of new SSL-VPN MFA bypass flaw exploited in attacks

---

## 🟠 HIGH

### 📰 OpenSSH 'SSHole' Auth Bypass (CVE-2026-123158)
**Product:** OpenBSD OpenSSH | **CVE:** CVE-2026-123158 | **CVSS:** 8.1 | **Threat score:** 8/10 | **Popularity:** 6.3/10 (3/7 newsrooms, 1/5 trending lists)

In affected configurations, such as Alpine Linux, passwords between 256 and 1024 characters may be accepted regardless of the actual password. A public PoC is available, and honeypots have already recorded exploitation attempts. Patches were rushed to address the flaw.

**Why it matters:** Attackers can gain root access to Linux accounts that were intended to be password-disabled or secured.

**Signals:** EPSS 0.01 · SSVC exploitation: poc · public PoC · trending: CVE Crowd

**Mitigation:**
- Update OpenSSH to version 10.6p2 or later
- Ensure PAM is configured if using musl libc

**Covered by:** The Hacker News — 2026-11-06 Hackers Target OpenSSH SSHole Flaw Within Hours of Disclosure, Gain Root on Honeypot | BleepingComputer — 2026-11-05 OpenSSH flaw lets attackers log into password-disabled Linux accounts | SecurityWeek — 2026-11-06 OpenSSH Rushes Patches for ‘SSHole’ Authentication Bypass

---

## 🟡 MEDIUM

### 🔄 Barracuda ESG/ADC Root Access Chain
**Product:** Barracuda Email Security Gateway / Load Balancer ADC | **CVE:** CVE-2026-116606, CVE-2026-111560 | **CVSS:** 9.3 | **Threat score:** 6/10 (was 6) | **Popularity:** 7.0/10 (3/7 newsrooms, 2/5 trending lists)

**Since 2026-11-05:** new newsroom reports

CVE-2026-116606 allows an unauthenticated user to restore a crafted configuration archive. This can be chained with CVE-2026-111560, an OS command injection in the timezone field. Security experts have recently demonstrated a full chain enabling root access without login.

**Why it matters:** Attackers can take complete control of email security gateways and load balancers, intercepting traffic or pivoting into the network.

**Signals:** EPSS 0.01 · SSVC exploitation: none · trending: CVE Crowd, Vulmon trends

**Mitigation:**
- Update Barracuda ESG to version 9.4.0.030 or later
- Audit appliance configuration logs for unauthorized imports

**Covered by:** The Hacker News — 2026-11-06 Experts Demonstrate Barracuda Email Security Gateway Chain Enabling Root Access Without Login

---

### 📰 Microsoft Paint RCE (CVE-2026-83844)
**Product:** Microsoft Paint | **CVE:** CVE-2026-83844 | **CVSS:** 8.1 | **Threat score:** 5/10 | **Popularity:** 6.3/10 (1/7 newsrooms, 3/5 trending lists)

The flaw is triggered by processing a specially crafted file. While Microsoft has released a fix, reports indicate that Windows Update may not be delivering the patch automatically to all users. No public PoC is currently available.

**Why it matters:** Windows users are at risk of remote code execution if they open a malicious image file in Paint.

**Signals:** EPSS 0.01 · SSVC exploitation: none · trending: CVE Crowd, Vulmon trends, securityvulnerability.io trending

**Mitigation:**
- Manually check for and install the latest Windows security updates
- Avoid opening image files from untrusted sources

**Covered by:** The Hacker News — 2026-11-06 Microsoft Paint RCE Fix Now Available, but Windows Update Won't Deliver It

---

## 📋 Noted

- **CVE-2026-9198** (IBM Langflow OSS): Unauthenticated RCE via auto-login bypass and code validation.
- **CVE-2025-43529** (Apple Safari/iOS/iPadOS): Use-after-free in web content processing leading to arbitrary code execution.
- **CVE-2026-46300** (Linux Kernel): Memory corruption in skbuff coalescing allowing local privilege escalation.
- **CVE-2026-63030** (WordPress): REST API route confusion and SQL injection leading to RCE.
- **CVE-2026-96654** (Plex Media Server): URL injection allowing attackers to call other plugin functions.
- **CVE-2016-6210** (OpenSSH): Timing difference in password hashing allowing remote user enumeration.
- **CVE-2026-110264** (GitLab): Integer overflow in regular expression compilation leading to unauthenticated RCE.
- **CVE-2026-110193** (IBM Langflow OSS): Authenticated RCE via Agentic Assistant component code generation.
- **CVE-2026-104339** (IBM Langflow OSS): RCE due to improper neutralization of OS command elements.
- **CVE-2026-118331** (Google Chrome): Use-after-free in FileAPI allowing RCE outside the sandbox.
- **CVE-2026-118344** (Google Chrome): Use-after-free in Layout allowing RCE inside the sandbox.
- **CVE-2026-118348** (Google Chrome): Integer overflow in Skia allowing RCE outside the sandbox.
- **CVE-2026-110192** (IBM Langflow OSS): Information disclosure of sensitive credentials for authenticated attackers.
- **CVE-2021-33044** (Dahua IP Cameras): Identity authentication bypass via malicious data packets.
- **CVE-2025-55182** (Meta React Server Components): Pre-authentication RCE via unsafe deserialization of HTTP payloads.
- **CVE-2021-33045** (Dahua IP Cameras/NVR): Identity authentication bypass via malicious data packets.
- **CVE-2025-54236** (Adobe Commerce): Improper input validation leading to session takeover.
- **CVE-2025-8088** (WinRAR): Path traversal allowing arbitrary code execution via malicious archives.
- **CVE-2026-102764** (BeyondTrust Remote Support): Improper origin validation allowing unauthenticated file upload and RCE.
- **CVE-2026-110447** (Collabora Online CODE Server): OS command injection in proxy.php leading to RCE.
- **CVE-2025-14174** (Google Chrome): Out of bounds memory access in ANGLE on macOS.
- **CVE-2026-48356** (Adobe Commerce): Unrestricted upload of dangerous file types leading to RCE.
- **CVE-2021-38003** (Google Chrome): Heap corruption in V8 allowing remote exploitation via HTML.
- **CVE-2026-86950** (Apple iOS/iPadOS/macOS): Out-of-bounds write in CoreGraphics leading to arbitrary code execution.
- **CVE-2026-102489** (Zammad): Session hijack vulnerability leading to RCE as the zammad user.
- **CVE-2026-96652** (Plex Media Server): SSRF via the /player/timeline endpoint.
- **CVE-2026-102490** (Zammad): Local privilege escalation to root via writable service files.
- **CVE-2026-96655** (Plex Media Server): Authenticated SSRF via the transcode universal path parameter.
- **CVE-2026-68820** (Microsoft Windows): Use-after-free in WinSock driver allowing local privilege escalation.
- **CVE-2024-4671** (Google Chrome): Use-after-free in Visuals allowing sandbox escape.

## Index

Every CVE of today's findings; later digests check it so they do not repeat themselves.

| CVE | Finding | Score | First seen |
|---|---|---|---|
| CVE-2026-119977 | WordPress Core RCE (CVE-2026-119977) | 10 | 2026-11-05 |
| CVE-2026-97229 | GitLab RCE (CVE-2026-97229) | 10 | 2026-10-30 |
| CVE-2026-19868 | SonicWall SonicOS SSL-VPN MFA Bypass | 9 | 2026-11-07 |
| CVE-2026-123158 | OpenSSH 'SSHole' Auth Bypass (CVE-2026-123158) | 8 | 2026-11-07 |
| CVE-2026-116606 | Barracuda ESG/ADC Root Access Chain | 6 | 2026-11-05 |
| CVE-2026-111560 | Barracuda ESG/ADC Root Access Chain | 6 | 2026-11-05 |
| CVE-2026-83844 | Microsoft Paint RCE (CVE-2026-83844) | 5 | 2026-11-07 |

## Source Coverage

| Source | Type | Status | Items |
|---|---|---|---|
| The Hacker News | news | ✅ | 123 |
| BleepingComputer | news | ✅ | 74 |
| SecurityWeek | news | ✅ | 100 |
| Krebs on Security | news | ✅ | 2 |
| Schneier on Security | news | ✅ | 7 |
| Rapid7 blog | news | ✅ | 9 |
| Cloudflare security blog | news | ✅ | 8 |
| CVE Crowd | buzz | ✅ | 35 |
| CVE Crowd | buzz | ✅ | 35 |
| ZoomEye | buzz | ✅ | 5 |
| securityvulnerability.io trending | buzz | ✅ | 18 |
| Intruder cvemon | buzz | ✅ | 10 |
| Vulmon trends | buzz | ✅ | 26 |
| FediSecFeeds | signal | ✅ | 40 |
| 0xMarcio trending public PoCs | signal | ✅ | 41 |
| CISA KEV | feed | ✅ | 13 |
| CERT/CC vulnerability notes | feed | ✅ | 4 |
| GitHub Security Lab advisories | feed | ✅ | 0 |
| Full Disclosure mailing list | feed | ✅ | 15 |
| oss-security mailing list | feed | ✅ | 132 |
| OpenCVE latest | feed | ✅ | 20 |
