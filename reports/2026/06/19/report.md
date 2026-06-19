# Watchtower Night Report — 2026-06-19
**Cycle:** Night | **Generated:** 2026-06-19 00:00 UTC (2026-06-19T00:00:00Z)
**Sources checked:** 19/30 | **CISA KEV total:** unreached (cisa.gov 403) | **New KEV additions:** unverified — see Source Coverage

---

## 🔴 CRITICAL

*No CRITICAL-tier items this cycle. The F5 NGINX pair below sits at the CRITICAL/HIGH boundary — no in-wild exploitation reported yet, so it's HIGH for now.*

---

## 🟠 HIGH

### F5 NGINX Out-of-Band Patches — CVE-2026-42530 (CVSS 9.2) HTTP/3 QUIC Use-After-Free + CVE-2026-42055 (CVSS 9.2) Proxy/gRPC Heap Overflow Allow Unauthenticated RCE
**Product:** F5 NGINX Open Source + NGINX Plus + NGINX Gateway Fabric + NGINX Instance Manager | **CVE:** CVE-2026-42530, CVE-2026-42055 | **CVSS:** 9.2 / 9.2 | **Status:** Patched (Out-of-Band) | **First reported:** 2026-06-18

F5 shipped emergency out-of-band patches for two CVSS-9.2 unauthenticated NGINX vulnerabilities. **CVE-2026-42530** is a use-after-free in `ngx_http_v3_module` triggered by specially crafted HTTP/3 QUIC sessions reopening QPACK encoder streams; remote code execution requires ASLR to be disabled or bypassed. **CVE-2026-42055** is a heap-based buffer overflow in `ngx_http_proxy_v2_module` and `ngx_http_grpc_module` when `proxy_http_version 2` or `grpc_pass` is configured for HTTP/2 proxying AND the `ignore_invalid_headers` directive is disabled. Two additional high-severity authenticated config-injection flaws (CVE-2026-11311, CVE-2026-50107) were patched in NGINX Gateway Fabric in the same batch. F5 reports no current in-the-wild exploitation.

**Timeline:** Disclosure → vendor advisory and OOB patches on 2026-06-18 (same day across NGINX Plus, Open Source, Gateway Fabric, Instance Manager).

**Why it matters:** NGINX powers a substantial fraction of internet-facing web servers and reverse proxies, including for many of our public surfaces. Two unauthenticated remote-code-execution paths with no auth, on configurations that are common (HTTP/3 enabled, gRPC/HTTP-2 upstream proxying) is precisely the surface that drives emergency patching. The ASLR-bypass prerequisite slightly limits theoretical universal exploitation, but practical RCE on misconfigured systems remains plausible.

**Discovered by:** Disclosed by F5 (no named researcher in the public advisory text).

**Mitigation:**
- Patch immediately to the F5-supplied fixed versions of NGINX Plus, NGINX Open Source, NGINX Gateway Fabric, and NGINX Instance Manager (per F5 advisory K000156174 and related KB articles).
- **CVE-2026-42530 workaround:** disable HTTP/3 by removing `quic` from `listen` directives.
- **CVE-2026-42055 workaround:** remove `ignore_invalid_headers off` from configuration and reduce `large_client_header_buffers` below 2 MB.
- Confirm ASLR is enabled at the kernel and per-binary level on all NGINX hosts; assume bypass is possible regardless.
- Audit for exposed HTTP/3 endpoints (UDP 443) and HTTP/2-proxied upstreams (`grpc_pass`, `proxy_http_version 2`).

**Sources:** [TheHackerNews — F5 Patches Two Critical NGINX Flaws](https://thehackernews.com/2026/06/f5-patches-two-critical-nginx-open.html) | [BleepingComputer — F5 Issues Out-of-Band Patches for Critical NGINX Vulnerabilities](https://www.bleepingcomputer.com/news/security/f5-issues-out-of-band-patches-for-critical-nginx-vulnerabilities/) | [SecurityWeek — F5 Patches NGINX Vulnerabilities](https://www.securityweek.com)

---

### Cisco ISE CVE-2026-20181 (CVSS 9.1) Authenticated-Admin → Root Command Injection + CVE-2026-20190 Hashed-Credential Disclosure Patched; Single-Node Deployments Can DoS
**Product:** Cisco Identity Services Engine (ISE) and ISE Passive Identity Connector (ISE-PIC), versions 3.3 / 3.4 / 3.5 | **CVE:** CVE-2026-20181, CVE-2026-20190 | **CVSS:** 9.1 (CVE-2026-20181) | **First reported:** 2026-06-18

Cisco patched a critical command-injection vulnerability (CVE-2026-20181, CVSS 9.1) in ISE / ISE-PIC. An authenticated remote attacker with admin credentials can send a specially crafted HTTP request to gain user-level access to the underlying OS, then escalate to root. On single-node deployments, exploitation can take the appliance down and block unauthenticated endpoints from network access until the system is restored. A second flaw, CVE-2026-20190 (high-severity), permits unauthenticated attackers to access sensitive information including hashed credentials. No active exploitation is reported.

**Timeline:** Cisco advisory and patches published 2026-06-18. Fixed in ISE/ISE-PIC 3.3 Patch 11 and 3.4 Patch 6, hotfix available for 3.5 with permanent fix in 3.5 Patch 4 (slated for August 2026).

**Why it matters:** Cisco ISE is the network-access-control control plane in a large share of enterprise networks — owning it owns auth decisions for the perimeter. CVE-2026-20181 requires admin auth, but in many environments ISE admin reach is broader than people think (helpdesk delegation, SSO breakage scenarios), and CVE-2026-20190 (hash disclosure) is unauthenticated and stackable.

**Mitigation:**
- Apply ISE/ISE-PIC 3.3 Patch 11, 3.4 Patch 6, or 3.5 hotfix per Cisco's advisory.
- Restrict ISE admin-UI exposure to a dedicated management VLAN/jump-host path. Treat any internet- or DMZ-reachable ISE admin interface as a P0.
- Rotate ISE admin credentials post-patch; assume the hashed-credential disclosure may have already been collected on long-exposed instances.
- For single-node deployments, schedule patching during a maintenance window — exploitation can hang the appliance.

**Sources:** [SecurityWeek — Critical Command Execution Vulnerability Patched in Cisco ISE](https://www.securityweek.com/critical-command-execution-vulnerability-patched-in-cisco-ise/)

---

### ShapedPlugin WordPress Supply-Chain Compromise — CVE-2026-10735 Backdoor In Build Pipeline From 2026-05-21; Product Slider Pro / Real Testimonials Pro / Smart Post Show Pro Paid Updates Shipped LicenseLoader.php Stealer
**Product:** ShapedPlugin paid WordPress plugins — Product Slider Pro (< 3.5.4), Real Testimonials Pro (3.2.5), Smart Post Show Pro (< 4.0.2); vendor's free versions on WordPress.org (~400K active installs combined) NOT affected | **CVE:** CVE-2026-10735 (primary; CVE-2026-49777 duplicate) | **First reported:** 2026-06-18

Attackers compromised ShapedPlugin's build pipeline — not the WordPress.org repository — on **2026-05-21** and injected a malicious loader (`LicenseLoader.php`) into official paid-plugin updates. The loader then downloads a second-stage backdoor disguised as fake WooCommerce plugins. The compromise rode through the vendor's legitimate update mechanism for **roughly three weeks** before customer reports surfaced on 2026-06-10 and vendor confirmation followed on 2026-06-12. Fixed versions shipped 2026-06-16. Exact paying-customer impact remains unclear.

**Impact and capabilities:** The backdoor harvests WordPress credentials and session cookies, 2FA secrets from security plugins, database credentials and authentication keys, the most recent **three months** of WooCommerce order and payment data, and SMTP / email-service credentials.

**Timeline:** Backdoor injection 2026-05-21 → customer reports 2026-06-10 → vendor confirmation 2026-06-12 → fixed releases 2026-06-16 → mainstream reporting 2026-06-18.

**Why it matters:** WordPress is a perennial part of any large public surface, and this is a textbook paid-plugin supply-chain attack — the malicious code shipped through the channel customers are explicitly told to trust. Any site running these three paid plugins between 2026-05-21 and 2026-06-16 should be treated as compromised, including a credential rotation that covers WP admin, 2FA, DB, SMTP, and any service that authenticated via Single-Sign-On from the affected WordPress instance during that window.

**Mitigation:**
- Update Product Slider Pro to ≥ 3.5.4, Real Testimonials Pro past 3.2.5, and Smart Post Show Pro to ≥ 4.0.2.
- Reset all WordPress credentials and 2FA secrets on affected sites; regenerate any application-passwords or REST API keys.
- Audit user accounts for unauthorized additions or privilege bumps in the 2026-05-21 → 2026-06-16 window.
- Rotate database credentials, SMTP/email-service credentials, and any WooCommerce payment-gateway secrets touched by the affected installations.
- Hunt for `LicenseLoader.php` and fake WooCommerce plugin files; review `wp-content/plugins/` for unexpected files.

**Sources:** [BleepingComputer — ShapedPlugin Update Flow Hacked to Infect WordPress Sites](https://www.bleepingcomputer.com/news/security/shapedplugin-update-flow-hacked-to-infect-wordpress-sites/)

---

### Arch Linux AUR Hijack — 400+ Abandoned Packages Adopted Since 2026-06-11; npm 'atomic-lockfile' + bun 'js-digest' Postinstall Pull Rust Infostealer With Optional eBPF Rootkit
**Product:** Arch Linux User Repository (AUR) — 400+ packages (attacker-adopted abandoned projects) | **CVE:** Not yet assigned | **First reported:** 2026-06-18

Starting 2026-06-11, attackers systematically adopted abandoned AUR projects, modified their `PKGBUILD` and `.install` scripts to run `npm install atomic-lockfile` (a second wave used `bun install js-digest`), and spoofed git commit metadata to look like long-standing maintainers. The npm/bun postinstall pulls a Rust-based Linux ELF named `deps`. **Arch's official systems were not breached** — the abuse vector is community-package adoption, similar in shape to recent npm and PyPI maintainer-takeover patterns.

**Capabilities:** The Rust infostealer harvests browser cookies and tokens from Chromium-based applications, session data from Electron apps (Slack, Discord, Teams), GitHub / npm / cloud credentials, SSH keys and shell histories, and Docker / container credentials. When the postinstall script runs as root (common on system-wide AUR builds via `makepkg -i`), an **optional eBPF rootkit** is deployed that hides processes and prevents debugger attachment using pinned BPF maps under `/sys/fs/bpf/`.

**Why it matters:** AUR is heavily used by developer workstations and CI build hosts. A developer that pulled a hijacked package in the last week and ran it as root may now have a stealthy eBPF rootkit, plus their GitHub / cloud / SSH keys may already be in attacker hands. Developer-machine credentials are a launchpad into production — this is a supply-chain issue with downstream blast radius beyond Arch users.

**Mitigation:**
- Arch maintainers are resetting malicious commits and banning compromised maintainer accounts; pull AUR helper updates and rebuild affected packages.
- On any host that built an AUR package since 2026-06-11, rotate browser-stored credentials, GitHub tokens, npm tokens, cloud-service tokens, SSH keys, Docker registry creds.
- Inspect `/sys/fs/bpf/` for unexpected pinned BPF maps; review systemd services for unknown additions.
- If the malicious postinstall ran as root: treat the host as compromised, reinstall from trusted media.

**Sources:** [TheHackerNews — Over 400 Arch Linux AUR Packages Hijacked](https://thehackernews.com/2026/06/over-400-arch-linux-aur-packages.html)

---

## 🟡 MEDIUM

### Klue OAuth Compromise → 'Icarus' Salesforce CRM Theft Campaign — Dormant Prototype-Integration Credential Abused To Mint OAuth Tokens For Customer Salesforce Tenants
**Product:** Klue Battlecards (market-intelligence platform) ↔ customer Salesforce CRM tenants connected via OAuth | **CVE:** None assigned | **Published:** 2026-06-18

Huntress and ReliaQuest report that the **Icarus** threat group (a fresh extortion actor that surfaced in April 2026, using the alias "mr bean" and a Session Messenger handle for contact) exploited a dormant credential for a prototype integration inside Klue's backend. They deployed malicious code that stole customer OAuth tokens, then used those tokens to drive Salesforce REST API queries against `/services/data/v59.0/sobjects` (recon) and `/services/data/v59.0/query` (exfil). Bursts of activity ranged from "almost a thousand queries in a 15-minute window" up to slower 6-hour intrusions. Stolen data includes business contacts, sales communications, price quotes, and competitive intelligence. Salesforce disabled the Klue Battlecards integration platform-wide. Klue also disabled integrations with HubSpot, SharePoint, Zoom, Gong, and Slack out of caution.

**Mitigation:**
- If your team uses Klue Battlecards, treat any data that crossed the Klue↔Salesforce OAuth bridge as exfiltrated; classify the impact and notify legal/privacy as required.
- Audit Salesforce CRM connected-apps and rotate OAuth tokens for any third-party CRM/marketing integrations.
- Review Salesforce event-monitoring logs for the API patterns described (high-volume `query` endpoint hits, esp. clustered bursts).
- Block / monitor egress to known Icarus indicators when Huntress / ReliaQuest publish IoCs.

**Sources:** [BleepingComputer — Klue OAuth Breach Linked to Icarus Salesforce Data Theft Attacks](https://www.bleepingcomputer.com/news/security/klue-oauth-breach-linked-to-icarus-salesforce-data-theft-attacks/)

---

### Operation Endgame SocGholish/FakeUpdates Takedown — 14,971 WordPress Sites Cleaned + 106 Servers/Domains Seized; Evil Corp-Linked Loader Active Since 2017
**Product:** SocGholish / FakeUpdates / GhoLoader JavaScript downloader (running on compromised WordPress installations) | **CVE:** None assigned | **Published:** 2026-06-18

The Dutch NHCTU, Canadian RCMP, US FBI, and German BKA — with Europol and Eurojust support — cleaned **14,971** SocGholish-infected WordPress sites and seized **106** servers/domains in a coordinated Operation Endgame action. SocGholish is a JavaScript-based downloader operating since at least 2017, previously linked to **Evil Corp**. The loader hijacks legitimate (primarily WordPress) sites and tricks visitors into downloading malicious payloads disguised as fake browser updates; once landed, it has been used to deploy Dridex, DoppelPaymer, Empire, Koadic, Chtonic, and Azorult.

**Mitigation:**
- Dutch police advise affected site owners to change credentials, enable MFA, delete unknown accounts, and update WordPress installations.
- For defender-side monitoring: persist hunts for "fake browser update" lure patterns — Evil-Corp-attributed actors typically rebuild infrastructure after takedowns rather than retire.
- Confirm WordPress sites you operate or partner with are not in the cleaned-list cohort (the 14,971 figure implies many partners may have been silently included).

**Sources:** [BleepingComputer — Law Enforcement Nukes SocGholish Malware From Nearly 15,000 Sites](https://www.bleepingcomputer.com/news/security/law-enforcement-nukes-socgholish-malware-from-nearly-15-000-sites/)

---

### Splunk AI Toolkit CVE-2026-20266 (CVSS 9.1) — Authenticated-Admin OS Command Injection Via Unsafe Shell Pattern In btool Configuration Helper
**Product:** Splunk AI Toolkit (versions before 5.7.4) | **CVE:** CVE-2026-20266 (high); CVE-2026-20265 (medium info-disclosure) | **CVSS:** 9.1 | **Published:** 2026-06-18

Splunk patched a critical OS command-injection bug in its AI Toolkit. Per the vendor advisory, the flaw arose from an unsafe shell pattern in the `_btool_` configuration helper that constructs OS commands without properly disabling shell interpretation. Exploitation requires authenticated administrator access. CVE-2026-20265 is a medium-severity information-disclosure bug from insecure default settings. Both are addressed in **AI Toolkit 5.7.4**.

**Mitigation:**
- Upgrade Splunk AI Toolkit to ≥ 5.7.4 on all Splunk environments where the toolkit is installed.
- Limit Splunk admin role assignments and audit admin sessions for unexpected `btool` invocations during the exposure window.
- Treat Splunk-adjacent AI tooling as part of the in-scope AI-platform attack surface — AI-toolchain CVEs continue to map cleanly onto Watchtower's AI-platform-security inclusion.

**Sources:** [SecurityWeek — Atlassian, Splunk Patch Critical Vulnerabilities](https://www.securityweek.com/atlassian-splunk-patch-critical-vulnerabilities/)

---

### Atlassian 100-Bulletin Quarterly Roll-Up — Critical Third-Party Dep Patches Across Jira/Confluence/Bitbucket/Bamboo (Axios x3, Apache Tomcat x5, Netty x1)
**Product:** Atlassian Jira, Confluence, Bitbucket, Bamboo (server + Data Center) | **CVE:** Multiple (across Axios, Apache Tomcat, Netty) | **Published:** 2026-06-18

Atlassian shipped **100 security bulletins** on 2026-06-18 addressing third-party dependency vulnerabilities across Jira, Confluence, Bitbucket, and Bamboo. Critical issues include three Axios CVEs, five Apache Tomcat CVEs, and one Netty CVE. Atlassian reports no active exploitation. The vendor recommends updating immediately.

**Mitigation:**
- Schedule patching of Jira/Confluence/Bitbucket/Bamboo Server and Data Center for the next maintenance window.
- For internet-facing Atlassian instances, treat this as a P1 because the Axios and Tomcat criticals are reachable in plenty of plausible request paths.
- Cross-check transitive Axios/Tomcat/Netty versions in your own builds — Atlassian's bump should not be the only signal.

**Sources:** [SecurityWeek — Atlassian, Splunk Patch Critical Vulnerabilities](https://www.securityweek.com/atlassian-splunk-patch-critical-vulnerabilities/)

---

## 📋 Noted / Monitoring

**INC Ransomware-as-a-Service Rust rewrite + Veeam DPAPI dumper** — THN 2026-06-18 reports 830+ victims since 2023-08, encryptors rewritten in Rust for cross-platform deployment, and an updated credential dumper targeting Veeam backups with salted DPAPI. Backup-server hardening is the relevant defender takeaway.

**DragonForce "Backdoor.Turn" — Microsoft Teams C2 abuse** — THN 2026-06-18 reports DragonForce-linked Backdoor.Turn conceals C2 inside Microsoft Teams relay infrastructure, dwelling 1–2 months undetected. Egress allowlists for `*.teams.microsoft.com` now need to expect this.

**CVE-2026-50656 — Microsoft Defender "RoguePlanet"** — no material change vs 2026-06-18. Patch still in development; tracking through next Patch Tuesday.

**"Gentlemen" RaaS EDR-killer toolkit** — BleepingComputer 2026-06-18 reports active development of a suite of EDR-killers for affiliates. Detection-bypass tradecraft, not a vulnerability.

**USB worm crypto-clipper (LNK + Tor C2)** — BleepingComputer 2026-06-18 reports a self-propagating USB clipper with wallet-address substitution. Endpoint USB-policy relevance, low Watchtower scope.

**Klue-affiliated SaaS integration shutdown impact** — BleepingComputer 2026-06-18 notes Klue also disabled integrations with HubSpot, SharePoint, Zoom, Gong, and Slack. Operational impact for teams that use Klue Battlecards.

**REDCap research-platform legacy-version exploitation (UNC6508)** — SecurityWeek 2026-06-18: ~8,500 internet-exposed REDCap instances, only 1.18% on latest 17.1.3. China-linked UNC6508 compromises legacy installs and drops InfiniteRed backdoor. Relevant if any biomedical-research partners run REDCap.

**Node.js June 2026 security releases (all active lines)** — openwall oss-security 2026-06-18 announces fixes across all active Node.js release lines. See nodejs.org/en/blog/vulnerability/june-2026-security-releases. Check supply-chain build images and Docker base layers.

**CVE-2026-43495 — Linux kernel MediaTek t7xx WWAN driver** — openwall oss-security 2026-06-18, slab OOB read. Local impact, mostly mobile-modem surface.

**CVE-2026-9692 — Mojolicious::Sessions::Storable (Perl)** — openwall oss-security 2026-06-18, session IDs generated with insufficient randomness through 0.05. Auth-bypass risk for Perl web apps still using that storage backend.

**Vim < 9.2.0671 (libsodium-encrypted files)** — openwall oss-security 2026-06-18, out-of-bounds read. Local-impact, bounded scope.

**Oracle June 2026 CPU criticals visible in OpenCVE** — Coherence CVE-2026-35307 (CVSS 10.0, scope-change), WebCenter Enterprise Capture CVE-2026-46781 (10.0, RMI RCE), WebCenter Content / Sites CVE-2026-35286 / CVE-2026-35296 (9.8, HTTP RCE), MySQL Shell CVE-2026-46850 (9.9). Follow-up triage from yesterday's Oracle CPU noted item. Prioritise WebCenter and Coherence for internet-facing instances.

**CVE-2026-38716 — InHand IR912/IR915 IoT routers** — OpenCVE 2026-06-18, command injection in export function → remote root. Low installed base in Watchtower-grade fleets but flag for field-deployed cellular routers.

**Cloudflare "vulnerability-discovery harness" blog** — defender-tooling reference (multi-stage LLM-driven vuln discovery + adversarial-review triage loop). Not a vulnerability — included so the lead doesn't get re-fetched next cycle.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | BleepingComputer, TheHackerNews, SecurityWeek, Krebs, Schneier | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/KEV, nvd.nist.gov | ❌ (HTTP 403 / no data) |
| Vendor advisories | F5 (via BleepingComputer/THN), Cisco (via SecurityWeek), Splunk/Atlassian (via SecurityWeek), MSRC | ✅ / ⚠️ MSRC (no in-window posts extractable) |
| Research / OSINT | Rapid7, avleonov, GitHub CVE search, github.com/0xMarcio/cve, dbugs.ptsecurity, fortinet TR, securitylab.github.com | ✅ / ⚠️ Fortinet TR + securitylab.github.com no in-window |
| Mailing lists | openwall oss-security, seclists.org/fulldisclosure | ✅ openwall / ⚠️ seclists last post 2026-06-15 |
| CERT / govCERT | kb.cert.org/vuls, cert.gov.ua | ✅ CERT/CC / ⚠️ cert.gov.ua empty |
| Russian-language | habr.com/tomhunter, teletype.in/@cyberok | ⚠️ both reachable, no recent posts (3.4mo / 4.4mo silence) |
| Aggregators | opencve.io, packetstormsecurity, Cloudflare security blog | ✅ opencve / ❌ packetstorm under maintenance / ⚠️ Cloudflare 1 off-topic post |

**Errors:**
- cisa.gov + cisa.gov/known-exploited-vulnerabilities-catalog — HTTP 403 (known limitation)
- attackerkb.com — HTTP 403 (known limitation)
- bugcrowd.com/disclosures — HTTP 404 (known limitation)
- googleprojectzero.blogspot.com — HTTP 404 (known limitation)
- cve.org, cve.mitre.org — JS-only / empty body
- hackerone.com/hacktivity — JS-only / empty body
- packetstormsecurity.com — site under maintenance
- nvd.nist.gov — search interface returned navigation page, no actual vuln data
- msrc.microsoft.com/blog → www.microsoft.com/en-us/msrc/blog — redirect succeeded but no in-window posts extractable

**CISA KEV:** unreached (cisa.gov 403 persists). KEV additions verified indirectly via THN / BleepingComputer / SecurityWeek mainstream coverage.

---

*Watchtower vulnerability-researcher | Cycle: 2026-06-19/night | Next: 2026-06-20/night*
