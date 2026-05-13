# Watchtower Night Report — 2026-05-13
**Cycle:** Night | **Generated:** 2026-05-13 00:30 UTC (2026-05-13T00:30:00Z)
**Sources checked:** 19/30 | **CISA KEV total:** unreachable via WebFetch (use SecurityAffairs as proxy) | **New KEV additions:** none confirmed since LiteLLM CVE-2026-42208 on 2026-05-11

---

## 🔴 CRITICAL

### 🔄 Mini Shai-Hulud npm Worm — Second Wave Now 416 Versions Across 170+ Packages With Valid SLSA Provenance Attestations (CVSS not applicable)
**Product:** npm + PyPI (TanStack, Mistral AI, UiPath, Guardrails AI, OpenSearch, BetterStack, plus 165+ others) | **CVE:** CVE-2026-45321 (TanStack arktype-adapter) and per-package GHSAs | **Status:** Active Exploitation — packages remained downloadable for hours after disclosure

Aikido, Endor Labs, Socket, and StepSecurity converged on a final tally of **416 malicious package artifacts** (Socket) / **373 malicious versions** (Aikido) / **160+ packages** (Endor Labs) across the second Shai-Hulud wave that began 2026-05-11. The standout escalation is that **84 of the malicious TanStack versions carry valid SLSA provenance attestations issued by npm's signing infrastructure and legitimate GitHub Actions signatures** — the cryptographic-attestation defenses that the JS ecosystem has been pushing for two years failed to flag this wave. Endor Labs documented the underlying chain: TeamPCP exploited (a) TanStack's `pull_request_target` workflow misconfiguration, (b) GitHub Actions cache poisoning, and (c) OIDC token theft from runner memory; the novel propagation primitive is **an orphaned commit pushed to a fork, referenced via a malicious optional dependency, causing npm to automatically fetch and execute attacker-controlled code at install time without ever touching the upstream package code**. The malware payload retains the prior wave's `router_init.js` credential exfil pattern (cloud providers, wallets, AI vendor keys, CI/CD secrets to `filev2.getsession.org`). Six-day cumulative compromise across two waves: ~585 distinct artifacts.

**Timeline:** 2026-04-30 Wave 1 (~25 packages) → 2026-05-11 Wave 2 begins (TanStack + Mistral) → 2026-05-12 Aikido / Endor Labs / Socket / StepSecurity disclosures → 2026-05-12 npm tombstoning underway; some versions still resolvable for transitive consumers.

**Why it matters:** The SLSA-attested signature on 84 of 373 versions is the single most consequential supply-chain story of 2026 so far — it invalidates the "verify provenance attestation" mitigation that defenders have been told is the authoritative defense against npm tampering. Any CI/CD pipeline that pinned to TanStack/Mistral/UiPath/Guardrails/OpenSearch since 2026-05-11 must be treated as credential-leaked, and **provenance-attestation-based allowlisting alone is no longer a sufficient supply-chain control**. Combined with the BufferZoneCorp Go-toolchain wrapping pattern (2026-05-03) and the Mini Shai-Hulud first-wave AI-agent config persistence (`.claude/settings.json` SessionStart) from 2026-04-30, TeamPCP now has a working playbook for compromised-trusted-publisher attacks across npm + PyPI + RubyGems + Go modules + Composer ecosystems.

**Discovered by:** StepSecurity, Endor Labs, Aikido (Charlie Eriksen), Socket; CVE-2026-45321 reported by Daniel Pereira (GitHub) for @tanstack/arktype-adapter.

**Mitigation:**
- Audit every CI runner that resolved any TanStack, Mistral AI, UiPath, Guardrails AI, OpenSearch, BetterStack npm package since 2026-05-11; rotate all GitHub PATs, npm publish tokens, cloud provider keys, and AI vendor keys present in those runner environments.
- Pin to known-clean versions (each package will publish a clean re-release once tombstoned); do not rely on SLSA provenance verification alone in the meantime.
- Disable `pull_request_target` workflows that check out untrusted PR code; if required, ensure they cannot access secrets.
- Inspect `~/.ssh/authorized_keys` on every developer workstation that ran `npm install` against affected packages — Shai-Hulud first wave appended attacker-controlled keys.
- Block egress to `filev2.getsession.org` at firewalls and EDR.

**Sources:** [BleepingComputer — Shai Hulud attack ships signed malicious TanStack, Mistral npm packages](https://www.bleepingcomputer.com/news/security/shai-hulud-attack-ships-signed-malicious-tanstack-mistral-npm-packages/) | [SecurityWeek — TanStack, Mistral AI, UiPath Hit in Fresh Supply Chain Attack](https://www.securityweek.com/tanstack-mistral-ai-uipath-hit-in-fresh-supply-chain-attack/) | [The Hacker News — Mini Shai-Hulud Worm Compromises TanStack, Mistral AI, Guardrails AI](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html) | [GitHub Advisory — GHSA-g7cv-rxg3-hmpx (@tanstack/arktype-adapter)](https://github.com/advisories/GHSA-g7cv-rxg3-hmpx)

**Previous threat score:** 9 → **9** (broadened scope + cryptographic-trust breakdown justifies sustained CRITICAL despite no new CVSS change)

---

### Fortinet Critical Unauthenticated RCEs in FortiSandbox (CVE-2026-26083) and FortiAuthenticator (CVE-2026-44277) — Both Perimeter-Security Appliances (CVSS not published, both rated Critical by vendor)
**Product:** FortiSandbox 4.4, 5.0; FortiSandbox Cloud 23, 24, 5.0; FortiSandbox PaaS 22.1–23.4; FortiAuthenticator 6.5.x, 6.6.x, 8.0.x (Cloud IDaaS unaffected) | **CVE:** CVE-2026-26083 (FortiSandbox, missing authorization, GUI), CVE-2026-44277 (FortiAuthenticator, improper access control), CVE-2026-39808 (FortiSandbox, OS command injection in API, also Critical) | **Status:** Patched 2026-05-12; no confirmed in-the-wild exploitation at disclosure

Fortinet's May 12 PSIRT batch ships two Critical unauthenticated-RCE advisories on flagship security appliances: **FG-IR-26-136 / CVE-2026-26083** is a missing-authorization flaw in the FortiSandbox web UI letting an unauthenticated attacker execute arbitrary code/commands via crafted HTTP requests; **FG-IR-26-100 / CVE-2026-39808** is a companion OS-command injection in the FortiSandbox API endpoint, also unauthenticated. **CVE-2026-44277** is an improper-access-control flaw in FortiAuthenticator (the SAML/RADIUS/MFA IdP product) that allows unauthenticated code/command execution via crafted requests; patched in 6.5.7, 6.6.9, 8.0.3. Companion advisories include FortiOS CAPWAP OOB-write (CVE-2025-53844, High) and FortiAP/FortiAnalyzer/FortiManager mediums.

**Timeline:** Coordinated vendor advisory 2026-05-12; no public exploitation reporting yet.

**Why it matters:** Fortinet sits on CISA KEV with 24 prior entries and 13 of those have appeared in ransomware campaigns — auth-bypass RCEs on Fortinet edge gear are a same-week ransomware monetisation pattern (cf. cPanel CVE-2026-41940 disclosure→ransomware in 5 days). FortiAuthenticator is particularly painful because it is *itself* the auth boundary for downstream services — pre-auth RCE on an MFA IdP yields total impersonation of every account it brokers. Treat both as immediate-patch class for any internet-exposed instance.

**Discovered by:** Internal Fortinet PSIRT.

**Mitigation:**
- Upgrade FortiSandbox to a patched build per FG-IR-26-136 / FG-IR-26-100 before exploitation tooling appears.
- Upgrade FortiAuthenticator to 6.5.7 / 6.6.9 / 8.0.3 per FG-IR for CVE-2026-44277.
- Restrict management-plane access (GUI, API) of both products to administrative network ranges; never expose to the public internet.
- Hunt for unauthenticated POST to FortiSandbox `/api/` endpoints in proxy/WAF logs in the past 7 days.
- For FortiAuthenticator: invalidate any session tokens issued in the preceding 30 days as a precaution; audit MFA-bypass-suggesting event sequences.

**Sources:** [BleepingComputer — Fortinet warns of critical RCE flaws in FortiSandbox and FortiAuthenticator](https://www.bleepingcomputer.com/news/security/fortinet-warns-of-critical-rce-flaws-in-fortisandbox-and-fortiauthenticator/) | [Fortinet PSIRT — FG-IR-26-136 / FG-IR-26-100](https://www.fortiguard.com/psirt)

---

## 🟠 HIGH

### Apache Tomcat 7-CVE Batch — Digest Auth Bypass, AJP Timing, Security Constraint Bypass, WebDAV Unbounded Read, HTTP/2 + WebSocket Issues
**Product:** Apache Tomcat (all currently supported branches; check vendor advisory matrix) | **CVE:** CVE-2026-43512 (digest authenticator bypass), CVE-2026-43513 (LockOutRealm case-sensitivity), CVE-2026-43514 (AJP secret timing attack), CVE-2026-43515 (security constraints bypass), CVE-2026-41284 (WebDAV unbounded read DoS), CVE-2026-41293 (HTTP/2 header validation), CVE-2026-42498 (WebSocket authentication exposure) | **CVSS:** not yet assigned at oss-security disclosure | **First reported:** 2026-05-12

Mark Thomas (Apache Tomcat lead) shipped seven CVE disclosures to oss-security on 2026-05-12 covering authentication, authorization, and protocol-handling issues. **CVE-2026-43512** is the most directly exploitable — a digest authenticator bypass against credential-protected admin pages and legacy realms; **CVE-2026-43513** is a parallel case-sensitivity issue in LockOutRealm (account-lockout enforcement) that lets attackers re-attempt credentials under case variants without triggering lockout. **CVE-2026-43514** is a timing-attack on the AJP secret used between Tomcat and front-end web servers (Apache HTTPD mod_proxy_ajp, Nginx); successful recovery of the AJP secret yields backend command-injection class impact equivalent to the historical Ghostcat CVE-2020-1938. **CVE-2026-43515** is a security-constraint enforcement bypass — Servlet-3.x `@HttpConstraint` annotations not consistently honored. The HTTP/2 + WebSocket + WebDAV trio (CVE-2026-41293, CVE-2026-42498, CVE-2026-41284) are protocol-handling issues with DoS-class impact at this analysis stage but warrant detail-tracking once full advisory text drops.

**Mitigation:**
- Upgrade Tomcat to the patched branch versions identified in the Apache Tomcat security page within the standard maintenance window.
- For exposed AJP listeners (port 8009 by default), regenerate the AJP `secret` post-patch and verify that `secretRequired="true"` is set; do not rely on network isolation alone.
- Audit logs for digest-authenticator paths under unusual `Authorization: Digest` headers and abnormal lockout-counter resets.
- For HTTP/2 endpoints, enable connection-level rate limits and request-validation middleware in front-end proxies until the patched build is rolled out.

**Sources:** [oss-security 2026-05-12 — Mark Thomas Tomcat CVE thread](https://www.openwall.com/lists/oss-security/2026/05/12/) | [Apache Tomcat Security Page (forthcoming detail)](https://tomcat.apache.org/security.html)

---

### Exim CVE-2026-45185 "Dead.Letter" — BDAT-over-GnuTLS Use-After-Free → Heap Corruption / Potential RCE (CVSS not yet published)
**Product:** Exim 4.97 → 4.99.2 (only builds compiled with `USE_GNUTLS=yes`; OpenSSL builds unaffected) | **CVE:** CVE-2026-45185 | **CVSS:** not published; XBOW characterises as "one of the highest-caliber bugs in Exim's history" | **First reported:** 2026-05-12

A use-after-free in Exim's BDAT (CHUNKING) message-body parser when used over GnuTLS. The trigger: a client sends a TLS `close_notify` alert *before* the BDAT body transfer completes, then writes a final byte in cleartext on the same TCP connection. During TLS shutdown Exim frees its TLS transfer buffer, but a nested BDAT receive wrapper still invokes `ungetc()`, writing one attacker-controlled byte into the freed region. The single-byte UAF write into a heap region whose layout has known structure makes this a viable RCE primitive class, not just a DoS. Exim 4.99.3 has shipped with a fix that resets the input-processing stack on TLS close-notify. No public exploit yet, but a detection script (`liamromanis101/Dead.Letter-CVE-2026-45185`) is already on GitHub.

**Why it matters:** Exim is on roughly 60% of internet-facing SMTP servers per most surveys. While the GnuTLS-build limit narrows the population, it's nontrivial — many distros (notably Debian's default) ship GnuTLS builds. SMTP is unauthenticated to internet-side senders by design, so the attack precondition is just "open SMTP on port 25 with STARTTLS, GnuTLS build, BDAT extension enabled (the default)." This is the cleanest near-perimeter RCE class disclosure of the week.

**Discovered by:** Federico Kirschbaum (Head of Security Lab, XBOW).

**Mitigation:**
- Upgrade to Exim 4.99.3 immediately on all internet-facing MTAs; do not wait for distro packaging.
- If 4.99.3 cannot be rolled out, **rebuild Exim against OpenSSL instead of GnuTLS** as a stopgap.
- Confirm BDAT extension exposure with `nc -v <mta> 25` → `EHLO test` and check for `CHUNKING` advertisement; remove from `acl_smtp_chunkin` if unused (BDAT is rarely needed in practice for inbound mail).
- Hunt for TLS-shutdown-then-cleartext-byte sequences in MTA packet captures (heuristic: TLS close_notify immediately followed by a single non-TLS byte on the same connection in BDAT-mode flows).

**Sources:** [The Hacker News — New Exim BDAT Vulnerability Exposes GnuTLS Builds](https://thehackernews.com/2026/05/new-exim-bdat-vulnerability-exposes.html) | [oss-security 2026-05-12 — EXIM-Security-2026-05-01.1 Security Release 4.99.3](https://www.openwall.com/lists/oss-security/2026/05/12/) | [XBOW Security Lab Disclosure](https://xbow.com)

---

### OpenClaude CVE-2026-42074 — Sandbox Bypass via Model-Controlled `dangerouslyDisableSandbox` Flag (CVSS 9.3) — Sixth AI-Agent Attack Surface in 14 Days
**Product:** OpenClaude (npm) — community CLI/framework for interacting with Claude models — versions prior to 0.5.1 | **CVE:** CVE-2026-42074 | **CVSS:** 9.3 | **First reported:** 2026-05-12 (GitHub advisory GHSA-m77w-p5jj-xmhg)

OpenClaude's `BashTool` exposes a `dangerouslyDisableSandbox: boolean` parameter to the LLM in its tool-call schema. The implementation in `src/tools/BashTool/shouldUseSandbox.ts` honors that flag when the host has set `allowUnsandboxedCommands: true` (the *default* in the shipped config). Because the parameter sits on the model-controlled input surface, **any prompt-injection that causes the model to emit `"dangerouslyDisableSandbox": true` in a bash tool call results in immediate sandbox-free command execution as the OpenClaude process owner**. Patched in 0.5.1 by gating the flag behind a host-set capability rather than model-supplied input.

**Why it matters:** This is the sixth AI-agent attack-surface disclosure in 14 days, following Mini Shai-Hulud `.claude/settings.json` SessionStart persistence (2026-04-30), Google Gemini CLI CVSS-10 implicit-trust-of-config (2026-05-01), Claude Code MCP hijacking + Adversa.AI "TrustFall" cross-vendor folder-trust bypass (2026-05-07), LayerX ClaudeBleed browser-extension origin-vs-context confusion (2026-05-08), and GitHub Copilot CLI nested-bare-repo `core.fsmonitor` RCE (2026-05-11). The pattern is consistent: AI agent runtimes give models access to capability surfaces they treat as instructions, and any prompt-injection turns that into RCE-equivalent on the developer host. The novelty here is that **the bypass is the agent's own threat-model anti-pattern: a flag literally named "dangerously" is exposed to untrusted input**, which the OpenClaude threat model itself warns against ("The model/agent is not a trusted principal. Assume prompt/content injection can manipulate behavior"). Treat AI-agent config + tool-schema audits as continuing high-yield bug-hunting territory for 2026-Q2.

**Discovered by:** Independent GHSA submitter (credits per the advisory).

**Mitigation:**
- Upgrade OpenClaude to 0.5.1 immediately on any developer workstation that has invoked it against untrusted input or shared MCP servers.
- Default-deny any AI-agent CLI config flag that begins with "dangerously", "skip", "unsafe", or "disable" to model-controlled inputs — these are tripwires by convention.
- Audit any AI-agent tool-call schema in your environment for similar parameters that gate security boundaries (sandbox toggle, network egress, file write scope, shell execution flag); model these as part of the boundary, not as model input.
- For incident response, hunt OpenClaude logs for tool calls carrying `dangerouslyDisableSandbox=true` since 2026-04-01.

**Sources:** [GitHub Advisory — GHSA-m77w-p5jj-xmhg](https://github.com/advisories/GHSA-m77w-p5jj-xmhg) | (See also MEMORY.md AI-agent attack-surface pattern entries)

---

### esm.sh CVE-2026-44593 — Legacy Route Path Traversal → Arbitrary File Write → RCE on Public JS CDN (CVSS not yet assigned, GHSA Critical)
**Product:** esm.sh — Go-based public npm CDN service used as transitive dependency by countless browser JS projects — versions prior to `0.0.0-20260508100112-1960055e1d53` | **CVE:** CVE-2026-44593 (+ CVE-2026-44594, related path-traversal via package.json `browser` field) | **CVSS:** not published; GHSA marks Critical | **First reported:** 2026-05-12 / 2026-05-13

DEVCORE researcher splitline reported a path-traversal in esm.sh's legacy router: encoded `..%2f` sequences in the URL path are forwarded to `legacyServer`, where path components are concatenated without sanitization. Filesystem path resolution then walks out of the intended directory, and the response content is written to an attacker-chosen on-disk location. Overwriting system binaries or autorun scripts yields RCE as the esm.sh service account. Companion CVE-2026-44594 leaks server-side files via the `browser` field of `package.json`. Patched 2026-05-08 in `0.0.0-20260508100112-1960055e1d53`.

**Why it matters:** esm.sh is a widely-used public CDN for ES-module-format npm packages — used by countless modern browser JS projects that want CDN-served esmodule semantics without a build step. The hosted service (esm.sh) is operated by the maintainer and serves millions of requests/day; the same code is also widely self-hosted as an internal CDN by orgs that want air-gapped or proxied npm-CDN behavior. Any self-hosted esm.sh on an internal network needs immediate patching — RCE on a CDN that resolves `import` URLs for the whole org is a high-value pivot.

**Discovered by:** splitline (DEVCORE Research Team).

**Mitigation:**
- Update self-hosted esm.sh to the patched commit or later; for the public esm.sh service, monitor maintainer comms for confirmation that the public infra has been rotated/cleaned.
- Audit any internal CDN that proxies esm.sh URLs — they may have served compromised resources during the window.
- Block `..%2f` and similar percent-encoded traversal sequences at the reverse proxy in front of any module-serving service.

**Sources:** [GitHub Advisory — GHSA-3636-h3vx-6465 (CVE-2026-44593)](https://github.com/advisories/GHSA-3636-h3vx-6465) | [GitHub Advisory — GHSA-rg65-45m7-hq57 (CVE-2026-44594)](https://github.com/advisories/GHSA-rg65-45m7-hq57)

---

### SAP S/4HANA CVE-2026-34260 + Commerce Cloud CVE-2026-34263 — Critical Auth Bypass / SQLi → Code Execution
**Product:** SAP Commerce Cloud (improper Spring Security configuration → unauth code execution), SAP S/4HANA (SQL injection via direct user-input concatenation) | **CVE:** CVE-2026-34260 (S/4HANA SQLi), CVE-2026-34263 (Commerce Cloud missing-auth → RCE) | **CVSS:** not published in vendor advisory text; both flagged "Critical" | **First reported:** 2026-05-12 SAP Patch Day

SAP's May 2026 Patch Day shipped 15 advisories, with **CVE-2026-34263** the standout: a missing authentication check in SAP Commerce Cloud stemming from "improper Spring Security configuration" that lets an unauthenticated attacker upload malicious configuration and inject code → arbitrary server-side execution. **CVE-2026-34260** is an SQL injection in S/4HANA requiring only "basic privileges" — the application directly concatenates user input into database queries. Either is enterprise-RCE class against the most-deployed ERP platform in the Fortune 1000.

**Why it matters:** SAP S/4HANA and Commerce Cloud are deployed at thousands of large enterprises and carry the most-sensitive transactional data (finance ledgers, customer PII, order pipelines). SAP Critical-class advisories are typically followed within weeks by SAP-specific scanner modules (Onapsis, ERPScan-class) and credential-broker activity — these will be on threat-actor radars by next week.

**Mitigation:**
- Apply SAP May 2026 Security Patch Day fixes (SAP Note numbers per vendor portal) on all S/4HANA and Commerce Cloud instances on standard SAP change-management cadence; treat as same-week priority.
- For Commerce Cloud: validate that Spring Security configuration explicitly authenticates every administrative path; do not rely on the upstream default.
- For S/4HANA: inventory any custom SQL pass-through paths and audit logs for query patterns suggestive of injection.

**Sources:** [SecurityWeek — SAP Patches Critical S/4HANA, Commerce Vulnerabilities](https://www.securityweek.com/sap-patches-critical-s-4hana-commerce-vulnerabilities/) | [BleepingComputer — SAP fixes critical vulnerabilities in Commerce Cloud and S/4HANA](https://www.bleepingcomputer.com/news/security/sap-fixes-critical-vulnerabilities-in-commerce-cloud-and-s-4hana/)

---

## 🟡 MEDIUM

### Microsoft May 2026 Patch Tuesday — 120 Vulnerabilities, 17 Critical, Zero Zero-Days (First Zero-Day-Free Patch Tuesday in ~2 Years)
**Product:** Windows (DNS Client, Native WiFi, Netlogon, Hyper-V, Graphics, GDI), Microsoft Office + Word, SharePoint, Dynamics 365, M365 Copilot, Microsoft SSO Plugin for Jira/Confluence | **CVE:** see batch below | **Published:** 2026-05-12

Microsoft addressed 120 CVEs with 17 marked Critical and zero in-the-wild zero-days disclosed — Krebs notes this is the first Patch Tuesday in nearly two years without an emergency zero-day. Highest-attention items: **CVE-2026-41096** (Windows DNS Client memory corruption via crafted DNS response — remote attacker with attacker-controlled DNS server, no client interaction beyond name resolution), **CVE-2026-32161** (Windows Native WiFi RCE — wireless adjacency), **CVE-2026-41089** (Windows Netlogon RCE — domain-controller-class impact), **CVE-2026-40402** (Hyper-V EoP), **CVE-2026-42898** (Dynamics 365 On-Premises RCE), **CVE-2026-41103** (Microsoft SSO Plugin for Jira & Confluence EoP), **CVE-2026-26164** (M365 Copilot information disclosure), plus four Office and four Word RCEs via malicious documents.

**Mitigation:** Apply May 2026 cumulative on standard enterprise cadence. Priority order based on internet exposure: DNS Client (CVE-2026-41096) and Netlogon (CVE-2026-41089) > SharePoint (CVE-2026-40365) > Dynamics 365 (CVE-2026-42898) > Office/Word document-handling. The Jira/Confluence SSO plugin (CVE-2026-41103) needs separate attention from the OS rollout — that's the Atlassian-side plugin and follows their patch process.

**Sources:** [BleepingComputer — Microsoft May 2026 Patch Tuesday fixes 120 flaws, no zero-days](https://www.bleepingcomputer.com/news/microsoft/microsoft-may-2026-patch-tuesday-fixes-120-flaws-no-zero-days/) | [SecurityWeek — Microsoft Patches 137 Vulnerabilities](https://www.securityweek.com/microsoft-patches-137-vulnerabilities/) | [Krebs on Security — Patch Tuesday, May 2026 Edition](https://krebsonsecurity.com/2026/05/patch-tuesday-may-2026-edition/)

---

### Adobe Connect CVE-2026-34660 — Authorization Vuln → Arbitrary Code Execution (CVSS 9.3)
**Product:** Adobe Connect 2025.9.15 and earlier (also 2025.8.157 and earlier) | **CVE:** CVE-2026-34660 | **CVSS:** 9.3 | **Published:** 2026-05-12

Authorization flaw in Adobe Connect enabling arbitrary code execution via malicious script injection into web pages, granting elevated access to victims who interact with crafted URLs. Adobe Connect is web-conferencing software widely deployed in regulated-industry training stacks (financial services, healthcare). Part of Adobe's broader May 2026 Patch Tuesday — 52 CVEs across 10 products with none yet exploited in the wild.

**Mitigation:** Upgrade Adobe Connect per APSB-26-XX. Audit pre-2025.9.15 instances for anomalous user-impersonation events in the preceding 30 days. Restrict admin-console access to known-good IP ranges.

**Sources:** [SecurityWeek — Adobe Patches 52 Vulnerabilities in 10 Products](https://www.securityweek.com/adobe-patches-52-vulnerabilities-in-10-products/) | [OpenCVE — CVE-2026-34660](https://app.opencve.io/cve/CVE-2026-34660)

---

### protobuf.js 6-CVE Batch — Code Injection + OS Command Injection + Prototype Pollution + DoS
**Product:** protobuf.js (npm) ≤ 7.5.5 and 8.0.0–8.0.1 (patched 7.5.6 / 8.0.2) | **CVE:** CVE-2026-44289 (DoS via unbounded recursion), CVE-2026-44290 (process-wide DoS via unsafe option paths), CVE-2026-44291 (code generation gadget after prototype pollution), CVE-2026-44293 (code injection via bytes field defaults, CVSS 7.7), CVE-2026-44295 (code injection in CLI static output), CVE-2026-42290 (OS command injection in CLI) | **Published:** 2026-05-12 / 2026-05-13

Six-CVE batch from a coordinated review of protobuf.js code-generation paths. The headline issues: **CVE-2026-44293** — `toObject` conversion function generates JavaScript that incorporates an unsafe expression derived from a schema-controlled `bytes` field default; **CVE-2026-42290** — OS-command injection in the protobufjs CLI's static-output handler; **CVE-2026-44291** — code-generation gadget reachable after generic prototype pollution. Exploit precondition for the in-process issues is that the application accepts attacker-controlled `.proto` schemas/descriptors (think gRPC services that load proto definitions from user input, or design tools that import third-party `.proto` files). The CLI issues are exploitable wherever build scripts invoke `pbjs` against attacker-supplied files.

**Mitigation:** Upgrade protobuf.js to 7.5.6 or 8.0.2 across all repos. For services that ingest third-party `.proto` content, audit `toObject` invocation paths and disable `defaults: true` if not strictly required. Sandbox the `pbjs` CLI in CI/build scripts (run in a container without inherited credentials).

**Sources:** [GitHub Advisory — GHSA-66ff-xgx4-vchm (CVE-2026-44293)](https://github.com/advisories/GHSA-66ff-xgx4-vchm) | [GitHub Advisory — GHSA-f84p-cvgm-xgjj (CVE-2026-42290)](https://github.com/advisories/GHSA-f84p-cvgm-xgjj)

---

### Cleanuparr CVE-2026-44183 — X-Forwarded-For Spoofing → Admin Access (CVSS 9.8)
**Product:** Cleanuparr (containerized media-stack cleanup tool) < 2.9.10 | **CVE:** CVE-2026-44183 | **CVSS:** 9.8 | **Published:** 2026-05-12

`TrustedNetworkAuthenticationHandler.ResolveClientIp` parses the *leftmost* entry of the `X-Forwarded-For` header as the client IP — an attacker can place `127.0.0.1` (or any "trusted-network" address) in the header and gain unauthenticated administrator access to the Cleanuparr admin UI. Patched in 2.9.10.

**Mitigation:** Upgrade Cleanuparr to 2.9.10. Configure any reverse proxy in front of Cleanuparr to overwrite (not append to) the `X-Forwarded-For` header so attacker-supplied values cannot reach the trusted-network handler. Audit homelab/self-hosted media stacks (Sonarr/Radarr/Jellyfin orchestration) where Cleanuparr commonly runs.

**Sources:** [OpenCVE — CVE-2026-44183](https://app.opencve.io/cve/CVE-2026-44183) | [dbugs.ptsecurity.com — CVE-2026-44183](https://dbugs.ptsecurity.com)

---

### RubyGems Mass Malicious Package Upload — Sign-Ups Temporarily Suspended (CVE not applicable)
**Product:** RubyGems registry | **CVE:** none | **Published:** 2026-05-12

RubyGems temporarily disabled new user registration after hundreds of malicious packages were uploaded in a coordinated campaign. Per Maciej Mensfeld (Mend.io), the bulk of the malicious packages were targeted *at Mend.io specifically* — the security-research firm that scans RubyGems — but "some carrying exploits" were broader-scope. No attribution at disclosure; no detected exploitation of legitimate downstream consumers. New account registration suspended as a containment measure while incident response continues.

**Mitigation:** No general action required for downstream consumers given the Mend-targeting scope. Defenders should monitor RubyGems advisory feeds for any escalation. For organizations using internal Ruby mirrors, do not pull new package versions during the response window.

**Sources:** [The Hacker News — RubyGems Suspends New Signups After Hundreds of Malicious Packages Are Uploaded](https://thehackernews.com/2026/05/rubygems-suspends-new-signups-after.html)

---

## 📋 Noted / Monitoring

**dalfox/v2 CVE-2026-45087 / 45088 / 45089 / 45090** — Triple critical/high batch (unauth RCE in server mode via `found-action`, arbitrary file read with OOB exfiltration, arbitrary file write, unauth DoS); dalfox is a popular Go-based XSS scanner — patch any CI deployment that runs dalfox `--server` mode.

**Xen Security Advisory 490 (CVE-2025-54518)** — x86 CPU opcode cache corruption disclosed 2026-05-12; affects hypervisor instances on x86; vendor patching path detailed in XSA-490.

**uriparser 1.0.2 — CVE-2026-44927 + CVE-2026-44928** — Two issues in widely-used URI parsing library; patch via distro updates as upstream releases propagate.

**Apple May 2026 macOS / iOS patches** — Dozens of vulnerabilities including a backport of an iOS deleted-chats-recovery issue; mostly out-of-scope (client-only), but track per regulatory device-management requirements.

**West Pharmaceutical Services ransomware disruption** — Global systems offline after data exfil + file-encrypting ransomware deployment; pharma-sector incident, ransomware family not yet disclosed.

**BWH Hotels 6-month dwell-time breach** — Attackers had access to reservation system data (names + contact info) for 6+ months before detection; hospitality sector, broad PII exposure for affected guests.

**JDownloader CMS compromise — additional IOC enrichment** — Investigations of the trojanised Windows/Linux installer incident (2026-05-06 → 2026-05-10) continue to surface; no fundamentally new findings since main coverage but watch for second-stage payload analysis.

**South Staffordshire Water — UK ICO £963,900 / $1.3M fine** — Enforcement action against UK water supplier for 2022-2024 breach exposing 664k customers; reinforces the 2026-05-09 Polish ABW water-treatment pre-positioning pattern, this time as a regulatory-cost data-point.

**Signal — in-app phishing / social-engineering warning surface** — Defense-side feature addition rather than a vulnerability; relevant to user-education content but not a triage item.

**SailPoint GitHub repo intrusion follow-up** — Vendor reiterated no customer-data impact; remains worth tracking only if linked to the broader vendor-source-code-theft cluster (Checkmarx / Cisco / Trellix).

**OpenAI Daybreak** — New AI-vulnerability-detection program (gpt-5.5 / gpt-5.5-Cyber variants) targeting vuln triage and patch validation; pilot integrations with Akamai/Cisco/Cloudflare/CrowdStrike/Fortinet/Oracle/PAN/Zscaler. Notable as a market-defining "AI 90-day-disclosure policy is dead" framing but not itself a vulnerability.

**SillyTavern CVE-2026-44648 / 44649 / 44650 (npm)** — Triple advisory: session persistence after password change (account takeover), SSO header injection auth bypass, path traversal; affects self-hosted AI-chat front-end (smaller deployment than Open WebUI).

**UltraJSON CVE-2026-44660** — Memory leak in `ujson.dump()` on write failure; Python ecosystem widely deployed but DoS-only impact.

**Apache Tomcat EncryptInterceptor CVE-2026-34486 (n-day PoC)** — Public PoC for the EncryptInterceptor fail-open bypass surfaced on 0xMarcio CVE repo; older CVE getting weaponized — patch if not already on the latest 9.x/10.x branch.

**MantisBT 7-CVE batch** — Multiple XSS, injection, and access-control issues in MantisBT (Composer); upgrade if running self-hosted MantisBT.

**Perl CPAN string of small advisories (CVE-2026-8368 LWP::UserAgent header leakage, CVE-2026-5089 YAML::Syck OOB, CVE-2026-45179/45180 Plack/Catalyst Statsd, CVE-2026-45190/45191 Net::CIDR::Lite, CVE-2026-8177 XML::LibXML)** — Multiple Perl-ecosystem patches landed at oss-security 2026-05-10 to 05-13; cumulative impact mostly low-severity but worth a per-distro `cpan upgrade` audit pass.

**Dovecot OXDC-2026-0002** — Second Dovecot security advisory of 2026; detail thin in oss-security thread, awaiting full text from Open-Xchange.

**Mr_Rot13 attribution for cPanel CVE-2026-41940 mass exploitation** — Active-since-October-2020 actor with PHP backdoor samples on VirusTotal since 2022, encoding C2 domains via ROT13 cipher; >2,000 attacker source IPs across Germany/US/Brazil/Netherlands; deploys "Filemanager" Go-based cross-platform backdoor with bash-history + SSH-credential + DB-password harvesting. Reinforces the auth-bypass→ransomware monetisation pattern from prior coverage.

**CRPx0 cross-platform malware** — macOS/Windows targeting with Linux variants in development; "Free OnlyFans" social-engineering lure; commodity-class but cross-platform pattern worth tracking.

**TrickMo TON-C2 + SOCKS5 variant** — Android banking trojan using The Open Network for C2 + SOCKS5 tunneling to create network pivots; mobile-only, out of Watchtower scope but novel TTP combination.

**LLMs and Text-in-Text Steganography (Schneier 2026-05-11)** — Research demonstrating LLMs are exceptionally effective at concealing text-in-text covert channels; relevant context for data-loss-prevention and steganalysis programs but not an actionable advisory.

**Public security analysis + LLM-assisted variant discovery (oss-security 2026-05-12, Tim Shephard)** — Discussion thread on coordinated-disclosure norms in the LLM era following the 2026-05-11 Google GTIG AI-generated 0-day disclosure; non-advisory but informs scoring-calibration for the AI-found semantic-logic-bug pattern.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer, thehackernews, securityweek, krebsonsecurity, schneier | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (use securityaffairs as proxy) |
| Vendor advisories | fortinet PSIRT, msrc, securitylab.github, opencve, dbugs.ptsecurity, github/advisories | ✅ / ⚠️ |
| Research / OSINT | seclists.org/fulldisclosure, packetstorm, openwall oss-security, kb.cert.org/vuls, avleonov, github 0xMarcio cve, schneier | ✅ / ⚠️ |
| Supply chain | bleepingcomputer + thehackernews + securityweek + github advisories | ✅ |
| Threat intel | rapid7, fortinet/blog/threat-research, schneier, securityaffairs | ✅ / ⚠️ |

**Errors:** cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403), attackerkb.com (403), seclists.org/fulldisclosure (302 redirect failure), cve.mitre.org (JS-only), cve.org (JS-only), googleprojectzero.blogspot.com (redirect to projectzero.google/), msrc.microsoft.com/blog (redirect+empty), hackerone.com/hacktivity (JS-only), bugcrowd.com/disclosures (404), cert.gov.ua (empty)

**Degraded (returned no useful May 12-13 content):** fortinet.com/blog/threat-research, packetstorm.news, nvd.nist.gov, github.com/0xMarcio/cve, habr.com/ru/companies/tomhunter/articles, teletype.in/@cyberok

**CISA KEV:** No new entries confirmed since CVE-2026-42208 (LiteLLM) added 2026-05-11; verify next cycle via SecurityAffairs proxy.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-13/night | Next: 2026-05-14/night*
