# Watchtower Night Report — 2026-07-11
**Cycle:** Night | **Generated:** 2026-07-11 00:08 UTC (2026-07-11T00:08:46Z)
**Sources checked:** 24/30 | **CISA KEV total:** unreachable (403) | **New KEV additions:** unreachable

---

## 🔴 CRITICAL

### Progress ShareFile Storage Zone Controller — Vendor-Mandated Emergency Shutdown Over "Credible External Security Threat" (2026-07-10; No CVE Assigned; Possible New Zero-Day or Live Exploitation of April CVE-2026-2699/2701 Chain) (CVSS n/a)
**Product:** Progress ShareFile — Storage Zone Controllers (on-prem Windows) | **CVE:** None assigned | **Status:** Vendor-mandated shutdown / suspected active exploitation

Progress Software emailed ShareFile customers who use on-prem Storage Zone Controllers overnight on 2026-07-09→10 instructing them to immediately shut down the Windows servers hosting the controllers due to a "credible external security threat." Progress temporarily disabled ShareFile accounts using SZCs as a precaution and states it has no indication of unauthorized access "at this time"; the notice first surfaced when a customer posted the email to r/sysadmin. Progress has not disclosed whether this is a new zero-day, exploitation of the still-unpatched-in-some-fleets watchTowr CVE-2026-2699 auth-bypass + CVE-2026-2701 RCE chain from April 2026, or a non-CVE compromise vector (stolen keys, upstream credential theft). No patch has been offered — the mitigation is server shutdown, which by itself signals no available fix.

**Timeline:** 2026-04 — watchTowr disclosed CVE-2026-2699 (auth bypass, CVSS 9.8) + CVE-2026-2701 (RCE, CVSS 9.1) pre-auth webshell chain, vendor patched → 2026-07-09/10 — Progress emails customers to shut down SZCs, temporarily disables SZC access → 2026-07-10 — customer surfaces the email publicly.

**Why it matters:** ShareFile Storage Zone Controllers are edge components that hold and proxy customer file data, are typically DMZ-facing, and have a well-documented pre-auth webshell chain from April. Progress's own response — an urgent shutdown order — indicates the vendor believes the risk is high enough that switching servers off is preferable to keeping them online while investigating. For any Watchtower reader running SZCs, treat this as "assume active exploitation" until the vendor publishes technical detail.

**Discovered by:** Progress Security (via customer notice)

**Mitigation:**
- Follow Progress's instruction: manually shut down the Windows servers hosting Storage Zone Controllers immediately; do not rely on the temporary account-level access disable alone.
- If SZCs were reachable from the internet since April 2026 and CVE-2026-2699/2701 patching lagged, treat those hosts as potentially compromised: preserve memory + disk images, hunt for `w3wp.exe` spawning `cmd.exe`/`powershell.exe`, look for unexpected ASPX files under IIS webroots, review Windows event/IIS logs for anomalous X-Forwarded-For headers and unauthenticated `/cifs` or `/files` requests.
- Rotate any long-lived credentials, storage-account keys, and reverse-proxy shared secrets that were reachable from the SZC hosts.
- Monitor Progress's advisory channel (docs.sharefile.com, product@progress) for the technical writeup and revised patch.
- Notify downstream tenants of the account-access disable window; check ShareFile audit logs for successful API activity from unexpected source IPs in the 24 hours preceding shutdown.

**Sources:** [BleepingComputer — Progress urges ShareFile admins to shut down servers over "credible" threat](https://www.bleepingcomputer.com/news/security/progress-urges-sharefile-customers-to-shut-down-servers-over-credible-threat/) | [The Hacker News — URGENT: Progress Tells ShareFile Customers to Shut Down](https://thehackernews.com/2026/07/urgent-progress-tells-sharefile.html) | [watchTowr Labs — original CVE-2026-2699/2701 chain (April 2026)](https://labs.watchtowr.com/youre-not-supposed-to-sharefile-with-everyone-progress-sharefile-pre-auth-rce-chain-cve-2026-2699-cve-2026-2701/)

---

### Gitea CVE-2026-20896 (CVSS 9.8) — Docker-Image Default `REVERSE_PROXY_TRUSTED_PROXIES=*` Turns `X-WEBAUTH-USER` Header Into One-Header Admin Impersonation; Actively Exploited From 2026-07-07 (~13 Days After Disclosure), ProtonVPN Probe Node Observed (CVSS 9.8)
**Product:** Gitea official Docker image (versions ≤ 1.26.2 default configuration) | **CVE:** CVE-2026-20896 | **Status:** Active exploitation confirmed, patched in 1.26.3/1.26.4

Gitea's official Docker image ships `REVERSE_PROXY_TRUSTED_PROXIES=*` in the default config, which — once reverse-proxy authentication is enabled — trusts the `X-WEBAUTH-USER` HTTP header from every source IP. A remote attacker who can reach the Gitea port can therefore send a single request with `X-WEBAUTH-USER: gitea_admin` (or any target username) and be logged in with that account's privileges, including administrator, with no password, token, or MFA challenge. Security researcher Michael Clark documented active exploitation beginning approximately 13 days after Gitea's public advisory, with initial reconnaissance traced to a ProtonVPN exit node (159.26.98.241) — attackers are enumerating exposed instances and pivoting to repository/secret exfiltration. Approximately 6,200 Gitea instances are publicly reachable; the vulnerable population is smaller (only those with reverse-proxy auth enabled) but the exploit is a single crafted HTTP header, requires no prior access, and yields full admin.

**Timeline:** 2026-06-24 — Gitea 1.26.3 released with the fix (regression addressed in 1.26.4 shortly after) → 2026-07-07 — active exploitation reported by Michael Clark and confirmed by multiple threat-intel feeds → 2026-07-10 — BleepingComputer, SecurityWeek, The Hacker News amplify.

**Why it matters:** Gitea is one of the two most common self-hosted Git servers in engineering environments (alongside Forgejo/Gogs) and holds source code + CI secrets — an admin-impersonation primitive here typically leads to CI credential theft, source poisoning, and lateral movement into cloud infra via committed keys. The one-header exploit is trivial to weaponize into a mass-scan → repo-clone → secret-scan pipeline, and the 13-day lag between advisory and exploitation is exactly the window in which most self-hosted patch cycles slip.

**Discovered by:** Gitea security team (initial advisory); active exploitation reported by Michael Clark

**Mitigation:**
- Upgrade the Docker image to Gitea 1.26.4 immediately (skip 1.26.3 — it introduced a regression).
- If upgrade is not possible in the next hours, restrict `REVERSE_PROXY_TRUSTED_PROXIES` in `app.ini` (or docker-compose env) to the specific IP(s) of your reverse proxy, never `*`. Alternatively disable reverse-proxy auth entirely (`ENABLE_REVERSE_PROXY_AUTHENTICATION = false`) if not in use.
- Hunt: check Gitea access logs for successful requests carrying `X-WEBAUTH-USER` from source IPs outside your reverse proxy, especially `admin`, `gitea_admin`, or CI service accounts. Review recent admin-session activity, personal-access-token creation, and repository-clone events; rotate any long-lived tokens present at the time of a suspicious login.
- Egress-block SSH clone/deploy-key usage from unexpected outbound IPs on Gitea hosts and force a re-encrypted CI-secret rotation if repos containing pipeline secrets were exposed.

**Sources:** [BleepingComputer — Hackers exploit critical auth bypass in Gitea Docker image](https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-auth-bypass-in-gitea-docker-image/) | [The Hacker News — Threat Actors Probe Gitea Docker Flaw 13 Days After Disclosure](https://thehackernews.com/2026/07/threat-actors-probe-gitea-docker-flaw.html) | [SecurityWeek — Critical Gitea Flaw Under Active Exploitation](https://www.securityweek.com/critical-gitea-flaw-under-active-exploitation-researchers-warn/)

---

## 🟠 HIGH

### Zimbra Collaboration Suite 10.1.19 — Critical Stored XSS in Classic Web Client Reported by Google TAG (No CVE Assigned); Open-Email Trigger, APT29/APT28 History of Zimbra XSS Exploitation
**Product:** Zimbra Collaboration Suite (Classic/Ajax Web Client) | **CVE:** Not yet assigned | **CVSS:** Not published (vendor classifies as critical) | **First reported:** 2026-07-08 (patch), publicised 2026-07-10

Zimbra released ZCS 10.1.19 on 2026-07-08 to patch a stored cross-site scripting vulnerability in the Classic (Ajax) Web Client — a specially crafted email executes JavaScript in the recipient's session upon open, yielding session-cookie theft, mailbox contents access, account settings tampering, and potentially rule-based persistent exfiltration. The flaw was reported by Google's Threat Analysis Group; TAG almost exclusively surfaces bugs that are already known to be under state-sponsored exploitation against high-risk individuals (dissidents, journalists, government researchers), and Zimbra's own recent history — APT29 mass-exploited Zimbra XSS in 2024, APT28 exploited another Zimbra XSS against Ukrainian government targets in March 2025 — makes this fit a well-worn pattern. Only Classic Web Client users are affected; users of the Modern client are not.

**Body:** No CVE has been assigned at time of publication. Vendor guidance is to upgrade to ZCS 10.1.19 without delay if Classic Web Client is enabled. The trigger is server-side stored (email body → rendered on message open), which means the attacker only needs the target's Zimbra address — no interaction beyond opening the email is required. Google TAG's involvement is the strongest available signal that in-the-wild exploitation exists even though Zimbra has not confirmed it.

**Mitigation:**
- Upgrade to Zimbra 10.1.19 across all Zimbra fleet nodes immediately; verify by inspecting the ZCS package build version on each mailbox server.
- If upgrade cannot happen in the next 24 hours, force all users to the Modern Web Client (`zmprov modifyServer <host> zimbraFeatureMailForwardingEnabled TRUE` and disable Classic per-COS via `zimbraFeatureClassicUIEnabled FALSE`); Classic is the only affected surface.
- Hunt: review Zimbra mail-store logs for unusual outbound API calls originating from user sessions immediately after inbound mail delivery; check `mailbox.log` for unexpected `soap:GetInfoRequest` or `soap:GetFolderRequest` bursts, and Zimbra proxy logs for session-cookie-bearing requests from unfamiliar IPs. Force session re-authentication and rotate `zmauth` tokens.
- If your Zimbra fleet is internet-facing for webmail, treat any account that received mail in the last 72 hours as potentially exposed until the patch is verified.

**Sources:** [BleepingComputer — Zimbra urges customers to patch critical web client XSS flaw](https://www.bleepingcomputer.com/news/security/zimbra-urges-customers-to-patch-critical-web-client-xss-flaw/) | [Zimbra Blog — Patch Release Update: Zimbra 10.1.19](https://blog.zimbra.com/2026/07/patch-release-update-zimbra-10-1-19/) | [Zimbra Wiki — Releases/10.1.19](https://wiki.zimbra.com/wiki/Zimbra_Releases/10.1.19)

---

### OpenClaw 2026.6.6 — Three GHSAs (CVSS 8.4–8.8) Chain WhatsApp Message → Host Code Execution: `sanitizeEnvVars()` Denylist Bypass via `NODE_OPTIONS`/`BASH_ENV`/`PYTHONSTARTUP` + Sandbox Bind-Mount Path Traversal
**Product:** OpenClaw self-hosted AI assistant (WhatsApp / Slack / Discord / Telegram / Teams bridges) | **CVE:** None assigned (GHSA IDs only) | **CVSS:** 8.8 / 8.8 / 8.4 | **First reported:** 2026-07-10

Researcher Chinmohan Nayak disclosed three chainable vulnerabilities in OpenClaw ≤ 2026.6.5 that turn an inbound WhatsApp message into code execution on the OpenClaw operator's host: **GHSA-hjr6-g723-hmfm (CVSS 8.8)** — OpenClaw's `sanitizeEnvVars()` denylists credential-like variables but ignores 12 interpreter-startup variables (`NODE_OPTIONS`, `BASH_ENV`, `PYTHONSTARTUP`, and 9 others), letting an attacker inject code that executes before the target script runs; **GHSA-9969-8g9h-rxwm (CVSS 8.8)** — a second variant of the same denylist bypass in a related filter path; **GHSA-575v-8hfq-m3mc (CVSS 8.4)** — path traversal + symlink following in the sandbox bind-mount handler lets an attacker mount parent directories like `/home` or `/var`, escaping the intended workspace jail and reaching SSH keys, AWS credentials, and Docker sockets. Nayak demonstrated the full chain from a single external WhatsApp message; all three are patched in OpenClaw 2026.6.6. This is a more direct attack surface than the "Claw Chain" vulnerabilities Cyera disclosed in May 2026, which required initial foothold.

**Body:** In-scope AI-platform advisory per [Watchtower's AI platform scope]. No confirmed in-the-wild exploitation reported, but the researcher published a working chain; OpenClaw hosts frequently expose bridges to public messaging apps (WhatsApp especially) where sender identity is trivially spoofable, making the WhatsApp → RCE path a realistic remote entry point rather than a lab-only concern. Watchtower's MEMORY.md previously flagged widely deployed OpenClaw fleets as running versions well behind current patched — many likely still on ≤ 2026.3.22 with 15+ open CVEs plus these three new advisories.

**Mitigation:**
- Upgrade OpenClaw to 2026.6.6 or later immediately (`openclaw update`); confirm the version post-upgrade via `openclaw version` on every operator host.
- If you cannot upgrade in the next 24 hours, disable inbound message ingestion from public bridges (WhatsApp, Discord, Telegram) at the OpenClaw config or firewall level; keep only trusted internal channels (Slack workspaces you own, Teams tenants) enabled.
- Hunt: on operator hosts, review shell history and `~/.claude`, `~/.aws`, `~/.ssh` access timestamps for anomalies since 2026-06-01; audit any Docker socket usage from OpenClaw processes; look for unexpected outbound network from `node` / `python` / `bash` processes spawned by OpenClaw.
- Rotate long-lived credentials on any host that ran a pre-2026.6.6 OpenClaw with public-bridge ingestion enabled — AWS access keys, SSH keys, GitHub tokens, `.env` secrets — as though they were exposed.

**Sources:** [The Hacker News — Researcher Details WhatsApp-to-Host Attack Chain Using Three OpenClaw Flaws](https://thehackernews.com/2026/07/researcher-details-whatsapp-to-host.html) | [GitHub Advisory — GHSA-hjr6-g723-hmfm (env-var injection)](https://github.com/openclaw/openclaw/security/advisories) | [CybersecurityNews — WhatsApp Message Turns OpenClaw Into RAT](https://cybersecuritynews.com/whatsapp-message-openclaw-remote-access-tool/)

---

## 🔄 UPDATE

### Squidbleed CVE-2026-47729 — Correction: Fix Was NOT in Squid 7.6, Scheduled For Squid 7.7 (Amos Jeffries clarification 2026-06-15, mainstream Schneier surfacing 2026-07-10); Our 2026-06-13 Coverage Incorrectly Stated 7.6 Patched This CVE
**Product:** Squid caching proxy — FTP gateway parser | **CVE:** CVE-2026-47729 (Squidbleed) | **CVSS:** not scored | **Previous threat score:** 6 → **New threat score:** 6

Correction to Watchtower 2026-06-13 coverage of the Squid 7.6 multi-CVE batch: Squid maintainer Amos Jeffries posted an update to oss-security on 2026-06-15 clarifying that Squid 7.6 did **not** actually ship the CVE-2026-47729 Squidbleed patch — 7.6 shipped only the CVE-2026-50012 cache-digests heap-overflow fix and additional Squidbleed root-cause explanation. The two-character null-terminator fix in `FtpGateway.cc` was merged into the Squid v7 branch in May but did not make the 7.6 cut; it is scheduled for Squid 7.7, which has not yet been released as of 2026-07-10. Debian maintainer Salvatore Bonaccorso raised the version-labelling confusion on the list on 2026-06-22. This changes the defensive posture: operators who upgraded to Squid 7.6 believing they were patched against Squidbleed are still exposed to the FTP-gateway heap over-read cross-session data disclosure, and must either apply the upstream patch commit `865a131c7d557e68c965043d98c2eccae26deef8` manually, disable Squid's FTP gateway support (`ftp_only off` and/or drop the FTP scheme from `acl SSL_ports`), or wait for 7.7.

**Body:** Threat score stays at 6 — the vulnerability characteristics (memory disclosure primitive, cleartext HTTP + TLS-terminating deployments, no code execution) have not changed. What changed is the availability of a shipped fix: our 2026-06-13 report told readers to upgrade to 7.6 to close it, and that is now known to be insufficient.

**Mitigation:**
- If you upgraded Squid to 7.6 based on our 2026-06-13 recommendation for Squidbleed, either (a) apply upstream commit `865a131c7d557e68c965043d98c2eccae26deef8` on top of 7.6, (b) disable FTP gateway (recompile without FTP support or block FTP schemes at the ACL), or (c) plan to move to 7.7 as soon as it releases.
- Multi-tenant proxy fleets (corporate, ISP, education) should treat 7.6 as still-vulnerable and remove FTP support until 7.7 lands.
- Continue tracking the Squid 7.7 release announcement on `squid-users` / `oss-security` — this is where the confirmed shipped fix will appear.

**Sources:** [oss-security — Amos Jeffries correction on 7.6 vs 7.7](https://www.openwall.com/lists/oss-security/2026/06/12/1) | [Debian Security Tracker — CVE-2026-47729](https://security-tracker.debian.org/tracker/CVE-2026-47729) | [Schneier — Squidbleed post (surfacing 2026-07-10)](https://www.schneier.com)

---

## 🟡 MEDIUM

### XQUIC "XRING" HTTP/3 Denial-of-Service — 260-Byte QPACK Traffic Crashes Any Server Embedding XQUIC ≤ 1.9.4 (No Patch, No CVE); Affects Tengine and Alibaba's CDN Fronting Taobao / Alipay
**Product:** Alibaba XQUIC library (QUIC + HTTP/3), including Tengine web server that embeds it | **CVE:** Not assigned | **Published:** 2026-07-08 disclosure by FoxIO

FoxIO researcher Sébastien Féry disclosed XRING on 2026-07-08: a single-line variable-shadowing bug in XQUIC's QPACK dynamic-table handling lets any unauthenticated remote client crash the server process with roughly 260 bytes of completely well-formed QPACK traffic. No login is required, no malformed packets are needed — legal HTTP/3 traffic against default QPACK settings takes the server down. Every release of XQUIC up to and including v1.9.4 (current latest) is affected. XQUIC is embedded in Tengine, Alibaba's Nginx-based web server that per FoxIO fronts Alibaba's cloud and CDN including sites such as Taobao and Alipay, and — because XQUIC is open source — in any third-party HTTP/3 endpoint that adopted it for QUIC/H3 support. There is no fixed release and no CVE as of 2026-07-11.

**Mitigation:** Until a patched XQUIC release ships, set `SETTINGS_QPACK_MAX_TABLE_CAPACITY=0` at HTTP/3 server startup to disable QPACK's dynamic table (removes the vulnerable code path with modest performance cost), or drop HTTP/3 support entirely and serve H1/H2 only. Fronting fleets (CDNs, edge proxies) that embed XQUIC should apply the QPACK-cap-zero mitigation across the entire pool; monitor CPU-idle % and process-restart counters on edge nodes for signs of active exploitation while unpatched. Follow `github.com/alibaba/xquic/issues` for the fixed release.

**Sources:** [The Hacker News — Unpatched XRING Flaw in XQUIC Lets Remote Clients Crash HTTP/3 Servers](https://thehackernews.com/2026/07/unpatched-xring-flaw-in-xquic-lets.html) | [alibaba/xquic issues](https://github.com/alibaba/xquic/issues)

---

## 📋 Noted / Monitoring

**U-Boot 6-flaw batch (BRLY-2026-037 through BRLY-2026-042; BleepingComputer + The Hacker News 2026-07-09→10)** — Binarly disclosed six FIT (Flattened Image Tree) signature-verification flaws in U-Boot; two enable arbitrary code execution before signature verification during boot, four cause crashes. Vulnerable code exists since U-Boot 2013.07 (50+ stable releases); patches accepted upstream but individual hardware vendors must rebuild firmware. Firmware/pre-OS scope is mostly local per Watchtower policy, but BMCs with remote firmware update capability provide a remote component — track vendor firmware advisories for BMC-equipped servers in the fleet.

**Apache IoTDB 8-CVE batch — CVE-2026-28564, CVE-2026-40005, CVE-2026-40006, CVE-2026-40007, CVE-2026-40008, CVE-2026-40009, CVE-2026-40452, CVE-2026-40454 (oss-security 2026-07-10)** — Apache IoTDB REST auth accepting stale cached credentials, path traversal in Pipe file transfer, unauth heap-DoS + unbounded-recursion on AirGap receiver, arbitrary-class instantiation via Pipe RPC, auth escalation via `__internal_aud*` rename, `/rest/v2/fastLastQuery` authz bypass, C++ client OOB reads. IoTDB is an in-scope Apache framework but rarely internet-exposed; internal-platform hygiene priority.

**CVE-2026-56815 pwnlift symlink TOCTOU root file write (Full Disclosure 2026-07-10, CVSS 7.8)** — Symlink following + TOCTOU race in the privileged upload handler yields arbitrary file write as root; niche product but classic LPE-adjacent primitive worth tracking for internal engineering fleets that adopted pwnlift.

**Control Web Panel (CWP) ≤ 0.9.8.1224 SQL injection via `userRes` POST parameter (Full Disclosure 2026-07-09, KIS-2026-12)** — SQLi in hosting-control-panel admin surface; CWP is used by small VPS/hosting providers, moderate internet exposure, watch for CVE assignment and vendor advisory.

**Snipe-IT 9-CVE batch — CVE-2026-54329 (CVSS 7.7), CVE-2026-55460, CVE-2026-55464, CVE-2026-55472, CVE-2026-55474, CVE-2026-55476, CVE-2026-55478, CVE-2026-55516, CVE-2026-55843 (NVD 2026-07-10)** — Mass-assignment `company_id` bypass, javascript URI in markdown, authorization bypasses across accessory/user/location/kit/maintenance endpoints, private-upload-directory path concatenation. Enterprise IT-asset management with limited internet exposure; upgrade-window is not urgent.

**OpenPLC Runtime CVE-2026-14480 (OpenCVE 2026-07-10)** — Authenticated arbitrary file write anywhere writable by the OpenPLC webserver process; can chain to native code execution via malicious C++ file injection. In-scope for OT-adjacent internet-facing deployments; monitor for vendor patch.

**OpenReplay CVE-2026-55879 (OpenCVE 2026-07-10)** — Stored XSS via tracking SDK accepting custom event names and captured page URLs from any visitor holding the public project key; compromises authenticated dashboard sessions. Product-analytics platforms with dashboards accessible to admins are in-scope for AI/observability-adjacent AI advisory tracking.

**Spinnaker CVE-2026-55175 (OpenCVE 2026-07-10)** — Unsafe YAML processing in Kustomize bake operations creating RCE on `rosco` pods; internal CI/CD platform, low internet exposure but critical for cluster-mgmt hygiene.

**Genetec Security Center CVE-2026-55727 (OpenCVE 2026-07-10)** — Authentication mechanism flaws permit unauthenticated access to live video streams; physical-security platform, internet-exposed CCTV/video surveillance nodes should be reviewed.

**Anviz devices CVE-2026-40066 (OpenCVE 2026-07-10)** — Unverified firmware updates enable unauthenticated remote code execution across multiple device models; access-control/time-attendance devices, niche footprint but zero-auth RCE-via-firmware primitive.

**CERT VU#734812 — Xerte Online Toolkit authentication bypass leading to RCE (CERT/CC 2026-07-09; existing 2026-07-10 Noted)** — 30-day dedup, no new development beyond continued coverage.

**CERT VU#849433 — Adalo Database API cross-app user-data extraction via over-fetching and missing authorization controls (CERT/CC 2026-07-08)** — no-code/low-code platform data-exposure primitive; watching for follow-up advisory and vendor fix.

**WordPress WP-SHELLSTORM webshell-injection campaign leveraging Breeze caching plugin + Joomla JCE editor (The Hacker News 2026-07-10)** — Internal logs from operator infrastructure showed 1.4M+ targeted sites; documents ongoing mass-webshell activity against widely deployed CMS plugins. Continuous monitoring / plugin-inventory hardening priority.

**Microsoft Entra "Passkey Phishing" campaign (The Hacker News 2026-07-10)** — Voice-phishing directs users to fake passkey enrollment, hijacking accounts for downstream extortion; identity-defence calibration, awareness training + Entra passkey-enrollment logging review; extends the AI-assisted phishing / device-code / MITM Entra trend documented over the last quarter.

**Google Chrome 150 — 27 vulns patched incl. 13 UAFs, 2 critical (SecurityWeek 2026-07-09)** — Browser-client scope generally out per Watchtower policy, but noted for infrastructure fleets that pin Chrome for headless-Chrome CI or Puppeteer-based scraping — upgrade the pinned image.

**Alibaba PANW PAN-OS batch escalation — no new material beyond 2026-07-10 News coverage of CVE-2026-0288 / CVE-2026-0265 / CVE-2026-0300; 30-day dedup applies.**

**Ubiquiti UniFi 7-CVE batch — no new material beyond 2026-07-10 News coverage (CVE-2026-50746 series); 30-day dedup applies.**

**Injective SDK npm cryptocurrency-wallet stealer (BleepingComputer + The Hacker News 2026-07-10)** — Continuation of 2026-07-10 Noted item: Injective Labs GitHub compromise now traced to @injectivelabs/sdk-ts v1.20.21 fake-telemetry exfiltration; supply-chain calibration, developer-workstation scope.

**Rapid7 blog post on active exploitation of Oracle PeopleSoft CVE-2026-35273 (Rapid7 2026-07-10)** — Analysis wrap-up; no new material beyond existing 2026-06-11/12/14 coverage. Calibration only.

**IRIS C2 offensive-cybersecurity startup (KrebsOnSecurity 2026-07-08)** — Investigative reporting on Burkman/Wohl operating a zero-day acquisition company; ecosystem/threat-actor calibration, no defensive-patching action.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ 403 unreachable |
| Vendor advisories | msrc.microsoft.com/blog, blog.cloudflare.com/tag/security, fortinet.com/blog/threat-research, securitylab.github.com | ⚠️ reachable, no in-window content |
| Research / OSINT | schneier.com, krebsonsecurity.com, rapid7.com, avleonov.com, projectzero.google, github.com/0xMarcio/cve, dbugs.ptsecurity.com | ✅ (Schneier surfaced Squidbleed; Rapid7 PeopleSoft wrap-up; 0xMarcio/dbugs — new CVE feeds; others no in-window content) |
| Advisories / DBs | opencve.io, nvd.nist.gov, cve.mitre.org, cve.org, kb.cert.org/vuls, packetstormsecurity.com | ✅ opencve/nvd/kb.cert productive; ⚠️ cve.mitre/cve.org/packetstormsecurity landing pages returned no listed content |
| Full Disclosure / oss-security | seclists.org/fulldisclosure, openwall.com/lists/oss-security (out-of-list but per MEMORY) | ✅ |
| GitHub PoC | github.com/search?q=CVE, github.com/0xMarcio/cve | ✅ |
| Community intel | habr.com/ru/companies/tomhunter/articles, teletype.in/@cyberok, cert.gov.ua, attackerkb.com, bugcrowd.com/disclosures, hackerone.com/hacktivity | ⚠️/❌ (habr/teletype no in-window content; cert.gov.ua/attackerkb/bugcrowd/hackerone unreachable) |

**Errors:**
- `cisa.gov` — HTTP 403 (unreachable)
- `cisa.gov/known-exploited-vulnerabilities-catalog` — HTTP 403 (unreachable)
- `attackerkb.com` — HTTP 403 (unreachable)
- `bugcrowd.com/disclosures` — HTTP 404 (unreachable)
- `hackerone.com/hacktivity` — JS-only page, no server-rendered content (unreachable)
- `cert.gov.ua` — no content returned (unreachable)

**CISA KEV:** unreachable this cycle (403); no direct enumeration of new KEV additions. Existing 2026-07-08 KEV additions (Adobe ColdFusion CVE-2026-48282, Langflow, Joomla iCagenda CVE-2026-56290) remain in the 30-day dedup window and were covered in earlier reports.

---

*Watchtower vulnerability-researcher | Cycle: 2026-07-11/night | Next: 2026-07-12/night*
