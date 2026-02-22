# Vulnerability Intelligence Report — 2026-02-16 Morning

---

## 📰 Chrome Zero-Day Exploited in the Wild (CVE-2026-2441)

**Threat Score:** 8
**Affected Technology:** Google Chrome / Chromium-based browsers
**CVE:** CVE-2026-2441
**CVSS:** High (not yet scored)

### Summary
Google released emergency updates to fix a high-severity use-after-free vulnerability in the CSS component of Chromium. The flaw allows a remote attacker to potentially exploit heap corruption via a crafted HTML page. Google confirmed exploitation in the wild, making this the first Chrome zero-day patched in 2026. All Chromium-based browsers (Edge, Opera, Brave) are affected.

### Why It Matters
Chromium powers the vast majority of enterprise web browsers. Any zero-day with confirmed wild exploitation against a rendering engine component is an immediate patching priority across 100k+ endpoints.

### Discovery
**First seen at:** bleepingcomputer.com
**How found:** Google security advisory + CISA KEV addition on Feb 17
**Latency:** On-time

### Sources
- https://www.bleepingcomputer.com/news/security/google-patches-first-chrome-zero-day-exploited-in-attacks-this-year/
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog

---

## 📰 BeyondTrust RCE Under Active Exploitation — CISA 3-Day Deadline (CVE-2026-1731)

**Threat Score:** 9
**Affected Technology:** BeyondTrust Remote Support (RS) & Privileged Remote Access (PRA)
**CVE:** CVE-2026-1731
**CVSS:** 9.9

### Summary
CISA ordered federal agencies to patch a critical pre-authentication OS command injection vulnerability in BeyondTrust RS/PRA within three days. The flaw (CVSS 9.9) allows unauthenticated remote attackers to execute OS commands in the context of the site user. A public PoC was published, and active exploitation has been confirmed since at least Feb 12. CISA KEV added it on Feb 13 with a Feb 16 deadline. Known to be used in ransomware campaigns.

### Why It Matters
BeyondTrust remote access products are deployed across enterprise environments for privileged access management. Pre-auth RCE with CVSS 9.9 and active exploitation means any exposed instance is already a target.

### Discovery
**First seen at:** bleepingcomputer.com
**How found:** CISA KEV alert + BleepingComputer coverage
**Latency:** On-time

### Sources
- https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-beyondtrust-flaw-within-three-days/
- https://www.bleepingcomputer.com/news/security/critical-beyondtrust-rce-flaw-now-exploited-in-attacks-patch-now/
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog

---

## 📰 Infostealer Malware Now Targeting OpenClaw AI Agent Secrets

**Threat Score:** 6
**Affected Technology:** OpenClaw (self-hosted AI agent framework)
**CVE:** Not yet assigned
**CVSS:** N/A

### Summary
Information-stealing malware families have been observed specifically targeting OpenClaw configuration files containing API keys, authentication tokens, and other secrets. With the rapid adoption of OpenClaw, its local configuration files have become a high-value target alongside traditional browser credential stores.

### Why It Matters
OpenClaw is increasingly deployed in enterprise environments. Stolen API keys can provide access to LLM providers, messaging platforms, and internal systems — a new lateral movement vector through AI infrastructure.

### Discovery
**First seen at:** bleepingcomputer.com
**How found:** BleepingComputer exclusive report
**Latency:** On-time

### Sources
- https://www.bleepingcomputer.com/news/security/infostealer-malware-found-stealing-openclaw-secrets-for-first-time/

---

## 📋 Noted

- **No CVE** — Eurail B.V.: Stolen traveler data from earlier breach now for sale on dark web.
- **No CVE** — Washington Hotel Japan: Ransomware infection disclosed; business data exposed.

---

## 📡 Source Coverage

**Sources checked:** 90/90
**Sources with findings:** 5

| Status | Source | Notes |
|--------|--------|-------|
| ✅ | bleepingcomputer.com | 3 findings (Chrome 0day, BeyondTrust, OpenClaw infostealers) |
| ✅ | cisa.gov | BeyondTrust KEV deadline, Chrome KEV |
| ✅ | thehackernews.com | BeyondTrust coverage |
| ✅ | securityweek.com | BeyondTrust coverage |
| ✅ | nvd.nist.gov | CVE-2026-2441, CVE-2026-1731 |
| ✅ | All remaining sources | Checked, nothing new in scope |
