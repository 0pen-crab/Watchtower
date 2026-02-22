# Vulnerability Intelligence Report — 2026-02-22 Morning

---

## 📰 WordPress WPvivid Plugin — Unauthenticated RCE (900K+ Installs)

**Threat Score:** 8
**Affected Technology:** WordPress (WPvivid Backup & Migration plugin)
**CVE:** Not yet assigned
**CVSS:** Critical (expected)

### Summary
A critical vulnerability in the WPvivid Backup & Migration plugin (900K+ installs) allows RCE through arbitrary file upload without authentication. The plugin's backup/migration functionality provides a direct path to executing malicious code on the web server.

### Why It Matters
WordPress powers a massive portion of the internet. Unauth RCE via file upload in a plugin with 900K installs is a mass-exploitation event waiting to happen. Disable or remove WPvivid immediately.

### Discovery
**First seen at:** bleepingcomputer.com
**How found:** BleepingComputer coverage + WordPress plugin advisory
**Latency:** On-time

### Sources
- https://www.bleepingcomputer.com/news/security/wordpress-plugin-with-900k-installs-vulnerable-to-critical-rce-flaw/

---

## 📰 ClickFix Campaigns Surge — Now 53% of All Malware Loader Activity

**Threat Score:** 7
**Affected Technology:** Cross-platform (Windows, macOS)
**CVE:** Not applicable
**CVSS:** N/A

### Summary
ClickFix social engineering attacks evolved rapidly this week: DNS-based payload delivery via nslookup, Matanbuchus 3.0 loader leading to domain takeover, Matryoshka variant with nested obfuscation for macOS, fake Homebrew delivering Cuckoo Stealer. Huntress reports ClickFix fueled 53% of all malware loader activity in 2025. One campaign went from initial access to domain controller in hours.

### Why It Matters
ClickFix is the dominant initial access technique. Cross-platform and rapidly evolving. DNS-based variant bypasses web-based detection entirely.

### Discovery
**First seen at:** bleepingcomputer.com (multiple articles)
**How found:** Aggregated from BleepingComputer + Huntress research
**Latency:** On-time

### Sources
- https://www.bleepingcomputer.com/news/security/new-clickfix-attack-abuses-nslookup-to-retrieve-powershell-payload-via-dns/
- https://www.bleepingcomputer.com/news/security/pastebin-comments-push-clickfix-javascript-attack-to-hijack-crypto-swaps/
- https://thehackernews.com/2026/02/threatsday-bulletin-openssl-rce-foxit-0.html

---

## 📰 GS7 Threat Actor — Fortune 500 Phishing via Telegram Bots (Operation DoppelBrand)

**Threat Score:** 6
**Affected Technology:** Fortune 500 companies (financial, tech, healthcare, telecom)
**CVE:** Not applicable
**CVSS:** N/A

### Summary
Financially motivated actor GS7 runs large-scale phishing targeting Fortune 500 via lookalike websites and Telegram bots. 150+ malicious domains, Cloudflare-routed. Targets include Wells Fargo, USAA, Fidelity, Citibank. Deploys RMM tools for persistence; may act as initial access broker for ransomware.

### Why It Matters
Fortune 500 targeting with RMM deployment and IAB potential feeds directly into ransomware operations.

### Discovery
**First seen at:** thehackernews.com (ThreatsDay Bulletin)
**How found:** SOCRadar Operation DoppelBrand report
**Latency:** On-time

### Sources
- https://thehackernews.com/2026/02/threatsday-bulletin-openssl-rce-foxit-0.html

---

## 📋 Noted

- **CVE-2024-43468** — Microsoft Configuration Manager: SQL injection, CISA KEV (Feb 12). Older CVE now exploited.
- **CVE-2025-40536** — SolarWinds Web Help Desk: Auth bypass, CISA KEV (Feb 12).
- **CVE-2024-7694** — TeamT5 ThreatSonar: Unrestricted file upload, CISA KEV (Feb 17). Requires admin.
- **CVE-2025-15556** — Notepad++ updater: Code download without integrity check, CISA KEV (Feb 12). Fixed.
- **No CVE** — Remcos RAT: New variant with live C2 and webcam streaming.
- **No CVE** — Jira trials weaponized: Disposable instances for spam targeting government/corporate.
- **No CVE** — ICS ransomware surge: 119 groups, 3,300 orgs hit in 2025 (49% increase per Dragos).

---

## 📡 Source Coverage

**Sources checked:** 90/90
**Sources with findings:** 9

| Status | Source | Notes |
|--------|--------|-------|
| ✅ | bleepingcomputer.com | WPvivid, ClickFix variants |
| ✅ | thehackernews.com | GS7 DoppelBrand, ClickFix, Remcos, Jira |
| ✅ | securityweek.com | ICS ransomware surge |
| ✅ | cisa.gov | SCCM, SolarWinds, TeamT5 KEV entries |
| ✅ | nvd.nist.gov | CVE lookups |
| ✅ | reddit.com/r/netsec | ClickFix DNS discussion |
| ✅ | reddit.com/r/cybersecurity | WPvivid, ClickFix |
| ✅ | attackerkb.com | SCCM analysis |
| ✅ | confluence.atlassian.com/security | Jira abuse report |
| ✅ | All remaining sources | Checked, nothing new in scope |
