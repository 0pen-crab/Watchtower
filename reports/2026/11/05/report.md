# Watchtower Night Report — 2026-11-05
**Cycle:** Night | **Generated:** 2026-11-05 03:10 UTC
**Sources checked:** 21/21 | **KEV additions (30 days):** 14

---

## 🔴 CRITICAL

### 🔄 PHP 'PHP2Shell' RCE
**Product:** PHP | **CVE:** CVE-2026-109619 | **CVSS:** 9.2 | **Threat score:** 10/10 (was 10) | **Popularity:** 7.6/10 (4/7 newsrooms, 2/5 trending lists)

**Since 2026-10-30:** public PoC appeared

The flaw occurs when global state is not correctly reset, allowing subsequent requests to branch on stale memory. It is actively exploited and listed in CISA KEV. A public PoC has now appeared, increasing the risk of widespread attacks.

**Why it matters:** Administrators of PHP-based web servers are exposed to full system compromise by unauthenticated remote attackers.

**Signals:** CISA KEV since 2026-10-26 · EPSS 1.00 · SSVC exploitation: active · public PoC · trending: Vulmon trends, ZoomEye · registries: CERT/CC vulnerability notes 2026-10-22, CISA KEV 2026-10-26

**Mitigation:**
- Apply emergency security patches from PHP
- Monitor for unusual child process spawning from web servers
- Implement a Web Application Firewall (WAF) to detect common RCE patterns

**Covered by:** The Hacker News — 2027-12-31 PHP2Shell: Two Unpatched Critical PHP RCE Flaws (CVSS 9.2) Trigger Emergency Security Alert | SecurityWeek — 2026-10-30 PHP2Shell Attacks Root Palo Alto Firewalls but Fail Against WordPress | Krebs on Security — 2026-10-23 Widespread PHP Flaw May Cause Many Site Outages Today | Cloudflare security blog — 2026-10-27 Introducing the Cloudflare PHP Capture the Flag challenge

---

### 🔄 GitLab RCE (CVE-2026-97229)
**Product:** GitLab CE/EE | **CVE:** CVE-2026-97229 | **CVSS:** 10 | **Threat score:** 10/10 (was 10) | **Popularity:** 7.0/10 (3/7 newsrooms, 2/5 trending lists)

**Since 2026-10-30:** EPSS 0.273 -> 0.652

The vulnerability affects multiple versions of GitLab CE/EE prior to 19.2.8, 19.3.5, and 19.4.2. It is actively exploited in the wild and listed in CISA KEV. EPSS scores have risen significantly as attacks continue against vulnerable servers.

**Why it matters:** Organizations hosting GitLab instances are at risk of total server takeover by unauthenticated attackers.

**Signals:** CISA KEV since 2026-10-29 · EPSS 0.65 · SSVC exploitation: active · trending: CVE Crowd, Vulmon trends · registries: CISA KEV 2026-10-29

**Mitigation:**
- Update GitLab to versions 19.2.8, 19.3.5, 19.4.2 or later
- Restrict access to CI/CD configuration interfaces where possible

**Covered by:** The Hacker News — 2026-10-30 CISA Adds Actively Exploited GitLab RCE and Cisco Firewall DoS Flaws to KEV | BleepingComputer — 2026-11-02 Over 1,000 GitLab servers vulnerable to ongoing RCE attacks | SecurityWeek — 2026-10-30 Max-Severity GitLab Vulnerability Exploited Against Alpine Linux

---

### 📰 WordPress Core RCE (CVE-2026-119977)
**Product:** WordPress Core | **CVE:** CVE-2026-119977 | **CVSS:** 8.1 | **Threat score:** 10/10 | **Popularity:** 7.0/10 (2/7 newsrooms, 3/5 trending lists)

The flaw affects WordPress versions 4.7 through 7.1.3 during the upgrade window. CISA has added this to KEV, confirming active exploitation in the wild. Attackers can execute arbitrary code on the server while a full-package upgrade is in progress.

**Why it matters:** Millions of WordPress sites are potentially exposed to full server compromise during software update cycles.

**Signals:** CISA KEV since 2026-11-03 · EPSS 0.01 · SSVC exploitation: active · trending: CVE Crowd, Intruder cvemon, Vulmon trends · registries: CISA KEV 2026-11-03

**Mitigation:**
- Update WordPress Core to the latest patched version
- Ensure updates are performed over secure, monitored connections
- Use a security plugin to monitor for unauthorized file changes in staging directories

**Covered by:** The Hacker News — 2026-11-04 CISA Confirms Hackers Exploiting WordPress Core Flaw During Software Upgrades | BleepingComputer — 2026-11-04 CISA flags WordPress RCE flaw as actively exploited in attacks

---

## 🟠 HIGH

### 📰 Android Remote Code Execution Flaws
**Product:** Google Android | **CVE:** CVE-2026-58868, CVE-2026-58876, CVE-2026-58936 | **CVSS:** Not specified | **Threat score:** 8/10 | **Popularity:** 6.3/10 (2/7 newsrooms, 2/5 trending lists)

The flaws include a heap buffer overflow in FrameDecoder.cpp and use-after-free issues in various components, including PNG processing. These vulnerabilities are patched in the November 2026 security update. Exploitation is possible remotely and does not require any user interaction.

**Why it matters:** Users of unpatched Android devices are exposed to complete system compromise by a remote attacker.

**Signals:** EPSS 0.00 · SSVC exploitation: none · trending: CVE Crowd, Vulmon trends

**Mitigation:**
- Apply the November 2026 Android security update
- Enable Google Play System Updates
- Keep all system applications updated

**Covered by:** The Hacker News — 2026-11-04 Google Issues Patches for Critical Android Flaw That Could Allow RCE Without User Interaction | SecurityWeek — 2026-11-03 Android’s November 2026 Updates Patch Over 200 Vulnerabilities

---

### 🔄 Google Chrome Use-After-Free (CVE-2026-118306)
**Product:** Google Chrome | **CVE:** CVE-2026-118306 | **CVSS:** 9.6 | **Threat score:** 8/10 (was 6) | **Popularity:** 5.4/10 (1/7 newsrooms, 2/5 trending lists)

**Since 2026-11-04:** public PoC appeared

The flaw exists in versions prior to 156.0.8078.73 and can be triggered via a crafted HTML page. A public proof-of-concept (PoC) has now emerged, increasing the risk of exploitation. Google has released a patch as part of Chrome version 157.

**Why it matters:** Users visiting a malicious website could have their system compromised by an attacker executing arbitrary code with high privileges.

**Signals:** EPSS 0.00 · SSVC exploitation: none · public PoC · trending: Intruder cvemon, securityvulnerability.io trending

**Mitigation:**
- Update Google Chrome to version 157 or later
- Enable automatic updates for the browser

**Covered by:** SecurityWeek — 2026-11-04 Chrome 157 Rolls Out With 213 Security Fixes, Seven Rated Critical

---

### 🔄 Linux Kernel TCP Use-After-Free
**Product:** Linux Kernel | **CVE:** CVE-2026-98432 | **CVSS:** 9.8 | **Threat score:** 7/10 (was 7) | **Popularity:** 6.3/10 (1/7 newsrooms, 3/5 trending lists)

**Since 2026-10-30:** new newsroom reports

The flaw involves the improper handling of inet_opt and ireq_opt during TCP SYN processing. Red Hat has issued patches for the 9.8-rated flaw, and Ubuntu has released fixes for testing. The issue can lead to remote code execution.

**Why it matters:** Servers running vulnerable Linux kernels are susceptible to remote memory corruption and potential takeover.

**Signals:** EPSS 0.01 · trending: CVE Crowd, Vulmon trends, securityvulnerability.io trending · registries: oss-security mailing list

**Mitigation:**
- Update the Linux kernel to the latest patched version
- Apply Red Hat or Ubuntu security updates immediately

**Covered by:** The Hacker News — 2026-11-03 Red Hat Patches 9.8-Rated Linux TCP RCE Flaw While Ubuntu Releases Fixes for Testing

---

### 📰 Zyxel GS1900 Series Out-of-Bounds Write
**Product:** Zyxel GS1900-10HP/16/24E Switches | **CVE:** CVE-2026-107441 | **CVSS:** 8.8 | **Threat score:** 7/10 | **Popularity:** 5.4/10 (1/7 newsrooms, 2/5 trending lists)

The vulnerability affects firmware versions through 2.90(AAHK.2)C0. Reports indicate this flaw was exploited as a zero-day to target nearly 1,000 network switches. Zyxel has released firmware updates to address the issue.

**Why it matters:** Attackers on the same local network can gain full control over critical network switching infrastructure.

**Signals:** EPSS 0.00 · trending: CVE Crowd, Vulmon trends

**Mitigation:**
- Update switch firmware to the latest available version
- Restrict access to the management interface via VLANs or ACLs

**Covered by:** BleepingComputer — 2026-11-04 Zyxel fixes zero-day exploited to hack nearly 1,000 network switches

---

## 🟡 MEDIUM

### 📰 Barracuda ESG and ADC Root Access Chain
**Product:** Barracuda Email Security Gateway (ESG) and Load Balancer ADC | **CVE:** CVE-2026-116606, CVE-2026-111560 | **CVSS:** 9.3 | **Threat score:** 6/10 | **Popularity:** 5.4/10 (3/7 newsrooms, 0/5 trending lists)

CVE-2026-116606 allows unauthenticated remote attackers to restore a crafted configuration archive. This can be chained with CVE-2026-111560, where an authenticated administrator (or someone who has bypassed authentication) can inject OS commands via the timezone field. Patches are available for affected ESG versions.

**Why it matters:** Attackers can bypass security controls and achieve full administrative control over email gateways and load balancers.

**Signals:** EPSS 0.01 · SSVC exploitation: none

**Mitigation:**
- Update Barracuda ESG to version 9.4.0.030 or later
- Apply latest security patches for Barracuda ADC appliances

**Covered by:** The Hacker News — 2026-11-03 Barracuda Flaws Could Be Chained to Bypass Authorization and Gain Root Access | BleepingComputer — 2026-11-03 Barracuda warns of critical flaws allowing root access to devices | SecurityWeek — 2026-11-04 Barracuda ESG Authentication Bypass Flaw Opens Path to Root

---

### 🔄 Android SMS 'of Death' DoS
**Product:** Google Android | **CVE:** CVE-2026-58882 | **CVSS:** Not specified | **Threat score:** 5/10 (was 5) | **Popularity:** 7.0/10 (3/7 newsrooms, 2/5 trending lists)

**Since 2026-11-04:** new newsroom reports

The vulnerability exists in WapPushOverSms.java and leads to an out-of-bounds read. Recent reports highlight that this is part of a broader set of critical patches released by Google. A patch is available in the November 2026 update.

**Why it matters:** Attackers can remotely cause a denial of service on Android devices by sending a specially crafted SMS.

**Signals:** EPSS 0.00 · trending: CVE Crowd, Vulmon trends

**Mitigation:**
- Apply the November 2026 Android security update
- Monitor for unexpected device reboots

**Covered by:** The Hacker News — 2026-11-04 Google Issues Patches for Critical Android Flaw That Could Allow RCE Without User Interaction

---

## 📋 Noted

- **CVE-2026-9198** (IBM Langflow OSS): Unauthenticated RCE via auto-login bypass and code validation.
- **CVE-2026-63030** (WordPress): RCE via REST API route confusion and SQL injection.
- **CVE-2026-7273** (Zyxel GS1900 Series): LAN-based unauthenticated RCE via stack-based buffer overflow.
- **CVE-2024-27834** (Apple Safari/iOS/iPadOS): Pointer Authentication bypass for attackers with arbitrary read/write capability.
- **CVE-2025-1974** (kubernetes ingress-nginx): RCE escalation for unauthenticated attackers with pod network access.
- **CVE-2026-93674** (IBM Langflow OSS): Remote code execution due to improper neutralization of OS command elements.
- **CVE-2026-7873** (IBM Langflow OSS): Authenticated OS command injection via the code validation endpoint.
- **CVE-2026-10134** (IBM Langflow OSS): Unauthenticated server-side RCE via PythonCodeStructuredTool in public flows.
- **CVE-2026-110264** (GitLab): Unauthenticated RCE via integer overflow during regular expression compilation.
- **CVE-2024-10441** (Synology BeeStation/DiskStation Manager): Remote code execution via improper output encoding in the system plugin daemon.
- **CVE-2026-110193** (IBM Langflow OSS): Low-privileged authenticated RCE via the Agentic Assistant.
- **CVE-2026-104339** (IBM Langflow OSS): Remote code execution due to improper neutralization of OS command elements.
- **CVE-2026-109593** (SonicWall GMS): Unauthenticated read of internal files in end-of-life software.
- **CVE-2026-109594** (SonicWall GMS): Authenticated SQL injection in end-of-life software.
- **CVE-2026-118331** (Google Chrome): Use-after-free in FileAPI allowing RCE outside the sandbox.
- **CVE-2026-118344** (Google Chrome): Use-after-free in Layout allowing RCE inside the sandbox.
- **CVE-2026-118348** (Google Chrome): Integer overflow in Skia allowing RCE outside the sandbox.
- **CVE-2026-106378** (Google Chrome): Sandbox privilege elevation on macOS.
- **CVE-2026-110192** (IBM Langflow OSS): Authenticated information disclosure due to unprotected credentials.
- **CVE-2026-109518** (Debian/Ubuntu APT): Root RCE via MitM attack using hard link reuse during package installation.
- **CVE-2026-120422** (Sogou Input Method): RCE via insecure HTTP configuration retrieval in SGTool.exe.
- **CVE-2021-33044** (Dahua IP Cameras/Devices): Identity authentication bypass during the login process.
- **CVE-2021-33045** (Dahua IP Cameras/Devices): Identity authentication bypass during the login process.
- **CVE-2025-54236** (Adobe Commerce): Improper input validation leading to session takeover.
- **CVE-2025-8088** (WinRAR): Path traversal allowing arbitrary code execution via malicious archives.
- **CVE-2026-42208** (BerriAI litellm): Unauthenticated SQL injection in Proxy API key verification.
- **CVE-2026-102764** (BeyondTrust Remote Support): Unauthenticated file operations via improper origin validation.
- **CVE-2026-110447** (Collabora Online CODE Server): Remote code execution via OS command injection in proxy.php.
- **CVE-2025-14174** (Google Chrome): Out-of-bounds memory access in ANGLE on macOS.
- **CVE-2026-48356** (Adobe Commerce): Unrestricted upload of dangerous file types leading to RCE.

## Index

Every CVE of today's findings; later digests check it so they do not repeat themselves.

| CVE | Finding | Score | First seen |
|---|---|---|---|
| CVE-2026-109619 | PHP 'PHP2Shell' RCE | 10 | 2026-10-30 |
| CVE-2026-97229 | GitLab RCE (CVE-2026-97229) | 10 | 2026-10-30 |
| CVE-2026-119977 | WordPress Core RCE (CVE-2026-119977) | 10 | 2026-11-05 |
| CVE-2026-58868 | Android Remote Code Execution Flaws | 8 | 2026-11-05 |
| CVE-2026-58876 | Android Remote Code Execution Flaws | 8 | 2026-11-05 |
| CVE-2026-58936 | Android Remote Code Execution Flaws | 8 | 2026-11-05 |
| CVE-2026-118306 | Google Chrome Use-After-Free (CVE-2026-118306) | 8 | 2026-11-04 |
| CVE-2026-98432 | Linux Kernel TCP Use-After-Free | 7 | 2026-10-30 |
| CVE-2026-107441 | Zyxel GS1900 Series Out-of-Bounds Write | 7 | 2026-11-05 |
| CVE-2026-116606 | Barracuda ESG and ADC Root Access Chain | 6 | 2026-11-05 |
| CVE-2026-111560 | Barracuda ESG and ADC Root Access Chain | 6 | 2026-11-05 |
| CVE-2026-58882 | Android SMS 'of Death' DoS | 5 | 2026-11-04 |

## Source Coverage

| Source | Type | Status | Items |
|---|---|---|---|
| The Hacker News | news | ✅ | 110 |
| BleepingComputer | news | ✅ | 55 |
| SecurityWeek | news | ✅ | 99 |
| Krebs on Security | news | ✅ | 2 |
| Schneier on Security | news | ✅ | 7 |
| Rapid7 blog | news | ✅ | 8 |
| Cloudflare security blog | news | ✅ | 6 |
| CVE Crowd | buzz | ✅ | 25 |
| CVE Crowd | buzz | ✅ | 25 |
| ZoomEye | buzz | ✅ | 5 |
| securityvulnerability.io trending | buzz | ✅ | 18 |
| Intruder cvemon | buzz | ✅ | 9 |
| Vulmon trends | buzz | ✅ | 26 |
| FediSecFeeds | signal | ✅ | 150 |
| 0xMarcio trending public PoCs | signal | ✅ | 44 |
| CISA KEV | feed | ✅ | 14 |
| CERT/CC vulnerability notes | feed | ✅ | 5 |
| GitHub Security Lab advisories | feed | ✅ | 0 |
| Full Disclosure mailing list | feed | ✅ | 15 |
| oss-security mailing list | feed | ✅ | 149 |
| OpenCVE latest | feed | ✅ | 20 |
