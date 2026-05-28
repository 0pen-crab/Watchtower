# Watchtower Night Report — 2026-05-28
**Cycle:** Night | **Generated:** 2026-05-28 22:00 UTC (2026-05-28T22:00:00Z)
**Sources checked:** 20/30 | **CISA KEV total:** ~1,400 (estimate) | **New KEV additions:** 1 (CVE-2026-48172 LiteSpeed cPanel Plugin, KEV-added 2026-05-26)

---

## 🔴 CRITICAL

### LiteSpeed cPanel Plugin CVE-2026-48172 (CVSS 10.0) — Any-User-to-Root Privilege Escalation Actively Exploited, KEV-Listed With 4-Day Federal Deadline
**Product:** LiteSpeed cPanel/WHM Plugin (versions 2.3 → 2.4.4, fixed in 2.4.5; WHM Plugin 5.3.1.0 bundles cPanel plugin 2.4.7) | **CVE:** CVE-2026-48172 | **Status:** 0-Day → Patched / Active Exploitation / KEV

Improper privilege management (CWE-266) in the `lsws.redisAble` function of the LiteSpeed cPanel Plugin lets any authenticated cPanel user — regardless of role or privilege level — execute arbitrary scripts with root privileges on the underlying shared-hosting host. LiteSpeed's coordinated 2026-05-27 advisory confirms in-the-wild exploitation; CISA added the CVE to KEV on 2026-05-26 under BOD 22-01 with a Federal-civilian remediation deadline of 2026-05-29 (a 4-day window — matching the tempo of the cPanel CVE-2026-41940 advisory that monetised to "Sorry" Linux ransomware against 44k IPs within 5 days, MEMORY 2026-05-03). LiteSpeed has not published exploitation indicators.

**Timeline:** 2026-05-25 LiteSpeed advisory authored → 2026-05-26 CISA KEV addition with 2026-05-29 Federal deadline → 2026-05-27 cross-vendor reporting (BleepingComputer / SecurityWeek / TheHackerNews / GBHackers) → 2026-05-28 mass-fleet patching window closes for Federal civilian.

**Why it matters:** This is the second cPanel-ecosystem any-user-to-root primitive in 60 days (after CVE-2026-41940). cPanel/WHM shared-hosting environments host hundreds of thousands of customer-tenant sites per appliance; a single low-privileged user account compromise yields root across every co-tenant site, every customer credential database, and every TLS cert on the host. Web-hosting providers in fleet must patch LSWS plugin to 2.4.5+ (WHM plugin 5.3.1.0+) within hours, not days. Expect ransomware-affiliate monetisation tempo identical to CVE-2026-41940 (≤5 days) given the established Sorry / Webpros-ecosystem precedent.

**Discovered by:** LiteSpeed Technologies internal triage following exploitation telemetry (researcher name not disclosed).

**Mitigation:**
- Upgrade LiteSpeed cPanel Plugin to version 2.4.5 or later (or upgrade WHM Plugin to 5.3.1.0+ which bundles cPanel plugin 2.4.7).
- If patching is not possible immediately, disable the LiteSpeed cPanel Plugin entirely until upgraded — the plugin is non-critical for LSWS operation.
- Audit cPanel user account inventory for newly-created admin accounts, cron entries running as root, and `~/.ssh/authorized_keys` modifications across all tenant accounts in the last 14 days.
- Rotate all credentials stored on shared-hosting tenants (database passwords, API keys, FTP passwords) for any tenant on an unpatched host.
- Federal civilian agencies: enforce BOD 22-01 deadline 2026-05-29.

**Sources:** [The Hacker News — LiteSpeed cPanel Plugin CVE-2026-48172 Exploited to Run Scripts as Root](https://thehackernews.com/2026/05/litespeed-cpanel-plugin-cve-2026-48172.html) | [SecurityWeek — CISA Urges Immediate Patching of Exploited LiteSpeed cPanel Plugin Zero-Day](https://www.securityweek.com/cisa-urges-immediate-patching-of-exploited-litespeed-cpanel-plugin-zero-day/) | [BleepingComputer — CISA Gives Feds 4 Days to Patch Actively Exploited cPanel Plugin Flaw](https://www.bleepingcomputer.com/news/security/cisa-gives-feds-4-days-to-patch-actively-exploited-cpanel-plugin-flaw/)

---

### Samba Unauth RCE Pair — CVE-2026-4408 (DCE/RPC SAMR %u, CVSS 10.0) + CVE-2026-4480 (Printing %J, CVSS 10.0)
**Product:** Samba (all currently-supported branches prior to 4.24.3 / 4.23.8 / 4.22.10) — both CVEs apply to file servers + classic (non-AD) domain controllers and Samba print servers | **CVE:** CVE-2026-4408, CVE-2026-4480 | **Status:** Patched (2026-05-26), no confirmed ITW yet

The Samba team shipped a six-CVE batch on 2026-05-26 led by two CVSS-10.0 unauthenticated RCE primitives: (1) **CVE-2026-4408** — the DCE/RPC SAMR password-validation handler passes the client-controlled username to the `check password script` directive via the `%u` substitution without escaping shell meta-characters, yielding unauth RCE as the `samba-dcerpcd` process user against any deployment that configures `check password script` with `%u` and runs `samba-dcerpcd` as a system service; (2) **CVE-2026-4480** — the printing subsystem passes the client-controlled job description to the `print command` directive via the `%J` substitution without escaping, yielding unauth RCE against any Samba print server that runs `printing = bsd` or `printing = sysv` with `%J` in the print command (default `printing = cups` and `printing = iprint` are not vulnerable). Print servers typically permit guest access by default, lowering the auth barrier further. No public PoC yet; no confirmed ITW yet.

**Timeline:** 2026-05-26 Samba 4.24.3 / 4.23.8 / 4.22.10 released with six-CVE security advisory → 2026-05-27 cross-vendor distro patches begin shipping (Debian, Ubuntu, Red Hat).

**Why it matters:** Samba is one of the most-widely-deployed enterprise file-sharing services on Linux/Unix; even fleets that have moved to AD-only deployments often retain Samba file shares for legacy or cross-platform integration. Both primitives are unauthenticated and require only a network-reachable Samba service in the standard misconfiguration. Print-server `%J` substitution is the broader-exposure of the two (guest-printing common in branch-office / hospital / education / SMB environments). Expect Mirai-class scanners to incorporate this within 14 days; expect APT exploitation against high-value Linux file servers within 7 days.

**Discovered by:** Coordinated disclosure to the Samba security team (researcher attribution per Samba advisory: external reporters).

**Mitigation:**
- Upgrade Samba to 4.24.3 / 4.23.8 / 4.22.10 immediately on every Samba server in fleet (file, print, classic DC).
- Workarounds for CVE-2026-4408: switch from `check password script` with `%u` substitution to on-demand RPC helpers OR retrieve usernames via the `SAMBA_CPS_ACCOUNT_NAME` environment variable.
- Workarounds for CVE-2026-4480: remove `%J` from `print command` configuration OR switch to `printing = cups` / `printing = iprint` (which are not vulnerable).
- Audit all internet-exposed Samba services with smbclient/nmap against ports 139/445 (file-share) and 631/* (print) and prioritise Internet-facing instances first.
- For Samba file servers with `check password script` configured, treat as presumptive-RCE-class until proven patched.

**Sources:** [Samba Security Advisory CVE-2026-4408](https://www.samba.org/samba/security/CVE-2026-4408.html) | [Samba Security Advisory CVE-2026-4480](https://www.samba.org/samba/security/CVE-2026-4480.html) | [oss-security mailing list, 2026-05-27](https://www.openwall.com/lists/oss-security/2026/05/27/)

---

## 🟠 HIGH

### Gitea CVE-2026-27771 — Unauthenticated Private Container Image Exposure on 30,000+ Instances
**Product:** Gitea self-hosted Git platform (all versions prior to 1.26.2, fixed 1.26.2) — Container Registry feature | **CVE:** CVE-2026-27771 | **CVSS:** Not yet assigned (vendor-described "high impact") | **First reported:** 2026-05-27

Noscope disclosed 2026-05-27 a four-year-latent authorization flaw in Gitea's Container Registry: the `private` designation on a container repository did not enforce authentication on container image pulls; any unauthenticated remote attacker could pull private container images from any vulnerable Gitea instance without an account or password. The flaw affects ~30,000 internet-facing Gitea instances across 30+ countries; concentration in China, U.S., Germany, France, U.K. with affected organizations in healthcare, aerospace, retail, and ISPs. Because container images frequently bundle build-time secrets (database credentials, API keys, internal service endpoints, TLS certs, hardcoded environment variables), each successful pull is a potential secret-disclosure event. Patched in Gitea 1.26.2 (released alongside disclosure).

**Mitigation:**
- Upgrade Gitea to 1.26.2 or later on every self-hosted instance.
- If patching is delayed, set `[service].REQUIRE_SIGNIN_VIEW=true` in `app.ini` as the documented workaround (forces authentication for all repo views including container registry).
- Treat every private container image pulled from a vulnerable Gitea instance during the 4-year window as potentially-disclosed — rotate every credential, API key, TLS private key, and signing key referenced in image layers / build args / environment variables across the affected window.
- Audit Gitea instance access logs (if retained) for container manifest/blob fetches with no `Authorization` header against private repos.
- Hunt for unfamiliar registry pulls from cloud provider IP ranges and Tor exit IPs.

**Sources:** [The Hacker News — Gitea Vulnerability Exposes Private Container Images without Authentication](https://thehackernews.com/2026/05/gitea-vulnerability-exposes-private.html) | [Noscope — Gitea Instances Exposing Private Container Images](https://www.noscope.com/blog/gitea-instances-exposing-private-container)

---

### SymJack — Symlink-Hijack Supply Chain Attack Confirmed Against Six AI Coding Agents (Adversa AI, 2026-05-27)
**Product:** Claude Code, Gemini CLI, Antigravity CLI, Cursor Agent CLI, GitHub Copilot CLI, Grok Build, OpenAI Codex CLI — single attack pattern works across all six | **CVE:** Not assigned | **CVSS:** Not assigned | **First reported:** 2026-05-27

Adversa AI published the SymJack technique 2026-05-27: a malicious repository plants a symlink that, when an AI coding agent processes a benign-looking file operation like `cp` or `mv`, secretly overwrites the agent's own configuration file. Once the agent restarts, the attacker-controlled MCP server registration in the modified config runs arbitrary code with the developer's full user privileges. The attack bypasses the per-operation approval dialog because the developer approves the visible file operation while the kernel writes elsewhere via the symlink redirection. Validated across all six listed AI coding agents (Claude Code, Gemini/Antigravity CLI, Cursor, Copilot CLI, Grok Build, Codex CLI). In CI environments — where agents typically run in non-interactive auto-approve mode — the attack chain executes end-to-end with no operator approval at all, making this a particularly potent supply-chain delivery vector via a single malicious PR.

**Mitigation:**
- Treat every AI-coding-agent config dir (`~/.claude/`, `~/.gemini/`, `~/.cursor/`, `~/.copilot/`, `~/.codex/`, `~/.grok/`) as security-sensitive: restrict write access, monitor for unexpected changes, version-control them where feasible.
- In CI environments, disable auto-approve for any AI coding agent tool that processes arbitrary repo content; require operator review for any agent run against untrusted PRs.
- Maintain a per-repo allow-list of file operations the agent may perform without prompt.
- Add EDR / file-integrity rules to alert on any write to an AI-agent config file by a process other than the agent itself.
- Until vendors patch the symlink approval-dialog mismatch, treat any cloned untrusted repository as presumptive code-execution risk when opened by any of the six listed agents.

**Sources:** [Adversa AI — The Approval Prompt is Lying: A Critical Coding Agent Security Flaw](https://adversa.ai/blog/the-approval-prompt-is-lying-to-you-symlink-rce-in-five-ai-coding-agents-claude-code-cursor-antigravity-copilot-grok-build/) | [SecurityWeek — 'SymJack' Attack Turns AI Coding Agents Into Supply Chain Attack Delivery Systems](https://www.securityweek.com/symjack-attack-turns-ai-coding-agents-into-supply-chain-attack-delivery-systems/)

---

## 🟡 MEDIUM

### Jenkins Security Advisory 2026-05-27 — 11-CVE Plugin Batch Including LDAP/AD Referral RCE and Email Extension Arbitrary File Read
**Product:** Multiple Jenkins plugins (LDAP, Active Directory, Email Extension, Pipeline: Groovy Libraries, Credentials Binding, AppSpider, Bitbucket OAuth, GitHub Integration, Multijob, Job Import, buildgraph-view) | **CVE:** CVE-2026-48916 → 48927, CVE-2026-9674 | **Published:** 2026-05-27

Jenkins shipped an 11-vulnerability plugin advisory 2026-05-27. Highest-impact items: (a) **CVE-2026-48916/48917 LDAP Plugin + CVE-2026-48918/48919 Active Directory Plugin** — both follow LDAP referrals from the configured LDAP server, and if the referral points to an `rmi://` URL, Java deserialization of attacker-controlled content yields RCE on the Jenkins controller; (b) **CVE-2026-48920 Email Extension Plugin (High)** — `inlining images as base64` feature accepts `file:` URLs, allowing read of arbitrary files from the Jenkins controller's filesystem; (c) **CVE-2026-48921 Pipeline: Groovy Libraries Plugin (High)** — missing symbolic-link restrictions enable filesystem access outside the workspace; (d) **CVE-2026-48922 Credentials Binding Plugin (High)** — insufficient file name sanitisation permits path traversal; (e) **CVE-2026-48927 buildgraph-view Plugin (High)** — unescaped build URLs cause stored XSS, **no fix available**. Several CSRF / authorization-check / redirect items round out the batch (medium severity).

**Mitigation:**
- Upgrade affected Jenkins plugins per advisory matrix; for buildgraph-view, disable the plugin until a fix ships.
- For LDAP/Active Directory plugins: ensure the configured LDAP server is trusted (does not return malicious referrals) — defence-in-depth even with patches applied.
- Audit Jenkins controller for any current LDAP referral pointing outside the trusted directory infrastructure.
- For Email Extension Plugin, validate that no in-flight pipelines rely on `file:`-scheme URLs that may now be blocked.

**Sources:** [Jenkins Security Advisory 2026-05-27](https://www.jenkins.io/security/advisory/2026-05-27/) | [CyberSecurityNews — Jenkins Patches High-Severity Plugin Flaws Including Path Traversal and Stored XSS](https://cybersecuritynews.com/jenkins-patches-multiple-vulnerabilities-2/)

---

### Pretalx CVE-2026-41241 — Stored XSS via Organiser Search Auto-Accepts Talk Submissions, Used to Auto-Apply for 40 Conferences
**Product:** Pretalx open-source conference CFP management platform (versions prior to 2026.1.0, fixed 2026.1.0) | **CVE:** CVE-2026-41241 | **Published:** 2026-05-27

Sonar / Novee researchers disclosed a stored XSS in Pretalx's organiser search interface: any user controlling searchable fields (submission titles, speaker display names, usernames, email addresses) can inject arbitrary JavaScript that executes in the organiser's browser session when an organiser's search query matches the malicious record. The PoC: researcher used the flaw to auto-submit talk proposals to 40 conferences and got accepted at every one by injecting JS that programmatically clicked the "Accept" button when the organiser searched. While the immediate concrete impact is reputation / process integrity rather than RCE, Pretalx is widely used at major security and developer conferences (PyCon US, fwd:cloudsec, postmarketOS, Open Data Hub Day) — and an attacker who breaches an organiser account gains access to attendee data, speaker contact info, and embargoed submission content.

**Mitigation:**
- Upgrade Pretalx to 2026.1.0 or later immediately.
- Review accepted talks from the past 90 days for ones whose acceptance pattern looks anomalous (single reviewer, no committee review, last-minute acceptance).
- Audit organiser accounts for unfamiliar admin actions and rotate organiser credentials.
- Restrict the organiser search interface to vetted personnel only until upgrade is complete.

**Sources:** [SecurityWeek — Vulnerability in Popular Conference Software Granted Attackers a 100% Talk Acceptance Rate](https://www.securityweek.com/vulnerability-in-popular-conference-software-granted-attackers-a-100-talk-acceptance-rate/) | [The Register — Pretalx XSS Flaw Exposed Conference CFP Systems](https://www.theregister.com/security/2026/05/27/pretalx-xss-flaw-exposed-conference-cfp-systems/) | [Sonar Research — Pretalx Vulnerabilities: How to Get Accepted at Every Conference](https://www.sonarsource.com/blog/pretalx-vulnerabilities-how-to-get-accepted-at-every-conference)

---

### 🔄 GlassWorm Botnet C2 Disruption (CrowdStrike + Google + Shadowserver, 2026-05-26 14:00 UTC) — All Four C2 Channels Severed
**Product:** GlassWorm developer-targeting botnet — operative since early 2025; previously tracked as GlassWorm v2 on 2026-04-28 (73 Open VSX sleeper extensions, 320+ artifacts since 2025-12-21) | **CVE:** N/A (campaign-level disruption, not new vulnerability)

CrowdStrike Counter Adversary Operations executed a coordinated takedown 2026-05-26 at 14:00 UTC, in collaboration with Google and the Shadowserver Foundation, against all four GlassWorm command-and-control channels simultaneously: (1) the Solana blockchain, (2) BitTorrent DHT, (3) Google Calendar event titles, and (4) traditional VPS servers — all of which had been designed for resilience against conventional takedowns. The botnet had compromised VSCode + Cursor + Positron + Windsurf + VSCodium extensions through marketplace publishing, 300+ GitHub repos via force-pushed commits using stolen developer credentials, and npm/Python packages with malicious postinstall hooks. Capabilities included full-featured GlasswormRAT (Node.js cross-platform RAT covering Windows/macOS/Linux). Attribution: Russian (CIS-skip locale check in malware payload). This is a material change to the GlassWorm v2 entry from 2026-04-28: the C2 plane is now offline, blast radius for new infections drops significantly, but compromised endpoints retain implants and stolen credentials remain in attacker possession.

**Mitigation:**
- Run retroactive hunt against the IOC set published by CrowdStrike / Google / Shadowserver across the full 2025-01 → 2026-05 GlassWorm window — any infection during that period leaves credential-theft residue (SSH keys, git credentials, cloud credentials, browser session cookies, crypto wallets).
- For any developer endpoint that installed one of the 320+ identified GlassWorm artefacts (per Koi/Aikido prior research), assume credential disclosure and rotate all credentials including dev cloud creds, SSH keys, GitHub PATs, browser-stored credentials, and crypto wallet seed phrases.
- Maintain takedown-resilience posture: the same actors typically resurface within 30-60 days under a new C2 architecture; do not assume the campaign is over.
- For the VS Code extension allow-list, continue restricting auto-update on devices with privileged GitHub PATs (cf. MEMORY 2026-05-21 Nx Console pattern).

**Sources:** [CrowdStrike — Disrupting Glassworm: Inside CrowdStrike's Takedown](https://www.crowdstrike.com/en-us/blog/inside-crowdstrike-takedown-of-a-developer-targeting-botnet/) | [Cybersecurity Dive — Coordinated Operation Takes Down Glassworm Botnet](https://www.cybersecuritydive.com/news/takedown-glassworm-botnet-crowdstrike-Google-Shadowserver/821227/) | [The Register — CrowdStrike, Google Shatter Glassworm Botnet](https://www.theregister.com/cyber-crime/2026/05/27/crowdstrike-google-shatter-glassworm-botnet/)

---

## 📋 Noted / Monitoring

**mouse5212-super-formatter (npm, "Malware-Slop")** — Malicious npm package (676 downloads) targets Anthropic Claude's `/mnt/user-data` workspace directory, exfiltrating files to attacker-controlled GitHub repos via postinstall script (using either victim's GitHub token or a hardcoded fallback). Notable for being the **first publicly-tracked malware specifically targeting the Claude AI sandboxed workspace data directory** (extends the AI-agent-config-as-code class from MEMORY 2026-05-01 / 05-07 / 05-08 to AI-agent **data** dirs). Operator OPSEC was poor (hardcoded token leaked) suggesting AI-assisted authorship without security review — joins the AI-assisted-malware-development pattern (Nimbus Manticore, MEMORY 2026-05-26).

**Apache Artemis CVE-2026-40914** — STOMP protocol address routing-type modification allows authenticated users without `createAddress` permission to alter routing — extends the CVE-2025-27427 pattern; oss-security disclosure 2026-05-27.

**Perl Module Batch (oss-security 2026-05-27): CVE-2026-8450 HTTP::Daemon OS command injection via `send_file()` (<6.17); CVE-2026-48962 IO::Compress arbitrary code execution via `File::GlobMapper` (<2.220); CVE-2026-48961 IO::Compress zipdetails-CLI undefined-sub crash (2.207-2.220); CVE-2026-48959 IO::Uncompress::Unzip CPU exhaustion in `fastForward` (<2.220); CVE-2025-15649 IO::Uncompress::Unzip uncaught-exception (<2.215)** — substantial CPAN-stack security batch from Perl community; HTTP::Daemon and IO::Compress are widely embedded in legacy CGI / data-pipeline / build-tool stacks.

**OpenStack Swift CVE-2026-49010** — Denial of service via truncated `s3api` chunked upload (oss-security 2026-05-27); affects Swift S3-compatibility layer used by private cloud / scientific computing deployments.

**Linux Kernel io_uring/zcrx Race CVE-2026-43121** — Concurrent scrub + refill paths corrupt the niov freelist → double-free + 4-byte OOB write → arbitrary code execution in kernel context. Requires `CAP_NET_ADMIN` + NIC supporting page-pool-backed memory (mlx5/nfp) + `CONFIG_IO_URING_ZCRX=y`. LPE-only (Watchtower scope-adjacent, noted for K8s control-plane / multi-tenant Linux operators) — extends the page-cache-LPE-to-container-escape trajectory class (MEMORY 2026-05-16 Copy Fail K8s PoC).

**WPCode WordPress Plugin CVE-2026-8832 (CVSS 8.8)** — PT-Security dbugs 2026-05-27 (PT-2026-43573); WPCode is a code-snippet management plugin with broad install base — auth-bypass-to-RCE class consistent with the May 2026 WordPress plugin pattern (Burst Statistics, Funnel Builder, AI Engine).

**Cockpit on Red Hat Enterprise Linux CVE-2026-4802 (CVSS 8.0)** — Remote command execution via unsanitised parameters in system-logs UI; shell metacharacter injection in crafted URLs. Affects RHEL / Fedora / CentOS Stream Cockpit deployments where the web management UI is reachable.

**Dolibarr ERP/CRM CVE-2026-37711 (CVSS 7.3)** — RCE in core actions file in Dolibarr v22.0.0-v22.0.4, v24.0.0-alpha; widely deployed SMB ERP/CRM.

**FastNetMon CVE-2026-48687 (CVSS 8.1)** — OS command injection in Juniper-router integration plugin (`_log()` function concatenates unsanitised data into shell commands); additional CVE to the FastNetMon batch already Noted on 2026-05-27 (CVE-2026-48686/48688/48692/48695).

**Stark Industries Solutions Hosting Infrastructure Seizure (Dutch authorities, 2026-05-25)** — 800+ servers seized + two operators arrested; Russian-staging-ground hosting provider previously used for DDoS + EU-targeted disinformation. Operational / infrastructure-level disruption, not a vulnerability — but worth noting in the May 2026 takedown-cluster context (joins Fox Tempest MSaaS 2026-05-19, GlassWorm 2026-05-26).

**Samba Companion Advisories (additional to CVE-2026-4408 / 4480 above): CVE-2026-1933 (reparse point access checks missing), CVE-2026-2340 (WORM vfs module overwrites), CVE-2026-3012 (auto-enrollment GPO CA cert over plain HTTP without verification), CVE-2026-3238 (AD DC WINS server DoS)** — Lower-impact items in the same 2026-05-26 Samba security release.

**Mesa CVE-2026-29075** — Arbitrary code execution in `benchmarks.yml` CI workflow (GHSL-2025-009); workflow-file scope, limited to CI-job-compromise rather than runtime impact.

**Chatwoot GHSL-2026-059 SQL injection** — Open-source customer-support platform; no CVE assigned yet (GitHub Security Lab disclosure).

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer, thehackernews, securityweek, schneier, krebsonsecurity | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (403 Forbidden — used THN/SecurityWeek/BleepingComputer for KEV data) |
| Vendor advisories | samba.org, jenkins.io, msrc.microsoft.com/blog | ✅ Samba/Jenkins direct; ⚠️ MSRC nav-only |
| Research / OSINT | securitylab.github.com, fortinet.com/blog/threat-research, rapid7.com/blog, attackerkb.com, opencve.io, github 0xMarcio/cve, github search?q=CVE, googleprojectzero | ✅ GitHub SecurityLab/Fortinet/Rapid7/OpenCVE/GitHub-search/0xMarcio; ❌ AttackerKB 403, ProjectZero redirect |
| Supply chain | seclists.org/fulldisclosure, packetstormsecurity, openwall.com/lists/oss-security | ✅ seclists/oss-security; ⚠️ packetstorm homepage only |
| Threat intel | cloudflare/tag/security, dbugs.ptsecurity, avleonov, habr.com/ru/companies/tomhunter, teletype.in/@cyberok, cert.gov.ua, kb.cert.org/vuls | ✅ Cloudflare/dbugs/avleonov/kb.cert; ⚠️ habr/teletype no recent; ❌ cert.gov.ua empty |
| CVE indexes | nvd.nist.gov, cve.mitre.org, cve.org | ⚠️ All JS/nav-only; data obtained via opencve.io as proxy |
| Bug bounty | hackerone.com/hacktivity, bugcrowd.com/disclosures | ❌ JS-only / 404 |

**Errors:** cisa.gov / cisa-kev (403), attackerkb.com (403), msrc.microsoft.com/blog (redirect to nav-only), hackerone.com/hacktivity (JS-only), bugcrowd.com/disclosures (404), cert.gov.ua (empty response), cve.mitre.org (redirects to cve.org with JS-only), cve.org (JS-only), googleprojectzero.blogspot.com (redirect-only), rapid7.com/blog (timeout on first try, retried homepage successfully).
**CISA KEV:** 1 new addition observed since 2026-05-26 — CVE-2026-48172 (LiteSpeed cPanel Plugin) — 4-day Federal deadline 2026-05-29.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-28/night | Next: 2026-05-29/night*
