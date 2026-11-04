# Watchtower Night Report — 2026-11-04
**Cycle:** Night | **Generated:** 2026-11-04 03:09 UTC
**Sources checked:** 21/21 | **KEV additions (30 days):** 13

---

## 🔴 CRITICAL

### 🔄 Ivanti Connect Secure Zero-Day Chain
**Product:** Ivanti Connect Secure | **CVE:** CVE-2026-104935, CVE-2026-118527 | **CVSS:** 8.6 | **Threat score:** 10/10 (was 9) | **Popularity:** 5.4/10 (1/7 newsrooms, 2/5 trending lists)

**Since 2026-11-01:** SSVC exploitation unknown -> active; CVSS assigned: 4.3

CVE-2026-104935 allows unauthenticated remote command execution via authentication bypass. CVE-2026-118527 allows authenticated attackers to upload files to known locations. Both are part of an active attack chain and have been added to CISA KEV.

**Why it matters:** Organizations using Ivanti Connect Secure are exposed to full system compromise by unauthenticated remote attackers.

**Signals:** CISA KEV since 2026-10-13 · EPSS 0.89 · SSVC exploitation: active · trending: CVE Crowd, Intruder cvemon

**Mitigation:**
- Apply patches for versions 25.1.3.0 and 25.1.1.3/22.8R2.6
- Review system logs for unauthorized file uploads
- Restrict management interface access

**Covered by:** BleepingComputer — 2026-11-02 Ivanti patches two more Connect Secure zero-days chained in attacks | SecurityWeek — 2026-11-02 Ivanti Patches Two More Zero-Days Exploited in Connect Secure Attack Chain | Rapid7 blog — 2026-11-02 Additional Ivanti Connect Secure zero-days exploited in the wild (CVE-2026-111357, CVE-2026-118527)

---

### 📰 Siemens SIMATIC IoT2050 Unauthenticated RCE
**Product:** Siemens SIMATIC IoT2050 Advanced | **CVE:** CVE-2026-58115 | **CVSS:** 10 | **Threat score:** 9/10 | **Popularity:** 5.4/10 (1/7 newsrooms, 2/5 trending lists)

The vulnerability exists in versions prior to V4.3.4.1 running Industrial OS with Node-RED. Attackers can create malicious flows to plant backdoors or execute code. It is rated CVSS 10.

**Why it matters:** Industrial operators using these IoT gateways are vulnerable to complete device takeover and potential lateral movement into OT networks.

**Signals:** EPSS 0.01 · SSVC exploitation: none · trending: CVE Crowd, Vulmon trends

**Mitigation:**
- Update to version V4.3.4.1 or later
- Disable the Node-RED HTTP interface if not required
- Isolate IoT devices from public internet access

**Covered by:** The Hacker News — 2026-11-03 Attackers Exploit Critical Siemens IoT2050 Flaw to Plant Remote Command Backdoors

---

## 🟠 HIGH

### 📰 CryptoPayment Gateway WordPress Plugin RCE
**Product:** CryptoPayment Gateway WordPress Plugin | **CVE:** CVE-2026-81648 | **CVSS:** 10 | **Threat score:** 8/10 | **Popularity:** 5.4/10 (1/7 newsrooms, 2/5 trending lists)

Versions 1.2.1 through 1.2.2 fail to apply authorization checks on administrative endpoints. This allows for arbitrary file deletion and configuration overwrites. Public PoCs are available.

**Why it matters:** WordPress site administrators using this plugin risk the theft of cryptocurrency wallet credentials and server-side file manipulation.

**Signals:** EPSS 0.01 · SSVC exploitation: poc · trending: CVE Crowd, Vulmon trends

**Mitigation:**
- Update the plugin to a version beyond 1.2.2
- Audit server files for unauthorized deletions or modifications
- Rotate wallet credentials if the plugin was exposed

**Covered by:** The Hacker News — 2026-11-03 Attackers Target Unpatched CryptoPayment Gateway Flaw That Can Expose Wallet Credentials

---

## 🟡 MEDIUM

### 📰 Google Chrome Use-After-Free (CVE-2026-118306)
**Product:** Google Chrome | **CVE:** CVE-2026-118306 | **CVSS:** 9.6 | **Threat score:** 6/10 | **Popularity:** 5.4/10 (0/7 newsrooms, 3/5 trending lists)

The flaw exists in versions prior to 156.0.8078.73 and is triggered via a specially crafted HTML page. While Chromium labels the severity as Critical, there are currently no public PoCs or reports of active exploitation. A patch has been released to address the memory management issue.

**Why it matters:** Users of outdated Chrome browsers are exposed to remote attackers who could gain full system control by tricking them into visiting a malicious website.

**Signals:** EPSS 0.00 · SSVC exploitation: none · trending: Intruder cvemon, Vulmon trends, securityvulnerability.io trending

**Mitigation:**
- Update Google Chrome to version 156.0.8078.73 or later
- Enable automatic browser updates
- Use a security-hardened browser profile

---

### 📰 Android SMS 'of Death' DoS
**Product:** Google Android | **CVE:** CVE-2026-58882 | **CVSS:** Not specified | **Threat score:** 5/10 | **Popularity:** 6.3/10 (2/7 newsrooms, 2/5 trending lists)

The vulnerability is located in WapPushOverSms.java and triggers an out-of-bounds read. It requires no user interaction to execute. Google has addressed this in the November 2026 security update.

**Why it matters:** Android users with unpatched devices can be remotely crashed by a malicious SMS, leading to a denial of service.

**Signals:** EPSS 0.00 · trending: CVE Crowd, Vulmon trends

**Mitigation:**
- Install the November 2026 Android security update
- Keep system apps updated via the Google Play Store

**Covered by:** BleepingComputer — 2026-10-31 New Android SMS of Death exploit can remotely crash unpatched phones | SecurityWeek — 2026-11-03 Android’s November 2026 Updates Patch Over 200 Vulnerabilities

---

## 📋 Noted

- **CVE-2025-8088** (win.rar GmbH WinRAR): Path traversal vulnerability allowing arbitrary code execution via malicious archives.
- **CVE-2026-9198** (IBM Langflow OSS): Unauthenticated remote code execution via auto-login bypass and code validation.
- **CVE-2026-102764** (BeyondTrust Remote Support): Improper origin validation allowing unauthenticated file upload to RCE.
- **CVE-2026-63030** (WordPress): REST API route confusion and SQL injection leading to remote code execution.
- **CVE-2025-1974** (kubernetes ingress-nginx): RCE escalation in the admission controller for attackers with pod network access.
- **CVE-2026-93674** (IBM Langflow OSS): Remote code execution due to improper neutralization of OS command elements.
- **CVE-2026-7873** (IBM Langflow OSS): Authenticated code injection via the code validation endpoint.
- **CVE-2026-10134** (IBM Langflow OSS): Unauthenticated server-side RCE via PythonCodeStructuredTool in public flows.
- **CVE-2026-110264** (GitLab): Unauthenticated RCE via integer overflow when compiling regular expressions.
- **CVE-2026-110193** (IBM Langflow OSS): Authenticated RCE via the Agentic Assistant using unblocked code patterns.
- **CVE-2026-104339** (IBM Langflow OSS): Remote code execution due to improper neutralization of OS command elements.
- **CVE-2026-116606** (Barracuda Email Security Gateway): Authentication bypass allowing unauthenticated global configuration restore.
- **CVE-2026-111560** (Barracuda Appliances): Authenticated OS command injection via the timezone configuration field.
- **CVE-2026-106378** (Google Chrome): Sandbox privilege elevation on macOS allowing code execution outside the sandbox.
- **CVE-2026-110192** (IBM Langflow OSS): Authenticated information disclosure due to insufficiently protected credentials.
- **CVE-2026-58868** (Google Android): Heap buffer overflow in FrameDecoder allowing remote code execution.
- **CVE-2026-58876** (Google Android): Use-after-free memory safety issue allowing remote code execution.
- **CVE-2026-58936** (Google Android): Use-after-free memory corruption in pngset.c allowing remote code execution.
- **CVE-2021-33044** (Dahua IP Cameras/Devices): Identity authentication bypass during the login process via malicious packets.
- **CVE-2021-33045** (Dahua IP Cameras/Devices): Identity authentication bypass during the login process via malicious packets.
- **CVE-2025-54236** (Adobe Commerce): Improper input validation allowing session takeover without user interaction.
- **CVE-2026-42208** (BerriAI litellm): Unauthenticated SQL injection in Proxy API key verification.
- **CVE-2026-110447** (Collabora Online CODE Server): OS command injection in proxy.php allowing remote code execution.
- **CVE-2026-48356** (Adobe Commerce): Unrestricted upload of dangerous file types leading to arbitrary code execution.
- **CVE-2026-86950** (Apple iOS/iPadOS/macOS): Out-of-bounds write in CoreGraphics allowing arbitrary code execution via crafted files.
- **CVE-2026-102489** (Zammad): Session hijack vulnerability leading to remote code execution.
- **CVE-2026-102490** (Zammad): Local privilege escalation to root for users with filesystem write privileges.
- **CVE-2026-68820** (Microsoft Windows): Use-after-free in WinSock driver allowing local privilege elevation.
- **CVE-2024-39717** (Versa Director): Malicious file upload via the Change Favicon option for administrative users.
- **CVE-2026-96654** (Plex Media Server): URL injection allowing attackers to call other plugins' functions with custom parameters.

## Index

Every CVE of today's findings; later digests check it so they do not repeat themselves.

| CVE | Finding | Score | First seen |
|---|---|---|---|
| CVE-2026-104935 | Ivanti Connect Secure Zero-Day Chain | 10 | 2026-11-01 |
| CVE-2026-118527 | Ivanti Connect Secure Zero-Day Chain | 10 | 2026-11-01 |
| CVE-2026-58115 | Siemens SIMATIC IoT2050 Unauthenticated RCE | 9 | 2026-11-04 |
| CVE-2026-81648 | CryptoPayment Gateway WordPress Plugin RCE | 8 | 2026-11-04 |
| CVE-2026-118306 | Google Chrome Use-After-Free (CVE-2026-118306) | 6 | 2026-11-04 |
| CVE-2026-58882 | Android SMS 'of Death' DoS | 5 | 2026-11-04 |

## Source Coverage

| Source | Type | Status | Items |
|---|---|---|---|
| The Hacker News | news | ✅ | 107 |
| BleepingComputer | news | ✅ | 44 |
| SecurityWeek | news | ✅ | 102 |
| Krebs on Security | news | ✅ | 2 |
| Schneier on Security | news | ✅ | 7 |
| Rapid7 blog | news | ✅ | 8 |
| Cloudflare security blog | news | ✅ | 6 |
| CVE Crowd | buzz | ✅ | 18 |
| CVE Crowd | buzz | ✅ | 18 |
| ZoomEye | buzz | ✅ | 5 |
| securityvulnerability.io trending | buzz | ✅ | 18 |
| Intruder cvemon | buzz | ✅ | 8 |
| Vulmon trends | buzz | ✅ | 26 |
| FediSecFeeds | signal | ✅ | 160 |
| 0xMarcio trending public PoCs | signal | ✅ | 40 |
| CISA KEV | feed | ✅ | 13 |
| CERT/CC vulnerability notes | feed | ✅ | 5 |
| GitHub Security Lab advisories | feed | ✅ | 5 |
| Full Disclosure mailing list | feed | ✅ | 15 |
| oss-security mailing list | feed | ✅ | 156 |
| OpenCVE latest | feed | ✅ | 20 |
