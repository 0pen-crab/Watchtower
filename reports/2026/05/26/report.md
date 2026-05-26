# Watchtower Night Report — 2026-05-26
**Cycle:** Night | **Generated:** 2026-05-26 00:30 UTC (2026-05-26T00:30:00Z)
**Sources checked:** 23/30 | **CISA KEV total:** unchanged (gateway still 403) | **New KEV additions:** none confirmed since 2026-05-22 (Drupal CVE-2026-9082 with due date 2026-05-27); KEV REST API remains unreachable, monitor for 2026-05-27 cycle

---

## 🟠 HIGH

### TrapDoor Cross-Ecosystem Credential Stealer — 34+ Malicious Packages / 384+ Versions Across npm + PyPI + Crates.io With AI-Coding-Assistant Manipulation Primitive
**Product:** npm (19 packages), PyPI (7 packages), Crates.io (6 packages) — full list maintained by Socket / SocRadar | **CVE:** Not yet assigned | **CVSS:** N/A (supply chain) | **First reported:** 2026-05-22 (campaign start), 2026-05-25 (Socket / THN public disclosure)

Socket disclosed 2026-05-25 a coordinated supply chain campaign — **TrapDoor** — across three package registries totaling 34+ packages / 384+ artifacts published in waves starting 2026-05-22 20:20 UTC by attacker account `ddjidd564`. Three ecosystem-specific execution primitives: (1) npm postinstall hook deploys `trap-core.js` to scan for SSH keys / AWS / GitHub tokens, validate stolen credentials, and establish persistence via cron / systemd / Git hooks / SSH lateral movement; (2) PyPI import-time execution loads a remote JavaScript payload from a GitHub Pages domain (`ddjidd564.github.io`) — letting the attacker modify behavior **without publishing new versions**; (3) Crates.io `build.rs` exfiltrates wallet keystores XOR-encrypted with a hardcoded key. The headline novelty is the **AI-coding-assistant manipulation primitive**: zero-width Unicode characters injected into `.cursorrules` and `CLAUDE.md` configuration files smuggle hidden instructions telling Cursor / Claude Code / Copilot CLI agents to "perform a security scan" that surfaces and exfiltrates developer secrets to the attacker. Targets DeFi / Solana / crypto / AI development teams. Distinct from Laravel-Lang (2026-05-22 noted yesterday) and Mini Shai-Hulud Wave 2 / Megalodon — TrapDoor uses fresh-author publications rather than tag rewriting or compromised maintainer credentials.

**Timeline:** PyPI `eth-security-auditor@0.1.0` first uploaded 2026-05-22 20:20 UTC → coordinated wave releases through the weekend → Socket public disclosure + THN / SocRadar / cybersecuritynews coverage 2026-05-25 → registry takedown progress unclear at time of writing.

**Why it matters:** First documented supply-chain campaign weaponizing AI-coding-assistant configuration files to trick *the developer's AI agent itself* into being the credential-exfil vector. Zero-width Unicode injection is invisible in normal text editors and not consistently rendered by lint / pre-commit hooks — `.cursorrules` and `CLAUDE.md` inspection becomes a new mandatory step in dependency review for any team using AI coding assistants. The 384-version count + 3-ecosystem reach makes any team running unrestricted `npm install` / `pip install` / `cargo build` on developer machines a viable target — and the post-publication JavaScript payload-swap technique on PyPI means **clean-at-install-time scans are insufficient**: malicious behavior can be added later by mutating the remote payload. Combined with prior wave (Laravel-Lang 2026-05-22 tag rewriting + Mini Shai-Hulud Wave 2 + Megalodon 5,500+ GitHub-injected repos), this is the fourth distinct supply-chain primitive in 14 days — sustained tempo escalation.

**Discovered by:** Socket research team (primary disclosure 2026-05-25); SocRadar, cybersecuritynews relays.

**Mitigation:**
- Audit every npm / PyPI / Crates.io install on dev / build machines since 2026-05-22 against the Socket-published package list — pin to commit SHAs (not tags) until ecosystem cleanup confirmed.
- **Treat `.cursorrules` and `CLAUDE.md` as untrusted code**: add zero-width Unicode detection to pre-commit hooks (`grep -P "[\x{200B}-\x{200F}\x{202A}-\x{202E}\x{2060}-\x{206F}\x{FEFF}]"`) and to CI dependency-review pipelines; treat any non-ASCII content in agent-config files as suspect.
- Disable AI-coding-assistant filesystem write-out / network-egress by default in shared dev containers; require explicit per-task allowlist of egress destinations.
- Rotate any dev-machine credentials potentially in scope: AWS keys, GitHub tokens, SSH keys, browser-saved credentials, cryptocurrency wallets, environment variables (`.env`, `.aws/credentials`, `~/.ssh/`).
- Egress hunting: query DNS / proxy logs for `ddjidd564.github.io` and any pattern-matching GitHub Pages subdomains — block at perimeter.
- Treat **GitHub Pages domains** as a payload-hosting infrastructure class in your network policy — high-volume developer-tooling traffic to `*.github.io` is normal, which makes it a chronic blind spot; consider domain-categorization rather than allowlisting.
- Re-baseline AppSec policy: for every project consuming third-party packages, distrust mutable tags + mutable remote-loaded code + mutable AI-agent config files; pin SHAs and read agent-config files as part of dependency review.

**Sources:** [TheHackerNews — TrapDoor Supply Chain Attack Spreads Credential-Stealing Malware via npm, PyPI, and CratesIO](https://thehackernews.com/2026/05/trapdoor-supply-chain-attack-spreads.html) | [Socket — TrapDoor Crypto Stealer Supply Chain Attack Hits 34 Packages](https://socket.dev/blog/trapdoor-crypto-stealer-npm-pypi-crates) | [SocRadar — TrapDoor: Malicious npm, PyPI, Crates.io Packages](https://socradar.io/blog/trapdoor-npm-pypi-cratesio-secrets-ai-tooling/)

---

## 🟡 MEDIUM

### Apache Syncope CVE-2026-42782 Post-Auth RCE via Groovy Static Initializer Sandbox Bypass + CVE-2026-42797 JexlContextBuilder Info Disclosure
**Product:** Apache Syncope 3.0 → 3.0.16, 4.0 → 4.0.5, 4.1.0 | **CVE:** CVE-2026-42782, CVE-2026-42797 | **Published:** 2026-05-25 (oss-security)

Francesco Chicchiriccò posted two coordinated Apache Syncope advisories on oss-security 2026-05-25. **CVE-2026-42782 (Moderate, Improper Isolation/CWE-653)** — an administrator with `Implementations` entitlement can upload a Groovy class whose **static initializer** executes during class loading *before any sandbox/SecureASTCustomizer enforcement*. Static initializers reached a non-sandboxed execution path, granting access to `Runtime.exec` / `ProcessBuilder` / `File` / `Socket` / reflection — i.e. full JVM-level RCE on the Syncope identity-management server. Fixed in 4.0.6 / 4.1.1 by extending sandbox enforcement to static initializers via Jenkins Script Security mechanisms (SecureASTCustomizer + SandboxTransformer + runtime blacklist for high-risk APIs). **CVE-2026-42797 (Moderate)** — companion JexlContextBuilder issue leaking sensitive application context to authenticated callers without `Implementations` entitlement. Apache Syncope is widely deployed as identity-management front for enterprise-grade IAM / SSO / user-lifecycle workflows; while the primary RCE needs admin-with-Implementations privileges, Syncope deployments often expose admin consoles to administrative network segments where lateral compromise from a phished admin laptop is realistic. Public PoC details circulating via cybersecuritynews / gbhackers / cyberpress same day (2026-05-25). Credit: Trung Nguyen (CyStack).

**Mitigation:** Upgrade Apache Syncope to **4.0.6** or **4.1.1** (or **3.0.17** in the 3.x branch) immediately on every Syncope deployment. Until upgrade: (1) audit which admin users have `Implementations` entitlement and remove if not strictly needed (defense-in-depth even after upgrade); (2) restrict admin console reachability to a privileged-management network segment; (3) review Groovy implementation classes uploaded in the prior 90 days for static-initializer blocks containing `Runtime`, `ProcessBuilder`, `File`, `Socket`, or reflection — these are now indicators of pre-disclosure exploitation attempts. Treat any Syncope deployment used by IAM/SSO as crown-jewel-class: a Syncope compromise yields the ability to provision, escalate, or impersonate any managed identity.

**Sources:** [oss-security 2026-05-25 — CVE-2026-42782 Apache Syncope Post-auth RCE via Groovy static (Francesco Chicchiriccò)](https://www.openwall.com/lists/oss-security/2026/05/25/4) | [oss-security 2026-05-25 — CVE-2026-42797 JexlContextBuilder Info Disclosure](https://www.openwall.com/lists/oss-security/2026/05/25/5) | [cybersecuritynews — Apache Syncope Groovy RCE Vulnerability Let Attackers Inject Malicious Code](https://cybersecuritynews.com/apache-syncope-groovy-rce-vulnerability/)

---

### Apache Shiro Four-CVE Authentication Framework Batch — Session Fixation / Missing Cookie Secure Flag / Open Redirect / SSRF (Jakarta EE Module)
**Product:** Apache Shiro 1.0.0 → 2.1.0 (stable); 3.0.0-alpha-0 → 3.0.0-alpha-1 (alpha); Jakarta EE module | **CVE:** CVE-2026-43827, CVE-2026-43828, CVE-2026-44598, CVE-2026-48589 | **Published:** 2026-05-25 (oss-security)

Lenny Primak (Apache Shiro PMC) posted four coordinated advisories on oss-security 2026-05-25. **CVE-2026-43827 (Session fixation)** — Shiro does not invalidate the existing session nor generate a new ID after successful login by default, enabling classical session-fixation via pre-login session plant; fixed by forcing new-session-on-login. **CVE-2026-43828 (Cookie security flags)** — Shiro's native `session` and `rememberMe` cookies omit the `Secure` flag by default, exposing cookies on plaintext fallback channels. **CVE-2026-44598 (Jakarta EE: Open redirect + SSRF, requires valid credentials)** — Shiro Jakarta EE module's post-auth redirect handler accepts user-controlled host targets, yielding open redirect + SSRF from authenticated context. **CVE-2026-48589 (Jakarta EE: Open redirect via Referer)** — post-login redirect flow trusts untrusted `Referer` header, enabling spoofed redirect after auth. Apache Shiro is among the three most-deployed JVM authentication frameworks (alongside Spring Security + JAAS); session-fixation issues are particularly important for legacy Spring-MVC / Spring-Boot apps that route through Shiro for session management. Discoverer: Rasmus Moorats (43827); Lenny Primak handled remediation.

**Mitigation:** Upgrade to Shiro 2.1.1 (stable) or 3.0.0-alpha-2 (alpha). For 1.x deployments past EOL: enforce `Secure` and `HttpOnly` cookie flags via container-side configuration, configure session-on-login regeneration explicitly via `SecurityManager`, and restrict redirect targets to a hard-coded host allowlist. For Jakarta EE module users specifically: audit the post-auth redirect path for arbitrary-Referer behavior and constrain to an internal-paths-only allowlist until the upgrade lands.

**Sources:** [oss-security 2026-05-25 — CVE-2026-43827 Apache Shiro Session fixation (Lenny Primak)](https://www.openwall.com/lists/oss-security/2026/05/25/6) | [oss-security 2026-05-25 — CVE-2026-43828 Cookie Security Flags](https://www.openwall.com/lists/oss-security/2026/05/25/7) | [oss-security 2026-05-25 — CVE-2026-44598 Jakarta EE Module open redirect + SSRF](https://www.openwall.com/lists/oss-security/2026/05/25/8) | [oss-security 2026-05-25 — CVE-2026-48589 Jakarta EE Open Redirect via Referer](https://www.openwall.com/lists/oss-security/2026/05/25/9)

---

## 📋 Noted / Monitoring

**Anthropic Project Glasswing / Mythos Preview 10,000-Vulnerability Milestone Update (2026-05-22 Anthropic update, 2026-05-25 press cycle)** — Anthropic published 2026-05-22 that Mythos Preview deployed to ~50 trusted partners has collectively identified **more than 10,000 high/critical-severity vulnerabilities** in the first month (6,202 critical + 16,817 lower-tier of 23,019 total findings), thousands classified as previously-unknown zero-days. Notable disclosures referenced: 27-year-old OpenBSD bug, 16-year-old FFmpeg bug, wolfSSL certificate forgery primitive (cited as "billions of devices"). Mean time to patch: 2 weeks. Material update on the long-running Mythos/Glasswing track (first noted 2026-04-25 "271 Firefox") — defensively relevant because the **patch-availability lag becomes the operational chokepoint**, not the discovery rate. Expect a sustained vendor-advisory wave through 2026-Q3 as partners disclose disclosure-deadline-driven CVEs from this pipeline.

**TrendMicro Apex One CVE-2026-34926 KEV Promotion (2026-05-21 KEV, 2026-05-22 mainstream coverage)** — Directory-traversal flaw in on-premise Apex One added to CISA KEV 2026-05-21 alongside Langflow CVE-2025-34291. Federal deadline implied 2026-06-11. Tracked yesterday's report; no material change today.

**Drupal Core CVE-2026-9082 KEV Federal Deadline 2026-05-27 (1 Day From Now)** — Highly-critical PostgreSQL SQL injection in Drupal Core SA-CORE-2026-004; added to CISA KEV 2026-05-22 with federal deadline 2026-05-27. Active exploitation confirmed since 2026-05-22. Defender priority: any Drupal+PostgreSQL stack not yet on the patched line should treat tomorrow's window as no-grace remediation.

**FBI Kali365 OAuth Device-Code Phishing-as-a-Service Advisory (BleepingComputer 2026-05-25)** — FBI alert on phishing-as-a-service platform abusing Microsoft 365 OAuth device-code authentication flow to steal session tokens + bypass MFA on enterprise tenants. Not a new vulnerability — exploitation of the documented device-code auth weakness — but operationally relevant for blue teams; folds into the existing EvilTokens / OAuth-consent-phishing pattern (noted 2026-05-13). Defensive priority: disable device-code flow on tenant Conditional Access policy where not strictly required.

**CVE-2026-5222 Rust Cargo URL Normalization Authorization Decision (CVSS 2.3 Low, 2026-05-25)** — Cargo 1.68–1.96 vulnerable to credential leak across multiple-registry-same-domain hosting via non-canonical sparse-index URL normalization (CWE-647). Low severity; affects only multi-registry-on-same-domain deployments with arbitrary names allowed. Fix landed in Cargo PR #17031 / Rust security release 2026-05-25. Tracking — relevant for any team running private Cargo registries with multi-tenant hosting.

**Anthropic Mythos macOS M5 Kernel Memory Corruption Disclosure (Schneier 2026-05-21)** — Researchers used Anthropic Mythos to identify a kernel memory-corruption primitive on Apple M5 (no CVE published yet). Apple-hardware-specific, out-of-scope for our infrastructure focus but flagged as another datapoint in the **Mythos-finds-X** sequence — track for whether the bug yields any remote-network primitive when CVE lands.

**Google Chromium Background-JavaScript-After-Close Disclosure (BleepingComputer 2026-05-21)** — Google accidentally exposed details of an unfixed Chromium flaw where JavaScript continues executing after browser closure, enabling RCE. Browser scope and client-only — kept on Noted because **AI-coding-agent embedded browsers** (Cursor, ChatGPT Atlas, Claude Code browser tools) inherit Chromium internals and may execute attacker JS even after a developer thinks the session is closed. Watch for Chrome / Chromium emergency patch announcement.

**Apache CVE Wave (Syncope + Shiro above) — Pattern Continuation** — These two oss-security batches (six CVEs total) extend the May Apache-CVE-wave pattern observed across MINA (CVE-2026-42778/79 incomplete fix of 41409), CXF (CVE-2026-44417/44618/44930 incomplete fix of 2025-48913), Airflow (six provider advisories across 2026-05-10 → 24), Tomcat (7-CVE batch), OFBiz (17-CVE batch), Wicket (4-CVE batch), and HTTP Server (11-CVE batch). The Apache project's coordinated multi-CVE disclosure cadence remains the highest-signal monthly rhythm in the May 2026 batch — schedule a 30-day Apache-portfolio patch sprint inventory.

**WordPress Plugin Critical-Severity SQLi Batch (dbugs.ptsecurity 2026-05-25)** — Four new WP-class advisories surfaced via Patchstack relay: CVE-2026-42773 eMagicOne Store Manager (CVSS 9.3 blind SQLi, ≤1.3.2), CVE-2026-42774 Crocoblock JetEngine (CVSS 9.3 blind SQLi, ≤3.8.8.1), CVE-2026-48837 Unlimited Elements for Elementor (CVSS 8.5 blind SQLi), CVE-2026-45216 StoreApps Smart Manager (CVSS 8.8 incorrect privilege assignment). All four require attacker-controlled input reaching the vulnerable handler — typically authenticated subscriber or contributor; collectively part of the long tail of WP-class SQLi disclosures that recur every 2–3 days. Tracking, will promote individual entries if active exploitation surfaces.

**CVE-2026-45217 ThemeHigh Stripe Payment Gateway for WooCommerce Auth Bypass (Patchstack 2026-05-25, CVSS 6.5)** — Through-version 5.0.7 broken-auth vulnerability enables unauth password-recovery exploitation against WooCommerce + Stripe deployments. WordPress + payment-gateway scope; relevant given prior Funnel-Builder skimmer campaign (noted 2026-04-30) — payment-handling plugins are a current attacker focus.

**CVE-2026-31802 npm tar Path Traversal Symlink Extract (PoC public, 2026-05-25 GitHub trending)** — npm tar package vulnerable to arbitrary file overwrite via symlink extraction in crafted tar archives. Primarily client-side (developer machines extracting third-party tarballs), but folds into the broader supply-chain-on-developer-machine pattern alongside TrapDoor / Mini Shai-Hulud / Megalodon. Affected versions not yet published; tracking for fix release.

**Lazarus RemotePE Memory-Only RAT (THN 2026-05-25)** — DPRK-attributed multi-stage attack chain deploying memory-resident-only RAT against DeFi / crypto sector financial institutions. Not a vulnerability advisory — adversary tradecraft — but operationally relevant: any DeFi / crypto trading desk should incorporate memory-only payload detection into EDR tuning and validate that EDR doesn't fall back to disk-based scanning for executables loaded via reflective injection.

**Netherlands Seizes 800 Servers of Bulletproof Hosting Operator (BleepingComputer + Krebs 2026-05-22)** — Dutch authorities arrested two operators of hosting companies (Stark Industries Solutions / PQHosting / MIRhosting / the.hosting) supporting Russia-backed cyber operations. Law-enforcement action; signals continued infrastructure-takedown pressure on bulletproof hosting providers — short-term shifts in C2 hosting / phishing infrastructure may follow as operators relocate.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ |
| Vendor advisories | msrc.microsoft.com/blog, blog.cloudflare.com/tag/security, fortinet.com/blog/threat-research | ⚠️ |
| Research / OSINT | schneier.com, krebsonsecurity.com, rapid7.com, attackerkb.com, securitylab.github.com, googleprojectzero.blogspot.com, avleonov.com, kb.cert.org/vuls | ⚠️ |
| Supply chain | github.com/search?q=CVE, github.com/0xMarcio/cve, packetstormsecurity.com | ⚠️ |
| Threat intel | seclists.org/fulldisclosure, opencve.io, dbugs.ptsecurity.com, nvd.nist.gov, cve.org, cve.mitre.org | ✅ |
| Regional (RU/UA) | habr.com/ru/companies/tomhunter/articles, teletype.in/@cyberok, cert.gov.ua | ❌ |
| Vendor / BB | hackerone.com/hacktivity, bugcrowd.com/disclosures | ❌ |

**Errors:** cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403), attackerkb.com (403), msrc.microsoft.com/blog (redirect to nav-only page), hackerone.com/hacktivity (no content / JS-only), bugcrowd.com/disclosures (404), cert.gov.ua (no content).
**Degraded:** packetstormsecurity.com (redirected to packetstorm.news; homepage statistics only), habr.com/ru/companies/tomhunter/articles (no posts since March 2026), teletype.in/@cyberok (no posts since February 2026), cve.mitre.org (redirected to cve.org, JS-only content).
**Supplemental sources hit (not counted in 30):** openwall.com/lists/oss-security (2026-05-25 archive ✅ — primary source for Apache Syncope + Apache Shiro batches above); socket.dev/blog (TrapDoor campaign disclosure ✅).
**CISA KEV:** Gateway 403 — no new additions confirmed since 2026-05-22 (Drupal CVE-2026-9082 with 2026-05-27 federal deadline). Tomorrow's report should re-check KEV REST API recovery.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-26/night | Next: 2026-05-27/night*
