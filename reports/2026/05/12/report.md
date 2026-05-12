# Watchtower Night Report — 2026-05-12
**Cycle:** Night | **Generated:** 2026-05-12 00:35 UTC (2026-05-12T00:35:00Z)
**Sources checked:** 23/30 | **CISA KEV total:** unreachable via WebFetch | **New KEV additions:** CVE-2026-42208 BerriAI LiteLLM SQL injection (2026-05-11, see UPDATE below)

---

## 🔴 CRITICAL

### 🔄 Mini Shai-Hulud npm Worm Resurges — 169 Compromised Packages incl. TanStack + UiPath, Trusted-Publisher Workflow Propagation
**Product:** npm ecosystem (TanStack, UiPath, plus 160+ additional packages — exact public list pending) | **CVEs:** Multiple (per-package GHSAs pending) | **CVSS:** N/A (campaign-scope) | **First reported:** 2026-04-29 (original) | **Update reported:** 2026-05-11 → 2026-05-12 (escalation)
**Previous threat score:** 9 → **Current threat score:** 9 (escalation)

Aikido published an alert on **2026-05-12** confirming the **Mini Shai-Hulud npm worm is back** — this second wave compromised **169 npm packages** so far, including widely-used **TanStack** packages (the React Query / Router / Table family) and **UiPath** packages (workflow-automation tooling deployed across enterprise RPA stacks). The worm uses the same playbook as the April 29–30 wave: it steals developer and CI/CD secrets (cloud credentials, npm/GitHub tokens, SSH keys, `.npmrc`/`.gem/credentials`/AWS keys, and runner-memory secrets via `/proc/<pid>/maps`/`mem` on GitHub-Actions Runner.Worker) and then **self-propagates through the victim's trusted-publishing workflows** — i.e. it re-publishes malicious versions of every package the compromised npm credential can publish to. This is the same self-propagation primitive that made the April wave a worm rather than an injection.

The TanStack hit is particularly load-bearing — TanStack libraries are dependencies in **a very large fraction of modern React/Next.js codebases** and many CI pipelines auto-update to latest minor/patch versions; the UiPath hit is the first time we have seen this worm cross into the enterprise-RPA ecosystem.

**Timeline:** **2026-04-29** original Mini Shai-Hulud wave (SAP `@cap-js`, mbt) → **2026-04-30** intercom-client, expanded npm wave → **2026-05-01** PyTorch Lightning 2.6.2/2.6.3 (PyPI cross-over, executes on `import`) → **2026-05-02** new IOC: `/proc/<pid>/maps`+`mem` runner-memory harvest → **2026-05-09** Socket / 84-TanStack artifacts identified → **2026-05-11→12** Aikido reports 169-package count and explicit UiPath inclusion.

**Why it matters:** Two things have changed since the April coverage. **First**, the package count crossed the 150-mark threshold where "compromise window response" stops working — the campaign is now too broad for org-by-org rotation playbooks to keep up. **Second**, UiPath inclusion means the same campaign now reaches into enterprise-RPA secret stores (orchestration tokens, robot creds, customer-tenant credentials embedded in workflow files). Any org that auto-updates its npm dependencies or pulls fresh packages on every CI run between **2026-05-09 and 2026-05-12** must treat the contents of every CI-runner-accessible secret as exposed.

**Discovered by:** Aikido Security (campaign-scope analysis); Socket (TanStack artifact identification); ongoing multi-vendor research.

**Mitigation:**
- Freeze npm dependency updates for ≥48 hours; pin to known-good versions until package lists are publicly enumerated.
- Audit `npm install` / `pnpm install` events in CI from **2026-05-09 onwards** — assume any runner that resolved a fresh TanStack/UiPath dep is compromised.
- Rotate **all CI-runner-accessible secrets**: npm tokens, GitHub tokens, AWS/GCP/Azure keys, SSH keys, OIDC tokens, internal-vault paths the runner can hit.
- For self-hosted GitHub Actions runners, audit `/proc/<pid>/maps` access events — the new IOC (covered 2026-05-02) is in-memory secret harvest from `Runner.Worker`.
- Apply the prior Mini Shai-Hulud guardrails: block `.claude/`, `.gemini/`, `.cursor/`, `.copilot/`, `.vscode/tasks.json` writes in CI; alert on any new SessionStart hook in a repo; treat AI-agent config dirs as workflow files.
- Hunt for the previously-published Bun-runtime stealer marker (`_runtime/start.py`, `router_runtime.js`, `execution.js`) and the AES-256-GCM exfil-via-public-repo pattern.

**Sources:** [Aikido — Mini Shai-Hulud Is Back: npm Worm Hits over 160 Packages](https://www.aikido.dev/blog/mini-shai-hulud-is-back-npm-worm-hits-over-160-packages) | [Socket — TanStack npm Packages Compromised in Ongoing Mini Shai-Hulud Supply-Chain Attack](https://socket.dev/blog)

---

### 🔄 CVE-2026-42208 LiteLLM Pre-Auth SQL Injection — Added to CISA KEV (Active Exploitation Now Federally Mandated)
**Product:** BerriAI LiteLLM proxy < 1.83.7 | **CVE:** CVE-2026-42208 | **CVSS:** 9.3 (Critical) | **First reported:** 2026-04-29 | **Update reported:** 2026-05-11
**Previous threat score:** 9 → **Current threat score:** 10 (KEV addition + ongoing exploitation)

CISA added **CVE-2026-42208** — LiteLLM's pre-auth SQL injection in the API-key verification path — to the **Known Exploited Vulnerabilities catalog on 2026-05-11**. The bug concatenates the supplied `Authorization` header into a SQL query, giving any unauthenticated network client a pre-auth injection sink against any LiteLLM API route; an attacker can enumerate and dump the LiteLLM database (virtual keys, master keys, env/config secrets used to broker requests to OpenAI / Anthropic / AWS Bedrock / other upstream providers). Sysdig confirmed exploitation began ~36 hours after the 2026-04-24 public disclosure; the KEV listing **formalises that exploitation has continued for over two weeks**, now triggering the 21-day federal patch deadline for U.S. government agencies and putting the bug squarely in the same urgency tier as cPanel CVE-2026-41940 and PAN-OS CVE-2026-0300.

**Timeline:** **2026-04-24** public disclosure → **2026-04-26** Sysdig confirms ITW exploitation → **2026-04-29** covered as CRITICAL (threat score 9) in 2026-04-29 report → **2026-05-11** CISA KEV addition with federal compliance deadline.

**Why it matters:** This is the **third** AI-platform vulnerability in 2026 to reach CISA KEV (after nginx-ui CVE-2026-33032 MCP path and now LiteLLM). LiteLLM sits at the upstream-credential broker layer of most enterprise self-hosted AI stacks — dumping its database yields organisation-wide LLM-provider keys, which carry significant downstream blast radius (cost, data exfil via prompt history, model-tampering). The KEV addition is the public signal that the exploitation tempo has not slowed since April — patching to **1.83.7+** is no longer optional, and any LiteLLM proxy exposed to the internet must be treated as compromised pending forensics.

**Mitigation:**
- Upgrade LiteLLM to **1.83.7 or later** immediately if not already patched.
- For any LiteLLM proxy that was internet-reachable between 2026-04-24 and patch deployment: **rotate all upstream LLM provider keys** (OpenAI, Anthropic, AWS Bedrock, Google Vertex, Azure OpenAI), assume virtual-key store and master-key are leaked, and audit for unauthorised model invocations / cost spikes.
- Federal agencies: 21-day KEV deadline applies.
- Hunt for the Sysdig-reported exploitation patterns: phase-one targeted enumeration of `LiteLLM_VerificationToken` and `LiteLLM_MasterKey` tables, phase-two pivot to fresh IPs.

**Sources:** [Security Affairs — CISA adds BerriAI LiteLLM flaw to KEV catalog](https://securityaffairs.com) | [Watchtower 2026-04-29 — CVE-2026-42208 original CRITICAL coverage](reports/2026/04/29/report.md)

---

### 📰 Checkmarx Jenkins AST Plugin Compromise (TeamPCP) — Credential-Stealing Plugin Live on Jenkins Marketplace
**Product:** Checkmarx Jenkins AST plugin (malicious version `2026.5.09`, safe baseline `2.0.13-829.vc72453fa_1c16`) | **CVE:** None assigned | **CVSS:** N/A | **Status:** **Active supply-chain compromise**, IOCs published, plugin pulled by maintainer
**Threat score:** 9 (CRITICAL) | **Discovery latency:** on-time

A malicious `2026.5.09` build of the **Checkmarx Jenkins AST plugin** was published to the **official Jenkins Marketplace (repo.jenkins-ci.org)** on **2026-05-09 (Saturday)** and remained available until disclosure on 2026-05-11. The plugin carries credential-stealing malware; the attackers left a signed message — **"Checkmarx fails to rotate secrets again. With love — TeamPCP"** — that explicitly attributes the attack to the **TeamPCP threat cluster** behind the **prior LiteLLM, Trivy, KICS-Docker, and Bitwarden CLI compromises**. Checkmarx confirmed the attackers maintained access to its GitHub environment for **at least 30 days** before publishing the malicious plugin, and that the GitHub intrusion was enabled by **stolen credentials from the earlier Trivy attack** — i.e. Checkmarx detected the Trivy breach in March 2026 but did **not** rotate the affected secrets, and TeamPCP retained access through that mistake to pivot into Jenkins plugin distribution.

**Timeline:** **March 2026** — TeamPCP Trivy/KICS-Docker compromise yields Checkmarx GitHub credentials → **April 2026** — Bitwarden CLI npm via Checkmarx GitHub Action (covered 2026-04-24) → **~April 10, 2026** — TeamPCP gains continued GitHub access (≥30-day dwell) → **2026-05-09 Saturday** — malicious Jenkins AST plugin `2026.5.09` published to Jenkins Marketplace → **2026-05-11** — public disclosure (BleepingComputer / The Hacker News / SecurityWeek).

**Why it matters:** This is **a security vendor's IaC/SAST scanning plugin** being weaponised to drop credential stealers on every CI/CD pipeline that runs static-analysis on every commit — the highest-privilege locations in any engineering org. Any Jenkins instance that installed/upgraded the Checkmarx AST plugin between **2026-05-09 and 2026-05-11** must be treated as compromised: the stealer runs in Jenkins-agent context, which typically holds source-code-read, artifact-publish, deploy, and (depending on environment) production-touching credentials. The published "fails to rotate secrets again" signal also confirms the **TeamPCP campaign now systematically exploits incomplete-IR-rotation in security vendors** — a pattern that will likely recur against any AppSec vendor whose breach response did not include full secret rotation.

**Discovered by:** Checkmarx internal detection; public disclosure by BleepingComputer / The Hacker News / SecurityWeek (2026-05-11).

**Mitigation:**
- **Immediately** verify Jenkins AST plugin version is **2.0.13-829.vc72453fa_1c16 or earlier** (the last known-good baseline) — uninstall `2026.5.09` if installed.
- Assume Jenkins-agent credentials are compromised for any pipeline that ran with the malicious plugin: rotate npm/GitHub/AWS/GCP/Azure tokens, SSH keys, artifact-registry creds.
- Audit Jenkins controller logs for outbound connections from the AST plugin process from 2026-05-09 onwards.
- Review CI/CD pipelines for any other Checkmarx-published artefacts (KICS scanner image, GitHub Action) and re-verify image digests / action SHAs.
- Treat this as **the second confirmed example of a 2026 supply-chain attack pivoting via a security-vendor relationship** (after the DigiCert chat-channel pattern, 2026-05-04) — extend the SOC playbook for trust-infra vendors to include "did our last vendor breach prompt them to rotate their CI/distribution credentials?" verification.

**Sources:** [BleepingComputer — Official CheckMarx Jenkins package compromised with infostealer](https://www.bleepingcomputer.com/news/security/) | [The Hacker News — TeamPCP Compromises Checkmarx Jenkins AST Plugin](https://thehackernews.com) | [SecurityWeek — Checkmarx Jenkins AST Plugin Compromised in Supply Chain Attack](https://www.securityweek.com)

---

## 🟠 HIGH

### 📰 Google GTIG — First Documented Use of AI-Generated Zero-Day Exploit in the Wild (2FA Bypass Against Open-Source Web Admin Tool)
**Product:** Unnamed open-source Python-based web administration tool (vendor notified, name withheld pending patch) | **CVE:** Not yet assigned | **CVSS:** Not assigned | **First reported:** 2026-05-11
**Threat score:** 8 | **Discovery latency:** on-time

Google **Threat Intelligence Group (GTIG)** disclosed on **2026-05-11** what it describes as the **first documented case of threat actors weaponising an AI-generated zero-day exploit in the wild**. The target was an unnamed popular open-source, web-based system administration tool (Python); the exploit is a 2FA bypass — a **high-level semantic logic bug**, not a memory-corruption issue. GTIG identified AI involvement through code-style analysis: "educational docstrings, a hallucinated CVSS score, and a structured, textbook Pythonic format highly characteristic of LLM training data." Google explicitly states **Gemini was not the LLM used**; the specific model is not named. Google detected the exploit before the "mass exploitation phase" and notified the software developer — patch status TBD.

**Mitigation:**
- This disclosure has **no specific product patch to apply yet** (vendor name withheld) — its operational value is the pattern signal.
- **AppSec impact:** AI-found semantic logic bugs (auth state machines, 2FA flows, session lifecycle, authz checks) are now a distinct class of disclosure to watch — they bypass the "memory-safety wave" mental model that has dominated 2024–2025 vuln tracking.
- Tighten review on any open-source admin-tool deployments — particularly Python web-based admin panels — for 2FA-flow logic bugs in code recently audited only by humans.
- Watch for follow-on disclosures naming the tool over the next 7–14 days.
- Strategic: this is the first concrete data point in **the "AI as bug finder for adversaries" pattern** (mirroring Anthropic Mythos and similar defensive announcements); plan for the volume of logic-bug class disclosures to grow non-linearly through 2026-Q3/Q4.

**Sources:** [BleepingComputer — Google: Hackers used AI to develop zero-day exploit for web admin tool](https://www.bleepingcomputer.com/news/security/) | [The Hacker News — First documented AI-built zero-day 2FA bypass](https://thehackernews.com) | [SecurityWeek — Google Detects First AI-Generated Zero-Day Exploit](https://www.securityweek.com)

---

### 🔄 CVE-2026-43284 / CVE-2026-43500 "Dirty Frag" — Microsoft Defender Confirms In-the-Wild Exploitation; Real-World Attack Chain Includes GLPI LDAP Tampering
**Product:** Linux kernel (xfrm-ESP IPsec page-cache write + RxRPC/RxKAD page-cache write) | **CVEs:** CVE-2026-43284, CVE-2026-43500 | **Status:** Limited ITW exploitation confirmed, CVE-2026-43284 patched in mainline, CVE-2026-43500 patch pending | **First reported:** 2026-05-08
**Previous threat score:** 8 → **Current threat score:** 9

SecurityWeek and Microsoft confirmed on **2026-05-11** that **Dirty Frag** (the public PoC name for the CVE-2026-43284 + CVE-2026-43500 universal Linux LPE chain) is **being exploited in the wild** — Microsoft Defender for Endpoint observed limited but real exploitation activity. The documented attack chain in the wild post-exploits the LPE-to-root primitive to: **(1)** modify GLPI's LDAP authentication-handling files to subvert tenant login, **(2)** conduct system reconnaissance against the host, **(3)** access sensitive data from PHP session files, **(4)** manipulate session files to both disrupt active sessions and read their contents. The CVE-2026-43284 mainline patch landed by 2026-05-08; CVE-2026-43500 (RxRPC) patch remains pending.

**Why it matters:** Two material changes since the 2026-05-08 disclosure. **First**, ITW exploitation has now been confirmed — the embargo break ("pre-patch public PoC at dirtyfrag.io") is being capitalised on. **Second**, the public attack chain shows attackers chaining the kernel LPE with application-layer post-exploit (GLPI tampering) — a pattern that maps cleanly onto any environment where Linux LPE provides the privilege uplift to manipulate web-app session/auth state. Every unpatched Linux host with the affected kernels is now LPE-to-root one PoC run away.

**Mitigation:**
- Apply distro kernel updates for CVE-2026-43284 immediately (mainline patch shipped; check distro backports — Ubuntu, RHEL, Amazon Linux, openSUSE, CentOS Stream, AlmaLinux, Fedora all have updates in flight).
- For CVE-2026-43500: apply the kernel `modprobe.d` workaround to disable `rxrpc` if not used.
- Audit any GLPI deployment on Linux for tampered LDAP config files and unexpected session-file mtimes — this is the published ITW chain.
- Treat any LPE-capable Linux host with public-facing GLPI/PHP web-app as priority-1 for patching.

**Sources:** [SecurityWeek — New "Dirty Frag" Linux Vulnerability Possibly Exploited in Attacks](https://www.securityweek.com) | [Wiz — Dirty Frag: Linux Kernel LPE via ESP and RxRPC (analysis, 2026-05-08)](https://wiz.io/blog) | [Avleonov — Dirty Frag analysis](https://avleonov.com) | [Watchtower 2026-05-08 — Dirty Frag prior CRITICAL coverage](reports/2026/05/08/report.md)

---

### 📰 GitHub Copilot CLI CVE-2026-45033 — Nested Bare Repository → Arbitrary Command Execution (Fifth AI-Agent Attack Surface in 12 Days)
**Product:** `@github/copilot` (npm; GitHub Copilot CLI) | **CVE:** CVE-2026-45033 | **CVSS:** High | **First reported:** 2026-05-11
**Threat score:** 7 | **Discovery latency:** on-time

GitHub published GHSA-9ccr-r5hg-74gf / CVE-2026-45033 on **2026-05-11**: a **nested bare Git repository inside a regular working copy** that **Copilot CLI** is asked to operate against can execute arbitrary commands via `core.fsmonitor` configuration. Git's per-repository config — including `core.fsmonitor`, which runs an arbitrary process on every Git operation — is honoured even when the repository is nested inside another working tree, and Copilot CLI invoked from the outer repo will pick up the nested config. Outcome: cloning a repo that *contains a nested bare repo* and then running Copilot CLI inside it yields **arbitrary command execution as the developer**.

**Mitigation:**
- Upgrade `@github/copilot` to the patched version per GHSA-9ccr-r5hg-74gf (check the advisory text for exact version).
- For developer machines that run Copilot CLI against arbitrary cloned repos, treat the upgrade as priority — this is reachable from `git clone <attacker-repo>; copilot <prompt>`.
- Hunt for `core.fsmonitor` settings in nested bare repos across recently-cloned third-party / sample / training repositories.

**Sources:** [GitHub Advisory GHSA-9ccr-r5hg-74gf — Nested Bare Repository Can Execute Arbitrary Commands via core.fsmonitor](https://github.com/advisories/GHSA-9ccr-r5hg-74gf)

**Why it matters:** This is the **fifth AI-agent attack surface disclosed in 12 days** — joining Mini Shai-Hulud Claude SessionStart (2026-04-30), Gemini CLI CVSS-10 implicit-trust (2026-05-01), Adversa TrustFall + Claude Code MCP-hijack (2026-05-07), ClaudeBleed Chrome extension (2026-05-08–09). The mechanism here (nested-bare-repo + `core.fsmonitor`) is different from the prior "folder-trust dialog accepts Yes" pattern, but the **defensive failure is the same shape**: the AI-agent CLI runs *implicitly trusted code* surfaced by the developer's working tree. For an enterprise that has rolled out Copilot CLI to thousands of developers, this is a workstation-RCE primitive reachable from any third-party repo a developer clones — exactly the kind of surface security-aware orgs cannot easily audit, because the agents are pulled in via individual developer onboarding rather than centrally provisioned tooling.

---

### 📰 Next.js Multi-CVE Batch (6 CVEs in 24h) — Middleware/Proxy Bypass × 4, SSRF, DoS
**Product:** Next.js (`next` npm) | **CVEs:** CVE-2026-44573 (Pages Router i18n middleware bypass), CVE-2026-44574 (dynamic route parameter injection middleware bypass), CVE-2026-44575 (App Router segment-prefetch middleware bypass), CVE-2026-45109 (App Router segment-prefetch middleware bypass — incomplete-fix follow-up), CVE-2026-44578 (WebSocket-upgrade SSRF in Cache Components), CVE-2026-44579 (Cache Components connection-exhaustion DoS) | **CVSS:** High across the batch | **First reported:** 2026-05-11
**Threat score:** 7 | **Discovery latency:** on-time

GitHub Advisories published a coordinated **six-CVE batch** for **Next.js** on **2026-05-11**: four middleware/proxy-bypass advisories (CVE-2026-44573 / 44574 / 44575 / 45109), one SSRF in the Cache Components WebSocket-upgrade path (CVE-2026-44578), and one DoS (CVE-2026-44579) in the same Cache Components path. The recurring theme is **middleware can be bypassed by route-resolution edge cases** that route requests directly to handlers without running the middleware chain — i.e. any auth-check / IP-allowlist / CSRF-check implemented as Next.js middleware is bypassable in the affected versions. CVE-2026-45109 is explicitly an **incomplete-fix iteration** on CVE-2026-44575 (segment-prefetch path), confirming a recurring code-quality issue on the middleware-routing surface.

**Mitigation:**
- Upgrade Next.js to the patched release per each GHSA — verify the version covers all six advisories (the App Router segment-prefetch incomplete-fix means more than one bump may be needed).
- For any Next.js-fronted app that uses **middleware for authn/authz/rate-limiting** rather than per-route checks, prioritise this upgrade above other non-critical work — middleware bypass is the closest thing to "authn-disabled-by-default" you can ship on a popular framework.
- For Cache Components: confirm no internet-facing SSR endpoint accepts WebSocket upgrades from untrusted origins until 44578 is patched.

**Sources:** [GHSA-36qx-fr4f-26g5 (44573 i18n)](https://github.com/advisories/GHSA-36qx-fr4f-26g5) | [GHSA-492v-c6pp-mqqv (44574 dynamic-route)](https://github.com/advisories/GHSA-492v-c6pp-mqqv) | [GHSA-267c-6grr-h53f (44575 segment-prefetch)](https://github.com/advisories/GHSA-267c-6grr-h53f) | [GHSA-26hh-7cqf-hhc6 (45109 segment-prefetch incomplete-fix)](https://github.com/advisories/GHSA-26hh-7cqf-hhc6) | [GHSA-c4j6-fc7j-m34r (44578 SSRF)](https://github.com/advisories/GHSA-c4j6-fc7j-m34r) | [GHSA-mg66-mrh9-m8jx (44579 DoS)](https://github.com/advisories/GHSA-mg66-mrh9-m8jx)

---

### 🔄 VulnCheck OpenClaw 16-CVE Batch (CVE-2026-44991 → CVE-2026-45006) — Second Mass-Disclosure Wave in 72 Hours
**Product:** OpenClaw (versions prior to 2026.4.10) | **CVEs:** CVE-2026-44991 → CVE-2026-45006 (16 new advisories) | **CVSS:** mixed (4 × High, 11 × Medium, 1 × Low) | **First reported:** 2026-05-11
**Previous threat score:** 8 → **Current threat score:** 8 (continued mass-disclosure)

VulnCheck published a **second batch** of **16 OpenClaw advisories on 2026-05-11**, on top of the **9-CVE batch (CVE-2026-43575 → 43583) on 2026-05-09** already covered. Headline items in the new batch:
- **CVE-2026-44995 (High)** — Arbitrary code execution via **MCP stdio environment variables** (MCP transport boundary bypass).
- **CVE-2026-45001 (High)** — Gateway config-mutation guard bypass via agent tool access.
- **CVE-2026-45004 (High)** — Arbitrary code execution via `setup-api.js` in current working directory.
- **CVE-2026-45006 (High)** — Unsafe config mutation via gateway tool denylist bypass.
- Medium-severity items cluster on authorisation bypass (44991, 44994), connector-host override via workspace dotenv (44992, 45003), trust-label tampering (44999), SSRF via CDP profile creation (45000), and webhook secret-cache invalidation (45005).

The **combined total** is now **25 OpenClaw CVEs disclosed in 72 hours** — directly applicable to the platform's **2026.2.21-2** version documented in MEMORY (which our own deployments were running as of the 2026-03-30 outdated-version note). The MCP-transport boundary, gateway config-mutation, and workspace-dotenv-as-config-override patterns are recurring themes across both batches.

**Mitigation:**
- Upgrade to OpenClaw **2026.4.10** or later **immediately** if not already on the latest; the cumulative exposure window from the 2026.2.21-2 baseline is now in the 25-CVE range.
- For the MCP-transport pattern (CVE-2026-44995): audit any custom MCP server registered with OpenClaw — environment-variable handling on `stdio` transports is the bypass primitive.
- Apply the agent-tool / workspace-config-trust audit: the prior MEMORY note on workspace files being readable via MEDIA: protocol compounds with these advisories.

**Sources:** [VulnCheck — OpenClaw advisories May 2026 (CVE-2026-44991 → CVE-2026-45006)](https://vulncheck.com/advisories) | [Watchtower 2026-05-09 — OpenClaw 9-CVE batch prior coverage](reports/2026/05/09/report.md)

---

## 🟡 MEDIUM

### 📰 GhostLock Disruption Tool — Windows `CreateFileW` Exclusive-Access Abuse as Data-Distraction Primitive
**Product:** Windows (any version — `CreateFileW` is core kernel32 API) | **CVE:** None (POC/technique disclosure) | **CVSS:** N/A | **First reported:** 2026-05-11
**Threat score:** 5 | **Discovery latency:** on-time

Kim Dvash of **Israel Aerospace Industries** released a proof-of-concept tool called **GhostLock** demonstrating abuse of Windows' `CreateFileW` API with `dwShareMode = 0`. The PoC opens files with exclusive access on local and SMB shares, preventing all other processes (including legitimate users) from reading or writing the file. The technique is **disruption-class** rather than destructive — no file is encrypted or deleted, but operational impact mirrors a ransomware outage: file servers become unusable while an attacker holds the lock. Detection is non-trivial because legitimate open requests do not trigger encryption-pattern or mass-write alerts; the researcher recommends monitoring per-session open-file counts with `ShareAccess = 0` at the file-server layer (a stat available in SMB management interfaces but not in standard Windows audit logs / EDR).

**Mitigation:**
- Inventory monitoring coverage for SMB session open-file counts with `ShareAccess = 0` — most fleets do not collect this signal today.
- For file servers: add the NDR rules and detection queries published in the researcher's whitepaper.
- Recovery is operational: terminate the SMB session, kill the holding process, reboot if needed.
- Strategic value is in **diversion-tactic awareness** — GhostLock is exactly the kind of noisy distraction an attacker may use to occupy IT/SOC attention while pursuing lateral movement or data exfil elsewhere.

**Sources:** [BleepingComputer — New GhostLock tool abuses Windows API to block file access](https://www.bleepingcomputer.com/news/security/new-ghostlock-tool-abuses-windows-api-to-block-file-access/)

---

## 📋 Noted / Monitoring

**CVE-2026-43898 @nyariv/sandboxjs (Critical, npm)** — Sandbox escape via `Function.caller` leakage of internal call op. Niche library; track if it surfaces as a dependency in any AI-eval / online-IDE backend.

**CVE-2026-27478 Unity Catalog Server (Critical, Maven)** — JWT issuer validation bypass enabling complete user impersonation. Self-hosted data-governance tooling; matters where Databricks Unity Catalog is replaced by community fork.

**CVE-2026-25244 WebdriverIO BrowserStack Service (Critical, npm)** — Command injection in browser-test plugin. CI-runner code; check JS test pipelines.

**CVE-2026-44643 angular-expressions (Critical, npm)** — Remote code execution using filters. Affects any app that evaluates user-supplied angular-expressions strings.

**CVE-2026-44477 cloudnative-pg (Critical, Go)** — Metrics exporter allows privilege escalation to PostgreSQL superuser and OS RCE on Kubernetes Postgres operator. Cluster-secret-equivalent in CNPG-managed K8s Postgres deployments — promote if widely deployed in fleet.

**CVE-2026-44336 PraisonAI (Critical, pip)** — Path traversal and RCE via Python `.pth` injection in `tools/call`. Latest AI-agent framework CVE; pattern aligns with Mini Shai-Hulud / agent-config code execution series.

**CVE-2026-44916 OpenStack Ironic (oss-security 2026-05-11)** — RCE when Anaconda driver enabled. Operator-side config issue.

**CVE-2026-43638 / 43639 / 43640 Bitwarden Server (2 × High, 1 × Medium)** — Missing authorisation on org cipher import / provider clients, authentication bypass via SCIM API key. Self-hosted Bitwarden deployments only — Bitwarden Cloud unaffected.

**CVE-2026-40217 LiteLLM Custom-Code Guardrail Sandbox Escape (High, pip)** — Separate from CVE-2026-42208 (KEV-listed today). Sandbox escape on the custom-code guardrail surface; patch in same upgrade cycle.

**CVE-2026-45033 @github/copilot (High, npm)** — Promoted to HIGH section above due to AI-agent-config pattern.

**CVE-2026-45061 budibase (High, npm)** — SSRF via `.tar.gz` substring bypass in plugin URL upload. Self-hosted Budibase only.

**CVE-2026-45047 bird-lg-go (High, Go)** — Fatal OOM DoS via unbounded JSON decoding. Niche network-ops tooling.

**CVE-2026-44544 / 44521 / 39850 (High, Maven/Composer)** — local-path-provisioner HelperPod template injection, elFinder SQL injection, Yii2 view-parameter LFI. Each niche but should be patched in affected stacks.

**CVE-2026-44211 cline (High, npm)** — Cross-origin WebSocket hijacking. AI-coding-agent extension surface — track alongside ClaudeBleed for cross-vendor browser-extension pattern.

**CVE-2026-44588 / 44670 siyuan/kernel; 43944 / 43940 electerm (High, Go/npm)** — XSS-to-Electron-renderer RCE chains in two separate Electron apps. Local-desktop tooling.

**CVE-2026-44523 note-mark/backend (Critical, Go)** — JWT secret weakness allowing full account takeover via token forgery; already in 2026-05-08 noted.

**CVE-2026-44473 ellanetworks/core + free5gc 5-CVE batch (Critical/High, Go)** — 5G core auth-missing on NEF/SMF management APIs (already in 2026-05-09 dedup); ellanetworks UE downlink redirection adds a 5G-RAN MITM primitive.

**Apache Airflow Providers CVE-2026-43826 / 41018 (oss-security 2026-05-10)** — OpenSearch + Elasticsearch log-handler credential leaks. Operator-side; rotate any Airflow connection URLs with embedded credentials.

**CVE-2026-7210 CPython XML Hash-Flooding (oss-security 2026-05-11)** — Insufficient entropy in expat / ElementTree parser hash protection. CPU DoS class only.

**CVE-2026-45186 libexpat 2.8.1 (oss-security 2026-05-11)** — DoS in XML parser. Patch with distro updates.

**CVE-2026-7010 HTTP::Tiny CRLF Injection (oss-security 2026-05-11)** — Perl HTTP-client request smuggling. Niche language ecosystem.

**CVE-2026-44931 malcontent D-Bus DoS (oss-security 2026-05-11)** — Disk-exhaustion via globally accessible D-Bus API. Linux-desktop parental-controls package.

**CVE-2026-43186 Linux Kernel IPv6 IOAM Heap Overflow (CVSS 9.8, opencve.io)** — Remote kernel panic / memory corruption via crafted IPv6 packets. Most enterprises do not have IOAM enabled, but check IPv6-heavy fleets.

**CVE-2026-41489 Pi-hole Local Privilege Escalation (CVSS 8.8)** — Local-only; out of scope per Watchtower scope rules but flagged because Pi-hole is common in home-lab/SMB environments.

**CVE-2026-43899 / 43900 Deepchat (CVSS 9.6 / 9.3, dbugs.ptsecurity.com)** — Recent disclosure; details thin pending more sources. Track.

**VU#937808 Casdoor Arbitrary File Write (CERT/CC, 2026-05-11)** — Identity-provider self-hosted server; arbitrary file write primitive enables RCE-equivalent. Niche.

**VU#471747 dnsmasq Multi-CVE (CERT/CC, 2026-05-11)** — DNS redirect + privilege escalation + heap manipulation in widely-deployed DNS forwarder. Defaults vary by distribution — verify your distro shipped the patch wave.

**NVIDIA GeForce NOW Armenian-User Data Breach (2026-05-08)** — Account-information exposure, no broader infrastructure impact reported.

**Skoda Online Shop Data Breach (2026-05-11)** — Customer PII (names, addresses, emails, phone numbers) via portal vulnerability. PII-only, no infrastructure impact.

**South Staffordshire Water 2-Year Unauthorised Network Access** — Long-dwell ICS-adjacent breach disclosed 2026-05-11. Confirms the Polish ABW pattern (covered 2026-05-09) of pre-positioning on water-utility infrastructure — track if the IR report names a threat actor.

**Crimenetwork Marketplace Takedown (German Federal Police, 2026-05-11)** — 22k users / 100+ sellers. Operational, not a vulnerability — useful for IOC enrichment if your fleet has prior interaction with the cluster.

**Schneier — LLMs and Text-in-Text Steganography (2026-05-11)** — Research note on covert-channel possibilities. Not operationally actionable yet.

**TrickMo Android Banker — TON Blockchain C2 (BleepingComputer, 2026-05-11)** — Mobile-only; out of scope per Watchtower rules.

**Instructure / Canvas — Root Cause Confirmed as XSS in Free-for-Teacher User-Generated-Content Features (BleepingComputer, 2026-05-11)** — Confirms the April-29 / May-7 / May-9 chain was a single XSS-to-admin-session vulnerability class. Already covered as breach incident in multiple prior reports (2026-05-04, 05-08, 05-09); root-cause confirmation is not a new advisory but worth dedup-aware noting.

**SailPoint GitHub Repository Hack (Disclosed 2026-05-11; intrusion 2026-04-20)** — No customer-data impact per vendor statement; flagged because it appears to fit the broader vendor-source-code-theft cluster of 2026 (Checkmarx, Cisco, Trellix). Track if the third-party vulnerability is named.

**Cloudflare Layoffs (2026-05-11)** — Not a security event; flagged because revenue-driven security-vendor restructurings sometimes correlate with reduced advisory output / IR cadence. Operational note only.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com, schneier.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (relayed via SecurityWeek + Security Affairs) |
| Vendor advisories | github.com/advisories, securitylab.github.com, msrc.microsoft.com/blog, vulncheck.com/advisories, fortinet.com/blog/threat-research | ✅ / ⚠️ |
| Research / OSINT | seclists.org/fulldisclosure, openwall.com/lists/oss-security, kb.cert.org/vuls, wiz.io/blog, labs.watchtowr.com, schneier.com, avleonov.com | ✅ |
| Supply chain | socket.dev, aikido.dev, safedep.io | ✅ |
| Threat intel | rapid7.com/blog, blog.cloudflare.com/tag/security, securityaffairs.com, helpnetsecurity.com | ✅ |
| CVE feeds | opencve.io / app.opencve.io, nvd.nist.gov, github.com/search?q=CVE, github.com/0xMarcio/cve, dbugs.ptsecurity.com | ✅ / ⚠️ |
| Russian / regional | habr/tomhunter, teletype/cyberok, cert.gov.ua | ⚠️ (no May 2026 content surfaced) |

**Errors:** cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403), attackerkb.com (403), bugcrowd.com/disclosures (404 — URL change unresolved since 2026-04-14), cve.mitre.org / cve.org (JS-required), googleprojectzero.blogspot.com → projectzero.google/ (JS-required), hackerone.com/hacktivity (JS-required), trendmicro.com (consistently empty via WebFetch).
**Degraded:** packetstorm.news (homepage only), msrc.microsoft.com/blog (footer-only via WebFetch — Patch Tuesday content scheduled later today), nvd.nist.gov (search-results page requires form post), dbugs.ptsecurity.com (stats only via WebFetch), fortinet.com (no May posts surfaced), snyk.io/blog (no May 2026 posts), habr/tomhunter (no May 2026 posts).
**CISA KEV:** CVE-2026-42208 LiteLLM added 2026-05-11 (relayed via Security Affairs / Help Net Security). Federal 21-day patch deadline ≈ 2026-06-01.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-12/night | Next: 2026-05-13/night*
