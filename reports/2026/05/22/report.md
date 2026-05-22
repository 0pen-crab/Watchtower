# Watchtower Night Report — 2026-05-22
**Cycle:** Night | **Generated:** 2026-05-22 03:30 UTC (2026-05-22T03:30:00Z)
**Sources checked:** 20/30 (10 unreachable per persistent MEMORY notes; 1 degraded) | **CISA KEV total:** ~1,400+ | **New KEV additions:** 7 (2026-05-20: CVE-2026-41091, CVE-2026-45498, plus 5 legacy 2008-2010 Microsoft/Adobe items)

---

## 🔴 CRITICAL

### CVE-2026-20223 — Cisco Secure Workload Unauthenticated Cross-Tenant Site-Admin RCE (CVSS 10.0)
**Product:** Cisco Secure Workload (Cluster Software — SaaS + on-prem) | **CVE:** CVE-2026-20223 | **Status:** Patched (no confirmed ITW; vendor-discovered)

Cisco disclosed a CVSS 10.0 perfect-score vulnerability in Cisco Secure Workload's internal REST APIs on 2026-05-21. Weak validation and authentication checks let any remote unauthenticated attacker cross isolated tenant boundaries, read sensitive information, and make configuration changes with Site Admin user privileges across every tenant on a cluster. The flaw was found during internal security testing; Cisco has no public exploitation evidence yet, but the bug profile (network attack, no auth, no user interaction, full admin authority over a multi-tenant Zero-Trust / micro-segmentation product) makes ITW within 7-14 days the default planning assumption.

**Timeline:** 2026-05-21 vendor advisory + fixed releases (3.10.8.3 and 4.0.3.17). SaaS deployments patched at the cloud-infrastructure level (no customer action). No public exploit at disclosure.

**Why it matters:** Cisco Secure Workload is the canonical "agent on every workload to enforce micro-segmentation policy" product across enterprise data centers and large cloud estates — the same trust position as an EDR but with network-policy authority. A Site Admin compromise yields the ability to silently mutate firewall enforcement policies across every workload in every tenant. Pair with the 2026-Q2 Cisco-perimeter-CVE pattern (SD-WAN CVE-2026-20127, CVE-2026-20182, CVE-2026-20182 — six exploited zero-days in 2026 per Talos / UAT-8616 attribution) and Cisco-management-plane CVEs are now a sustained KEV tempo. Treat as patch-now even though SaaS is mitigated server-side; on-prem clusters are exposed until the upgrade lands.

**Discovered by:** Cisco internal security testing

**Mitigation:**
- On-prem Cisco Secure Workload Cluster Software: upgrade to 3.10.8.3 or 4.0.3.17 immediately. No workaround documented.
- SaaS customers: no action required (Cisco patched the cloud infrastructure).
- Audit Secure Workload audit logs for unexpected `siteAdmin`-scope API calls from internal API endpoints over the past 30 days; hunt for tenant-boundary-crossing read/configure operations.
- Restrict management-plane network reachability — even if patched, defense-in-depth for any product with this attack profile.
- Pre-position IR playbook for "Secure Workload compromised" → assume policy state mutated and any agent could be downgraded; cross-check current policy against last known-good backup.

**Sources:** [The Register](https://www.theregister.com/security/2026/05/21/cisco-serves-up-yet-another-perfect-10-bug-with-secure-workload-admin-flaw/) | [BleepingComputer](https://www.bleepingcomputer.com/news/security/cisco-max-severity-secure-workload-flaw-gives-hackers-site-admin-privileges/) | [SecurityAffairs](https://securityaffairs.com/192473/security/cisco-fixed-maximum-severity-flaw-cve-2026-20223-in-secure-workload.html) | [SecurityOnline](https://securityonline.info/cisco-secure-workload-api-vulnerability-cve-2026-20223-cvess-10/)

---

### Microsoft Defender Zero-Days — CVE-2026-41091 (LPE) + CVE-2026-45498 (DoS) Actively Exploited + KEV-Added 2026-05-20
**Product:** Microsoft Defender (Malware Protection Engine + AV Platform — every Windows endpoint) | **CVE:** CVE-2026-41091, CVE-2026-45498 | **Status:** KEV (Federal deadline 2026-06-03 / 2026-06-10 per source); Actively Exploited; Patched

Two Microsoft Defender vulnerabilities disclosed 2026-05-19 are being exploited in the wild and were added to CISA's KEV catalog on 2026-05-20. CVE-2026-41091 (CVSS 7.8 LPE — codenamed "UnDefend") is an improper link-following flaw in the Malware Protection Engine that yields SYSTEM-privilege code execution from a local user; researchers note the attack chain is the standard "AV-writes-from-SYSTEM, link-resolve-to-attacker-controlled-path" pattern. CVE-2026-45498 (CVSS 4.0 — codenamed "RedSun") forces Defender into a denial-of-service state, effectively blinding endpoint EDR while the rest of an intrusion runs. Both are confirmed exploited together — RedSun disables Defender, UnDefend escalates to SYSTEM — making this a paired post-exploitation primitive on any Windows host where the attacker has user-level code execution.

**Timeline:** 2026-05-19 MSRC advisories shipped (Malware Protection Engine 1.1.26040.8+ / AV Platform 4.18.26040.7+ ship the fix). 2026-05-20 CISA KEV addition with Federal deadline 2026-06-03. 2026-05-21 confirmed paired-exploitation framing in vendor + media reporting.

**Why it matters:** Defender is the universal Windows EDR — every domain-joined endpoint, server, and managed device. The DoS+LPE pair is the canonical "blind the EDR then escalate" intrusion sequence and is the single most reusable post-exploit Defender chain since the 2021 NotPetya-class wave. Combined with the Fox Tempest MSaaS takedown (MEMORY 2026-05-19) and the 4 newly-named ransomware affiliates (yesterday's update), assume sophisticated ransomware crews now ship this pair as standard tradecraft. Patch ahead of the Federal deadline; treat any incident response on Windows from May 19 onward as plausibly involving Defender being silenced before the attacker pivot.

**Discovered by:** Microsoft Security Response Center (exploitation reports attributed to multiple unnamed external sources)

**Mitigation:**
- Confirm Malware Protection Engine ≥ 1.1.26040.8 across the fleet. Defender Engine auto-updates by default — verify it's still happening, the rate of stale clients in any large fleet is non-trivial.
- Confirm AV Platform version ≥ 4.18.26040.7.
- Hunt for Defender service shutdown / DoS events (event IDs 5008, 5010, 1015) in the May 19 → present window — these may now be intentional pre-LPE blind-the-EDR steps rather than benign noise.
- Configure tamper-protection and prevent Defender service shutdown via Group Policy / Intune; even a DoS that crashes the engine should re-spawn cleanly with telemetry intact.
- For sensitive environments: combine Defender with a secondary EDR / network-side telemetry so a Defender DoS does not yield full visibility loss.

**Sources:** [Help Net Security](https://www.helpnetsecurity.com/2026/05/21/microsoft-defender-vulnerabilities-cve-2026-41091-cve-2026-45498/) | [BleepingComputer](https://www.bleepingcomputer.com/news/security/microsoft-warns-of-new-defender-zero-days-exploited-in-attacks/) | [The Hacker News](https://thehackernews.com/2026/05/microsoft-warns-of-two-actively.html) | [Cybernewscentre KEV summary](https://www.cybernewscentre.com/21st-may-2026-cisa-kev-old-bugs-microsoft-defender/)

---

## 🟠 HIGH

### 🔄 UPDATE — CVE-2026-46333 ssh-keysign-pwn Promoted: Multi-Distro Patches Shipped, Two Public Exploits, Reframed as "Fourth Linux Kernel CVE in Three Weeks"
**Product:** Linux kernel — `__ptrace_may_access()` (every distro built since November 2016) | **CVE:** CVE-2026-46333 | **CVSS:** ~5.5 (NVD) — info disclosure | **First reported:** 2026-05-15 (Noted 2026-05-16)

Originally Noted on 2026-05-16 as "Qualys logic bug, public PoC `_SiCk/ssh-keysign-pwn`, no CVE assigned — track for promotion if KEV-added or chained." Promotion criteria are now met: (1) CVE-2026-46333 assigned, (2) upstream fix landed in Linus's tree on 2026-05-14 (commit 31e62c2ebbfd), (3) AlmaLinux, Ubuntu, Red Hat, CloudLinux, Debian, Fedora have all published mitigation advisories, (4) two distinct public exploits demonstrated (ssh-keysign reads `/etc/ssh/ssh_host_*_key`; chage reads `/etc/shadow`), and (5) industry framing has shifted from "noted research" to "the fourth Linux kernel vulnerability in three weeks" (alongside Copy Fail CVE-2026-31431, Dirty Frag CVE-2026-43284/43500, and Fragnesia CVE-2026-46300). The bug is a 9-year-old race window in `__ptrace_may_access()`: during a SUID helper's `do_exit()`, the kernel runs `exit_mm()` (drops `mm`) before `exit_files()`, leaving a window where the dumpable check is skipped while file descriptors remain open — an unprivileged local attacker steals the SUID helper's FDs and reads files only the SUID helper can read.

**Previous threat_score:** 4 (noted 2026-05-16). **New score:** 6 — info disclosure with public-PoC SSH-key + `/etc/shadow` read, multi-distro patch availability, no public container-escape demo yet (cf. the page-cache-write LPE → K8s escape pattern). Not in KEV (yet).

**Why it matters:** Local-only and info-disclosure-only at this stage, so it does not meet our normal pre-auth-RCE scope on its own. But the SSH-host-key read primitive is a strong lateral-movement enabler in any multi-tenant Linux host (CI runners, jump boxes, multi-user dev workstations) — steal host keys, MITM future SSH connections to that host. Treat patch SLA as ≤14 days on every multi-tenant Linux estate and ≤30 days everywhere else.

**Mitigation:**
- Apply distro kernel updates: AlmaLinux 2026-05-15, Ubuntu, Red Hat, Debian, Fedora, CloudLinux all shipped.
- Interim mitigation (Qualys confirmed): set `kernel.yama.ptrace_scope = 2` or `3` via `/etc/sysctl.d/` — blocks every public exploit (`2` = admin-only attach, `3` = no attach).
- Rotate SSH host keys on any pre-patch multi-tenant Linux host where local unprivileged users had access between disclosure (2026-05-15) and patch deployment.
- Track for KEV addition — if added, expect the trajectory to mirror Copy Fail (LPE-only → KEV → K8s container-escape PoC within 14 days).

**Sources:** [The Hacker News](https://thehackernews.com/2026/05/9-year-old-linux-kernel-flaw-enables.html) | [AlmaLinux blog](https://almalinux.org/blog/2026-05-15-ssh-keysign-pwn-cve-2026-46333/) | [Ubuntu Security](https://ubuntu.com/blog/ssh-keysign-pwn-linux-vulnerability-fixes-available) | [Red Hat](https://access.redhat.com/security/cve/cve-2026-46333) | [Gotekky](https://www.gotekky.com/guides/security/cve-2026-46333-ssh-keysign-pwn-linux-kernel/)

---

### CVE-2026-45695 — Kopia Backup Daemon SSH ProxyCommand Pre-Auth RCE (CVSS 9.8)
**Product:** Kopia (Go-based backup software with HTTP server) | **CVE:** CVE-2026-45695 | **CVSS:** 9.8 | **First reported:** 2026-05-21

A pre-authentication remote code execution vulnerability in Kopia versions ≤ 0.22.3 chains two flaws: (a) when the Kopia HTTP server is started with `--without-password`, it accepts unauthenticated requests to `/api/v1/repo/exists`, and (b) for SFTP backends configured with `externalSSH: true`, attacker-supplied SSH arguments are split on spaces and passed directly to `exec.CommandContext`. Passing `-oProxyCommand=<cmd>` causes OpenSSH to execute the embedded command via the user's shell before any SSH connection attempt. A single unauthenticated HTTP request yields arbitrary command execution as the Kopia process user. Fixed in 0.23.0.

**Why it matters:** Kopia is a moderately deployed self-hosted backup product (Go binary, popular in home labs and small/mid orgs, and used by some Kubernetes operators for cluster backup). The `--without-password` listener mode is widely used in lab and internal deployments under the assumption "I'm on a trusted network" — exactly the configuration where this CVE yields trivial RCE. The Kopia process typically runs as the user owning the backup repository — that user often has read access to every file the backup covers, making this a fast path from "any LAN reachability" to full data exfiltration. Add to the running pattern of pre-auth RCEs on self-hosted Go-based infrastructure (cf. nginx-ui, Open WebUI, n8n, OpenClaw, FastGPT — all default-no-auth or trivial-auth-bypass classes in 2026).

**Mitigation:**
- Upgrade Kopia to 0.23.0+. Version 0.23.0 also prevents `--without-password` servers from listening on non-loopback interfaces, hardening the default config.
- For pre-patch deployments: bind the Kopia HTTP server to `localhost` only; require authentication; disable any `externalSSH: true` SFTP backends until upgrade.
- Hunt for unexpected outbound connections from the Kopia process user — any process spawn from `kopia` should be benign (rclone, ssh, etc.) but ProxyCommand exploitation will spawn arbitrary shells.

**Mitigation:**
- Upgrade to Kopia 0.23.0+.
- Restrict Kopia server network access to localhost / management VLAN.
- Audit `externalSSH: true` configs.

**Sources:** [GitHub Advisory GHSA-2q4c-3mrw-63c3](https://github.com/advisories/GHSA-2q4c-3mrw-63c3) | [oss-security 2026-05-19 archive](https://www.openwall.com/lists/oss-security/2026/05/)

---

### Showboat Linux Malware — China-Aligned Calypso (Bronze Medley / Red Lamassu) Middle East Telecom Implant (Persistent Since 2022)
**Product:** Compromised Linux servers at Middle East / Asia-Pacific telecommunications providers and ISPs | **CVE:** None — threat-intel disclosure | **First reported:** 2026-05-21 (The Hacker News)

A new modular Linux post-exploitation framework dubbed "Showboat" has been disclosed targeting a Middle Eastern telecommunications provider since at least mid-2022. The framework supports remote shell, file transfer, and SOCKS5 proxy backdoor capability. Attribution: at least one (and possibly more) China-affiliated threat clusters, with C2 infrastructure correlating to Chengdu IP addresses. The named cluster is **Calypso (Bronze Medley / Red Lamassu)**, active since September 2016 against government and telecom in Brazil, India, Kazakhstan, Russia, Thailand, and Turkey. Additional confirmed victims surfaced via infrastructure analysis: an Afghanistan ISP and an unknown Azerbaijan target.

**Why it matters:** Telecom-sector long-dwell Linux implants are part of the same broader 2026 pattern as the recent Webworm EchoCreep / GraphWorm cluster (Russia + Central Asia, noted yesterday) and FamousSparrow / SHADOW-EARTH-053 (China + on-prem Exchange initial access, MEMORY 2026-05-14 / 2026-05-02). For US-based enterprises this is primarily a defensive-intelligence data point: (a) it widens the China-aligned Linux-implant inventory for SOCs running cross-referencing detections, (b) confirms that SOCKS5-proxy + remote-shell + file-transfer modules are now the standard Linux-implant feature triple, and (c) supports the working hypothesis that core-router / telecom-infrastructure long-dwell campaigns at Tier-2 and Tier-3 carriers create lawful-intercept / signalling-plane risk for any organization relying on those carriers for transit or interconnect. Hunt for Showboat-class TTPs on internet-facing Linux infrastructure with telecom adjacency.

**Mitigation:**
- Pull Showboat IOCs / YARA rules from THN / BleepingComputer / vendor TI feeds as they publish; deploy to Linux EDR.
- Hunt for SOCKS5 proxy listener processes on Linux infrastructure that should not be running one (unexpected `socks5` / random-high-port binds from non-VPN service users).
- Hunt for C2 to Chengdu-IP-range (and the broader Calypso infrastructure documented in this disclosure).
- If you transit traffic through Middle East / Asia-Pacific telecom infrastructure, consider end-to-end encryption posture review (e.g., MASQUE / WireGuard / mTLS overlay rather than pure IPSec to a carrier-managed VPN concentrator).

**Sources:** [The Hacker News](https://thehackernews.com/2026/05/showboat-linux-malware-hits-middle-east.html) | [BleepingComputer (Chinese hackers target telcos)](https://www.bleepingcomputer.com/news/security/chinese-hackers-target-telcos-with-new-linux-windows-malware/)

---

## 📋 Noted / Monitoring

**CVE-2026-47102 + CVE-2026-47101 LiteLLM (PT-2026-42538/42539, CVSS 8.8 each)** — Authenticated user-role modification + API-key privilege escalation that yield proxy_admin access on LiteLLM proxy. Builds on the recent CVE-2026-42208 KEV-listed LiteLLM exploitation (MEMORY 2026-05-12) — LiteLLM is now a sustained AI-platform CVE cluster; treat any LiteLLM deployment as deprecation-or-segment candidate.

**CVE-2026-46703 + CVE-2026-46695 @boxlite-ai/boxlite (Go, both critical)** — Path traversal → arbitrary file write on host plus a permission bypass for read-only files. AI-infra Go package, low estimated deployment count but worth tracking as part of the broader AI-platform vuln pipeline.

**CVE-2026-46614 Fission router missing-authentication on function endpoints (Go, Critical)** — Fission FaaS router exposes function invocation on the public listener without HTTPTrigger protection; unauth function-execution primitive on any internet-exposed Fission cluster.

**CVE-2026-45697 Craft CMS Formie plugin Twig template injection (Critical)** — Pre-auth template injection via hidden form field on Craft CMS sites using the Formie form-builder plugin; companion CVE class to today's Twig fix wave.

**CVE-2026-46633 Twig `{% use %}` PHP code injection (Composer, Critical)** — Companion vulnerability to yesterday's CVE-2026-24425 Twig sandbox bypass, shipped in the same Twig 3.26.0 fix. Single-quote in template name escapes the cache-file string literal and yields PHP code execution. Affects sandboxed Twig usage. Treat as part of the same "upgrade Twig to 3.26.0+" remediation as yesterday's advisory.

**CVE-2026-46395 @haxtheweb/haxcms-nodejs private-key disclosure (Critical)** — Broken HMAC handling exposes private signing key; affects HAXcms node.js CMS deployments. Low estimated footprint.

**CVE-2026-45625 arcane backend missing-authorization Git credentials disclosure (Critical)** — Self-hosted Git management tool exposes credentials due to missing authorization — Niche tool, noted for completeness.

**CVE-2026-47243 Kata Containers `runtime-rs` virtiofsd Symlink Escape** — Container-escape primitive in Kata Containers (used by some K8s shops for stronger isolation than runc); not a default K8s configuration but worth flagging given Linux-kernel page-cache escapes already trending (MEMORY 2026-05-16).

**CVE-2026-47323 Apache Camel Message Header Injection** — Header-injection class in widely-used Java integration framework; full impact and CVSS pending vendor advisory expansion.

**CVE-2026-48207 Apache Fory PyFory ReduceSerializer Policy Enforcement** — Python deserialization policy-enforcement gap in Fory serialization library; same class as prior Python-pickle ecosystem CVEs.

**CVE-2026-45760 Apache Camel K Cross-Namespace Build Deputy Attack** — Cross-namespace confused-deputy in Camel K builds; relevant for K8s shops running Camel K integrations.

**CVE-2026-45250 FreeBSD `setcred` Stack Overflow ("FatGid")** — FreeBSD-specific LPE; out of normal Linux scope but logged for any BSD-based appliance fleets.

**CVE-2026-6960 BookingPress Appointment Booking Pro (PT-2026-42552, CVSS 9.8)** — Critical WordPress plugin advisory from PT-Security dbugs ahead of Wordfence. WP-plugin auth-bypass CVE class — track for skimmer-monetisation pattern (cf. Burst Statistics / Funnel Builder, MEMORY 2026-05-12).

**CVE-2026-8134 Concrete CMS (PT-2026-42535, CVSS 9.4)** — Critical Concrete CMS issue from PT-Security dbugs; part of a broader Concrete CMS multi-CVE batch (authorization bypasses, CSRF, XSS) disclosed via OpenCVE 2026-05-21.

**CVE-2026-22678 Webmin (PT-2026-42550, CVSS 5.4)** — Lower-severity Webmin advisory; noted because Webmin is internet-exposed on many SOHO Linux servers.

**DFIR-IRIS multi-CVE batch (CVE-2026-42329 / 42538-40 / 42543 / 42547)** — Open Redirect + Insecure File Upload + Excessive Data Exposure + Mass Assignment + CSRF + False Alert Attribution in the DFIR-IRIS incident-response platform. Niche but noted; affects DFIR teams running self-hosted IRIS.

**Apache Camel-K + Camel + Airflow + OFBiz Apache-ecosystem CVE wave (oss-security 2026-05-19/20/21)** — The OFBiz 17-CVE batch (MEMORY 2026-05-20, yesterday's coverage) extends to broader Apache wave: Camel (CVE-2026-47323), Camel K (CVE-2026-45760), Airflow (CVE-2026-27173 JWT exposure, CVE-2026-42526 AWS Secrets Manager ACL), Fory (CVE-2026-48207). Aggregate signal: Apache project security batch tempo is sustained through May.

**Google accidentally exposed unfixed Chromium Service-Worker JavaScript-runs-after-close flaw** — Service Worker persists JS execution even after the browser is closed; affects all Chromium-based browsers (Chrome, Edge, Brave, Opera, Vivaldi, Arc). Researcher Lyra Rebane published originally restricted issue details after 14+ week public-bug-tracker exposure window. No CVE yet. Browser/client-only — out of normal Watchtower scope, but logged because the "compromised browser as DDoS botnet / proxy relay" framing has corporate-laptop fleet implications.

**QEMU CXL Memory Corruption ("QEMUtiny", oss-security 2026-05-20)** — QEMU CXL-emulation memory corruption disclosed; affects environments using QEMU with CXL-memory emulation in CI/test pipelines. CVE pending.

**Memcached 1.6.42 "major security focused release" (CVE TBD)** — Pre-announced via oss-security 2026-05-19; CVEs not yet published. Memcached is widely deployed as a backend cache; watch for the CVE drop and patch tempo over the next 7-14 days.

**PowerDNS Security Advisory 2026-06 (oss-security 2026-05-20)** — Multiple issues in PowerDNS; details pending vendor advisory expansion. Companion to the broader DNS-stack May patch wave (BIND, Unbound, PowerDNS — all in flight in 2026-05-20 window, BIND/Unbound already covered yesterday).

**Samba upcoming security releases (heads-up for 2026-05-26)** — Pre-announced Samba release window scheduled for 2026-05-26; pre-position patch teams for AD-related Samba advisory next week.

**EvilTokens / Anthropic Claude Code SOCKS5 / Microsoft RAMPART + Clarity AI-agent security tooling** — Already covered yesterday (2026-05-21 report); no material changes today.

**Kimwolf IoT botnet operator arrested (Canada, 23yo, ~30 Tbps attacks)** — Law-enforcement event, useful for IR posture (one less botmaster) but not a vulnerability advisory.

**CISA contractor GovCloud key leak (Krebs)** — Already covered (MEMORY 2026-05-19). No new material.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com, schneier.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (403 via WebFetch — KEV covered via THN / cybernewscentre relay) |
| Vendor advisories | fortiguard.com/psirt, msrc.microsoft.com/blog, securitylab.github.com, blog.cloudflare.com/tag/security | ✅ / ⚠️ (MSRC sparse) |
| Research / OSINT | rapid7.com, schneier.com, avleonov.com, kb.cert.org/vuls, dbugs.ptsecurity.com, github.com/advisories | ✅ |
| Supply chain | github.com/0xMarcio/cve, github.com/advisories, seclists.org/fulldisclosure | ✅ |
| Threat intel | thehackernews.com, bleepingcomputer.com, fortiguard.com, schneier.com | ✅ |
| Mailing lists | seclists.org/fulldisclosure, openwall.com/lists/oss-security/2026/05/ | ✅ |
| CVE/NVD aggregators | app.opencve.io | ✅ |
| Russian InfoSec | habr.com/ru/companies/tomhunter, teletype.in/@cyberok | ⚠️ (no fresh May content surfaced) |
| Ukrainian CERT | cert.gov.ua | ❌ (WebFetch returned empty content; likely JS-rendered) |
| Aggregator | packetstorm.news | ⚠️ (homepage WebFetch returns navigation only — degraded) |

**Errors:** cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog, attackerkb.com, nvd.nist.gov, cve.mitre.org, cve.org, msrc.microsoft.com/blog, hackerone.com/hacktivity, bugcrowd.com/disclosures, cert.gov.ua — all return 403 / empty / JS-required via WebFetch (per MEMORY). packetstormsecurity.com → redirected to packetstorm.news, degraded.

**CISA KEV:** 2026-05-20 batch added 7 CVEs — CVE-2026-41091 + CVE-2026-45498 (Microsoft Defender, this report's CRITICAL #2) + 5 legacy 2008-2010 Microsoft/Adobe (CVE-2008-4250, CVE-2009-1537, CVE-2009-3459, CVE-2010-0249, CVE-2010-0806). Federal deadline 2026-06-10. Legacy items reflect lingering exploitation against still-deployed Windows XP / Server 2003 era systems — defensive aperture for unmanaged-legacy-asset triage.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-22/night | Next: 2026-05-23/night*
