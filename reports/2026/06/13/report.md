# Watchtower Night Report — 2026-06-13
**Cycle:** Night | **Generated:** 2026-06-13 00:30 UTC (2026-06-13T00:30:00Z)
**Sources checked:** 21/30 | **CISA KEV total:** advisory-channel only — cisa.gov direct fetch 403 | **New KEV additions:** Ivanti Sentry CVE-2026-10520 added 2026-06-11 (first BOD 26-04 invocation, 3-day deadline 2026-06-14)

---

## 🔴 CRITICAL

### Ivanti Sentry CVE-2026-10520 (CVSS 10.0) — CISA KEV-Added 2026-06-11 With First-Ever BOD 26-04 3-Day Federal Deadline Of 2026-06-14 (Sunday); Shadowserver Scanning Now Reports A 2/19 Backdoored-To-Vulnerable Ratio On Internet-Exposed Gateways; Ivanti Disputes Production-Exploitation Framing (Calls It "Honeypot-Only")
**Product:** Ivanti Sentry (formerly MobileIron Sentry) mobile-gateway | **CVE:** CVE-2026-10520 | **Status:** KEV / Active Exploitation / Vendor-Disputed Framing

The OS command injection vulnerability that Watchtower has tracked since 2026-06-09 — first as a PT-Security dbugs NOTED, then as the 06-10 vendor advisory + watchTowr PoC UPDATE, then as the 06-11 Shadowserver "2-of-19 already backdoored" CRITICAL UPDATE — graduated overnight to its KEV/BOD-26-04 endgame. CISA added CVE-2026-10520 to the Known Exploited Vulnerabilities Catalog on 2026-06-11 and immediately invoked Binding Operational Directive 26-04 (published 2026-06-11, see yesterday's NOTED), pinning a 3-day FCEB remediation deadline of Sunday 2026-06-14. Per BleepingComputer this is the **first vulnerability ever to trigger BOD 26-04** — the directive's "KEV-listed full-control issue on internet-exposed asset" tier — and the deadline lands the same week the directive itself was published. Shadowserver's 2026-06-11/12 scanning continues to report 2-of-19 internet-exposed gateways already backdoored ("the rest probably also compromised"). Ivanti's official response (SecurityWeek) frames the observed exploitation as **honeypot traffic only** and reiterates that the management port 8443 "should never be exposed to the internet" — a vendor-disputed-framing dynamic to watch, given Shadowserver's scanning explicitly distinguishes vulnerable-and-backdoored from honeypot signature matches.

**Timeline:** PT-Security dbugs index 2026-06-09 → vendor advisory + watchTowr PoC 2026-06-10 → Shadowserver active-exploit confirmation 2026-06-11 → CISA KEV add + BOD 26-04 first invocation 2026-06-11 → FCEB deadline 2026-06-14 (Sunday).

**Why it matters:** Any internet-facing Sentry gateway that is not yet on R10.5.2 / R10.6.2 / R10.7.1 should be treated as already-compromised, not "to be patched soon" — Shadowserver's 2/19 ratio with a publicly available PoC means commodity ransomware affiliates have a 5-day head start on a deadline a single AD-joined org-domain credential could weaponise into Veeam-style backup-server pivoting. The Ivanti "honeypot-only" framing should NOT delay your IR sweep; the same Shadowserver dataset that detected the 2 backdoors flagged 19 still-vulnerable Internet-exposed instances — that is the universe at risk.

**Discovered by:** Original vulnerability — Saudi NCA + Ivanti PSIRT. Active-exploitation detection — Shadowserver Foundation. KEV / BOD-26-04 enforcement — CISA.

**Mitigation:**
- Upgrade Ivanti Sentry to R10.5.2 / R10.6.2 / R10.7.1 *today*; if you cannot patch by 2026-06-14, take internet-exposed gateways offline.
- IR-hunt every reachable Sentry gateway for backdoor artefacts using Shadowserver's published signatures (web shells, persistence units, anomalous root processes).
- If management port 8443 is exposed to the internet for any reason, restrict to mTLS-only with allow-listed admin IPs, then re-audit access logs for the 2026-05-08 → 2026-06-12 window.
- Treat any unpatched perimeter Sentry as already compromised — credential rotation, key roll-over, full host-level IR.
- Update SOC content with BOD 26-04 tiered SLAs (3-day for KEV full-control on internet-exposed assets, 14-day for KEV partial-control / non-automatable) as the new federal-equivalent benchmark.

**Sources:** [BleepingComputer — CISA orders feds to patch Ivanti flaw by Sunday](https://www.bleepingcomputer.com/news/security/cisa-gives-feds-3-days-to-patch-ivanti-flaw-exploited-in-attacks/) | [SecurityWeek — Ivanti Sentry exploitation attempts hitting honeypots](https://www.securityweek.com/ivanti-sentry-exploitation-attempts-hitting-honeypots/)

---

### Arch Linux AUR Mass-Compromise — 400+ Hijacked Packages Pushing Rust-Based Credential Stealer + eBPF Kernel Rootkit Via `atomic-lockfile@1.4.2` npm Dependency Injected Into Spoofed-Maintainer PKGBUILD Files; Targets Browser/Slack/Discord/Teams Sessions + GitHub/npm/Vault/SSH/Docker Credentials; Detection IOCs Published 2026-06-12
**Product:** Arch User Repository (AUR) build scripts (PKGBUILD) — 400+ community packages compromised; Arch official repositories unaffected | **CVE:** None assigned (supply-chain incident, not a code-level CVE) | **Status:** Active Compromise / Detection IOCs Available

Threat actors adopted abandoned packages on Arch's community repository (AUR), edited the PKGBUILD build scripts of >400 packages, and spoofed git commit metadata to make the changes look like long-standing-maintainer commits. The malicious build step pulls `atomic-lockfile@1.4.2` from npm during the user's local package build; that npm dep loads a Rust-compiled ELF infostealer that harvests:

- Browser cookies / tokens / local storage from Chrome, Edge, Brave
- Electron-app session data from Slack, Discord, Microsoft Teams
- GitHub credentials / npm tokens / HashiCorp Vault tokens / SSH artefacts
- Docker and Podman registry credentials
- Telegram session keys

When run with root (e.g. via `makepkg -i` or any AUR helper that escalates), the same payload deploys an eBPF rootkit that hides processes, files, and network interfaces — surviving conventional cleanup. Researcher **Whanos** has published a detection script + IOC list; the main payload SHA-256 is `6144d433f8a0316869877b5f834c801251bbb936e5f1577c5680878c7443c98b`. Arch maintainers began removing the malicious commits and banning the offending accounts overnight 2026-06-11/12.

**Timeline:** Hijacking activity backdated via spoofed commit timestamps; public disclosure 2026-06-12 (BleepingComputer, THN, Sonatype). 20 orphaned-package hijacks reported by Sonatype before the broader >400 figure was confirmed.

**Why it matters:** Any developer workstation, CI/CD agent, or container image build host that ran an AUR `makepkg` operation since 2026-06-11 must be treated as credential-compromised AND potentially eBPF-rootkitted. The blast radius extends beyond Arch desktop users — corporate Linux dev fleets that allow Arch in containerised CI runners, hobbyist sysadmin endpoints with cached AWS/GCP/GitHub tokens, and anyone using AUR for ephemeral dev tooling are all in scope. This is the **third Rust + eBPF supply-chain incident in 2026** (joins IronWorm npm Wave-2 from 2026-06-04 and Miasma 2026-06-02) — the IronWorm prediction window for "3-7 more Wave-2-class compromises by 2026-06-15" is now confirmed at four.

**Discovered by:** Whanos (detection IOCs), Sonatype (orphan-package analysis), broader Arch community via PKGBUILD audits.

**Mitigation:**
- Audit every workstation / CI host / container that ran `makepkg` or any AUR helper (yay, paru, etc.) since 2026-06-11; treat as credential-compromised.
- Use Whanos's detection script + check `/sys/fs/bpf/` for hidden eBPF maps; SHA-256 hunt for `6144d433f8a0316869877b5f834c801251bbb936e5f1577c5680878c7443c98b`.
- Rotate all credentials any affected user might have had locally: GitHub PATs, npm tokens, Vault tokens, AWS / GCP / Azure CLI credentials, SSH keys, Slack / Teams / Discord session cookies, browser-stored passwords.
- For any host that ran the payload as root: consider reinstall from clean media — eBPF rootkit removal is unreliable.
- Block / quarantine `atomic-lockfile@1.4.2` in npm proxies; add to artefact-registry deny-lists.
- Restrict AUR usage in corporate fleets to a curated allow-list pinned to known-good commits; require manual review for any orphaned-package adoption.

**Sources:** [BleepingComputer — 400+ Arch Linux packages compromised](https://www.bleepingcomputer.com/news/security/over-400-arch-linux-packages-compromised-to-push-rootkit-infostealer/) | [The Hacker News — Over 400 Arch Linux AUR packages](https://thehackernews.com/2026/06/over-400-arch-linux-aur-packages.html)

---

## 🟠 HIGH

### "Agentjacking" — New Attack Class Hijacks AI Coding Agents (Claude Code, Cursor) Via Crafted Sentry Error Events Injected At The DSN Ingest Endpoint; 2,388 Organisations With Exposed DSNs Confirmed; 85% Success Rate Across Tested AI Coding Assistants; Sentry Declined Architectural Fix Citing "Not Technically Defensible"
**Product:** Sentry error-tracking platform + downstream AI coding agents (Claude Code, Cursor) consuming Sentry data via Model Context Protocol (MCP) | **CVE:** None assigned | **CVSS:** N/A | **First reported:** 2026-06-12

Researchers at **Tenet Security** disclosed a new attack class targeting the trust gap between Sentry's event ingestion API and AI coding agents that consume Sentry data via MCP. Sentry DSNs (Data Source Names) are public, write-only credentials embedded in client-side code so the application can POST error events — and Sentry's event-ingestion endpoint accepts arbitrary payloads from anyone holding the DSN. An attacker who scrapes a target DSN from public website JavaScript can POST a maliciously formatted error event whose `message` and `context` fields contain markdown that renders identically to legitimate Sentry templates. When a developer subsequently asks their AI coding agent to "fix unresolved Sentry issues," the agent queries Sentry via MCP and interprets the attacker's markdown as **trusted system output** — executing the embedded instructions with developer-account privileges. Tenet reports an 85% success rate across tested AI coding assistants and 2,388 organisations with vulnerable DSNs in their published proof-set. The technique bypasses EDR, WAF, IAM, VPN, Cloudflare, and host firewalls because the malicious traffic flows over the legitimate Sentry ingest path. Sentry has acknowledged the report, declined an architectural fix (calling it "not technically defensible"), and shipped a content filter that blocks specific payload strings — a duct-tape mitigation that adversarial markdown can almost certainly evade.

**Mitigation:**
- Audit every product / repository whose source code or build artefacts embed a Sentry DSN — these are now an attacker-reachable injection point.
- If your engineers use Claude Code / Cursor with Sentry MCP integrations, disable the integration on shared / multi-tenant projects until a structural fix lands.
- Treat any AI-coding-agent action whose source is "Sentry error context" as untrusted input — require human review before the agent applies code changes, runs shell commands, or exfiltrates files.
- Track Tenet Security's public DSN-exposure list and rotate any DSNs that appear; consider front-ending Sentry ingest with an authentication proxy on internal projects.
- Long-term: treat all third-party MCP data sources as untrusted — this is a generalisable pattern that will recur (Jira / Linear / Slack / Notion / GitHub Issues all expose similar agent-readable surfaces).

**Sources:** [The Hacker News — Agentjacking attack tricks AI coding agents](https://thehackernews.com/2026/06/agentjacking-attack-tricks-ai-coding.html)

---

### Velvet Ant "Operation Highland" — China-Nexus APT Backdoored Linux PAM + OpenSSH On Air-Gapped Networks With Nine Modified PAM Modules + Credential-Logging OpenSSH Builds + Secret Password Switches; Persistence Dates To 2016 (~Decade-Long Dwell Time); Sygnia Discovery 2026-06-12
**Product:** Linux authentication stack — `/lib/security/pam_*.so` modules + `sshd` binary across glibc-based distros on air-gapped enterprise networks | **CVE:** None assigned (post-compromise persistence, not a CVE-class advisory) | **CVSS:** N/A | **First reported:** 2026-06-12

Sygnia researchers published a deep technical report on a Velvet Ant intrusion they call **Operation Highland** — a Chinese state-aligned APT that has been resident inside an air-gapped enterprise network since approximately **2016**, evading repeated eradication attempts by backdooring the Linux authentication stack itself. The implants comprise **nine separate modified PAM modules** plus a custom `sshd` build that logs credentials + command history + supports two persistence primitives: (1) a hard-coded master password that authenticates any user, and (2) a hidden environment-variable switch that disables credential logging when an operator wants stealth. Because authentication itself is compromised, traditional containment (password resets, key rotation, session termination) is ineffective. Initial-access staging went through an internet-facing web server bridge into the air-gapped segment. Sygnia frames this as the most durable Velvet-Ant dwell time documented — joining the same group's prior Cisco / F5 / Juniper edge-device zero-day campaigns (Watchtower covered the F5 line in February 2026).

**Why it matters:** Linux servers in your environment that authenticate against PAM (effectively all of them — Active Directory–integrated PAM via SSSD, local Unix accounts, even Kubernetes node SSH) are exactly the integrity-monitoring blind spot Velvet Ant exploits. The Sygnia report is **the canonical detection playbook** for this attack class: file-integrity-check `pam_unix.so` / `pam_sssd.so` / `sshd` against known-good baselines, hunt for hidden environment-variable switches in `/etc/ssh/sshd_config.d/`, and treat any sshd binary whose mtime predates the last package upgrade by years as suspect.

**Mitigation:**
- Run integrity checks (sha256sum + AIDE/Tripwire baseline) on `/lib/x86_64-linux-gnu/security/pam_*.so`, `/usr/sbin/sshd`, and any PAM module file across every Linux host — compare against distro package hashes from the repository.
- Hunt for the secret-password authentication primitive: review auth.log for successful logins where the username does not match any account in the local /etc/passwd or AD.
- Audit `/etc/environment` + `/etc/ssh/sshd_config.d/` for unexpected variables that suppress logging.
- Re-image any host whose sshd / PAM hash does not match the package manager's known-good — credential rotation alone does not work when auth itself is backdoored.
- Treat MSP-managed and air-gapped hosts with the same EDR / file-integrity coverage as internet-facing hosts; Velvet Ant's lack-of-EDR-on-air-gap pattern is by now well-documented.

**Sources:** [The Hacker News — China-linked hackers backdoored Linux login systems](https://thehackernews.com/2026/06/china-linked-hackers-backdoored-linux.html)

---

### phpBB 10-Year Authentication Bypass — Single-HTTP-Request Login As Any User (Including Administrators) On Default Configurations; Affects 3.3.16 And Below + 4.0.0-a2 And Below; Patched 3.3.17 Released 2026-06-06 By Aikido / HackerOne; Disclosed Publicly 2026-06-12
**Product:** phpBB forum software — 3.3.16 and below, 4.0.0-a2 and below | **CVE:** Not yet assigned | **CVSS:** Critical-class auth bypass (no formal score yet) | **First reported:** 2026-06-12 (4-day responsible-disclosure window)

A 10-year-old logic flaw in phpBB authentication allows an unauthenticated attacker to log in as any user — administrator included — with **a single HTTP request requiring no special knowledge**, under default configuration. Researchers at **Aikido** found the bug on 2026-06-02, reported it through phpBB's HackerOne program, and phpBB shipped 3.3.17 four days later on 2026-06-06; public disclosure landed 2026-06-12. Remote code execution is **not** directly reachable because the Admin Control Panel is behind a separate password-prompt layer, but the bypass yields complete impersonation: read private messages, manipulate content / accounts, deface forums, exfiltrate registered-user PII. No safe 4.x release exists yet — the only path is downgrade or wait.

**Why it matters:** phpBB is still a non-trivial corporate exposure surface — community forums attached to mid-market e-commerce brands, internal support portals for legacy products, embedded user-management for industry conferences, partner-portal forums. The bypass-as-any-administrator vector also makes phpBB instances a credible **credential-harvesting waterhole**: an attacker who deface-modifies a phpBB instance can pivot to harvesting employee credentials reused across other corporate properties.

**Mitigation:**
- Inventory every phpBB instance on owned or hosted properties; upgrade 3.x deployments to 3.3.17 immediately.
- For 4.0.0-a2 / earlier 4.x deployments: no safe release yet — either downgrade to 3.3.17 or apply IP allow-listing on the login + ACP endpoints until 4.0.0-a3 ships.
- Audit `/store/log_*.log` for unexpected successful admin logins since 2025-06-12 (10-year retroactive window).
- Force password reset on any account that has been an admin or moderator on an affected instance.
- Add phpBB to your asset-discovery + EOL-software inventory if not already tracked — it is a long-tail attack surface.

**Sources:** [BleepingComputer — phpBB fixes auth bypass bug lurking for a decade](https://www.bleepingcomputer.com/news/security/phpbb-forum-fixes-auth-bypass-bug-lurking-for-a-decade/)

---

### Squid 7.6 Multi-CVE Batch — CVE-2026-47729 Out-Of-Bounds Read In FTP Gateway (Cross-Session Data Disclosure) + CVE-2026-50012 Heap Buffer Overflow In Cache Digests (Malicious-Server RCE Primitive, --enable-cache-digests Only); oss-security Disclosure 2026-06-12 By Amos Jeffries / Squid Software Foundation
**Product:** Squid caching proxy / web cache — patched in Squid 7.6 | **CVE:** CVE-2026-47729, CVE-2026-50012 | **CVSS:** Pending | **First reported:** 2026-06-12

Amos Jeffries (Squid Software Foundation) disclosed two new Squid CVEs via oss-security: **CVE-2026-47729** is an out-of-bounds read in the FTP gateway component — a legitimate FTP client connecting through Squid against a malicious FTP server can disclose data from unrelated client sessions sharing the same Squid worker process, an information-disclosure primitive that is particularly dangerous for multi-tenant proxy fleets. **CVE-2026-50012** is a heap-based buffer overflow in cache-digests parsing — a malicious upstream cache responding to a `cache_digest` request can corrupt the Squid worker process's heap, providing a memory-corruption RCE primitive — but only when Squid is compiled with `--enable-cache-digests` (not the most common build flag, but a non-zero population of enterprise builds enable it for performance reasons). Patches are linked in the advisory (`865a131c7d557e68c965043d98c2eccae26deef8` for FTP, `19fcfe922717c8b255270c032dcde4071c003bcd` for cache digests).

**Mitigation:**
- Upgrade Squid to 7.6 across the proxy fleet.
- If you cannot upgrade immediately and your build was compiled with `--enable-cache-digests`, recompile without that flag as a stopgap.
- For shared-tenant Squid deployments (ISP / CDN / large-corporate), prioritise FTP-gateway-disabled builds where the FTP-proxy feature is not in use.
- Audit upstream-cache-peer configurations — `cache_digest` parsing only triggers on configured peers, so unconfigured peers cannot reach the overflow path.

**Sources:** [oss-security — Squid CVE-2026-47729 and CVE-2026-50012](https://www.openwall.com/lists/oss-security/2026/06/12/1)

---

## 🟡 MEDIUM

### Portainer CVE-2026-33590 (CVSS 8.2) — Insecure Default Settings Allow Regular Portainer Users To Execute Arbitrary Commands With Elevated Privileges On The Container Host (Bind-Mount + Privileged-Mode Defaults); Patched 2.38.0 + 2.39.0 By Sifis Bampionitakis / intWave 2026-06-12
**Product:** Portainer < 2.38.0 (STS) / < 2.39.0 (LTS) — Docker / Kubernetes container management UI | **CVE:** CVE-2026-33590 | **Published:** 2026-06-12

Sifis Bampionitakis (intWave intern) disclosed via oss-security that Portainer ships with insecure default Docker security settings that allow regular Portainer users to spin up containers with **bind-mounts of arbitrary host paths + privileged-mode flag set**, which is a textbook container-escape-by-design primitive — mount `/` from the host into a privileged container, you have host root. Fixed in Portainer 2.38.0 (short-term support) and 2.39.0 (long-term support) by tightening the default Docker Security Settings.

**Mitigation:** Upgrade to Portainer 2.38.0 STS or 2.39.0 LTS. For instances that cannot be upgraded immediately, manually disable bind-mounts and privileged-mode in the Docker Security Settings UI for all non-admin Portainer roles. Audit every non-admin user's recent container creation history for surprise privileged + bind-mount-`/` containers, and treat any host running such a container as compromised.

**Sources:** [oss-security — CVE-2026-33590 Portainer host takeover](https://www.openwall.com/lists/oss-security/2026/06/12/3)

---

### LangGraph 3-CVE Chain — CVE-2025-67644 (CVSS 7.3) SQL Injection In SQLite Checkpointer + CVE-2026-28277 (CVSS 6.8) Unsafe msgpack Deserialization + CVE-2026-27022 (CVSS 6.5) RediSearch Query Injection; SQLi + Deser Chain Yields Self-Hosted RCE On Exposed get_state_history(); LangSmith Managed Platform Unaffected
**Product:** LangGraph (LangChain agentic-framework) — self-hosted deployments using SQLite or Redis checkpointers | **CVE:** CVE-2025-67644, CVE-2026-28277, CVE-2026-27022 | **Published:** 2026-06-12

LangChain disclosed three checkpointer-store CVEs in LangGraph. Two chain: an attacker controlling the metadata-filter input to a `get_state_history()` endpoint can inject SQL via the SQLite checkpointer (CVE-2025-67644) to return malicious checkpoint blobs, which then trigger the unsafe msgpack deserialiser (CVE-2026-28277) → arbitrary code execution on the LangGraph server. CVE-2026-27022 is an independent RediSearch query-injection issue in the Redis checkpointer that allows access-control bypass on stored agent state. **LangSmith's managed platform is not affected** — this is a self-hosted-deployment issue only.

**Mitigation:** Upgrade `langgraph-checkpoint-sqlite` to 3.0.1+, `langgraph` to 1.0.10+, and `@langchain/langgraph-checkpoint-redis` to 1.0.1+. Restrict who can reach the `get_state_history()` endpoint until you patch. Continues the durable pattern from MEMORY 2026-06-11: self-hosted AI workflow / agent platforms (Langflow, Flowise, Open WebUI, FastGPT, now LangGraph) need Web/HTTP-fleet-tier patch SLAs because they expose agent state machinery to attacker input by default.

**Sources:** [The Hacker News — LangGraph flaw chain exposes self-hosted RCE](https://thehackernews.com/2026/06/langgraph-flaw-chain-exposes-self.html)

---

## 📋 Noted / Monitoring

**Cal Water — California Water Service breach by Iranian "Handala" group** — Threat actor published ~5GB including customer PII (names, addresses, phone, account numbers, payment histories), administrative credentials for an RTKBase GNSS-base-station instance running for 783 continuous hours, and mountpoint-level NTRIP passwords across 7 districts; Cal Water serves ~2M customers across 100 California communities; no CVE — initial access likely through the unmanaged RTKBase platform; Cal Water has not publicly acknowledged the intrusion as of disclosure (SecurityWeek 2026-06-12).

**Tchap French government messenger breach — scope confirmed 73,000 accounts (~9% of 825,000 registered)** — Continuation of the 2026-06-10 Watchtower NOTED; threat actor compromised a single user account via social engineering and scraped unencrypted public-room metadata (names, emails, organisational affiliations, avatars) — private E2EE conversations not exposed; actor claims 13.5GB documents/media + hardcoded LDAP credentials; not a protocol-level CVE.

**Sniper Dz phishing-as-a-service platform dismantled — INTERPOL Operation Ramz, 201 arrests across 13 MENA countries + admin "Guedz" arrested in Algeria** — Group-IB-supported takedown of a decade-old PhaaS platform that generated 20K+ phishing domains and 45K+ victim records targeting PayPal/Facebook/Netflix-class brands; operational item, no IOCs of immediate-defender relevance (THN 2026-06-12).

**AudiA6 cryptocurrency-laundering service dismantled — Europol-coordinated takedown 2026-06-10 (~€336M / $389M laundered since 2021)** — Two Ukrainian + Russian nationals arrested in Georgia; 25 domains seized + 30 servers offline + €692K crypto + €86K cash frozen; DoJ conspiracy + money-laundering charges (20yr max); traced ~393.39 BTC (~$19.2M) from darknet markets and ransomware orgs directly into AudiA6 wallets (THN 2026-06-12).

**Google Civil Lawsuit Against Chinese "Outsider" Smishing PhaaS Network — Gemini-AI-assisted phishing-page generation** — Filed 2026-06-12: 100K+ victims, 9K fake sites + 1.59M fraudulent URLs created between 2025-11 and 2026-04, 2.5M smishing texts to Android users in a 2-week May-June window; kit costs $88/week with 290+ brand templates + Telegram-bot ordering; Google partnered with AT&T/T-Mobile/Verizon for blocking; AI-platform-misuse data point for defenders monitoring Gemini-as-a-toolchain abuse.

**The Gentlemen ransomware-as-a-service operator profile — Zeta88 / Hastalamuerte, 90/10 affiliate split, 478 victims claimed including 240+ in 2026** — Krebs 2026-06-10 deep-dive on the second-most-active RaaS gang; Russian-speaking; LockBit-affiliate-evolved-to-independent; targets internet-facing VPN/firewall devices; durable affiliate-economic-pressure signal for any org with perimeter-fleet patch SLAs slipping past 14 days.

**Anthropic Claude "Fable 5" — researcher prompt-based jailbreak claim, Anthropic disputes it constitutes a genuine vulnerability** — SecurityWeek 2026-06-12; tracked for AI-vendor-vs-researcher dispute pattern; if validated, the cluster would join earlier Microsoft 365 Copilot + LiteLLM mitigated-server-side AI-platform disclosures from MEMORY 2026-06-08 / 2026-06-10.

**Crypt::PBKDF2 Perl module pre-0.261630 batch — CVE-2017-20240 timing-attack on derived-key comparison + CVE-2026-9638 weak salt-RNG + CVE-2026-9641 weak default algorithm/iteration-count** — Robert Rothenberg via oss-security 2026-06-12; Perl-ecosystem long-tail; relevant only to legacy Perl auth services that selected Crypt::PBKDF2 for password hashing.

**Aqara Smart Home cluster CVSS 9.0+ — IAM/SSO Gateway CVE-2026-50086 (CVSS 10.0), Cloud OAuth CVE-2026-50090 (CVSS 9.3), Cloud API CVE-2026-50084 (CVSS 9.6), Mobile App CVE-2026-50091 (CVSS 9.1)** — PT-Security dbugs 2026-06-12; IoT consumer-home scope, out-of-Watchtower-core, tracked here only because the IAM/SSO Gateway hits a perfect-10 (mass smart-home OAuth landscape).

**Amasty Order Attributes (Magento module) CVE-2026-53787 (CVSS 9.8) + JMESPath.Php CVE-2026-54133 (CVSS 9.8)** — PT-Security dbugs 2026-06-12; the Magento-extension CVSS 9.8 cadence remains steady (joins Mirasvit Full Page Cache Warmer KEV add from 2026-06-03 — MEMORY 2026-06-08), continue treating Magento ecosystem as 14-day patch SLA on the extension fleet.

**Yarbo Mobile Application CVE-2026-10557 (CVSS 9.8)** — PT-Security dbugs 2026-06-12; consumer-mobile scope, out of Watchtower core; tracked for visibility.

**7-Zip GHSL-2026-115 → GHSL-2026-122 + GHSL-2026-140 (CVE-2026-48095) heap buffer write overflow + multi-CVE memory-access-violation batch (GitHub Security Lab, Jaroslav Lobačevski)** — Continuation of 7-Zip's recurring memory-safety advisory cycle; relevant to any service-side automation that decompresses untrusted .7z payloads (mail-scanning gateways, malware-sandbox feeders, archive-handling SaaS).

**Chatwoot GHSL-2026-059 SQL injection (Man Yue Mo / GitHub Security Lab) + Apache Doris CVE-2024-48019 REST API arbitrary file read** — GitHub Security Lab disclosures landing alongside the 7-Zip batch; Chatwoot is a widely deployed open-source customer-support helpdesk; Apache Doris is an analytics-DB used in modern data stacks.

**npm `tar` path-traversal CVE-2026-31802 — symlink extract → arbitrary file overwrite (Recorded-texteditor120 PoC published)** — Updated PoC repository on github.com/0xMarcio/cve; npm `tar` is transitively present in millions of Node.js dependency trees; await mainstream advisory + verify patched-tar version pinned in your lock files.

**Netlogon CVE-2026-41089 PoC update — additional implementations 10h ago on 0xMarcio/cve tracker, post-MEMORY-2026-06-02 (already NEWS) + Microsoft June Patch Tuesday (Watchtower 2026-06-12 NOTED)** — Continuation of the Netlogon CLDAP stack BoF tracking; PoC maturity tick warrants holding it on the Patch-Tuesday-promotion list, no material-change UPDATE yet but escalate if a Metasploit module lands.

**Anthropic Microsoft / IBM / AT&T "hack cover-up" allegations (SecurityWeek "In Other News" 2026-06-12)** — Industry-disclosure-ethics calibration item; not a CVE / advisory; tracked for narrative-watch.

**Conti Ukrainian operator pleads guilty (extradited from Ireland) — conspiracy charges in the Conti ransomware-as-a-service case (BleepingComputer 2026-06-12)** — Operational law-enforcement item; joins the AudiA6 / Sniper Dz cluster for this week's anti-cybercrime momentum.

**Novo Nordisk clinical-trial data breach (BleepingComputer 2026-06-12)** — Insulin-manufacturer breach with patient information from specific clinical trials affected; scope not yet quantified; no CVE.

**OnyxC2 stealer malware tracking 200+ applications ($250/month, encrypted payloads + DLL sideloading + in-memory execution)** — SecurityWeek 2026-06-12 commercial-stealer profile; not a CVE; relevant calibration for SOC content tuning against modern stealer-as-a-service families.

**Microsoft fixes BitLocker recovery-mode boot bug + WUSA installer network-share install bug (June 2026 Patch Tuesday follow-on)** — Quality-of-life patches landing alongside the 206-CVE batch; not security-impactful directly, noted for Patch-Tuesday operations awareness.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ direct fetch 403 — KEV add for CVE-2026-10520 picked up via BleepingComputer + SecurityWeek relay |
| Vendor advisories | rapid7.com, fortinet.com/blog/threat-research, blog.cloudflare.com/tag/security, msrc.microsoft.com/blog | ✅ / ⚠️ — msrc empty; cloudflare silent for 06-12/13 |
| Research / OSINT | schneier.com, securitylab.github.com, opencve.io, dbugs.ptsecurity.com, kb.cert.org/vuls, avleonov.com, github.com/0xMarcio/cve, github.com/search?q=CVE | ✅ |
| Disclosure lists | seclists.org/fulldisclosure (degraded — only 06-04→06-08 content), openwall oss-security (Squid + Portainer + Crypt::PBKDF2 today) | ⚠️ |
| Tier-2 Russian / Ukrainian | habr.com/ru/companies/tomhunter/articles (silent since 2026-03-06), teletype.in/@cyberok (silent since 2026-02-04), cert.gov.ua (empty content) | ⚠️ all three persistent silence |
| JS-required degraded | hackerone.com/hacktivity, cve.mitre.org, cve.org, attackerkb.com, bugcrowd.com/disclosures, packetstormsecurity.com, projectzero.google | ⚠️ / ❌ |

**Errors:** cisa.gov + cisa.gov/known-exploited-vulnerabilities-catalog persistent 403; attackerkb.com 403; bugcrowd.com/disclosures 404; hackerone.com/hacktivity + cve.mitre.org + cve.org JS-required; packetstormsecurity.com no useful content; msrc.microsoft.com/blog no useful content.
**CISA KEV:** CVE-2026-10520 (Ivanti Sentry) added 2026-06-11 — first BOD 26-04 invocation with 3-day FCEB deadline of 2026-06-14; surfaced via BleepingComputer + SecurityWeek relay because cisa.gov direct fetch continues to return 403.

---

*Watchtower vulnerability-researcher | Cycle: 2026-06-13/night | Next: 2026-06-14/night*
