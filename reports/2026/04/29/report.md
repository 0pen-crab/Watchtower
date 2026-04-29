# Watchtower Night Report — 2026-04-29
**Cycle:** Night | **Generated:** 2026-04-29 00:06 UTC (2026-04-29T00:06:50Z)
**Sources checked:** 20/30 | **CISA KEV new additions:** 0 (no additions since 2026-04-24)

---

## 🔴 CRITICAL

### CVE-2026-42208 — LiteLLM Pre-Auth SQL Injection Actively Exploited Within 36 Hours of Disclosure (CVSS Critical)
**Product:** LiteLLM proxy < 1.83.7 | **CVE:** CVE-2026-42208 | **Status:** Patched (1.83.7) — Active Exploitation Confirmed

LiteLLM's API-key verification step concatenated the supplied `Authorization` header straight into a SQL query, giving any unauthenticated network client a pre-auth injection sink against any LLM API route. The injection lets the attacker enumerate and dump the LiteLLM database — virtual keys, master keys, and the env/config secrets used to broker requests to OpenAI, Anthropic, AWS Bedrock, and other upstream providers. Sysdig confirmed exploitation began **roughly 36 hours after the bug was publicly disclosed on 2026-04-24**: phase one was targeted, deliberate enumeration of the secrets tables; phase two saw the actors pivot to fresh IPs and refine payloads using intel from phase one. The patch (1.83.7) replaces concatenation with parameterised queries.

**Timeline:** Public disclosure 2026-04-24 → fix in 1.83.7 same-day → first observed exploitation ~2026-04-26 → Sysdig public write-up and BleepingComputer coverage 2026-04-28.

**Why it matters:** LiteLLM is the de-facto enterprise gateway for routing model traffic through a single API contract, which means a compromised LiteLLM instance hands the attacker a working set of OpenAI/Anthropic/Bedrock credentials in one request — a high-leverage SaaS-billing and data-exfil primitive without ever needing to touch the upstream model providers directly. Any internet-reachable LiteLLM proxy is now in active exploitation; even internal LiteLLM brokers are exposed to anyone who can reach the listener (CI runners, partner networks, dev tunnels). This continues the AI-tooling RCE/SQLi pattern (Langflow, LMDeploy, FastGPT, n8n, SGLang) where the AI control plane is the new edge.

**Discovered by:** Initially disclosed by the LiteLLM project on 2026-04-24; exploitation analysis by **Sysdig Threat Research** (Stefano Chierici and team).

**Mitigation:**
- Upgrade every LiteLLM proxy to **1.83.7** immediately; restart the process so cached config is reloaded.
- Where upgrade is delayed, set `disable_error_logs: true` in the LiteLLM config (vendor-recommended interim mitigation that suppresses the leaky error responses).
- **Treat all virtual keys, master keys, and provider secrets stored in any LiteLLM instance reachable since 2026-04-24 as compromised** — rotate OpenAI / Anthropic / Bedrock / Azure / Vertex API keys held by LiteLLM and re-issue virtual keys to consumers.
- Block inbound to LiteLLM listener from non-trusted networks; place behind authenticated reverse proxy with WAF SQLi rules at minimum.
- Hunt SIEM/WAF logs for `Authorization:` headers containing SQL syntax (`' OR `, `UNION SELECT`, `;--`, hex-encoded payloads) since 2026-04-24 against LiteLLM hostnames.
- Review OpenAI/Anthropic/Bedrock audit logs for unexpected calls or new API key creations from the LiteLLM time window.

**Sources:** [BleepingComputer — Hackers are exploiting a critical LiteLLM pre-auth SQLi flaw](https://www.bleepingcomputer.com/news/security/hackers-are-exploiting-a-critical-litellm-pre-auth-sqli-flaw/) | [Sysdig Threat Research](https://sysdig.com/blog)

---

### CVE-2026-3854 — GitHub Enterprise Server / GitHub.com Authenticated-Push RCE (CVSS 8.7)
**Product:** GitHub.com, GitHub Enterprise Cloud (incl. Data Residency / EMU), GitHub Enterprise Server 3.14.x – 3.20.x | **CVE:** CVE-2026-3854 | **Status:** Patched — GitHub.com fixed within 2 hours; GHE patches available across 3.14–3.20 release lines

Wiz disclosed a command-injection chain that turns a single authenticated `git push` into RCE on the GitHub backend. User-supplied push-option values were not sanitised before being concatenated into internal service headers; semicolon delimiters allow injection of arbitrary metadata fields. Exploitation chains three payloads: (1) injecting a non-production `rails_env` to bypass sandbox protections, (2) injecting `custom_hooks_dir` to redirect hook execution, (3) injecting `repo_pre_receive_hooks` with crafted entries that trigger path traversal and ultimately execute arbitrary commands as the `git` system user — full filesystem access and visibility into internal service config. Approximately **88% of GitHub Enterprise Server instances were vulnerable at public disclosure**.

**Timeline:** Discovered by Wiz 2026-03-04 → reported to GitHub Security same week → GitHub.com patched within 2 hours of validation → GHES patches released across 3.14.25 / 3.15.20 / 3.16.16 / 3.17.13 / 3.18.8 / 3.19.4 / 3.20.0 → coordinated public disclosure 2026-04-28.

**Why it matters:** GitHub is the canonical source of trust for code, CI secrets, and deployment automation. A compromised GHE instance is one ssh-key dump away from owning every internal service — secrets in repo settings, code-signing keys for downstream artefacts, OIDC trust into cloud accounts, and (because the attacker becomes the `git` user) the ability to forge pushes that look exactly like legitimate developer activity. Public-facing GHE endpoints are common at large enterprises and are exactly the topology Wiz analysed. The "auth required" gating is a thin barrier — any user with push to a single repo on a multi-tenant GHE owns the box. Worst case: a self-hosted GHE running an old 3.16.x with internet-facing SSH.

**Discovered by:** Wiz Research (Google-owned cloud security firm). GitHub Engineering published the corroborating internal incident write-up on 2026-04-28.

**Mitigation:**
- Upgrade GitHub Enterprise Server to the latest patch on your release line **today**: 3.14.25, 3.15.20, 3.16.16, 3.17.13, 3.18.8, 3.19.4, or 3.20.0+. Re-run patch verification after upgrade — `ghe-version` and confirm `git push` advertised options no longer accept stray semicolons.
- For GitHub Enterprise Cloud and GitHub.com, no customer action required — GitHub patched the multi-tenant fleet on 2026-03-04.
- Review GHE audit logs for unusual `pre-receive` hook config changes, new `custom_hooks_dir` entries, or `git` user shell sessions in the discovery window (any time before your upgrade).
- Hunt: Wiz published exploit indicators including unexpected files under `/data/repositories/.../custom_hooks` and unexpected `git` user processes running shell binaries; correlate with `git push` traffic in HTTPS/SSH access logs.
- Treat any GHE secret (Actions secrets, OIDC trust policies, deploy keys, signed-commit keys) on a previously-vulnerable instance as suspect — rotate where blast radius warrants.

**Sources:** [The Hacker News — Researchers Discover Critical GitHub CVE-2026-3854 RCE Flaw](https://thehackernews.com/2026/04/researchers-discover-critical-github.html) | [GitHub Engineering — Securing the git push pipeline](https://github.blog/security/) | [Wiz — Disclosure of CVE-2026-3854](https://www.wiz.io/blog)

---

## 🟠 HIGH

### CVE-2026-25874 — Hugging Face LeRobot Unauthenticated RCE via Pickle Deserialization (CVSS 9.3, **UNPATCHED**)
**Product:** Hugging Face LeRobot ≤ 0.4.3 | **CVE:** CVE-2026-25874 | **CVSS:** 9.3 | **First reported:** 2026-04-28

LeRobot's async-inference pipeline deserialises gRPC payloads with `pickle.loads()` over **unauthenticated, plaintext gRPC channels** (no TLS, no client cert, no token). An attacker with TCP reach to the PolicyServer port can ship a crafted pickle through `SendPolicyInstructions`, `SendObservations`, or `GetActions` and gain arbitrary code execution as the user running the server or client. **No fix is shipped today** — the vendor plans to land a remediation in version 0.6.0. The bug was originally reported by `chenpinji` in December 2025; VulnCheck (Valentin Lobstein) published the public write-up 2026-04-28 after a four-month vendor delay.

**Mitigation:**
- Network-isolate every LeRobot PolicyServer behind a strict firewall — only operator workstations and trusted automation should reach it.
- Run LeRobot inference inside a hardened container (no host SSH key mount, no AWS credentials, no GitHub token) so an RCE has minimal lateral value until 0.6.0 ships.
- Where LeRobot integrates with physical actuators, add an out-of-band kill switch — RCE on a robot controller is a physical-safety hazard, not just a data-confidentiality one.
- Monitor PolicyServer port for connections from unexpected sources; alert on Python `pickle.loads`-derived stack traces in process telemetry.
- If LeRobot is not strictly required, decommission until 0.6.0 lands.

**Sources:** [The Hacker News — Critical Unpatched Flaw Leaves Hugging Face LeRobot Open to Unauthenticated RCE](https://thehackernews.com/2026/04/critical-cve-2026-25874-leaves-hugging.html) | [VulnCheck Disclosure — CVE-2026-25874](https://vulncheck.com/blog)

---

### CoreDNS TSIG Authentication Bypass Bundle — CVE-2026-35579, CVE-2026-33190, CVE-2026-33489 (CVSS 7.5)
**Product:** CoreDNS < 1.14.3 | **CVEs:** CVE-2026-35579, CVE-2026-33190, CVE-2026-33489, CVE-2026-32936, CVE-2026-32934 | **CVSS:** 7.5 (lead) | **First reported:** 2026-04-28

CoreDNS shipped five high-severity advisories on 2026-04-28, with the headline issues being TSIG authentication bypasses across modern transports. **CVE-2026-35579 (gRPC + QUIC):** the code checks whether a TSIG key name exists in config but never verifies the HMAC signature, so any request quoting a known key name authenticates regardless of MAC. **CVE-2026-33190 (DoT, DoH, DoH3, DoQ, gRPC):** the response writer hardcodes TSIG status to `nil`, treating any TSIG-bearing request as authenticated **even without a valid key name** — total bypass over encrypted DNS transports. **CVE-2026-33489:** zone-transfer ACLs select the wrong stanza via lexicographic compare, enabling subzone exfiltration. **CVE-2026-32936 / 32934:** DoH GET amplification and DoQ stream-backlog exhaustion (DoS). All fixed in **1.14.3**.

**Mitigation:**
- Upgrade every CoreDNS deployment to **1.14.3** — this includes Kubernetes clusters (default DNS), CoreDNS-fronted public resolvers, and any DNS-over-HTTPS edge that uses CoreDNS.
- For Kubernetes specifically: bump the CoreDNS Helm chart / kube-dns image and rolling-restart the CoreDNS DaemonSet. Confirm with `kubectl exec ... -- coredns -version`.
- If upgrade is delayed, **disable gRPC, QUIC, DoH, DoH3, and DoQ transports** on CoreDNS and serve only over UDP/TCP/DoT until patched. TSIG-protected zone transfers must be moved off the affected transports.
- Restrict zone-transfer ACL membership to IP allow-lists at the network layer, not just at the CoreDNS config layer (`view`/`acl` plugins).
- Hunt: review DNS query logs for AXFR/IXFR requests over gRPC/QUIC/DoH/DoH3/DoQ transports from unexpected sources since 2026-04-01; any successful zone transfer to an unknown peer is a confirmed compromise indicator.

**Sources:** [GitHub Advisory — CVE-2026-35579 CoreDNS TSIG bypass on gRPC/QUIC](https://github.com/advisories/GHSA-vp29-5652-4fw9) | [GitHub Advisory — CVE-2026-33190 CoreDNS TSIG bypass on DoT/DoH/DoH3/DoQ/gRPC](https://github.com/advisories/GHSA-qhmp-q7xh-99rh) | [CoreDNS Release 1.14.3](https://github.com/coredns/coredns/releases)

---

## 🔄 Update

### CVE-2026-32202 — Microsoft Confirms Active In-the-Wild Exploitation by APT28 (Threat score 8, previously 7)
**Product:** Windows Shell (all currently supported) | **CVE:** CVE-2026-32202 | **Threat score:** 8 (previously 7) | **First reported:** 2026-04-28

Microsoft revised the CVE-2026-32202 advisory on **2026-04-27** to mark the bug as actively exploited. Akamai's Maor Dahan publicly attributed the exploitation to APT28 (Forest Blizzard / Fancy Bear), who is using the incomplete-patch behaviour described in yesterday's report as part of an LNK-based attack chain against Ukraine and EU targets. The chain combines CVE-2026-32202 with the previously-patched CVE-2026-21510 + CVE-2026-21513 (MSHTML) to bypass SmartScreen and coerce NTLMv2 hashes via SMB.

**Why this is an update vs. last entry (2026-04-28):** yesterday's entry framed CVE-2026-32202 as "no active exploitation reported yet — weaponisation is a matter of time." Today Microsoft explicitly updated the advisory to "exploitation detected" — that's the trigger for promoting the urgency tier and re-broadcasting to detection teams. Akamai also published the threat-actor attribution to APT28.

**Mitigation:**
- Re-run April 2026 Patch Tuesday compliance check across all Windows estates — any host without the April cumulative update is exposed to a confirmed-in-the-wild APT28 chain. The February patch is **not** sufficient (incomplete fix).
- Tighten outbound SMB egress (TCP 445, 139) to internal subnets only; require SMB signing and NTLMv2 only on all clients.
- Prioritise patching for: Windows hosts at EU/NATO entities, hosts with Ukraine-related data, and any host of a user with diplomatic / defence / energy-sector relationships.
- Hunt SIEM for outbound TCP 445 connections from workstations to non-internal IPs since 2026-02-01 — any historical SMB to an external IP with CVE-2026-32202-class LNK payloads in the user's downloaded folder = potential APT28 compromise.
- Update detection content to include APT28 LNK/MSHTML chain TTPs (Akamai indicators).

**Sources:** [The Hacker News — Microsoft Confirms Active Exploitation of Windows Shell CVE-2026-32202](https://thehackernews.com/2026/04/microsoft-confirms-active-exploitation.html) | [MSRC Advisory — CVE-2026-32202](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-32202) | [Akamai — APT28 LNK Coercion Chain](https://www.akamai.com/blog/security-research)

---

## 📋 Noted / Monitoring

**Microsoft Entra ID — Agent ID Administrator role privilege escalation (Silverfort, patched 2026-04-09)** — Silverfort (Noa Ariel) disclosed that the Entra ID "Agent ID Administrator" role granted ownership-takeover of *arbitrary* service principals (not just AI-agent identities), enabling attackers with that role to add their own credentials to any service principal and authenticate as it. Microsoft patched 2026-04-09; post-fix attempts return Forbidden. No active exploitation reported. Disclosed publicly 2026-04-28.

**PhantomRPC — local privilege escalation via fake RPC servers (Kaspersky / Haidar Kabibo, no patch)** — Local attackers can deploy a fake RPC server impersonating a disabled Windows service; when a privileged process contacts it, the malicious server escalates to System via impersonation. Microsoft classified moderate-severity and **declined to patch**. Out of scope (no remote vector) but worth tracking for defenders building EDR rules — any process exposing an RPC endpoint that shouldn't be is suspicious.

**GitPython command injection bypass — GHSA-rpm5-65cw-6hj4 (CVSS 8.8, fixed 3.1.47)** — Underscore-form Python kwargs (`upload_pack=`, `receive_pack=`) bypass GitPython's safety check because dashification happens after validation. Affects any Python app passing user-supplied dicts as `**kwargs` to `Repo.clone_from`/`Remote.fetch`/`pull`/`push`. CI/CD platforms and self-hosted git mirrors that wrap GitPython are the realistic blast radius. Fix released 2026-04-22.

**CVE-2026-7241 — Totolink A8000RU consumer router unauth RCE (CVSS 10.0, 2026-04-28)** — Critical RCE flaw in consumer-grade router firmware. Already a Mirai/IoT-botnet candidate (compare to CVE-2026-7037 covered 2026-04-27). Out of corporate scope for most readers; tracked for ISPs and IoT teams.

**CVE-2026-24178 / CVE-2026-24186 — NVIDIA NVFlare Dashboard auth bypass (9.8) and FOBS deserialisation RCE (8.8)** — Federated learning framework vulnerabilities published to OpenCVE 2026-04-28. NVFlare is niche (used by hospitals/research consortia for federated ML), but the unauth-bypass + RCE pairing on a single product is the FastGPT / Langflow / LMDeploy template — promote to News if exploitation appears.

**Spring AI CVE-2026-40978 (CVSS 8.8) and CVE-2026-40980 (CVSS 6.5), 2026-04-28** — Two new Spring AI advisories. Watching for vendor write-up; if these touch the actuator endpoints exposed by the CVE-2026-40976 Spring Boot bypass we covered yesterday, we may have a stacked Spring problem. Promote next cycle when details land.

**Vimeo / Anodot ShinyHunters breach (data exposure, 2026-04-28)** — ShinyHunters used stolen Anodot authentication tokens to pivot into customers' Snowflake / BigQuery instances; Vimeo confirmed video metadata, titles, and some customer email addresses exposed. No video content, credentials, or payment data lost. Not a CVE but a SaaS-supply-chain pattern worth flagging — any organisation using Anodot should audit data-warehouse access logs from the breach window.

**Itron utility-vendor breach (preliminary, 2026-04-26 disclosure)** — Energy/water meter manufacturer disclosed unauthorised access to internal IT detected 2026-04-13. No attribution, no data details, no ransomware claim, no operational impact. Tracked for OT-supply-chain implications; promote if technical detail emerges.

**Germany suspects Russia behind Signal phishing of top officials (2026-04-28)** — German federal prosecutors investigating sustained phishing of Signal accounts belonging to senior officials since February 2026. Operational/political signal rather than a CVE; relevant for any high-value-target user authenticating via Signal in the enterprise.

**ClickFix campaign disguised as Claude installer (Rapid7 ThreatCommand, 2026-04-25)** — ClickFix-style social engineering luring users to "install Claude" pages that actually run a PowerShell payload. Confirms the AI-installer phishing trend (mirrors fake Cursor / Windsurf installers). Block known C2 IOCs from Rapid7 advisory; warn developer population.

**VECT 2.0 ransomware acts as wiper for files >131KB (BleepingComputer, 2026-04-28)** — VECT 2.0 has a fatal flaw in its encryption routine that destroys any file over 131KB on Windows / Linux / ESXi targets. **Operationally significant**: do not pay the ransom — files are unrecoverable. Push the IOCs (sample hashes) into AV signatures and EDR blocklists.

**108 malicious Chrome extensions (April 2026)** — Browser extension campaign harvested credentials from 20,000 users across multiple platforms. Client-side, out of corporate-perimeter scope but worth noting if your extension allow-list is loose.

**Anthropic Mythos commentary (Schneier, SecurityWeek, 2026-04-28)** — Industry commentary on Anthropic's recently announced Mythos AI-security model that autonomously discovers software vulnerabilities. Strategic-context piece, not actionable today; flagged because the next 90 days will see "Mythos found X" advisories appearing across vendor blogs.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com, schneier.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (403 — used THN/BC/SecurityWeek for KEV mirror) |
| Vendor advisories | msrc.microsoft.com/blog, fortinet.com/blog/threat-research, spring.io/security | ⚠️ (msrc nav-only; Spring direct) |
| Research / OSINT | securitylab.github.com (github.blog/security), seclists.org/fulldisclosure, kb.cert.org/vuls, avleonov.com, projectzero.google | ✅ / ⚠️ (fulldisclosure no posts since Apr 14; projectzero.google last post Mar 5) |
| CVE databases | app.opencve.io, dbugs.ptsecurity.com, github.com/0xMarcio/cve, github.com/search, github.com/advisories | ✅ |
| Cloud / vendor blogs | blog.cloudflare.com/tag/security, rapid7.com | ✅ / ⚠️ (Cloudflare last sec post Apr 14) |
| Bug bounty | hackerone.com/hacktivity, bugcrowd.com/disclosures, attackerkb.com | ❌ (JS / 404 / 403) |
| Russian / non-English | habr.com/ru/companies/tomhunter, teletype.in/@cyberok, cert.gov.ua | ⚠️ (no recent / empty extract) |
| Authoritative DBs | nvd.nist.gov, cve.org, cve.mitre.org | ⚠️ / ❌ (no extract / JS) |
| Research labs | googleprojectzero.blogspot.com (now projectzero.google), packetstormsecurity.com (now packetstorm.news) | ⚠️ (redirects, stats only) |

**Errors:** cisa.gov + cisa.gov/known-exploited-vulnerabilities-catalog (403); attackerkb.com (403); bugcrowd.com/disclosures (404); hackerone.com/hacktivity, cve.org, cve.mitre.org (JS); packetstormsecurity.com→packetstorm.news (stats-only); msrc.microsoft.com/blog (nav-only); googleprojectzero.blogspot.com (redirect).
**CISA KEV:** No new additions since 2026-04-24 (Samsung MagicINFO, SimpleHelp x2, D-Link DIR-823X). No federal patch deadlines elapsing 2026-04-29 in the watched set.

---

*Watchtower vulnerability-researcher | Cycle: 2026-04-29/night | Next: 2026-04-30/night*
