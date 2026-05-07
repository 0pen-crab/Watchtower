# Watchtower Night Report — 2026-05-07
**Cycle:** Night | **Generated:** 2026-05-07 06:30 UTC (2026-05-07T06:30:00Z)
**Sources checked:** 18/30 | **CISA KEV total:** unchanged (last add CVE-2026-31431 on 2026-05-01) | **New KEV additions:** none reachable directly (cisa.gov 403)

---

## 🔴 CRITICAL

### Palo Alto Networks PAN-OS Captive Portal Pre-Auth RCE — CVE-2026-0300 (CVSS 9.3) — Active 0-Day Across PA-Series and VM-Series Firewalls, Patches Not Until 2026-05-13
**Product:** Palo Alto Networks PAN-OS — User-ID Authentication Portal (Captive Portal) | **CVE:** CVE-2026-0300 | **Status:** 0-Day, Unpatched, Active Exploitation Confirmed

Buffer overflow in the Captive Portal of the User-ID Authentication Portal lets an unauthenticated attacker send a crafted packet and execute arbitrary code as root on PA-Series hardware and VM-Series firewall instances. Palo Alto's advisory (security.paloaltonetworks.com/CVE-2026-0300) confirms "limited exploitation" against portals exposed to untrusted IPs and the public internet. Affected: PAN-OS 12.1 < 12.1.4-h5/12.1.7, 11.2 < 11.2.4-h17/.7-h13/.10-h6/.12, 11.1 < 11.1.4-h33 through 11.1.15, 10.2 < 10.2.7-h34 through 10.2.18-h6. CVSS drops to 8.7 when the portal is restricted to trusted internal IPs only. Fixes are scheduled to begin shipping 2026-05-13 — for the next ~6 days defenders are operating without a patch. Shadowserver tracks 5,800+ PAN-OS VM-Series firewalls publicly exposed (2,466 in Asia, 1,998 in North America), and that count is only the VM editions — physical PA-Series exposure is on top.

**Timeline:** Palo Alto advisory published 2026-05-06 → vendor confirmed limited exploitation in the wild same day → patches first available 2026-05-13 → PoC repository (`p3Nt3st3r-sTAr/CVE-2026-0300-POC`) appeared on GitHub within hours of the advisory.

**Why it matters:** This is the worst class of finding for our environment — pre-auth RCE on a perimeter device that thousands of orgs run as their internet-facing identity gateway, no patch for nearly a week, and active exploitation already happening. The Captive Portal sits on the same management plane that handles SSO and SAML for downstream apps; root on the firewall typically means lateral access to the directory infrastructure on the inside. Treat as the highest-priority advisory of the week — the operational tempo from 0-day disclosure to mass auth-bypass→ransomware (cPanel CVE-2026-41940 took 5 days) suggests the same playbook applies here.

**Discovered by:** Palo Alto Networks PSIRT (no external researcher credited in the advisory; exploitation observed by Unit 42 telemetry per the vendor advisory).

**Mitigation:**
- Disable the User-ID Authentication Portal (Captive Portal) entirely if not in active use — this is the only effective mitigation pre-patch.
- If the portal must remain enabled, restrict the ingress ACL to trusted internal subnets only (drops CVSS to 8.7, removes most of the internet-facing attack surface).
- Apply patches the moment they ship 2026-05-13 — the GitHub PoC means scanning will be commodity within hours of patch availability.
- Hunt for unexpected child processes of the Captive Portal handler and unusual outbound connections from the firewall management plane in the 2026-05-01 → patch window.
- Pull Shadowserver's exposure feed and confirm none of your firewalls are in the 5,800 already-exposed VM-Series count.

**Sources:** [Palo Alto Networks Security Advisory CVE-2026-0300](https://security.paloaltonetworks.com/CVE-2026-0300) | [BleepingComputer — Palo Alto Networks Warns of Actively Exploited Firewall Zero-Day](https://www.bleepingcomputer.com/news/security/palo-alto-networks-warns-of-actively-exploited-firewall-zero-day/) | [The Hacker News — Palo Alto PAN-OS Flaw Under Active Exploitation Enables RCE](https://thehackernews.com/2026/05/palo-alto-pan-os-flaw-under-active.html) | [SecurityWeek — Palo Alto Networks to Patch Zero-Day Exploited to Hack Firewalls](https://www.securityweek.com/palo-alto-networks-to-patch-zero-day-exploited-to-hack-firewalls/) | [Rapid7 ETR — Critical Buffer Overflow in PAN-OS User-ID Authentication Portal CVE-2026-0300](https://www.rapid7.com/blog/post/etr-critical-buffer-overflow-in-palo-alto-networks-pan-os-user-id-authentication-portal-cve-2026-0300/)

---

## 🟠 HIGH

### nginx-ui Unauthenticated RCE Via Backup Restore — CVE-2026-42238 (CVSS 9.0) — Third Pre-Auth RCE in This Project Inside Two Months
**Product:** nginx-ui (web management UI for nginx, Go) | **CVE:** CVE-2026-42238 | **CVSS:** 9.0 | **First reported:** 2026-05-06 (GitHub Security Advisory GHSA-4pvg-prr3-9cxr)

Three-bug chain on the `/api/backup/restore` endpoint: (1) the endpoint skips authentication during the first 10 minutes after every process start (and the timer resets on each restart, so an attacker who can also crash the process gets unlimited windows); (2) the restored archive overwrites `app.ini` and the SQLite DB without content validation; (3) the `TestConfigCmd` field of the restored config is passed verbatim to `/bin/sh -c` on application restart, giving OS command injection as whatever user nginx-ui runs as — root in the default Docker compose. All versions before 2.3.8 are affected. EPSS sits at 0.23%, but the PoC pattern is mechanical: hit the restore endpoint within the 10-minute window with a crafted backup containing a malicious `TestConfigCmd`, then trigger restart. This is the third unauthenticated RCE in nginx-ui in our reporting window after CVE-2026-33032 (April, MCP server path) and the earlier nginx-ui authn issues — the project has a recurring authorisation-handling weakness that warrants being on every web-tier inventory's to-deprecate-or-segment list.

**Mitigation:**
- Upgrade to nginx-ui 2.3.8 immediately.
- If you cannot upgrade, restrict TCP 9000 (default port) to a management VLAN only — never expose nginx-ui to the public internet.
- Ensure the nginx-ui service does not run as root (defense-in-depth against the OS command injection step).
- Hunt logs for any POST to `/api/backup/restore` from external IPs in the past 30 days; assume RCE on hit.
- Treat any nginx-ui in your fleet as a high-value pivot target — three pre-auth RCEs in two months is a code-quality signal, not bad luck.

**Sources:** [GitHub Security Advisory GHSA-4pvg-prr3-9cxr](https://github.com/advisories/GHSA-4pvg-prr3-9cxr)

---

### fast-jwt JWT Auth Bypass Via Empty HMAC Secret — CVE-2026-44351 (CVSS 9.1) — Async Key Resolver Returning Empty String Lets Anyone Mint Valid Tokens
**Product:** fast-jwt (Node.js JWT library, npm) | **CVE:** CVE-2026-44351 | **CVSS:** 9.1 | **First reported:** 2026-05-06 (GHSA-gmvf-9v4p-v8jc)

The library's async key resolver, when returning `''` or a zero-length Buffer, is silently converted by `crypto.createSecretKey` to a valid (empty) HMAC secret. A token signed with the empty key will pass verification. An unauthenticated attacker can therefore forge JWTs with arbitrary `sub`, `roles`, `scopes`, etc. as long as the application uses the standard JWKS pattern with a function-typed key resolver and HMAC algorithms remain in the allowed set (the default). The 1000-entry default cache amplifies blast radius — once a forged token is verified once, subsequent requests skip the check. Affected: fast-jwt ≤ 6.2.3; patched in 6.2.4.

**Mitigation:**
- Upgrade fast-jwt to 6.2.4 immediately.
- Audit your async key resolver code: it should never be possible to return an empty string / zero-length Buffer; throw on missing-key conditions instead.
- Restrict allowed signing algorithms in your verification config to RS256/ES256 only — disable the HMAC family unless you positively need it.
- Roll cached verification entries (or restart the service) after upgrading; the existing cache may contain forged tokens.
- Audit recent admin / privileged API calls for the past 30 days in services that use fast-jwt with JWKS-style resolvers.

**Sources:** [GitHub Security Advisory GHSA-gmvf-9v4p-v8jc](https://github.com/advisories/GHSA-gmvf-9v4p-v8jc)

---

### vm2 Sandbox Escape — Second Public RCE in 48 Hours (CVE-2026-26956 + CVE-2026-44007) Across 1.3M Weekly-Download Library Used By Online Code Sandboxes and AI Coding Platforms
**Product:** vm2 (Node.js sandbox library, npm) | **CVE:** CVE-2026-26956 (new today), CVE-2026-44007 (2026-05-05) | **CVSS:** Not yet finalised (rated Critical); GHSA pending | **First reported:** 2026-05-06 (BleepingComputer)

Yesterday's noted item (CVE-2026-44007 — sandbox escape in NodeVM when nesting is enabled, oss-security 2026-05-05) is now joined by an independent escape (CVE-2026-26956) reported by BleepingComputer 2026-05-06: a malicious script triggers a crafted `TypeError` inside the sandbox; vm2's WebAssembly exception handling on Node.js 25 (confirmed on 25.6.1) leaks the unsanitised host-side error object back into the sandbox; constructor-chain walking from the leaked object recovers Node.js internals (`process`) and gives full host RCE. Public PoC published. vm2 receives 1.3M weekly downloads and is the primary sandbox in many SaaS code-execution platforms, automation tools, AI coding assistants that run user-supplied snippets, and online IDE products. Patched in 3.10.5 (CVE-2026-26956); CVE-2026-44007 patched in the parallel release line — pull 3.11.2 (latest) to cover both.

**Mitigation:**
- Upgrade vm2 to 3.11.2 — both CVEs are addressed by the latest line.
- Strategic action: vm2 has had 8+ historical sandbox escapes plus 2 new ones in 48 hours. If you are running it in production to evaluate untrusted user code, plan the migration to `isolated-vm` or a true VM/container-isolated execution backend now.
- Treat any host that has executed untrusted user code via vm2 in the last 7 days as compromised until proven otherwise — pull `process.env`, harvest tokens, harvest mounted secrets paths.

**Sources:** [BleepingComputer — Critical vm2 Sandbox Bug Lets Attackers Execute Code on Hosts](https://www.bleepingcomputer.com/news/security/critical-vm2-sandbox-bug-lets-attackers-execute-code-on-hosts/) | [oss-security 2026/05/05 — vm2 sandbox escape (CVE-2026-44007)](https://www.openwall.com/lists/oss-security/2026/05/05/11)

---

### ShinyHunters → Anodot SaaS Token Theft → Vimeo + "Dozens" of Customers Compromised — New SaaS-Vendor-Token-as-Initial-Access Cluster
**Product:** Anodot (SaaS data anomaly detection) — used as supply-chain pivot to its customers | **CVE:** None | **CVSS:** N/A | **First reported:** 2026-04-27 (Vimeo disclosure); pivot pattern made public 2026-05-06

Vimeo confirmed 2026-04-27 that 119,000 individuals' email addresses, names, and video metadata were exposed after attackers obtained valid Anodot authentication tokens and used them to query Vimeo's systems via the Anodot integration. ShinyHunters has since posted a 106 GB archive on its leak site and tells reporters the same Anodot-token pivot was used against "dozens of organizations across multiple industries." Anodot is a SaaS data-monitoring product that is given direct API access (with broad read scopes) to customer telemetry and frequently touches production data warehouses, billing systems, and product event streams — the access scope makes a single compromised SaaS vendor a high-value reusable beachhead. This is the same pattern class as the DigiCert support-portal compromise (covered 2026-05-05) but with the SaaS-API-token vector instead of support-channel: trust-relationship-as-initial-access against SaaS vendors that customers grant deep read access.

**Mitigation:**
- Immediately inventory every Anodot integration in your fleet (look for Anodot API keys / OAuth clients, Anodot-installed IPs in firewall logs, Anodot OAuth grants in IDP audit logs).
- Rotate all Anodot-issued credentials and revoke the integration where possible until Anodot publishes specific IOC guidance.
- Treat any SaaS vendor with broad read access to your telemetry / data warehouse as a Tier-1 supply-chain risk — audit token scopes and apply per-tenant network egress restrictions.
- Hunt for unexpected data-export volume from any SaaS vendor's IP space in the last 60 days; the Vimeo case was caught only when archive size showed up on the leak site.
- Add Anodot to the same monitoring tier as your IDP — its tokens carry equivalent read-side blast radius.

**Sources:** [BleepingComputer — Vimeo Data Breach Exposes Personal Information of 119,000 People](https://www.bleepingcomputer.com/news/security/vimeo-data-breach-exposes-personal-information-of-119-000-people/)

---

### MuddyWater (Iran/MOIS) Uses Microsoft Teams Social Engineering and Chaos Ransomware as Decoy — Custom Game.exe Backdoor + Stagecomp/Darkcomp + Code-Signed Tooling
**Product:** Enterprise Microsoft Teams + targeted endpoints (cross-sector, US per Rapid7 telemetry) | **CVE:** None | **CVSS:** N/A | **First reported:** 2026-05-06 (Rapid7 / The Hacker News / SecurityWeek)

Rapid7 detailed an Iran-aligned MuddyWater intrusion that opens with Microsoft Teams contact (impersonating IT helpdesk), pivots through fake Microsoft Quick Assist phishing pages or password-prompt text-file harvesting, then modifies the victim's MFA settings to maintain access. The intruder deploys RDP / DWAgent / AnyDesk for persistence, drops a custom loader (`ms_upd.exe`) that fetches a 12-command custom backdoor (`Game.exe`) supporting PowerShell/CMD execution and file ops, and uses Chaos ransomware purely as decoy / cover. Stagecomp and Darkcomp samples (both signed with MuddyWater's known certificate) confirm attribution at moderate confidence; alias set: Static Kitten, Mango Sandstorm, Seedworm. This is now the seventh enterprise intrusion in 30 days using the Teams-helpdesk-impersonation → MFA-tamper chain (BlackFile, SNOW, Cordial Spider, Snarky Spider, Microsoft "Code-of-Conduct" AiTM, VENOMOUS#HELPER, MuddyWater) — at this volume the chain is no longer a single-actor TTP but the mainstream initial-access pattern of 2026-Q2.

**Mitigation:**
- Make Microsoft Teams external chat / external meeting invitations require explicit per-recipient allow-list approval, or disable external chat outside business hours.
- Alert on any user-side change to MFA registration (new authenticator app, new phone number, new FIDO key) — the Teams chain hinges on this step.
- Block AnyDesk / DWAgent / unsigned RDP wrappers at the EDR / app-control tier unless the user is on the IT-tooling allow-list.
- IOC: hash sets for `Game.exe`, `ms_upd.exe`, Stagecomp, and Darkcomp per Rapid7's writeup.
- Train helpdesk and frontline users on the Teams-impersonation pattern — the SE chain depends on the user accepting the chat and downloading the loader.

**Sources:** [BleepingComputer — MuddyWater Hackers Use Chaos Ransomware as a Decoy](https://www.bleepingcomputer.com/news/security/muddywater-hackers-use-chaos-ransomware-as-a-decoy-in-attacks/) | [The Hacker News — MuddyWater Uses Microsoft Teams to Steal Credentials](https://thehackernews.com/2026/05/muddywater-uses-microsoft-teams-to.html) | [SecurityWeek — Iranian APT Intrusion Masquerades as Chaos Ransomware Attack](https://www.securityweek.com/iranian-apt-intrusion-masquerades-as-chaos-ransomware-attack/)

---

### 🔄 UPDATE — DAEMON Tools Trojanised Installers Confirmed by Vendor; Clean Version Released; "Dozen" Government & Scientific Sector Hosts Hit With QUIC RAT Second Stage
**Product:** DAEMON Tools (signed Windows installer, supply-chain distribution channel) | **CVE:** None | **Status:** Vendor-confirmed; clean version available | **Previous threat score:** 7

Yesterday (2026-05-06) we covered Kaspersky's disclosure of the DAEMON Tools installer trojanisation since 2026-04-08. New developments today: (1) DAEMON Tools developers publicly confirmed the breach, identified the affected installer build IDs (v12.5.0.2421-2434), and released a malware-free version. (2) SecurityWeek reports the second-stage QUIC RAT was deployed to "a dozen targeted hosts" in government and scientific entities globally — a much narrower victim set than the broad first-stage stealer install base, suggesting the campaign was a targeted intelligence-gathering operation that used a wide-net commercial-software trojanisation as the funnel. The attribution to "likely Chinese-speaking actor" (Kaspersky) holds. Score drops slightly because there is now a vendor-supplied remediation path, but the original breach window is unchanged and any host that ran an installer between 2026-04-08 and 2026-05-06 should still be IR-triaged.

**Mitigation:**
- Update DAEMON Tools to the developer-released clean version on every host that has installed v12.5.0.2421–2434.
- Audit installer download-and-execute telemetry for the 2026-04-08 → 2026-05-06 window across the fleet.
- Particular focus: any government / scientific / R&D endpoint that pulled DAEMON Tools in the window — Kaspersky's "dozen-host" QUIC RAT victim count means individual targeted infections are out there in those sectors.
- Add the QUIC-protocol C2 indicator to NDR rules for the next 30 days (QUIC C2 to non-Cloudflare / non-Google IPs from a developer workstation is a notable signal).

**Sources:** [BleepingComputer — DAEMON Tools Devs Confirm Breach, Release Malware-Free Version](https://www.bleepingcomputer.com/news/security/daemon-tools-devs-confirm-breach-release-malware-free-version/) | [SecurityWeek — Government, Scientific Entities Hit via DAEMON Tools Supply Chain Attack](https://www.securityweek.com/government-scientific-entities-hit-via-daemon-tools-supply-chain-attack/)

---

## 🟡 MEDIUM

### Apache Wicket — Four-CVE Batch (XSS, Path Traversal, ResourceGuard Bypass, JS-Sequence Escape) — CVE-2026-40010 / 42509 / 43646 / 43975
**Product:** Apache Wicket (Java web framework) | **CVE:** CVE-2026-40010, CVE-2026-42509, CVE-2026-43646, CVE-2026-43975 | **Published:** 2026-05-06 (oss-security)

Coordinated four-CVE disclosure on the Apache Wicket security mailing list: AuthenticatedWebSession session-fixation (40010), JavaScript-sequence escape via crafted strings enabling stored XSS (42509), `PackageResourceGuard` bypass via malicious URLs (43646), and path traversal in `FolderUploadsFileManager` (43975). Affected: Wicket 8.0.0–8.17.0, 9.0.0–9.22.0, 10.0.0–10.8.0. All four are fixed in 10.9.0 (and corresponding 8.x / 9.x backports). Wicket is widely deployed in enterprise Java apps (especially European banking, e-government, and ERP front-ends); the path traversal is the most directly weaponisable item in the batch — pre-auth file read on misconfigured upload-folder endpoints.

**Mitigation:** Upgrade Wicket to 10.9.0, 9.x latest, or 8.x latest; disable `FolderUploadsFileManager` on internet-facing endpoints if you cannot upgrade immediately; treat any Wicket app that accepts file upload as an immediate triage target.

**Sources:** [oss-security 2026/05/06 — Apache Wicket security batch](https://www.openwall.com/lists/oss-security/2026/05/06/) (messages /2, /3, /4, /5)

---

### Quarkus Authorization Bypass — CVE-2026-39852 (GHSL-2026-099)
**Product:** Quarkus (Red Hat / IBM Java cloud-native framework) | **CVE:** CVE-2026-39852 | **Published:** 2026-05-06 (GitHub Security Lab — Peter Stöckli)

GitHub Security Lab disclosed an authorization bypass in Quarkus on 2026-05-06. Public details are sparse pending the upstream advisory, but the GHSL author and the framework involved (Quarkus is the dominant Java cloud-native framework on OpenShift / OKD and the basis of many serverless Java functions) make this worth front-of-queue attention. Score is provisional — expect to revise once the advisory body and CVSS land.

**Mitigation:** Watch for the upstream Quarkus security advisory; assume any internet-facing Quarkus service may be exposed until you can confirm the affected version range. If you run Quarkus, subscribe to the security mailing list now.

**Sources:** [GitHub Security Lab — CVE-2026-39852 Quarkus Authorization Bypass (GHSL-2026-099)](https://github.com/advisories/GHSL-2026-099)

---

### Tor 0.4.9.7 — Six Security Fixes (TROVE-2026-006 → -011)
**Product:** Tor (anonymity network — relay and client software) | **CVE:** TROVE-2026-006 through TROVE-2026-011 | **Published:** 2026-05-06 (oss-security)

Tor 0.4.9.7 ships with six fixes: out-of-bounds reads in END/TRUNCATE/TRUNCATED cell handling and in malformed BEGIN cell handling on relays/onion services, a null-pointer dereference on out-of-sequence CERT cells, conflux-leg BEGIN_DIR misuse, conflux/relay queue accounting error, and a pathbias double-close client crash. Affected versions span 0.1.1.1-alpha through 0.4.8.1-alpha — i.e., effectively every Tor build prior to today. Defensive interest is moderate: Tor relays are not typically internet-facing in our scope, but anyone running a Tor node, an Onion Service, or any product that bundles Tor (Brave Tor windows, Tails, Whonix, custom anonymity-preserving tooling) should pull 0.4.9.7.

**Mitigation:** Upgrade to Tor 0.4.9.7. If you ship a product that bundles Tor, expedite the rebuild.

**Sources:** [oss-security 2026/05/06/8 — Tor 0.4.9.7 release announcement](https://www.openwall.com/lists/oss-security/2026/05/06/8)

---

## 📋 Noted / Monitoring

**CVE-2026-20188 — Cisco Crosswork Network Controller / NSO DoS** — Inadequate connection rate limiting in CNC ≤ 7.1 and NSO ≤ 6.3 lets unauthenticated attackers exhaust the connection pool; recovery requires manual reboot. Not internet-facing in most deployments. Patches: CNC 7.2 / NSO 6.4.1.3 / 6.5.

**Mirai-based xlabs_v1 botnet exploiting ADB on TCP/5555** — DDoS-for-hire variant targeting Android devices with exposed ADB. Out of our public-facing infrastructure scope, but firewall any 5555/tcp egress to internal networks if you have Android-derived embedded devices on the corporate net.

**UAT-8302 China-aligned APT (Cisco Talos)** — Government targeting in South America (since late 2024) and southeastern Europe. NetDraft / NosyDoor backdoor (.NET FINALDRAFT variant), shared infrastructure with Ink Dragon / CL-STA-0049 / Earth Alux / Jewelbug / REF7707. Tools: CloudSorcerer, SNOWLIGHT/SNOWRUST, Deed RAT, Zingdoor, Draculoader, Stowaway, SoftEther. Worth tracking if you operate gov-adjacent or critical-infrastructure assets in those regions.

**pnpm 11 — Supply-chain protection defaults** (2026-05-04, Socket) — pnpm now defaults to a 1-day Minimum Release Age and blocks "exotic subdeps." Direct counter-measure to the Mini Shai-Hulud / TeamPCP rapid-publish pattern. Recommend rolling pnpm 11 across all CI / dev environments where you don't need cutting-edge package versions same-day.

**PyPI fixes high-severity audit findings** (2026-05-01, Socket / PyPI) — Permission bugs, stale access following package transfers, and authorization bypass weaknesses resolved. Defensive update — no action required by package consumers, but worth noting that PyPI is hardening at the same tempo as the supply-chain attack tempo is rising.

**Oracle launches monthly Critical Patch Updates** — Cadence change from quarterly to monthly. Will increase patch volume but should reduce the "n-day window" from up to 90 days to ~30. Plan for the operational impact in your patch cycle.

**CISA "CI Fortify" critical-infrastructure resilience program** — Guidance and exercises to prepare OT operators for geopolitical cyber conflict — worth pulling for any team that runs OT-adjacent assets.

**Google Android Binary Transparency** — Public cryptographic logs for shipped APKs, modeled on Certificate Transparency. Defensive measure against supply-chain tampering of Play Store apps. Not a finding for our scope but a structural improvement to the broader ecosystem.

**Rowhammer attack against NVIDIA GPUs (Schneier blog 2026-05-06)** — Research demonstration of rowhammer on NVIDIA GDDR; can compromise host systems. Out of immediate public-facing-services scope, but watch for disclosure of which GPU SKUs / firmware versions are affected — relevant to data-center GPU clusters once it's mapped to specific hardware.

**DarkSword iOS exploit chain leaked (Schneier 2026-05-05)** — Six-zero-day chain originally used by a commercial spyware vendor, now public. Out of scope (mobile only) but IOC packs are circulating; iOS fleet management should accelerate the next OS update.

**CVE-2026-44364 misp-modules CSRF (pip)** — Missing CSRF protection in the website home blueprint. MISP threat-intel users only.

**CVE-2026-42555 valtimo SpEL injection RCE (Maven)** — RCE by admin users on the BPM platform; admin-only attack so internal-only impact.

**Composer phpmyfaq — Unauth SQL injection via User-Agent header in BuiltinCaptcha + 2FA brute-force on /admin/check** — phpmyfaq users only; if you run it, patch and rotate admin creds.

**CVE-2026-44262 scramble (Composer / PHP) RCE** — Eval of user-controlled validation rules; PHP-stack-only impact.

**CVE-2026-43948 wger ≤ 2.5 (pip)** — `gym=None` authorization-comparison bug allows cross-tenant password reset with plaintext disclosure in the response body. Niche fitness/gym software; patched in 2.6.

**CVE-2026-5081 Apache::Session::Generate::ModUniqueId (Perl) — insecure session IDs** — Session IDs with insufficient entropy generated by mod_unique_id derivative. Perl-only; patch via CPAN.

**CVE-2026-40562 Gazelle (Perl) HTTP request smuggling via header precedence** — Perl reverse-proxy-adjacent. Narrow.

**axonflow (Go) multi-tenant isolation / access-control fix** — Critical-rated GHSA, no CVE. Multi-tenant SaaS framework — relevant only if you've adopted axonflow.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com | ✅ |
| Government / KEV | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog, cert.gov.ua | ❌ (cisa 403; cert.gov.ua empty) |
| Vendor / vuln disclosure | rapid7.com, fortinet.com/blog/threat-research, securitylab.github.com, msrc.microsoft.com/blog, blog.cloudflare.com/tag/security, attackerkb.com | ✅ except msrc/attackerkb (JS / 403) |
| OSS / CVE feeds | seclists.org/fulldisclosure, openwall.com/lists/oss-security, opencve.io, github.com/search?q=CVE, github.com/0xMarcio/cve, kb.cert.org/vuls | ✅ |
| NVD-class | nvd.nist.gov, cve.mitre.org, cve.org | ❌ (all JS / no extractable data) |
| Bug bounty | hackerone.com/hacktivity, bugcrowd.com/disclosures | ❌ (JS / 404) |
| Research / OSINT | krebsonsecurity.com, schneier.com, avleonov.com, googleprojectzero.blogspot.com, dbugs.ptsecurity.com, habr.com/ru/companies/tomhunter, teletype.in/@cyberok | ✅ except googleprojectzero (redirect/JS) |
| Off-list productive | openwall.com/lists/oss-security (counted above), socket.dev/blog, labs.watchtowr.com, trendmicro.com, securelist.com (Kaspersky) | ✅ socket/labs.watchtowr; ❌ trendmicro 403, securelist ECONNREFUSED |
| Packet aggregator | packetstormsecurity.com (now packetstorm.news) | ❌ (only TOS page reachable; advisory listings not extractable) |

**Total active sources:** 30 | **Checked:** 18 | **With findings:** 10 | **Unreachable (12):** cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog, attackerkb.com, packetstormsecurity.com, nvd.nist.gov, cve.mitre.org, cve.org, googleprojectzero.blogspot.com, msrc.microsoft.com/blog, hackerone.com/hacktivity, bugcrowd.com/disclosures, cert.gov.ua

**CISA KEV:** Direct fetch returns 403 (consistent with prior runs). No new KEV additions surfaced via THN/Krebs/SecurityWeek today; last confirmed addition is CVE-2026-31431 (CopyFail) on 2026-05-01.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-07/night | Next: 2026-05-08/night*
