# Vulnerability Intelligence Report — 2026-02-18 Morning

---

## 📰 SmarterMail RCE Flaws Rapidly Weaponized — Ransomware Activity Confirmed (CVE-2026-24423 & CVE-2026-23760)

**Threat Score:** 9
**Affected Technology:** SmarterMail (email server)
**CVE:** CVE-2026-24423, CVE-2026-23760
**CVSS:** Critical (details pending)

### Summary
Two critical SmarterMail vulnerabilities are being rapidly weaponized. Underground Telegram channels shared exploit PoCs and stolen admin credentials within days of disclosure. Over 1,000 servers remain vulnerable. Exploitation tied to active ransomware campaigns.

### Why It Matters
Email servers are tier-1 internet-facing infrastructure. SmarterMail is deployed across thousands of organizations as an Exchange alternative. Ransomware-linked exploitation with public PoCs means active mass-exploitation.

### Discovery
**First seen at:** BleepingComputer (Flare research report)
**How found:** BleepingComputer coverage + Telegram channel monitoring by Flare
**Latency:** On-time

### Sources
- https://www.bleepingcomputer.com/news/security/telegram-channels-expose-rapid-weaponization-of-smartermail-flaws/

---

## 📰 Honeywell CCTV Authentication Bypass — Critical Infrastructure at Risk

**Threat Score:** 7
**Affected Technology:** Honeywell CCTV products (multiple models)
**CVE:** Not specified in coverage
**CVSS:** Critical

### Summary
CISA warned of a critical auth bypass in multiple Honeywell CCTV products allowing unauthorized access to camera feeds or account hijacking. Deployed across critical infrastructure facilities.

### Why It Matters
Auth bypass in critical infrastructure surveillance systems could enable physical security breaches or serve as a pivot into OT networks.

### Discovery
**First seen at:** bleepingcomputer.com
**How found:** CISA advisory monitoring
**Latency:** On-time

### Sources
- https://www.bleepingcomputer.com/news/security/critical-infra-honeywell-cctvs-vulnerable-to-auth-bypass-flaw/

---

## 📰 AI Platforms Abused as Covert C2 Channels

**Threat Score:** 5
**Affected Technology:** Grok (X/Twitter), Microsoft Copilot, AI assistants with web browsing
**CVE:** Not yet assigned
**CVSS:** N/A

### Summary
Researchers demonstrated AI assistants with web browsing capabilities can be abused to intermediate C2 communications, making malicious traffic appear as legitimate AI API calls — invisible to traditional network monitoring.

### Why It Matters
Novel C2 technique exploiting ubiquitous AI deployment. Traditional network detection won't flag AI platform traffic as malicious.

### Discovery
**First seen at:** bleepingcomputer.com
**How found:** Research publication coverage
**Latency:** On-time

### Sources
- https://www.bleepingcomputer.com/news/security/ai-platforms-can-be-abused-for-stealthy-malware-communication/

---

## 📰 Cline CLI Supply Chain Attack Installs OpenClaw on Developer Machines

**Threat Score:** 6
**Affected Technology:** Cline CLI (npm package), OpenClaw
**CVE:** Not yet assigned
**CVSS:** N/A

### Summary
Compromised npm publish token used to push Cline CLI v2.3.0 with postinstall script silently installing OpenClaw on developer machines. Unauthorized installation represents a supply chain compromise. Token revoked, malicious version pulled.

### Why It Matters
Supply chain attacks on developer tools continue escalating. Highlights OpenClaw's growing attack surface as both target and vector.

### Discovery
**First seen at:** thehackernews.com
**How found:** The Hacker News coverage of Cline advisory
**Latency:** On-time

### Sources
- https://thehackernews.com/2026/02/cline-cli-230-supply-chain-attack.html

---

## 📋 Noted

- **No CVE** — Figure Technology data breach: Nearly 1M accounts compromised by ShinyHunters.
- **No CVE** — Deutsche Bahn DDoS: Large-scale attack disrupted booking systems.
- **CW1226324** — Microsoft 365 Copilot DLP bypass: Bug since Jan 21 let Copilot summarize confidential emails. Fixed Feb 3.

---

## 📡 Source Coverage

**Sources checked:** 90/90
**Sources with findings:** 7

| Status | Source | Notes |
|--------|--------|-------|
| ✅ | bleepingcomputer.com | 3 findings (SmarterMail, Honeywell, AI C2) |
| ✅ | thehackernews.com | Cline supply chain attack |
| ✅ | securityweek.com | Deutsche Bahn, OpenClaw security |
| ✅ | cisa.gov | Honeywell advisory |
| ✅ | nvd.nist.gov | CVE lookups |
| ✅ | reddit.com/r/netsec | SmarterMail discussion |
| ✅ | reddit.com/r/cybersecurity | AI C2 discussion |
| ✅ | All remaining sources | Checked, nothing new in scope |
