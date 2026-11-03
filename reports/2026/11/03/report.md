# Watchtower Night Report — 2026-11-03
**Cycle:** Night | **Generated:** 2026-11-03 03:08 UTC
**Sources checked:** 21/21 | **KEV additions (30 days):** 12

---

## 🔴 CRITICAL

### 🔄 GitLab RCE (CVE-2026-97229)
**Product:** GitLab CE/EE | **CVE:** CVE-2026-97229 | **CVSS:** 10 | **Threat score:** 10/10 (was 9) | **Popularity:** 7.6/10 (3/7 newsrooms, 3/5 trending lists)

**Since 2026-10-30:** new newsroom reports

The vulnerability affects multiple versions of GitLab CE/EE. It is currently listed in CISA KEV with active, automatable exploitation reported. Recent reports indicate over 1,000 servers are currently targeted in ongoing RCE attacks.

**Why it matters:** Unauthenticated remote attackers can gain full control over the GitLab server. Organizations hosting their own GitLab instances are at high risk.

**Signals:** CISA KEV since 2026-10-29 · EPSS 0.27 · SSVC exploitation: active · trending: CVE Crowd, Intruder cvemon, Vulmon trends · registries: CISA KEV 2026-10-29

**Mitigation:**
- Update to versions 19.2.8, 19.3.5, or 19.4.2
- Audit CI/CD configurations for suspicious regular expressions
- Restrict access to GitLab instances via VPN or IP allowlists

**Covered by:** BleepingComputer — 2026-11-02 Over 1,000 GitLab servers vulnerable to ongoing RCE attacks

---

### 🔄 Ivanti Connect Secure Zero-Days
**Product:** Ivanti Connect Secure | **CVE:** CVE-2026-111357, CVE-2026-118527 | **CVSS:** 7 | **Threat score:** 9/10 (was 9) | **Popularity:** 7.6/10 (4/7 newsrooms, 2/5 trending lists)

**Since 2026-11-01:** new newsroom reports

CVE-2026-111357 allows privilege escalation to root via mishandled DSCache configuration data. CVE-2026-118527 is an additional zero-day identified as part of the same attack chain. Both are listed in CISA KEV and have been actively exploited.

**Why it matters:** Attackers can gain full administrative (root) access to the VPN gateway. This allows for total network compromise and credential theft.

**Signals:** CISA KEV since 2026-10-30 · EPSS 0.01 · SSVC exploitation: active · trending: Intruder cvemon, Vulmon trends · registries: CISA KEV 2026-10-30

**Mitigation:**
- Apply the latest security patches from Ivanti
- Perform a factory reset of the appliance if compromise is suspected
- Monitor logs for unusual dsinvoked broker activity

**Covered by:** BleepingComputer — 2026-11-02 Ivanti patches two more Connect Secure zero-days chained in attacks | SecurityWeek — 2026-11-02 Ivanti Patches Two More Zero-Days Exploited in Connect Secure Attack Chain | Rapid7 blog — 2026-11-02 Additional Ivanti Connect Secure zero-days exploited in the wild (CVE-2026-111357, CVE-2026-118527)

---

## 🟠 HIGH

### 📰 IBM Langflow OSS (ARTEX) RCE
**Product:** IBM Langflow OSS | **CVE:** CVE-2026-93680, CVE-2026-110186 | **CVSS:** 9.8 | **Threat score:** 8/10 | **Popularity:** 6.3/10 (3/7 newsrooms, 1/5 trending lists)

The vulnerabilities affect versions 1.0.0 through 1.12.8 of the Langflow OSS framework. Reports indicate that Chinese threat actors are using these flaws in automated attacks against hundreds of organizations. The flaws allow for unauthenticated remote code execution.

**Why it matters:** Organizations deploying Langflow for AI orchestration are exposed to full server takeover. Attackers can steal sensitive data or use the server as a pivot point.

**Signals:** EPSS 0.02 · SSVC exploitation: none · trending: CVE Crowd

**Mitigation:**
- Update Langflow OSS to a version beyond 1.12.8
- Ensure the application is not exposed directly to the public internet
- Implement strong authentication and network segmentation

**Covered by:** The Hacker News — 2026-11-02 Critical Langflow Flaws Could Let Unauthenticated Attackers Run Code on Servers | BleepingComputer — 2026-11-02 Chinese hackers use ARTEX AI in automated attacks against 200 orgs | Rapid7 blog — 2026-10-23 Metasploit Wrap Up: Langflow, MongoDB, and More

---

## 📋 Noted

- **CVE-2026-104935** (Ivanti Connect Secure): Authentication bypass allows remote unauthenticated command execution.
- **CVE-2026-9198** (IBM Langflow OSS): Unauthenticated RCE via auto-login bypass and code validation.
- **CVE-2026-102764** (BeyondTrust Remote Support): Improper origin validation allows unauthenticated file operations and RCE.
- **CVE-2026-63030** (WordPress): REST API route confusion and SQL injection lead to RCE.
- **CVE-2025-1974** (kubernetes ingress-nginx): Unauthenticated attacker on pod network can achieve RCE in the controller.
- **CVE-2026-93674** (IBM Langflow OSS): Remote code execution due to improper neutralization of OS command elements.
- **CVE-2026-10134** (IBM Langflow OSS): Unauthenticated server-side RCE via PythonCodeStructuredTool in public flows.
- **CVE-2026-7873** (IBM Langflow OSS): Authenticated code injection in the code validation endpoint.
- **CVE-2026-110264** (GitLab): Unauthenticated RCE via integer overflow when compiling regular expressions.
- **CVE-2026-113380** (Signal RingRTC): FSM queue saturation allows a caller to block local hang-ups.
- **CVE-2026-110193** (IBM Langflow OSS): Low-privileged authenticated users can execute OS commands via Agentic Assistant.
- **CVE-2026-104339** (IBM Langflow OSS): Remote code execution due to improper neutralization of OS command elements.
- **CVE-2026-93577** (GitLab): Authenticated RCE via integer overflow in CI/CD regular expression compilation.
- **CVE-2026-89078** (GitLab): Authenticated RCE via double free when parsing CI/CD regular expressions.
- **CVE-2026-15723** (GitLab): LDAP injection allows authenticated account takeover when SAML and LDAP auto-linking are enabled.
- **CVE-2026-118306** (Google Chrome): Memory corruption in FileSystem allows remote code execution outside the sandbox.
- **CVE-2026-106378** (Google Chrome): Sandbox privilege elevation allows code execution outside the sandbox on macOS.
- **CVE-2026-110192** (IBM Langflow OSS): Remote authenticated attackers can obtain sensitive credentials.
- **CVE-2026-112212** (GitLab): HTTP request smuggling allows unauthenticated poisoning of OAuth/OIDC discovery documents.
- **CVE-2026-112706** (Apple iOS/iPadOS/tvOS): Permissions issue may allow an app to access sensitive user data.
- **CVE-2026-115560** (unknown product): Vulnerability related to php2shell protections.
- **CVE-2026-58882** (Google Android): Integer overflow in WapPushOverSms allows remote denial of service via SMS.
- **CVE-2021-33044** (Dahua IP Cameras/Devices): Identity authentication bypass allows attackers to hijack devices.
- **CVE-2021-33045** (Dahua IP Cameras/Devices): Identity authentication bypass allows attackers to hijack devices.
- **CVE-2025-54236** (Adobe Commerce): Improper input validation allows unauthenticated session takeover.
- **CVE-2026-42208** (BerriAI litellm): Unauthenticated SQL injection in Proxy API key verification.
- **CVE-2026-76460** (Cisco ISE): Insufficient authentication control on an API endpoint allows remote bypass.
- **CVE-2026-110447** (Collabora Online CODE Server): OS command injection in proxy.php allows remote code execution.
- **CVE-2026-48356** (Adobe Commerce): Unrestricted upload of dangerous file types allows RCE via user interaction.
- **CVE-2026-86950** (Apple iOS/iPadOS/macOS): Out-of-bounds write in CoreGraphics allows arbitrary code execution via crafted files.

## Index

Every CVE of today's findings; later digests check it so they do not repeat themselves.

| CVE | Finding | Score | First seen |
|---|---|---|---|
| CVE-2026-97229 | GitLab RCE (CVE-2026-97229) | 10 | 2026-10-30 |
| CVE-2026-111357 | Ivanti Connect Secure Zero-Days | 9 | 2026-11-01 |
| CVE-2026-118527 | Ivanti Connect Secure Zero-Days | 9 | 2026-11-01 |
| CVE-2026-93680 | IBM Langflow OSS (ARTEX) RCE | 8 | 2026-11-03 |
| CVE-2026-110186 | IBM Langflow OSS (ARTEX) RCE | 8 | 2026-11-03 |

## Source Coverage

| Source | Type | Status | Items |
|---|---|---|---|
| The Hacker News | news | ✅ | 108 |
| BleepingComputer | news | ✅ | 34 |
| SecurityWeek | news | ✅ | 103 |
| Krebs on Security | news | ✅ | 2 |
| Schneier on Security | news | ✅ | 8 |
| Rapid7 blog | news | ✅ | 8 |
| Cloudflare security blog | news | ✅ | 7 |
| CVE Crowd | buzz | ✅ | 28 |
| CVE Crowd | buzz | ✅ | 28 |
| ZoomEye | buzz | ✅ | 5 |
| securityvulnerability.io trending | buzz | ✅ | 18 |
| Intruder cvemon | buzz | ✅ | 9 |
| Vulmon trends | buzz | ✅ | 26 |
| FediSecFeeds | signal | ✅ | 173 |
| 0xMarcio trending public PoCs | signal | ✅ | 46 |
| CISA KEV | feed | ✅ | 12 |
| CERT/CC vulnerability notes | feed | ✅ | 5 |
| GitHub Security Lab advisories | feed | ✅ | 5 |
| Full Disclosure mailing list | feed | ✅ | 15 |
| oss-security mailing list | feed | ✅ | 141 |
| OpenCVE latest | feed | ✅ | 20 |
