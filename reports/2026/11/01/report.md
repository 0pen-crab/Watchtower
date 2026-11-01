# Watchtower Night Report — 2026-11-01
**Cycle:** Night | **Generated:** 2026-11-01 00:06 UTC
**Sources checked:** 21/21 | **KEV additions (30 days):** 18

---

## 🔴 CRITICAL

### 📰 Ivanti Connect Secure Root Escalation (CVE-2026-111357)
**Product:** Ivanti Connect Secure | **CVE:** CVE-2026-111357 | **CVSS:** 7 | **Threat score:** 9/10 | **Popularity:** 5.4/10 (1/7 newsrooms, 2/5 trending lists)

The flaw exists in the dsinvoked broker's handling of DSCache configuration data. It is currently being exploited in the wild, often chained with other vulnerabilities to achieve unauthenticated root access. CISA added this CVE to the KEV catalog on October 30, 2026.

**Why it matters:** Administrators of Ivanti VPN gateways are exposed; a successful attack grants full system control to the attacker.

**Signals:** CISA KEV since 2026-10-30 · EPSS 0.01 · SSVC exploitation: active · trending: Intruder cvemon, Vulmon trends · registries: CISA KEV 2026-10-30

**Mitigation:**
- Apply the latest vendor security patches immediately
- Review system logs for unauthorized root-level activity
- Restrict management interface access to trusted networks

**Covered by:** The Hacker News — 2026-10-31 Attackers Chain Three Ivanti Connect Secure Flaws to Gain Unauthenticated Root Access

---

### 🔄 Oracle E-Business Suite RCE (CVE-2026-101767)
**Product:** Oracle Application Object Library | **CVE:** CVE-2026-101767 | **CVSS:** 9.8 | **Threat score:** 9/10 (was 8) | **Popularity:** 5.4/10 (2/7 newsrooms, 1/5 trending lists)

**Since 2026-10-30:** public PoC appeared

This critical vulnerability affects versions 12.2.3 through 12.2.15 of the Oracle E-Business Suite Core component. A public PoC has now appeared, and reports indicate attackers are actively probing for vulnerable systems. Oracle released a patch as part of the October 2026 CPU.

**Why it matters:** Organizations using Oracle EBS are at high risk of full system takeover by unauthenticated remote actors.

**Signals:** EPSS 0.01 · SSVC exploitation: none · public PoC · trending: Vulmon trends

**Mitigation:**
- Install the October 2026 Critical Patch Update (CPU)
- Implement strict network segmentation for EBS instances
- Monitor HTTP traffic for exploitation attempts

**Covered by:** The Hacker News — 2026-10-28 Hackers Target Critical Oracle E-Business Suite RCE Flaw Days After Security Patch | SecurityWeek — 2026-10-28 Hackers Start Probing Fresh Oracle EBS Vulnerability

---

## 🟠 HIGH

### 🔄 Drupal Commerce Core Authorization Bypass (CVE-2026-118539)
**Product:** Drupal Commerce Core | **CVE:** CVE-2026-118539 | **CVSS:** 6.5 | **Threat score:** 8/10 (was 8) | **Popularity:** 7.0/10 (3/7 newsrooms, 2/5 trending lists)

**Since 2026-10-30:** CVSS assigned: 6.5

The flaw affects Commerce Core versions 0.0.0-2.41 and 3.0.0-3.3.13. While the CVSS is now assigned at 6.5, news reports indicate the flaw has been exploited in attacks against online stores. A patch is available via SA-CONTRIB-2026-254.

**Why it matters:** Online store owners using Drupal Commerce may have sensitive data exposed to unauthorized users.

**Signals:** EPSS 0.00 · SSVC exploitation: none · trending: CVE Crowd, Vulmon trends

**Mitigation:**
- Update Drupal Commerce Core to the latest patched version
- Audit access logs for unusual forceful browsing patterns
- Verify authorization settings on critical store endpoints

**Covered by:** The Hacker News — 2026-10-30 Hackers Actively Exploit Highly Critical Drupal Commerce Core Authorization Bypass Flaw | BleepingComputer — 2026-10-30 Drupal warns of critical Commerce Core flaw exploited in attacks | SecurityWeek — 2026-10-30 Drupal Commerce Core Vulnerability Exploited Against Online Stores

---

## 📋 Noted

- **CVE-2026-104935** (Ivanti Connect Secure): Remote unauthenticated command execution via authentication bypass by spoofing.
- **CVE-2026-88771** (Citrix NetScaler ADC/Gateway): Remote code execution via improper input validation.
- **CVE-2026-86950** (Apple iOS/iPadOS/macOS): Arbitrary code execution via an out-of-bounds write issue.
- **CVE-2026-46300** (Linux Kernel): Vulnerability in skbuff coalescing that breaks invariants for in-place writers.
- **CVE-2026-63030** (WordPress): Remote code execution via REST API route confusion and SQL injection.
- **CVE-2026-96654** (Plex Media Server): URL injection allowing attackers to call other plugins' functions.
- **CVE-2026-110936** (Siemens Software Center): Local privilege escalation via DLL hijacking from an uncontrolled search path.
- **CVE-2026-110264** (GitLab): Unauthenticated remote code execution via integer overflow in regular expression compilation.
- **CVE-2026-111862** (Rank Math SEO PRO): Supply-chain compromise delivering a self-restoring backdoor.
- **CVE-2026-80097** (Microsoft Authenticator for Android): Local privilege elevation allowing apps to steal work account tokens.
- **CVE-2026-113470** (Mozilla Firefox/Thunderbird): Cryptographic issue in security block-lists and allow-lists.
- **CVE-2026-106378** (Google Chrome): Sandbox escape on macOS allowing remote code execution outside the sandbox.
- **CVE-2026-86990** (Apple iOS/iPadOS/macOS): Malicious apps may access the camera without user permission.
- **CVE-2026-86987** (Apple iOS/iPadOS): Remote attacker may access sensitive user data via authorization issues.
- **CVE-2026-65339** (Apple iOS/iPadOS/macOS): Logic issue allowing apps to leak sensitive user information.
- **CVE-2026-58882** (Android): SMS of Death exploit that can remotely crash unpatched phones.
- **CVE-2021-33044** (Dahua IP Cameras/Devices): Identity authentication bypass via malicious data packets.
- **CVE-2021-33045** (Dahua IP Cameras/Devices): Identity authentication bypass via malicious data packets.
- **CVE-2025-54236** (Adobe Commerce): Improper input validation leading to session takeover.
- **CVE-2026-42208** (BerriAI litellm): Unauthenticated SQL injection in Proxy API key verification.
- **CVE-2026-88772** (Citrix NetScaler ADC/Gateway): Memory overflow leading to remote code execution or denial of service.
- **CVE-2026-110447** (Collabora Online CODE Server): Remote code execution via OS command injection in proxy.php.
- **CVE-2026-48356** (Adobe Commerce/B2B): Arbitrary code execution via unrestricted upload of dangerous file types.
- **CVE-2026-102764** (BeyondTrust Remote Support): Unauthenticated file operations via improper origin validation.
- **CVE-2026-88779** (Citrix NetScaler ADC/Gateway): Memory overflow leading to denial of service.
- **CVE-2026-68820** (Microsoft Windows 10): Local privilege escalation via use-after-free in WinSock driver.
- **CVE-2024-39717** (Versa Director): Malicious file upload via the Change Favicon option.
- **CVE-2026-75650** (Adobe Commerce/B2B): Remote code execution via improper neutralization in a template engine.
- **CVE-2026-96652** (Plex Media Server): Server-side request forgery via the player timeline endpoint.
- **CVE-2026-96656** (Plex Media Server): Arbitrary file write allowing execution of malicious .so files.

## Index

Every CVE of today's findings; later digests check it so they do not repeat themselves.

| CVE | Finding | Score | First seen |
|---|---|---|---|
| CVE-2026-111357 | Ivanti Connect Secure Root Escalation (CVE-2026-111357) | 9 | 2026-11-01 |
| CVE-2026-101767 | Oracle E-Business Suite RCE (CVE-2026-101767) | 9 | 2026-10-30 |
| CVE-2026-118539 | Drupal Commerce Core Authorization Bypass (CVE-2026-118539) | 8 | 2026-10-30 |

## Source Coverage

| Source | Type | Status | Items |
|---|---|---|---|
| The Hacker News | news | ✅ | 110 |
| BleepingComputer | news | ✅ | 21 |
| SecurityWeek | news | ✅ | 103 |
| Krebs on Security | news | ✅ | 2 |
| Schneier on Security | news | ✅ | 11 |
| Rapid7 blog | news | ✅ | 11 |
| Cloudflare security blog | news | ✅ | 9 |
| CVE Crowd | buzz | ✅ | 19 |
| CVE Crowd | buzz | ✅ | 19 |
| ZoomEye | buzz | ✅ | 5 |
| securityvulnerability.io trending | buzz | ✅ | 18 |
| Intruder cvemon | buzz | ✅ | 8 |
| Vulmon trends | buzz | ✅ | 26 |
| FediSecFeeds | signal | ✅ | 146 |
| 0xMarcio trending public PoCs | signal | ✅ | 48 |
| CISA KEV | feed | ✅ | 18 |
| CERT/CC vulnerability notes | feed | ✅ | 4 |
| GitHub Security Lab advisories | feed | ✅ | 5 |
| Full Disclosure mailing list | feed | ✅ | 15 |
| oss-security mailing list | feed | ✅ | 130 |
| OpenCVE latest | feed | ✅ | 20 |
