# Vulnerability Intelligence Report — 2026-03-04 Night

---

## 📰 Fake Laravel Packages on Packagist Deploy Cross-Platform RAT

**Threat Score:** 8
**Affected Technology:** PHP/Packagist ecosystem (Laravel)
**CVE:** Not applicable
**CVSS:** N/A

### Summary
Malicious PHP packages on Packagist impersonating Laravel utilities deploy a cross-platform RAT functional on Windows, macOS, and Linux. Packages "nhattuanbl/lara-helper", "nhattuanbl/simple-queue", and "nhattuanbl/lara-swagger" use control flow obfuscation and encoded payloads. The RAT is installed via a Composer dependency chain — lara-swagger pulls in lara-helper which contains the malware.

### Why It Matters
Laravel is one of the most popular PHP frameworks. Packagist is the primary dependency manager for the entire PHP ecosystem. Supply chain attacks via Composer dependencies can compromise any Laravel application that pulls these packages.

### Discovery
**First seen at:** thehackernews.com (Mar 4)
**How found:** Socket security research via The Hacker News
**Latency:** On-time

### Sources
- https://thehackernews.com/2026/03/fake-laravel-packages-on-packagist.html

---

## 🔄 Update: VMware Aria Operations CVE-2026-22719 — Federal Patch Deadline Set

**Previous Threat Score:** 9 → **Updated Threat Score:** 9
**CVE:** CVE-2026-22719

### What Changed
CISA set March 24 as the federal patch deadline. Additional analysis confirms the vulnerability is exploitable during support-assisted migration, meaning orgs that recently migrated or are planning migrations are at highest risk. Three CVEs total need patching: CVE-2026-22719 (RCE), CVE-2026-22720 (XSS), CVE-2026-22721 (privilege escalation).

### Sources
- https://thehackernews.com/2026/03/cisa-adds-actively-exploited-vmware.html

---

## 📰 Europol Takes Down Tycoon 2FA Phishing-as-a-Service Platform

**Threat Score:** 6
**Affected Technology:** Phishing infrastructure (MFA bypass)
**CVE:** Not applicable
**CVSS:** N/A

### Summary
Europol-led coalition dismantled Tycoon 2FA, one of the largest PhaaS platforms enabling adversary-in-the-middle credential harvesting at scale. The kit was sold via Telegram/Signal from $120 for 10 days. Developer allegedly based in Pakistan. Platform featured pre-built templates, redirect logic, and victim tracking panels. Linked to 64,000+ attacks.

### Why It Matters
Tycoon 2FA was a major enabler of MFA-bypassing phishing attacks against enterprise SSO. Its takedown should reduce the volume of AitM phishing campaigns, though competitors like Starkiller remain active.

### Discovery
**First seen at:** thehackernews.com (Mar 5, reporting on Mar 4 operation)
**How found:** The Hacker News coverage of Europol operation
**Latency:** On-time

### Sources
- https://thehackernews.com/2026/03/europol-led-operation-takes-down-tycoon.html

---

## 📰 FBI and Europol Seize LeakBase Forum

**Threat Score:** 5
**Affected Technology:** Cybercrime infrastructure
**CVE:** Not applicable
**CVSS:** N/A

### Summary
Joint FBI/Europol operation seized LeakBase, one of the largest forums for buying/selling stolen credentials and cybercrime tools. The forum had 142,000+ members and 215,000+ messages. All content including user accounts, private messages, and IP logs preserved for evidence.

### Why It Matters
LeakBase was a major marketplace for stolen credentials used in credential stuffing and account takeover attacks against enterprises. Its seizure (with preserved IP logs) may lead to follow-on arrests.

### Discovery
**First seen at:** thehackernews.com (Mar 5, reporting on Mar 4 seizure)
**How found:** The Hacker News coverage
**Latency:** On-time

### Sources
- https://thehackernews.com/2026/03/fbi-and-europol-seize-leakbase-forum.html

---

## 📋 Noted

- **No CVE** — Ransomware infrastructure mapped: Huntress published analysis of brute-force attack unmasking RaaS infrastructure tied to initial access brokers.
- **No CVE** — Google Chrome shifts to 2-week release cycle for faster security patches.
- **No CVE** — Fake Google Security PWA steals credentials and MFA codes via browser-based phishing.

---

## 📡 Source Coverage

**Sources checked:** 90/90
**Sources with findings:** 5

| Status | Source | Notes |
|--------|--------|-------|
| ✅ | thehackernews.com | Laravel supply chain, VMware update, Tycoon 2FA, LeakBase |
| ✅ | bleepingcomputer.com | Ransomware infra, Chrome release cycle, Google PWA phishing |
| ✅ | cisa.gov | VMware Aria deadline |
| ✅ | nvd.nist.gov | CVE lookups |
| ✅ | reddit.com/r/netsec | Tycoon 2FA discussion |
| ✅ | All remaining sources | Checked, nothing new in scope |
