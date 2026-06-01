# Watchtower Night Report — 2026-06-01
**Cycle:** Night | **Generated:** 2026-06-01 06:30 UTC (2026-06-01T06:30:00Z)
**Sources checked:** 21/30 | **CISA KEV total:** unavailable (cisa.gov blocking WebFetch) | **New KEV additions:** see prior reports (Asocks botnet + PAN-OS CVE-2026-0257 added 2026-05-29)

---

## 🟠 HIGH

### WP Maps Pro CVE-2026-8732 — Unauthenticated Admin-Account Creation Actively Exploited on ~15,000 WordPress Sites
**Product:** WP Maps Pro (Envato Market premium WordPress plugin) ≤ 6.1.0 | **CVE:** CVE-2026-8732 | **CVSS:** Critical (CVSS not yet aggregated on NVD) | **Status:** Patched (6.1.1, released 2026-05-20) — Active Exploitation Confirmed

The plugin shipped a vendor-support "temporary access" AJAX endpoint protected only by a publicly exposed nonce in frontend JavaScript. Unauthenticated attackers can call the endpoint to create new WordPress administrator accounts with one-click passwordless login URLs. Defiant / Wordfence blocked more than 3,600 exploitation attempts in the 24-hour window before disclosure (BleepingComputer 2026-05-31). The plugin has 15,800+ recorded sales on Envato, with ~15,000 active installs estimated.

**Timeline:** Vendor patch 6.1.1 released 2026-05-20 → active exploitation telemetry surfaced 2026-05-30 → public disclosure 2026-05-31 (BleepingComputer / Wordfence). Envato Market plugins do not benefit from the WordPress.org auto-update channel — every install is a deliberate operator update, so the long tail of unpatched sites is structurally larger than wp.org-hosted plugins.

**Why it matters:** Direct unauthenticated admin-account creation = full site takeover (web shell drop, persistent backdoor, redirect/SEO campaigns, supply-chain pivot to admin-only plugin installs). Three-day window since disclosure typically marks the transition from opportunistic scanners to automated mass-defacement / SEO-spam botnets on WordPress; expect KEV addition within 14 days given the active-exploitation signal.

**Discovered by:** Defiant / Wordfence Threat Intelligence Team (researcher attribution pending; campaign telemetry).

**Mitigation:**
- Inventory: search every WordPress fleet for WP Maps Pro plugin file `wp-content/plugins/wp-maps-pro/` or the `wpmp_` AJAX action prefix; do NOT rely solely on Envato license records (resold/forked copies are common).
- Upgrade to WP Maps Pro 6.1.1 immediately, or remove the plugin if usage cannot be confirmed.
- Audit `wp_users` table for unfamiliar administrator accounts created after 2026-05-20; check WP audit log plugins / object cache for `create_user` events from unauthenticated sources.
- Rotate all administrator-tier passwords on any host that had WP Maps Pro ≤ 6.1.0 exposed.
- Add WAF / mod_security rule blocking `admin-ajax.php?action=wpmp_*` from unauthenticated origins as a stop-gap if patching is delayed.

**Sources:** [BleepingComputer — WP Maps Pro bug exploited to create admin accounts](https://www.bleepingcomputer.com/news/security/wp-maps-pro-bug-exploited-to-create-admin-accounts-on-wordpress-sites/) | [Defiant / Wordfence Threat Intelligence](https://www.wordfence.com)

---

### Apache Airflow 16-CVE Batch — Authenticated RCE via XCom PATCH + BashOperator Jinja2 Injection + Multi-Endpoint AuthZ Bypass
**Product:** Apache Airflow (data-orchestration platform) | **CVE:** CVE-2026-40861, CVE-2026-40961, CVE-2026-40963, CVE-2026-41014, CVE-2026-41017, CVE-2026-41084, CVE-2026-42252, CVE-2026-42358, CVE-2026-42359, CVE-2026-42360, CVE-2026-45360, CVE-2026-45426, CVE-2026-46764, CVE-2026-48726, CVE-2026-49267, CVE-2026-49298 | **CVSS:** mixed — RCE class CVE-2026-42359 and CVE-2026-45360 are highest-priority | **First reported:** 2026-05-31 (oss-security batch by Rahul Vats)

Sixteen-CVE coordinated disclosure across the Airflow security tree. Highest-priority items: **CVE-2026-42359** — authenticated RCE via XCom PATCH endpoint (an authenticated low-privilege user mutates an XCom value that downstream code deserialises in a way that executes attacker-supplied Python); **CVE-2026-45360** — arbitrary import in custom deadline-reference deserialization (auth-required but yields code-execution context); **CVE-2026-42252** — BashOperator Jinja2 template injection via `dag_run.conf` with the documented low-privilege user pattern (any user that can trigger a DAG run yields shell-on-worker). The rest of the batch is a wide spread of authorization bypasses (DAG-scoped permission filter bypass via Python `lstrip()` character-stripping on JWT cookies — CVE-2026-45426 is a defensive-engineering wake-up call), JWT cookie missing Secure flag behind HTTPS-terminating proxies (CVE-2026-41017), cross-DAG mutation of bulk TaskInstances (CVE-2026-41084), template-truncation bypassing nested sensitive-key masking (CVE-2026-42360), variable-masker depth-limit bypass (CVE-2026-42358), and SMTP STARTTLS lacking cert validation (CVE-2026-49267).

**Why it matters:** Airflow is the de facto data-orchestration platform in our scope — DAG workers typically run with broad cloud-IAM scope (read/write S3, BigQuery, Snowflake, Vault, KMS) and Airflow JWT-cookie misconfigurations are a common artefact of "reverse-proxy auth in front of Airflow" deployments. CVE-2026-45426 (Python `lstrip()` character-stripping JWT authz bypass) is the kind of bug that repeats elsewhere — audit any internal Python service that hand-rolls `lstrip()` on a cookie value before signature validation.

**Mitigation:**
- Upgrade to the patched Airflow release per vendor advisory (release numbers in apache.org/airflow CVE page; expect 2.x and 3.x release branches both impacted).
- For multi-tenant Airflow: even after patch, treat every Airflow user as a privileged user. The DAG-permission model is leaky by design — separate environments per trust boundary rather than relying on per-DAG ACLs.
- Audit Airflow webserver behind reverse proxies: confirm the proxy forwards `X-Forwarded-Proto: https` correctly so the new Secure-flag JWT cookie is set; otherwise the auth cookie is sent over HTTP.
- For BashOperator + Jinja2 pattern (CVE-2026-42252): freeze the set of users who can trigger DAG runs with conf, or disable conf-from-API.
- Run `grep -r "BashOperator" .` against your DAG repos to inventory blast-radius before patching window closes.

**Sources:** [oss-security 2026-05-31 — Apache Airflow batch](https://www.openwall.com/lists/oss-security/2026/05/31/) | [GitHub Advisories — Apache Airflow](https://github.com/advisories?query=apache+airflow)

---

### Apache ActiveMQ 6-CVE Batch — Jolokia addNetworkConnector RCE + Authorization Defects in Messaging Core
**Product:** Apache ActiveMQ (Classic) | **CVE:** CVE-2026-42253, CVE-2026-42588, CVE-2026-45505, CVE-2026-46605, CVE-2026-49157, CVE-2026-49270 | **CVSS:** RCE class CVE-2026-42588 highest priority | **First reported:** 2026-05-31 (oss-security batch by Christopher Shannon)

Six-CVE batch. Highest-priority item: **CVE-2026-42588** — remote code execution via Jolokia `addNetworkConnector` invocation. Jolokia is the JMX-over-HTTP bridge ActiveMQ exposes by default on the admin interface; `addNetworkConnector` lets an attacker plumb the broker to attacker-controlled hosts, with the connector URL parsed and executed in a code-loading context. Companion bugs: **CVE-2026-45505** discovery-side weakness in the same `addNetworkConnector` path; **CVE-2026-49157** authenticated low-privilege web users retain Jolokia capability after privilege downgrade (privilege-escalation-via-stale-token); **CVE-2026-42253** HTTP response header injection via JMS message properties; **CVE-2026-46605** incomplete authorization during destination operations; **CVE-2026-49270** durable subscription disclosure via crafted message.

**Why it matters:** ActiveMQ has a sustained mass-exploitation history (CVE-2023-46604 → HelloKitty / TellYouThePass ransomware Oct 2023; CVE-2024-32114 → KEV July 2024). Jolokia-class RCE bugs hit ActiveMQ within the same 60-day patch-to-exploit window as Confluence / Atlassian. CVE-2026-42588 is particularly worrying because ActiveMQ Jolokia is on by default and admin-interface authentication is widely misconfigured.

**Mitigation:**
- Upgrade ActiveMQ to the patched version per Apache advisory (5.18.x / 5.19.x patched branches).
- Disable Jolokia on the broker admin interface unless explicitly required: comment out the `jolokia-agent.xml` import in `jetty.xml`, or restrict by IP allow-list at reverse proxy.
- Inventory ActiveMQ instances reachable from internet via Shodan facet `port:8161 jetty`.
- Confirm broker admin interface uses a non-default password — the `admin/admin` default is endemic.
- Add monitoring rule for HTTP requests to `/api/jolokia/exec/org.apache.activemq:type=Broker/addNetworkConnector` — any such request from non-management origin is presumptive exploitation.

**Sources:** [oss-security 2026-05-31 — Apache ActiveMQ batch](https://www.openwall.com/lists/oss-security/2026/05/31/) | [GitHub Advisories — Apache ActiveMQ](https://github.com/advisories?query=activemq)

---

## 📋 Noted / Monitoring

**Yamcs-core 3-CVE batch (CVE-2026-46621 / CVE-2026-46562 / CVE-2026-44632)** — authenticated RCE in Yamcs (mission control / telemetry platform for satellites) via Jython algorithm code injection, mission-database algorithm override, and Janino expression-engine injection. GitHub Advisories 2026-05-31. Niche aerospace / SCADA scope but warrants tracking for downstream satellite-ground-segment fleets.

**liquidjs CVE-2026-45618** — RCE in widely deployed JavaScript template engine (GitHub Advisories 2026-05-31). Track for downstream SSG / CMS impact (used by Eleventy and many static-site pipelines); flagged for npm-package dependency-tree audit.

**nezha CVE-2026-46716** — cross-tenant RCE via API endpoint in nezha Go server-monitoring tool (GitHub Advisories 2026-05-31). Self-hosted ops-monitoring tool — same default-no-auth pattern as the wider AI/SCADA self-host class. Flagged for ops-team inventory.

**vm2 npm — 5 additional CVEs (CVE-2026-47131 / 47137 / 47140 / 47208 / 47210)** — five new sandbox-escape variants joining the 12-CVE batch from MEMORY 2026-05-08. The library remains structurally unfixable per maintainer acknowledgment; this is continued confirmation, not a new pattern. Treat any vm2 dependency as "presumed-RCE in untrusted-input flow" and migrate to isolated-vm or process-sandbox.

**langroid CVE-2026-25879** — prompt-to-SQL injection → RCE in langroid agent framework (GitHub Advisories 2026-05-31). Extends the AI-agent-framework attack-surface class (MEMORY: PraisonAI multi-batch). Flagged for any internal LLM-database-bridge tooling.

**Anthropic confirms Claude Mythos-class models rollout to public after delaying for security risks (BleepingComputer 2026-05-31)** — non-CVE policy note. Anthropic acknowledged "identified security risks to software systems" caused the delay; calibration data point for AI-platform threat-model evolution.

**Tenda W12 4-CVE stack-overflow batch + Edimax BR-6478AC pair + Totolink N300RH** — SOHO/router CVSS-9.0 batch via dbugs / PT-Security (2026-05-31). Commodity-router scope; track for Mirai-variant uptake but OOS for corporate-perimeter focus.

**Carnival Cruise Line breach — ~6M customers (SecurityWeek + BleepingComputer 2026-05-28)** — ShinyHunters extortion gang attribution; non-CVE, incident-pattern data point joining Charter (4.9M) and 23andMe litigation in the 2026-Q2 mega-breach cluster.

**Anthropic Claude security plugin / Azure privilege escalation / Kali365 MFA bypass (THN ThreatsDay 2026-05-31)** — weekly roundup-only mentions; specifics unavailable from the roundup pointer alone, flagged for follow-up next cycle if standalone advisories surface.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ unreachable (403) |
| Vendor advisories | fortinet.com/blog/threat-research, msrc.microsoft.com/blog, blog.cloudflare.com/tag/security, fortiguard.com/psirt | ✅ / ⚠️ msrc unreachable |
| Research / OSINT | rapid7.com, schneier.com, avleonov.com, googleprojectzero.blogspot.com→projectzero.google, securitylab.github.com, fortinet.com | ✅ / ⚠️ |
| Supply chain | github.com/advisories (added 2026-05-07), github.com/0xMarcio/cve | ✅ |
| Mailing lists | seclists.org/fulldisclosure, openwall.com/lists/oss-security, kb.cert.org/vuls | ✅ |
| CVE DBs | nvd.nist.gov, opencve.io, app.opencve.io, cve.mitre.org, cve.org | ✅ / ❌ (cve.org + cve.mitre.org JS-only) |
| Bug bounty | hackerone.com/hacktivity, bugcrowd.com/disclosures, attackerkb.com | ❌ unreachable |
| Regional / specialty | dbugs.ptsecurity.com, habr.com/ru/companies/tomhunter/articles, teletype.in/@cyberok, cert.gov.ua | ⚠️ degraded |
| Aggregators | packetstormsecurity.com, github.com/search?q=CVE | ⚠️ / ✅ |

**Errors:** cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403), attackerkb.com (403), msrc.microsoft.com/blog (footer-only after redirect), hackerone.com/hacktivity (JS-only empty), bugcrowd.com/disclosures (404 stale URL), cve.mitre.org (JS-only redirect to cve.org), cve.org (JS-only empty), cert.gov.ua (empty content).
**Degraded:** packetstormsecurity.com (redirects to packetstorm.news), habr.com/ru/companies/tomhunter/articles (no recent posts), teletype.in/@cyberok (no recent posts).
**CISA KEV:** Cannot fetch directly via WebFetch; per prior-report relay coverage (BleepingComputer / THN) the most recent KEV additions are PAN-OS CVE-2026-0257 (2026-05-29, federal deadline 2026-06-01), Asocks botnet infrastructure (2026-05-29 Dutch takedown), and the 2026-05-27 triple-supply-chain add (DAEMON Tools CVE-2026-8398 + TanStack CVE-2026-45321 + Nx Console CVE-2026-48027, deadline 2026-06-10).

---

*Watchtower vulnerability-researcher | Cycle: 2026-06-01/night | Next: 2026-06-02/night*
