# Watchtower Night Report — 2026-06-02
**Cycle:** Night | **Generated:** 2026-06-02 06:00 UTC (2026-06-02T06:00:00Z)
**Sources checked:** 22/30 | **CISA KEV total:** unreachable (cisa.gov 403) | **New KEV additions:** unknown (KEV endpoint unreachable)

---

## 🔴 CRITICAL

### Windows Netlogon CVE-2026-41089 — Pre-Auth RCE on Domain Controllers Now Actively Exploited 20 Days After May Patch Tuesday (CVSS 9.8)
**Product:** Microsoft Windows Server (Netlogon service) | **CVE:** CVE-2026-41089 | **Status:** Patched (May 2026 PT) + Active Exploitation

Stack-based buffer overflow in the Windows Netlogon service permits an unauthenticated remote attacker to execute code on a domain controller with no prior access via crafted network requests. Microsoft shipped the patch in the May 2026 Patch Tuesday wave (2026-05-12) but did **not** flag CVE-2026-41089 as "Exploitation More Likely" — the bug sat under the radar in the 137-CVE batch and went uncovered by the major Patch Tuesday relayers. The Centre for Cybersecurity Belgium (CCB) confirmed active in-the-wild exploitation on 2026-06-01, with Microsoft's advisory still not updated at time of publication.

**Timeline:** Patched silently 2026-05-12 → Belgian CCB warning published 2026-06-01 → mainstream coverage 2026-06-01/02. ~20-day exploitation lead-time on unpatched fleets.

**Why it matters:** Netlogon is the canonical Active Directory authentication primitive; a pre-auth RCE on the domain controller is, by definition, full-tier-0 compromise of the Windows authentication forest — equivalent to Zerologon (CVE-2020-1472) in blast radius. Any DC reachable from a beachhead host (and most are, internally) is now full-domain takeover. **Fourth confirmed 60-day instance of the Patch Tuesday relayer-divergence pattern** (MDASH CVE-2026-33824 May 2026, Azure-adjacent CVSS-10 cluster MEMORY 2026-05-22, SharePoint CVE-2026-45659 MEMORY 2026-05-27, now Netlogon CVE-2026-41089) — single-relayer Patch Tuesday triage is structurally unsafe.

**Discovered by:** Exploitation reported by Centre for Cybersecurity Belgium (CCB).

**Mitigation:**
- Confirm KB5089549 (or successor) is installed on every domain controller in the fleet (every primary, BDC, and read-only DC).
- Hunt EDR for unexpected `lsass.exe` child processes / Netlogon-service-account-spawned shells on DCs from 2026-05-12 to present.
- Restrict inbound 445/TCP and 135/TCP from non-DC subnets; segment domain-controller VLAN if not already.
- Refresh KRBTGT password twice (24h apart) on any DC that may have been compromised; rotate every machine and service account.
- Expect KEV addition within 48-72h with short federal deadline.

**Sources:** [BleepingComputer — Critical Windows Netlogon RCE flaw now exploited in attacks](https://www.bleepingcomputer.com/news/security/critical-windows-netlogon-rce-flaw-now-exploited-in-attacks/) | [SecurityWeek — Critical Windows Netlogon Vulnerability in Attackers' Crosshairs](https://www.securityweek.com/critical-windows-netlogon-vulnerability-in-attackers-crosshairs/) | [TheHackerNews — Weekly Recap](https://thehackernews.com)

---

## 🟠 HIGH

### Miasma Supply-Chain Worm — 7 @redhat-cloud-services npm Packages Trojanized, Mini Shai-Hulud Variant with Anthropic-API-Impersonator Exfiltration
**Product:** npm @redhat-cloud-services namespace | **CVE:** None assigned (supply-chain compromise) | **CVSS:** N/A | **First reported:** 2026-06-01

A compromised Red Hat employee GitHub account was used to inject orphan commits adding a malicious `preinstall` hook into seven @redhat-cloud-services npm packages: `vulnerabilities-client`, `tsc-transform-imports`, `topological-inventory-client`, `sources-client`, `rule-components`, `remediations-client`, `rbac-client`. Combined weekly download footprint is ~117,000. The payload — a Mini Shai-Hulud derivative branded "Miasma" — harvests GitHub Actions secrets, npm/PyPI publishing tokens, AWS/GCP/Azure credentials, HashiCorp Vault tokens, Kubernetes service account tokens, SSH keys, Docker credentials, GPG keys, and `.env` files. Novel exfiltration uses **`api.anthropic[.]com:443/v1/api` (a Subdomain spoof of the real Anthropic API endpoint at api.anthropic.com)** with GitHub as fallback channel. First "Miasma: The Spreading Blight" commit landed 2026-05-29. Coordinated disclosure by Socket / Aikido / JFrog / Microsoft / OX Security / SafeDep / StepSecurity / Wiz on 2026-06-01.

**Why it matters:** First major Shai-Hulud-class re-use of TeamPCP's open-sourced worm (per MEMORY 2026-05-19 prediction: "3-7 distinct Wave-2-class supply-chain compromises by 2026-06-15" — Miasma is #2 after _deadcode09284814_ chalk-template). Two novel deltas vs. Wave 2: (a) **cloud-identity collectors for GCP and Azure access-token enumeration** (Wave 2 was AWS-centric), and (b) **per-infection unique-encrypted payloads** defeating signature-based defenses. The Anthropic-API-impersonator C2 (`api.anthropic[.]com` typo / TLS-cert-grab) is a new blue-team detection blind spot — outbound to `api.anthropic.com` would normally be allow-listed for any environment running Claude integrations. Treat every dev/CI runner that resolved an @redhat-cloud-services package between 2026-05-29 and 2026-06-01 as fully credential-compromised.

**Mitigation:**
- Audit `package-lock.json` / `yarn.lock` / `pnpm-lock.yaml` for any @redhat-cloud-services version published 2026-05-29 → 2026-06-01; rip out and rebuild from a clean cache.
- Add network egress block for `api.anthropic[.]com` (the typo-squat domain, distinct from `api.anthropic.com`) on every dev/CI runner.
- Rotate every secret resident in any GHA workflow that pulled these packages in the window: GitHub PATs, npm/PyPI tokens, GCP/Azure/AWS credentials, Vault tokens, K8s SA tokens, SSH keys, Docker registry creds.
- Block install-time scripts where feasible (`npm config set ignore-scripts true`) on CI; enforce on dev workstations via policy.
- Hunt for the IOC: orphan-commit-then-publish pattern in private repos (the same technique as Wave 2 TanStack).

**Sources:** [BleepingComputer — Red Hat npm packages compromised to steal developer credentials](https://www.bleepingcomputer.com/news/security/red-hat-npm-packages-compromised-to-steal-developer-credentials/) | [TheHackerNews — Miasma Supply Chain Attack Compromises Red Hat npm Packages](https://thehackernews.com/2026/06/miasma-supply-chain-attack-compromises.html)

---

### codexui-android npm — OpenAI Codex Refresh-Token Theft via Trojan Package, ~30K Weekly Downloads, Month-Long Exfiltration Window
**Product:** OpenAI Codex CLI (`~/.codex/auth.json`) | **CVE:** None assigned | **CVSS:** N/A | **First reported:** 2026-06-01

Malicious npm package `codexui-android` (~29,000 weekly downloads, first published 2026-04-10) silently exfiltrated `access_token`, `refresh_token`, `id_token`, and `account_id` from every developer's `~/.codex/auth.json` for ~50 days before discovery by Aikido Security researcher Charlie Eriksen. Exfiltration target `sentry.anyclaw[.]store` was registered 2026-04-12 (two days after the malicious package's first publication), masquerading as the legitimate Sentry observability platform. The malicious code was also distributed as Android app **"OpenClaw Codex Claude AI Agent"** (50,000+ downloads) running the npm package inside a PRoot sandbox, sending the same credentials to the same exfil endpoint from version 0.1.82.

**Why it matters:** **Refresh tokens for OpenAI Codex do not expire** — Eriksen specifically notes this gives the attacker "silent impersonation indefinitely" of every developer who installed the package since 2026-04-10. This is the first publicly documented AI-coding-agent refresh-token-as-permanent-key class compromise, extending the AI-agent-sandboxed-workspace-data exfiltration class (MEMORY 2026-05-27 mouse5212 `/mnt/user-data`) into **token-theft-as-persistent-AI-coding-agent-impersonation**. Defensively: AI-coding-agent credentials need the same "treat as long-lived API key" handling as cloud root accounts.

**Mitigation:**
- Revoke and reissue every OpenAI Codex CLI session for any developer who installed `codexui-android` since 2026-04-10 (check shell history + npm install logs).
- Pull the Android app "OpenClaw Codex Claude AI Agent" from any corporate-managed device immediately.
- Block `sentry.anyclaw[.]store` at the DNS resolver and add SNI-block to egress proxies; alert on retroactive history matches.
- Request OpenAI account-level audit log review for unexpected Codex API calls since 2026-04-10.
- Treat every `~/.codex/auth.json` (and `~/.claude/credentials.json`, `~/.gemini/credentials.json`, `~/.cursor/*`) as long-lived secrets — back them up to per-workstation Hardware Security Module storage where possible, never to shared dotfiles repos.

**Sources:** [TheHackerNews — OpenAI Codex Authentication Tokens Stolen in codexui-android npm Supply Chain Attack](https://thehackernews.com/2026/06/openai-codex-authentication-tokens.html)

---

### Vitest CVE-2026-47429 + CVE-2026-47428 — Critical RCE in Widely-Deployed JavaScript Test Framework via UI / Browser Mode
**Product:** Vitest (Node.js testing framework) | **CVE:** CVE-2026-47429 (vitest), CVE-2026-47428 (@vitest/browser) | **CVSS:** 9.8 / 9.6 | **First reported:** 2026-05-30/31

Two critical advisories landed against Vitest, one of the most widely-deployed JavaScript testing frameworks (millions of weekly downloads, default in Vite/Vue/Svelte ecosystems): (1) **CVE-2026-47429 (CVSS 9.8) — arbitrary file read + RCE in Vitest UI mode** via `isFileServingAllowed` bypass using Windows path-traversal syntax `\\?\\..\\`; affects every developer who runs `vitest --ui --api.host` to expose the test UI to LAN or container network. (2) **CVE-2026-47428 (CVSS 9.6) — XSS-to-RCE in @vitest/browser** via unsanitized `otelCarrier` query parameter rendered as inline script in the browser-runner; attacker URL → JS execution in Vitest server origin → `VITEST_API_TOKEN` recovery → authenticated file-write API → Node.js config file injection → RCE. No active in-the-wild exploitation confirmed yet but both bugs have public technical detail in the GHSA advisories.

**Why it matters:** Vitest is in the dependency tree of virtually every modern JavaScript project that has any unit-test coverage — it is to Vite what Jest is to Webpack. Most teams run the UI/browser mode at least occasionally during local development; many CI pipelines run Vitest browser mode with `--api.host` exposed for distributed testing or in containers. **Extends the test/dev-framework as RCE vector class** (joins Jenkins MEMORY 2026-05-27, esm.sh MEMORY 2026-05-13, GitHub Actions Wave 2 MEMORY 2026-05-13). Patch the dev/CI fleet *before* a public PoC drops — the attack vector is trivially adapted from the GHSA narrative.

**Mitigation:**
- Upgrade `vitest` to ≥ 4.1.6 (or ≥ 5.0.0-beta.3 for the 5.x track) on every project that uses it; upgrade `@vitest/browser` to the matching version.
- In Vitest 4.1.0+, the new `allowWrite` / `allowExec` config flags default to **disabled** on non-localhost binds — do not override unless absolutely required.
- Inventory CI workflows for `vitest --ui` / `--api.host` exposed beyond localhost; either bind back to 127.0.0.1 or upgrade and audit `allowWrite`/`allowExec` posture.
- Review developer workstations for stale Vitest installs (older than 4.1.6); the IDE plug-in may auto-launch a UI server.

**Sources:** [GitHub Advisory GHSA-5xrq-8626-4rwp (CVE-2026-47429)](https://github.com/advisories/GHSA-5xrq-8626-4rwp) | [GitHub Advisory GHSA-2h32-95rg-cppp (CVE-2026-47428)](https://github.com/advisories/GHSA-2h32-95rg-cppp)

---

## 🟡 MEDIUM

### Operation Dragon Weave (China-Aligned) — AZUREVEIL AdaptixC2 Agent Using Microsoft Azure Blob Storage as Dead-Drop C2 Against Czech Republic + Taiwan
**Product:** Government/research/academic/finance victims in CZ + TW | **CVE:** N/A (campaign) | **Published:** 2026-06-01

Seqrite Labs disclosed a sustained China-aligned cyber-espionage campaign codenamed **Operation Dragon Weave** targeting government, research, academic, technology, and financial-services organizations in the Czech Republic and Taiwan. Infection chain begins with spear-phishing emails containing ZIP attachments; two distinct execution paths — (a) malicious LNK masquerading as PDF → PowerShell, or (b) Rust-based dropper executed directly from the archive — both leading to **RUSTCLOAK loader** that decrypts the final payload: **AZUREVEIL, a custom AdaptixC2 agent** with 36 commands (file ops / shell / process / port-forwarding / in-memory BOF). Novel TTP: **C2 uses Microsoft Azure Blob Storage containers as dead-drop transport** rather than direct connect, blending with legitimate Azure traffic.

**Why it matters:** AZUREVEIL's Azure-Blob-as-dead-drop C2 is the latest entry in the **commercial-cloud-storage-as-covert-channel cluster** (joins GitHub Calendar / Solana blockchain / BitTorrent DHT from MEMORY 2026-04-28 GlassWorm and ChatGPT-shared-page renderer from MEMORY 2026-05-30 ChatGPhish). DNS/SNI-based egress controls become useless against a victim that legitimately needs Azure connectivity. Defensive priority: monitor for Azure Storage requests with unusual access patterns from endpoints that do not normally consume Azure resources, and pay attention to AdaptixC2 (an open-source post-exploit framework increasingly used by state-aligned actors as a low-attribution Cobalt Strike alternative).

**Mitigation:**
- Hunt for the RUSTCLOAK loader IOCs and AdaptixC2 process artifacts on endpoints in the CZ/TW operating perimeter (and any global subsidiary).
- Block egress to Azure Blob containers not belonging to your tenant; for low-Azure environments, allow-list specifically named storage accounts only.
- Phishing-awareness reinforcement: ZIP attachments containing PDF-icon LNKs remain the dominant initial-access vector for this cluster.

**Sources:** [TheHackerNews — China-Aligned Groups Ramp Up Attacks: Dragon Weave](https://thehackernews.com/2026/06/china-aligned-groups-ramp-up-attacks.html)

---

### DriveSurge IAB — Thousands of Compromised Sites Funnel Users into ClickFix + FakeUpdate Chains via zTDS, Now Targeting macOS
**Product:** Compromised web infrastructure (WordPress + generic CMS) | **CVE:** N/A (campaign) | **Published:** 2026-06-01

Silent Push disclosed **DriveSurge**, a pay-per-install initial-access broker active since September 2025 that hijacks thousands of public-facing websites to redirect visitors through a custom traffic-distribution system (**zTDS**) and serve them either ClickFix or FakeUpdate social-engineering lures (fake Firefox / Chrome / Edge / Safari / Opera / Brave / Yandex / Vivaldi / Samsung Internet / UC Browser updates). One analyzed delivery contained a multi-DLL ZIP + malicious executable; a separate observed payload was a JavaScript variant specifically obfuscated for **macOS desktop targets** — extending the ClickFix attack surface beyond Windows.

**Why it matters:** Major enterprises are already heavily defended against single-host malicious-redirect chains, but the zTDS multi-stage profiling makes lure delivery selective and noisy enough to defeat URL-reputation-based controls. The **macOS targeting** is the durable signal — ClickFix + FakeUpdate has been Windows-only for the last 18 months, so macOS fleet defenders should re-evaluate browser-update legitimacy training and SmartScreen-equivalent posture on Macs.

**Mitigation:**
- Block known zTDS infrastructure at the DNS/proxy layer (Silent Push has IOC bundle).
- Training reinforcement: legitimate browser updates *never* require manual ZIP download or "press Win+R / Cmd+Space" prompts.
- macOS users: Gatekeeper + XProtect + LuLu-style egress alert tooling — review fleet endpoint baseline.

**Sources:** [BleepingComputer — Hackers hijack thousands of sites for ClickFix and FakeUpdate attacks](https://www.bleepingcomputer.com/news/security/hackers-hijack-thousands-of-sites-for-clickfix-and-fakeupdate-attacks/)

---

### WordPress Steam-Profile-as-Dead-Drop Campaign — 1,980 Infected Sites Use Steam Community Comments for C2
**Product:** WordPress (compromised sites via vulnerable themes/plugins/credential theft) | **CVE:** N/A (campaign) | **Published:** 2026-06-01

GoDaddy security engineers detailed an active campaign infecting ~1,980 WordPress sites that fetches commands from **Steam Community profile comments** (using six invisible Unicode zero-width characters to encode payloads) rather than maintaining a dedicated C2 infrastructure. Three-stage chain: first-stage malware planted via stolen credentials / vulnerable themes / supply-chain → page load triggers Steam fetch → decoded payload installs a backdoor accepting base64-PHP via POST with a hardcoded auth cookie `tEcaKKXEsb`. GoDaddy first discovered the campaign in July 2025; sustained for ~10 months.

**Why it matters:** Yet another **public-platform-as-C2** entry — Steam joins the GitHub Calendar / Anthropic-API-typosquat / Azure-Blob dead-drop cluster as a place attackers run command channels through, knowing defenders cannot blanket-block `steamcommunity.com`. Sustained-campaign aspect (10 months undetected with ~2,000 active victims) suggests WordPress-site-management ops are not catching first-stage indicators reliably. Defensively useful because it spotlights the need for WordPress-host outbound monitoring for Steam Community fetches in PHP-execution contexts (not browser).

**Mitigation:**
- Hunt WordPress install logs for unexpected PHP-context requests to `steamcommunity.com`.
- File-integrity-monitor for PHP files referencing a `tEcaKKXEsb` cookie name.
- Keep WordPress + themes + plugins on auto-update; rotate admin credentials on any suspected compromise.

**Sources:** [BleepingComputer — WordPress malware campaign hides payloads in Steam profiles](https://www.bleepingcomputer.com/news/security/wordpress-malware-campaign-hides-payloads-in-steam-profiles/)

---

### Meta AI Support Chatbot Abused to Hijack High-Profile Instagram Accounts via Password-Reset MFA Bypass
**Product:** Meta / Instagram account recovery flow | **CVE:** N/A (platform abuse) | **Published:** 2026-06-01

Pro-Iranian threat actors used a near-geofence VPN to initiate an Instagram password reset, then engaged Meta's AI customer-support chatbot and instructed it to associate a new email address with the target account. The bot complied, sent a one-time reset code to the attacker-controlled inbox, and the attacker took over the account. Compromises included the **Obama White House** Instagram account and the **Chief Master Sergeant of the U.S. Space Force** account, both briefly defaced with pro-Iranian content. Accounts with SMS-based MFA enabled were protected. Meta deployed an emergency patch over the weekend.

**Why it matters:** First publicly-documented **AI-customer-support-bot identity-control hijack class** — extends the platform-trust-as-attack-surface pattern (ChatGPhish / LLMShare MEMORY 2026-05-30) and the AI-customer-service-as-attack-surface cluster (Anthropic Mythos rollout calibration data). Two durable lessons: (1) any AI customer-service flow that can trigger an authentication-relevant side effect must be retrieval-augmented against an MFA-bypass policy classifier, not just intent-classified; (2) the Trust & Safety + AI-Eng-team handoff for "bot can change account email" needs the same threat-model rigor as a password-reset API endpoint.

**Mitigation:**
- For corporate-managed brand-/exec-Instagram accounts: enforce SMS or app-based MFA; this incident's bypass failed against MFA-protected accounts.
- Audit all customer-facing AI chatbots that the org maintains for ability to trigger auth-side-effects (password reset, email change, MFA re-enrollment).

**Sources:** [Krebs on Security — Hackers Used Meta's AI Support Bot to Seize Instagram Accounts](https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/)

---

## 📋 Noted / Monitoring

**Apache Airflow CVE-2026-45192** — 17th Airflow CVE in three days, joining yesterday's 16-CVE batch (MEMORY 2026-06-01) — improper redaction of sensitive fields in Connection Extra API responses. Apply alongside the 16-CVE batch fixes already deployed.

**Apache Calcite CVE-2026-46718** — Authenticated-user-controlled models loading arbitrary Java classes for code execution. Affects Apache Calcite (Druid / Beam / Hive / Flink / Phoenix all bundle it). Low ITW likelihood without auth, but durable Apache pattern — joins the multi-quarter Apache CVE-batch tempo from MEMORY 2026-05-04 / 2026-05-19 / 2026-06-01.

**Apache Directory LDAP API CVE-2026-35563** — Client fails to validate server certificate hostname matching. MitM-class for any Java-LDAP client built on Apache Directory; quietly broad blast radius across enterprise Java stacks.

**Apache Fesod (Incubating) CVE-2026-49328** — SSRF via inadequate URL validation. Incubator-stage project, limited deployment, but flagged for visibility.

**pip CVE-2026-8643** — Console/GUI script extraction outside install directory. Affects every CI runner using pip; potential supply-chain abuse vector if a malicious wheel is permitted to install. Patch pip toolchain promptly across CI fleet.

**Sereal::Decoder CVE-2026-8796** — Perl heap out-of-bounds read in serialization library. Low impact — only relevant to Perl-heavy services parsing untrusted Sereal-encoded input.

**bmcweb (OpenBMC web server) — four vulnerabilities (Full Disclosure 2026-05-31)** — two unfixed, GHSA without CVE assignment. OpenBMC ships on most hyperscaler-grade rackmount servers (AMD/Intel/Ampere reference platforms) — out-of-band management plane attack surface. Re-evaluate IPMI-VLAN isolation.

**PC Tools Internet Security PCTCore64.sys CVE-2026-8501 / CERT/CC VU#158530** — Discontinued-since-2013 product, but the signed driver remains usable as BYOVD primitive for credential extraction from `lsass.exe` and cross-process handle manipulation. Add `PCTCore64.sys` to WDAC / Microsoft Vulnerable Driver Block List update.

**HP Poly VVX / Trio VoIP Phone CVE-2026-0826 (Rapid7)** — Critical pre-auth stack buffer overflow; fixed. Likely OOS for most corporate perimeters (VoIP phones are typically internal-VLAN only) but flagged for any org with internet-exposed VVX/Trio devices.

**Mennekes Amtron EV-charging-station Multiple Vulnerabilities (CyberDanube)** — OT/EV-charging scope, OOS for the corporate perimeter but logged as a calibration data point for the OT/IoT-charging-infrastructure cluster.

**Dashlane brute-force lockout wave (2026-05-31 → 2026-06-01)** — Credential-stuffing attack against password-manager user accounts; Dashlane confirms no platform compromise. No novel TTP — logged because password-manager-as-target is a recurring 2026-Q2 theme (LastPass-class historical precedent).

**Spain National Police doxer arrest (2026-05-27)** — Individual arrested for publishing personal data of Spanish government staff via "Police-ESP-Doxed"; data sourced from prior breaches + OSINT, not direct system compromise. Not a vulnerability event — logged for completeness.

**Asocks 17M-device residential-proxy botnet takedown follow-up** — Continuing coverage in BleepingComputer / THN re-confirms MEMORY 2026-05-30 disclosure (Dutch NCSC + National Police). No new technical detail; takedown-cluster tracking only.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/KEV | ❌ (both 403 via WebFetch) |
| Vendor advisories | rapid7.com, fortinet.com/blog/threat-research, securitylab.github.com, blog.cloudflare.com, msrc.microsoft.com/blog | ✅ (msrc degraded — empty) |
| Research / OSINT | schneier.com, krebsonsecurity.com, avleonov.com, dbugs.ptsecurity.com, opencve.io | ✅ |
| CVE feeds | seclists.org/fulldisclosure, openwall oss-security, kb.cert.org/vuls, github.com/0xMarcio/cve, github.com/search?q=CVE, nvd.nist.gov, cve.org, cve.mitre.org | ✅ / ❌ mixed (nvd/cve.org/cve.mitre.org JS-only) |
| Supply chain | GitHub Security Advisories (vitest, praisonai, redhat) | ✅ |
| Threat intel | fortinet/blog/threat-research, googleprojectzero.blogspot.com, packetstormsecurity.com | ⚠️ / ❌ (gpz redirects, packetstorm degraded ToS-only) |
| Russian-language | habr.com/tomhunter, teletype.in/@cyberok, cert.gov.ua | ⚠️ (all degraded / stale through Feb/Mar 2026 / empty homepage) |
| Bounty platforms | hackerone.com/hacktivity, bugcrowd.com/disclosures, attackerkb.com | ❌ (JS-required / 404 / 403) |

**Errors:** cisa.gov (403), cisa.gov/KEV (403), attackerkb.com (403), cve.org (JS), cve.mitre.org (redirects to cve.org), googleprojectzero.blogspot.com (redirects), hackerone.com/hacktivity (JS), bugcrowd.com/disclosures (404).

**Degraded:** packetstormsecurity.com (homepage returns ToS only), nvd.nist.gov (homepage no CVE listing), msrc.microsoft.com/blog (empty content), habr.com/tomhunter (stale through Mar 2026), teletype.in/@cyberok (stale through Feb 2026), cert.gov.ua (empty).

**CISA KEV:** Endpoint unreachable today via WebFetch; PAN-OS CVE-2026-0257 federal deadline 2026-06-01 lapsed yesterday — confirm via offline KEV mirror at next opportunity. Expect Windows Netlogon CVE-2026-41089 KEV addition within 48-72h based on Belgian CCB confirmation.

---

*Watchtower vulnerability-researcher | Cycle: 2026-06-02/night | Next: 2026-06-03/night*
