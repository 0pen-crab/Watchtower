# Watchtower Night Report — 2026-11-11
**Cycle:** Night | **Generated:** 2026-11-11 03:13 UTC
**Sources checked:** 21/21 | **KEV additions (30 days):** 17

---

## 🔴 CRITICAL

### 📰 IBM Aspera Faspex Authorization Bypass
**Product:** IBM Aspera Faspex | **CVE:** CVE-2026-123218 | **CVSS:** 9.8 | **Threat score:** 10/10 | **Popularity:** 6.3/10 (2/7 newsrooms, 2/5 trending lists)

The flaw exists in versions 5.0.0 through 5.0.19. CISA has added the vulnerability to its KEV catalog, confirming active exploitation in the wild. A patch is available from IBM.

**Why it matters:** Organizations using Aspera Faspex for high-speed file transfers are at risk of total system compromise by a malicious authorized user.

**Signals:** CISA KEV since 2026-11-09 · EPSS 0.01 · SSVC exploitation: active · trending: CVE Crowd, Vulmon trends · registries: CISA KEV 2026-11-09

**Mitigation:**
- Update Aspera Faspex to the latest patched version
- Audit administrative account logs for unauthorized privilege escalation

**Covered by:** The Hacker News — 2026-11-10 CISA Warns of Active Exploitation of OpenSSH, GPUStack, FreeSWITCH, and IBM Flaws | SecurityWeek — 2026-11-10 IBM Aspera Faspex, SignalWire FreeSwitch Vulnerabilities Exploited in Attacks

---

### 🔄 SignalWire FreeSWITCH RCE (CVE-2026-116779)
**Product:** SignalWire FreeSWITCH | **CVE:** CVE-2026-116779 | **CVSS:** 9.8 | **Threat score:** 10/10 (was 10) | **Popularity:** 5.4/10 (1/7 newsrooms, 2/5 trending lists)

**Since 2026-11-10:** new newsroom reports

The flaw exists in the sofia_presence_handle_sip_i_message function, which improperly processes chat protocol selectors. This allows an attacker to reach switch_api_execute and run administrative commands. The vulnerability is currently being exploited in the wild and has been added to CISA KEV.

**Why it matters:** Organizations using FreeSWITCH for telecom infrastructure are exposed to full system compromise via unauthenticated remote requests.

**Signals:** CISA KEV since 2026-11-09 · EPSS 0.02 · SSVC exploitation: active · trending: CVE Crowd, Vulmon trends · registries: CISA KEV 2026-11-09

**Mitigation:**
- Update FreeSWITCH to version 1.11.3 or later
- Restrict inbound SIP MESSAGE traffic to trusted peers
- Monitor FreeSWITCH API logs for unauthorized command execution

**Covered by:** SecurityWeek — 2026-11-10 IBM Aspera Faspex, SignalWire FreeSwitch Vulnerabilities Exploited in Attacks

---

### 📰 GPUStack Authentication Bypass (CVE-2026-102895)
**Product:** GPUStack | **CVE:** CVE-2026-102895 | **CVSS:** 9.8 | **Threat score:** 10/10 | **Popularity:** 5.4/10 (1/7 newsrooms, 2/5 trending lists)

The vulnerability stems from the API treating requests appearing to originate from 127.0.0.1 as the built-in administrator by default. Attackers can trigger this via a reverse proxy or by manipulating the X-GPUStack-Real-IP header. CISA has confirmed active exploitation of this flaw.

**Why it matters:** Administrators of AI GPU clusters are at risk of total cluster takeover and unauthorized resource provisioning.

**Signals:** CISA KEV since 2026-11-09 · EPSS 0.01 · SSVC exploitation: active · trending: CVE Crowd, Vulmon trends · registries: CISA KEV 2026-11-09

**Mitigation:**
- Update GPUStack to version 2.2.0 or later
- Enable force_auth_localhost in the configuration
- Configure reverse proxies to strip or validate X-GPUStack-Real-IP headers

**Covered by:** The Hacker News — 2026-11-10 CISA Warns of Active Exploitation of OpenSSH, GPUStack, FreeSWITCH, and IBM Flaws

---

### 🔄 OpenSSH 'SSHole' Auth Bypass
**Product:** OpenBSD OpenSSH | **CVE:** CVE-2026-123158 | **CVSS:** 8.1 | **Threat score:** 9/10 (was 9) | **Popularity:** 8.1/10 (4/7 newsrooms, 3/5 trending lists)

**Since 2026-11-07:** EPSS 0.010 -> 0.165

The vulnerability allows any password between 256 and 1024 characters to succeed under specific configurations. It is now listed in CISA KEV and shows active exploitation. A patch is available in version 10.6p2.

**Why it matters:** Users of Alpine Linux or other musl-based systems without PAM are exposed to full system compromise via unauthorized SSH access.

**Signals:** CISA KEV since 2026-11-09 · EPSS 0.17 · SSVC exploitation: active · public PoC · trending: CVE Crowd, Vulmon trends, securityvulnerability.io trending · registries: CISA KEV 2026-11-09

**Mitigation:**
- Update OpenSSH to 10.6p2 or later
- Implement PAM where possible
- Restrict SSH access via firewall

**Covered by:** The Hacker News — 2026-11-10 CISA Warns of Active Exploitation of OpenSSH, GPUStack, FreeSWITCH, and IBM Flaws | Schneier on Security — 2026-11-10 New OpenSSH Vulnerability

---

### 📰 Google Chrome XML Use-After-Free
**Product:** Google Chrome | **CVE:** CVE-2026-125350 | **CVSS:** 8.8 | **Threat score:** 9/10 | **Popularity:** 7.6/10 (2/7 newsrooms, 4/5 trending lists)

The flaw is triggered via a crafted HTML page and executes code within the browser sandbox. It has been added to CISA KEV due to active exploitation in the wild. Google has released a security update to address this zero-day.

**Why it matters:** Any user visiting a malicious website can have arbitrary code executed on their machine.

**Signals:** CISA KEV since 2026-11-10 · SSVC exploitation: active · public PoC · trending: CVE Crowd, Intruder cvemon, Vulmon trends, securityvulnerability.io trending · registries: CISA KEV 2026-11-10

**Mitigation:**
- Update Google Chrome to version 157.0.8103.50 or later
- Enable automatic browser updates

**Covered by:** The Hacker News — 2026-11-10 Google Issues Chrome Security Update for Eighth Actively Exploited Zero-Day of 2026 | SecurityWeek — 2026-11-10 Chrome Update Patches Exploited XML Zero-Day, Eighth This Year

---

### 🔄 Barracuda ESG/ADC Root Access Chain
**Product:** Barracuda Email Security Gateway / Load Balancer ADC | **CVE:** CVE-2026-116606, CVE-2026-111560 | **CVSS:** 9.3 | **Threat score:** 9/10 (was 6) | **Popularity:** 6.3/10 (3/7 newsrooms, 1/5 trending lists)

**Since 2026-11-05:** added to CISA KEV 2026-11-10; SSVC exploitation none -> active

CVE-2026-116606 allows unauthenticated configuration restores, while CVE-2026-111560 enables root command injection via timezone settings. Both are now listed in CISA KEV with confirmed active exploitation. Updates to version 9.4.0.030 or later are required.

**Why it matters:** Attackers can gain full administrative control over email gateways and load balancers, compromising network traffic and mail flow.

**Signals:** CISA KEV since 2026-11-10 · EPSS 0.02 · SSVC exploitation: active · trending: CVE Crowd · registries: CISA KEV 2026-11-10

**Mitigation:**
- Update Barracuda ESG to 9.4.0.030 or later
- Restrict management interface access to trusted IPs

**Covered by:** BleepingComputer — 2026-11-10 Hackers now exploit critical Barracuda ESG flaws to gain root access

---

### 📰 N-able N-central 'Able2Shell' Account Takeover
**Product:** N-able N-central | **CVE:** CVE-2026-18577, CVE-2026-18556 | **CVSS:** 8.2 | **Threat score:** 9/10 | **Popularity:** 5.4/10 (3/7 newsrooms, 0/5 trending lists)

The issues involve an initial bypass and a subsequent incomplete patch (CVE-2026-18577) that failed to resolve the risk. Both are listed in CISA KEV and are actively exploited. N-able recently took its cloud platform offline following the disclosure of multiple zero-days.

**Why it matters:** Attackers can gain full administrative control over RMM (Remote Monitoring and Management) infrastructure, potentially pivoting to all managed endpoints.

**Signals:** CISA KEV since 2026-08-03 · EPSS 0.15 · SSVC exploitation: active

**Mitigation:**
- Update N-central to the latest version beyond 2026.3.1
- Review administrative access logs for unauthorized logins

**Covered by:** The Hacker News — 2026-11-10 N-able Takes N-central Cloud Offline After Researcher Discloses 33 Zero-Days with PoC Exploits | BleepingComputer — 2026-11-09 N-able takes cloud platform offline after 30+ "zero-days" published | SecurityWeek — 2026-11-10 N-able Takes N-central Offline as Researcher Drops Over 30 Zero-Days

---

## 🟠 HIGH

### 📰 Microsoft Outlook Spoofing Vulnerability
**Product:** Microsoft Office Outlook | **CVE:** CVE-2026-124194 | **CVSS:** 6.5 | **Threat score:** 8/10 | **Popularity:** 7.6/10 (4/7 newsrooms, 2/5 trending lists)

The product UI fails to warn users of unsafe actions, enabling spoofing attacks. This flaw was patched as part of the November 2026 Patch Tuesday and is currently being exploited. A public PoC exists.

**Why it matters:** Enterprise users of Microsoft 365 Apps and Office LTSC 2021 are susceptible to phishing and social engineering attacks.

**Signals:** CISA KEV since 2026-11-10 · SSVC exploitation: active · public PoC · trending: CVE Crowd, Intruder cvemon · registries: CISA KEV 2026-11-10

**Mitigation:**
- Apply November 2026 Microsoft security updates
- Educate users on identifying spoofed emails

**Covered by:** BleepingComputer — 2026-11-10 Microsoft November 2026 Patch Tuesday fixes 1,235 flaws, Outlook zero-day | SecurityWeek — 2026-11-10 Exploited Outlook Zero-Day Among 1,094 Flaws Patched by Microsoft | Krebs on Security — 2026-11-10 Microsoft Fixes Nearly 1,100 Security Vulnerabilities | Rapid7 blog — 2026-11-10 Patch Tuesday - November 2026

---

### 📰 SAP NetWeaver and Web Dispatcher 'ICM2SHELL/ProxyGate'
**Product:** SAP NetWeaver AS ABAP / SAP Web Dispatcher | **CVE:** CVE-2026-76964, CVE-2026-89126 | **CVSS:** 10 | **Threat score:** 8/10 | **Popularity:** 6.3/10 (3/7 newsrooms, 1/5 trending lists)

These flaws, nicknamed ICM2SHELL and ProxyGate, stem from insufficient validation of network traffic. Successful exploitation leads to full system compromise. SAP has released critical patches for both components.

**Why it matters:** Unauthenticated attackers can remotely execute arbitrary code on core SAP infrastructure, impacting confidentiality and integrity of enterprise data.

**Signals:** EPSS 0.00 · trending: CVE Crowd

**Mitigation:**
- Apply the latest security patches from SAP
- Restrict network access to the Internet Communication Manager (ICM) and Web Dispatcher

**Covered by:** The Hacker News — 2026-11-10 SAP Patches Four CVSS 10.0 Flaws, Including Two Enabling Remote Code Execution | BleepingComputer — 2026-11-10 SAP patches ICM2SHELL and PROXYGATE maximum severity flaws | SecurityWeek — 2026-11-10 SAP Patches Critical ICM2SHELL, ProxyGate Vulnerabilities

---

## 📋 Noted

- **CVE-2026-9198** (Langflow): Unauthenticated remote code execution vulnerability used in automated attacks.
- **CVE-2025-43529** (Apple Safari/iOS/iPadOS): Use-after-free vulnerability allowing arbitrary code execution via crafted web content.
- **CVE-2026-46300** (Linux Kernel): Kernel vulnerability in skbuff coalescing allowing root escalation.
- **CVE-2026-96652** (Plex Media Server): SSRF vulnerability via the /player/timeline endpoint.
- **CVE-2026-96655** (Plex Media Server): Authenticated SSRF vulnerability via the transcode universal path.
- **CVE-2026-96656** (Plex Media Server): Arbitrary file write vulnerability allowing code execution by admin users.
- **CVE-2026-63030** (WordPress): REST API route confusion and SQL injection leading to remote code execution.
- **CVE-2026-20320** (Cisco BroadWorks): XXE vulnerability in the OCI XML Parser allowing sensitive information disclosure.
- **CVE-2026-110264** (GitLab): Integer overflow in regular expression compilation allowing unauthenticated RCE.
- **CVE-2026-104353** (Adobe Campaign Classic): OS command injection vulnerability allowing arbitrary code execution.
- **CVE-2026-110193** (IBM Langflow OSS): RCE vulnerability allowing authenticated users to execute OS commands.
- **CVE-2026-104339** (IBM Langflow OSS): Unauthenticated remote code execution via improper neutralization of OS commands.
- **CVE-2026-104350** (Adobe Campaign Classic): Reflected cross-site scripting vulnerability requiring user interaction.
- **CVE-2026-104351** (Adobe Campaign Classic): Code injection vulnerability allowing arbitrary code execution by low-privileged users.
- **CVE-2026-115252** (Confection WordPress Plugin): Unauthenticated RCE via insecure writing of settings to a PHP file.
- **CVE-2026-118331** (Google Chrome): Use-after-free in FileAPI allowing RCE outside the sandbox.
- **CVE-2026-118344** (Google Chrome): Use-after-free in Layout allowing RCE inside the sandbox.
- **CVE-2026-118348** (Google Chrome): Integer overflow in Skia allowing RCE outside the sandbox.
- **CVE-2026-89103** (SAP Gateway): Broken access control allowing unauthenticated attackers to perform unauthorized actions.
- **CVE-2026-120017** (SAP NetWeaver): Authentication bypass in SAML2 Service Provider allowing user impersonation.
- **CVE-2026-110192** (IBM Langflow OSS): Information disclosure vulnerability due to insufficiently protected credentials.
- **CVE-2026-111760** (Git): Vulnerability allowing code execution during recursive clones of malicious repositories.
- **CVE-2025-3248** (Langflow): Unauthenticated RCE via the /api/v1/validate/code endpoint.
- **CVE-2025-31324** (SAP NetWeaver): Unauthenticated arbitrary file upload in Visual Composer development server.
- **CVE-2025-8088** (WinRAR): Path traversal vulnerability allowing arbitrary code execution via malicious archives.
- **CVE-2023-2868** (Barracuda Email Security Gateway): Remote command injection via improperly sanitized .tar files.
- **CVE-2026-105133** (AhsayCBS): Improper authentication in the API allowing remote access.
- **CVE-2026-105134** (AhsayCBS): Remote OS command injection in the Replication Receiver component.
- **CVE-2026-102764** (BeyondTrust Remote Support): Improper origin validation allowing unauthenticated file upload and RCE.
- **CVE-2025-14174** (Google Chrome): Out-of-bounds memory access in ANGLE on macOS.

## Index

Every CVE of today's findings; later digests check it so they do not repeat themselves.

| CVE | Finding | Score | First seen |
|---|---|---|---|
| CVE-2026-123218 | IBM Aspera Faspex Authorization Bypass | 10 | 2026-11-11 |
| CVE-2026-116779 | SignalWire FreeSWITCH RCE (CVE-2026-116779) | 10 | 2026-11-10 |
| CVE-2026-102895 | GPUStack Authentication Bypass (CVE-2026-102895) | 10 | 2026-11-11 |
| CVE-2026-123158 | OpenSSH 'SSHole' Auth Bypass | 9 | 2026-11-07 |
| CVE-2026-125350 | Google Chrome XML Use-After-Free | 9 | 2026-11-11 |
| CVE-2026-116606 | Barracuda ESG/ADC Root Access Chain | 9 | 2026-11-05 |
| CVE-2026-111560 | Barracuda ESG/ADC Root Access Chain | 9 | 2026-11-05 |
| CVE-2026-18577 | N-able N-central 'Able2Shell' Account Takeover | 9 | 2026-11-11 |
| CVE-2026-18556 | N-able N-central 'Able2Shell' Account Takeover | 9 | 2026-11-11 |
| CVE-2026-124194 | Microsoft Outlook Spoofing Vulnerability | 8 | 2026-11-11 |
| CVE-2026-76964 | SAP NetWeaver and Web Dispatcher 'ICM2SHELL/ProxyGate' | 8 | 2026-11-11 |
| CVE-2026-89126 | SAP NetWeaver and Web Dispatcher 'ICM2SHELL/ProxyGate' | 8 | 2026-11-11 |

## Source Coverage

| Source | Type | Status | Items |
|---|---|---|---|
| The Hacker News | news | ✅ | 130 |
| BleepingComputer | news | ✅ | 103 |
| SecurityWeek | news | ✅ | 103 |
| Krebs on Security | news | ✅ | 3 |
| Schneier on Security | news | ✅ | 5 |
| Rapid7 blog | news | ✅ | 10 |
| Cloudflare security blog | news | ✅ | 6 |
| CVE Crowd | buzz | ✅ | 42 |
| CVE Crowd | buzz | ✅ | 42 |
| ZoomEye | buzz | ✅ | 5 |
| securityvulnerability.io trending | buzz | ✅ | 18 |
| Intruder cvemon | buzz | ✅ | 12 |
| Vulmon trends | buzz | ✅ | 26 |
| FediSecFeeds | signal | ✅ | 30 |
| 0xMarcio trending public PoCs | signal | ✅ | 44 |
| CISA KEV | feed | ✅ | 17 |
| CERT/CC vulnerability notes | feed | ✅ | 4 |
| GitHub Security Lab advisories | feed | ✅ | 0 |
| Full Disclosure mailing list | feed | ✅ | 15 |
| oss-security mailing list | feed | ✅ | 105 |
| OpenCVE latest | feed | ✅ | 20 |
