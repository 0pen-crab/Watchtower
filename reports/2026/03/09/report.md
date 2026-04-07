# Watchtower Report — 2026-03-09 (Night)

---

## 📰 Velvet Tempest Deploys CastleRAT via ClickFix in Termite Ransomware Campaign

**Threat Score:** 8/10
**Affected Technology:** Windows endpoints
**CVE:** None
**CVSS:** N/A

### Summary
MalBeacon researchers observed Velvet Tempest (DEV-0504) — an affiliate historically linked to Ryuk, REvil, Conti, BlackMatter, BlackCat, LockBit, and RansomHub — conducting a 12-day intrusion against a US non-profit with 3,000+ endpoints. The initial access came via malvertising leading to ClickFix/CAPTCHA lures that trick victims into pasting obfuscated commands into the Windows Run dialog. The attack used finger.exe for payload retrieval, PowerShell for Chrome credential harvesting, and ultimately deployed DonutLoader and CastleRAT backdoor (associated with CastleLoader). The staging IP was linked to Termite ransomware infrastructure, though encryption was not deployed during the observation period.

### Why It Matters
Velvet Tempest is one of the most prolific ransomware affiliates in existence. The combination of ClickFix social engineering with CastleRAT and Termite infrastructure signals an evolution in their tooling. ClickFix now accounts for 53% of all malware loader activity per prior reporting.

### Discovery
**First seen at:** bleepingcomputer.com
**How found:** BleepingComputer security news monitoring.

### Sources
- https://www.bleepingcomputer.com/news/security/termite-ransomware-breaches-linked-to-clickfix-castlerat-attacks/

---

## 📰 AirSnitch — Full Bidirectional MitM Attack Against Wi-Fi Encryption

**Threat Score:** 7/10
**Affected Technology:** Wi-Fi (all implementations — WPA2, WPA3)
**CVE:** None
**CVSS:** N/A

### Summary
Researchers presented AirSnitch at NDSS 2026, demonstrating a novel cross-layer identity desynchronization attack against Wi-Fi networks. Unlike previous attacks, AirSnitch exploits the failure to bind and synchronize a client across Layers 1 and 2, enabling full bidirectional MitM across homes, offices, and enterprise networks. The attacker can be on the same SSID, a different SSID, or even a separate network segment. This allows interception of all link-layer traffic, DNS cache poisoning, credential theft on unencrypted connections (estimated 6-20% of page loads), and exploitation of unpatched vulnerabilities.

### Why It Matters
A fundamental Wi-Fi protocol weakness affecting all implementations. With 6-20% of web traffic still unencrypted and many intranets using plaintext, the real-world impact for enterprise environments is significant.

### Discovery
**First seen at:** schneier.com
**How found:** Schneier on Security blog, referencing NDSS 2026 paper and Ars Technica coverage.

### Sources
- https://www.schneier.com/blog/archives/2026/03/new-attack-against-wi-fi.html
- https://www.ndss-symposium.org/ndss-paper/airsnitch-demystifying-and-breaking-client-isolation-in-wi-fi-networks/

---

## 📰 Transparent Tribe Uses AI to Mass-Produce Polyglot Malware Implants Targeting India

**Threat Score:** 7/10
**Affected Technology:** Government and military networks (India)
**CVE:** None
**CVSS:** N/A

### Summary
Bitdefender disclosed that Pakistan-aligned APT Transparent Tribe has adopted AI-assisted malware development to industrialize implant production. The group now generates high-volume disposable binaries ("vibeware") in lesser-known languages — Nim, Zig, and Crystal — to evade detection. The implants use trusted services (Slack, Discord, Supabase, Google Sheets) as C2 channels to blend with legitimate traffic.

### Why It Matters
The transition to AI-assisted malware industrialization represents a paradigm shift. Rather than sophisticated single implants, Transparent Tribe floods targets with disposable polyglot binaries that overwhelm detection engines through sheer variety.

### Discovery
**First seen at:** thehackernews.com
**How found:** The Hacker News feed.

### Sources
- https://thehackernews.com/2026/03/transparent-tribe-uses-ai-to-mass.html

---

## 📰 CL-UNK-1068 — Chinese Espionage Campaign Targets Asian Critical Infrastructure

**Threat Score:** 7/10
**Affected Technology:** Aviation, energy, government, telecom, pharma (South/Southeast/East Asia)
**CVE:** None
**CVSS:** N/A

### Summary
Palo Alto Networks Unit 42 disclosed CL-UNK-1068, a previously undocumented Chinese espionage cluster targeting critical infrastructure across aviation, energy, government, law enforcement, pharma, tech, and telecom sectors in South, Southeast, and East Asia. The group uses custom malware, modified open-source utilities, and living-off-the-land binaries (LOLBINs) for persistent access. Assessed with moderate-to-high confidence as cyber espionage.

### Why It Matters
Yet another Chinese APT cluster targeting critical infrastructure sectors. The breadth of targeted industries (seven sectors across three regions) and use of LOLBINs makes detection challenging.

### Discovery
**First seen at:** thehackernews.com
**How found:** The Hacker News feed.

### Sources
- https://thehackernews.com/2026/03/web-server-exploits-and-mimikatz-used.html

---

## 📰 Phishing Campaigns Abuse .arpa DNS and IPv6 Reverse DNS to Evade Defenses

**Threat Score:** 6/10
**Affected Technology:** Email security gateways
**CVE:** None
**CVSS:** N/A

### Summary
Infoblox researchers discovered threat actors abusing ip6.arpa reverse DNS zones to host phishing infrastructure that bypasses domain reputation checks and email security gateways, leveraging the good reputations of Hurricane Electric and Cloudflare DNS services.

### Why It Matters
A novel phishing evasion technique that abuses a fundamental internet infrastructure mechanism. Email security vendors will need to update their detection logic to account for .arpa abuse.

### Discovery
**First seen at:** bleepingcomputer.com
**How found:** BleepingComputer security news monitoring.

### Sources
- https://www.bleepingcomputer.com/news/security/hackers-abuse-arpa-dns-and-ipv6-to-evade-phishing-defenses/
- https://www.infoblox.com/blog/threat-intelligence/abusing-arpa-the-tld-that-isnt-supposed-to-host-anything/

---

## 📰 BoryptGrab Stealer Distributed via 100+ Malicious GitHub Repositories

**Threat Score:** 6/10
**Affected Technology:** Developer workstations
**CVE:** None
**CVSS:** N/A

### Summary
Over 100 GitHub repositories are distributing the BoryptGrab information stealer, which targets browser data, cryptocurrency wallet data, system information, and user files from developer workstations.

### Why It Matters
Supply chain attacks via malicious GitHub repos continue to be an effective vector against developers. The scale (100+ repos) indicates an organized campaign.

### Discovery
**First seen at:** securityweek.com
**How found:** SecurityWeek homepage monitoring.

### Sources
- https://www.securityweek.com/over-100-github-repositories-distributing-boryptgrab-stealer/

---

## 📋 Noted

- **N/A** — US Cyber Strategy: Trump administration published new cyber strategy targeting adversaries, critical infrastructure, and emerging technologies including AI and post-quantum cryptography.
- **N/A** — Google TIG: Google reported 90 zero-days were exploited in attacks throughout 2025, with nearly half targeting enterprise software and appliances.

---

## 📡 Source Coverage

**Sources checked:** 35/35
**Sources with findings:** 5

| Status | Source | Notes |
|--------|--------|-------|
| ✅ | bleepingcomputer.com | 3 findings |
| ✅ | thehackernews.com | 2 findings |
| ✅ | securityweek.com | 1 finding (BoryptGrab) |
| ✅ | schneier.com | 1 finding (AirSnitch) |
| ✅ | cisa.gov/kev | No new additions since Mar 5 |
| ✅ | krebsonsecurity.com | AI agent security analysis — informational |
| ✅ | rapid7.com | No new findings |
| ✅ | attackerkb.com | No new entries |
| ✅ | fortinet.com/blog | No new findings |
| ✅ | securitylab.github.com | No new findings |
| ✅ | seclists.org/fulldisclosure | No new findings |
| ✅ | packetstormsecurity.com | No new findings |
| ✅ | opencve.io | CVEs corroborated |
| ✅ | nvd.nist.gov | CVE metadata confirmed |
| ✅ | cve.mitre.org/cve.org | CVE metadata confirmed |
| ✅ | googleprojectzero.blogspot.com | No new posts |
| ✅ | blog.cloudflare.com/tag/security | No new findings |
| ✅ | msrc.microsoft.com/blog | No new advisories |
| ✅ | hackerone.com/hacktivity | No relevant findings |
| ✅ | bugcrowd.com/disclosures | No relevant findings |
| ✅ | kb.cert.org/vuls | No new findings |
| ✅ | avleonov.com | No new posts |
| ✅ | github.com/0xMarcio/cve | No new findings |
| ✅ | cert.gov.ua | No new advisories |
| ✅ | dbugs.ptsecurity.com | No new findings |
| ✅ | habr.com | No new findings |
| ✅ | teletype.in/@cyberok | No new findings |
| ✅ | github.com (advisories + trending) | No new findings |
| ✅ | Vendor advisories | No new findings |
| ⚠️ | securityweek.com | Cloudflare blocked article detail pages |
| ✅ | Watchtowr/Assetnote/Horizon3 | No new findings |
| ✅ | Nuclei templates | No new relevant templates |
