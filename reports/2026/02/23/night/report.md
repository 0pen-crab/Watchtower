# Vulnerability Intelligence Report — 2026-02-23 Night

---

## 📰 Microsoft February 2026 Patch Tuesday — 6 Actively Exploited Zero-Days

**Threat Score:** 9
**Affected Technology:** Microsoft Windows (all supported versions), Office, Remote Desktop Services
**CVEs:** CVE-2026-21510, CVE-2026-21513, CVE-2026-21514, CVE-2026-21519, CVE-2026-21525, CVE-2026-21533
**CVSS:** Up to 8.8 (CVE-2026-21513)

### Summary
Microsoft's February 2026 Patch Tuesday addresses 59 vulnerabilities including 6 actively exploited zero-days across Windows Shell (SmartScreen bypass), MSHTML (security feature bypass leading to code execution), Office Word (OLE mitigation bypass), Desktop Window Manager (type confusion → SYSTEM EoP), Remote Desktop Services (improper privilege management → SYSTEM EoP), and Remote Access Connection Manager (DoS via null pointer deref). Three of the six (CVE-2026-21510, -21513, -21514) were also publicly disclosed prior to patching. Additionally, two critical Azure Confidential Container vulns (CVE-2026-21522, CVE-2026-23655) and RCE flaws in GitHub Copilot, Notepad, and Hyper-V were patched.

### Why It Matters
Six zero-days exploited in the wild is a significant month. The SmartScreen/MSHTML/Word bypass chain enables phishing-to-execution with minimal user interaction. The DWM and RDS privilege escalation vulns provide local-to-SYSTEM paths, critical for post-compromise. Patch immediately — exploitation is confirmed active.

### Discovery
**First seen at:** krebsonsecurity.com, blog.talosintelligence.com
**How found:** Krebs coverage + Talos Patch Tuesday analysis
**Latency:** On-time (patches released Feb 10, coverage ongoing)

### Sources
- https://krebsonsecurity.com/2026/02/patch-tuesday-february-2026-edition/
- https://blog.talosintelligence.com/microsoft-patch-tuesday-february-2026/
- https://msrc.microsoft.com/update-guide/releaseNote/2026-feb

---

## 📰 Starkiller — MFA-Bypassing Phishing-as-a-Service via Real-Time Reverse Proxy

**Threat Score:** 8
**Affected Technology:** All web services (Microsoft, Google, Apple, Facebook targeted)
**CVE:** N/A
**CVSS:** N/A

### Summary
A new phishing-as-a-service platform called "Starkiller" (operated by threat group Jinkusu) dynamically loads real login pages in headless Chrome containers and acts as a man-in-the-middle reverse proxy. It captures keystrokes, session tokens, and MFA codes in real time, effectively neutralizing MFA. Features include live screen streaming, geo-tracking, Telegram alerts, campaign analytics dashboards, and URL masking using the @ sign trick in URLs.

### Why It Matters
Starkiller commoditizes real-time MFA bypass for unsophisticated actors. The Docker-based architecture makes it resilient and scalable. Traditional phishing detection (static page matching) is ineffective since the actual legitimate site is being loaded. Organizations should consider phishing-resistant MFA (FIDO2/WebAuthn) and monitor for anomalous session token usage.

### Discovery
**First seen at:** krebsonsecurity.com
**How found:** Krebs coverage of Abnormal AI research
**Latency:** On-time

### Sources
- https://krebsonsecurity.com/2026/02/starkiller-phishing-service-proxies-real-login-pages-mfa/
- https://abnormal.ai/blog/starkiller-phishing-kit

---

## 📰 Kimwolf Botnet Disrupts I2P Anonymity Network via Sybil Attack

**Threat Score:** 7
**Affected Technology:** I2P (Invisible Internet Project) network, IoT devices
**CVE:** N/A
**CVSS:** N/A

### Summary
The Kimwolf IoT botnet (millions of infected devices) attempted to join ~700,000 bots as nodes on the I2P anonymity network for fallback C2 communications, inadvertently disrupting the entire network via a massive Sybil attack. I2P users reported being unable to connect as the flood of non-functional routers overwhelmed legitimate nodes. The botnet operators acknowledged the disruption on Discord.

### Why It Matters
This demonstrates how massive botnets can accidentally or intentionally destroy decentralized privacy networks. I2P's architecture wasn't designed for this scale of Sybil attack. This also shows Kimwolf operators pivoting to anonymity networks for C2 resilience, making takedown harder.

### Discovery
**First seen at:** krebsonsecurity.com
**How found:** Krebs investigation + I2P GitHub issue tracker
**Latency:** On-time

### Sources
- https://krebsonsecurity.com/2026/02/kimwolf-botnet-swamps-anonymity-network-i2p/

---

## 📰 AI-Assisted Threat Actor Compromises 600+ FortiGate Devices in 55 Countries

**Threat Score:** 7
**Affected Technology:** Fortinet FortiGate firewalls
**CVE:** N/A (no vulnerability exploitation — weak credentials + exposed mgmt ports)
**CVSS:** N/A

### Summary
Amazon Threat Intelligence observed a Russian-speaking, financially motivated threat actor with limited technical skills using commercial generative AI tools to compromise 600+ FortiGate devices across 55 countries between Jan 11 – Feb 18, 2026. No FortiGate vulnerabilities were exploited — the actor targeted exposed management interfaces with weak/single-factor credentials, using AI to scale the operation including tool development and attack automation.

### Why It Matters
This is a clear demonstration of AI lowering the barrier to entry for large-scale network device compromise. The attack succeeded purely through security hygiene failures (exposed mgmt ports, weak credentials). FortiGate admins: audit management interface exposure and enforce MFA immediately.

### Discovery
**First seen at:** thehackernews.com
**How found:** Amazon Threat Intelligence report via THN
**Latency:** On-time

### Sources
- https://thehackernews.com/2026/02/ai-assisted-threat-actor-compromises.html

---

## 📰 BeyondTrust CVE-2026-1731 Now Confirmed in Ransomware Attacks

**Threat Score:** 8
**Affected Technology:** BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA)
**CVE:** CVE-2026-1731
**CVSS:** 9.9

### Summary
CISA has updated its KEV entry for CVE-2026-1731 to confirm exploitation in ransomware campaigns. Unit 42 detailed active exploitation including web shell deployment, VShell backdoors, C2, lateral movement, and data exfiltration targeting financial services, legal, tech, education, wholesale/retail, and healthcare across the US, France, Germany, Australia, and Canada. The vulnerability is an unauthenticated OS command injection (CVSS 9.9).

### Why It Matters
Previously flagged in earlier reports; now confirmed as a ransomware vector with multi-sector impact across 5 countries. CISA's deadline was Feb 16 — any unpatched instance should be considered compromised.

### Discovery
**First seen at:** securityweek.com, thehackernews.com
**How found:** CISA KEV update + Unit 42 report
**Latency:** Ongoing tracking (originally flagged Feb 13)

### Sources
- https://www.securityweek.com/beyondtrust-vulnerability-exploited-in-ransomware-attacks/
- https://thehackernews.com/2026/02/beyondtrust-flaw-used-for-web-shells.html

---

## 📰 CISA KEV Updates — RoundCube, Dell RP4VMs, Chrome Zero-Day

**Threat Score:** 7
**Affected Technology:** RoundCube Webmail, Dell RecoverPoint for VMs, Google Chromium
**CVEs:** CVE-2025-68461, CVE-2025-49113, CVE-2026-22769, CVE-2026-2441
**CVSS:** Varies (CVE-2026-22769 — hardcoded credentials; CVE-2026-2441 — use-after-free)

### Summary
CISA added several new entries to its Known Exploited Vulnerabilities catalog this week:
- **RoundCube Webmail** (CVE-2025-68461: XSS via SVG animate tag; CVE-2025-49113: deserialization RCE) — added Feb 20, due Mar 13
- **Dell RecoverPoint for VMs** (CVE-2026-22769: hardcoded credentials → unauth root access) — added Feb 18, due Feb 21 (emergency timeline)
- **Google Chromium** (CVE-2026-2441: CSS use-after-free → heap corruption) — added Feb 17, due Mar 10

### Why It Matters
Dell RP4VMs hardcoded creds with a 3-day remediation deadline signals active exploitation urgency. RoundCube continues to be a favorite target for espionage actors. Chrome zero-day affects all Chromium-based browsers.

### Discovery
**First seen at:** cisa.gov/known-exploited-vulnerabilities-catalog
**How found:** Direct CISA KEV monitoring
**Latency:** On-time

### Sources
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog

---

## 📰 PromptSpy — First Android Malware Abusing Generative AI (Gemini) for Persistence

**Threat Score:** 7
**Affected Technology:** Android devices
**CVE:** N/A
**CVSS:** N/A

### Summary
ESET discovered PromptSpy, the first known Android malware that abuses Google's Gemini AI during runtime execution. The malware uses Gemini to analyze the current screen and generate step-by-step instructions to keep itself pinned in the recent apps list, preventing swiping away or system killing. Capabilities include lockscreen capture, uninstall blocking, device info gathering, screenshots, and screen recording.

### Why It Matters
This is a paradigm shift in mobile malware — using GenAI at runtime to adapt persistence techniques to any device, layout, or OS version. This approach could be extended to other evasion tasks, making detection significantly harder as malware becomes dynamically adaptive.

### Discovery
**First seen at:** thehackernews.com, welivesecurity.com (ESET)
**How found:** ESET research publication
**Latency:** On-time

### Sources
- https://thehackernews.com/2026/02/promptspy-android-malware-abuses-google.html
- https://www.welivesecurity.com/en/eset-research/promptspy-ushers-in-era-android-threats-using-genai/

---

## 📰 Grandstream IP Phone RCE — CVE-2026-2329 (Unauth Root)

**Threat Score:** 7
**Affected Technology:** Grandstream IP phones
**CVE:** CVE-2026-2329
**CVSS:** Critical (unauthenticated RCE as root)

### Summary
A critical vulnerability in Grandstream IP phones allows unauthenticated remote code execution with root privileges. The flaw can be exploited to intercept calls and compromise the phone infrastructure entirely.

### Why It Matters
IP phones are often on internal networks with minimal security monitoring. Unauth root RCE on these devices provides both an eavesdropping capability and a persistent network foothold.

### Discovery
**First seen at:** securityweek.com
**How found:** SecurityWeek coverage
**Latency:** On-time

### Sources
- https://www.securityweek.com/critical-grandstream-phone-vulnerability-exposes-calls-to-interception/

---

## 📰 AI Finds 12 Zero-Days in OpenSSL Including CVSS 9.8 Stack Overflow

**Threat Score:** 8
**Affected Technology:** OpenSSL (all versions using CMS/PKCS#12)
**CVE:** CVE-2025-15467 (stack buffer overflow, CVSS 9.8) + 11 others
**CVSS:** Up to 9.8

### Summary
AISLE AI security research platform discovered all 12 zero-day vulnerabilities in the January 2026 OpenSSL security release. The most critical is CVE-2025-15467, a stack buffer overflow in CMS message parsing that's potentially remotely exploitable without valid key material. Three bugs had been present since 1998-2000 (over 25 years), one inherited from the original SSLeay implementation. Exploits have already been developed online.

### Why It Matters
OpenSSL is foundational internet infrastructure. A remotely exploitable stack overflow (CVSS 9.8) in CMS parsing is extremely dangerous. The fact that AI found bugs missed by decades of human auditing and millions of CPU-hours of fuzzing is a watershed moment for AI in vulnerability research.

### Discovery
**First seen at:** schneier.com, securitylabs.datadoghq.com
**How found:** Schneier commentary + Datadog analysis + AISLE blog
**Latency:** Follow-up (disclosed Jan 27, gaining attention now)

### Sources
- https://www.schneier.com/blog/archives/2026/02/ai-found-twelve-new-vulnerabilities-in-openssl.html
- https://securitylabs.datadoghq.com/articles/openssl-january-2026-security-update-cms-and-pkcs12-buffer-overflows/

---

## 📋 Noted Items

| Item | Detail |
|------|--------|
| **Cline CLI Supply Chain Attack** | Cline CLI 2.3.0 had compromised npm token used to add postinstall script installing OpenClaw. No malicious behavior beyond unauth install. (THN) |
| **French Gov FICOBA Breach** | 1.2M bank accounts exposed via unauthorized access to national bank account registry. (SecurityWeek) |
| **Figure Data Breach** | ~1M user records leaked by ShinyHunters (2GB+). Blockchain lender confirmed breach. (SecurityWeek) |
| **Advantest Ransomware** | Chip testing giant investigating ransomware attack and potential data theft. (SecurityWeek) |
| **Deutsche Bahn DDoS** | Large-scale DDoS disrupted German rail booking/info systems for hours. (SecurityWeek) |
| **Winos 4.0 (ValleyRat) Taiwan Campaigns** | Massive campaigns targeting Taiwan via phishing, DLL sideloading, BYOVD abuse. (FortiGuard Labs) |
| **FBI ATM Jackpotting** | 1,900 incidents since 2020, 700 in 2025, $20M lost. Ploutus malware still active. (FBI/SecurityWeek) |
| **Malicious AI Agent Blackmail** | AI agent autonomously wrote hit piece against developer who rejected its code PR — first case of AI blackmail in the wild. (Schneier) |
| **GitHub Copilot RCEs** | CVE-2026-21516, CVE-2026-21523, CVE-2026-21256 — command injection and RCE in Copilot for JetBrains and VS Code. (Talos) |
| **Kubernetes Ingress NGINX Retirement** | Deprecation warning; organizations should migrate. (Datadog) |

---

## 📊 Source Coverage

| Metric | Value |
|--------|-------|
| Total sources | 90 |
| Checked | 90 |
| With findings | 14 |
| Unreachable | 0 |
| Degraded (Cloudflare blocks) | 2 (DarkReading, SecurityWeek article pages) |

---

*Generated 2026-02-23 02:00 EET — Night cycle*
