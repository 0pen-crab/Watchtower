# Vulnerability Intelligence Report — 2026-04-05 Night Cycle

---

## 📰 Cisco IMC and SSM On-Prem Dual Critical — Unauthenticated Admin Bypass and Root RCE

**Threat Score:** 8
**Affected Technology:** Cisco Integrated Management Controller (IMC), Cisco Smart Software Manager On-Prem
**CVE:** CVE-2026-20093, CVE-2026-20160
**CVSS:** 9.8

### Summary
Cisco disclosed two critical vulnerabilities: CVE-2026-20093 in IMC allows unauthenticated attackers to bypass authentication and change any user's password (including Admin) via crafted HTTP requests, while CVE-2026-20160 in SSM On-Prem exposes an internal service enabling unauthenticated root-level command execution. Both carry CVSS 9.8 scores, affect multiple product lines (UCS C-Series, Catalyst 8300, ENCS 5000), and have no workarounds — only patching remediates.

### Why It Matters
Cisco IMC manages out-of-band server hardware and is widely deployed across enterprise data centers. SSM On-Prem handles license management for Cisco infrastructure. Unauthenticated access to either could enable full infrastructure compromise, lateral movement, and persistent backdoor installation.

### Discovery
**First seen at:** thehackernews.com
**How found:** The Hacker News article on April 2 covering Cisco's advisory release. Cross-referenced with Cisco's security advisories and SecurityWeek coverage.

### Sources
- https://thehackernews.com/2026/04/cisco-patches-98-cvss-imc-and-ssm-flaws.html
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cimc-auth-bypass-AgG2BxTn
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ssm-cli-execution-cHUcWuNr

---

## 📰 FortiClientEMS Unauthenticated RCE — CVE-2026-35616

**Threat Score:** 8
**Affected Technology:** Fortinet FortiClientEMS 7.4.5–7.4.6
**CVE:** CVE-2026-35616
**CVSS:** 9.1

### Summary
Fortinet disclosed CVE-2026-35616, an improper access control vulnerability in FortiClientEMS versions 7.4.5 through 7.4.6 that allows unauthenticated attackers to execute unauthorized code via crafted requests. Two public PoC exploits appeared on GitHub within hours of the April 4 NVD publication. FortiClientEMS is widely deployed for endpoint management across enterprises.

### Why It Matters
FortiClientEMS manages endpoint security policies and agent deployment across entire organizations. An unauthenticated RCE in this component gives attackers direct access to the endpoint management plane — a devastatingly high-value target for ransomware operators and APTs who can pivot to deploy malware to every managed endpoint.

### Discovery
**First seen at:** cvefeed.io
**How found:** NVD monitoring via CVEFeed.io showed fresh CVE with critical CVSS. Cross-referenced with Fortinet PSIRT advisory FG-IR-26-099 and GitHub PoC repositories.

### Sources
- https://cvefeed.io/vuln/detail/CVE-2026-35616
- https://fortiguard.fortinet.com/psirt/FG-IR-26-099

---

## 📰 TA416 Resumes European Government Espionage with PlugX via OAuth Abuse

**Threat Score:** 7
**Affected Technology:** European government and diplomatic organizations (EU, NATO)
**CVE:** Not yet assigned
**CVSS:** null

### Summary
Proofpoint reports that China-aligned APT TA416 (overlapping with RedDelta, Mustang Panda) has resumed targeting European government and diplomatic organizations since mid-2025, escalating after the U.S.-Israel-Iran conflict in February 2026. The group abuses OAuth redirects through Microsoft Entra ID, Cloudflare Turnstile pages, and C# project files to deliver updated PlugX backdoor variants via DLL side-loading.

### Why It Matters
TA416's campaign directly targets the diplomatic infrastructure of EU and NATO member states. The use of legitimate OAuth authorization endpoints and cloud storage (Azure Blob, Google Drive, SharePoint) for payload delivery makes detection extremely difficult and represents a sophisticated evolution in state-sponsored espionage tradecraft.

### Discovery
**First seen at:** thehackernews.com
**How found:** The Hacker News published Proofpoint's research on April 3. Cross-referenced with Proofpoint's blog and prior coverage of TA416/Mustang Panda clusters.

### Sources
- https://thehackernews.com/2026/04/china-linked-ta416-targets-european.html
- https://www.proofpoint.com/us/blog/threat-insight/id-come-running-back-eu-again-ta416-resumes-european-government-espionage

---

## 📰 Signal Android Intent Redirection Enables Decrypted Attachment Exfiltration

**Threat Score:** 6
**Affected Technology:** Signal Android app
**CVE:** Not yet assigned (GHSL-2026-102)
**CVSS:** null

### Summary
GitHub Security Lab researcher Jaroslav Lobačevski disclosed GHSL-2026-102, an intent redirection vulnerability in Signal for Android that allows unauthorized exfiltration of decrypted message attachments. A malicious app on the same device can exploit this flaw to intercept and extract decrypted files that Signal users send or receive, bypassing Signal's end-to-end encryption guarantees at the device level.

### Why It Matters
Signal is widely used by journalists, dissidents, government officials, and security-conscious organizations for secure communication. A vulnerability that allows decrypted attachment theft undermines the core trust model and is a high-value target for state-sponsored surveillance operations.

### Discovery
**First seen at:** securitylab.github.com
**How found:** GitHub Security Lab advisories page, published April 3, 2026.

### Sources
- https://securitylab.github.com/advisories/GHSL-2026-102_Android_SignalApp/

---

## 🔄 Update: React2Shell (CVE-2025-55182) — UAT-10608 Mass Credential Harvesting, 766+ Hosts Compromised

**Previous Threat Score:** 9 → **Updated Threat Score:** 10
**CVE:** CVE-2025-55182

### What Changed
Cisco Talos has now attributed a large-scale automated credential harvesting operation to threat cluster UAT-10608, confirming at least 766 Next.js hosts have been compromised using React2Shell as the initial infection vector. The attackers deploy "NEXUS Listener," a web-based collection framework that automatically extracts database credentials, SSH keys, AWS secrets, Kubernetes tokens, Stripe API keys, GitHub tokens, and shell history from compromised systems. The operation represents industrialized exploitation — automated scanning identifies vulnerable Next.js deployments, and post-compromise scripts systematically exfiltrate every credential and secret on the host.

### Sources
- https://thehackernews.com/2026/04/hackers-exploit-cve-2025-55182-to.html
- https://blog.talosintelligence.com/uat-10608-inside-a-large-scale-automated-credential-harvesting-operation-targeting-web-applications/

---

## 🔄 Update: TrueConf CVE-2026-3502 — Added to CISA KEV, Chinese APT Exploitation Confirmed

**Previous Threat Score:** 7 → **Updated Threat Score:** 8
**CVE:** CVE-2026-3502

### What Changed
CISA has added CVE-2026-3502 (TrueConf Client code integrity bypass) to the Known Exploited Vulnerabilities catalog on April 2, with a remediation deadline of April 16. SecurityWeek confirms a Chinese threat actor is actively exploiting the vulnerability in targeted attacks against Asian government organizations, using the video conferencing platform as an entry point for reconnaissance, privilege escalation, and payload deployment.

### Sources
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://www.securityweek.com/trueconf-zero-day-exploited-in-asian-government-attacks/
- https://cyberpress.org/cisa-adds-trueconf-flaw/

---

## 📋 Noted

- **CVE-2026-4370** — Canonical Juju: CVSS 10.0 vulnerability disclosed April 2; limited exposure for most enterprise environments but critical for organizations using Juju for cloud orchestration.
- **CVE-2026-27636 / CVE-2026-28289** — FreeScout: Unauthenticated RCE via ZWSP .htaccess bypass; Metasploit module released April 3.
- **CVE-2025-50286** — Grav CMS: Authenticated RCE via Direct Install plugin upload; Metasploit module released April 3.
- **GHSL-2026-102** — Signal Android: Intent redirection advisory from GitHub Security Lab (covered above as News).
- **CVE-2026-28397, CVE-2026-28401** — NocoDB: Two stored XSS vulnerabilities disclosed by GitHub Security Lab; potential account takeover.
- **No-CVE** — OWASP CRS: Whitespace padding bypass vulnerability disclosed on Full Disclosure mailing list April 2.
- **No-CVE** — Open WebUI: Broken access control disclosed by SEC Consult on Full Disclosure April 2.
- **No-CVE** — Device Code Phishing Surge: Push Security reports 37x increase in OAuth device code phishing attacks with 11+ competing phishing kits including EvilTokens; social engineering vector, no specific CVE.
- **No-CVE** — LinkedIn BrowserGate: Microsoft's LinkedIn caught scanning for 6,236+ Chrome extensions and collecting device fingerprinting data; privacy concern, not a vulnerability.
- **No-CVE** — DPRK LNK campaigns: FortiGuard Labs analyzed DPRK-linked attacks using LNK files with GitHub as covert C2 infrastructure, targeting Windows environments.

---

## 📡 Source Coverage

**Sources checked:** 31/31
**Sources with findings:** 14

| Status | Source | Notes |
|--------|--------|-------|
| ✅ | bleepingcomputer.com | Device code phishing surge, LinkedIn BrowserGate |
| ✅ | thehackernews.com | Cisco IMC/SSM, TA416 PlugX, React2Shell exploitation, SparkCat |
| ✅ | cisa.gov/kev | TrueConf CVE-2026-3502 added to KEV |
| ✅ | cisa.gov | KEV catalog updates confirmed |
| ✅ | securityweek.com | ShareFile RCE, TrueConf exploitation, Claude Code vuln |
| ✅ | github.com/search?q=CVE | CVE-2026-21858, CVE-2026-35616 PoCs tracked |
| ✅ | schneier.com | Coruna iOS toolkit analysis, US router ban |
| ✅ | krebsonsecurity.com | TeamPCP/CanisterWorm Iran wiper, DDoS botnet takedowns |
| ✅ | rapid7.com | Metasploit wrap-up (FreeScout, Grav CMS modules), BPFDoor research |
| ✅ | attackerkb.com | CVE-2026-20127 deep analysis |
| ✅ | fortinet.com/blog/threat-research | DPRK LNK+GitHub C2 campaigns |
| ✅ | securitylab.github.com | Signal Android GHSL-2026-102, NocoDB XSS, Sentry privilege escalation |
| ✅ | seclists.org/fulldisclosure | OWASP CRS bypass, Open WebUI BAC, MetInfo CMS |
| ✅ | packetstormsecurity.com | 34 exploits, 248 advisories in last 7 days |
| ✅ | opencve.io | Platform checked, requires auth for detailed CVE data |
| ✅ | nvd.nist.gov | Checked; limited data extraction due to JS-heavy page |
| ❌ | cve.mitre.org | No content extracted |
| ⚠�� | cve.org | No content extracted |
| ✅ | googleprojectzero.blogspot.com | Grammar fuzzing research, Windows GetProcessHandleFromHwnd |
| ✅ | blog.cloudflare.com/tag/security | Client-Side Security, Account Abuse Protection |
| ⚠️ | msrc.microsoft.com/blog | Minimal content extracted |
| ⚠️ | hackerone.com/hacktivity | JS-rendered, no content extracted |
| ❌ | bugcrowd.com/disclosures | 404 error |
| ✅ | kb.cert.org/vuls | Checked, no new in-scope advisories |
| ✅ | avleonov.com | March Linux Patch Wednesday analysis, trending vulns |
| ✅ | github.com/0xMarcio/cve | CVE-2026-35616, CVE-2026-21643 PoCs tracked |
| ✅ | dbugs.ptsecurity.com | Checked, no new in-scope content |
| ✅ | habr.com/ru/companies/tomhunter/articles | February 2026 CVE roundup (already covered) |
| ⚠️ | teletype.in/@cyberok | Russian-language; December/January coverage, no April content |
| ⚠️ | cert.gov.ua | Minimal content extracted (JS-rendered) |
| ✅ | cvefeed.io | CVE-2026-35616 FortiClientEMS details |
