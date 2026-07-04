# Watchtower Night Report — 2026-07-04
**Cycle:** Night | **Generated:** 2026-07-04 00:00 UTC (2026-07-04T00:00:00Z)
**Sources checked:** 22/30 | **CISA KEV total:** unreached (cisa.gov 403) | **New KEV additions:** none confirmed via BC/SW/THN cross-reference in 24h window; SharePoint CVE-2026-45659 BOD 26-04 FCEB deadline lands TODAY (Saturday 2026-07-04)

---

## 🔴 CRITICAL

### Apache Solr CVE-2026-44825 (CVSS 9.8) — Unauthenticated Velocity Response Writer Template-Injection RCE In Solr 9.4.0–9.10.1 + 10.0.0; Mass-Exploitation Framework Public On GitHub Same Day
**Product:** Apache Solr (enterprise search platform) | **CVE:** CVE-2026-44825 | **Status:** Patched (9.10.2 / 10.0.1) | **Public PoC** | **Mass-Exploitation Tooling Landed**

Apache Solr's Velocity Response Writer processes unsanitized user-supplied template parameters at the `/select` endpoint with `wt=velocity`. An attacker injects a Velocity template that calls `java.lang.Runtime.exec()`, yielding unauthenticated remote code execution. Vulnerable branches: 9.4.0 through 9.10.1 + 10.0.0. Patches landed in 9.10.2 and 10.0.1. Within the same day of PoC disclosure the "solrradar" mass-exploitation framework surfaced on GitHub (shinthink/solrradar) — three-tier detection (body / headers / auth-probe), credential brute-forcing, interactive shell access. No public in-wild exploitation confirmed at time of writing but the template-injection primitive is the same class as the 2019 Solr Velocity CVE-2019-17558 which Clop-era operators weaponized within 72 hours.

**Timeline:** Public disclosure 2026-07-03 → mass-exploitation framework published on GitHub same day (2026-07-03).

**Why it matters:** Solr is deployed across enterprise search, log analytics, and content-management back-ends; the `/select` endpoint is typically internet-adjacent behind auth-proxies but many corporate deployments expose it directly on management VLANs and DMZs. Historical Velocity-RCE Solr events converted to full-fleet compromise inside a week — treat any Solr 9.x/10.x on the wire with 24-hour patch SLA.

**Discovered by:** Not publicly attributed at time of writing.

**Mitigation:**
- Patch Apache Solr immediately to 9.10.2 (or 10.0.1 for the 10.x branch); this is the only durable fix.
- Interim: disable Velocity Response Writer entirely by removing `wt=velocity` from allowed response writers in `solrconfig.xml`; restart the collection.
- Front any internet-facing `/select` endpoint with a WAF rule blocking `wt=velocity` parameter values.
- Hunt Solr JVM child processes (`java → bash / cmd`) and unexpected outbound connections from Solr hosts for the last 72 hours; treat any suspicious child as compromise.
- Rotate any credentials Solr had access to (database connections, cloud IAM roles, integration tokens).

**Sources:** [openwall oss-security — Apache Solr Velocity Response Writer CVE-2026-44825](https://www.openwall.com/lists/oss-security/2026/07/) | [GitHub — shinthink/solrradar mass-exploitation framework](https://github.com/shinthink/solrradar)

---

### Joomla Page Builder CK Extension CVE-2026-56290 — Unauthenticated File Upload → PHP RCE, Public Mass-Exploitation Framework Landed 2026-07-03
**Product:** Page Builder CK Joomla extension (versions ≤ 3.5.10) | **CVE:** CVE-2026-56290 | **Status:** Patched (versions >3.5.10 marked possibly patched) | **Public PoC + Mass Exploitation Framework**

Page Builder CK's `browse.ajaxAddPicture` controller accepts user-supplied files and destination paths with only `trim()` sanitization — no authentication is required. An attacker harvests a CSRF token from any public Joomla page, then POSTs a PHP webshell with a bypassed extension (case manipulation, alternative handlers, double extensions — 40+ variants tested) to any of 20+ writable extension directories. The `shinthink/pbck-exploit` GitHub framework published 2026-07-03 automates endpoint discovery, CSRF harvesting, shell deployment, validation, and cleanup. This is the **fourth** Joomla-extension mass-exploitation event in 30 days after Joomla JCE Pro CVE-2026-48907 (BOD 26-04 06-17), the June Mirasvit Magento supply-chain campaign, and the Awesome Motive CDN plugin compromise per MEMORY 2026-06-18.

**Timeline:** Public disclosure 2026-07-03 → mass-exploitation framework published same day.

**Why it matters:** Joomla remains a large-footprint enterprise CMS; Page Builder CK is a page-builder plugin popular on marketing and product sites. Unauth file upload → PHP RCE is the exact primitive Clop and IABs have weaponized against CMS extensions three times in the last month. Corporate Joomla instances should be scanned same-day.

**Discovered by:** Not publicly attributed; PoC and framework published by "shinthink" on GitHub.

**Mitigation:**
- Inventory all Joomla installations for Page Builder CK; patch to the latest available version (>3.5.10) immediately.
- If patch is delayed even 24 hours, take the extension out of service (`disable`) or WAF-block POST requests to `index.php?option=com_pagebuilderck&task=browse.ajaxAddPicture`.
- Hunt Joomla `images/`, `media/`, and extension-directory paths for unexpected `.php`, `.phtml`, `.phar`, or double-extension files during the last 72 hours.
- Rotate Joomla admin credentials and any application-layer secrets accessible from the compromised host.
- Cross-check Joomla logs for CSRF-token harvesting patterns (GET on public Joomla pages followed by POST to `browse.ajaxAddPicture` within seconds).

**Sources:** [GitHub — shinthink/pbck-exploit mass-exploitation framework](https://github.com/shinthink/pbck-exploit)

---

### Apache Lucene.Net Replicator 3-CVE Batch (CVE-2026-47896 + CVE-2026-47897 + CVE-2026-47898) — Unauthenticated Arbitrary File Read + Arbitrary File Write + XXE
**Product:** Apache Lucene.Net Replicator + Analysis.Common (widely-embedded .NET search infrastructure) | **CVE:** CVE-2026-47896, CVE-2026-47897, CVE-2026-47898 | **Status:** Patched (per oss-security 2026-07-03 disclosure) | **Public Technical Detail**

Apache Software Foundation disclosed a three-CVE batch on oss-security 2026-07-03 covering the Lucene.Net Replicator and Analysis.Common components. **CVE-2026-47896** is an unauthenticated arbitrary file read against the Lucene.Net.Replicator replication *server* (attacker-controlled clients read files off the server). **CVE-2026-47897** is the mirror-image — a malicious *server* writes arbitrary files to Lucene.Net.Replicator *clients*. **CVE-2026-47898** is XXE in `Lucene.Net.Analysis.Common`'s `PatternParser`. Lucene.Net powers the search backend for a wide range of .NET enterprise applications; the replication surface is used in distributed-index deployments.

**Timeline:** Public disclosure 2026-07-03 via Apache Software Foundation on openwall oss-security.

**Why it matters:** Lucene.Net is embedded in enterprise .NET search stacks (SharePoint-adjacent search, product-catalog search, log-analytics apps). The unauth file-read on the replication server yields config, secrets, and connection strings; the client-side arbitrary write is a direct code-drop primitive. XXE on `PatternParser` can be chained to SSRF and internal-network probing. All three primitives require no authentication.

**Discovered by:** Apache Software Foundation security team (per oss-security posting).

**Mitigation:**
- Inventory Lucene.Net-consuming .NET applications and update to the fixed release per the vendor advisories linked from openwall oss-security 2026-07-03.
- Restrict the replication server port to a management VLAN; deny external network reach.
- For applications parsing untrusted `PatternParser` input, disable XML external entities entirely in the .NET XML parser configuration.
- Rotate any secrets on any host running Lucene.Net.Replicator on an internet-facing or DMZ-adjacent port during the last 30 days.

**Sources:** [openwall oss-security — Apache Lucene.Net CVE-2026-47896/47897/47898 batch](https://www.openwall.com/lists/oss-security/2026/07/03/1)

---

## 🟠 HIGH

### Cursor AI Code Editor 'DuneSlide' — CVE-2026-50548 + CVE-2026-50549 (CVSS 9.8) Sandbox-Escape → OS-Level RCE, Patched April But Public Disclosure Today
**Product:** Cursor AI code editor (pre-3.0 versions) | **CVE:** CVE-2026-50548, CVE-2026-50549 | **CVSS:** 9.8 | **Status:** Patched (Cursor 3.0, 2026-04-02) | **Public Disclosure 2026-07-03**

Cato Networks disclosed two critical Cursor pre-3.0 vulnerabilities on 2026-07-03. Both abuse Cursor's automatic terminal-command execution: **CVE-2026-50548** exploits improper path validation — a crafted prompt redirects the working directory outside project scope, allowing overwriting of the `cursorsandbox` executable itself and full sandbox bypass. **CVE-2026-50549** exploits symlink path-canonicalization errors — write-only symbolic links force Cursor to misidentify file destinations and yield equivalent sandbox escape. The chain reaches OS-level RCE on the operator workstation with no user interaction beyond opening the crafted content. Cursor patched both in v3.0 released 2026-04-02; CVE IDs assigned early June; public disclosure landed 2026-07-03.

**Timeline:** Reported to Cursor by Cato Networks February 2026 → Cursor 3.0 patched 2026-04-02 → CVE IDs assigned early June 2026 → Public disclosure 2026-07-03 via SecurityWeek.

**Why it matters:** Cursor is one of the two dominant AI-augmented code editors alongside VS Code + Copilot. Any developer running pre-3.0 Cursor while reviewing untrusted repositories, PRs, or Slack-shared code snippets is one prompt-injected file away from OS RCE. This is the **third** AI-coding-assistant compromise primitive in 60 days after Agentjacking (Sentry-DSN prompt injection MEMORY 2026-06-13) and SymJack (2026-05-28 Adversa AI symlink-hijack). The pattern is clear: agentic-execution flows in developer tooling are a viable initial-access vector for supply-chain and IP theft.

**Discovered by:** Cato Networks.

**Mitigation:**
- Force-upgrade Cursor to v3.0 or later on every developer workstation; audit MDM / package manager to confirm compliance.
- Prohibit pre-3.0 Cursor from touching any untrusted repository, PR review, or Slack-shared snippet; block pre-3.0 versions on network policy where feasible.
- Adopt the MEMORY 2026-06-13 Agentjacking hardening as a baseline: sandbox any AI-agent code-execution flow in a container without production credentials or corporate SSO.
- Monitor developer endpoints for `cursorsandbox` binary modifications or unexpected symlink creation in Cursor's workspace directories.

**Sources:** [SecurityWeek — Critical Cursor AI IDE Flaws Could Lead to OS-Level Remote Code Execution](https://www.securityweek.com/critical-cursor-ai-ide-flaws-could-lead-to-os-level-remote-code-execution/)

---

### Gitea Self-Hosted Git Server 8-CVE Batch Including CVE-2026-58426 (CVSS 9.6) + CVE-2026-58424 (CVSS 8.9)
**Product:** Gitea (open-source self-hosted Git service) | **CVE:** CVE-2026-58418, CVE-2026-58419, CVE-2026-58421, CVE-2026-58422, CVE-2026-58423, CVE-2026-58424, CVE-2026-58426, CVE-2026-28705 | **CVSS:** 9.6 (top), 8.9, 7.7, 6.5, N/A x4 | **Published:** 2026-07-03 via dbugs.ptsecurity.com

Positive Technologies dbugs surfaced an 8-CVE Gitea batch on 2026-07-03. Top severities: **CVE-2026-58426 (CVSS 9.6)** — details pending vendor advisory; **CVE-2026-58424 (CVSS 8.9)**; **CVE-2026-58423 (CVSS 7.7)**. The CVSS 9.6 items point to unauthenticated or low-privilege code-execution primitives. Gitea underpins many corporate self-hosted Git deployments and CI/CD source-of-truth workflows; compromise of a Gitea instance is a supply-chain-adjacent primitive.

**Timeline:** dbugs.ptsecurity disclosure 2026-07-03 → no mainstream reporting yet → discovery latency **early**.

**Why it matters:** Gitea is a common cost-effective alternative to GitLab / GitHub Enterprise in orgs that self-host source. A CVSS 9.6 unauth code execution against Gitea yields not just code-repository theft but the SSH keys, deploy tokens, and CI/CD secrets scoped to those repos. In the 30-day window with three CMS-extension mass-exploitation events (JCE, Mirasvit, Awesome Motive) and the Argo CD unpatched disclosure per 2026-07-03 report, self-hosted developer infrastructure is a first-class target.

**Mitigation:**
- Inventory Gitea deployments and align patch SLA to the vendor advisory (link expected via Gitea repo / release notes).
- Front any internet-facing Gitea instance with an authenticated reverse proxy or VPN; treat direct-DMZ Gitea as an emergency P0 misconfiguration.
- Rotate SSH deploy keys, CI/CD tokens, and any secrets scoped to Gitea-hosted repos in the last 30 days.
- Hunt Gitea audit logs for unexpected admin actions and repository additions during the disclosure window.

**Sources:** [dbugs.ptsecurity.com — PT-2026-55658 Gitea CVE-2026-58426 CVSS 9.6 + 7 companion CVEs](https://dbugs.ptsecurity.com)

---

### ARToken PhaaS Exposes 'EvilTokens' Microsoft 365 Device-Code Phishing Toolkit — 37x YoY Surge in Device-Code Attacks, 11+ Kits Now Selling This Technique
**Product:** Microsoft 365 accounts (device-code phishing) | **CVE:** None assigned | **First reported:** 2026-07-03

Researchers exposed the **ARToken** phishing-as-a-service (PhaaS) platform, an affiliate offering of the EvilTokens toolkit family. ARToken's admin panel exposes 80+ API endpoints and productizes attacks against Microsoft's OAuth 2.0 Device Authorization Grant flow: victims are lured to enter a legitimate Microsoft-issued code on the *real* microsoft.com login page, and Microsoft issues tokens directly to the attacker's device — completely bypassing MFA. Device-code phishing volume is up **37x** year-over-year; at least 11 PhaaS platforms now offer the technique. Infrastructure is Cloudflare Workers-hosted; the attackers create look-alike SharePoint tenants inside their own M365 workspace to mimic legitimate document-share invites. This is a **distinct** primitive from yesterday's 81M-login password-spray campaign against Microsoft 365 (LSHIY hosting cluster) — device-code phishing does not brute-force credentials at all, so lockout policies do not defend against it.

**Timeline:** Public exposure via BleepingComputer 2026-07-03; PhaaS platform active over the past 12 months per researcher timeline.

**Why it matters:** Device-code phishing sidesteps every MFA control, every Conditional Access policy that trusts a browser-based first-party sign-in, and every password-manager posture. Only Conditional Access policies that explicitly block device-code authentication defend against it. Corporate tenants that have not disabled the device-code flow in Conditional Access are one email away from token compromise for privileged users.

**Discovered by:** Not publicly attributed at time of writing.

**Mitigation:**
- Implement Conditional Access policy blocking the device-code authentication flow for all users except a documented set of legitimate device-flow scenarios (typically nil for most corporate tenants).
- Alert on any Entra ID sign-in with `authentication_details.authentication_method` = "Device Code" for accounts that do not have a business need.
- Review the 12-month back-window for token grants against the device-code flow; treat every successful device-code sign-in from an unrecognized device as a candidate compromise.
- Rotate refresh tokens for any high-value accounts (executives, IT admins, service principals) that could have been targeted.
- Add Microsoft-look-alike SharePoint tenant domain patterns to email-gateway detection; block invitation notifications from non-approved tenant IDs.

**Sources:** [BleepingComputer — ARToken PhaaS Exposes EvilTokens' Microsoft 365 Phishing Toolkit](https://www.bleepingcomputer.com/news/security/artoken-phaas-exposes-eviltokens-microsoft-365-phishing-toolkit/)

---

### Medtronic Data Breach Scoped At 3.8 Million Individuals; ShinyHunters Attribution Confirmed + Apparent Ransom Payment Signal
**Product:** Medtronic corporate IT (post-ShinyHunters compromise) | **CVE:** None assigned | **First reported:** 2026-07-03 (formal notification wave)

SecurityWeek reported 2026-07-03 that the Medtronic ShinyHunters compromise (originally noted 2026-07-03 report at unspecified scope) now confirms **3,834,294 individuals** notified per Indiana AG filing. Stolen data includes names, contact details, dates of birth, Social Security numbers, and health-related details. **ShinyHunters removed Medtronic from its leak site**, which SecurityWeek explicitly cites as a signal that Medtronic likely paid a ransom to recover the data. The compromise dates to April 2026, with the group posting Medtronic to the leak site 2026-04-17 claiming 9M+ records. This continues the ShinyHunters healthcare-and-manufacturing extortion cluster tracked since MEMORY 2026-06-16→06-19.

**Timeline:** April 2026 initial breach → 2026-04-17 leak-site posting → 2026-07 formal notification letters → 2026-07-03 SecurityWeek publishes 3.8M scope + apparent ransom-payment signal.

**Why it matters:** 3.8M PHI records at a medical-device manufacturer is a Notifiable Data Breach in every US state and under GDPR / HIPAA. The apparent ransom payment is a durable signal about ShinyHunters' current negotiation success rate — MEMORY 2026-06-16 tracked eight ShinyHunters victims across Salesforce+CRM+PeopleSoft chains and this is the third confirmed-payment inference of that cluster (Google Salesforce and Nottingham University being the prior two).

**Mitigation:**
- If your org receives Medtronic-manufactured device telemetry or shares HR/patient data with Medtronic-adjacent business partners: assume the exposed PHI subset may include your workforce or patient population; extend HaveIBeenPwned-class monitoring.
- Continue the MEMORY 2026-06-16→06-19 ShinyHunters cluster IR posture: rotate any Salesforce API tokens shared with third-party integrators (Klue-type dormant credentials remain a high-value ShinyHunters vector), enforce IP allowlists on Salesforce OAuth, and audit for the ShinyHunters-linked user-agent + hosting-provider patterns.
- Treat the payment signal as **calibration input**: ShinyHunters extortion works when the healthcare / manufacturing target is time-pressured by regulatory notification deadlines. Building the notification playbook in advance reduces payment coercion pressure on future incidents.

**Sources:** [SecurityWeek — Medtronic Data Breach Impacts 3.8 Million People](https://www.securityweek.com/medtronic-data-breach-impacts-3-8-million-people/)

---

## 🟡 MEDIUM

### FatFs Embedded Filesystem 7-CVE Batch (CVE-2026-6682 → CVE-2026-6688) — Malicious USB / SD / Firmware Yields "Any Physical Access = Jailbreak" On Millions Of Embedded Devices; No Upstream Patch
**Product:** FatFs (embedded FAT filesystem, powering ESP-IDF / STM32Cube / Zephyr / MicroPython / ArduPilot / Mbed / TizenRT / SWUpdate) | **CVE:** CVE-2026-6682, 6683, 6684, 6685, 6686, 6687, 6688 | **CVSS:** up to 7.6 | **Published:** 2026-07-03

runZero disclosed a seven-CVE FatFs batch. Three items are CVSS 7.6 (heap / buffer corruption reachable via malicious USB drive, SD card, or malformed firmware update), three are CVSS 4.6, one is CVSS 6.1. Only **CVE-2026-6684** has an upstream fix (R0.16); the other six are UNPATCHED because the FatFs maintainer is unresponsive and there is no security mailing list. Affected device categories: security cameras, drones, industrial controllers, hardware crypto wallets, generic IoT. Public PoCs, test harnesses, and QEMU examples are in runZero's companion GitHub repository.

**Mitigation:** For any FatFs-consuming embedded fleet within your scope: audit whether external-storage-media parsing runs on trust boundaries you actually enforce (security cameras, industrial PLCs), and constrain physical access to USB / SD slots on production hardware. This is a supply-side coordination problem — the FatFs upstream is inactive, so each vendor SDK must patch independently.

**Sources:** [TheHackerNews — Unpatched Flaws Disclosed in Filesystem Bundled Into Millions of Embedded Devices](https://thehackernews.com/2026/07/unpatched-flaws-disclosed-in-filesystem.html)

---

### 'Bad Epoll' Linux Kernel CVE-2026-46242 — Use-After-Free Root LPE Reachable From Chrome Renderer Sandbox With ~99% Success
**Product:** Linux kernel 6.4+ (and Android devices on kernel 6.4+; excludes Pixel 8-class 6.1 kernels) | **CVE:** CVE-2026-46242 | **Published:** 2026-07-03

Jaeyoung Chung disclosed a use-after-free bug in the epoll multiplexer (Linux kernel 6.4+, introduced by a 2023 refactor). Two kernel paths simultaneously clean up the same memory object — a six-instruction race window. Chung's PoC widens the window such that the exploit succeeds **~99% of the time on tested systems, triggerable from inside Chrome's renderer sandbox**. Upstream patch commit `a6dc643c6931`; distribution backports pending. No in-wild exploitation observed; only functional exploit is inside Google's kernelCTF. An Android version is under development.

**Mitigation:** Prioritize kernel updates on any Linux fleet running 6.4+ once distro backports land (RHEL / Ubuntu / Debian queues). For internet-facing services where Chrome-renderer-adjacent code paths could be reached (headless-Chrome scrapers, Puppeteer-based automation on shared hosts), treat this as an urgent kernel-refresh candidate.

**Sources:** [TheHackerNews — New "Bad Epoll" Linux Kernel Flaw Lets Unprivileged Users Gain Root](https://thehackernews.com/2026/07/new-bad-epoll-linux-kernel-flaw-lets.html)

---

### Rapid7 Metasploit Wrap-Up 2026-07-03 — Peyara Remote Mouse RCE Module + SMB-to-Meterpreter Capability + Miscellaneous
**Product:** Metasploit Framework | **Published:** 2026-07-03

Rapid7 shipped the weekly Metasploit Wrap-Up 2026-07-03. Notable additions: **Peyara Remote Mouse RCE exploit module** (client-side remote-input software, out-of-primary-scope but signal for developer-endpoint fleets), **SMB-to-Meterpreter** capability improvements (SMB relay pivot chain gets easier). No new Metasploit modules landed for any of the CVEs previously flagged as high-severity in our 30-day window that weren't already covered.

**Mitigation:** Continue the MEMORY 2026-06-12 Rapid7 ETR + Metasploit Wrap-Up polling cadence; log any Metasploit module additions to the internal exploitation-tempo tracker to inform patch prioritization.

**Sources:** [Rapid7 — Weekly Metasploit Update 2026-07-03](https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-07-03-2026/)

---

## 📋 Noted / Monitoring

**Google Chrome 150.0.7871.47 — 11-CVE Fresh Batch Including 3 x CVSS 9.6 Sandbox Escapes (CVE-2026-14017 Navigation, CVE-2026-14043 GetUserMedia UAF, CVE-2026-14056 Media Video Sandbox Escape)** — Client-side but sandbox-escape severity means push to endpoint fleet on 24-hour SLA. Distinct from the Chrome 149.x → 149.y 382-CVE batch flagged 2026-07-03.

**Microsoft Edge 24-CVE Batch On dbugs.ptsecurity 2026-07-03 (CVE-2026-58278 → CVE-2026-58524, CVE-2026-57987 → 57993, CVE-2026-56645, CVE-2026-45489, CVE-2026-55945)** — Chromium-family; largely mirrors the Chrome 150 batch. Client-side, fleet push.

**CVE-2026-56015 Perl Net::IP::LPM ≤ 1.10 — Heap OOB Read Via Unbounded Prefix Length** — Server-side Perl network utility; low-impact but broadly deployed. openwall oss-security 2026-07-03.

**"Pandemic of Incomplete Error Handling in the OpenSSL Ecosystem"** — Systemic error-handling research post on oss-security 2026-07-03. Not a single CVE — durable calibration input on error-suppression-as-vuln-class.

**Avalon Malware Framework + CrownX Ransomware Capabilities** — New modular malware distributed via phishing with credential theft + lateral movement + ransomware execution. THN 2026-07-03. Malware family signal, not vuln.

**North Korea-Linked npm Packages Impersonating Rollup Polyfills** — Malicious npm packages mimicking legitimate Rollup tooling to steal developer secrets. THN 2026-07-03; continues the DPRK developer-supply-chain cluster from MEMORY 2026-06-17 (UNK_Deadrop Overlord loader), Miasma expansion, and IronWorm.

**Papa Johns Surveillance-Based Advertising / Flock Cameras Vehicle-Fingerprint Surveillance / Schneier "Cybersecurity Mission Creep" Post** — Policy and surveillance-tradecraft calibration input from Schneier 2026-07-03; no operational action.

**Cloudflare "Attribution Business Insights" 2026-07-03** — Product launch for crawler-attribution dashboard; ecosystem change, no immediate action.

**CVE-2026-20841 Windows Notepad Markdown-Link RCE — Two Distinct PoCs Landed On GitHub Within ~40 Minutes On 2026-07-03** — Already covered in 30-day dedup window; the PoC surface widening is worth logging as exploitation-tempo signal, though the Notepad client-side vector remains out of primary scope.

**Solr / Joomla PBCK Mass-Exploitation Frameworks Both Land Same-Day (2026-07-03)** — Not a separate item; noted as pattern signal that GitHub is now the primary same-day distribution channel for mass-exploitation frameworks against CMS + enterprise-search classes.

**SharePoint CVE-2026-45659 BOD 26-04 FCEB Deadline Lands 2026-07-04 (TODAY, Saturday)** — Not a new advisory but calendar signal; every internet-facing SharePoint that missed the May patch and the July 2 KEV addition + 3-day deadline should be treated as candidate-compromised per Storm-2603 / Warlock attribution.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ 403 |
| Vendor advisories | rapid7.com, fortinet.com/blog/threat-research, blog.cloudflare.com/tag/security, msrc.microsoft.com/blog | ✅ / ⚠️ msrc empty |
| Research / OSINT | seclists.org/fulldisclosure, opencve.io, app.opencve.io, avleonov.com, dbugs.ptsecurity.com, github.com/0xMarcio/cve, github.com/search?q=CVE, kb.cert.org/vuls, openwall.com/lists/oss-security | ✅ |
| CVE databases | nvd.nist.gov, cve.mitre.org, cve.org | ❌ JS-only |
| Research labs | securitylab.github.com, googleprojectzero.blogspot.com → projectzero.google | ⚠️ no items in window |
| Threat intel / research | schneier.com | ✅ |
| Bug bounty | hackerone.com/hacktivity, bugcrowd.com/disclosures, attackerkb.com | ❌ JS/403/404 |
| Aggregators | packetstormsecurity.com → packetstorm.news | ⚠️ nav-only |
| Regional Tier-2 | habr.com/ru/companies/tomhunter, teletype.in/@cyberok, cert.gov.ua | ⚠️ silent >4-5 months |

**Errors:** cisa.gov (403) + cisa.gov/known-exploited-vulnerabilities-catalog (403) + attackerkb.com (403) + bugcrowd.com/disclosures (404) + hackerone.com/hacktivity (JS-only) + nvd.nist.gov (JS-only) + cve.mitre.org (JS-only redirect to cve.org) + cve.org (JS-only)
**Degraded:** msrc.microsoft.com/blog (redirect+nav-only) + packetstormsecurity.com (nav-only) + securitylab.github.com (no items — still 2026-05-22 batch, 43-day silence) + projectzero.google (no items — still 2026-05-13 post) + habr.com/ru/companies/tomhunter (silent 4.0-month) + teletype.in/@cyberok (silent 5.0-month) + cert.gov.ua (empty)
**CISA KEV:** Direct cisa.gov unreachable — KEV signal derived from BleepingComputer + SecurityWeek + TheHackerNews cross-reference. No new KEV adds confirmed in the 2026-07-03 → 2026-07-04 24-hour window. SharePoint CVE-2026-45659 3-day BOD 26-04 FCEB deadline lands today (Saturday 2026-07-04).

---

*Watchtower vulnerability-researcher | Cycle: 2026-07-04/night | Next: 2026-07-05/night*
