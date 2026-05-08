# Watchtower Night Report — 2026-05-08
**Cycle:** Night | **Generated:** 2026-05-08 06:30 UTC (2026-05-08T06:30:00Z)
**Sources checked:** 19/30 | **CISA KEV total:** unchanged direct fetch (403); CVE-2026-0300 + CVE-2026-6973 confirmed added via THN/BleepingComputer relays | **New KEV additions:** 2 (PAN-OS, Ivanti EPMM)

---

## 🔴 CRITICAL

### 🔄 UPDATE — Palo Alto Networks PAN-OS CVE-2026-0300 Added to CISA KEV With May 9 Deadline; Attribution to Likely Chinese State-Sponsored Cluster CL-STA-1132; Exploitation Confirmed Since April 9
**Product:** Palo Alto Networks PAN-OS — User-ID Authentication Portal (Captive Portal) | **CVE:** CVE-2026-0300 | **Status:** 0-Day, Unpatched (patches 2026-05-13), CISA KEV (added 2026-05-07), Active Exploitation | **Previous threat score:** 10

Three material developments in 24 hours on yesterday's CRITICAL: (1) **CISA added CVE-2026-0300 to KEV on 2026-05-07 with a Federal mandatory remediation deadline of 2026-05-09** — i.e., agencies are expected to disable the Captive Portal *tomorrow* given patches do not ship until 2026-05-13. (2) **Unit 42 attributed exploitation to CL-STA-1132**, a likely state-sponsored cluster whose tooling — `Earthworm` for tunneling and `ReverseSocks5` for NAT bypass — overlaps with Volt Typhoon and APT41 historical TTPs. (3) **Successful RCE has been observed in the wild since 2026-04-16** (with unsuccessful attempts beginning 2026-04-09), pushing the actual unpatched-and-attacked window to ~30 days; post-exploitation includes nginx crash-record cleanup, kernel-message cleanup, core-dump deletion, and Active Directory enumeration against domain root + DomainDnsZones. Shadowserver count revised to 5,400+ exposed VM-Series instances (was 5,800) — same order of magnitude, refined telemetry. The exposure-to-AD-enumeration playbook confirms the worst-case scenario yesterday's report flagged.

**Timeline:** 2026-04-09 first failed exploitation attempts → 2026-04-16 successful RCE in production → 2026-05-06 vendor advisory → 2026-05-07 CL-STA-1132 attribution + KEV addition → 2026-05-09 Federal deadline → 2026-05-13 patch availability → ongoing Federal compliance window.

**Why it matters:** The window between successful exploitation (April 16) and the Federal disable-or-patch deadline (May 9) is ~24 days. Any organisation that ran an exposed Captive Portal in that window must assume root-on-firewall and downstream AD enumeration. The CL-STA-1132 Earthworm/ReverseSocks5 toolset means NDR teams should hunt for outbound SOCKS5 from the firewall management plane and unusual outbound DNS to non-corporate resolvers.

**Discovered by:** Palo Alto Networks Unit 42 telemetry (vendor-internal); attribution analysis by Unit 42.

**Mitigation:**
- **Today:** Disable Captive Portal entirely or restrict the ingress ACL to trusted internal IPs only — this is your last defensive day before the Federal KEV deadline.
- Hunt firewall logs for nginx crash-record / core-dump deletion patterns and any outbound SOCKS5 (non-DNS) from the management plane during the 2026-04-09 → present window.
- Pull AD audit logs for unexpected enumeration queries against domain root and DomainDnsZones from any source matching firewall management IPs.
- Apply patches the moment they ship 2026-05-13 — public PoC repository (`p3Nt3st3r-sTAr/CVE-2026-0300-POC`) means commodity scanning will appear within hours of patch.
- IOCs: Earthworm + ReverseSocks5 binaries on firewalls; Shadowserver exposure feed for tracking VM-Series instances.

**Sources:** [BleepingComputer — PAN-OS Firewall RCE Zero-Day Exploited Since April 9](https://www.bleepingcomputer.com/news/security/pan-os-firewall-rce-zero-day-exploited-in-attacks-since-april-9/) | [SecurityWeek — Palo Alto Zero-Day Exploited in Campaign Bearing Hallmarks of Chinese State Hacking](https://www.securityweek.com/palo-alto-zero-day-exploited-in-campaign-bearing-hallmarks-of-chinese-state-hacking/) | [Palo Alto Networks Security Advisory CVE-2026-0300](https://security.paloaltonetworks.com/CVE-2026-0300)

---

### Argo CD CVE-2026-42880 (CVSS 9.6) — Plaintext Kubernetes Secret Extraction via ServerSideDiff Endpoint
**Product:** Argo CD (declarative GitOps continuous delivery for Kubernetes) | **CVE:** CVE-2026-42880 | **Status:** Patched (3.2.11, 3.3.9), GHSA-3v3m-wc6v-x4x3 published to GitHub Advisory Database 2026-05-07

The ServerSideDiff gRPC/REST endpoint fails to mask Secret data unlike sibling endpoints which call `hideSecretData()`. An authenticated user with read-only Argo RBAC permissions on an Application can call ServerSideDiff and receive **plaintext** Kubernetes Secret values — service account tokens, TLS keys, database credentials, and any API keys stored as Secrets in the etcd of the target cluster. Exploitation is amplified when the Application carries the annotation `argocd.argoproj.io/compare-options: IncludeMutationWebhook=true` because that bypasses `removeWebhookMutation()` entirely. Affected: Argo CD ≥ 3.2.0 < 3.2.11 and ≥ 3.3.0 < 3.3.9; fixed in 3.2.11 / 3.3.9. CVSS 9.6 reflects that the privileges required are *low* (read-only auth) while the impact is full Secret disclosure across the managed cluster — a privilege-escalation primitive in any environment where Argo CD is granted broad Application visibility.

**Timeline:** Upstream advisory published 2026-05-01; reviewed and published to GitHub Advisory Database 2026-05-07 (which is when most defenders see it).

**Why it matters:** Argo CD is the dominant GitOps controller across enterprise Kubernetes; in a typical deployment a developer with read-only Argo permissions has implicit cluster-Secret-read by virtue of this bug. Combined with Mini Shai-Hulud's Claude Code SessionStart persistence pattern (covered 2026-04-30) and the BufferZoneCorp toolchain wrapping (2026-05-03), the post-exploitation flow on any compromised dev workstation that has Argo read access now ends in cluster-secret exfil.

**Discovered by:** hoang-prod (reporter credit on the GHSA).

**Mitigation:**
- Upgrade Argo CD to 3.2.11 or 3.3.9 immediately.
- Audit any Application carrying `argocd.argoproj.io/compare-options: IncludeMutationWebhook=true` — this annotation makes exploitation universal (bypasses the partial defense).
- Review Argo CD RBAC: any role with `applications, get` on a Project that touches secret-bearing Applications should be considered cluster-secret-equivalent until the upgrade lands.
- Hunt etcd / Kubernetes audit logs for Server-Side Apply dry-run requests from Argo CD's service account in the past 30 days; treat any read by a non-admin Argo identity as a candidate exfil event.

**Sources:** [GitHub Security Advisory GHSA-3v3m-wc6v-x4x3 (CVE-2026-42880)](https://github.com/advisories/GHSA-3v3m-wc6v-x4x3) | [OpenCVE — CVE-2026-42880](https://app.opencve.io/cve/CVE-2026-42880)

---

### Gotenberg CVE-2026-42589 (CVSS 9.8) — Unauthenticated RCE via ExifTool Metadata Key Injection
**Product:** Gotenberg (Docker-based Chromium / LibreOffice / PDF / ExifTool conversion microservice) | **CVE:** CVE-2026-42589 | **Status:** Unpatched at disclosure; advisory GHSA-rqgh-gxv4-6657 published 2026-05-07

The `/forms/pdfengines/metadata/write` endpoint passes JSON metadata keys to `go-exiftool` without filtering control characters. An unauthenticated attacker can inject `\n` into a metadata key to smuggle arbitrary ExifTool flags — most notably `-if`, which evaluates Perl expressions and yields OS-command execution as the Gotenberg process user. The endpoint returns HTTP 200 with a valid PDF body, masking the attack from reverse-proxy logs that only watch status codes. Affected: Gotenberg v8 ≤ 8.29.1; **no patched version available** at disclosure time. A second advisory in the same batch — **CVE-2026-42596** (Critical) — is an unauthenticated SSRF in the `downloadFrom` and `webhook` parameters via default deny-list bypass; same authentication posture, same target service. Gotenberg is widely deployed in DocOps stacks (invoice generation, document conversion), CMS print pipelines, and headless-PDF SaaS backends.

**Timeline:** GHSA-rqgh-gxv4-6657 (RCE) and GHSA-4vmc-gm8v-m35h (SSRF) both published 2026-05-07. No vendor patch released; the advisories include a defensive `strings.ContainsAny(key, "\n\r\x00")` filter as a temporary mitigation.

**Why it matters:** Most teams expose Gotenberg internally on the assumption that document-conversion is low-risk, but the Docker default config has no auth and binds to all interfaces. With unauth RCE and SSRF in the same release, Gotenberg becomes a one-shot pivot for any attacker who can reach the internal Docker network — and several SaaS products embed Gotenberg as a sub-container, so a vulnerable Gotenberg may be reachable indirectly via the parent product's trusted-internal flows.

**Mitigation:**
- Place Gotenberg behind an authenticated reverse proxy *immediately* — do not wait for an upstream patch.
- Add the control-character filter in your reverse proxy or sidecar (`POST /forms/pdfengines/metadata/write` body: reject any JSON key containing `\n\r\x00`).
- Audit ingress: any direct exposure of Gotenberg container ports (default 3000/tcp) outside a trusted Docker network is a same-day patch priority.
- Hunt outbound from Gotenberg containers for unexpected DNS / HTTP to non-internal endpoints; the Perl `-if` chain typically `curl|sh`s a stage 2.

**Sources:** [GitHub Security Advisory GHSA-rqgh-gxv4-6657 (CVE-2026-42589 RCE)](https://github.com/advisories/GHSA-rqgh-gxv4-6657) | [GHSA-4vmc-gm8v-m35h (CVE-2026-42596 SSRF)](https://github.com/advisories/GHSA-4vmc-gm8v-m35h)

---

### 🔄 UPDATE — vm2 Sandbox Escape Disclosure Expands to 12 Total CVEs (Three CVSS 10.0); Maintainer Acknowledges Library Is Structurally Unsalvageable
**Product:** vm2 (Node.js sandbox library, npm — 1.3M weekly downloads) | **CVE:** CVE-2026-43997, CVE-2026-43999, CVE-2026-44005, CVE-2026-44006, CVE-2026-44008, CVE-2026-44009 (all new today) plus CVE-2026-26956, CVE-2026-44007 (covered 2026-05-07), CVE-2026-24118, CVE-2026-24120, CVE-2026-24781, CVE-2026-26332 (in the same coordinated drop) | **Status:** Patched (3.11.2 covers all) | **Previous threat score:** 7

Yesterday's report covered two vm2 sandbox escapes (CVE-2026-26956 + 44007). Today THN, the GitHub Advisory Database, and dbugs.ptsecurity confirm the disclosure was actually a coordinated 12-CVE batch, **with three CVSS 10.0 entries**: CVE-2026-43997 (host Object access via code injection), CVE-2026-44005 (prototype pollution via JavaScript escape, affects 3.9.6–3.10.5), CVE-2026-44006 (code injection via `BaseHandler.getPrototypeOf`). The remaining new entries are CVE-2026-43999 (NodeVM allowlist bypass loading `child_process`), CVE-2026-44008 (escape via `neutralizeArraySpeciesBatch()`), CVE-2026-44009 (null-proto exception escape), plus four prior-disclosed-but-grouped CVEs (24118 / 24120 / 24781 / 26332) covering `__lookupGetter__`, promise species, inspect function, and SuppressedError attack paths. **All twelve are addressed by vm2 3.11.2** — there is no minimal upgrade path; the entire library line has to roll forward. The vm2 maintainer publicly acknowledged that "future bypasses remain likely given JavaScript's complexity," confirming the structural-unsafety conclusion from yesterday's report.

**Why it matters:** Score moves from 7 → 8 because the disclosure has gone from "two escapes" to "twelve, with three rated 10.0," and because the maintainer has effectively conceded the library is unfixable. Any production SaaS that runs untrusted user code through vm2 (online IDE products, AI-coding-assistant evaluation backends, automation/no-code tools) should treat hosts touched in the past 14 days as compromise-suspect: the disclosure window is wider than a single weekly-cycle would suggest because several of these CVEs (43997, 44005, 44006) affect everything down to 3.9.6.

**Mitigation:**
- Upgrade vm2 to 3.11.2 — only complete coverage path. Do not piecemeal-patch individual CVEs.
- Strategic action remains: migrate to `isolated-vm` (V8-isolate-based) or to genuine VM/container-isolated execution. vm2's structural model — same V8 isolate, prototype-fence sandbox — has now produced 20+ documented escapes since 2020.
- Pull `process.env`, mounted-secret paths, and outbound network history for any host that has executed untrusted user code via vm2 since 2026-04-25 (the earliest plausible PoC-publication window for this batch).
- For any application currently using vm2 in production: if you cannot migrate this quarter, at least add an outbound network-egress allow-list at the host or sidecar level — sandbox escape gives RCE only if the attacker can reach C2.

**Sources:** [The Hacker News — vm2 Node.js Library Vulnerabilities Enable Sandbox Escape](https://thehackernews.com/2026/05/vm2-nodejs-library-vulnerabilities.html) | [GitHub Security Advisory GHSA-947f-4v7f-x2v8 (CVE-2026-43999)](https://github.com/advisories/GHSA-947f-4v7f-x2v8) | [GHSA-vwrp-x96c-mhwq (CVE-2026-44005)](https://github.com/advisories/GHSA-vwrp-x96c-mhwq) | [GHSA-47x8-96vw-5wg6 (CVE-2026-43997)](https://github.com/advisories/GHSA-47x8-96vw-5wg6) | [GHSA-qcp4-v2jj-fjx8 (CVE-2026-44006)](https://github.com/advisories/GHSA-qcp4-v2jj-fjx8)

---

## 🟠 HIGH

### Axios npm Supply-Chain Compromise (1.14.1, 0.30.4) — Attributed to North Korea / UNC1069; ~3% of 100M-Weekly-Downloads User Base Pulled the Backdoored Version
**Product:** axios (most-popular Node.js HTTP client; 100M+ weekly downloads) | **CVE:** None | **CVSS:** N/A | **First reported:** 2026-05-07 (SecurityWeek / Google Threat Intelligence)

Two backdoored axios versions (1.14.1 and 0.30.4) were published just past midnight on 2026-03-31 UTC and pulled ~3 hours later. In the ~3-hour window an estimated 3% of axios's user base — i.e. roughly 3M of 100M weekly downloads — fetched the malicious build, which silently installs a phantom dependency `plain-crypto-js` carrying a cross-platform RAT dropper for Windows, macOS, and Linux. **Google attributes the campaign to North Korean cluster UNC1069**, with the macOS binary overlapping prior WaveShaper samples. The publication tradecraft is precise: clean phantom dependency was pre-published 18 hours earlier to establish history, malicious dependency posted ~20 minutes before the first axios release, second backdoored axios version followed 39 minutes after the first. This is the first publicly attributed North Korean npm campaign against the most-popular HTTP client in the ecosystem; the previous DPRK npm clusters (`AppleScriptHandler`, `WaveShaper`) targeted developer-tools rather than runtime libraries. The 6-week reporting lag (March 31 → May 7) means infected hosts have had 38 days to deploy second-stage payloads before defenders heard about it.

**Why it matters:** axios sits in the dependency tree of almost every Node.js HTTP-emitting application — internal microservices, CI runners, SaaS backends, edge functions. The 3% capture rate is conservative because that's just the original-version installs; transitive consumers and lock-file pinning could push the actual touched-host count meaningfully higher. The DPRK attribution shifts the threat model: North Korean clusters typically end with cryptocurrency theft and software-supply-chain pivots back to defense / fintech targets, not opportunistic cryptominers.

**Mitigation:**
- Run `npm ls axios` (and `pnpm ls axios`, `yarn list axios`) across every CI runner and production host; downgrade any 1.14.1 or 0.30.4 build to a verified safe version (1.14.2+ or 1.13.x; 0.30.5+ or 0.29.x).
- Audit lock files (`package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`) for hashes matching the malicious versions; CI artefacts built between 2026-03-31 00:00 and 2026-04-01 should be rebuilt.
- Hunt for the phantom `plain-crypto-js` dependency in any current node_modules tree; presence indicates the backdoored axios was installed even if the parent has since been upgraded.
- Treat any developer workstation or CI runner that pulled axios in the 38-day window as IR-triage candidates: rotate cloud / SCM credentials, scan for OS-specific backdoor artefacts (Windows: registry persistence; macOS: WaveShaper-class binaries; Linux: shared object stubs).

**Sources:** [SecurityWeek — Axios NPM Package Breached in North Korean Supply Chain Attack](https://www.securityweek.com/axios-npm-package-breached-in-north-korean-supply-chain-attack/)

---

### PCPJack — Self-Propagating Cloud Credential Worm Exploiting 5 CVEs; Targets Docker / Kubernetes / Redis / MongoDB / RayML; Cleans Out TeamPCP Infections to Take Over the Cloud-Worm Niche
**Product:** Cloud infrastructure (Docker, Kubernetes, Redis, MongoDB, RayML) reachable from the internet | **CVE:** CVE-2025-29927, CVE-2025-55182, CVE-2026-1357, CVE-2025-9501, CVE-2025-48703 (all reused) | **CVSS:** N/A (campaign) | **First reported:** 2026-05-07 (SentinelOne / BleepingComputer / The Hacker News)

PCPJack is a new credential-stealing framework that scans the internet for exposed cloud infrastructure, exploits a fixed set of five known CVEs to land code execution, harvests credentials from cloud / container / developer / productivity / financial services, exfiltrates over Telegram, and **actively removes competing TeamPCP infections from the same hosts**. Five CVEs leveraged: CVE-2025-29927 (Next.js middleware auth bypass), CVE-2025-55182 (React/Next.js Server Actions deserialization, "React2Shell"), CVE-2026-1357 (WPVivid Backup unauth file upload), CVE-2025-9501 (W3 Total Cache PHP injection via cached comments), CVE-2025-48703 (CentOS Web Panel filemanager shell injection). Architecture is six Python modules orchestrated by `worm.py` (Telegram-C2 monitor), with `cloud_ranges.py` collecting AWS / GCP / Azure / Cloudflare IP ranges from Common Crawl + provider feeds and `cloud_scan.py` doing the propagation sweep. Exfil uses X25519 ECDH + ChaCha20-Poly1305 with credentials chunked to 2,800 bytes for Telegram-channel ingestion. Notably **lacks the cryptominer that's standard in this class** — SentinelOne assesses this as evidence of probable former-TeamPCP-operator authorship pivoting from mining to pure cred theft. With 100% TeamPCP-eviction logic baked into the worm, PCPJack is positioning to monopolise the cloud-cred-worm niche.

**Why it matters:** This is the first credential-harvesting worm in 2026 to combine (1) a curated CVE set targeting both web stacks (Next.js, WordPress plugins, CentOS Web Panel) and the cloud-control-plane (Docker, K8s, Redis, Mongo, Ray), (2) eviction logic that removes a specific competing botnet, and (3) Telegram-C2-only exfil with a TLS-tunneled SSH-key harvest stage. CVE-2025-29927 (Next.js) and CVE-2025-55182 (React2Shell) have been patched for ~6 months but PCPJack's success rate suggests significant unpatched footprint persists in cloud-deployed Next.js / React server-side. RayML targeting is novel — Ray clusters are widely deployed for ML workloads with default-no-auth posture, complementing the same theme covered in yesterday's Ollama Bleeding Llama report.

**Mitigation:**
- Patch the five CVEs across your perimeter: any internet-exposed Next.js (CVE-2025-29927), React2Shell-class app (CVE-2025-55182), WPVivid Backup (CVE-2026-1357), W3 Total Cache (CVE-2025-9501), or CentOS Web Panel (CVE-2025-48703) is a same-day priority target.
- Apply auth + network restriction to Docker / Kubernetes / Redis / MongoDB / Ray clusters: do not expose any control-plane API to the internet, ever — this campaign monetises that posture.
- Hunt for outbound HTTPS to `api.telegram.org` from any production server (PCPJack uses Telegram REST API, not native MTProto — the destination is the consumer Telegram API endpoint); whitelist if you have a legitimate Telegram-bot use case.
- IOC: presence of the six Python modules (`worm.py`, `parser.py`, `lateral.py`, `crypto_util.py`, `cloud_ranges.py`, `cloud_scan.py`) in any non-developer path; check `/tmp`, `/dev/shm`, and any user home directory.

**Sources:** [The Hacker News — PCPJack Credential Stealer Exploits 5 CVEs to Spread Worm-Like Across Cloud Systems](https://thehackernews.com/2026/05/pcpjack-credential-stealer-exploits-5.html) | [BleepingComputer — New PCPJack Worm Steals Credentials, Cleans TeamPCP Infections](https://www.bleepingcomputer.com/news/security/new-pcpjack-worm-steals-credentials-cleans-teampcp-infections/)

---

### Ivanti EPMM CVE-2026-6973 — Authenticated-Admin RCE Actively Exploited; Added to CISA KEV With May 10 Federal Deadline
**Product:** Ivanti Endpoint Manager Mobile (on-premises EPMM) | **CVE:** CVE-2026-6973 | **CVSS:** 7.2 | **Status:** Patched (12.6.1.1 / 12.7.0.1 / 12.8.0.1), CISA KEV (added 2026-05-07), Active Exploitation

Improper input validation in EPMM's admin interface lets an authenticated administrator execute arbitrary code on the host. Ivanti reports "very limited exploitation" but did not credit a specific actor. **CISA added CVE-2026-6973 to the Known Exploited Vulnerabilities catalog on 2026-05-07 with a Federal remediation deadline of 2026-05-10**, alongside four other Ivanti EPMM CVEs (CVE-2026-5786 through 5788, CVE-2026-7821) ranging from 7.0 to 8.9. The "authenticated admin only" gate is misleading: prior Ivanti EPMM 0-days (CVE-2026-1281, CVE-2026-1340 in January) chained admin-only RCEs with separate auth bypasses, and Ivanti's own advisory recommends rotating admin credentials specifically because pre-patch attackers may have already harvested them. Shadowserver tracks ~850 internet-exposed EPMM instances (508 in Europe, 182 in North America) — small but high-value, since EPMM controls mobile-device policy / VPN / certificate enrollment for whole organisations.

**Timeline:** Disclosure 2026-05-07 → CISA KEV 2026-05-07 → Federal deadline 2026-05-10. Patches available simultaneously: 12.6.1.1, 12.7.0.1, 12.8.0.1.

**Why it matters:** EPMM is the on-prem MDM that pushes WiFi / VPN / cert profiles to managed mobile fleets. Admin-RCE on the EPMM host is admin-of-the-mobile-fleet — including the ability to push trusted-CA certs, configure VPNs to attacker infrastructure, and enrol new devices. The chain history (Jan 0-days were 1281+1340 stacked) means assume an unauth-bypass companion is already in private hands.

**Mitigation:**
- Apply the May 7 patches today — 3-day Federal compliance window.
- Rotate every Ivanti EPMM admin credential — not just for KEV compliance, but because the previous January chain was credential-theft adjacent.
- Audit EPMM admin sessions and certificate / VPN profile pushes for the past 30 days; any unexpected profile push is an IR trigger.
- Cloud-based Ivanti Neurons for MDM is unaffected — only on-prem EPMM is in scope.

**Sources:** [BleepingComputer — Ivanti Warns of New EPMM Flaw Exploited in Zero-Day Attacks](https://www.bleepingcomputer.com/news/security/ivanti-warns-of-new-epmm-flaw-exploited-in-zero-day-attacks/) | [The Hacker News — Ivanti EPMM CVE-2026-6973 RCE Under Active Exploitation](https://thehackernews.com/2026/05/ivanti-epmm-cve-2026-6973-rce-under.html)

---

### 🔄 UPDATE — Instructure / Canvas LMS: ShinyHunters Defaces 330 Login Portals; Final Tally 8,809 Institutions / 280M Records / May 12 Ransom Deadline
**Product:** Instructure Canvas LMS (cloud SaaS — K-12, higher-ed, online learning) | **CVE:** None disclosed (Canvas data-export feature abuse) | **Status:** Active extortion | **Previous threat score:** 6

Material developments since the 2026-05-04 disclosure: (1) **scope confirmed at 8,809 educational institutions and 280M individual records**, with ShinyHunters publishing per-institution record counts ranging from tens of thousands to several million; (2) the actor escalated from data-theft-only to **direct defacement of ~330 Canvas login portals**, replacing the login UI with the extortion message and a 2026-05-12 ransom deadline (the defacement is also visible in the Canvas mobile app); (3) the secondary defacement attack used "a vulnerability in Instructure's systems that allowed the threat actor to modify the login portals" — separate from the original DAP-queries / provisioning-reports / user-API export abuse that produced the data-theft. The University of Colorado Boulder confirmed institutional impact; Rutgers said it has not yet been notified. SaaS-tenant-defacement at this scale is novel — most LMS / CRM extortion stops at data theft.

**Why it matters:** The combination of broad student-PII exposure (names, emails, private messages) + defaced public-facing login pages is engineered for maximum institutional pressure ahead of the May 12 deadline. From a defensive perspective for non-edu orgs: (1) any employee whose children attend an affected school will see their household-email / home-address / student-ID corpus surface in the credential-stuffing pool that follows; (2) the second-stage portal-defacement vulnerability suggests Instructure's tenant-isolation has more than one issue — any Canvas tenant should be on heightened monitoring through the May 12 deadline.

**Mitigation:**
- For affected orgs: prepare comms / IR for the May 12 ransom deadline; do not pay (extortion deadlines do not produce data-deletion guarantees).
- Add monitoring for Canvas API token use that does not match enrolled-instructor patterns; the original exfil came through legitimate `DAP queries` + `provisioning reports` + user APIs.
- For corporate orgs adjacent to education: expect a credential-stuffing wave against employee accounts using `firstname.lastname@employer.example` patterns harvested from the 280M-record corpus.
- Watch for the next set of "Canvas login portal" defacements — the existence of a tenant-modification vulnerability separate from data-export abuse means Instructure has at least two independent issues open.

**Sources:** [BleepingComputer — Canvas Login Portals Hacked in Mass ShinyHunters Extortion Campaign](https://www.bleepingcomputer.com/news/security/canvas-login-portals-hacked-in-mass-shinyhunters-extortion-campaign/) | [BleepingComputer — Instructure Hacker Claims Data Theft From 8,800 Schools, Universities](https://www.bleepingcomputer.com/news/security/instructure-hacker-claims-data-theft-from-8-800-schools-universities/)

---

### Claude Code MCP Hijacking + "TrustFall" Auto-Trust Folder Bypass — Cross-Vendor AI-Coding-Agent Attack Chain Affects Claude Code, Gemini CLI, Cursor CLI, Copilot CLI
**Product:** AI coding assistants — Anthropic Claude Code, Google Gemini CLI, Cursor CLI, GitHub Copilot CLI | **CVE:** None assigned | **CVSS:** N/A | **First reported:** 2026-05-07 (SecurityWeek — two adjacent disclosures: Adversa.AI's "TrustFall" + an unnamed researcher's MCP hijacking)

Two adjacent disclosures hit on 2026-05-07 against the same trust-boundary class in AI-coding-agents:

**(a) MCP Hijacking via malicious npm `postinstall`:** A malicious npm package writes pre-approved trust-dialog entries to `~/.claude.json` during install (Claude Code stores OAuth tokens for dynamic-auth MCP servers there in *plaintext*). The hook then injects an attacker-controlled MCP proxy URL; subsequent OAuth refresh / session establishment routes through the attacker, harvesting the OAuth tokens silently. The hook is self-healing — it rewrites the configuration after token rotation or URL edits. **Anthropic responded "out of scope"** on the basis that the user has already consented to the folder-trust dialog; Adversa disputes whether the user can give informed consent without seeing folder contents.

**(b) "TrustFall" cross-vendor auto-trust (Adversa.AI):** A malicious repo plants standard MCP-config JSON (e.g. `.mcp.json` / `.gemini/settings.json` / equivalents) in the cloned tree. When the user clicks "Yes, Trust" on the folder-trust dialog **once**, all four agents (Claude Code, Gemini CLI, Cursor CLI, Copilot CLI) auto-spawn the configured MCP servers — RCE-equivalent on the developer workstation. All four default to "Yes/Trust" in the dialog. In CI/CD pipelines this enables harvesting signing certs, deploy keys, npm/PyPI publish credentials — i.e. the Salesloft-Drift class of incident, but at the AI-coding-agent layer rather than the SaaS layer.

**Why it matters:** This is the third AI-agent-config-as-code disclosure in 9 days (Mini Shai-Hulud Claude SessionStart 2026-04-30, Gemini CLI CVE 10.0 2026-05-01, TrustFall + Claude OAuth 2026-05-07). The pattern is consistent: the AI-agent vendors have engineered "consent" surfaces that are easy to manipulate from a malicious repo or package. From a defensive posture, **AI-agent config files are no longer "configuration" — they are executable code that runs implicitly when the right wrapper opens them**. CI guardrails need to treat `.claude/`, `.gemini/`, `.cursor/`, `.copilot/` directories the same way they treat `.github/workflows/` and `.gitlab-ci.yml`.

**Mitigation:**
- Block AI-agent config dirs in CI checkouts: explicit `.gitignore`-equivalent for `.claude/`, `.gemini/`, `.cursor/`, `.copilot/`, `.mcp.json` in any repo cloned into a CI runner.
- For developer workstations: keep AI-agent CLIs out of unattended-CI roles; require human review before pointing any AI-coding-agent at a third-party-controlled repo.
- For Claude Code specifically: audit `~/.claude.json` for unexpected MCP server URLs; rotate any OAuth tokens that may have transited through an attacker proxy.
- Monitor outbound to non-vendor MCP hostnames from any Claude Code / Gemini CLI / Cursor CLI / Copilot CLI host.
- Anthropic has declined to fix the OAuth-proxy issue as a vulnerability; teams that rely on Claude Code in security-sensitive contexts should consider this a permanent risk and design accordingly (per-project credentials, scoped tokens with short TTLs).

**Sources:** [SecurityWeek — Claude Code OAuth Tokens Can Be Stolen Through Stealthy MCP Hijacking](https://www.securityweek.com/claude-code-oauth-tokens-can-be-stolen-through-stealthy-mcp-hijacking/) | [SecurityWeek — AI Coding Agents Could Fuel Next Supply Chain Crisis](https://www.securityweek.com/ai-coding-agents-could-fuel-next-supply-chain-crisis/) | [SecurityWeek — Gemini CLI Vulnerability Could Have Led to Code Execution, Supply Chain Attack](https://www.securityweek.com/gemini-cli-vulnerability-could-have-led-to-code-execution-supply-chain-attack/)

---

### Cisco Unity Connection Authenticated SSRF→RCE-as-Root — CVE-2026-20034 / CVE-2026-20035 Plus Multi-Product Cisco Patch Batch
**Product:** Cisco Unity Connection (enterprise unified messaging / voicemail), with adjacent fixes for SG350/SG350X switches, IoT Field Network Director, Crosswork Network Controller, NSO, ISE, Slido, Prime Infrastructure, ECE | **CVE:** CVE-2026-20034, CVE-2026-20035 (Unity Connection); CVE-2026-20185 (SG350 SNMP DoS); CVE-2026-20167 (IoT FND DoS); CVE-2026-20188 (CNC/NSO DoS, covered 2026-05-07) | **Status:** Patched | **Published:** 2026-05-07

Cisco's mid-week semi-annual batch ships a high-severity authenticated SSRF in Unity Connection (CVE-2026-20034 + CVE-2026-20035) that allows arbitrary code execution **as root** by sending crafted HTTP requests through insufficient input validation. Unity Connection sits in most enterprise voice / messaging stacks and is integrated into the SIP plane with privileged access to mailbox stores. Companion fixes: CVE-2026-20185 SNMP DoS on SG350/SG350X switches (any SNMP version, requires read-only or read-write community), CVE-2026-20167 IoT Field Network Director web-interface DoS via crafted input, plus seven medium-severity issues across Slido / Prime Infrastructure / ISE / ECE. CVE-2026-20188 (Crosswork Network Controller / NSO unauth DoS, covered yesterday) is part of the same release wave. No active exploitation reported on any of these.

**Why it matters:** Authenticated RCE on Unity Connection is post-credential-compromise lateral-movement gold — Unity tends to share an authentication backend with Active Directory, and root on a Unity host gives mailbox content access for any user the system serves. The combined-batch nature also matters: an org running Cisco enterprise infrastructure typically has 4-6 of these products in service, so the patching cycle is non-trivial.

**Mitigation:**
- Apply the Unity Connection patch first — authenticated RCE-as-root is the highest-blast-radius item in the batch.
- For SG350/SG350X: rotate SNMPv3 credentials and disable SNMPv1/v2c if you can; CVE-2026-20185 only requires *valid* community strings, so credential rotation matters.
- For IoT FND: restrict the web interface to a management VLAN — DoS via crafted input is a same-day patch but the management plane should not be broadly reachable anyway.
- See yesterday's 📋 Noted item for CVE-2026-20188 mitigation (CNC ≤ 7.1 / NSO ≤ 6.3 → CNC 7.2 / NSO 6.4.1.3 / 6.5).

**Sources:** [SecurityWeek — Cisco Patches High-Severity Vulnerabilities in Enterprise Products](https://www.securityweek.com/cisco-patches-high-severity-vulnerabilities-in-enterprise-products/) | [BleepingComputer — New Cisco DoS Flaw Requires Manual Reboot to Revive Devices](https://www.bleepingcomputer.com/news/security/new-cisco-dos-flaw-requires-manual-reboot-to-revive-devices/)

---

## 🟡 MEDIUM

### OpenStack Cyborg Access Control Bypass — OSSA-2026-011 (CVE-2026-40213 / CVE-2026-40214)
**Product:** OpenStack Cyborg (accelerator-management service) | **CVE:** CVE-2026-40213, CVE-2026-40214 | **Published:** 2026-05-07 (oss-security)

Two coordinated access-control flaws in OpenStack Cyborg: CVE-2026-40213 (default policy rules on `device`, `deployable`, and `attribute` API endpoints use unconditional-allow checks, granting access to *any authenticated user* regardless of role or project scope, v5.0.0+); CVE-2026-40214 (Accelerator Request resources lack project-ownership validation, enabling cross-tenant ARQ enumeration / modification / deletion, v3.0.0+). Affected: Cyborg ≥3.0.0 <14.0.1, ≥15.0.0 <15.0.1, ≥16.0.0 <16.0.1. Patches across all release branches (24 PRs landed).

**Mitigation:** Upgrade Cyborg to 14.0.1 / 15.0.1 / 16.0.1 per release branch; until then, restrict Cyborg API access at the load-balancer to admin-only identities. Audit ARQ access logs for cross-tenant queries.

**Sources:** [oss-security 2026/05/07/6 — OSSA-2026-011](https://www.openwall.com/lists/oss-security/2026/05/07/6)

---

### Postorius (Mailman 3) ≤1.3.13 — Admin UI XSS Actively Exploited; No Patched Release Available
**Product:** Postorius — web admin UI for GNU Mailman 3 mailing-list software | **CVE:** None assigned | **Published:** 2026-05-07 (oss-security)

Reflected/stored XSS in the Postorius admin UI is reported as **actively exploited**. The fix was merged upstream in January 2025 but **no official Postorius release containing the patch has been made**, leaving distributions that package the latest tagged release (1.3.13) vulnerable unless they backport. Mailman 3 is widely deployed on academic, FOSS-project, and enterprise mailing-list infrastructure; admin compromise via XSS gives list-takeover (subscribe/unsubscribe arbitrary addresses, modify list config, post as admin).

**Mitigation:** Apply the upstream commit referenced in the advisory directly to your Postorius deployment if you cannot wait for the official release; restrict admin-UI access to a management VLAN; review Mailman list-admin sessions for unexpected configuration changes.

**Sources:** [oss-security 2026/05/07/3 — XSS in Postorius (Mailman 3)](https://www.openwall.com/lists/oss-security/2026/05/07/3)

---

### filebrowser CVE-2026-42542 (CVSS 9.1) — Unauth Path Traversal Enables File Deletion via Public Share
**Product:** filebrowser (Go-based self-hosted file management UI) | **CVE:** CVE-2026-42542 | **Published:** 2026-05-07 (GHSA-fwj3-42wh-8673)

Public-share `DELETE` API joins attacker-controlled path with a trusted base path *before* sanitization, enabling `../` traversal out of the shared directory. An unauthenticated attacker with a valid public-share hash and delete permissions on the share can delete arbitrary files within the owner's storage scope. Two vulnerable code paths: stable releases at `/public/api/resources?hash=<>&path=../victim` (middleware.go:111) and dev-build bulk-delete at `/public/api/resources/bulk?hash=<>` with JSON traversal payload. Affected: all versions before commit `0.0.0-20260501183844-112740bdd41d`. Fixed in that commit and later.

**Mitigation:** Upgrade to the patched build; do not expose filebrowser public-share links to the internet without rate-limiting / WAF; audit deleted-files logs for `../`-pattern paths in the last 30 days.

**Sources:** [GitHub Security Advisory GHSA-fwj3-42wh-8673](https://github.com/advisories/GHSA-fwj3-42wh-8673)

---

### Linux Kernel KTLS + Sockmap Reverse-Order Use-After-Free (CVE Pending) — Kernel Crash and UAF With CAP_BPF + CAP_NET_ADMIN
**Product:** Linux kernel — KTLS + BPF sockmap interaction | **CVE:** Pending CNA assignment | **Published:** 2026-05-07 (oss-security)

Forward-order attachment (KTLS first, then sockmap) is blocked, but reverse-order setup (sockmap first, then `tls_init`) bypasses the protection and corrupts the data path: TCP receive queue is drained without sequence-number updates, leading to stale-data handling, kernel WARN_ON_ONCE crashes, and a use-after-free that may yield privesc following the same exploitation pattern as CVE-2025-37756. Confirmed on Linux 6.12.77 (LTS) and likely affects all kernels supporting both KTLS and sockmap. Requires `CAP_BPF` + `CAP_NET_ADMIN` to trigger — i.e., privileged-container or limited-but-elevated user. Possible container escape.

**Mitigation:** Apply the suggested fix to `tls_init` in `net/tls/tls_main.c` blocking reverse-order setup; audit container security profiles to ensure CAP_BPF is not handed out broadly. Once a CVE lands, expect distribution kernel updates.

**Sources:** [oss-security 2026/05/07/1 — KTLS + sockmap reverse-order UAF](https://www.openwall.com/lists/oss-security/2026/05/07/1)

---

## 📋 Noted / Monitoring

**🔄 UPDATE — CVE-2026-31431 "Copy Fail" / "Copy Fail 2" / "Dirty Frag" Linux LPE — Independent N-Day PoC Published 2026-05-07 by `afflicted.sh`** — `SiCk` published an independent n-day weaponisation derived from the public netdev fix commit (`f4c50a4034e62ab75f1d5cdd191dd5f9c77fdff4`) and Brad Spengler's public identification of it as security-relevant; explicitly states no contact with linux-distros embargo. PoC is one-line Python. Combined with Theori's prior 100%-reliable exploit (covered 2026-05-05) the Copy Fail family now has at least three public exploits and one cross-distribution embargo break. CISA Federal deadline remains 2026-05-15.

**🔄 UPDATE — Cloudflare published "How Cloudflare Responded to Copy Fail" (2026-05-07)** — Defensive case study describing how Cloudflare rolled mitigation across its infrastructure with zero customer impact and no malicious exploitation observed in their fleet. Useful template for any large Linux fleet that has not yet completed CVE-2026-31431 patching.

**Dirty Frag Universal Linux LPE (no CVE) — Public PoC, Embargo Broken Pre-Patch** — Two-bug chain (xfrm ESP4/ESP6 + RxRPC/RxKAD) chained for root via direct `/usr/bin/su` overwrite or `/etc/passwd` empty-password edit. Affects all major Linux distributions. PoC + 192-byte minimal ELF + fcrypt brute-force tool published at dirtyfrag.io. **Out-of-immediate-scope as LPE-only** but high-interest because the embargo broke pre-patch and the workaround is `modprobe install esp4 /bin/false` etc — straightforward on hardened production hosts. Watch for a CVE assignment in the next 14 days; LPE-only items can become in-scope when added to KEV (see Copy Fail).

**TCLBanker (BleepingComputer 2026-05-07)** — Brazilian-targeting banking trojan distributed via trojanised Logitech AI Prompt Builder MSI installer; self-spreads through WhatsApp web (browser-stored auth hijack, hidden Chromium instances) and Outlook (COM automation contact harvest). Targets 59 banking / fintech / crypto platforms but checks Brazilian timezone / keyboard / locale. Likely LATAM-confined for now but historical pattern is geo-expansion within 6 months. **Mostly out-of-scope (consumer banking malware)** but the WhatsApp / Outlook propagation pattern is a notable enterprise contact-list-poisoning vector if a Brazilian employee gets infected.

**Microsoft "Beagle" Backdoor via Fake Claude AI Website (BleepingComputer 2026-05-07)** — Same ClickFix-class campaign as the 2026-04-18 fake-Claude-Installer disclosure, now with a dedicated Beagle Windows backdoor as second stage. Same defensive playbook: alert on `claude.ai`-impersonating domains in DNS / proxy logs.

**Australia ACSC Warns of ClickFix → Vidar Stealer Campaign (BleepingComputer 2026-05-07)** — National advisory; same SE class as the BlackFile / SNOW / Cordial Spider chain. Vidar Stealer harvests browser creds + crypto wallets.

**Hackers Abuse Google Ads for GoDaddy ManageWP Login Phishing (BleepingComputer 2026-05-06)** — Sponsored-search-result poisoning targeting WordPress-management-plane creds. Same general class as the Anodot SaaS-token theft pattern (covered 2026-05-07): legitimate-channel-trust as initial-access against SaaS administrative interfaces.

**ZiChatBot PyPI Supply-Chain (THN 2026-05-07)** — `uuid32-utils` (1,479 dl), `colorinal` (614 dl), `termncolor` (387 dl) — uploaded July 2025, removed before being noticed. Zulip REST API as C2 (novel C2 channel — same defensive pattern as Telegram-API-as-C2). Kaspersky 64% similarity to OceanLotus / APT32 dropper.

**intercom-client npm v7.0.4 Compromise (Mini Shai-Hulud)** — Compromised release on 2026-04-30 15:00-17:00 UTC, harvests cloud creds (AWS/GCP/Azure), env vars, .env files, GitHub/npm tokens, SSH keys. Approximately 2-hour exposure window. Already covered as part of Mini Shai-Hulud campaign (2026-04-30 / 2026-05-01); flag here for explicit IOC reference.

**intercom-php Composer Tag Compromise (Mini Shai-Hulud, GHSA-gr3r-crp5-qrrm)** — Companion to the npm intercom-client compromise; tag-based push to GitHub Composer registry. Pattern reinforces Mini Shai-Hulud's multi-ecosystem reach: npm + PyPI + Composer now confirmed.

**CVE-2026-44523 note-mark/backend (Go) — JWT Secret Weakness (CVSS 10.0)** — Backend accepts any base64-decodable string as JWT secret (no minimum length / entropy enforcement); allows offline brute-force of short keys to forge admin tokens. Niche application.

**CVE-2026-44542 filebrowser** — listed under MEDIUM above; flagged here for repeat reference in any team that uses filebrowser as a quick file-share.

**CVE-2026-42596 Gotenberg SSRF (companion to RCE in CRITICAL)** — Same Gotenberg release adds an unauth SSRF in `downloadFrom` and `webhook` parameters via default deny-list bypass. Less severe than the RCE but same defensive footing — put Gotenberg behind an authenticated reverse proxy.

**CVE-2026-41050 Fleet (Helm impersonation bypass)** — GitOps Fleet operator allows Helm impersonation that retains cluster-admin during template rendering. Niche but combine-with-Argo CD for K8s-native shops.

**CVE-2026-44484 PyTorch Lightning 2.6.2 / 2.6.3** — Already covered 2026-05-01 as Mini Shai-Hulud Python-ecosystem expansion; Lightning AI advisory now formalised as CVE on 2026-05-07. CVSS 9.3.

**Linux io_uring zcrx Freelist OOB Write (oss-security 2026/05/07/5–11)** — CVE pending. Linux 6.15+ vulnerability; upstream fix landed 2026-04-21 (`770594e`) but not yet in stable. Reporter behaviour suggests AI-generated disclosure; maintainer skepticism. Watch for CVE assignment.

**Vim Heap Buffer Overflow in Spell File Loading (oss-security 2026/05/07/9)** — Vim < 9.2.0450; integer overflow → heap-based buffer overflow on crafted `.spl`. Requires `'modeline'` enabled + crafted spell file in runtimepath OR explicit `:setlocal spelllang=foo` action. Practical impact is local DoS, not RCE. Patch in 9.2.0450.

**Cisco SG350/SG350X SNMP DoS CVE-2026-20185** — Listed under HIGH above (Cisco batch). Authenticated DoS via SNMP — listed here only for completeness; the headline Cisco item is Unity Connection.

**Cisco IoT FND DoS CVE-2026-20167** — Listed under HIGH above (Cisco batch).

**Chrome 148 Stable — 127 Security Fixes (SecurityWeek 2026-05-07)** — Critical integer overflow + use-after-free fixes among the 127. **Browser sandbox out of scope per Watchtower scope rules** but worth tracking as a baseline-cadence indicator: 127 fixes is unusually large.

**Microsoft April Updates Cause Backup Failures (BleepingComputer)** — Operational issue confirmed by Microsoft; April patches blocked a vulnerable driver that some backup software depended on. Workaround / hotfix expected. **Operational only — no security impact in either direction.**

**Smart Glasses for Authorities (Schneier 2026-05-07)** — ICE building face-recognition smart glasses linked to government databases. **Out of scope** but worth surfacing because surveillance-capability normalisation has secondary impacts on threat models for sensitive employees.

**Taiwan High-Speed Rail Hack via TETRA Replay (BleepingComputer 2026-05-07)** — University student decoded TETRA radio parameters with SDR, transmitted General Alarm signal; halted four trains for 48 minutes on 2026-04-05. **OT-adjacent / out of scope** but reinforces the pattern that long-deployed (19-year) TETRA networks with un-rotated parameters are exposed to hobbyist-level RF attacks.

**MetalSoft / EnOcean SmartServer Flaws Expose Buildings to Remote Hacking (SecurityWeek 2026-05-07)** — Building-automation vulnerabilities; CVEs not enumerated in the headline; OT-adjacent.

**TeamPCP Moves From OSS to AWS Environments (SecurityWeek 2026-05-07)** — Threat-tracker update; primarily an attribution / scope item. Companion to PCPJack-as-eviction-rival (HIGH).

**npm math.js CVE-2026-41139 (CVSS 8.8)** — Mathematical-library vulnerability; ecosystem niche — relevant if you run math.js in a server context with untrusted input.

**Hexpm Decimal CVE-2026-32686** — Erlang/Elixir decimal-arithmetic library vulnerability; ecosystem niche.

**WordPress Bricks Builder CVE-2026-41554 (CVSS 7.1)** — WP page-builder plugin; relevant to any WordPress fleet running Bricks.

**Wallos CVE-2026-41688 (CVSS 7.7)** — Self-hosted subscription tracker.

**PyPI Docling-Graph CVE-2026-44520** — Python library vulnerability.

**Go gittuf CVE-2026-44544** — Git-trust framework; niche.

**Weblate CVE-2026-44264** — Translation platform; niche; medium severity.

**Karakurt Ransomware Negotiator Sentenced to Prison (SecurityWeek 2026-05-05)** — Deniss Zolotarjovs convicted; legal-action item, not a finding.

**Two US Security Experts Sentenced for Helping Ransomware Gang (SecurityWeek 2026-05-01)** — Insider-threat ground-truth: practitioners-turning-criminal still happens.

**Two Americans Sentenced for North-Korean Laptop-Farm Operation (BleepingComputer 2026-05-07)** — DPRK-IT-worker insider-risk pattern; the laptop-farm-as-service model is becoming a recurring criminal-justice case. Worth bookmarking for HR/IT teams running developer-hire pipelines.

**Webinar — Why Modern Attacks Require Both Security and Recovery (BleepingComputer)** — Sponsored content; not a finding.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com | ✅ |
| Government / KEV | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog, cert.gov.ua | ❌ (cisa 403; cert.gov.ua empty) — KEV additions confirmed via THN/BleepingComputer relays (CVE-2026-0300, CVE-2026-6973) |
| Vendor / vuln disclosure | rapid7.com, fortinet.com/blog/threat-research, securitylab.github.com, msrc.microsoft.com/blog, blog.cloudflare.com/tag/security, attackerkb.com | ✅ rapid7 / securitylab / cloudflare; ❌ fortinet (no new), msrc/attackerkb (JS / 403) |
| OSS / CVE feeds | seclists.org/fulldisclosure, openwall.com/lists/oss-security, opencve.io, github.com/search?q=CVE, github.com/0xMarcio/cve, kb.cert.org/vuls | ✅ openwall (12 messages May 7), opencve, github search (rate-limited but partial); ❌ seclists redirect, kb.cert old data, 0xMarcio JS |
| NVD-class | nvd.nist.gov, cve.mitre.org, cve.org | ❌ all JS / no extractable data |
| Bug bounty | hackerone.com/hacktivity, bugcrowd.com/disclosures | ❌ JS / 404 |
| Research / OSINT | krebsonsecurity.com, schneier.com, avleonov.com, googleprojectzero.blogspot.com, dbugs.ptsecurity.com, habr.com/ru/companies/tomhunter, teletype.in/@cyberok | ✅ krebs (no May 7-8 posts), schneier, avleonov (no new), dbugs; ❌ googleprojectzero (redirect), habr / teletype (no new) |
| Off-list productive | openwall.com/lists/oss-security (counted above), socket.dev/blog, labs.watchtowr.com, trendmicro.com, securelist.com (Kaspersky), github.com/advisories | ✅ socket (no new), labs.watchtowr (no new), github advisories (~17 fresh GHSAs); ❌ trendmicro 403, securelist ECONNREFUSED |
| Packet aggregator | packetstormsecurity.com (now packetstorm.news) | ❌ only TOS page reachable; advisory listings not extractable |

**Total active sources:** 30 | **Checked:** 19 | **With findings:** 12 | **Unreachable (11):** cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog, attackerkb.com, packetstormsecurity.com, nvd.nist.gov, cve.mitre.org, cve.org, googleprojectzero.blogspot.com, msrc.microsoft.com/blog, hackerone.com/hacktivity, bugcrowd.com/disclosures

**CISA KEV:** Direct fetch returns 403 (consistent). Two new KEV additions confirmed via THN/BleepingComputer relays today: **CVE-2026-0300** (PAN-OS, Federal deadline 2026-05-09) and **CVE-2026-6973** (Ivanti EPMM, Federal deadline 2026-05-10). CVE-2026-31431 (Copy Fail) deadline remains 2026-05-15.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-08/night | Next: 2026-05-09/night*
