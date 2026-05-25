# Watchtower Night Report — 2026-05-25
**Cycle:** Night | **Generated:** 2026-05-25 00:30 UTC (2026-05-25T00:30:00Z)
**Sources checked:** 23/30 | **CISA KEV total:** unchanged (gateway 403) | **New KEV additions:** none confirmed since 2026-05-21 (Trend Micro Apex One CVE-2026-34926 + Langflow CVE-2025-34291) — KEV API still unreachable, monitor for 2026-05-26 cycle

---

## 🔴 CRITICAL

### Ghost CMS CVE-2026-26980 Pre-Auth SQL Injection — Mass ClickFix Campaign Compromises 700+ Domains Including Harvard / Oxford / Auburn / DuckDuckGo (CVSS Critical)
**Product:** Ghost CMS (Node.js publishing platform) versions 3.24.0 → 6.19.0 | **CVE:** CVE-2026-26980 | **Status:** Active Exploitation / Patched 6.19.1 (2026-02-19)

Unauthenticated SQL injection in Ghost CMS lets attackers read arbitrary data from the site database — including admin API keys, which grant management access to users, articles, and themes. XLab disclosed 2026-05-24 that the flaw is now under large-scale active exploitation: at least two distinct activity clusters compromised more than 700 domains (Harvard, Oxford, Auburn, DuckDuckGo, AI/SaaS companies, media outlets, fintech firms, security sites), injected malicious JavaScript into articles, served fake Cloudflare ClickFix prompts via iframes, and deployed DLL loaders, JavaScript droppers, and an Electron-based UtilifySetup.exe payload. Patches shipped 2026-02-19 — three-month patch gap is the operative IoC.

**Timeline:** Patch 2026-02-19 (Ghost 6.19.1) → SentinelOne exploitation write-up 2026-02-27 → XLab campaign report 2026-05-24 (BleepingComputer relay same day) → ongoing re-infection of cleaned sites with different payloads.

**Why it matters:** Ghost CMS is among the most widely deployed Node.js publishing platforms after WordPress for high-traffic editorial sites; 3-month patch gap on a SaaS-class product is unusually long because many deployments are self-hosted by smaller editorial teams without active maintenance. Mass exploitation of compromised admin API keys means attackers retain persistent edit-level access even after patching — every unpatched-pre-2026-02-19 instance must rotate keys + audit articles for injected JS, not just upgrade. ClickFix monetization couples this CMS-pivot to second-stage malware delivery, raising the supply-chain reach beyond just defacement.

**Discovered by:** Initial vulnerability disclosure by Ghost project. Mass exploitation campaign tracked by XLab.

**Mitigation:**
- Upgrade Ghost CMS to 6.19.1 or later — anything 3.24.0–6.19.0 is exploitable.
- Rotate all admin API keys regardless of upgrade — pre-upgrade keys may already be exfiltrated.
- Audit all articles published on the instance for injected `<script>` tags, base64-encoded JS, and iframe injections.
- Maintain 30-day admin API logs and inspect for unexpected article modifications, user creations, and theme uploads.
- Block known XLab campaign IoCs at the perimeter (consult XLab report for current IoC list).
- For any compromised site: assume full Ghost-admin-equivalent foothold, rebuild from clean state if uncertain.

**Sources:** [BleepingComputer — Ghost CMS SQL injection flaw exploited in large-scale ClickFix campaign](https://www.bleepingcomputer.com/news/security/ghost-cms-sql-injection-flaw-exploited-in-large-scale-clickfix-campaign/) | [TheHackerNews — Drupal Core SQL Injection / Ghost CMS coverage](https://thehackernews.com/) | [XLab campaign report — referenced]

---

### LiteSpeed cPanel Plugin CVE-2026-48172 — Maximum-Severity (CVSS 10.0) cPanel-User-to-Root RCE Actively Exploited Across Shared Hosting
**Product:** LiteSpeed User-End cPanel Plugin v2.3 → v2.4.4 (WHM plugin not affected) | **CVE:** CVE-2026-48172 | **Status:** Active Exploitation / Patched 2.4.5+ (recommend WHM plugin 5.3.1.0 bundled with cPanel plugin 2.4.7+)

Incorrect privilege assignment in the `lsws.redisAble` function lets any cPanel user (including attackers operating from compromised low-privilege accounts) execute arbitrary scripts as root on the host server. LiteSpeed confirmed in-the-wild exploitation, but provided only a single forensic primitive: `grep -rE "cpanelplugin_jsonapi_func=redisAble" /var/cpanel/logs` — no output means the server was not targeted. With CVSS 10.0 and the cPanel-user-to-root primitive being the canonical shared-hosting takeover chain, expect this to enroll into existing shared-hosting compromise tooling within days.

**Timeline:** LiteSpeed disclosure + patch 2026-05-22 → TheHackerNews coverage 2026-05-23 → active exploitation confirmed by vendor — no public PoC URL yet.

**Why it matters:** Pairs directly with the cPanel CVE-2026-41940 auth-bypass campaign (MEMORY) — any IAB or ransomware crew that already weaponized 41940 now has a second cPanel-ecosystem root-escalation primitive in the same monetization workflow. Shared hosting providers cannot rely on per-tenant isolation here: a single compromised cPanel user becomes root on the shared host, exposing every other tenant on the same machine. Internet exposure is implicit on every commercial cPanel-managed VPS / shared hosting box.

**Discovered by:** David Strydom (security researcher).

**Mitigation:**
- Upgrade LiteSpeed User-End cPanel Plugin to 2.4.5+ immediately on every cPanel host running LiteSpeed.
- Preferred: install LiteSpeed WHM Plugin 5.3.1.0 (bundles cPanel plugin 2.4.7+) to address both the User-End plugin and ensure WHM plugin currency.
- Run the LiteSpeed compromise check: `grep -rE "cpanelplugin_jsonapi_func=redisAble" /var/cpanel/logs` on every cPanel host — any non-empty output is grounds for full forensic triage.
- For shared hosting providers: treat any cPanel host running LSWS pre-2.4.5 as potentially-root-compromised until logs confirm otherwise; rotate root credentials, SSH keys, and review cron / startup scripts for persistence.
- Pair this hunt with the cPanel CVE-2026-41940 IoC sweep — same monetization workflow likely chains both.

**Sources:** [TheHackerNews — LiteSpeed cPanel Plugin CVE-2026-48172 Exploited to Run Scripts as Root](https://thehackernews.com/2026/05/litespeed-cpanel-plugin-cve-2026-48172.html) | [LiteSpeed advisory — vendor confirmation of ITW exploitation]

---

## 🟠 HIGH

### Laravel-Lang PHP Packages Supply Chain Compromise — 700+ Malicious Versions Pushed via Git-Tag Rewriting Targeting Composer Autoload
**Product:** laravel-lang/lang, laravel-lang/http-statuses, laravel-lang/attributes, laravel-lang/actions (Composer) | **CVE:** Not yet assigned | **CVSS:** N/A (supply chain) | **First reported:** 2026-05-22 / 2026-05-23

A novel supply-chain primitive: the attackers did not modify source code directly — instead, they **rewrote every existing git tag in each repository to point to a new malicious commit**. The payload was a `src/helpers.php` file registered in autoload configuration, so the backdoor executes on every PHP request without requiring special triggers. Over 700 compromised versions were published 2026-05-22 / 2026-05-23, many appearing seconds apart, indicating automated mass-tag rewriting rather than manual per-package attacks. Payload is a cross-platform credential stealer targeting cloud credentials, cryptocurrency wallets, browser data, VPN configurations, and environment variables across Windows, Linux, and macOS.

**Mitigation:**
- Audit every Composer lock file for `laravel-lang/lang`, `laravel-lang/http-statuses`, `laravel-lang/attributes`, and `laravel-lang/actions` — pin to known-good pre-2026-05-22 tags or upstream-confirmed clean versions.
- Treat any deploy that pulled a Laravel-Lang version between 2026-05-22 and 2026-05-23 as a credential-stealer infection vector: rotate cloud credentials, wallets, browser-stored secrets, VPN configs, and environment variables on every host that ran the affected PHP code.
- Add `src/helpers.php` modification detection to CI artifact integrity scanning for all Composer dependencies — the autoload-registration pattern is the same primitive that earlier npm Shai-Hulud waves used.
- Lock dependency pinning policy: distrust mutable tags in Composer + npm + Go module ecosystems; pin to commit SHAs, not version tags, for critical dependencies.
- Monitor Packagist + GitHub Releases for the Megalodon / Shai-Hulud-class repeat patterns; this is the third major mutable-package-metadata abuse in 30 days (Mini Shai-Hulud Wave 2 + Megalodon May 18 + Laravel-Lang May 22).

**Sources:** [TheHackerNews — Laravel-Lang PHP Packages Compromised to Deliver Cross-Platform Credential Stealer](https://thehackernews.com/2026/05/laravel-lang-php-packages-compromised.html)

---

### Underminr DNS Domain-Fronting Variant — CDN Tenant-Misrouting Technique Affects ~88M Domains, Already Used in ClickFix Campaigns
**Product:** Shared-tenancy CDN infrastructure (US/UK/Canada-anchored CDNs most affected) | **CVE:** Not assigned | **CVSS:** N/A (technique disclosure) | **First reported:** 2026-05-23

ADAMnetworks disclosed Underminr — a domain-fronting variant that "presents the SNI and HTTP Host of a domain while forcing a request to the IP address of another tenant on the same shared edge." Unlike classical domain fronting (which relies on a front domain), Underminr exploits CDN tenant routing such that traffic appears legitimate but actually connects to malicious infrastructure on the same shared CDN. ADAMnetworks puts the affected scope at ~88 million domains. SecurityWeek reports the technique is already being used to hide C2, circumvent DNS filtering and protective-DNS services, enable VPN/proxy traffic to evade policies, and is being incorporated into ClickFix campaign infrastructure.

**Timeline:** ADAMnetworks disclosure 2026-05-23 → SecurityWeek coverage same day → reported as already in-use in ClickFix campaigns (presumed including the Ghost CMS / CVE-2026-26980 cluster above).

**Why it matters:** Protective-DNS, secure web gateway, and TLS-inspection-based egress filtering all use the SNI / HTTP Host as primary indicators of "where does this connection actually go." Underminr breaks that correlation at the CDN-tenant layer — defenders cannot reliably enforce policy on traffic to shared-tenancy CDNs without forcing CDN providers to correlate DNS decisions, edge IPs, SNI, Host headers, and tenant routing. Practically, this is a defensive-blindness escalation for the ClickFix / supply-chain ecosystem and will be increasingly weaponized in AI-generated malware infrastructure.

**Mitigation:**
- For protective-DNS / SWG / egress-filtering products: request vendor statement on whether and how they detect SNI-vs-actual-CDN-tenant divergence.
- For CDN procurement: question CDN providers (Cloudflare, Fastly, Akamai, AWS CloudFront) on whether they correlate DNS decisions, edge IPs, SNI, Host headers, and tenant routing to deny cross-tenant requests.
- Tactical: prioritize blocking known C2 infrastructure at IP layer (rather than only domain layer) for high-risk threat clusters; SNI-based blocks alone are no longer sufficient.
- Hunt: review egress logs for traffic to shared CDN IP space where the SNI / Host header does not match the destination IP's expected tenant.
- Track ADAMnetworks technical write-up + future CDN-vendor response for detection signatures.

**Sources:** [SecurityWeek — 'Underminr' Vulnerability Lets Attackers Hide Malicious Connections Behind Trusted Domains](https://www.securityweek.com/underminr-vulnerability-lets-attackers-hide-malicious-connections-behind-trusted-domains/) | [ADAMnetworks disclosure — referenced]

---

## 🟡 MEDIUM

### Apache Airflow Provider Two-CVE Disclosure — CVE-2026-45361 Google ComputeEngineSSHHook Host-Key-Verification-Disabled + CVE-2026-46745 FAB Auth Manager LDAP Filter Injection
**Product:** apache-airflow-providers-google (< 22.0.0) + apache-airflow-providers-fab (< 3.6.4) | **CVE:** CVE-2026-45361, CVE-2026-46745 | **Published:** 2026-05-24

Two distinct Airflow provider advisories landed on oss-security 2026-05-24. CVE-2026-45361 (Low severity) — `ComputeEngineSSHHook` disables SSH host-key verification by default, exposing Airflow→Compute Engine VM SSH traffic to in-path MITM. CVE-2026-46745 (Moderate severity) — the FAB Auth Manager `/auth/token` endpoint exposes a vulnerable `_search_ldap` function permitting unauthenticated LDAP filter injection (CWE-90); attackers can exfiltrate directory data or bypass authentication entirely. This extends the May Airflow CVE wave (CVE-2026-43826 / 41018 OpenSearch/Elasticsearch credential leak from 2026-05-10, CVE-2026-27173 Kubernetes JWT exposure from 2026-05-19) into a 6-CVE cumulative drip across the 2026-05-10 → 2026-05-24 window.

**Mitigation:** Upgrade `apache-airflow-providers-google` to 22.0.0+ and `apache-airflow-providers-fab` to 3.6.4+ on every Airflow deployment. As an interim measure for the FAB issue: disable LDAP authentication on FAB Auth Manager until the patch is applied. For Google provider: until upgrade, set `assert_hostkey=True` explicitly on every ComputeEngineSSHHook usage. Audit any prior SSH-via-ComputeEngine traffic for MITM-injected commands.

**Sources:** [oss-security 2026-05-24 — CVE-2026-45361 (Jens Scheffler)](https://www.openwall.com/lists/oss-security/2026/05/24/9) | [oss-security 2026-05-24 — CVE-2026-46745 (Jens Scheffler)](https://www.openwall.com/lists/oss-security/2026/05/24/10)

---

## 📋 Noted / Monitoring

**CVE-2026-9277 shell-quote command injection (npm, ≤1.8.3, CVSS 8.1)** — Akshat Sinha disclosed 2026-05-22; literal newline in `.op` of object tokens bypasses POSIX shell escaping in `quote()`, allowing command injection. Fixed in 1.8.4. Niche integration pattern (apps passing object tokens to `quote()` or `parse(cmd, envFn)` with `envFn` returning objects); CI/CD and build-tooling exposure if attacker-controlled input reaches shell-quote.

**CVE-2026-45249 Apache ECharts XSS in Lines series tooltip (< 6.1.0)** — Zhongxiang Wang disclosed 2026-05-23; raw HTML in `series.data[i].name` rendered via innerHTML when Lines series + tooltips used without custom formatter. Widely embedded charting library; risk on any dashboard accepting user-controlled data labels.

**Packagist 8-package supply chain compromise (2026-05-23)** — `moritz-sauer-13/silverstripe-cms-theme`, `crosiersource/crosierlib-base`, `devdojo/wave`, `devdojo/genesis`, `katanaui/katana`, `elitedevsquad/sidecar-laravel`, `r2luna/brain`, `baskarcm/tzi-chat-ui`. Malicious code inserted into `package.json` (not composer.json) targeting JS build tooling alongside PHP; postinstall script downloads Linux binary to `/tmp/.sshd` and executes. Socket investigation found ~777 files across GitHub referencing the same payload — broader operation, no Shai-Hulud attribution. Removed from Packagist. Separate primitive from Laravel-Lang above.

**ROOT framework (CERN) heap buffer overflow in TKey::Streamer / TBasket::ReadBasketBuffers (CVSS 7.8, v6-00-00 → v6-40-00)** — Manopakorn Kooharueangrong disclosed 2026-05-24; integer overflow in `fObjlen + fKeylen` validation lets attacker-controlled `.root` files trigger 32KB heap OOB write at TBasket.cxx:601. Fix in PR #22377. Relevant for any CERN SWAN / batch worker / grid-storage environment processing third-party `.root` files; tangentially relevant for any data-engineering org consuming external scientific datasets in ROOT format. 90-day disclosure timer running from 2026-05-24 absent CVE assignment.

**PuTTY 0.84 three minor security fixes (2026-05-24)** — (1) ECDSA-NIST-curve point-addition assertion-failure DoS exploitable by MITM to deny service before host verification; (2) RSA-key-exchange double-free remote-triggerable crash (regression from 2019); (3) Telnet trust-sigil persistence across proxy auth allowing spoofed-password-prompt deception; plus disputed CVE-2026-4115 (EdDSA signature validation). Client-side scope, but PuTTY is fleet-deployed in many enterprise admin shops — upgrade window for next ITSM cycle.

**CVE-2026-48700 PCManFM-Qt arbitrary file open via D-Bus `ShowFolders`** — Aaron Rainbolt disclosed 2026-05-24; file URI passed to `ShowFolders` triggers MIME handler invocation rather than directory listing; with Wine+WineHQ packages installed, this enables sandbox escape (Flatpak / Snap) by dropping an EXE and pointing PCManFM-Qt at it. Linux desktop scope, but flagged because of the sandbox-escape primitive.

**Totolink A8000RU 6-CVE OS command injection batch (CVE-2026-9385/9386/9388/9404/9405/9406, all CVSS 9.8)** — Recently published unauth command injection across `setRemoteCfg`, `setGameSpeedCfg`, `setDdnsCfg`, `setScheduleCfg`, `setLanguageCfg`, `setTracerouteCfg`. Same product family already noted on 2026-04-27 (CVE-2026-7037) — consumer/SOHO router; IoT-botnet recruitment vector, OOS for typical enterprise estate but tracked for ISP fleets and remote-worker home-router exposure.

**Apache CXF 3-CVE batch CVE-2026-44417 / 44618 / 44930 (continued from 2026-05-22)** — Colm O hEigeartaigh re-pushed on 2026-05-22 thread: incomplete-fix for CVE-2025-48913 + XXE in WS-Transfer + LDAP injection in XKMS LDAP Repository. Already noted 2026-05-23 but staying on the list — this is the same Apache-incomplete-fix pattern as MINA / OFBiz earlier in May.

**Anthropic Coordinated Vulnerability Disclosure dashboard launch (oss-security 2026-05-23)** — Alan Coopersmith relayed Anthropic's new CVD tracking dashboard. Process change, not a vulnerability — relevant for security teams tracking Claude API surface advisories.

**Kimwolf Botmaster Arrest (Krebs 2026-05-21)** — 23-year-old Ottawa resident "Dort" arrested in US/Canada for operating the Kimwolf IoT botnet responsible for record-breaking 30 Tbps+ DDoS attacks. Law-enforcement action, not a defensive advisory — but signals continued LE pressure on DDoS infrastructure operators; may correlate with reduced DDoS volumes near-term.

**CISA Contractor AWS GovCloud Credential Leak (Krebs / Schneier 2026-05-22)** — A CISA contractor maintained a public GitHub repository containing plaintext credentials to AWS GovCloud accounts and internal CISA systems. No new technical primitive but operationally relevant: any defender whose threat model includes the CISA infrastructure (KEV consumers, threat-feed consumers) should re-evaluate trust assumptions until CISA's incident-response is complete. Watch for follow-up on what data may have been accessed.

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

**Errors:** cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403), attackerkb.com (403), msrc.microsoft.com/blog (redirect, no content), hackerone.com/hacktivity (no content), bugcrowd.com/disclosures (404), cert.gov.ua (no content).
**Degraded:** packetstormsecurity.com (redirected, statistics only), habr.com/ru/companies/tomhunter/articles (no posts since March 2026), teletype.in/@cyberok (no posts since February 2026), cve.mitre.org (redirected to cve.org, content limited).
**Supplemental sources hit (not counted in 30):** openwall.com/lists/oss-security (5/22–24 archive ✅ — primary source for the Airflow / shell-quote / ECharts / ROOT / PCManFM-Qt / PuTTY findings above).
**CISA KEV:** Gateway 403 — no new additions confirmed since 2026-05-21 (Trend Micro Apex One CVE-2026-34926 + Langflow CVE-2025-34291). Monitor KEV REST API recovery for 2026-05-26.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-25/night | Next: 2026-05-26/night*
