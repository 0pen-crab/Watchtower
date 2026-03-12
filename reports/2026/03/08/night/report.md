# Watchtower Report — 2026-03-08 (Night)

---

## 📰 FreeScout Mail2Shell — Zero-Click RCE via Crafted Email

**Threat Score:** 9/10
**Affected Technology:** FreeScout Helpdesk
**CVE:** CVE-2026-28289
**CVSS:** 10.0

### Summary
A maximum-severity zero-click RCE vulnerability in FreeScout allows unauthenticated attackers to achieve full server compromise by sending a single crafted email to any mailbox configured in the platform. The flaw bypasses a previous patch (CVE-2026-27636) using a Unicode zero-width space character (U+200B) to circumvent filename validation, enabling .htaccess file upload and arbitrary command execution. Over 1,100 FreeScout instances are publicly exposed according to Shodan. Patch available in version 1.8.207. No in-the-wild exploitation confirmed yet, but the zero-click nature makes imminent weaponization highly likely.

### Why It Matters
FreeScout is a self-hosted helpdesk/shared mailbox platform — exactly the kind of internet-facing email infrastructure found across enterprise environments. Zero-click RCE via email is the most dangerous attack vector possible.

### Discovery
**First seen at:** bleepingcomputer.com
**How found:** Monitoring BleepingComputer security news feed. OX Security published the original research.

### Sources
- https://www.bleepingcomputer.com/news/security/mail2shell-zero-click-attack-lets-hackers-hijack-freescout-mail-servers/
- https://www.ox.security/blog/freescout-rce-cve-2026-28289/
- https://github.com/freescout-help-desk/freescout/security/advisories/GHSA-5gpc-65p8-ffwp

---

## 📰 Cisco Secure FMC — Two Max-Severity Flaws Allow Unauthenticated Root Access

**Threat Score:** 8/10
**Affected Technology:** Cisco Secure Firewall Management Center
**CVE:** CVE-2026-20079, CVE-2026-20131
**CVSS:** 10.0

### Summary
Cisco released patches for two CVSS 10.0 vulnerabilities in Secure Firewall Management Center (FMC). CVE-2026-20079 is an authentication bypass allowing root OS access via crafted HTTP requests. CVE-2026-20131 is a Java deserialization RCE enabling arbitrary code execution as root. CVE-2026-20131 also affects Cisco Security Cloud Control. No PoC or in-the-wild exploitation confirmed yet, but given Cisco's recent track record with SD-WAN zero-days, these deserve urgent attention.

### Why It Matters
Cisco FMC is the central management plane for enterprise firewall deployments. Compromising FMC gives attackers control over the entire firewall infrastructure — IPS rules, URL filtering, malware protection policies.

### Discovery
**First seen at:** bleepingcomputer.com
**How found:** BleepingComputer security news monitoring.

### Sources
- https://www.bleepingcomputer.com/news/security/cisco-warns-of-max-severity-secure-fmc-flaws-giving-root-access/
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-rce-NKhnULJh

---

## 📰 WordPress User Registration Plugin — Actively Exploited Privilege Escalation

**Threat Score:** 8/10
**Affected Technology:** WordPress (User Registration & Membership plugin)
**CVE:** CVE-2026-1492
**CVSS:** 9.8

### Summary
A critical privilege escalation vulnerability in the WordPress User Registration & Membership plugin (60,000+ installations) allows unauthenticated attackers to create administrator accounts by supplying a user-specified role during membership registration. Active exploitation confirmed — Wordfence blocked over 200 exploitation attempts in the past 24 hours. Fixed in version 5.1.3.

### Why It Matters
WordPress plugins with privilege escalation bugs are consistently among the most actively exploited vulnerabilities on the internet. 60K installations means a large attack surface.

### Discovery
**First seen at:** bleepingcomputer.com
**How found:** BleepingComputer security news monitoring.

### Sources
- https://www.bleepingcomputer.com/news/security/wordpress-membership-plugin-bug-exploited-to-create-admin-accounts/
- https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/user-registration/user-registration-membership-512-unauthenticated-privilege-escalation-via-membership-registration

---

## 📰 Coruna iOS Exploit Kit — Spyware-Grade Chains Now Used for Crypto Theft

**Threat Score:** 8/10
**Affected Technology:** Apple iOS 13.0–17.2.1
**CVE:** Multiple (23 exploits including CVE-2024-23222)
**CVSS:** N/A

### Summary
Google GTIG disclosed "Coruna," an iOS exploit kit containing five full exploit chains (23 exploits) targeting iOS 13 through 17.2.1. Originally observed in surveillance vendor operations, it was later used by Russian cyberspies (UNC6353) in watering-hole attacks on Ukrainian websites, and most recently by Chinese threat actor UNC6691 for cryptocurrency theft. The kit delivers PlasmaGrid malware targeting MetaMask, Phantom, Exodus, and other crypto wallet apps. Documentation suggests Western origin based on native English comments.

### Why It Matters
A spyware-grade exploit kit crossing from nation-state espionage to financially motivated crime signals broader proliferation. Any organization with iOS users browsing compromised sites is at risk.

### Discovery
**First seen at:** bleepingcomputer.com
**How found:** Cross-referencing BleepingComputer with CISA KEV additions (iOS entries) and Google GTIG research blog.

### Sources
- https://www.bleepingcomputer.com/news/security/spyware-grade-coruna-ios-exploit-kit-now-used-in-crypto-theft-attacks/
- https://cloud.google.com/blog/topics/threat-intelligence/coruna-powerful-ios-exploit-kit

---

## 📰 CISA KEV: Rockwell ICS, Hikvision, and Apple iOS Flaws Added

**Threat Score:** 7/10
**Affected Technology:** Rockwell Automation, Hikvision, Apple iOS
**CVE:** CVE-2021-22681, CVE-2017-7921, CVE-2023-41974, CVE-2021-30952, CVE-2023-43000
**CVSS:** N/A

### Summary
CISA added five vulnerabilities to KEV on March 5: Rockwell Automation insufficient protected credentials (CVE-2021-22681) enabling unauthorized Logix controller access, Hikvision improper authentication (CVE-2017-7921) for privilege escalation, and three Apple iOS/iPadOS flaws (CVE-2023-41974, CVE-2021-30952, CVE-2023-43000) linked to the Coruna exploit kit. Federal agencies have until March 24-26 to patch.

### Why It Matters
The Rockwell ICS flaw being confirmed exploited in attacks is significant for any organization with industrial control systems. The Apple iOS entries reinforce the Coruna threat above.

### Discovery
**First seen at:** cisa.gov
**How found:** Direct monitoring of CISA KEV catalog.

### Sources
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://www.securityweek.com/cisa-adds-ios-flaws-from-coruna-exploit-kit-to-kev/

---

## 📰 UAT-9244 — Chinese APT Targets South American Telecoms with Three New Implants

**Threat Score:** 7/10
**Affected Technology:** Telecommunications infrastructure
**CVE:** None
**CVSS:** N/A

### Summary
Cisco Talos disclosed UAT-9244, a China-linked APT associated with FamousSparrow (and potentially Salt Typhoon), targeting South American telecom providers since 2024. The campaign uses three previously undocumented implants: TernDoor (Windows), PeerTime/angrypeer (Linux), and BruteEntry (network edge devices), compromising Windows, Linux, and edge infrastructure.

### Why It Matters
Telecom targeting by Chinese APTs is a persistent theme (Salt Typhoon). Three new implants across Windows, Linux, and edge devices shows sophisticated cross-platform capability.

### Discovery
**First seen at:** thehackernews.com
**How found:** The Hacker News feed and BleepingComputer coverage.

### Sources
- https://thehackernews.com/2026/03/china-linked-hackers-use-terndoor.html
- https://www.bleepingcomputer.com/news/security/chinese-state-hackers-target-telcos-with-new-malware-toolkit/

---

## 📋 Noted

- **N/A** — Wikipedia: Self-propagating JavaScript worm vandalized pages and modified user scripts across multiple wikis; incident contained.
- **N/A** — Cognizant TriZetto: Healthcare IT breach exposed health data of 3.4 million patients.
- **N/A** — HungerRush POS: Threat actor mass-mailed extortion emails to restaurant patrons of HungerRush-using businesses.

---

## 📡 Source Coverage

**Sources checked:** 35/35
**Sources with findings:** 5

| Status | Source | Notes |
|--------|--------|-------|
| ✅ | bleepingcomputer.com | 5 findings |
| ✅ | thehackernews.com | 1 finding (UAT-9244) |
| ✅ | securityweek.com | Corroborated Rockwell, CISA KEV, Cisco FMC |
| ✅ | cisa.gov/kev | 5 new KEV entries |
| ✅ | krebsonsecurity.com | AI agent security analysis — not in scope |
| ✅ | rapid7.com | No new findings beyond existing coverage |
| ✅ | schneier.com | AirSnitch Wi-Fi attack (Mar 9 — for next cycle) |
| ✅ | attackerkb.com | No new relevant entries |
| ✅ | fortinet.com/blog | No new findings |
| ✅ | securitylab.github.com | No new findings |
| ✅ | seclists.org/fulldisclosure | No new findings |
| ✅ | packetstormsecurity.com | No new findings |
| ✅ | opencve.io | CVEs corroborated |
| ✅ | nvd.nist.gov | CVE metadata confirmed |
| ✅ | cve.mitre.org | CVE metadata confirmed |
| ✅ | cve.org | CVE metadata confirmed |
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
| ✅ | habr.com/ru/companies/tomhunter/articles | No new findings |
| ✅ | teletype.in/@cyberok | No new findings |
| ✅ | github.com (advisories + trending) | Corroborated FreeScout GHSA |
| ✅ | Vendor advisories (Cisco) | Corroborated FMC advisories |
| ⚠️ | securityweek.com | Cloudflare blocked some article pages |
| ✅ | Watchtowr/Assetnote/Horizon3 blogs | No new findings |
| ✅ | Nuclei templates | No new relevant templates |
| ✅ | github.com/search?q=CVE | Corroborated CVE-2026-28289 |
| ✅ | Full disclosure mailing lists | No new findings |
