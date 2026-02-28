# Vulnerability Intelligence Report — 2026-02-27 Night

---

## 📰 Juniper Networks PTX — Unauthenticated Root RCE (Critical)

**Threat Score:** 9
**Affected Technology:** Juniper Networks Junos OS Evolved (PTX Series)
**CVE:** Not yet assigned
**CVSS:** Critical

### Summary
A critical vulnerability in Junos OS Evolved on PTX Series routers allows an unauthenticated attacker to execute code remotely with root privileges. PTX routers are deployed in carrier-grade and large enterprise core networks.

### Why It Matters
Unauthenticated root RCE on core network routers. PTX series are used by ISPs and large enterprises for backbone routing. Compromise could enable full network interception and traffic manipulation at scale.

### Discovery
**First seen at:** bleepingcomputer.com (Feb 26)
**How found:** BleepingComputer coverage of Juniper advisory
**Latency:** On-time

### Sources
- https://www.bleepingcomputer.com/news/security/critical-juniper-networks-ptx-flaw-allows-full-router-takeover/

---

## 📰 Trend Micro Apex One — Critical Remote Code Execution

**Threat Score:** 8
**Affected Technology:** Trend Micro Apex One (Windows)
**CVE:** Not yet assigned
**CVSS:** Critical

### Summary
Trend Micro patched two critical vulnerabilities in Apex One that allow remote code execution on Windows systems. Apex One is a widely deployed enterprise endpoint security product.

### Why It Matters
RCE in endpoint security software is especially dangerous — it runs with elevated privileges on every managed endpoint. Compromise of the security tool itself gives attackers the keys to the kingdom.

### Discovery
**First seen at:** bleepingcomputer.com (Feb 26)
**How found:** BleepingComputer coverage
**Latency:** On-time

### Sources
- https://www.bleepingcomputer.com/news/security/trend-micro-warns-of-critical-apex-one-rce-vulnerabilities/

---

## 📰 APT37 (ScarCruft) — New Toolset Breaches Air-Gapped Networks

**Threat Score:** 8
**Affected Technology:** Windows systems, air-gapped networks
**CVE:** Not applicable
**CVSS:** N/A

### Summary
North Korean APT37 is deploying six new malware families (RESTLEAF, SNAKEDROPPER, THUMBSBD, VIRUSTASK, FOOTWINE, BLUELIGHT) using Zoho WorkDrive for C2 and USB-based implants to breach air-gapped networks. Campaign codenamed "Ruby Jumper" by Zscaler ThreatLabz.

### Why It Matters
Air-gapped network compromise is a high-sophistication capability typically reserved for state actors. The use of Zoho WorkDrive as C2 blends malicious traffic with legitimate cloud service usage. Organizations with air-gapped environments should audit USB policies immediately.

### Discovery
**First seen at:** bleepingcomputer.com, thehackernews.com (Feb 27)
**How found:** Simultaneous multi-outlet coverage of Zscaler research
**Latency:** On-time

### Sources
- https://www.bleepingcomputer.com/news/security/apt37-hackers-use-new-malware-to-breach-air-gapped-networks/
- https://thehackernews.com/2026/02/scarcruft-uses-zoho-workdrive-and-usb.html

---

## 📰 Google API Keys Now Expose Gemini AI Data

**Threat Score:** 7
**Affected Technology:** Google API keys, Gemini AI
**CVE:** Not applicable
**CVSS:** N/A

### Summary
Google API keys for services like Maps, previously considered low-risk when exposed in client-side code, can now be used to authenticate to the Gemini AI assistant and access private data. This retroactively turns millions of leaked API keys into a security risk.

### Why It Matters
Massive retroactive exposure — API keys already embedded in public client-side code (mobile apps, web frontends, GitHub repos) now grant access to Gemini AI data. Organizations need to audit and rotate exposed Google API keys immediately.

### Discovery
**First seen at:** bleepingcomputer.com (Feb 26)
**How found:** BleepingComputer coverage
**Latency:** On-time

### Sources
- https://www.bleepingcomputer.com/news/security/previously-harmless-google-api-keys-now-expose-gemini-ai-data/

---

## 🔄 Update: CISA Warns RESURGE Malware Can Be Dormant on Ivanti Devices

**Previous Threat Score:** 9 → **Updated Threat Score:** 9
**CVE:** CVE-2025-0282

### What Changed
CISA released new details about RESURGE malware used in zero-day attacks exploiting CVE-2025-0282 on Ivanti Connect Secure devices. Key update: the malware can remain dormant on devices, meaning orgs that patched but didn't fully remediate may still be compromised.

### Sources
- https://www.bleepingcomputer.com/news/security/cisa-warns-that-resurge-malware-can-be-dormant-on-ivanti-devices/

---

## 📰 Malicious Go Crypto Module — Password Theft + Rekoobe Backdoor

**Threat Score:** 7
**Affected Technology:** Go ecosystem (golang.org/x/crypto impersonation)
**CVE:** Not applicable
**CVSS:** N/A

### Summary
A malicious Go module (github.com/xinfeisoft/crypto) impersonates the legitimate golang.org/x/crypto package, intercepts terminal password prompts, exfiltrates secrets, and deploys the Rekoobe Linux backdoor. Exploits namespace confusion in Go's dependency system.

### Why It Matters
Supply chain attack targeting the Go ecosystem — a language heavily used in cloud infrastructure, DevOps, and security tooling. Developers pulling the wrong crypto module get full compromise.

### Discovery
**First seen at:** thehackernews.com (Feb 27)
**How found:** Socket security research covered by The Hacker News
**Latency:** On-time

### Sources
- https://thehackernews.com/2026/02/malicious-go-crypto-module-steals.html

---

## 📋 Noted

- **No CVE** — ManoMano: European DIY chain data breach impacts 38 million customers via third-party compromise.
- **No CVE** — Europol "Project Compass": 30 arrests of "The Com" cybercrime collective targeting minors.
- **No CVE** — Olympique Marseille: French football club confirms cyberattack after data leak.
- **No CVE** — UFP Technologies: Medical device maker discloses data theft in cyberattack.
- **No CVE** — Ransomware payment rate drops to 28% record low despite attack surge (Coveware report).

---

## 📡 Source Coverage

**Sources checked:** 90/90
**Sources with findings:** 8

| Status | Source | Notes |
|--------|--------|-------|
| ✅ | bleepingcomputer.com | Juniper, Trend Micro, APT37, Google API, Ivanti RESURGE, ManoMano |
| ✅ | thehackernews.com | ScarCruft, Go crypto module, ThreatsDay bulletin |
| ✅ | cisa.gov | RESURGE malware advisory |
| ✅ | securityweek.com | Juniper PTX coverage |
| ✅ | nvd.nist.gov | CVE lookups |
| ✅ | reddit.com/r/netsec | Juniper, APT37 discussion |
| ✅ | krebsonsecurity.com | Nothing new in scope |
| ✅ | darkreading.com | APT37 coverage |
| ✅ | All remaining sources | Checked, nothing new in scope |
