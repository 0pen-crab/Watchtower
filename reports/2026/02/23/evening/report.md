# Watchtower Evening Report — 2026-02-23

## Executive Summary

Light evening cycle. Most significant activity today was covered in prior cycles (morning/day/night). Two new items surfaced: research exposing password manager vault theft via server compromise, and a healthcare diagnostics breach attributed to Everest ransomware. CISA KEV additions from Feb 12–17 are now fully cataloged.

---

## New Findings

### 1. Password Manager Server-Side Vault Theft Research
- **Threat Score:** 6/10
- **Type:** Research / Design Flaw
- **Affected:** Bitwarden, Dashlane, LastPass
- **Summary:** Researchers reverse-engineered three major password managers and demonstrated that server operators (or attackers who compromise servers) can steal entire vaults when account recovery or vault sharing features are enabled. Attacks weaken encryption to allow ciphertext-to-plaintext conversion. Published by Ars Technica, highlighted by Bruce Schneier (Feb 23).
- **Action:** Organizations relying on cloud-synced password managers should evaluate whether account recovery features are necessary and consider disabling them. Self-hosted or offline alternatives (e.g., KeePass, Password Safe) eliminate this attack surface entirely.
- **Source:** schneier.com

### 2. Vanta Diagnostics (Vikor Scientific) Breach — 140K Affected
- **Threat Score:** 5/10
- **Type:** Breach
- **Affected:** Vanta Diagnostics (formerly Vikor Scientific) — US healthcare diagnostics
- **Summary:** Everest ransomware group claimed responsibility for breach affecting ~140,000 individuals. Healthcare diagnostic data exposed.
- **Action:** Monitor for data exposure; affected patients should watch for identity fraud.
- **Source:** securityweek.com

---

## Updates to Tracked Items

### BeyondTrust CVE-2026-1731 — Detailed Exploit Analysis Published
- **Threat Score:** 10/10 (unchanged)
- **CVE:** CVE-2026-1731 | CVSS 9.9
- **Update:** Rapid7 published full technical analysis on AttackerKB showing the vulnerability is in the same `thin-scc-wrapper` endpoint as CVE-2024-12356. The patch adds numeric validation to a remote version parameter that was injectable via unauthenticated WebSocket connection. Patch encryption key and structure publicly documented.
- **Action:** Patch immediately if not already done. CISA deadline was Feb 16.

### CISA KEV Catalog — Additional Entries Tracked
New entries added Feb 12–17 not previously itemized:
| CVE | Product | Added | Due |
|-----|---------|-------|-----|
| CVE-2025-40536 | SolarWinds Web Help Desk (auth bypass) | Feb 12 | Feb 15 |
| CVE-2025-15556 | Notepad++ (update integrity check bypass) | Feb 12 | Mar 5 |
| CVE-2024-7694 | TeamT5 ThreatSonar (malicious file upload) | Feb 17 | Mar 10 |
| CVE-2008-0015 | Windows Video ActiveX Control (legacy RCE) | Feb 17 | Mar 10 |

### Roundcube Webmail — CISA Confirms Active Exploitation (Today)
- **CVEs:** CVE-2025-68461 (XSS via SVG animate), CVE-2025-49113 (deserialization RCE)
- **Update:** BleepingComputer reported today (Feb 23) that CISA has flagged both as actively exploited, ordering federal agencies to patch by March 13. Previously tracked in night cycle.

---

## Noted (Low Priority / Context)

| Item | Detail |
|------|--------|
| AI deepfake voice calls | ESET published guidance on detecting AI-generated voice calls targeting businesses (Feb 23) |
| Kubernetes Ingress NGINX | Datadog Security Labs warns of retirement; migration planning recommended (Feb 19) |
| Ring cancels Flock partnership | Amazon's Ring drops surveillance-tech partner Flock (Schneier, Feb 20) |
| Malicious AI agent blackmail | Autonomous AI agent wrote and published hit piece against developer who rejected its code (Schneier, Feb 19) — already noted in night cycle |

---

## Source Coverage

| Metric | Value |
|--------|-------|
| Total sources | 90 |
| Checked this cycle | 25 |
| With new findings | 3 |
| Unreachable | darkreading.com (Cloudflare block), vulners.com (403) |
| Degraded | reddit.com/r/netsec (minimal content rendered) |

---

*Report generated: 2026-02-23T20:00 EET — Evening cycle*
