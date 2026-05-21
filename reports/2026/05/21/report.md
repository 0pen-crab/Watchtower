# Watchtower Night Report — 2026-05-21
**Cycle:** Night | **Generated:** 2026-05-21 06:30 UTC (2026-05-21T06:30:00Z)
**Sources checked:** 20/30 | **CISA KEV total:** unreachable via WebFetch (use Krebs/THN/SW for KEV signals) | **New KEV additions:** none confirmed today

---

## 🔴 CRITICAL

### 🔄 UPDATE — Drupal Core SA-CORE-2026-004 / CVE-2026-9082 — PostgreSQL SQL Injection Patches Shipped 2026-05-20 (CVSS Highly Critical, NIST 20/25)
**Product:** Drupal core (database abstraction API, PostgreSQL backend) | **CVE:** CVE-2026-9082 | **Status:** Patched 2026-05-20 ~17:00-21:00 UTC; PoC not yet public; mass-exploitation window opening

Yesterday we covered the pre-announce. The patch shipped on schedule and CVE-2026-9082 has now been assigned. The vulnerability is an arbitrary SQL injection in Drupal's database abstraction API that affects any site running PostgreSQL backend — anonymous (unauthenticated) attackers can send specially crafted requests resulting in SQL injection that the advisory describes as enabling "information disclosure, and in some cases privilege escalation, remote code execution, or other attacks." MySQL/MariaDB sites are NOT affected. Discoverer Michael Maturi; fix authored by Björn Brala, Benji Fisher, and the Drupal Security Team.

**Timeline:** Pre-announce PSA-2026-05-18 → patch 2026-05-20 17:00-21:00 UTC → CVE-2026-9082 assigned → today (2026-05-21) is day-0 for exploit development; per Drupal Security Team historical pattern (SA-CORE-2018-002 / Drupalgeddon 2), mass automated scanning typically begins within 12h of advisory publication and mass exploitation within 24-72h.

**Why it matters:** Drupal-on-PostgreSQL is a non-trivial fraction of internet-facing Drupal sites (Drupal supports both Postgres and MySQL, and Postgres is the standard choice for government, university, and large enterprise Drupal deployments). Every Drupal site operator on internet-facing fleet must complete patching today before adversaries weaponize the diff.

**Discovered by:** Michael Maturi (reporter); fix by Björn Brala, Benji Fisher, and Drupal Security Team.

**Mitigation:**
- Update to 11.3.10 / 11.2.12 / 11.1.10 / 10.6.9 / 10.5.10 / 10.4.10 immediately.
- For EOL 8.9.x / 9.5.x: apply manual hotfix patches published by Drupal Security Team (8.9.20 / 9.5.11) — but plan migration; future PSAs may not cover EOL branches.
- For MySQL/MariaDB-only sites: still patch (defensive depth; the DB abstraction layer fix may close other latent SQL injection paths even if the PostgreSQL-specific exploit doesn't apply).
- Day-0 detection: hunt POSTs to /node, /user, /admin/* with unusual serialized PHP payloads, JSON bodies containing PostgreSQL functions (`pg_sleep`, `pg_read_server_files`), and any new web shells dropped under sites/default/files/, sites/all/modules/.
- Drupal Steward customers already have generic protection per Drupal Security Team statement; verify Steward is active in front of your sites.

**Sources:** [Drupal Security SA-CORE-2026-004](https://www.drupal.org/sa-core-2026-004) | [BleepingComputer](https://www.bleepingcomputer.com/news/security/drupal-critical-update-to-fix-bug-with-high-exploitation-risk/) | [SecurityWeek](https://www.securityweek.com/drupal-to-patch-highly-critical-vulnerability-at-risk-of-quick-exploitation/) | [The Hacker News](https://thehackernews.com/2026/05/drupal-to-release-urgent-core-security.html)

---

## 🟠 HIGH

### 📰 NEWS — GitHub Confirms 3,800+ Internal Repos Exfiltrated via Poisoned VS Code Extension (TeamPCP)
**Product:** GitHub internal SDLC + VS Code marketplace | **CVE:** None | **First reported:** 2026-05-20

GitHub publicly confirmed that TeamPCP exfiltrated approximately 3,800-4,000 internal repositories after a single employee installed a poisoned Visual Studio Code extension on a managed device. Listed for sale on dark-web markets at $50K minimum; sample listings include GitHub Actions internal code, agentic-workflows, Copilot internals, CodeQL tooling, infrastructure code, security tooling, Codespaces, and Dependabot. GitHub asserts no customer data exposure (`"Our current assessment is that the activity involved exfiltration of GitHub-internal repositories only"`). This is the same TeamPCP cluster that ran the Mini Shai-Hulud npm waves, the TanStack compromise (which downstream caught Grafana — see below), and the prior OpenAI / Mistral AI claimed intrusions.

**Why it matters:** (1) VS Code marketplace is now an unambiguously hostile supply chain — the same threat-actor pattern that hit npm has crossed into the editor itself; default-trust on Microsoft-curated extensions is no longer safe even at GitHub. (2) The leaked corpus includes Copilot internals and Dependabot infrastructure — defensive intel on supply-chain tooling now in adversary hands. (3) Confirms the broader 2026 pattern: TeamPCP runs *both* an npm-package supply-chain campaign *and* a VS-Code-extension supply-chain campaign in parallel, and a single compromised dev machine cascades into internal repo theft at the SaaS vendor itself.

**Mitigation:**
- Inventory VS Code extensions installed on developer endpoints; baseline against known-good list, alert on new installations.
- Move VS Code extension installation behind a curated allowlist (managed via Group Policy / MDM) for engineering laptops.
- Audit GitHub Actions workflow secrets; rotate any that touched compromised infrastructure between 2026-04-01 and 2026-05-20.
- For organizations that integrate Copilot / CodeQL / Dependabot: review for any custom integration secrets that may now be referenceable from leaked internal code.
- Watch for derivative attacks using leaked Dependabot / Actions internal code as a learning aid for novel supply-chain primitives over the next 30-60 days.

**Sources:** [The Hacker News](https://thehackernews.com/2026/05/github-investigating-teampcp-claimed.html) | [BleepingComputer](https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/) | [SecurityWeek](https://www.securityweek.com/github-confirms-hack-impacting-3800-internal-repositories/)

---

### 📰 NEWS — DNS Server Coordinated Patches 2026-05-20 — Unbound 11-CVE Batch (CVE-2026-33278 Critical RCE in DNSSEC Validation) + BIND 9 6-CVE Batch (CVE-2026-3593 DoH Heap-UAF → RCE)
**Product:** NLnet Labs Unbound + ISC BIND 9 (recursive + authoritative DNS) | **CVE:** Unbound: CVE-2026-33278, CVE-2026-42944, CVE-2026-42959, CVE-2026-32792, CVE-2026-40622, CVE-2026-41292, CVE-2026-42534, CVE-2026-42923, CVE-2026-42960, CVE-2026-44390, CVE-2026-44608. BIND: CVE-2026-3039, CVE-2026-3592, CVE-2026-3593, CVE-2026-5946, CVE-2026-5947, CVE-2026-5950 | **CVSS:** Unbound CVE-2026-33278 critical; BIND CVE-2026-3593 RCE-class | **First reported:** 2026-05-20

Two of the three most-deployed open-source DNS servers (Unbound 1.25.1 and BIND 9.18.49 / 9.20.23 / 9.21.22) shipped large multi-CVE security releases on the same day, with PowerDNS shipping a separate 5-CVE batch (2026-06) at the same time. Coordination suggests joint DNS-OARC notification. The two highest-impact items:

- **CVE-2026-33278 (Unbound, CRITICAL):** Possible remote code execution during DNSSEC validation — fix in 1.25.1. Any recursive resolver doing DNSSEC validation (i.e., the default) processes attacker-controlled records. Researcher Jianjun Chen.
- **CVE-2026-3593 (BIND 9):** Heap use-after-free vulnerability in BIND 9 DNS-over-HTTPS — RCE-class. DoH endpoints are increasingly common at enterprise edge.

Lower-impact but ship-with-the-same-patch: Unbound heap overflows in EDNS option parsing (CVE-2026-42944), DNSSEC validation crash (CVE-2026-42959), possible cache poisoning during delegation following (CVE-2026-42960); BIND amplification via self-pointed glue records (CVE-2026-3592), GSS-API TKEY memory exhaustion (CVE-2026-3039).

**Why it matters:** Every recursive resolver and every authoritative DNS server in the global internet-facing surface is in scope; DNS is the universal dependency. Unbound's DNSSEC-validation RCE is the most worrying — the attack surface is "any record this resolver is asked to validate," which is unauthenticated and reachable from the open internet for any open or partially-open resolver. Patching DNS servers requires brief outages; plan a maintenance window today.

**Mitigation:**
- **Unbound:** upgrade to 1.25.1 immediately.
- **BIND 9:** upgrade to 9.18.49 / 9.20.23 / 9.21.22.
- **PowerDNS:** upgrade to 4.9.15 (Authoritative) or 5.0.5 (with views/TCP-Proxy).
- Audit DoH-enabled BIND endpoints; restrict source IPs to known clients until patched.
- Confirm DNSSEC validation is happening on a patched Unbound (do not turn off DNSSEC as a workaround — that opens worse problems).
- Monitor recursive resolver logs for query patterns associated with DNSSEC validator crash / RCE attempts; ISC and NLnet Labs are expected to publish IOCs in follow-up.

**Sources:** [oss-security: BIND 9](https://www.openwall.com/lists/oss-security/2026/05/20/11) | [oss-security: Unbound 1.25.1](https://www.openwall.com/lists/oss-security/2026/05/20/5) | [oss-security: PowerDNS 2026-06](https://www.openwall.com/lists/oss-security/2026/05/20/12)

---

### 📰 NEWS — authentik CVE-2026-40165 — SAML NameID XML Comment Injection Authentication Bypass (CVSS 8.7)
**Product:** authentik (open-source identity provider) | **CVE:** CVE-2026-40165 | **CVSS:** 8.7 (High) | **First reported:** 2026-05-20

The widely deployed authentik IdP (used at significant enterprise + cloud-native scale) is vulnerable to a SAML NameID XML comment injection that enables authentication bypass — a class of bug well-known since the OneLogin SAML disclosures of 2018, but persistently re-emerging in newer SAML stacks. An attacker who controls or is in the trust path of a SAML assertion can inject XML comments inside NameID to confuse the parser and impersonate other users. Fixed in 2025.12.5 and 2026.2.3.

**Why it matters:** authentik fronts large numbers of internal applications and SSO logins; an auth-bypass at the IdP cascades into every dependent application. Many self-hosted Kubernetes operators (Argo CD, Grafana, internal portals) use authentik as the SAML/OIDC provider — exploitation impacts the blast radius of the entire SSO trust mesh.

**Mitigation:**
- Upgrade authentik to 2025.12.5 (LTS branch) or 2026.2.3 (current branch).
- Until patched, audit SAML assertion logs for NameID values containing `<!--` or `-->` substrings, or unusual XML structure.
- Verify all SAML SPs downstream of authentik consult username-based identity attributes that cannot be confused by NameID parser issues.

**Sources:** [app.opencve.io: CVE-2026-40165](https://app.opencve.io/cve/CVE-2026-40165)

---

### 🔄 UPDATE — Microsoft DCU 'Fox Tempest' MSaaS Takedown Expands — 4 New Ransomware Affiliates Named (INC, Qilin, BlackByte, Akira) + 3 Malware Families (Oyster, Lumma, Vidar)
**Product:** Microsoft Artifact Signing (abused) + downstream Windows code-signing trust | **CVE:** None | **Status:** Disrupted 2026-05-19; expanded attribution 2026-05-20

Yesterday's coverage captured the Microsoft DCU takedown of `signspace.cloud` and the initial four named ransomware affiliates (Vanilla Tempest / Storm-0501 / Storm-2561 / Storm-0249). Microsoft's 2026-05-20 expanded statement now adds **INC, Qilin, BlackByte, and Akira** ransomware operations to the affiliated cluster, plus three additional malware families distributed via Fox Tempest's signed-binary delivery — **Oyster (aka Broomstick/CleanUpLoader), Lumma Stealer, and Vidar**. Targeted regions: US, France, India, China; sectors: healthcare, education, government, financial services. Court documents reference a cooperative source who purchased the service Feb-Mar 2026; the service had pivoted in Feb 2026 to delivering pre-configured Cloudzy-hosted VMs to ransomware customers.

**Why it matters:** The retroactive-hunt aperture is now much wider — Akira / INC / Qilin / BlackByte are top-10 ransomware operators globally, and any incidents from these crews in 2026 should be reviewed against the revoked-certificate thumbprint set. Lumma + Vidar are commodity infostealers — every credential-theft incident from these families in the affected window should now be re-investigated with the assumption that the dropper binary may have been Authenticode-signed via the revoked certs.

**Mitigation:**
- Run a 90-day retroactive EDR / AV / WDAC / Defender ASR log hunt for executions of binaries signed by certificates in the revoked thumbprint set (Microsoft has published the revocation list).
- Map Lumma / Vidar / Oyster credential-theft incidents in your environment from Feb-May 2026 against the Fox Tempest signed-binary delivery hypothesis.
- For environments running Authenticode-trust enforcement: verify CRL / OCSP enforcement is hard-fail or short-cache (24h max); cached trust decisions are now a known-bad property.
- Treat Microsoft Threat Intelligence named-cluster attribution (Storm-XXXX, Vanilla Tempest, etc.) as a defensive IR layer to align playbooks against; the Storm cluster numbering correlates against MS attribution graphs.

**Sources:** [The Hacker News](https://thehackernews.com/2026/05/microsoft-takes-down-malware-signing.html) | [SecurityWeek](https://www.securityweek.com/microsoft-disrupts-malware-signing-service-run-by-fox-tempest/) | [BleepingComputer](https://www.bleepingcomputer.com/news/security/cybercrime-service-disrupted-for-abusing-microsoft-platform-to-sign-malware/)

---

## 🟡 MEDIUM

### 📰 NEWS — SonicWall Gen6 SSL-VPN CVE-2024-12802 MFA Bypass Actively Exploited Feb-Mar 2026 (Incomplete-Patch + EOL Convergence)
**Product:** SonicWall SSL-VPN (Gen6) | **CVE:** CVE-2024-12802 | **Published:** 2024 (re-surfaced 2026-05-20 with active exploitation reporting)

ReliaQuest published a writeup documenting active exploitation of CVE-2024-12802 — an MFA bypass on SonicWall Gen6 SSL-VPN appliances where the firmware patch alone is insufficient and administrators must also delete + re-create the LDAP configuration without `userPrincipalName` to fully close the gap. Gen6 reached EOL on 2026-04-16, meaning many sites are running unpatched Gen6 with the MFA-bypass surface live. Attacker pattern observed: credential brute-force → MFA bypass via UPN login → 30-60 minute recon → RDP via shared-local-admin credentials → ransomware deployment. Multiple sectors affected.

**Mitigation:** Inventory SonicWall SSL-VPN deployments; for Gen6 customers — apply the firmware *and* the manual LDAP reconfiguration (delete config, remove cached users, remove SSL VPN User Domain, reboot, recreate LDAP without UPN), or accelerate migration off Gen6 entirely. For Gen7/Gen8 the firmware patch is sufficient. Hunt for `sess="CLI"` indicator (scripted auth), event IDs 238 and 1080, VPN logins from suspicious VPS/VPN infrastructure.

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-bypass-sonicwall-vpn-mfa-due-to-incomplete-patching/)

---

### 📰 NEWS — EvilTokens OAuth Consent Phishing-as-a-Service — 340+ Microsoft 365 Organizations Compromised in 5 Weeks
**Product:** Microsoft 365 OAuth consent flow | **CVE:** None | **Published:** 2026-05-20

EvilTokens, a phishing-as-a-service platform launched February 2026, has compromised 340+ Microsoft 365 organizations across five countries by abusing the legitimate OAuth device-code consent flow. Victims are sent to `microsoft.com/devicelogin`, enter a short code, complete real MFA, and then click Accept on a consent screen — attacker walks away with valid refresh tokens scoped to Mail/Drive/Calendar/Contacts. MFA cannot block this; the tokens are issued by the legitimate identity provider as designed. Tokens then operate outside traditional sign-in event logging that most SIEMs watch.

**Mitigation:** This is a M365 architectural-posture problem, not a patchable bug. Recommended actions: (1) inventory OAuth applications consented in your tenant; review any app granted broad Mail.ReadWrite / Files.ReadWrite by user-level consent; (2) restrict user consent to verified-publisher apps only (admin consent for everything else); (3) build SIEM detections that fire on `Add app role assignment grant to user` / `Consent to application` events, not just sign-in events; (4) enable Continuous Access Evaluation for token-level revocation; (5) baseline expected OAuth grants and alert on anomalies (especially apps with three+ delegated permissions).

**Sources:** [The Hacker News](https://thehackernews.com/2026/05/the-new-phishing-click-how-oauth.html)

---

### 📰 NEWS — Anthropic Claude Code SOCKS5 Null-Byte Injection Sandbox Bypass — Silently Patched 2026-03-31, Disclosed 2026-05-20 (No CVE Assigned)
**Product:** Anthropic Claude Code (CLI agent) | **CVE:** None assigned by vendor (researcher criticized this publicly) | **Published:** 2026-05-20

Researcher Aonan Guan disclosed that between October 2025 and 2026-03-31, Claude Code's outbound network filter could be bypassed via a SOCKS5 hostname null-byte injection: an attacker-controlled prompt instructs the agent to connect to `attacker-host.com\x00.google.com`. The filter approves on the `.google.com` suffix; the OS truncates at the null byte and dials the attacker. Chained with prompt-injection (researcher named the chain "Comment and Control"), this enables exfiltration of environment variables, API tokens, and infrastructure data from any system running Claude Code. Fixed in commit 2026-03-27, shipped in Claude Code 2.1.88 on 2026-03-31. Anthropic declined to assign a CVE.

**Why it matters:** Sixth AI-agent attack-surface disclosure in 60 days (per our prior coverage of similar issues in OpenClaude, GitHub Copilot CLI, FastGPT, PenPot MCP, Coder). The pattern is consistent: agent sandboxes consistently fail to handle classic OS-level escape primitives (null byte, IFS, env injection) when interpreting model-controlled network targets. Treat any LLM-agent with outbound network capability as a sandbox-escape candidate by default.

**Mitigation:** Update Claude Code to 2.1.88+. For developer endpoints running any LLM-agent: prefer egress through a controlled HTTP proxy that doesn't truncate hostnames at null bytes and that enforces allowlists at the proxy, not in-process.

**Sources:** [SecurityWeek](https://www.securityweek.com/anthropic-silently-patches-claude-code-sandbox-bypass/)

---

### 📰 NEWS — rsync 3.4.3 — 6-CVE Batch Including CVE-2026-43618 (CVSS 8.1) Authenticated User Memory Disclosure + CVE-2026-29518 (CVSS 7.3) Daemon TOCTOU PrivEsc
**Product:** rsync (daemon + client) | **CVE:** CVE-2026-29518, CVE-2026-43617, CVE-2026-43618, CVE-2026-43619, CVE-2026-43620, CVE-2026-45232 | **Published:** 2026-05-20

rsync 3.4.3 fixes six security issues in versions 3.4.2 and earlier. The two most impactful: **CVE-2026-43618 (8.1 HIGH)** integer overflow in the compressed-token decoder enables remote memory disclosure to authenticated rsync daemon users (credentials, pointers, cleartext file content); **CVE-2026-29518 (7.3 HIGH)** TOCTOU symlink race in daemon mode without chroot enables privilege escalation. Lower-severity items: hostname/ACL bypass when DNS resolution unsupported (CVE-2026-43617), receiver OOB read DoS via malicious server (CVE-2026-43620), HTTP CONNECT proxy off-by-one (CVE-2026-45232).

**Mitigation:** Upgrade to 3.4.3 on every rsync daemon and client (build/deploy infrastructure, backup pipelines, CI mirrors). For deployments using `use chroot = no` (common where chroot would break cross-volume sync), CVE-2026-29518 / CVE-2026-43619 are exploitable by any authenticated rsync user — prioritize. For receivers pulling from untrusted servers (mirror clients): CVE-2026-43620 is reachable from any malicious server.

**Sources:** [oss-security: rsync 3.4.3](https://www.openwall.com/lists/oss-security/2026/05/20/6)

---

### 📰 NEWS — CVE-2026-24425 Twig Sandbox Bypass → Full RCE (CVSS 8.8) — Affects All 2.16.x + 3.9.0-3.25.x
**Product:** Twig PHP templating engine (used by Drupal, Symfony, eZ Platform, Craft CMS, many SaaS multi-tenant PHP apps) | **CVE:** CVE-2026-24425 | **CVSS:** 8.8 (High) | **Published:** 2026-05-20

Twig's `SourcePolicyInterface`-based sandbox can be bypassed to achieve full RCE by passing arbitrary PHP callables into `sort`, `filter`, `map`, and `reduce` filters. Attacker needs the ability to submit a Twig template (i.e., low-privilege access to a multi-tenant PHP app that lets users author templates). Fixed in Twig 3.26.0+.

**Why it matters:** Twig is widely embedded in Drupal, Symfony, and multi-tenant CMS / e-commerce platforms — multi-tenant SaaS where customers can write Twig fragments (storefront templates, email templates, page layouts) is the primary risk surface. Less impactful for vanilla Drupal sites where templates are admin-only, but in conjunction with today's Drupal SA-CORE-2026-004 (auth-bypass + admin escalation chain), this could become a secondary RCE primitive in compromised sites.

**Mitigation:** Upgrade Twig to 3.26.0+. For multi-tenant PHP platforms — audit which trust tier can submit Twig content; restrict to vetted templates until upgrade is complete; disable `SourcePolicyInterface` if sandbox is non-essential.

**Sources:** [app.opencve.io: CVE-2026-24425](https://app.opencve.io/cve/CVE-2026-24425)

---

## 📋 Noted / Monitoring

**CVE-2026-46339 (9router npm)** — Unauthenticated RCE via unprotected MCP custom plugin routes; published 2026-05-19 GHSA database; ninth MCP-server-class CVE in 60 days — pattern of MCP frameworks shipping with unauth routes continues unabated.

**CVE-2026-46421 (@cap-js/db-service npm)** — Mini Shai-Hulud Wave 3 extension; supply-chain compromise pattern continues into SAP Cloud Application Programming Model ecosystem. Already in scope for yesterday's Wave 3 coverage.

**CVE-2026-45758 (guardrails-ai pip)** — Supply-chain compromise on AI-safety package; meta-irony aside, this is another pip-side data point on the broader 2026 supply-chain wave.

**CVE-2026-7637 (WordPress Boost plugin by PixelYourSite)** — Unauth PHP Object Injection (CVSS 9.8) via STYXKEY-BOOST_USER_LOCATION cookie; plugin itself has no internal gadget chain, so impact depends on coexisting vulnerable plugins/themes — typical of "9.8 but only chains" PHP-object-injection issues.

**CVE-2026-8468 (Plug Erlang)** — Unbounded buffer accumulation in multipart header parsing → DoS on any Erlang/Elixir Plug-based web service (Phoenix Framework backbone). DoS-only, but Phoenix deployments are non-trivial in our scope.

**CVE-2026-4802 (Cockpit)** — Arbitrary code execution in the logs page via crafted link; affects Cockpit admin UI on Red Hat / Fedora servers. Admin-side, lower priority.

**CVE-2026-41054 (haveged)** — Local root privilege escalation via command socket; remains LPE-only as we noted yesterday. Patch when convenient.

**CVE-2026-24213, CVE-2026-24214 (NVIDIA Triton Inference Server, DALI backend)** — OOB read with CVSS 8.0; authenticated low-priv attacker. AI-inference servers continue to be a CVE-prolific surface.

**CVE-2026-24163 (NVIDIA TRT-LLM)** — CVSS 9.8 issue per dbugs.ptsecurity.com listing; details not yet public. Track for NVIDIA PSIRT bulletin.

**phpMyFAQ batch (GHSA-w9xh, GHSA-gp95, GHSA-xvp4, GHSA-9qv9)** — Four high-severity advisories: missing password-reset token enables account takeover, default empty API token auth bypass, IDOR, unauthenticated password-reset endpoint. phpMyFAQ deployment surface is narrow, but exploitation chains are trivial — patch if you run phpMyFAQ.

**VU#980487 Linux Kernel 'Dirty Frag' LPE** — CERT/CC vulnerability note published 2026-05-20; appears to be CERT/CC's coordination note covering the Dirty Frag / CopyFail / DirtyDecrypt / Fragnesia family already extensively covered in prior reports — no new CVE.

**CVE-2026-43067 Linux kernel block allocation wraparound (CVSS 9.8)** — Listed in app.opencve.io for 2026-05-20; indirect-mapped file scope; details limited — monitor for distro advisories.

**P2PInfect Kubernetes/Redis compromise (FortiGuard Labs 2026-05-20)** — Multiple GKE clusters compromised via unprotected Redis instances; persistent and dormant malware on misconfigured K8s. Not a new CVE but data point on the persistent risk of internet-reachable Redis on cloud Kubernetes.

**Webworm EchoCreep / GraphWorm Discord + Microsoft Graph API C2 (China-aligned)** — APT C2 abusing Discord and Graph API for command-and-control. Threat-intel reporting, not a vulnerability advisory; valuable for detection engineers tracking Graph API abuse signatures.

**PinTheft Arch Linux LPE** — Public PoC released on patched flaw; Arch-only; LPE-only — out of remote-services scope.

**Discord default-on E2EE for voice/video calls (continued rollout)** — Defensive positive; affects forensic visibility of Discord-based threat-actor coordination (relevant for IR teams that monitor Discord for credential market chatter).

**Grafana TanStack downstream breach disclosed 2026-05-19** — Already implicitly covered by Mini Shai-Hulud Wave 2 reporting; today's incremental detail is "single missed GitHub workflow token allowed continued access" — illustrates the breach-response-rotation gap pattern noted in MEMORY.

**Mini Shai-Hulud Wave 3 — VS Code + Claude Code config persistence backdoor (Aikido)** — Already covered yesterday in the Wave 3 update; today's incremental detail (Aikido's persistence-mechanism documentation) doesn't escalate threat score.

**SHADOW-EARTH-053/054 cluster activity** — Per MEMORY note; no fresh public reporting today.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com | ✅ |
| Industry research | schneier.com, rapid7.com, fortinet.com/threat-research, securitylab.github.com, blog.cloudflare.com/security, avleonov.com | ✅ |
| Vendor / CERT | drupal.org/security, kb.cert.org/vuls, fortiguard.fortinet.com/psirt | ✅ |
| CVE indexes | opencve.io (via app.opencve.io), github.com/advisories, dbugs.ptsecurity.com, github.com/0xMarcio/cve | ✅ |
| Mailing lists | seclists.org/fulldisclosure, openwall.com/lists/oss-security | ✅ |
| Russian-language threat intel | habr.com/ru/companies/tomhunter, teletype.in/@cyberok | ⚠️ (no new May posts) |
| Project Zero | projectzero.google | ✅ (no posts in window) |
| GitHub search | github.com/search?q=CVE | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (403 Forbidden via WebFetch) |
| Microsoft MSRC | msrc.microsoft.com/blog, msrc.microsoft.com/update-guide | ❌ (no content via WebFetch) |
| HackerOne / Bugcrowd | hackerone.com/hacktivity, bugcrowd.com/disclosures | ❌ (JS-only / 404) |
| NVD / MITRE | nvd.nist.gov, cve.mitre.org, cve.org | ❌ (JS-only / unreachable) |
| Packetstorm | packetstormsecurity.com → packetstorm.news | ⚠️ degraded (homepage only) |
| AttackerKB | attackerkb.com | ❌ (403 Forbidden) |
| CERT-UA | cert.gov.ua | ❌ (no content via WebFetch) |

**Errors:** 10 sources unreachable via WebFetch (CISA x2, AttackerKB, NVD, cve.mitre, cve.org, MSRC, HackerOne, Bugcrowd, CERT-UA); 1 degraded (Packetstorm — returned homepage only). All compensated for via primary news outlets (BleepingComputer / THN / SecurityWeek typically relay KEV additions and MSRC bulletins within 6-12h).

**CISA KEV:** unreachable via WebFetch today. Per cross-reference from THN/BC: no new KEV additions confirmed 2026-05-21. Drupal CVE-2026-9082 not yet in KEV (patch only ~14h old at report time); expect addition within 48-72h if exploitation activity is observed.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-21/night | Next: 2026-05-22/night*
