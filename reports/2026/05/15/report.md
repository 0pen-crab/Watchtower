# Watchtower Night Report — 2026-05-15
**Cycle:** Night | **Generated:** 2026-05-15 00:30 UTC
**Sources checked:** 19/30 | **CISA KEV total:** unchanged (gateway 403) | **New KEV additions:** CVE-2026-20182 Cisco SD-WAN (added 2026-05-14, federal due 2026-05-17 per BleepingComputer/SecurityAffairs relay)

---

## 🔴 CRITICAL

### Cisco Catalyst SD-WAN Controller CVE-2026-20182 — CVSS 10.0 Authentication-Bypass Zero-Day Actively Exploited In The Wild; CISA KEV With 3-Day Federal Deadline
**Product:** Cisco Catalyst SD-WAN Controller and Cisco Catalyst SD-WAN Manager (on-prem + SD-WAN Cloud) | **CVE:** CVE-2026-20182 | **Status:** 0-Day (Active Exploitation / KEV)

An unauthenticated attacker reaching the SD-WAN management plane can bypass peering authentication via crafted requests and log in as an internal high-privileged non-root user — the same user identity used by vManage→Controller fabric peering. From that foothold the attacker can inject rogue peers into the SD-WAN fabric and manipulate network configuration across every managed edge router; Cisco has confirmed in-the-wild zero-day exploitation prior to the public 2026-05-14 advisory. Rapid7 surfaced the bug while researching CVE-2026-20127 (the SD-WAN bug actively exploited since 2023 covered earlier in our digest), suggesting a clustered exploitation effort against the SD-WAN attack surface.

**Timeline:** Active exploitation observed (Cisco) → patch shipped → public advisory 2026-05-14 → CISA KEV add 2026-05-14 with federal remediation deadline 2026-05-17 (3-day window).

**Why it matters:** This is the second CVSS-10-class actively-exploited zero-day on Cisco SD-WAN infrastructure in 2026 (after CVE-2026-20127 in March). SD-WAN controllers sit at the perimeter of every site they manage and authorise the routing policy for every branch — a compromised Catalyst SD-WAN Controller is functionally equivalent to a compromised core router across the entire WAN. The 3-day federal deadline mirrors the PAN-OS CVE-2026-0300 / Ivanti EPMM CVE-2026-6973 cadence, signalling that CISA assesses the exploitation tempo as imminent. Treat any internet-facing Catalyst SD-WAN management plane (vManage / Controller) as compromised until proven otherwise.

**Discovered by:** Rapid7 research team (during follow-up research on the related CVE-2026-20127).

**Mitigation:**
- Patch Cisco Catalyst SD-WAN Controller / Manager to the fixed release immediately — no workaround exists.
- Audit Controller authentication logs for unauthorised `Accepted publickey for vmanage-admin` entries (specific IoC called out in Cisco/Rapid7 reporting).
- Remove any internet exposure of the SD-WAN management plane; restrict to dedicated management VPN with MFA.
- Hunt for unexpected SD-WAN policy changes, rogue peer additions, and unexplained configuration template pushes since 2026-04-15.
- For SD-WAN Cloud deployments: assume rotated credentials and review Cisco's managed-service incident response.

**Sources:** [BleepingComputer — Cisco warns of new critical SD-WAN flaw exploited in zero-day attacks](https://www.bleepingcomputer.com/news/security/cisco-warns-of-new-critical-sd-wan-flaw-exploited-in-zero-day-attacks/) | [TheHackerNews — Cisco Catalyst SD-WAN Controller Authentication Bypass](https://thehackernews.com) | [SecurityAffairs — CISA KEV addition](https://securityaffairs.com)

---

## 🟠 HIGH

### F5 NGINX 'NGINX Rift' CVE-2026-42945 — 18-Year-Old Heap Buffer Overflow Becomes CVSS 9.2 Pre-Auth RCE With ASLR Disabled; Full F5 Quarterly Advisory Lands With 50+ CVEs *(Update on 2026-05-14 coverage)*
**Product:** F5 NGINX Open Source 0.6.27–1.30.0; NGINX Plus R32–R36; NGINX-derivative ecosystem (OpenResty, Tengine, Angie, Kong, NGINX Ingress Controller) | **CVE:** CVE-2026-42945 (+ companion CVE-2026-41225, CVE-2026-41957, CVE-2026-34176, CVE-2026-39459) | **CVSS:** 9.2 | **First reported:** 2026-05-13 → escalated 2026-05-14

Yesterday's report carried CVE-2026-42945 at threat_score 6 based on the limited oss-security disclosure (CVSS 8.1, vague "ngx_http_rewrite_module vulnerability"). F5's full quarterly advisory dropped 2026-05-14 with substantially more detail: the bug is a **heap buffer overflow** triggered when an NGINX configuration combines `rewrite` and `set` directives, because the internal `is_args` flag persists across NGINX's two-pass script engine after rewrites containing `?`, producing a mismatch between calculated buffer size and actual bytes written. An unauthenticated attacker sending a crafted HTTP request triggers DoS, and with ASLR disabled (or specific gadget chains) the bug yields **remote code execution as the NGINX worker user**. CVSS escalates to 9.2. The bug is named 'NGINX Rift' and has been latent in the rewrite-module code for **18 years**, discovered April 2026 by DepthFirst AI autonomous code scanning — yet another AI-bug-finder data point joining the MDASH/Daybreak/Glasswing/Sandyaa cluster documented in MEMORY.

The advisory ships alongside companion BIG-IP / iControl REST issues (CVE-2026-41225 CVSS 8.6 Manager-permission iControl REST → command execution; three additional Auth-RCEs in BIG-IP; 12 BIG-IP DoS issues in the Traffic Management Microkernel).

**Mitigation:**
- Upgrade NGINX Open Source to 1.31.0 or 1.30.1.
- Upgrade NGINX Plus to R36 P4 or R32 P6.
- Coordinate with downstream ecosystem maintainers: OpenResty, Tengine, Angie, Kong, NGINX Ingress Controller, NGINX App Protect — vendor patches will follow over the next 7-14 days; track release notes.
- Interim mitigation per F5: replace **unnamed PCRE capture groups** in vulnerable rewrite rules with **named captures** to avoid the bug-triggering code path.
- Confirm ASLR is enabled on every NGINX host (most modern Linux defaults do this, but BSD/container distros may not).
- BIG-IP customers: roll the same quarterly patch set to address the companion iControl REST + BIG-IP issues.

**Sources:** [SecurityWeek — F5 Patches Over 50 Vulnerabilities](https://www.securityweek.com/f5-patches-over-50-vulnerabilities/) | [BleepingComputer — 18-year-old NGINX vulnerability allows DoS, potential RCE](https://www.bleepingcomputer.com/news/security/) | [SecurityAffairs — NGINX Rift Buffer Overflow](https://securityaffairs.com)

---

### Burst Statistics WordPress Plugin CVE-2026-8181 (CVSS 9.8) — Authentication Bypass Actively Exploited Against 115K+ Vulnerable Sites; Wordfence Blocked 7,400 Attacks In 24 Hours
**Product:** Burst Statistics WordPress plugin 3.4.0 and 3.4.1 (~200,000 active installs; ~115,000 sites unpatched) | **CVE:** CVE-2026-8181 | **CVSS:** 9.8 | **First reported:** 2026-05-12 (patch) → exploitation reported 2026-05-14

Burst Statistics misinterprets the return value of WordPress's `wp_authenticate_application_password()` function — `WP_Error` and `null` results are mistakenly treated as successful authentication, allowing the plugin to call `wp_set_current_user()` with any attacker-supplied username. Combined with the plugin's REST API endpoints, an unauthenticated attacker can impersonate any administrator and create rogue admin accounts on the target site. Wordfence reports blocking 7,400+ exploitation attempts in a 24-hour window. The plugin is active on ~200k WordPress sites; download statistics show ~85k installs of the patched 3.4.2 release since 2026-05-12, leaving ~115k unpatched and being actively scanned.

**Timeline:** 3.4.2 patch released 2026-05-12 → 7,400 exploitation attempts observed 2026-05-13/14 → public coverage 2026-05-14.

**Why it matters:** The WordPress plugin ecosystem produces a steady cadence of CVSS-9+ authentication bypasses (LiteSpeed Cache CVE-2024-44000, MalCare CVE-2024-44000, etc.); this one fits the pattern but with active exploitation at scale within 48 hours of patch — the standard auth-bypass→ransomware tempo previously documented in MEMORY for cPanel CVE-2026-41940.

**Mitigation:**
- Update Burst Statistics to 3.4.2 (or later) immediately.
- For unpatched sites, deactivate the plugin until patch can be deployed.
- Audit WordPress admin user list for unauthorised additions since 2026-05-12.
- Wordfence customers: ensure the WAF rule for CVE-2026-8181 is active (shipped 2026-05-12).
- Review WordPress audit logs for unexpected `wp_set_current_user()` events or REST API calls to Burst Statistics endpoints.

**Sources:** [BleepingComputer — Hackers exploit auth bypass flaw in Burst Statistics WordPress plugin](https://www.bleepingcomputer.com/news/security/) | [dbugs.ptsecurity.com — CVE-2026-8181](https://dbugs.ptsecurity.com)

---

### Mini Shai-Hulud Wave 2 Update — OpenAI Confirms 2-Employee-Device Breach + Code-Signing Cert Rotation; Mistral AI Source-Code For Sale; $1,000 BreachForums Supply-Chain Contest Announced *(Update on 2026-05-13 coverage)*
**Product:** Mini Shai-Hulud Wave 2 affected ecosystem (npm + PyPI + downstream: OpenAI internal repos, Mistral AI corpus) | **CVE:** CVE-2026-45321 (Wave 2 worm) | **CVSS:** —

Three material developments on yesterday's Mini Shai-Hulud Wave 2 entry:

1. **OpenAI confirmed breach** (2026-05-14): OpenAI disclosed that two employee devices were compromised during the Wave 2 wave, with "credential-focused exfiltration activity in a limited subset of internal source code repositories." Code-signing certificates for OpenAI applications across macOS, Windows, iOS, and Android were exposed (no evidence of misuse to sign malicious software) and have been rotated as a precaution — **macOS users must update OpenAI applications by 2026-06-12** to maintain code-signing chain. Customer data, production systems, and deployed software were not affected.

2. **Mistral AI source code for sale**: TeamPCP listed Mistral AI source code on BreachForums for sale, threatening leak if no buyer. This appears to be a separate compromise vector exploiting the Wave 2 wave (most likely a Mistral employee device).

3. **$1,000 supply-chain contest**: Socket reported that TeamPCP and BreachForums announced a $1,000 prize contest on 2026-05-14 incentivising the largest-scale package compromise under the "Shai-Hulud" banner — adversary monetisation of the worm primitive itself, distinct from monetising compromised credentials.

**Why this is a material update:** Yesterday's entry framed Wave 2 as an npm-worm event with valid SLSA provenance attestations (the cryptographic-trust breakdown). Today's developments extend the impact into the frontier-AI-lab perimeter (OpenAI + Mistral) and document an explicit incentive escalation by the attackers. For any organisation that uses OpenAI Mac/Windows/iOS/Android apps, the cert rotation deadline is a 4-week patching window with operational impact.

**Mitigation:**
- For OpenAI app users: schedule mandatory app update by 2026-06-12; track any code-signing failures as IoC.
- For any org with developers on npm/PyPI: confirm all developer endpoints are post-Wave-2 patched (TanStack, Mistral-published packages, and the broader 169-package compromise list) and that GitHub PATs / publish tokens were rotated.
- Treat the $1,000 contest as a leading indicator of follow-on supply-chain attacks; add hunt-rule tripwires for new sleeper packages in npm/PyPI/RubyGems/Go for the next 30-60 days.
- Hunt CI runner logs for OIDC token theft IoCs (cf. Wave 2 `pull_request_target` + OIDC chain documented in MEMORY).

**Sources:** [BleepingComputer — OpenAI confirms security breach in TanStack supply chain attack](https://www.bleepingcomputer.com/news/security/openai-confirms-security-breach-in-tanstack-supply-chain-attack/) | [BleepingComputer — TeamPCP hackers advertise Mistral AI code repos for sale](https://www.bleepingcomputer.com/news/security/) | [Socket — TeamPCP and BreachForums Launch $1,000 Contest for Supply Chain Attacks](https://socket.dev/blog)

---

### Linux Kernel 'Fragnesia' CVE-2026-46300 — Public PoC Released With No Race Condition; LPE-To-Root Via Page-Cache Write *(Promotion of 2026-05-14 Noted item)*
**Product:** Linux kernel — XFRM ESP-in-TCP subsystem (all distributions with pre-2026-05-13 kernels) | **CVE:** CVE-2026-46300 | **CVSS:** —

Yesterday's report carried Fragnesia / "copyfail 3.0" as a Noted item (LPE-only, out of scope by default). The 2026-05-14 disclosure cycle promotes this materially: CVE-2026-46300 is assigned, a **public proof-of-concept exploit** is on GitHub (v12-security repository), and the exploit works **without race conditions**. The bug is a logic flaw in the Linux XFRM ESP-in-TCP subsystem that lets unprivileged local attackers write arbitrary bytes to the kernel page cache of read-only files — the canonical demonstration is corrupting `/usr/bin/su` to obtain a root shell. The bug is a sequel to the Dirty Frag class previously documented in MEMORY; the precedent in this family is CVE-2026-31431 (CopyFail), which CISA added to KEV after public exploitation tempo escalated within 30 days.

**Why this is a material update vs. yesterday's Noted item:** A public PoC with no-race-condition exploitation against a default-installed kernel on most Linux distributions removes the practical barrier to weaponisation. While LPE-only, this is a routine post-foothold escalation primitive that any commodity malware or red-team toolkit will adopt within 7-14 days; expect ransomware operators using initial-access via the Teams-helpdesk-impersonation pattern (cf. MEMORY) to chain Fragnesia for domain-admin privilege escalation. The CopyFail precedent (KEV-added) suggests the same trajectory is plausible.

**Mitigation:**
- Apply the kernel patches that landed 2026-05-13 across major distributions (Ubuntu, RHEL, SUSE, Debian, Amazon Linux 2023) as soon as packaged.
- Interim workaround: disable the vulnerable kernel modules via `modprobe -r` and modprobe.conf blacklist — note this breaks IPsec VPNs and AFS file systems where used.
- EDR/threat-hunt: alert on unexpected modifications to `/usr/bin/su` / `/usr/bin/sudo` / setuid binaries; alert on `XFRM` syscall sequences from non-network-daemon processes.
- Track CISA KEV for Fragnesia addition; the CopyFail (CVE-2026-31431) precedent suggests this may follow within 30 days.

**Sources:** [BleepingComputer — New Fragnesia Linux flaw lets attackers gain root privileges](https://www.bleepingcomputer.com/news/security/new-fragnesia-linux-flaw-lets-attackers-gain-root-privileges/) | [SecurityWeek — Linux Kernel Fragnesia](https://www.securityweek.com) | [HelpNetSecurity — Fragnesia kernel LPE](https://www.helpnetsecurity.com) | [oss-security 2026/05/14](https://www.openwall.com/lists/oss-security/2026/05/14)

---

### PraisonAI CVE-2026-44338 — Legacy Flask API Auth Disabled By Default; First Exploitation Attempts Within 4 Hours Of Public Disclosure
**Product:** PraisonAI multi-agent orchestration framework — legacy Flask API server | **CVE:** CVE-2026-44338 | **CVSS:** 7.3 | **First reported:** 2026-05-14

The PraisonAI legacy Flask API server ships with authentication **disabled by default**, exposing protected agent-orchestration endpoints to unauthenticated callers. SecurityWeek reports first exploitation attempts observed **less than 4 hours** after public disclosure. This is the third PraisonAI advisory in 30 days after the April 2026 batch (three CVEs including unauthenticated WebSocket session hijacking, YAML RCE, and import-based code injection) and the 2026-05-12 CVE-2026-44336 path-traversal/RCE noted item.

**Why it matters:** Self-hosted AI-agent platforms continue to demonstrate the same **default-no-auth** posture documented in MEMORY for the Ollama / n8n / LangFlow / Flowise class — burden of proof is now on showing the platform requires auth, not on showing it lacks it. Three CVEs in 30 days on the same project is a code-quality signal in line with nginx-ui (3 pre-auth RCEs in 2 months), Open WebUI (5+ high-severity CVEs in 30 days), and electerm (3 advisories in 30 days) — recommend PraisonAI as a deprecation/segmentation candidate.

**Mitigation:**
- Patch to the PraisonAI release that requires authentication by default (vendor advisory linked from SecurityWeek).
- Audit all PraisonAI deployments for default-config installations; assume any internet-exposed PraisonAI Flask API is compromised.
- Network-segment PraisonAI from production data stores and shared credentials.
- Add to the AI-platform-deprecation-candidate watchlist alongside nginx-ui / Open WebUI / electerm.

**Sources:** [TheHackerNews — Hackers Targeted PraisonAI Vulnerability Hours After Disclosure](https://thehackernews.com) | [SecurityWeek — PraisonAI authentication bypass](https://www.securityweek.com)

---

### node-ipc npm Package — Malicious Versions 9.1.6 / 9.2.3 / 12.0.1 Contain Obfuscated Stealer Targeting Developer Credentials + Cloud Secrets
**Product:** `node-ipc` npm package — versions 9.1.6, 9.2.3, 12.0.1 (transitive in many Electron/Node tooling and CI stacks) | **CVE:** none assigned | **First reported:** 2026-05-14

Three node-ipc npm package versions were found to contain obfuscated malware that **fingerprints the host system**, **harvests developer credentials and cloud-provider secrets** (AWS, GCP, GitHub PATs), and **exfiltrates to attacker C2** servers. Distinct from the Mini Shai-Hulud Wave 2 worm in that node-ipc is a single-package compromise without the trusted-publisher self-propagation primitive, but inhabits the same broader 2026-Q2 supply-chain landscape.

**Why it matters:** node-ipc has been historically controversial (the 2022 author-protest sabotage on Russian/Belarusian IP ranges is the precedent); this 2026 compromise is a clear malicious-third-party event, not author sabotage. node-ipc is a transitive dependency in many Electron desktop applications and Node-based CI tooling — compromised versions in the dependency tree of any package executed during developer install or CI build can exfiltrate workstation/CI secrets at scale.

**Mitigation:**
- Pin node-ipc to known-good versions (avoid 9.1.6, 9.2.3, 12.0.1); use `npm audit signatures` and lockfile review.
- Search CI logs and developer workstations for node-ipc installation events between approximate compromise window and disclosure; assume credential exposure if found.
- Rotate AWS keys, GitHub PATs, npm tokens, and cloud-provider credentials on any host that installed one of the three versions.
- Add the malicious node-ipc versions to internal package-mirror denylist.

**Sources:** [TheHackerNews — Stealer Backdoor in Node-IPC Versions](https://thehackernews.com)

---

### KongTuke IAB Pivots To Microsoft Teams Helpdesk-Impersonation Chain — 5-Minute Foothold; 8th Actor In 30 Days In The Teams-SE→MFA-Tamper→RMM Pattern
**Product:** Microsoft Teams external chat surface; ModeloRAT (KongTuke's commodity RAT) | **CVE:** — | **First reported:** 2026-05-14

KongTuke — an established initial-access broker that historically used FileFix/CrashFix web-based lures — added Microsoft Teams external-chat IT-helpdesk impersonation to its TTP portfolio. The chain: spoofed display names using Unicode whitespace tricks to look legitimate, direct chat impersonating IT support, victim runs a PowerShell command that pulls a Dropbox-hosted ZIP containing portable WinPython that delivers ModeloRAT. KongTuke rotates **five Microsoft 365 tenants** to evade external-org blocking; ModeloRAT now ships with five C2 failover servers, randomised URL paths, and three independent access paths (primary RAT, reverse shell, TCP backdoor). The campaign moves from cold outreach to persistent foothold in **under 5 minutes**.

**Why it matters:** This is the **8th distinct actor in 30 days** to adopt the Teams-helpdesk-impersonation chain (after BlackFile, SNOW/UNC6692, Cordial Spider, Snarky Spider, Microsoft Code-of-Conduct AiTM, VENOMOUS#HELPER, MuddyWater). At this volume, the chain is no longer a single-actor TTP but the **mainstream 2026-Q2 enterprise initial-access pattern**. KongTuke specifically operates as an IAB selling foothold access to ransomware operators downstream, so today's Teams compromise becomes tomorrow's ransomware deployment.

**Mitigation:**
- Block Microsoft Teams external chat by default for the entire org or restrict to per-recipient pre-approval; reject incoming external chat from unverified org domains.
- Alert on Teams external-tenant chats containing PowerShell commands or download URLs (Dropbox/Mediafire/WeTransfer).
- Block portable WinPython execution at the EDR / app-control tier unless explicitly allow-listed.
- Add ModeloRAT C2 infrastructure IoCs to perimeter blocklists once vendor reports surface (track via Microsoft DART, Securonix, Sophos X-Ops, Rapid7 in coming days).
- Train helpdesk and frontline users on the Unicode-whitespace-display-name pattern as a specific IoC.

**Sources:** [BleepingComputer — KongTuke hackers now use Microsoft Teams for corporate breaches](https://www.bleepingcomputer.com/news/security/kongtuke-hackers-now-use-microsoft-teams-for-corporate-breaches/)

---

## 🟡 MEDIUM

### Pwn2Own Berlin 2026 Day 1 — 24 Unique Zero-Days In Windows 11 / Microsoft Edge / VMware Stack; $523,000 Awarded; VMware Fusion CVE-2026-41702 Proactively Patched Mid-Event
**Product:** Windows 11, Microsoft Edge, VMware Fusion + ESXi, additional virtualization and enterprise targets | **CVE:** CVE-2026-41702 (VMware Fusion); 23 additional pending vendor advisory assignment | **Published:** 2026-05-14

Day 1 of Pwn2Own Berlin (2026-05-14) saw researchers demonstrate **24 unique zero-days** against Windows 11, Microsoft Edge, and the VMware stack, with $523,000 in awards. Broadcom proactively shipped **VMware Fusion CVE-2026-41702** — a TOCTOU vulnerability in a SETUID binary allowing local non-administrative users to escalate to root, reported by Mathieu Farrell — during the event. The remaining 23 zero-day chains are under embargo pending vendor coordination; individual CVE assignments will land over the next 60-90 days.

**Mitigation:** Track ZDI's published advisories and the Microsoft, Broadcom, Mozilla, and other vendor security feeds over the next 60-90 days for the Pwn2Own Berlin CVE landings. Apply the Patch Tuesday flow rigorously through Q2 2026 — Pwn2Own batch sizes typically translate to 30-50 CVEs landing in the following two Patch Tuesdays.

**Sources:** [BleepingComputer — Windows 11 and Microsoft Edge hacked at Pwn2Own Berlin 2026](https://www.bleepingcomputer.com/news/security/windows-11-and-microsoft-edge-hacked-at-pwn2own-berlin-2026/) | [SecurityWeek — High-Severity Vulnerability Patched in VMware Fusion](https://www.securityweek.com/high-severity-vulnerability-patched-in-vmware-fusion/)

---

## 📋 Noted / Monitoring

**BitLocker YellowKey + GreenPlasma (unpatched, PoC released)** — Researcher 'Chaotic Eclipse' published PoC for two unpatched Windows issues on 2026-05-13: NTFS-transactions BitLocker bypass via FsTx file on USB/EFI + WinRE (TPM-only, original-device only) and CTFMON arbitrary-section-creation LPE; LPE/local-only and out of scope for fleet alerting but relevant for endpoint EDR teams.

**CVE-2026-31236 simonw LLM CLI tool 0.27.1** — CVSS 9.8 unrestricted Python code execution via unsanitized `--functions` argument; niche developer-tool RCE but the LLM CLI is widely installed in agentic-AI experimentation environments.

**CVE-2026-8328 CPython FTP PASV SSRF** — `ftpcp()` trusts server-supplied PASV host address instead of actual peer address (oss-security 2026-05-14); SSRF primitive in Python's FTP module — relevant for CI pipelines using CPython FTP against attacker-controlled servers.

**CVE-2026-45205 Apache Commons Configuration** — StackOverflowError via YAML cyclic data structures (oss-security 2026-05-14); DoS-class, widely-deployed Apache library.

**Vim 3-issue batch** — `tar.vim` command injection, `netrw` `NetrwMarkFile()` code injection, spell-file heap overflow (oss-security 2026-05-14); client-side editor issues affecting Vim < 9.2.480 — out of scope for the infrastructure perimeter but relevant for engineering-workstation hardening.

**CVE-2026-45411 vm2 sandbox (npm)** — Additional vm2 sandbox escape via async generators (GHSA-248r-7h7q-cr24, 2026-05-14) — extends the 'vm2 is structurally broken' pattern documented in MEMORY; recommendation unchanged (migrate to `isolated-vm`).

**Open WebUI multi-CVE batch** — CVE-2026-45675 (LDAP/OAuth first-user race condition), CVE-2026-45672 (Jupyter execution bypass when feature gate disabled), CVE-2026-45671 (shared-chat access-control bypass), CVE-2026-45665 (banner stored XSS), CVE-2026-45402 (cross-user file access) — five new GHSA advisories on 2026-05-14; extends the 4-high-severity-in-30-days code-quality signal already in MEMORY pattern library.

**CVE-2026-45369 + CVE-2026-45370 utcp-cli (pip)** — Command injection via unsanitized argument substitution + full-process-env exposure (GHSA 2026-05-14); niche CLI tool.

**deepseek-tui 4-CVE batch** — CVE-2026-45374 (RCE via prompt injection), CVE-2026-45311 (RCE via run_tests tool), CVE-2026-45373 (SSRF via IPv6 bypass), CVE-2026-45310 (SSRF via HTTP redirect bypass) — joins the AI-coding-assistant trust-boundary class (Claude Code MCP / TrustFall / ClaudeBleed).

**CVE-2026-45353 electerm (npm)** — Local code execution via single-instance socket vulnerability (GHSA 2026-05-14); third electerm advisory in 30 days after 2026-05-09 CVE-2026-43940/43944.

**@samanhappy/mcphub (npm)** — MCP Hub SSE endpoint accepts arbitrary username without authentication (GHSA-wf8q-wvv8-p8jf, 2026-05-14); fits the broader MCP-server authn-handling pattern.

**CVE-2026-45288 Marten (NuGet)** — Injection vulnerability in full-text search regConfig parameter (GHSA 2026-05-14); .NET data-access library.

**F5 BIG-IP companion CVEs** — CVE-2026-41225 (CVSS 8.6 Manager-permission iControl REST → command execution), CVE-2026-41957, CVE-2026-34176, CVE-2026-39459 — authenticated-attacker RCE/command-injection in BIG-IP, plus 12 BIG-IP DoS issues in the Traffic Management Microkernel. Bundled with NGINX Rift; same patch cycle.

**CVE-2026-42897 Microsoft Exchange Server (CVSS 8.1)** — May Patch Tuesday issue surfaced via dbugs.ptsecurity.com; track for any pivot to on-prem PRC-cluster ProxyNotShell-like chains.

**TeamPCP + BreachForums $1,000 supply-chain attack contest** — Socket reported a contest announced 2026-05-14 incentivising the largest-scale package compromise under the 'Shai-Hulud' banner; incentive-escalation data point, no live compromise yet.

**Packagist Composer / GitHub Actions token leak** — Socket reported a GitHub Actions token format change caused some PHP/Composer-side tokens to be inadvertently logged in CI; Packagist recommending immediate Composer update.

**Amazon Q authorization bypass** — Helpnetsecurity 2026-05-14 — users can bypass access controls to reach AI chat agents that should be blocked; limited technical detail published.

**MuddyWater (Iran/MOIS) South Korean major electronics maker** — Bleepingcomputer 2026-05-14 — MuddyWater cyber-espionage campaign expanded targeting to a major South Korean electronics manufacturer plus 9 high-profile organisations; same actor already covered in the Teams-helpdesk-impersonation pattern.

**West Pharmaceutical Services ransomware** — Bleepingcomputer 2026-05-14 — pharmaceutical packaging vendor disclosed data theft + encryption; no public attribution or novel TTP.

**Apache ActiveMQ CVE-2026-34197 Jolokia RCE retrospective** — Alexander Leonov published 2026-05-14 deep-dive analysis of CVE-2026-34197 (covered originally 2026-04-17/22/25) — ~7,000 servers exposed online, public exploits since early April; analytical, no new tempo signal.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog, cert.gov.ua | ❌ (403 / no content) — KEV-add tracked via BC/SA/SW relay |
| Vendor advisories | fortinet.com/blog/threat-research, fortiguard.com/psirt (suppl.), msrc.microsoft.com/blog | ⚠️ (Fortinet blog dated April; PSIRT direct latest 2026-05-12; MSRC blog redirects, no content) |
| Research / OSINT | schneier.com, krebsonsecurity.com, securitylab.github.com, kb.cert.org/vuls, openwall oss-security (suppl.), avleonov.com, github.com/advisories (suppl.) | ✅ / ⚠️ |
| Supply chain | socket.dev/blog (suppl.), aikido.dev/blog (suppl.) | ✅ |
| Threat intel | rapid7.com (degraded), opencve.io, dbugs.ptsecurity.com, securityaffairs.com (suppl.), helpnetsecurity.com (suppl.) | ✅ / ⚠️ |
| Reference DB | nvd.nist.gov, cve.org, cve.mitre.org, attackerkb.com, hackerone.com/hacktivity, bugcrowd.com/disclosures, github.com/0xMarcio/cve, packetstorm.news | ⚠️ / ❌ |

**Errors:** `cisa.gov` (403), `cisa.gov/known-exploited-vulnerabilities-catalog` (403), `attackerkb.com` (403), `seclists.org/fulldisclosure` (302 to root), `cve.mitre.org` → `cve.org` (JS-required), `cve.org` (JS-required), `googleprojectzero.blogspot.com` → `projectzero.google/` (JS-required), `msrc.microsoft.com/blog` (no content via WebFetch), `hackerone.com/hacktivity` (JS-required), `bugcrowd.com/disclosures` (404), `cert.gov.ua` (empty content). Degraded (reachable but no surfaced May 14-15 content): rapid7.com, fortinet.com/blog/threat-research, packetstorm.news, nvd.nist.gov, github.com/0xMarcio/cve, habr.com/ru/companies/tomhunter/articles, teletype.in/@cyberok, github.com/search?q=CVE.

**CISA KEV:** CVE-2026-20182 Cisco Catalyst SD-WAN Controller added 2026-05-14 with federal remediation deadline 2026-05-17 (per BleepingComputer / SecurityAffairs relay; CISA gateway 403 via WebFetch — verify via direct CISA query from a desktop browser).

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-15/night | Next: 2026-05-16/night*
