# Watchtower Night Report — 2026-05-03
**Cycle:** Night | **Generated:** 2026-05-03 00:15 UTC (2026-05-03T00:15:00Z)
**Sources checked:** 19/30 | **CISA KEV total:** 1 new addition since last report | **New KEV additions:** CVE-2026-31431 (Linux kernel CopyFail)

---

## 🔴 CRITICAL

### CVE-2026-41940 cPanel & WHM Authentication Bypass — "Sorry" Ransomware Mass-Encrypts 44,000 cPanel Servers, KEV Deadline Today (CVSS 9.8)
**Product:** cPanel & WHM | **CVE:** CVE-2026-41940 | **Status:** Active Mass Exploitation / KEV (deadline 2026-05-03)

Shadowserver confirms at least 44,000 cPanel-running IP addresses have been compromised since the CVE-2026-41940 missing-auth bug was disclosed on 2026-04-28, with attackers now layering a Go-based Linux ransomware called "Sorry" on top of the auth-bypass foothold. Sorry encrypts customer-site data with ChaCha20 + RSA-2048, appends `.sorry`, drops a `README.md` ransom note in every directory, and routes contact through Tox ID `3D7889AE…`. Hundreds of compromised victim sites are already indexed by Google. The CISA KEV remediation deadline for federal agencies is **today, 2026-05-03**.

**Timeline:** Disclosure 2026-04-28 → exploitation in the wild observed since 2026-02-23 → KEV addition 2026-04-30 → mass "Sorry" ransomware deployment confirmed 2026-05-02 → KEV deadline 2026-05-03.

**Why it matters:** cPanel hosts well over a million internet-facing shared-hosting servers and WHM runs the public web management plane on the majority of small/mid web hosters. A pre-auth bypass on the management plane that is now being weaponised for ransomware (rather than just credential theft) means every minute of patch lag = a compromised customer site you owe restoration on. Hosters that resell cPanel WHM must assume any unpatched instance is already touched and pre-position backups + IR.

**Discovered by:** Original disclosure WebPros International L.L.C.; "Sorry" ransomware analysis BleepingComputer + Shadowserver scanning.

**Mitigation:**
- Patch to cPanel & WHM 11.118.0.27 / 11.116.0.39 / 11.110.0.66 / 11.102.0.81 immediately.
- For any host with externally reachable WHM that was unpatched between 2026-02-23 and patch time: assume compromise. Hunt for `.sorry` files, `README.md` ransom notes, and the Tox contact ID; review WHM/cPanel access logs for unauthenticated requests to admin endpoints.
- Block management-plane access (port 2087/2083) from the public internet — restrict to bastion/VPN.
- Confirm clean backups exist for every customer site before applying any decryption-payment decision.
- Run watchtowr / Rapid7 IOC scanner published 2026-04-30 to triage your fleet.

**Sources:** [BleepingComputer — Sorry ransomware mass-exploits cPanel](https://www.bleepingcomputer.com/news/security/critrical-cpanel-flaw-mass-exploited-in-sorry-ransomware-attacks/) | [The Register — millions of sites could be hit](https://www.theregister.com/2026/05/01/critical_cpanel_vuln_hits_cisa/) | [HelpNetSecurity — exploited for months before patch](https://www.helpnetsecurity.com/2026/04/30/cpanel-zero-day-vulnerability-cve-2026-41940-exploited/) | [Rapid7 ETR](https://www.rapid7.com/blog/post/etr-cve-2026-41940-cpanel-whm-authentication-bypass/) | [labs.watchtowr — The Internet Is Falling Down](https://labs.watchtowr.com/the-internet-is-falling-down-falling-down-falling-down-cpanel-whm-authentication-bypass-cve-2026-41940/)

---

## 🟠 HIGH

### BufferZoneCorp Supply-Chain Campaign — 7 Ruby Gems + 9 Go Modules Hijack GitHub Actions, Append SSH Keys, Tamper go.sum
**Product:** RubyGems / Go module ecosystem (CI runners, GitHub Actions) | **CVE:** None | **CVSS:** N/A | **First reported:** 2026-05-01

Socket and BleepingComputer disclosed a multi-ecosystem credential-theft campaign run by GitHub user `BufferZoneCorp` (and RubyGems user `knot-theory`). Seven Ruby gems use a `knot-` prefix to mimic legitimate ActiveSupport/Devise/Rack libraries (e.g. `knot-activesupport-logger`, `knot-devise-jwt-helper`, `knot-rack-session-store`, `knot-rspec-formatter-json`); on install/runtime they harvest SSH keys, AWS credentials, `.npmrc`, and any secret-bearing env vars. Nine Go modules under `github.com/BufferZoneCorp/*` (e.g. `go-metrics-sdk`, `go-weather-sdk`, `go-retryablehttp`, `go-stdlib-ext`, `grpc-client`, `net-helper`, `config-loader`, `log-core`, `go-envconfig`) push the technique further: they tamper with `go.sum`, drop a fake `go` binary that intercepts and wraps calls to the real toolchain, and append the attacker's SSH public key to `~/.ssh/authorized_keys` for persistence on every CI runner that pulls them. Sleeper-style: packages were initially benign and weaponised post-trust. Packages have been yanked by RubyGems and blocked in the Go module proxy.

**Timeline:** Sleeper packages published over preceding weeks → weaponised payload pushed in late April → Socket disclosure 2026-05-01 → RubyGems pull / Go module proxy block same day.

**Why it matters:** This is the second multi-ecosystem CI-credential-theft campaign in five days (Mini Shai-Hulud npm/PyPI on 2026-04-29 / 05-01). The pattern is now: attackers publish dozens of plausibly-named libraries across multiple ecosystems, wait until a small population pulls them, then weaponise. The Go-side technique — wrapping the real `go` binary and writing to `authorized_keys` — is a new persistence pattern on self-hosted CI runners and bypasses package-pinning controls because the compromise happens via a transitive dependency rather than a direct one. Every team running self-hosted GitHub Actions on Ruby or Go projects should hunt now.

**Discovered by:** Socket research team (`socket.dev/blog`), reproduced by BleepingComputer and SC Media.

**Mitigation:**
- Search private registries and lockfiles for any `knot-*` Ruby gems and any `BufferZoneCorp/*` Go modules; remove and rotate every credential present in any CI runner that ever resolved them.
- Audit `~/.ssh/authorized_keys` on every self-hosted GHA runner for unknown keys (especially recently added, attacker may rotate over time).
- Verify `go.sum` integrity in your projects; investigate any unexplained changes to checksums.
- Pin Go dependencies to specific module versions and enable `GOFLAGS=-mod=readonly` on CI to detect tampering early.
- Treat the AI-agent config dirs already noted (`.claude/`, `.gemini/`, `.cursor/`, `.copilot/`, `.vscode/tasks.json`) and now also dependency-resolution artifacts (`go.sum`, `Gemfile.lock`, `package-lock.json`) as code that must be code-reviewed on every PR.

**Sources:** [Socket — Malicious Ruby Gems and Go Modules Steal Secrets](https://socket.dev/blog/malicious-ruby-gems-and-go-modules-steal-secrets-poison-ci) | [The Hacker News — Poisoned Ruby Gems and Go Modules](https://thehackernews.com/2026/05/poisoned-ruby-gems-and-go-modules.html) | [Cyberpress — Supply Chain Attack Targets GitHub Actions](https://cyberpress.org/supply-chain-attack-targets-github/) | [SC Media — sleeper packages for credential theft](https://www.scworld.com/brief/new-software-supply-chain-attack-uses-sleeper-packages-for-credential-theft-and-ci-tampering)

---

### CVE-2026-31431 Linux Kernel CopyFail — Added to CISA KEV Today, 168+ PoC Repos Public, Active Exploitation
**Product:** Linux kernel `algif_aead` (AF_ALG socket / crypto subsystem) | **CVE:** CVE-2026-31431 | **CVSS:** 7.8 | **Status:** Active Exploitation / KEV (added 2026-05-01) | **Previously reported:** Noted on 2026-04-30, 2026-05-01, 2026-05-02

CISA added CVE-2026-31431 to the Known Exploited Vulnerabilities catalog on 2026-05-01 with a remediation requirement, confirming the previously-noted local privilege escalation in the kernel's crypto subsystem (`algif_aead` copy-fail logic flaw, kernels 4.14+ shipped since Aug 2017, all major distributions affected) is now being used in the wild and not just experimentally. Public PoC count crossed 168 distinct repos on 2026-05-02 — Rust, C, Python, Zig, Go implementations — and at least one defensive-tooling project (BPF LSM blocker, Ansible remediation) has appeared. The flaw is straight-line logic, not a race window or kernel-specific offset, so reliability is high across distros.

**Why this is an UPDATE (not new):** Previously bracketed as out-of-remote-services scope and "Noted" because LPE-only; the KEV addition + active exploitation evidence + ubiquity of kernels >4.14 changes the calculus — every Linux server, jump host, container host, and self-hosted CI runner in the fleet is now in scope as a privilege-escalation pivot for any attacker who lands shell, including the supply-chain campaigns above.

**Mitigation:**
- Patch to 5.10.254+, 5.15.204+, 6.1.170+, 6.6.137+ (or distro backports).
- Where you cannot reboot in the next 24h, deploy the published BPF LSM blocker on each host (limits the syscall path).
- Hunt: any `algif_aead` syscall pattern from non-root processes is suspect; monitor for unexpected setuid escalations on patched-Apr distros.
- Prioritise Ubuntu 22.04/24.04, RHEL 8/9, Amazon Linux 2/2023, and SUSE 15-SP6 fleets first — these have the largest install base and confirmed PoC compatibility.

**Sources:** [CISA — CISA Adds One Known Exploited Vulnerability to Catalog (2026-05-01)](https://www.cisa.gov/news-events/alerts/2026/05/01/cisa-adds-one-known-exploited-vulnerability-catalog) | [BleepingComputer — Linux Copy Fail flaw grants root](https://www.bleepingcomputer.com/news/security/new-linux-copy-fail-flaw-grants-root-access/) | [Seclists OSS-Security — CopyFail thread (2026-05-02)](https://seclists.org/oss-sec/) | [github.com/0xMarcio/cve PoC index](https://github.com/0xMarcio/cve)

---

### CVE-2026-42167 ProFTPD mod_sql SQL Injection → Pre-Auth RCE / Auth Bypass
**Product:** ProFTPD <1.3.9a (mod_sql extension) | **CVE:** CVE-2026-42167 | **CVSS:** 8.1 | **First reported:** 2026-04-27 (patch); public technical analysis + PoC 2026-05-02

A logic flaw in ProFTPD's `is_escaped_text()` function lets an attacker submit a username that begins and ends with a single quote, defeating sanitization in the SQL logging path of `mod_sql`. Three attacker outcomes are documented in independent write-ups (ZeroPath, Shenlong CVE Platform):
- **RCE:** when ProFTPD's PostgreSQL DB user is a superuser, the attacker abuses `COPY TO PROGRAM` for arbitrary host code execution — pre-auth.
- **Authentication bypass:** when `mod_sql` is configured for SQLAuthenticate, attacker INSERTs a row into the users table giving themselves an account with chosen UID/home/password.
- **Privilege escalation:** attacker sets their home directory to `/`, giving filesystem-wide FTP browsing past the chroot.

Two public PoC repos already exist (`dinosn/proftpd-CVE-2026-42167-analysis`, `ZeroPathAI/proftpd-CVE-2026-42167-poc`).

**Timeline:** Patch landed in ProFTPD 1.3.9a 2026-04-27 → public technical analysis 2026-05-02 → PoCs published same day.

**Why it matters:** ProFTPD remains a common pick for managed-file-transfer / SFTP appliances, and `mod_sql` is enabled by default on many distro packages because it's the easiest way to wire FTP auth to an existing user database. Internet-exposed FTPS/FTP services are a long-running pivot in initial-access broker workflows. The PostgreSQL-superuser RCE path is the most dangerous and depends only on a common DBA misconfiguration.

**Discovered by:** Wojciech Reguła / SecuRing-tracked (researcher attribution per ZeroPath analysis).

**Mitigation:**
- Patch to ProFTPD 1.3.9a or later.
- If patching is delayed: comment out `LoadModule mod_sql.c` in `proftpd.conf` and restart.
- Audit `mod_sql` PostgreSQL connection strings — drop superuser to a dedicated low-priv role; revoke `pg_execute_server_program` and `COPY ... PROGRAM` privileges.
- Egress-restrict your FTPS hosts: a pre-auth RCE on an FTP server that can dial out is a fast pivot to the rest of the network.

**Sources:** [ZeroPath — CVE-2026-42167 auth bypass + privesc + RCE in ProFTPD](https://zeropath.com/blog/proftpd-cve-2026-42167-auth-bypass-privesc-rce) | [Shenlong CVE Platform — analysis + RCE PoC](https://cve.imfht.com/intel/591415?lang=en) | [GitHub Advisory GHSA-q25r-7mmc-3mcj](https://github.com/advisories/GHSA-q25r-7mmc-3mcj) | [PoC: ZeroPathAI/proftpd-CVE-2026-42167-poc](https://github.com/ZeroPathAI/proftpd-CVE-2026-42167-poc)

---

## 🟡 MEDIUM

### Trellix Source Code Repository Breach — "Portion" of Internal Code Accessed, No Exploitation Evidence Yet
**Product:** Trellix internal source-code repository (EDR / XDR vendor; merged McAfee Enterprise + FireEye assets) | **CVE:** None | **Published:** 2026-05-02

Trellix confirmed unauthorised access to a portion of its internal source-code repository. The vendor states there is no evidence of customer-data impact, no evidence the source code release/distribution pipeline was tampered with, and no evidence the accessed code has been exploited in the wild. Forensics and law enforcement engaged. No attribution, no scope detail (which products / which sub-repos), no breach date, no access duration, and no attacker entry vector have been disclosed. Trellix says updates will follow.

**Why this is medium not low:** Trellix is one of the largest EDR/XDR vendors in the enterprise market — source-code access has obvious follow-on bypass-development potential even if today's read-out is benign. Treat as a Trellix-ecosystem watching brief: if downstream signed-binary tampering, signed-Trellix-process supply-chain abuse, or new EDR-evasion tradecraft starts appearing in the next 30 days, this is a likely root cause to consider.

**Mitigation:**
- No customer-side patch action required as of 2026-05-03.
- For Trellix-deployed estates: monitor the vendor advisory channel for follow-up disclosure; pre-stage the IOC-ingestion playbook should signed-binary IOCs land.
- Validate SIEM/EDR rules cover anomalous Trellix process behaviour and unexpected updates from the Trellix update pipeline.

**Sources:** [The Hacker News — Trellix Confirms Source Code Breach](https://thehackernews.com/2026/05/trellix-confirms-source-code-breach.html) | [SecurityAffairs — Trellix discloses code repo breach](https://securityaffairs.com/191584/data-breach/trellix-discloses-the-breach-of-a-code-repository.html) | [CybersecurityNews — Trellix Source Code Breach](https://cybersecuritynews.com/trellix-source-code-breach/) | [Integrity360 advisory](https://insights.integrity360.com/threat-advisories/security-advisory-unauthorised-access-to-trellix-internal-source-code)

---

## 📋 Noted / Monitoring

**ConsentFix v3 (Push Security)** — Phishing/OAuth toolkit refinement automating Microsoft Azure CLI device-code abuse via Pipedream webhooks; v3 = scalability over earlier v1/v2 manual variants. Push notes "unclear whether v3 has gained traction yet" — track for adoption.

**EtherRAT (Atos TRC)** — March-to-April-2026 SEO-poisoning + GitHub-facade campaign; 44 fake repos spoofing PsExec/AzCopy/Sysmon/LAPS/KustoExplorer; payload uses Ethereum-blockchain C2 to resist takedown. Targets enterprise admins. Block direct GitHub→endpoint admin-tool downloads outside curated artifact stores.

**FIRESTARTER backdoor — federal Cisco Firepower campaign** — CISA Emergency Directive ED 25-03 deadline for federal agencies to inventory all Firepower / Secure Firewall devices was 2026-05-01 23:59 EST (yesterday). Backdoor enables persistence on Cisco ASA/FTD even after patching CVE-2025-20333 / CVE-2025-20362. If you operate ASA/Firepower edge devices and have not done a forensic check, do it now.

**Harvester / GoGra Linux backdoor (Symantec)** — Linux variant of the Harvester APT's GoGra backdoor uses the Microsoft Graph API + a hard-coded Outlook mailbox folder ("Zomato Pizza") for C2; targets observed in India/Afghanistan via VirusTotal artefacts. ELF disguised as PDF. Hunt for Graph API calls from Linux servers without legitimate Microsoft 365 integration.

**Sentry GHSA-rcmw-7mc7-3rj7** — Critical SAML SSO multi-organisation account-takeover advisory affecting `sentry` 21.12.0–26.4.0 published in the past 48h. Self-hosted multi-org Sentry only (Sentry SaaS already patched 2026-02-18). Patch self-hosted to current; verify `SENTRY_SINGLE_ORGANIZATION` posture.

**CVE-2026-30922 pyasn1** — Uncontrolled recursion in ASN.1 decoder enables DoS with sub-100KB input; affects ≤0.6.2. Wide indirect dependency surface (cryptography tooling, LDAP libs) — bump pinned versions.

**CVE-2026-7668 MikroTik RouterOS SCEP OOB read** — Out-of-bounds read in SCEP endpoint of RouterOS 6.49.8; CVSS 7.3, public exploit available. Niche but check internet-exposed MikroTik fleets.

**CVE-2026-7644 ChatGPTNextWeb / NextChat MCP authorization bypass** — Continues the MCP-server-as-attack-surface pattern (now mcp-atlassian, nginx-ui, OpenHarness, chatgpt-mcp-server, Branch Monkey MCP, Astro MCP, NextChat); CVSS 7.3. Add to MCP server inventory tracking.

**CVE-2026-2554 WCFM WordPress plugin** — Insecure direct object reference allowing user deletion (CVSS 8.1) — authenticated vendor-level required, but WCFM is a popular multivendor marketplace plugin.

**npm malware wave (GHSA-published 2026-05-01/02)** — `apple-pay-trust/cancelled`, `apple-internal-security-library-v99`, `gunpowder-ghost`, `sirens-lament`, `blackbeards-navigator` (and earlier `intercom-client` from PyTorch Lightning incident) — typo-/look-alike npm malware; no distribution numbers but worth a registry-scan.

**WordPress plugin batch (Positive Technologies dbugs 2026-04-30 → 05-02)** — User Verification (PT-2026-36569 CVSS 9.8), User Registration Advanced Fields (PT-2026-36566 CVSS 9.8), Profile Builder (PT-2026-36582 CVSS 8.1), Export/Import Users (PT-2026-36572 CVSS 8.8), WP Mail Gateway (PT-2026-36568 CVSS 8.8). All registration/auth-adjacent; high-risk on any membership-style site.

**Trendnet TEW-821DAP CVSS 9.0 (PT-2026-36586)** — Consumer/SOHO router; out of corporate-infra scope but worth flagging if your remote-worker fleet has these.

**ConnectWise ScreenConnect CVE-2024-1708** — Reminder: KEV addition 2026-04-29; if any ScreenConnect installs are still <23.9.8 in your environment, you are non-compliant with the federal deadline.

**Cybercrime sentencing — Goldberg + Martin (BlackCat ALPHV insider)** — Ryan Goldberg + Kevin Martin sentenced to 4 years 2026-05-01 for deploying BlackCat against US victims while employed at Sygnia / DigitalMint; useful policy reference for IR-program insider-risk language.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (403 — backfilled via THN/SecurityWeek/CISA-bulletins-via-search) |
| Vendor advisories | msrc.microsoft.com/blog, fortinet.com/blog/threat-research, blog.cloudflare.com/tag/security, kb.cert.org/vuls | ⚠️ (msrc empty, fortinet/cloudflare/cert no posts in window) |
| Research / OSINT | schneier.com, rapid7.com/blog, seclists.org/fulldisclosure, github.com/security-advisories, dbugs.ptsecurity.com, github.com/0xMarcio/cve, github.com/search?q=CVE, opencve.io | ✅ |
| CVE databases | nvd.nist.gov, cve.org, cve.mitre.org, app.opencve.io | ⚠️ (nvd/cve.org/cve.mitre JS-only) |
| Bug bounty / disclosure | hackerone.com/hacktivity, bugcrowd.com/disclosures, attackerkb.com, securitylab.github.com | ❌ (all 403/JS-only) |
| Project Zero / browser | projectzero.google | ✅ (no posts in window) |
| Russian-language community | habr.com/ru/companies/tomhunter, teletype.in/@cyberok, avleonov.com | ✅ (no posts in window) |
| Ukrainian govCERT | cert.gov.ua | ⚠️ (page empty) |
| Packetstorm | packetstorm.news | ⚠️ (limited content) |

**Errors:** CISA endpoints, attackerkb, bugcrowd, hackerone, cve.org, cve.mitre.org, securitylab.github.com — all unreachable via WebFetch (403 or JS-required). msrc.microsoft.com, nvd.nist.gov, packetstorm.news, cert.gov.ua — degraded (loaded but no usable content). Backfilled via WebSearch + secondary outlets.
**CISA KEV:** 1 new addition 2026-05-01 — CVE-2026-31431 (Linux kernel CopyFail). cPanel CVE-2026-41940 KEV deadline today.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-03/night | Next: 2026-05-04/night*
