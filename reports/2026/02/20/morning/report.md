# Vulnerability Intelligence Report — 2026-02-20 Morning

---

## 🔄 Update: BeyondTrust CVE-2026-1731 — Confirmed in Ransomware Attacks

**Previous Threat Score:** 9 → **Updated Threat Score:** 10
**CVE:** CVE-2026-1731

### What Changed
CISA updated KEV to confirm ransomware exploitation. Palo Alto Unit 42 published detailed report: web shell deployment, C2, backdoors, lateral movement, data exfiltration. Targeted sectors: financial, legal, tech, education, retail, healthcare across US, France, Germany, Australia, Canada. Pre-auth OS command injection, CVSS 9.9.

### Sources
- https://www.bleepingcomputer.com/news/security/cisa-beyondtrust-rce-flaw-now-exploited-in-ransomware-attacks/
- https://thehackernews.com/2026/02/beyondtrust-flaw-used-for-web-shells.html
- https://www.securityweek.com/beyondtrust-vulnerability-exploited-in-ransomware-attacks/

---

## 📰 Roundcube Webmail — Two Vulns Added to CISA KEV (CVE-2025-68461 & CVE-2025-49113)

**Threat Score:** 8
**Affected Technology:** Roundcube Webmail
**CVE:** CVE-2025-68461 (XSS via SVG), CVE-2025-49113 (Deserialization RCE)
**CVSS:** High to Critical

### Summary
CISA added two Roundcube vulnerabilities to KEV. CVE-2025-68461 is XSS via SVG animate tags. CVE-2025-49113 is deserialization RCE by authenticated users (unvalidated _from parameter in upload.php). Both under active exploitation. Patch deadline: March 13.

### Why It Matters
Roundcube is one of the most deployed open-source webmail clients — directly in scope. Chain potential: XSS → session theft → authenticated RCE → full server compromise.

### Discovery
**First seen at:** CISA KEV catalog
**How found:** CISA KEV monitoring
**Latency:** On-time

### Sources
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog

---

## 📰 LockBit 5.0 — Cross-Platform Ransomware Now Targeting Proxmox

**Threat Score:** 7
**Affected Technology:** Windows, Linux, ESXi, Proxmox VE
**CVE:** Not applicable
**CVSS:** N/A

### Summary
LockBit 5.0 introduces dedicated Proxmox builds targeting the open-source virtualization platform increasingly adopted as a VMware alternative. Windows variant includes DLL unhooking, process hollowing, ETW patching, log clearing.

### Why It Matters
Proxmox adoption is surging. Dedicated ransomware builds mean virtualization infrastructure is no longer safe by obscurity.

### Discovery
**First seen at:** thehackernews.com (ThreatsDay Bulletin)
**How found:** Acronis research
**Latency:** On-time

### Sources
- https://thehackernews.com/2026/02/threatsday-bulletin-openssl-rce-foxit-0.html

---

## 📋 Noted

- **No CVE** — PayPal data breach: SSNs exposed via loan application bug for ~6 months.
- **No CVE** — Advantest ransomware: Japanese chip testing giant compromised.
- **No CVE** — Mississippi medical center: All clinics closed statewide after ransomware.
- **No CVE** — FBI ATM jackpotting: $20M lost in 2025 from 700 incidents.

---

## 📡 Source Coverage

**Sources checked:** 90/90
**Sources with findings:** 8

| Status | Source | Notes |
|--------|--------|-------|
| ✅ | bleepingcomputer.com | BeyondTrust ransomware update, PayPal, Advantest |
| ✅ | cisa.gov | Roundcube KEV, BeyondTrust KEV update |
| ✅ | thehackernews.com | BeyondTrust deep-dive, LockBit 5.0 |
| ✅ | securityweek.com | BeyondTrust ransomware |
| ✅ | unit42.paloaltonetworks.com | BeyondTrust exploitation report |
| ✅ | nvd.nist.gov | CVE lookups |
| ✅ | reddit.com/r/netsec | Roundcube, BeyondTrust discussion |
| ✅ | reddit.com/r/blueteamsec | LockBit 5.0 discussion |
| ✅ | All remaining sources | Checked, nothing new in scope |
