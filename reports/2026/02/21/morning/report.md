# Vulnerability Intelligence Report — 2026-02-21 Morning

---

## 📰 AI-Assisted Hacker Compromises 600+ FortiGate Devices in 55 Countries

**Threat Score:** 8
**Affected Technology:** Fortinet FortiGate firewalls
**CVE:** None (weak credentials + exposed mgmt ports, no vulnerability exploited)
**CVSS:** N/A

### Summary
Amazon Threat Intelligence revealed a Russian-speaking, financially motivated actor used commercial generative AI to compromise 600+ FortiGate firewalls across 55 countries (Jan 11 – Feb 18, 2026). No vulnerabilities exploited — the campaign targeted exposed management ports and weak single-factor credentials. The attacker had limited technical skills but used AI to automate tool development and scaling.

### Why It Matters
Paradigm shift: unsophisticated actor used commercial AI to breach 600 firewalls in 5 weeks. The attack surface is misconfiguration, not a CVE — harder to patch away. AI amplification means similar campaigns will accelerate.

### Discovery
**First seen at:** Amazon Threat Intelligence, thehackernews.com, bleepingcomputer.com
**How found:** Amazon CISO report + simultaneous multi-outlet coverage
**Latency:** On-time

### Sources
- https://thehackernews.com/2026/02/ai-assisted-threat-actor-compromises.html
- https://www.bleepingcomputer.com/news/security/amazon-ai-assisted-hacker-breached-600-fortigate-firewalls-in-5-weeks/

---

## 📰 OpenClaw Security Vulnerabilities and Misconfiguration Risks

**Threat Score:** 6
**Affected Technology:** OpenClaw (AI agent framework)
**CVE:** Not yet assigned
**CVSS:** N/A

### Summary
SecurityWeek reported ongoing security issues with OpenClaw despite rapid patches and OpenAI-backed foundation transition. Combined with this week's infostealers (Feb 16) and Cline supply chain attack (Feb 17), three incidents in one week around AI agent infrastructure.

### Why It Matters
OpenClaw is deployed in our own infrastructure. Three security incidents in one week signals the AI agent ecosystem is a primary attack target. Prioritize hardening.

### Discovery
**First seen at:** securityweek.com
**How found:** SecurityWeek coverage
**Latency:** On-time

### Sources
- https://www.securityweek.com/openclaw-security-issues-continue-as-secureclaw-open-source-tool-debuts/

---

## 📰 Predator Spyware Hooks iOS SpringBoard to Hide Surveillance

**Threat Score:** 5
**Affected Technology:** iOS (via Predator/Intellexa spyware)
**CVE:** Not disclosed
**CVSS:** N/A

### Summary
Intellexa's Predator now hooks iOS SpringBoard to hide recording indicators while streaming camera/mic feeds. No visual indication of surveillance for victims.

### Why It Matters
CISO awareness: targeted executives could have enterprise communications and credentials compromised with no visible indicators.

### Discovery
**First seen at:** bleepingcomputer.com
**How found:** BleepingComputer coverage
**Latency:** On-time

### Sources
- https://www.bleepingcomputer.com/news/security/predator-spyware-hooks-ios-springboard-to-hide-mic-camera-activity/

---

## 📋 Noted

- **No CVE** — Arkanix Stealer: AI-assisted infostealer experiment on dark web forums. Short-lived PoC.
- **No CVE** — Google trade secret theft: Former engineers indicted for exfiltrating to Iran.

---

## 📡 Source Coverage

**Sources checked:** 90/90
**Sources with findings:** 7

| Status | Source | Notes |
|--------|--------|-------|
| ✅ | bleepingcomputer.com | FortiGate AI attack, Predator, Arkanix |
| ✅ | thehackernews.com | FortiGate AI attack |
| ✅ | securityweek.com | OpenClaw security issues |
| ✅ | aws.amazon.com/blogs/security | FortiGate campaign (Amazon TI) |
| ✅ | cisa.gov | Nothing new |
| ✅ | nvd.nist.gov | Nothing new |
| ✅ | reddit.com/r/netsec | FortiGate discussion |
| ✅ | All remaining sources | Checked, nothing new in scope |
