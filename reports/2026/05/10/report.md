# Watchtower Night Report — 2026-05-10
**Cycle:** Night | **Generated:** 2026-05-10 00:35 UTC (2026-05-10T00:35:00Z)
**Sources checked:** 22/30 | **CISA KEV total:** unreachable via WebFetch | **New KEV additions:** none confirmed since 2026-05-08 (CVE-2026-6973 Ivanti EPMM federal deadline TODAY 2026-05-10)

---

## 🔴 CRITICAL

### xrdp CVE-2025-68670 — Pre-Auth Stack-Buffer-Overflow RCE (Kaspersky, In-the-Wild Exploitation)
**Product:** xrdp open-source RDP server (versions <0.10.5 / pre-backport <0.9.27, <0.10.4.1) | **CVE:** CVE-2025-68670 | **Status:** Patched upstream, **actively exploited** for unauthenticated RCE → privilege escalation → lateral movement (per Kaspersky GReAT)

Kaspersky GReAT published an analysis of **CVE-2025-68670** — an unauthenticated stack-based buffer overflow in **xrdp**, the most widely deployed open-source RDP server (Linux/BSD), discovered by Kaspersky during a security assessment of their own USB Redirector product. The flaw is in xrdp's processing of user-domain information during the **initial RDP connect-sequence**, before any authentication occurs; insufficient bounds-checking allows a remote unauthenticated attacker to overwrite stack buffers and the saved return address, yielding arbitrary code execution. Kaspersky reports that attackers are exploiting this in the wild to gain unauthenticated RCE on xrdp servers, escalate privileges, and pivot inside victim networks. The fix is in xrdp **0.10.5** (and backports 0.9.27 / 0.10.4.1).

**Timeline:** Bug discovered during Kaspersky USB Redirector assessment → reported privately to xrdp maintainers → patched in 0.10.5 → backports 0.9.27 / 0.10.4.1 → Kaspersky public disclosure (Securelist) early-May 2026 → in-the-wild exploitation observed.

**Why it matters:** xrdp is the canonical "free Windows-style RDP on Linux" service — it's installed as the management plane on a huge fleet of Linux desktops, OpenStack/Proxmox/oVirt VMs, jump hosts, and KVM consoles in private clouds. Pre-auth RCE on a Linux service that *exists specifically to be exposed for remote management* is a perimeter-busting bug class — and Kaspersky says it's already being weaponised. For any environment that exposes 3389/tcp to internal segments (let alone the internet), this is a same-week patch. Note this is **distinct** from CVE-2026-32105 (xrdp MITM in classic-RDP mode, covered 2026-04-18) — different bug class, different exploitation primitive.

**Discovered by:** Kaspersky GReAT (researchers credited in Securelist post)

**Mitigation:**
- Inventory all hosts running xrdp; upgrade to **xrdp 0.10.5** (or backports 0.9.27 / 0.10.4.1) immediately.
- For internet-exposed instances, treat as compromise-suspect unless you can prove no traffic from the disclosure window onwards — pre-auth RCE.
- Block 3389/tcp at perimeter; require VPN/jump-host with MFA for any RDP access.
- Hunt for `xrdp-sesman` / `xrdp` child processes spawned by unusual users, unexpected outbound connections from xrdp hosts, and post-exploit Linux LPE artefacts (the Dirty Frag / Copy Fail kernel LPEs covered in prior reports chain naturally from a low-priv xrdp foothold to root).
- Add Snort/Suricata signatures matching oversized domain fields in early RDP negotiation packets (Kaspersky published technical signature material).

**Sources:** [Kaspersky Securelist — CVE-2025-68670 xrdp RCE analysis](https://securelist.com) | [Malware.News — Kaspersky details CVE-2025-68670](https://malware.news/t/cve-2025-68670-discovering-an-rce-vulnerability-in-xrdp/106802)

---

### JDownloader Official Site Compromise — Windows Python RAT + Linux ELF Persistence Kit (Supply Chain)
**Product:** JDownloader 2 download manager (Windows .exe and Linux shell installers downloaded from official site between **2026-05-06 00:01 UTC** and **2026-05-07**) | **CVE:** None | **Status:** **Active supply-chain compromise**, IOCs published, payloads online, takedown in progress

Attackers compromised the **official JDownloader website's CMS** and replaced the "Download Alternative Installer" Windows binary and the Linux shell installer with trojanised versions while leaving macOS, the JAR file, Flatpak/Winget/Snap, and the in-app updater untouched. The Windows payload is a **loader that drops a heavily obfuscated Python-based RAT** with modular bot capabilities (remote execution, screen capture, credential harvesting). The Linux payload is **two ELF binaries** with persistence via a **SUID-root binary in `/usr/bin/`** plus `/etc/profile.d/systemd.sh`. The trojanised Windows installers were signed by spoofed publishers ("Zipline LLC", "The Water Team") instead of the legitimate **AppWork GmbH**, which is what tipped off the first community reports. Two C2 servers — `parkspringshotel[.]com` and `auraguest[.]lk` — and a Linux dropper host `checkinnhotels[.]com` are the published IOCs.

**Timeline:** **2026-05-05 23:55 UTC** dummy-site dry run by attacker → **2026-05-06 00:01 UTC** real CMS modification → **2026-05-07** Reddit user "PrinceOfNightSky" notices SmartScreen flagging "Zipline LLC" publisher → **2026-05-08-09** vendor confirms hack → **2026-05-09** BleepingComputer/researcher Thomas Klemenc publish full analysis with IOCs.

**Why it matters:** JDownloader is one of the most widely installed cross-platform download managers (millions of users); a 24+ hour drop window of trojanised binaries from the *official* domain — with a real-looking installer-signing lookalike — is a classic *trusted-vendor distribution channel* compromise. Any developer / SOC analyst / power-user endpoint that ran an installer from the official site in the **2026-05-06 00:01 UTC → 2026-05-07** window must be treated as compromised: full Python RAT on Windows, SUID-root persistence on Linux. The Linux variant matters operationally — JDownloader is common on home-lab/seedbox boxes that often double as small-team file-share servers.

**Discovered by:** Thomas Klemenc (Windows analysis); BleepingComputer researchers (Linux ELF analysis); first community reports via "PrinceOfNightSky" on Reddit.

**Mitigation:**
- Identify any JDownloader 2 Windows `.exe` or Linux shell-installer downloads in the 2026-05-06 → 2026-05-07 window via proxy / EDR / endpoint-install logs.
- For confirmed installations from the bad window: **clean OS reinstall is the recommended action** per multiple analyses; password rotation alone is insufficient because of persistence + RAT scope.
- Block C2 IOCs at perimeter / DNS: `parkspringshotel[.]com`, `auraguest[.]lk`, `checkinnhotels[.]com`.
- Verify any JDownloader installer publisher signature is **AppWork GmbH** (not "Zipline LLC" / "The Water Team").
- Hunt on Linux: `/usr/bin/` SUID binaries with recent mtimes (early May 2026), `/etc/profile.d/systemd.sh` script, outbound to dropper host.
- Re-examine package-manager builds (Flatpak, Winget, Snap, JAR-download) — these were *not* compromised and are the safer redistribution channels.

**Sources:** [BleepingComputer — JDownloader site hacked to replace installers with Python RAT](https://www.bleepingcomputer.com/news/security/jdownloader-site-hacked-to-replace-installers-with-python-rat-malware/) | [SecurityOnline — JDownloader website breach malware installers swapped](https://securityonline.info/jdownloader-website-breach-malware-installers-swapped/) | [PiunikaWeb — JDownloader developers confirm site hack](https://piunikaweb.com/2026/05/08/jdownloader-website-hacked-malware/)

---

## 🟠 HIGH

### Open WebUI Multi-CVE Batch — Path Traversal + Auth Bypass + Stored XSS (Same Product, 24 Hours After LDAP Empty-Password Bypass)
**Product:** Open WebUI self-hosted ChatGPT-style front-end | **CVEs:** CVE-2026-44566 (path traversal RCE), CVE-2026-44567 (improper authorization), CVE-2026-44549 (stored XSS in Excel-file preview) | **CVSS:** all High | **First reported:** 2026-05-09

Within **24 hours** of yesterday's CVE-2026-44551 LDAP empty-password authentication bypass (CVSS 9.1), GitHub Advisories published **three additional Open WebUI advisories** on **2026-05-09**: **CVE-2026-44566** (arbitrary file upload + path traversal yielding RCE), **CVE-2026-44567** (improper authorization control on protected endpoints), and **CVE-2026-44549** (stored XSS via Excel-file preview rendering). All three are **High** severity. Combined with yesterday's LDAP bypass, an attacker now has a complete pre-auth → file-write → XSS chain on a self-hosted AI front-end with default-no-auth deployment patterns.

**Mitigation:**
- Upgrade Open WebUI to the latest patched release (post-0.9.0 — LDAP bypass plus the new 44566/44567/44549 set; verify advisory text for exact fix versions).
- Audit any Open WebUI instance reachable from the internet against Intruder-Labs' **31% no-auth rate** baseline for self-hosted AI front-ends — the CVE-2026-44551 LDAP bypass + new path-traversal/authz combo means default deployments are now stackable trivial-RCE primitives.
- Disable Excel-file preview if not required, until 44549 is patched.
- Treat Open WebUI as a deprecation/segmentation candidate; the velocity of high-severity CVEs (4 in 30 days) is a code-quality signal similar to nginx-ui's pattern (3 pre-auth RCEs in 2 months).

**Sources:** [GitHub Advisory GHSA-9pgh-j74g-qj6m (CVE-2026-44566)](https://github.com/advisories/GHSA-9pgh-j74g-qj6m) | [GHSA-4vg5-rp28-gvjf (CVE-2026-44567)](https://github.com/advisories/GHSA-4vg5-rp28-gvjf) | [GHSA-jwf8-pv5p-vhmc (CVE-2026-44549)](https://github.com/advisories/GHSA-jwf8-pv5p-vhmc)

---

### cPanel & WHM CVE-2026-29201 / 29202 / 29203 — Second Emergency TSR in 10 Days
**Product:** cPanel & WHM (multiple support branches) | **CVEs:** CVE-2026-29201 (CVSS 4.3 arbitrary file read), CVE-2026-29202 (CVSS 8.8 authenticated Perl RCE via plugin parameter), CVE-2026-29203 (CVSS 8.8 symlink → chmod LPE/DoS) | **CVSS:** up to 8.8 | **First reported:** 2026-05-09 (TSR shipped 2026-05-08 12:00 EST)

cPanel published their **second Technical Security Release in 10 days**, fixing three new bugs:
- **CVE-2026-29201 (CVSS 4.3)** — insufficient input validation of the feature file name in `feature::LOADFEATUREFILE` admin-bin call → arbitrary local file read.
- **CVE-2026-29202 (CVSS 8.8)** — input-validation bug in the `plugin` parameter of the `create_user API` call → authenticated arbitrary Perl code execution as a system user.
- **CVE-2026-29203 (CVSS 8.8)** — insecure symlink handling allows `chmod` on arbitrary files → DoS or local privilege escalation.

All three require **some authenticated context** (account-user or admin), so individually they are post-auth, but in combination with credential-leak / RAT footholds they convert directly to lateral movement. No active exploitation reported for these specific CVEs at disclosure, but cPanel is in an unprecedented quality-storm window: CVE-2026-41940 (CVSS 9.8 unauth bypass, 0-day exploited Feb-April → 44k servers ransomed by 2026-05-03) was patched 10 days ago, and now another emergency TSR.

Patched releases: **11.136.0.9+, 11.134.0.25+, 11.132.0.31+, 11.130.0.22+, 11.126.0.58+, 11.124.0.37+, 11.118.0.66+, 11.110.0.117+, 11.102.0.41+, 11.94.0.30+, 11.86.0.43+** (and WP Squared 11.136.1.10+).

**Mitigation:**
- Apply the May 8 TSR across **all** cPanel/WHM branches in fleet; do not skip branches in the legacy support tree.
- Audit account credentials and reset where password/2FA hygiene is weak — CVE-2026-29202 needs an authenticated account, and post-41940 stolen accounts are circulating.
- Hunt for unexplained Perl process spawn from the cPanel API path; chmod / symlink writes on system binaries.
- Treat the back-to-back cPanel TSRs as a code-quality signal — escalate cPanel-class platforms to the same monitoring tier as Webpros (parent — see CVE-2026-29200 Comet Backup multi-tenant IDOR from 2026-05-05).

**Sources:** [The Hacker News — cPanel WHM Patch 3 New Vulnerabilities](https://thehackernews.com/2026/05/cpanel-whm-patch-3-new-vulnerabilities.html) | [Panelica — cPanel CVE-2026-29201/29202/29203 May 2026 TSR](https://panelica.com/blog/cpanel-cve-2026-29201-29202-29203-may-2026-tsr-advisory) | [KnownHost forum — patch released 5/8/26 noon EST](https://www.knownhost.com/forums/threads/cpanel-cve-2026-29201-cve-2026-29202-and-cve-2026-29203-patch-released-5-8-26-noon-est.6603/)

---

### Apache CloudStack 4.20.3.0 / 4.22.0.1 — 7-CVE Batch Including CVE-2026-25077 Direct Download Template RCE
**Product:** Apache CloudStack (versions <4.20.3.0 / <4.22.0.1) | **CVEs:** CVE-2025-66170 (backup access), CVE-2025-66171 (cross-account VM creation), CVE-2025-66172 (cross-account volume attach), CVE-2025-66467 (MinIO bucket policy persistence), CVE-2025-69233 (resource-limit bypass), **CVE-2026-25077 (account-user command injection in direct download templates → RCE on KVM hosts)**, CVE-2026-25199 (Proxmox extension cross-tenant access) | **First reported:** 2026-05-09

Apache CloudStack shipped LTS releases **4.20.3.0** and **4.22.0.1** with a 7-CVE bundle. The headline item is **CVE-2026-25077**: account-users (default-allowed) can register Direct Download Templates for KVM-host primary storage, and **missing file-name sanitisation** in template registration lets the attacker inject shell metacharacters that execute on the **KVM hypervisor host** during download. Outcome: arbitrary code execution on KVM hosts → full hypervisor + tenant-VM compromise → integrity, confidentiality, DoS, availability hits across the cloud. The remaining six CVEs cluster into two themes:
- **Cross-tenant authorization bypasses** in backup operations (66170/66171/66172) and Proxmox extension (25199) — multi-tenant isolation broken.
- **Multi-tenant policy/limit bypass** (66467 MinIO bucket policy persistence + 69233 resource-limit enforcement) — tenants can survive bucket deletion or escape resource quotas.

**Mitigation:**
- Upgrade to CloudStack **4.20.3.0** (LTS) or **4.22.0.1** immediately on any hypervisor-fleet manager.
- Until patched, restrict who can register Direct Download Templates to admin only (default config — *don't* leave it as a default-allowed account-user permission).
- Audit existing KVM hypervisors for unexplained processes / persistence — if the CVE-2026-25077 vector was exercised by a tenant, the KVM host owns the rest of the cloud.
- Cross-tenant audit: validate backup ACLs and Proxmox-extension permissions against the new code paths.

**Sources:** [Apache CloudStack security release advisory 4.20.3.0 / 4.22.0.1](https://cloudstack.apache.org/blog/security-release-advisory-4.20.3.0-4.22.0.1/) | [oss-security — CVE-2026-25077 thread](https://www.openwall.com/lists/oss-security/2026/05/09/) | [ShapeBlue advisory](https://www.shapeblue.com/shapeblue-security-cloudstack-4-20-3-0-and-4-22-0-1)

---

## 🟡 MEDIUM

### Termix CVE-2026-42454 — Docker Container Management Endpoint Command Injection (CVSS 9.9)
**Product:** Termix (web-based SSH/SFTP/Docker terminal) versions <2.1.0 | **CVE:** CVE-2026-42454 | **Published:** 2026-05-08

Pre-2.1.0 Termix interpolates the `containerId` URL path parameter and WebSocket message field **directly into shell commands** executed via `ssh2.Client.exec()` against managed hosts — no sanitisation, no validation. **Authenticated** attackers craft a `containerId` to inject arbitrary OS commands which run with the privileges of the SSH connection on the **remote managed server**, achieving RCE on every Docker host the Termix instance manages. CVSS 9.9 reflects that one Termix-account compromise pivots immediately to every host the operator manages — the blast radius is the inventory.

**Mitigation:** Upgrade to Termix 2.1.0+; restrict who can authenticate to Termix; rotate SSH keys used by Termix to managed hosts post-upgrade.

**Sources:** [TheHackerWire — Termix Critical RCE via Unsanitized Container ID](https://www.thehackerwire.com/termix-critical-rce-via-unsanitized-container-id/) | [GitHub Advisories CVE-2026-42454](https://github.com/advisories)

---

### Hugging Face "Open-OSS/privacy-filter" — OpenAI Typosquat Pushes Rust Infostealer (244k Downloads, Trending)
**Product:** Hugging Face platform — typosquat repository named to impersonate OpenAI's "Privacy Filter" release | **CVE:** None | **Published:** 2026-05-09 (HiddenLayer disclosure, malicious repo discovered 2026-05-07)

HiddenLayer published analysis of **Open-OSS/privacy-filter**, a malicious Hugging Face repository typosquatting OpenAI's legitimate Privacy Filter release. The repo reached **trending** status and accumulated **244k downloads** (artificially inflated, but real downloads occurred) before takedown. Loader chain: `loader.py` disables SSL verification → PowerShell downloads a batch file → privilege escalation → adds Microsoft Defender exclusion → executes a **Rust-based infostealer** that exfiltrates browser cookies/passwords/encryption keys, Discord tokens, crypto wallets, SSH/FTP/VPN credentials, screenshots, and system info to `recargapopular[.]com`. Anti-analysis features include VM/sandbox/debugger checks. The 667 "likes" appear to be auto-generated bots.

**Mitigation:** Block `recargapopular[.]com` at egress; treat any researcher / data-scientist endpoint that pulled "Open-OSS/privacy-filter" as compromise-suspect; tighten Hugging Face usage policies (require model provenance verification, allow-list specific orgs). This is the second confirmed Hugging Face supply-chain incident in 11 days after CVE-2026-25874 LeRobot pickle-deser RCE (2026-04-29).

**Sources:** [BleepingComputer — Fake OpenAI repository on Hugging Face pushes infostealer](https://www.bleepingcomputer.com/news/security/fake-openai-repository-on-hugging-face-pushes-infostealer-malware/) | [HiddenLayer research](https://hiddenlayer.com)

---

## 📋 Noted / Monitoring

**Cisco Crosswork CNC / NSO CVE-2026-20188** — Unauth network DoS via inadequate connection rate-limiting on Crosswork Network Controller ≤7.1 / Network Services Orchestrator ≤6.3; manual reboot required to recover. No exploitation reported. Mgmt-plane risk for telecom / SP environments.

**TCLBANKER (LATAM Windows banking trojan, Elastic Security Labs)** — Trojanised Logitech AI Prompt Builder MSI delivers a Brazilian banking trojan targeting 59 banking/fintech/crypto platforms; self-spreads via WhatsApp + Outlook worm modules. Out-of-scope (desktop client) but note the WhatsApp/Outlook worm module pattern for future enterprise variants.

**PgBouncer CVE-2026-6664 / CVE-2026-6665 (High)** — Integer overflow in packet parsing (6664) + missing return-value check on `strlcat()` in SCRAM code (6665), both in PgBouncer <1.25.2; widely deployed Postgres connection pooler — apply when upstream patch lands in your Linux distro.

**LangChain-core CVE-2026-44843 (High, pip)** — Unsafe deserialization via overly permissive allowlists. Adds to the ML-pipeline-deserialization pattern (Apache OpenNLP, HuggingFace LeRobot/Marimo).

**LiteLLM CVE-2026-42271 (CVSS 8.8)** — MCP server test endpoint accepts stdio-transport configurations, permitting authenticated users to execute arbitrary commands; another MCP-server authorisation issue continuing the recurring MCP attack-surface trend.

**@yoda.digital/gitlab-mcp-server CVE-2026-44895 (npm, High)** — SSE transport with no authentication and wildcard CORS exposes GitLab tools to any caller; same auth-defaults pattern as prior MCP servers.

**siyuan-note CVE-2026-44588 (Go, High)** — Electron Renderer RCE via XSS in `aria-label` sink; **incomplete fix** for prior CVE-2026-34585 — second iteration on same code path. Watch for further bypasses (cf. Apache MINA `IoBuffer.getObject()` triple-CVE pattern).

**GitPython CVE-2026-42215 + GHSA-mv93-w799-cj2w (newline injection bypass, pip)** — Newline injection in `config_writer()` `section` parameter bypasses prior CVE-2026-42215 patch, enabling RCE; **incomplete fix**, third major GitPython advisory in 2026.

**Velocity.js CVE-2026-44966 (npm, High)** — Prototype pollution via `#set` path assignment; widely embedded in Node.js templating.

**smallbitvec CVE-2026-44983 (Rust, High)** — Integer overflow in safe API triggers heap buffer overflow; relevant to any Rust project pulling smallbitvec as a transitive dependency.

**Spring AI MilvusVectorStore CVE-2026-41705 (High)** — Filter-expression vulnerability in `doDelete`; another instance of the Spring AI / vector-DB weakness class.

**Snipe-IT CVE-2026-44832 (Composer, High)** — Privilege escalation via API permissions; commonly self-hosted IT-asset tracker.

**AzuraCast CVE-2026-42605 (8.8) / CVE-2026-42606 (8.1)** — Path traversal RCE via media-upload + ApplyXForwarded middleware password-reset poisoning; fixed 0.23.6. Niche (web-radio software) but internet-facing.

**phpVMS CVE-2026-42569 (CVSS 9.4)** — Unauthenticated access to legacy import feature; PHP airline-simulation app — niche but unauth.

**io_uring zcrx freelist OOB write (oss-security 2026-05-08)** — Linux kernel io_uring zero-copy receive freelist out-of-bounds write; CVE pending. Watch for upgrade path; chains naturally with Dirty Frag / Copy Fail for kernel-side LPE on container hosts.

**Go 1.26.3 / Go 1.25.10 security release (oss-security 2026-05-08)** — 11 security fixes in this release; review your Go-built service rebuild plan.

**Russh CVE-2026-42189 (CVSS 7.5)** — Pre-authentication DoS in Eugeny/russh SSH library via malformed packets; track if you embed russh.

**BioPython 1.87 — CVE-2025-68463 (XXE + SSRF)** — Bioinformatics library; relevant if pipelines accept user-supplied XML.

**Linux kernel CVE-2026-43125 (Critical 9.8)** — `dlm_dump_rsb_name()` OOB write claimed in OpenCVE; verify against upstream kernel.org advisories before action.

**Q1 2026 Vulnerability Report (Kaspersky, 2026-05-07)** — Quarterly meta-analysis; useful for trend-tracking but no individual finding actionable today.

**Ivanti EPMM CVE-2026-6973 — federal deadline TODAY (2026-05-10)** — Federal-civilian patch deadline expires; covered as Update on 2026-05-09. Confirm 12.6.1.1/12.7.0.1/12.8.0.1 deployment by EOD.

**Canvas/Instructure ransom deadline 2026-05-12** — ShinyHunters' May 12 ransom deadline approaching for the second-vulnerability portal-defacement claim; covered 2026-05-08. No new IOCs or technical detail since.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog, kb.cert.org/vuls | ⚠️ (CISA 403) ✅ (kb.cert.org) |
| Vendor advisories | rapid7.com, fortinet.com/blog/threat-research, securitylab.github.com, msrc.microsoft.com/blog, blog.cloudflare.com/tag/security, dbugs.ptsecurity.com | ✅ / ⚠️ (msrc empty; dbugs degraded) |
| Research / OSINT | seclists.org/fulldisclosure, openwall.com/lists/oss-security, schneier.com, avleonov.com, github.com/0xMarcio/cve, github.com/search?q=CVE | ✅ |
| Supply chain | socket.dev, aikido.dev, safedep.io, snyk.io | ✅ |
| Threat intel | wiz.io/blog, kaspersky/securelist, vulncheck.com/advisories, github.com/advisories, opencve.io | ✅ |
| Bottom-tier (zero-yield) | habr/tomhunter, teletype/cyberok, cert.gov.ua | ⚠️ (no May 2026 content) |

**Errors:** cisa.gov / cisa.gov/known-exploited-vulnerabilities-catalog (persistent 403), attackerkb.com (persistent 403), bugcrowd.com/disclosures (404), cve.mitre.org / cve.org (JS-required, empty), googleprojectzero.blogspot.com (redirect to projectzero.google), hackerone.com/hacktivity (JS-required), packetstorm.news (degraded — homepage only), nvd.nist.gov (homepage only via WebFetch), trendmicro.com (403), msrc.microsoft.com/blog (empty page).
**CISA KEV:** Direct fetch unreachable. Per yesterday's report and SecurityWeek/BleepingComputer relay, **CVE-2026-6973 Ivanti EPMM** federal deadline is **today (2026-05-10)**; no new KEV additions confirmed since 2026-05-08.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-10/night | Next: 2026-05-11/night*
