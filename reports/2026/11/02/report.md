# Watchtower Night Report — 2026-11-02
**Cycle:** Night | **Generated:** 2026-11-02 03:07 UTC
**Sources checked:** 21/21 | **KEV additions (30 days):** 18

---

## 🟠 HIGH

### 📰 Canonical LXD Certificate Validation Flaw
**Product:** Canonical LXD / MicroCloud | **CVE:** CVE-2026-112816 | **CVSS:** 10 | **Threat score:** 8/10 | **Popularity:** 5.4/10 (1/7 newsrooms, 2/5 trending lists)

The vulnerability stems from a failure to properly validate certificate chains in the HTTPS listener. A public PoC exists demonstrating how an attacker can gain full access to clusters and managed VMs without possessing a private key. Patches have been released for versions 4.0, 5.0, 5.21, and 6.9.

**Why it matters:** Administrators of LXD or MicroCloud clusters are exposed to total system compromise and unauthorized cluster management.

**Signals:** EPSS 0.00 · SSVC exploitation: none · public PoC · trending: CVE Crowd, Vulmon trends

**Mitigation:**
- Update LXD to versions 4.0.15, 5.0.11, 5.21.9, or 6.10.1
- Restrict network access to the LXD HTTPS listener to trusted IPs

**Covered by:** The Hacker News — 2026-11-01 CVSS 10.0 LXD, MicroCloud Flaw Lets Attackers Impersonate Trusted Clients Without a Private Key

---

## 📋 Noted

- **CVE-2026-104935** (Ivanti Connect Secure): Remote unauthenticated command execution via authentication bypass by spoofing.
- **CVE-2026-86950** (Apple iOS/iPadOS/macOS): Arbitrary code execution via out-of-bounds write when processing a crafted file.
- **CVE-2026-102764** (BeyondTrust Remote Support): Unauthenticated file operations via improper origin validation in internal messaging.
- **CVE-2026-63030** (WordPress): Remote code execution via REST API route confusion and SQL injection.
- **CVE-2026-96654** (Plex Media Server): URL injection allowing attackers to call other plugins' functions.
- **CVE-2026-110936** (Siemens Software Center): Local authenticated arbitrary code execution via DLL hijacking.
- **CVE-2026-118527** (unknown product): Vulnerability listed in CISA KEV without provided technical details.
- **CVE-2026-110264** (GitLab): Unauthenticated remote code execution via integer overflow in regular expression compilation.
- **CVE-2026-113380** (Signal RingRTC): Denial of service allowing malicious callers to block call hang-ups.
- **CVE-2026-80097** (Microsoft Authenticator for Android): Local privilege elevation allowing apps to steal work account tokens.
- **CVE-2026-113470** (Mozilla Firefox/Thunderbird): Cryptographic issue in security block-lists and allow-lists components.
- **CVE-2026-116366** (ClickHouse Server): Unauthenticated remote code execution via network access.
- **CVE-2026-106378** (Google Chrome): Sandbox privilege elevation on macOS via crafted HTML page.
- **CVE-2026-86990** (Apple iOS/iPadOS/macOS): Unauthorized camera access by malicious applications.
- **CVE-2026-86987** (Apple iOS/iPadOS): Remote access to sensitive user data via authorization issue.
- **CVE-2026-65339** (Apple iOS/iPadOS/macOS): Sensitive user information leak via logic issue.
- **CVE-2026-114820** (Oracle GraalVM/Java SE): Unauthenticated network-based vulnerability in the JSSE component.
- **CVE-2026-115560** (unknown product): Vulnerability referred to as php2shell by Cloudflare.
- **CVE-2026-58882** (unknown product): Android SMS of Death exploit causing remote phone crashes.
- **CVE-2021-33044** (Dahua IP Cameras/Devices): Identity authentication bypass via malicious data packets.
- **CVE-2021-33045** (Dahua IP Cameras/Devices): Identity authentication bypass via malicious data packets.
- **CVE-2025-54236** (Adobe Commerce): Improper input validation leading to session takeover.
- **CVE-2024-21413** (Microsoft Outlook): Remote code execution vulnerability in Microsoft 365 Apps and Office 2016.
- **CVE-2026-42208** (BerriAI litellm): Unauthenticated SQL injection in Proxy API key verification.
- **CVE-2026-88771** (Citrix NetScaler ADC/Gateway): Unauthenticated remote code execution via improper input validation.
- **CVE-2026-110447** (Collabora Online CODE Server): Remote code execution via OS command injection in proxy.php.
- **CVE-2026-48356** (Adobe Commerce): Arbitrary code execution via unrestricted upload of dangerous file types.
- **CVE-2026-88779** (Citrix NetScaler ADC/Gateway): Memory overflow leading to denial of service.
- **CVE-2026-68820** (Microsoft Windows 10): Local privilege elevation via use-after-free in WinSock driver.
- **CVE-2024-39717** (Versa Director): Malicious file upload via the Change Favicon option for administrators.

## Index

Every CVE of today's findings; later digests check it so they do not repeat themselves.

| CVE | Finding | Score | First seen |
|---|---|---|---|
| CVE-2026-112816 | Canonical LXD Certificate Validation Flaw | 8 | 2026-11-02 |

## Source Coverage

| Source | Type | Status | Items |
|---|---|---|---|
| The Hacker News | news | ✅ | 108 |
| BleepingComputer | news | ✅ | 24 |
| SecurityWeek | news | ✅ | 103 |
| Krebs on Security | news | ✅ | 2 |
| Schneier on Security | news | ✅ | 10 |
| Rapid7 blog | news | ✅ | 11 |
| Cloudflare security blog | news | ✅ | 8 |
| CVE Crowd | buzz | ✅ | 15 |
| CVE Crowd | buzz | ✅ | 15 |
| ZoomEye | buzz | ✅ | 5 |
| securityvulnerability.io trending | buzz | ✅ | 18 |
| Intruder cvemon | buzz | ✅ | 8 |
| Vulmon trends | buzz | ✅ | 26 |
| FediSecFeeds | signal | ✅ | 175 |
| 0xMarcio trending public PoCs | signal | ✅ | 46 |
| CISA KEV | feed | ✅ | 18 |
| CERT/CC vulnerability notes | feed | ✅ | 4 |
| GitHub Security Lab advisories | feed | ✅ | 5 |
| Full Disclosure mailing list | feed | ✅ | 15 |
| oss-security mailing list | feed | ✅ | 130 |
| OpenCVE latest | feed | ✅ | 20 |
