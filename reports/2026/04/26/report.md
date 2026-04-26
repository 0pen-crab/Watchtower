# Watchtower Night Report — 2026-04-26
**Cycle:** Night | **Generated:** 2026-04-26 03:30 UTC (2026-04-26T03:30:00Z)
**Sources checked:** 19/30 | **CISA KEV new additions:** 0 (no additions since 2026-04-24)

---

## 🟠 HIGH

### CVE-2026-40050 — CrowdStrike LogScale Self-Hosted Unauthenticated Path Traversal (CVSS 9.8)
**Product:** CrowdStrike LogScale Self-Hosted (1.224.0–1.234.0 GA, 1.228.0/1.228.1 LTS) | **CVE:** CVE-2026-40050 | **CVSS:** 9.8 | **First reported:** 2026-04-21 (full technical detail published 2026-04-25)

CrowdStrike published a full advisory for an unauthenticated path traversal in a cluster API endpoint of LogScale Self-Hosted that lets a remote attacker read arbitrary files from the underlying filesystem. Watchtower flagged this as a Noted item on 2026-04-24 when the patch landed without public detail; the technical write-up is now public, the affected version range is confirmed, and a CVE has been assigned. CrowdStrike states the issue was found during internal testing and that a proactive log review found no evidence of exploitation in the wild. SaaS customers were already protected by network-layer blocks deployed across all clusters on 2026-04-07; the exposure is on customer-operated self-hosted deployments.

**Timeline:** Internal discovery → SaaS network blocks 2026-04-07 → CVE reserved 2026-04-08 → CVE published 2026-04-21 → vendor advisory and full technical detail 2026-04-25.

**Why it matters:** LogScale is the central log/SIEM ingestion plane in many estates. Arbitrary unauthenticated file read against the SIEM gives an attacker access to the most sensitive operational data they could reasonably ask for: log secrets, ingestion tokens, credentials referenced in configuration, customer data in transit. Self-hosted SIEM is exactly the kind of internal-yet-network-reachable service where this score lands hardest.

**Mitigation:**
- Upgrade LogScale Self-Hosted to a fixed version above the affected ranges (per CrowdStrike advisory).
- Until upgrade, restrict the LogScale cluster API to a management VLAN/jump host; do not expose to general internal traffic, and never to the internet.
- Hunt: review LogScale access logs for unusual path-traversal characters (`..`, encoded dots) on cluster API endpoints. Rotate any tokens or secrets that may have been resident on disk.
- SaaS customers have no action; Next-Gen SIEM is unaffected.

**Sources:** [The420 — CrowdStrike LogScale CVE-2026-40050](https://the420.in/crowdstrike-logscale-vulnerability-cve-2026-40050-remote-file-theft-risk/) | [Network Security Magazine — Critical CrowdStrike LogScale Vulnerability](https://www.network-security-magazine.com/network-security/top-network-security-news/critical-crowdstrike-logscale-vulnerability-cve-2026-40050-exposes-servers-to-re/) | [CSIRT-CY advisory](https://csirt.cy/en/cve/2026/critical-path-traversal-vulnerability-in-crowdstrike-logscale) | [SecurityWeek — Vulnerabilities Patched in CrowdStrike, Tenable Products](https://www.securityweek.com/vulnerabilities-patched-in-crowdstrike-tenable-products/)

---

### UNC6692 "SNOW" Modular Toolset — Microsoft Teams Helpdesk Impersonation Reaches Domain Controllers
**Product:** Microsoft Teams (external federation) + Chromium (extension persistence) | **CVE:** None — TTP campaign | **CVSS:** N/A | **First reported:** 2026-04-23 (Mandiant detailed analysis published 2026-04-25)

Google Mandiant published a detailed analysis of UNC6692, a financially motivated cluster running an email-bombing → Microsoft Teams "IT helpdesk" social-engineering chain into a custom modular implant family called SNOW. The chain delivers SNOWBELT (persistence via a JavaScript Chromium extension running inside a headless Edge instance), SNOWGLAZE (Python-based WebSocket tunneler establishing a SOCKS proxy to a static C2 with hard-coded credentials), and SNOWBASIN (a local-HTTP-server backdoor for command execution, screenshots, and file transfer). Post-foothold the operator pivots via SMB/RDP, dumps LSASS, performs pass-the-hash to reach domain controllers, and exfiltrates Active Directory databases and SAM/SECURITY/SYSTEM hives using FTK Imager + LimeWire. Targeting between 2026-03-01 and 2026-04-01 was 77% senior employees.

**Timeline:** Active March–April 2026; first BleepingComputer coverage 2026-04-23; Mandiant detailed write-up + IOCs/YARA published 2026-04-25.

**Why it matters:** Two structural exposures. First, Microsoft Teams external federation is enabled by default in many tenants — a single inbound chat from a look-alike "IT helpdesk" account is sufficient to start the chain. Second, the implant lives inside a Chromium browser extension, which sidesteps a great deal of EDR and means the persistence surface is whatever browser-extension governance the tenant has, which is often nothing. Domain controller compromise was reached against multiple senior-employee initial victims.

**Discovered by:** Google Mandiant (UNC6692 cluster).

**Mitigation:**
- Restrict Microsoft Teams external chat federation to an explicit allowlist of partner tenants. If broad external chat is required, surface an unmistakable "external sender" banner.
- Enforce a Chromium/Edge browser-extension allowlist via GPO or MDM. Treat any newly installed extension named "MS Heartbeat" / "System Heartbeat" as IOC.
- Detect AutoHotkey execution from non-developer endpoints. Alert on FTK Imager and LimeWire on workstations.
- Run Mandiant's published YARA rules across endpoint and email gateways; block the SNOWGLAZE C2 host.
- Train senior-employee populations specifically on the "email-bomb then Teams call" pattern — UNC6692 picks them on purpose.

**Sources:** [Google Cloud Threat Intelligence — UNC6692 social engineering custom malware](https://cloud.google.com/blog/topics/threat-intelligence/unc6692-social-engineering-custom-malware) | [BleepingComputer — Threat actor uses Microsoft Teams to deploy new "Snow" malware](https://www.bleepingcomputer.com/news/security/threat-actor-uses-microsoft-teams-to-deploy-new-snow-malware/) | [The Hacker News — UNC6692 Impersonates IT Helpdesk via Microsoft Teams](https://thehackernews.com/2026/04/unc6692-impersonates-it-helpdesk-via.html)

---

### BlackFile Vishing Extortion Campaign — Retail and Hospitality Targeted via Salesforce/SharePoint API Exfiltration
**Product:** Identity (helpdesk + MFA self-service) + Salesforce + SharePoint | **CVE:** None — TTP campaign | **CVSS:** N/A | **First reported:** 2026-04-24

Unit 42 and RH-ISAC disclosed BlackFile, a financially motivated cluster (linked with moderate confidence to "The Com") that has run vishing-led intrusions against retail and hospitality organizations since February 2026. Operators spoof IT-support VoIP numbers, walk targets through credential harvesting and OTP capture on look-alike login pages, register their own MFA device using the stolen secrets, then scrape internal directories to escalate to executive accounts. Data theft is performed through legitimate Salesforce and SharePoint APIs with content filters for "confidential" / "SSN" before publication on a leak site; ransom demands run to seven figures and are followed up with swatting attempts against named senior executives.

**Timeline:** Campaign active since 2026-02; public disclosure via RH-ISAC + Unit 42 on 2026-04-24.

**Why it matters:** Three operational signals. (1) The MFA-bypass-via-self-service-enrollment pattern works against any environment that allows users to register a new MFA factor with only password+OTP — it is not a Salesforce or SharePoint flaw. (2) Exfiltration is over legitimate API surfaces, so DLP and EDR signal heavily depends on SaaS API monitoring rather than network egress. (3) Swatting of executives is a meaningful escalation in extortion tradecraft and is now being seen alongside ShinyHunters-cluster activity (ADT, Vercel, McGraw-Hill etc. in recent weeks).

**Mitigation:**
- Helpdesk: require multi-factor identity verification for any caller before password resets, MFA re-enrollment, or device registration; do not rely on personal data alone.
- MFA: gate self-service device registration behind a second strong factor (existing FIDO2 token, manager approval, or in-person verification).
- Salesforce / Microsoft 365: enable session-based conditional access, enforce IP allowlisting for executive accounts, and review API-driven export volume thresholds.
- Tabletop the swatting scenario with executive protection and local law enforcement liaisons; pre-script a response.
- Treat any inbound "IT support" voice call asking for OTP or device registration as adversary action by default.

**Sources:** [BleepingComputer — New BlackFile extortion gang targets retail and hospitality](https://www.bleepingcomputer.com/news/security/new-blackfile-extortion-gang-targets-retail-and-hospitality-orgs/) | [RH-ISAC analyst note (referenced)](https://www.bleepingcomputer.com/news/security/new-blackfile-extortion-gang-targets-retail-and-hospitality-orgs/)

---

## 📋 Noted / Monitoring

**GopherWhisper APT — China-aligned, Mongolian government primary target (ESET, 2026-04-23)** — New China-aligned cluster active since November 2023; abuses Slack, Discord, Microsoft Graph API, and file.io for C2; toolset includes LaxGopher, RatGopher, BoxOfFriends, SSLORDoor. Confirmed dozen-plus systems in a Mongolian government org plus "dozens" of additional victims. Geographically targeted, but the abuse-of-legitimate-services pattern (Slack/Discord/Graph C2) generalises and is worth tagging as a hunting hypothesis.

**Trigona ransomware — custom uploader_client.exe exfiltration tool + BYOVD (Symantec, 2026-04-23)** — Trigona affiliates have switched to a bespoke `uploader_client.exe` for exfil (parallel uploads to a hard-coded server) instead of Rclone/MegaSync, plus BYOVD chain (HRSword kernel driver + tooling to terminate PCHunter/Gmer/YDark/WKTools/DumpGuard/StpProcessMonitorByovd). Operationally relevant for endpoint detection tuning even where Trigona itself is not in scope.

**CVE-2026-33694 — Tenable Nessus Windows arbitrary code execution via junctions** — High-severity Nessus / Nessus Agent flaw on Windows; junction-based arbitrary file deletion can escalate to code execution at SYSTEM. Local exploitation only, so out of our standard remote-component scope; patch in Nessus 10.11.4 / Agent 11.1.3.

**26 FakeWallet apps on Apple App Store (2026-04-24)** — Malicious apps mimicking Bitpie, Coinbase, MetaMask, Trust Wallet etc., harvesting seed phrases. Mobile-only, out of scope, but worth a corporate phishing-awareness mention if employees use personal devices for crypto assets.

**Apple iOS 26.4.2 — fix for Signal notification-database recovery issue** — Carry-over from yesterday's Noted; Apple has now patched the bug Schneier and SecurityWeek covered last week. Mobile-only.

**Mastodon DDoS (2026-04-22)** — Same campaign that hit Bluesky earlier this month; mitigated within hours, no defensive action required for our estate, useful internet-weather context only.

**Cosmetics group Rituals data breach (2026-04-23)** — Customer data lost; consumer impact, not enterprise actionable. Tracking under the broader extortion-ecosystem activity (BlackFile + ShinyHunters).

**Locked Shields 2026 (2026-04-24)** — NATO's annual cyber defence exercise with 41 nations participating. Not a vulnerability — context only for engagement with state CERTs.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com, schneier.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (403, used THN/BC for KEV data) |
| Vendor advisories | msrc.microsoft.com, fortinet.com/blog/threat-research | ❌ / ⚠️ |
| Research / OSINT | securitylab.github.com, seclists.org/fulldisclosure, kb.cert.org/vuls, avleonov.com | ✅ |
| CVE databases | app.opencve.io, dbugs.ptsecurity.com, github.com/0xMarcio/cve, github.com/search | ✅ |
| Cloud / vendor blogs | blog.cloudflare.com/tag/security, rapid7.com | ✅ / ⚠️ |
| Bug bounty | hackerone.com/hacktivity, bugcrowd.com/disclosures, attackerkb.com | ❌ (JS/404/403) |
| Russian / non-English | habr.com, teletype.in/@cyberok, cert.gov.ua | ⚠️ (no recent posts / no extract) |
| Authoritative DBs | nvd.nist.gov, cve.org, cve.mitre.org | ❌ (JS / no API extract) |
| Research labs | googleprojectzero.blogspot.com (now projectzero.google), packetstormsecurity.com (now packetstorm.news) | ⚠️ / ⚠️ |

**Errors:** cisa.gov + cisa.gov/known-exploited-vulnerabilities-catalog (403); attackerkb.com (403); bugcrowd.com/disclosures (404); hackerone.com/hacktivity (JS); cve.org, cve.mitre.org (JS); nvd.nist.gov (no extract); msrc.microsoft.com/blog (no extract); opencve.io (marketing — used app.opencve.io).
**CISA KEV:** No new additions since 2026-04-24 (Samsung MagicINFO, SimpleHelp x2, D-Link DIR-823X). May 15, 2026 federal patch deadline still pending for that batch.

---

*Watchtower vulnerability-researcher | Cycle: 2026-04-26/night | Next: 2026-04-27/night*
