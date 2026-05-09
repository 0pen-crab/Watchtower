# Watchtower Night Report — 2026-05-09
**Cycle:** Night | **Generated:** 2026-05-09 00:30 UTC (2026-05-09T00:30:00Z)
**Sources checked:** 21/30 | **CISA KEV total:** unreachable via WebFetch | **New KEV additions:** 1 (CVE-2026-6973 Ivanti EPMM, fed deadline 2026-05-10)

---

## 🔴 CRITICAL

### ClaudeBleed — Claude Chrome Extension multi-app takeover (LayerX, partially patched)
**Product:** Anthropic Claude for Chrome browser extension | **CVE:** Not yet assigned | **Status:** Active research, partial patch shipped, root cause unfixed

LayerX disclosed **ClaudeBleed**, a logic flaw in Anthropic's Claude for Chrome extension that allows *any* installed Chrome extension to invoke a content script and issue commands to Claude because the extension trusts the page **origin** (claude.ai) rather than the **execution context**. Attack outcomes include remote prompt injection, forged user confirmations via repeated messaging, DOM manipulation to bypass the in-extension confirmation UI, and silent data exfiltration via the Claude agent from any application Claude is connected to (Gmail, GitHub, Google Drive, Notion). Anthropic shipped a partial fix that prevents extensions in the standard execution mode from issuing remote commands, but LayerX confirmed that an attacker can bypass the fix by switching to **privileged mode** without notifying the user — the underlying class confusion remains.

**Timeline:** LayerX research → Anthropic notified → partial patch shipped (date not specified) → public disclosure 2026-05-08 with bypass for the partial fix.

**Why it matters:** This is the **fourth** AI-agent-config / AI-agent-control attack surface disclosed in 9 days (Mini Shai-Hulud SessionStart 04-30 → Gemini CLI CVSS 10 on 05-01 → Adversa TrustFall + Claude Code MCP-hijack on 05-07 → ClaudeBleed on 05-08). For an enterprise running 100k+ endpoints, every Chrome user with the Claude extension installed is a foothold for credential and document theft from any app Claude is connected to — and the partial patch doesn't close it. Treat the Claude Chrome extension as **prerelease** in your browser-extension allow-list policy until a full architectural fix ships.

**Discovered by:** LayerX (Or Eshed et al.)

**Mitigation:**
- Block or remove the Claude for Chrome extension from managed browser fleets until full fix lands.
- For non-managed users, audit the **other** extensions that have permission to inject content scripts on `claude.ai` — any of them can drive the Claude agent.
- Tighten Claude's connector scopes (Gmail / Drive / GitHub / Notion) to least privilege; rotate connector tokens after compromise discovery.
- Add detection for unusual Claude-driven outbound activity (mass mail send, document sharing) in DLP and email-gateway telemetry.

**Sources:** [SecurityWeek — Claude Chrome extension AI agent takeover](https://www.securityweek.com/vulnerability-in-claude-extension-for-chrome-exposes-ai-agent-to-takeover/) | [LayerX research blog](https://layerx.com/blog) (referenced in coverage)

---

### Polish ABW reports ICS breaches at five water-treatment plants — APT28 / APT29 / UNC1151
**Product:** Industrial Control Systems (water-treatment SCADA) | **CVE:** None — operational compromise | **Status:** National-security agency confirmed, attribution to Russia/Belarus state actors

Poland's Internal Security Agency (ABW) published a report confirming intrusions at **five Polish water-treatment facilities** (Jabłonna Lacka, Szczytno, Małdyty, Tolkmicko, Sierakowo) over 2024–2025. Attackers obtained access sufficient to **modify equipment operational parameters**, creating direct risk to operational continuity and public water supply. ABW attributed activity to Russian APT28 and APT29, plus Belarusian-aligned UNC1151, noting that hacktivist personas in this space frequently front for foreign government operations. Initial access was obtained via **weak password policies** and **systems exposed directly to the internet** — not novel zero-days. ABW disclosed an August 2025 incident that nearly caused a city to lose water supply.

**Timeline:** Intrusions span 2024 → 2025 → August 2025 near-water-loss incident → ABW public report 2026-05-08.

**Why it matters:** Two years of nation-state ICS access on critical-infrastructure facilities reaching the parameter-modification threshold is the kind of pre-positioning that turns into actual sabotage during a geopolitical escalation. For US/EU water utilities, this is the third public disclosure in 2026 of state-aligned ICS access (after the broader EU-wide warnings) and reinforces that pre-positioning campaigns continue against utility OT. The attack vectors (weak passwords, direct internet exposure) are remediable today — there is no "wait for the patch" excuse. Expand ABW's scope warning beyond water: **wastewater treatment, waste incineration, and other municipal utility ICS** were identified as adjacent targets.

**Discovered by:** Agencja Bezpieczeństwa Wewnętrznego (ABW) — Poland's Internal Security Agency

**Mitigation:**
- Inventory all ICS / OT systems with internet-reachable HMI / engineering-workstation interfaces; segment behind VPN with phishing-resistant MFA.
- Rotate any operator credentials still using shared / weak passwords; enforce per-operator accounts with auditable session logs.
- Hunt for APT28 / APT29 / UNC1151 IOCs across the OT DMZ — overlap with the Polish incident set is plausible for any utility with legacy remote-maintenance access.
- Coordinate with national CERT (CISA / NCSC equivalent) for sector-specific IOC sharing on the ABW campaign.

**Sources:** [SecurityWeek — Polish ICS breaches at five water treatment plants](https://www.securityweek.com/polish-security-agency-reports-ics-breaches-at-five-water-treatment-plants/) | [ABW public statement (Polish)](https://www.gov.pl/web/abw)

---

### OpenClaw — 9-CVE batch with 3 critical (auth bypass, LPE, CDP exposure) — VulnCheck
**Product:** OpenClaw browser-automation platform (used by AI agent vendors) | **CVE:** CVE-2026-43575 / 43576 / 43577 / 43578 / 43579 / 43580 / 43581 / 43582 / 43583 | **Status:** Patched in 2026.4.10 / 2026.4.14, batch published 2026-05-06

VulnCheck published **nine OpenClaw vulnerabilities** in a single batch on 2026-05-06, three of which are **Critical**:
- **CVE-2026-43575** — Authentication Bypass in Sandbox noVNC Helper Route (affects 2026.2.21 < 2026.4.10).
- **CVE-2026-43578** — Privilege Escalation via Missed Async Exec Completion Events in Heartbeat Owner Downgrade (affects 2026.3.31 < 2026.4.10).
- **CVE-2026-43581** — Chrome DevTools Protocol Exposure via Overly Broad CDP Relay Binding (affects < 2026.4.10).
The remaining six cover SSRF (CDP /json/version, DNS rebinding), arbitrary file read via browser-interaction routes, insufficient access control on Nostr profile mutation routes, navigation-guard gaps, and group tool-policy context loss in delivery-queue recovery. The CDP-relay exposure (CVE-2026-43581) chains naturally with the noVNC auth bypass (CVE-2026-43575) and arbitrary file read (CVE-2026-43577) for full sandbox escape.

**Timeline:** OpenClaw 2026.4.10 patched 04-29 → 2026.4.14 patched 05-04 → coordinated VulnCheck disclosure 2026-05-06.

**Why it matters:** OpenClaw is the headless-browser substrate behind a growing number of AI-agent vendors and security tooling. Any environment running OpenClaw < 2026.4.10 can be remotely owned via the auth-bypass + CDP-relay chain, and the privilege-escalation (43578) makes a low-privileged local user root-equivalent inside the OpenClaw worker. **Per our internal MEMORY note, our own platform was on 2026.2.21-2 as of 2026-03-30** — this batch retroactively confirms that everything in the un-upgraded fleet is exposed to the noVNC auth bypass plus CDP exposure. Verify current OpenClaw version first before any other action today.

**Discovered by:** VulnCheck (researcher attribution not in advisory; batch coordinated by VulnCheck)

**Mitigation:**
- `openclaw update` to ≥ 2026.4.14 immediately; do not delay past today on any internet-reachable instance.
- Verify CDP-relay binding restrictions after upgrade (CVE-2026-43581 fix tightens to localhost / explicit allowlist).
- Audit any noVNC-helper sessions that occurred between 2026.2.21 and 2026.4.10 for unexpected commands / file-read activity (CVE-2026-43575 + 43577).
- For multi-tenant OpenClaw deployments, confirm Nostr profile-mutation routes (CVE-2026-43579) are rejecting cross-tenant writes after upgrade.

**Sources:** [VulnCheck advisories — OpenClaw batch](https://www.vulncheck.com/advisories) | [OpenClaw 2026.4.14 release notes](https://github.com/openclaw/openclaw/releases)

---

## 🟠 HIGH

### Open WebUI CVE-2026-44551 — LDAP empty-password authentication bypass (CVSS 9.1)
**Product:** Open WebUI (self-hosted ChatGPT-style AI front-end) | **CVE:** CVE-2026-44551 | **CVSS:** 9.1 | **First reported:** 2026-05-08

The LDAP authentication endpoint in Open WebUI ≤ 0.8.12 fails to validate that the password field is non-empty before binding to the LDAP server. Per RFC 4513, default OpenLDAP and several Active Directory configurations return success for **unauthenticated simple binds** with empty password — meaning a single `POST /api/v1/auths/ldap` with a valid username and empty password yields a full session token for the targeted user. No prior authentication, no MFA prompt, no enumeration required beyond knowing a username (typically email). Patched in **0.9.0**. CWE-287.

**Why it matters:** Open WebUI is the most widely deployed self-hosted ChatGPT-style front-end against Ollama / vLLM / TGI / hosted-API backends, with hundreds of thousands of deployments per Shodan / Censys / GitHub-stars proxies. Any internal Open WebUI integrated with corporate LDAP / AD using default-config OpenLDAP or AD un-authenticated-bind acceptance is a single POST away from full SSO impersonation. Combined with the prevailing self-hosted-AI default-no-auth posture (per Intruder Labs' 2026-05-05 finding), this lands in fleets where a successful LDAP-relayed compromise pivots into the AI provider tokens behind Open WebUI.

**Mitigation:**
- Upgrade Open WebUI to **0.9.0** or later immediately.
- On the LDAP / AD side, set `disallow_bind_anon` (OpenLDAP) and disable `LDAP_PERMIT_UNAUTHENTICATED_BIND` (AD policy) — defense-in-depth against any other application with the same bug.
- Audit Open WebUI authentication logs for prior LDAP-bind attempts with empty password fields back through the install date.
- Rotate any AI provider API keys that were configured per-user via the Open WebUI account hierarchy if you cannot rule out abuse.

**Sources:** [GitHub Security Advisory GHSA-2r4p-jpmg-48f4](https://github.com/advisories/GHSA-2r4p-jpmg-48f4) | [Open WebUI 0.9.0 release](https://github.com/open-webui/open-webui/releases/tag/v0.9.0)

---

### FastGPT CVE-2026-42302 — agent-sandbox unauth RCE on port 8080 (CVSS 9.8)
**Product:** FastGPT AI orchestration platform | **CVE:** CVE-2026-42302 | **CVSS:** 9.8 | **First reported:** 2026-05-08

The FastGPT agent-sandbox component exposes an unauthenticated remote-code-execution path on **port 8080** because authentication is **disabled by default** on that endpoint. Any attacker reaching the sandbox port can submit an agent-execution payload that runs arbitrary code inside the sandbox container — and from there pivot via the standard container-escape primitives that have been disclosed against agent sandboxes through 2026 (capability-leak, host-mount, runc bugs).

This is **distinct from the prior FastGPT NoSQL-injection auth-bypass we covered on 2026-04-18** — different code path, different CVE, same vendor. FastGPT now has two unauthenticated-impact CVEs in 30 days; the project's authorisation-handling code quality is becoming a recurring concern.

**Why it matters:** FastGPT is widely deployed in self-hosted AI environments alongside Ollama, Open WebUI, and vLLM — same default-no-auth posture that Intruder Labs flagged across 1M exposed AI services on 2026-05-05. Any FastGPT instance on a publicly-routable IP with port 8080 reachable is one HTTP request from RCE-as-container-user.

**Mitigation:**
- Upgrade FastGPT to the patched release (vendor advisory pending; track project release notes).
- Until patched, network-restrict port 8080 to the orchestration backend only — do not expose externally.
- Verify all FastGPT deployments behind reverse proxy with auth header injection; the agent-sandbox endpoint should not be publicly reachable under any circumstances.
- Hunt for `/sandbox/exec` (or equivalent) requests in FastGPT access logs over the past 30 days.

**Sources:** [OpenCVE — CVE-2026-42302](https://app.opencve.io/cve/CVE-2026-42302) | [FastGPT GitHub](https://github.com/labring/FastGPT)

---

### Braintrust SaaS-token theft — third AI-vendor-as-credential-warehouse incident in 14 days
**Product:** Braintrust AI evaluation / observability platform | **CVE:** None (operational breach) | **CVSS:** N/A | **First reported:** 2026-05-08

Braintrust, a SaaS AI-evaluation and observability platform, disclosed that an attacker accessed an internal AWS account used by their systems and harvested customer-stored **org-level AI provider keys** (OpenAI, Anthropic, etc.). Confirmed customer impact: at least one customer (with three additional customers reporting suspicious AI-provider usage spikes). Notably, Braintrust customers include **Box, Cloudflare, Dropbox, Notion, Ramp, and Stripe** per public case studies — implying an attacker who pivots through a stolen Braintrust-stored AI provider key is operating against frontier-model usage within those customers' organisations.

**Timeline:** 2026-05-04 incident discovered after a customer reported suspicious behavior → 2026-05-05 customer notification email → 2026-05-08 public reporting.

**Why it matters:** This is the **third SaaS-vendor-token theft pattern** in 14 days (Anodot 2026-05-07 → DigiCert support-channel 2026-05-04 → Braintrust 2026-05-08). The shared lesson: any SaaS data-monitoring / observability / AI-evaluation vendor that holds customer-issued API tokens with broad read/write scope is a single-point-of-compromise reusable beachhead. AI-evaluation vendors are particularly exposed because they hold the most-privileged keys: org-level Anthropic / OpenAI keys can incur six-figure usage bills in hours and exfiltrate corporate context via prompt leakage.

**Mitigation:**
- Rotate **all** AI provider keys (Anthropic, OpenAI, Cohere, Mistral) that have ever been stored in Braintrust org-level settings, regardless of whether you've been notified.
- Audit AI provider billing dashboards for unexpected usage spikes in the past 30 days; alert thresholds on new high-volume API patterns.
- Inventory other SaaS vendors holding AI provider tokens (Langfuse, Helicone, Portkey, LangSmith, Galileo, Arize) — apply the same Tier-1 supply-chain monitoring you apply to your IDP.
- For new Braintrust integrations going forward, prefer per-project keys with strict spend caps over org-level keys.

**Discovered by:** Customer report → Braintrust internal investigation.

**Sources:** [SecurityWeek — Braintrust prompts API key rotation after data breach](https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/) | [Braintrust customer notification (referenced)](https://www.braintrust.dev)

---

### Postiz-app CVE-2026-42298 — workflow Docker-build RCE via PR (CVSS 10.0)
**Product:** Postiz social-media scheduler | **CVE:** CVE-2026-42298 | **CVSS:** 10.0 | **First reported:** 2026-05-08

A workflow-injection vulnerability in Postiz allows **unauthenticated users** to execute arbitrary code during the project's Docker build process by submitting a malicious pull request with a modified Dockerfile. The CI workflow trusts the PR-submitted Dockerfile during the build stage, and any contributor (including drive-by external contributors) can craft a PR that runs attacker code in the build runner with the workflow's secrets in scope. CVSS 10.0 reflects the unauth attack vector + high impact (CI runner compromise + secret theft).

**Why it matters:** Narrower deployment than the other items today (Postiz is a smaller social-media scheduling tool), but the **vulnerability class** — workflow / CI runner trusting PR-submitted Dockerfile — is repeatable across many open-source projects with the same pattern. If your organisation runs OSS projects with PR-driven CI builds, audit for `pull_request_target` triggers reading PR-modified Dockerfiles or build scripts. Also relevant for any internal fork of Postiz used in production marketing/social workflows.

**Mitigation:**
- Upgrade Postiz to the patched release (vendor advisory pending).
- For self-hosted Postiz forks, disable PR-triggered Docker builds against `pull_request_target` until patched.
- More broadly: audit all GitHub Actions / GitLab CI workflows for `pull_request_target` triggers that reference PR-modified files; switch to `pull_request` (which lacks secret access) wherever possible.
- Rotate any secrets that were available to the Postiz build workflow over the past 60 days.

**Sources:** [OpenCVE — CVE-2026-42298](https://app.opencve.io/cve/CVE-2026-42298) | [Postiz GitHub](https://github.com/gitroomhq/postiz-app)

---

### PamDOORa — Linux PAM-based SSH backdoor sold on Russian forum
**Product:** Linux (any OpenSSH-using distro) | **CVE:** None — post-exploitation tool | **First reported:** 2026-05-08

Flare.io published technical analysis of **PamDOORa**, a Pluggable Authentication Module (PAM)-based post-exploitation backdoor for Linux x86_64. Initially advertised on the Russian-language **Rehub** cybercrime forum on 2026-03-17 by an actor using the persona **"darkworm"** for $1,600, the price was reduced to $900 by 2026-04-09 (suggesting tepid initial uptake or competition from established offerings). Capabilities: harvests credentials of all legitimate users authenticating through compromised systems, provides persistent SSH access via a magic-password-and-port combination, tampers with authentication logs to erase traces, and includes anti-debugging.

**Why it matters:** PamDOORa is **post-exploitation tooling** — not a vulnerability — and requires the adversary to have already obtained root access on the target. No public real-world deployment yet. But the public-tooling pattern (Russian-forum sale → Flare.io analysis → durable IOCs) means this enters the defender-IOC catalogue regardless of current campaign status, and the SSH-magic-password + log-tamper + anti-debug feature set will appear in incidents as adversaries adopt it. Treat as a same-class addition to the existing PAM-rootkit family (Plague, etc.).

**Mitigation:**
- Hunt for unauthorized PAM module additions across Linux fleets — `auth.so` / `pam_unix.so` modifications outside vendor-signed paths are the canonical IOC.
- Add EDR / OSquery rules for unexpected `dlopen` of PAM modules from non-system paths (`/tmp`, `/dev/shm`, `/var/tmp`).
- Alert on `auth.log` / `secure` log-file truncation or unexpected gaps in SSH-auth records.
- Verify that PAM-stack tampering monitoring is in place on internet-facing SSH bastions and developer / CI workstations (which are higher-value supply-chain targets per the Quasar Linux disclosure 2026-05-06).

**Sources:** [The Hacker News — PamDOORa Linux PAM backdoor](https://thehackernews.com/2026/05/new-linux-pamdoora-backdoor-uses-pam.html) | [Flare.io research (referenced in coverage)](https://flare.io/blog)

---

## 🔄 Updates

### 🔄 Ivanti EPMM CVE-2026-6973 — vendor patches released, KEV deadline 2026-05-10 (now: 8 / prev: 8)
**Product:** Ivanti Endpoint Manager Mobile | **CVE:** CVE-2026-6973 | **Status:** Patched 2026-05-08, CISA KEV add 2026-05-08, federal deadline 2026-05-10

We covered this on **2026-05-08** as authenticated-admin RCE actively exploited with KEV-add 2026-05-07 and 2026-05-10 federal deadline. Material developments in the last 24 hours:
- **Vendor patches now available**: Ivanti shipped 12.6.1.1, 12.7.0.1, and 12.8.0.1 on 2026-05-08 (versions ≤12.8.0.0 vulnerable).
- **Federal deadline confirmed at 4 days** from KEV add (instead of standard 21) — CISA explicitly cited "frequent attack vector" language.
- **Ivanti advisory chains the bug to prior 1281/1340 compromise**: customers who **rotated credentials** after January's 1281+1340 incident face significantly reduced exposure to 6973 — confirming our hypothesis that an unauth-bypass companion was already in private hands.
- **Shadowserver tracks 800+ exposed EPMM appliances**; patch-adoption rate not yet known.

**Mitigation update:**
- Apply 12.8.0.1 (or 12.6.1.1 / 12.7.0.1 for older branches) **before midnight 2026-05-10** if you're on a federal contract; before end of 2026-05-11 in commercial environments.
- If EPMM admin credentials existed before January 2025, **rotate** those credentials in addition to patching — the chain assumes prior credential theft from CVE-2026-1281+1340.
- Hunt for unauthorized admin-session tokens issued in the period 2026-04-15 → 2026-05-08 (likely active-exploitation window).

**Sources:** [SecurityWeek — Ivanti patches EPMM zero-day](https://www.securityweek.com/ivanti-patches-epmm-zero-day-exploited-in-targeted-attacks/) | [BleepingComputer — CISA gives feds four days to patch Ivanti](https://www.bleepingcomputer.com/news/security/cisa-gives-feds-four-days-to-patch-ivanti-flaw-exploited-as-zero-day/) | [CISA KEV catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### 🔄 Trellix source-code breach — RansomHouse claims responsibility (now: 6 / prev: 6)
**Product:** Trellix (XDR / EDR vendor) | **Incident** | **Status:** RansomHouse public claim 2026-05-08

We covered the Trellix source-code breach on **2026-05-03 / 05-05** with confirmed unauthorized access. Material development:
- **RansomHouse publicly claimed the breach** on 2026-05-08 with screenshots indicating access to Trellix's appliance management system.
- **Intrusion date stated as 2026-04-17** — over **3 weeks** of access before Trellix's 2026-05-01 disclosure.
- Trellix maintains "no evidence that source code release or distribution process was affected" — but this is necessarily a working assumption pending full integrity verification of the build pipeline.
- RansomHouse has historical operations against Askul (740k records) and uses Mario / MrAgent encryption tooling.

**Why it matters:** Trellix is XDR / EDR vendor for Fortune 100 across 185 countries with 3,500 employees — the exposure window of April 17 → May 1 is the period during which any malicious commit to the source-code repository could have been backdoored. Customers running Trellix XDR / EDR / NDR / Endpoint Security agents released April 17 → present should validate cryptographic signatures against the build pipeline and watch for anomalous agent behavior.

**Mitigation update:**
- Verify Trellix-signed agent integrity (signature chain + bill-of-materials) for releases dated 2026-04-17 onward.
- Monitor Trellix agent network behavior for anomalous outbound / config-pull patterns.
- Track RansomHouse leak-site postings over the next 30 days — a delayed leak is the standard play if Trellix declines to negotiate.

**Sources:** [BleepingComputer — Trellix source code breach claimed by RansomHouse](https://www.bleepingcomputer.com/news/security/trellix-source-code-breach-claimed-by-ransomhouse-hackers/) | [SecurityWeek — Ransomware group claims Trellix hack](https://www.securityweek.com/ransomware-group-takes-credit-for-trellix-hack/)

---

### 🔄 Dirty Frag Linux LPE — CVEs assigned (CVE-2026-43284, CVE-2026-43500) (now: 8 / prev: 8)
**Product:** Linux kernel (Ubuntu, RHEL, CentOS Stream, AlmaLinux, openSUSE, Fedora) | **CVE:** CVE-2026-43284 + CVE-2026-43500 | **Status:** Embargo broken, no patch, public PoC

We covered Dirty Frag on **2026-05-08** as "Universal Linux LPE, embargo broken, public PoC, no CVE". Material developments:
- **Two CVEs assigned**: **CVE-2026-43284** (xfrm/ESP page-cache write) and **CVE-2026-43500** (RxRPC page-cache write) — chains both vulnerabilities to modify protected system files in memory and grant root via a single command.
- **Wiz published technical analysis** (2026-05-08) confirming root-escalation impact across the noted distributions.
- **Cloudflare published mitigation case study** for Copy Fail (2026-05-07) — same general n-day cluster, reusable detection patterns.
- Still **no upstream patch** as of 2026-05-09 — researcher noted "embargo currently broken, no patch or CVE exists" at first publication; CVE assignment is now in place but kernel fixes remain pending.

**Mitigation update:**
- For unpatched fleets, the `modprobe` disable workarounds (`xfrm`, `rxrpc`) remain feasible defense-in-depth; verify against application requirements.
- Add IOCs from the Theori Copy Fail PoC publication (2026-05-05) and dirtyfrag.io to your hunting playbook.
- Subscribe to lkml / `linux-kernel@` for the upcoming patch release; expect coordinated distro releases within 1-2 weeks.

**Sources:** [BleepingComputer — Linux Dirty Frag zero-day with PoC](https://www.bleepingcomputer.com/news/security/new-linux-dirty-frag-zero-day-with-poc-exploit-gives-root-privileges/) | [Wiz blog — Dirty Frag analysis](https://www.wiz.io/blog) | [Cloudflare — Copy Fail mitigation](https://blog.cloudflare.com/copy-fail-linux-vulnerability-mitigation/)

---

## 🟡 MEDIUM

### 5 malicious NuGet packages impersonate Chinese UI libraries — Socket.dev
**Product:** NuGet (.NET ecosystem) | **CVE:** None (supply-chain campaign) | **Published:** 2026-05-06

Socket.dev disclosed five malicious NuGet packages posing as Chinese .NET UI libraries that deploy credential-stealer + cryptocurrency-wallet-theft tooling on developer machines and CI runners that install them. This is the **first significant 2026 NuGet supply-chain wave** — prior 2026 supply-chain campaigns concentrated on npm (Mini Shai-Hulud, intercom-client, axios), PyPI (PyTorch Lightning, ZiChatBot, lightning), RubyGems + Go (BufferZoneCorp). NuGet expansion confirms the **multi-ecosystem playbook** is fully active in .NET-side supply chains as well.

**Mitigation:** Verify any recent NuGet additions to .NET projects against the Socket.dev IOC list; for organisations running .NET CI pipelines, treat NuGet feeds with the same scrutiny applied to npm / PyPI (lockfile-pinning, minimum-release-age, dependency-review-action).

**Sources:** [Socket.dev — 5 malicious NuGet packages](https://socket.dev/blog/5-malicious-nuget-packages-impersonate-chinese-ui-libraries)

---

### electerm CVE-2026-43940 / 43944 — path-traversal arbitrary code execution
**Product:** electerm (cross-platform SSH/SFTP/Telnet terminal client built on Electron) | **CVE:** CVE-2026-43940 + CVE-2026-43944 | **Published:** 2026-05-08

Two vulnerabilities in electerm: **CVE-2026-43940** (path traversal leading to arbitrary code execution) and **CVE-2026-43944** (users can execute dangerous code via link / CLI). electerm is widely used by sysadmins and developers as a graphical SSH / SFTP client across Windows, Mac, and Linux. Combined with the recurring AI-agent-config-as-code pattern (Mini Shai-Hulud, Gemini CLI), this further confirms that **developer / sysadmin desktop tooling is now mainstream malware-delivery surface**.

**Mitigation:** Upgrade electerm to the latest patched release (project advisory pending); for managed developer workstations, pin allow-listed terminal clients (PuTTY, OpenSSH client) and treat Electron-based replacements as elevated-risk endpoints.

**Sources:** [GitHub Security Advisory GHSA-mpm8-cx2p-626q (CVE-2026-43944)](https://github.com/advisories/GHSA-mpm8-cx2p-626q) | [GitHub Security Advisory GHSA-f77v-9vpc-6pjm (CVE-2026-43940)](https://github.com/advisories/GHSA-f77v-9vpc-6pjm)

---

### MailEnable CVE-2026-44400 — WebAdmin authorization bypass
**Product:** MailEnable mail server | **CVE:** CVE-2026-44400 | **Published:** 2026-05-08

VulnCheck disclosed an authorization-bypass in the MailEnable WebAdmin interface. MailEnable is a Windows-based commercial mail server with a moderate small/medium business deployment footprint. The bypass provides administrative access to the mail server management plane without proper authentication checks — full mail-flow / mailbox access from a single bypass.

**Mitigation:** Apply MailEnable patches (vendor advisory pending); restrict WebAdmin port to internal IP ranges only. Audit administrative-action logs for unauthorized changes over the past 30 days.

**Sources:** [VulnCheck advisory — MailEnable WebAdmin authorization bypass](https://www.vulncheck.com/advisories) | [MailEnable](https://www.mailenable.com)

---

## 📋 Noted / Monitoring

**NVIDIA GeForce NOW Armenia (GFN.am) breach** — Third-party regional partner breach, names / emails / phones / DOBs / 2FA-status leaked for Armenian-region users; no NVIDIA infrastructure compromise. Out of scope for our enterprise surface but illustrates the regional-partner pattern (similar to vendor support-channel risks).

**Vvveb CMS 7-CVE batch (CVE-2026-41928 / 41929 / 41930 / 41931 / 41934 / 41936 / 41938)** — VulnCheck batch 2026-05-06 / 07; small-deployment CMS, mostly authenticated bugs with Media Upload RCE + XXE in Import worth attention if deployed.

**DrayTek CVE-2022-50994 (mainfunction.cgi OS command injection)** — VulnCheck reissued 2026-05-08; older bug in DrayTek routers / VPN devices, worth verification against patch state.

**SmarterTools CVE-2026-7807** — LFI via `/api/v1/report/summary/{type}` API; SmarterTools is small-footprint mail / help-desk; verify if any in fleet.

**free5gc multi-CVE batch (CVE-2026-44326 / 44327 / 44329 / 44330 / 44315)** — 5G Core test/research stack; multiple unauthenticated NEF + SMF API exposures. Limited production deployment, but worth tagging for telecom / lab environments.

**Windows Notepad CVE-2026-20841 — RCE via markdown links** — multiple PoC repos surfaced 2026-05-08; targets Windows Notepad < 11.2510. Out of scope (desktop-only, no remote-internet vector).

**KiviCare WordPress plugin CVE-2026-2991 — auth bypass via patient-social-login REST endpoint** — already overlap with the 04-30 KiviCare batch we covered; PoC repo update.

**Vim heap buffer overflow in spell file loading (Vim < 9.2.0450)** — disclosed 2026-05-07 on oss-security; local file-handling, not internet-facing.

**OpenStack Cyborg CVE-2026-40213 / 40214** — already covered 2026-05-08 (OSSA-2026-011 unconditional-allow + cross-tenant ARQ access).

**BYOVD process-termination via STProcessMonitor (CVE-2025-70795 / CVE-2026-0828)** — defender-evasion technique against process protection; out of scope (LPE / EDR-bypass only).

**Postorius (Mailman 3) admin XSS** — already covered 2026-05-08; still no patched release.

**pnpm 11 supply-chain protection defaults** — already covered 2026-05-07; defensive change, no action required for fleets already on pnpm ≥11.

**Chrome 148 — 127 security fixes** — already covered 2026-05-08; ensure Chrome auto-update is enforced.

**Federal contractor convicted for wiping federal databases** — insider abuse, no remote vector, out of scope.

**Taiwan high-speed rail student arrest** — physical-rail incident, out of scope.

**Anthropic Claude Code MCP hijacking + TrustFall Auto-Trust** — already covered 2026-05-08; no material updates.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer, thehackernews, securityweek, schneier, krebsonsecurity | ✅ |
| CISA / US Gov | cisa.gov / KEV | ❌ (403 via WebFetch — KEV news via THN/BleepingComputer) |
| Vendor advisories | rapid7, fortinet, msrc.microsoft.com, blog.cloudflare.com | ⚠️ MSRC empty, Fortinet no recent posts |
| Research / OSINT | github.com/0xMarcio/cve, securitylab.github.com, openwall oss-security, kb.cert.org, app.opencve.io | ✅ |
| Supply chain | socket.dev, snyk.io, aikido.dev, github.com/advisories, vulncheck.com | ✅ |
| Threat intel | wiz.io, labs.watchtowr.com, cert.gov.ua, dbugs.ptsecurity.com, habr.com/tomhunter, teletype.in/cyberok, avleonov.com | ⚠️ cert.gov.ua unreachable, several Russian-language sources stale |
| Full-disclosure | seclists.org/fulldisclosure, packetstorm.news | ⚠️ degraded (covered via openwall mirror) |
| Bug bounty | hackerone.com/hacktivity, bugcrowd.com/disclosures, attackerkb.com | ❌ all JS / 403 / 404 |
| CVE feeds | nvd.nist.gov, cve.mitre.org, cve.org, googleprojectzero.blogspot.com | ❌ JS-only / redirected (covered via opencve / github advisories) |

**Errors:** cisa.gov (403), cisa.gov KEV (403), attackerkb.com (403), bugcrowd.com (404), cve.mitre.org → cve.org (JS), cve.org (JS), hackerone.com/hacktivity (JS), googleprojectzero.blogspot.com (redirect 301), cert.gov.ua (empty WebFetch result).
**Degraded:** packetstorm.news (homepage doesn't list advisories), nvd.nist.gov (JS / search not accessible via WebFetch), msrc.microsoft.com (no posts visible), dbugs.ptsecurity.com (no individual entries listed).
**CISA KEV:** 1 new addition observable through secondary sources — CVE-2026-6973 (Ivanti EPMM, federal deadline 2026-05-10).

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-09/night | Next: 2026-05-10/night*
