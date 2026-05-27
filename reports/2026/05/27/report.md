# Watchtower Night Report — 2026-05-27
**Cycle:** Night | **Generated:** 2026-05-27 00:10 UTC (2026-05-27T00:10:00Z)
**Sources checked:** 23/30 | **CISA KEV total:** gateway 403 (unchanged) | **New KEV additions:** none confirmed since 2026-05-22 Drupal CVE-2026-9082 (federal deadline today)

---

## 🟠 HIGH

### Ghost CMS CVE-2026-26980 Active Mass Exploitation — 700+ Sites Compromised in ClickFix Campaign (Harvard / Oxford / DuckDuckGo Among Targets)
**Product:** Ghost CMS (Content API, versions prior to 6.19.1) | **CVE:** CVE-2026-26980 | **CVSS:** 9.4 | **First reported:** 2026-02 (patched 2026-02 in 6.19.1); active mass exploitation confirmed 2026-05-25

Three days after CVE-2026-26980 first surfaced in our 2026-05-25 report, QiAnXin XLab (research conducted with assistance from Anthropic's Claude) published evidence of an **active mass-exploitation campaign** compromising 700+ Ghost CMS websites — including high-profile victims at Harvard, Oxford, and DuckDuckGo. The unauthenticated SQL injection in Ghost's Content API allows arbitrary database reads, which attackers chain to extract the site's Admin API Key, then use that key to inject malicious JavaScript via Ghost's content-modification APIs. The injected JavaScript drives **ClickFix social-engineering attacks** against site visitors — the same chain that BleepingComputer and SecurityWeek both lead with on 2026-05-25 / 2026-05-26. Ghost is a default-publishing platform for newsletters, blogs, and small/medium publisher sites; the wide victim profile (top-tier research universities + privacy-focused search engine) confirms widespread unpatched-instance exposure on an SQLi disclosed and patched four months ago. Distinct from cPanel CVE-2026-41940 (auth-bypass → ransomware) and Drupal CVE-2026-9082 (PostgreSQL SQLi → KEV) but the same shape: **CMS pre-auth SQLi disclosed → mass exploitation on the long tail of unpatched instances** — recur every 6-8 weeks across the WordPress / Drupal / Ghost / Joomla / Magento ecosystem.

**Timeline:** Patch shipped 2026-02 (Ghost 6.19.1) → SocRadar / Wordfence / Patchstack tracking 2026-04 → coverage in our 2026-05-25 report as initial News → QiAnXin XLab + Anthropic Claude joint research confirming 700+ compromised sites + ClickFix monetization, published 2026-05-25 → BleepingComputer / SecurityWeek / THN coverage 2026-05-25 → THN secondary detail 2026-05-26.

**Why it matters:** **Materially escalates from "patched bug, scattered exploitation" to "active mass-exploitation wave with public-relations-grade victims"**, triggering Update criteria (incident activity confirmed by reporting). The Harvard / Oxford / DuckDuckGo headline lift will accelerate scanner attention — any unpatched Ghost CMS at scale should expect attempted compromise within hours. Also a notable case study in AI-assisted security research: QiAnXin XLab explicitly credits Claude for analysis assistance, making this the first major mass-exploitation campaign analyzed using a frontier AI model as part of the research workflow.

**Discovered by:** Original disclosure / patch credit retained with Ghost Security Team (2026-02); active-exploitation campaign disclosed by QiAnXin XLab (with Anthropic Claude as research assistant) 2026-05-25.

**Mitigation:**
- Confirm Ghost CMS version ≥ 6.19.1 on every Ghost deployment in fleet. Treat any unpatched instance as **presumed compromised** and rotate the Admin API Key + audit all published content for injected JavaScript.
- Hunt published content for `eval(`, `atob(`, `document.write`, `window.location.replace`, and any unexplained `<script src=` references to non-vendor domains since 2026-02.
- For high-profile Ghost deployments (publishers, education, large blogs), audit visitor-side referrer logs for ClickFix landing-page redirects — common pattern is fake captcha / fake browser-update prompt → PowerShell paste.
- For Ghost sites where Admin API Key may have been exfiltrated: revoke the existing key, generate a new one, audit all published Posts / Pages for content changes since key creation, and review Ghost's Members section for unexpected admin or owner additions.
- At the WAF / CDN tier, deploy a rule blocking `?filter=` and `?include=` query strings to `/ghost/api/content/` containing SQL keywords — temporary defense if instant patching is impossible.

**Sources:** [TheHackerNews — Ghost CMS Vulnerability Exploited in Active ClickFix Campaign (May 25, 2026)](https://thehackernews.com/2026/05/ghost-cms-clickfix-campaign.html) | [BleepingComputer — 700 websites hijacked via Ghost CMS flaw (May 25, 2026)](https://www.bleepingcomputer.com/news/security/) | [SecurityWeek — Over 700 sites compromised via Ghost CMS vulnerability (May 26, 2026)](https://www.securityweek.com/) | [QiAnXin XLab research (Claude-assisted) — Mass Exploitation Analysis](https://blog.xlab.qianxin.com/)

---

### Joomla! com_users Triple Critical Privilege-Escalation Batch — CVE-2026-48898 / 48899 / 48904 (CVSS 9.8, Unauthenticated)
**Product:** Joomla! CMS 4.0.0 → 5.4.5 and 6.0.0 → 6.1.0 (com_users component — batch tasks + group editing webservice endpoint) | **CVE:** CVE-2026-48898, CVE-2026-48899, CVE-2026-48904 | **CVSS:** 9.8 (CRITICAL) each | **First reported:** 2026-05-26

Three coordinated Joomla! Project security advisories published to NVD 2026-05-26 with NIST-confirmed CVSS 9.8 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) on each entry — all classified as **CWE-284 Improper Access Control** with **no authentication required**. Two distinct attack surfaces: **com_users batch task** (CVE-2026-48898 + CVE-2026-48899) and **com_users group editing webservice endpoint** (CVE-2026-48904). Both attack surfaces permit unauthenticated privilege escalation via missing access-validation checks. Affected: Joomla! 4.0.0 → 5.4.5 (current stable line including LTS) and pre-release 6.0.0 → 6.1.0. The Joomla! com_users component handles user account management — privilege escalation here yields administrator-level access to user databases, password-reset workflows, and (depending on Joomla configuration) the ability to add Super User accounts. Joomla powers roughly 1.5-3% of all live websites globally per W3Techs (second-largest open-source CMS after WordPress) — internet-exposed scope is multi-million sites.

**Timeline:** Joomla Project advisories published to NVD 2026-05-26 with CVSS 9.8 from NIST; CVSS 4.0 also assessed at 8.2 HIGH (the lower v4.0 score is the standard "less network reach, but same impact" calibration of v4.0 vs v3.1 — defenders should use v3.1 for triage). No public PoC observed at time of writing; no KEV addition yet.

**Why it matters:** Joomla pre-auth CRITICAL CVEs with broad version coverage historically trigger mass-scanner exploitation waves within 24-72h of advisory publication — the Joomla equivalent of the Drupalgeddon trajectory (cf. SA-CORE-2026-004 / CVE-2026-9082 KEV-added 2026-05-22, MEMORY 2026-05-20 / 2026-05-23). Three CVSS 9.8 unauth-priv-esc CVEs landing on the same component on the same day strongly suggests a coordinated audit by a researcher (Joomla typically batches related CVEs in single advisories — three separate IDs indicates distinct issue paths). Federal-style triage SLAs (<14 days) should apply on any internet-facing Joomla deployment regardless of vertical.

**Discovered by:** Researcher credit not yet visible on NVD entries; will surface on Joomla Security Center advisory page within 24-48h.

**Mitigation:**
- Inventory every Joomla! deployment in scope. Patch any Joomla 4.0.0 → 5.4.5 and 6.0.0 → 6.1.0 deployment to the patched line **immediately**. Check developer.joomla.org/security-centre for exact patched version once Joomla publishes the JSST-201X-XXX advisory.
- Until upgrade: at the WAF / reverse-proxy tier, block unauthenticated POST requests to `/administrator/components/com_users/users.php?task=users.batch` and to `/api/index.php/v1/users/groups` (the api.php webservice endpoint).
- Audit Joomla Super User account list and user-group membership for unexplained additions since 2026-05-25. Reset all admin passwords post-upgrade as standard hygiene.
- For Joomla shops with public-facing sites that cannot patch within 72h: deploy Wordfence / Patchstack / Atomicorp / similar virtual-patching at the WAF tier; pre-priority signatures for these CVEs are likely to ship within 24-48h.
- Track scanner activity for `?option=com_users&task=batch` and `?option=com_users&task=group` URI patterns from non-baseline IPs — these are the canonical exploit-attempt signatures.

**Sources:** [NVD — CVE-2026-48898 (Joomla! com_users batch task privilege escalation, CVSS 9.8)](https://nvd.nist.gov/vuln/detail/CVE-2026-48898) | [NVD — CVE-2026-48899 (Joomla! com_users batch task privilege escalation, CVSS 9.8)](https://nvd.nist.gov/vuln/detail/CVE-2026-48899) | [NVD — CVE-2026-48904 (Joomla! com_users group editing webservice endpoint privilege escalation, CVSS 9.8)](https://nvd.nist.gov/vuln/detail/CVE-2026-48904) | [dbugs.ptsecurity.com — Joomla! batch (2026-05-26)](https://dbugs.ptsecurity.com)

---

## 🟡 MEDIUM

### Digital Knowledge KnowledgeDeliver Zero-Day RCE — CVE-2026-5426 (ASP.NET ViewState Deserialization via Hardcoded Machine Keys, Godzilla Web Shell + Cobalt Strike Deployment)
**Product:** Digital Knowledge KnowledgeDeliver (Learning Management System — predominantly deployed in Japan) — vulnerable deployments prior to 2026-02-24 vendor-shipped patch | **CVE:** CVE-2026-5426 | **CVSS:** 7.5 | **Published:** 2026-05-25 (vendor + Mandiant + GTIG joint disclosure)

Mandiant and Google Threat Intelligence Group (GTIG) jointly disclosed an active zero-day exploitation campaign 2026-05-25 against Digital Knowledge's **KnowledgeDeliver** Learning Management System (the canonical LMS for Japanese higher-education + enterprise-training deployments). The root-cause primitive is **hardcoded ASP.NET `machineKey` values shipped in the product's `web.config`** — an unauthenticated remote attacker who knows the machine key (now publicly disclosed) can forge a valid `__VIEWSTATE` payload, triggering ASP.NET `LosFormatter.Deserialize()` → arbitrary type-confusion → RCE. The technical class is identical to the Telerik UI / Sitecore / SharePoint ASP.NET-ViewState-deserialization wave dating back to Microsoft's February 2025 advisory on machine-key abuse. Post-exploitation: attackers dropped the **Godzilla web shell** and the **Cobalt Strike Beacon**. Geographic targeting is Japan-skewed but the platform has international academic deployments. The patched product line was released 2026-02-24 by Digital Knowledge with rotated machine-key defaults; exploitation in the wild has been observed since at least early May per Mandiant timeline.

**Mitigation:** (1) Identify any KnowledgeDeliver deployment in scope and apply the 2026-02-24 vendor patch immediately, rotating `machineKey` values to environment-unique cryptographically-random keys per Microsoft's standard ASP.NET hardening guidance. (2) Hunt IIS access logs for `__VIEWSTATE` POST payloads larger than baseline (typical exploit payloads are 4-8 KB), particularly to `/Public/Login.aspx` and `/Admin/` endpoints. (3) Hunt host-side disk and memory for **Godzilla web shell** artifacts — typically ASP.NET ASPX files with single-line `<%@ Page %>` directives containing base64-encoded payloads — and for **Cobalt Strike Beacon** named-pipe / process-injection markers (well-documented EDR signatures exist). (4) Treat this as a pattern data point: any ASP.NET-based product shipped with a default `web.config` containing literal `validationKey` / `decryptionKey` values is presumptive ViewState-deserialization-class until proven otherwise — inventory across all internet-facing IIS apps in fleet. (5) If KnowledgeDeliver Auth + Authorization are integrated with a corporate IdP (likely on enterprise deployments), assume IdP-credential exposure: rotate any service-account credentials issued to KnowledgeDeliver.

**Sources:** [TheHackerNews — KnowledgeDeliver Zero-Day Exploited via Hardcoded ASP.NET Keys (2026-05-25)](https://thehackernews.com/2026/05/knowledgedeliver-zero-day.html) | [BleepingComputer — KnowledgeDeliver Godzilla Web Shell Campaign](https://www.bleepingcomputer.com/news/security/) | [SecurityWeek — Mandiant Confirms KnowledgeDeliver Zero-Day Active Exploitation](https://www.securityweek.com/)

---

### Microsoft SharePoint Server CVE-2026-45659 Post-Auth Deserialization RCE (CVSS 8.8) — Late-Disclosure From May 2026 Patch Tuesday
**Product:** Microsoft Office SharePoint Server (specific affected versions per MSRC advisory) | **CVE:** CVE-2026-45659 | **CVSS:** 8.8 (HIGH) AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H | **Published:** 2026-05-22 (NVD), modified 2026-05-26

NVD published Microsoft SharePoint Server CVE-2026-45659 on 2026-05-22 with NVD enrichment touch-up 2026-05-26 — **Deserialization of Untrusted Data (CWE-502) allowing an authorized attacker to execute code over a network**. Microsoft-assigned CVSS 8.8 reflects the authenticated-but-low-privilege requirement (PR:L) combined with full Confidentiality / Integrity / Availability impact and network reach. The deserialization-on-SharePoint pattern recurs in this product family (ToolShell CVE-2025-49706, prior 2024-2025 ToolPane wave); on-prem SharePoint Server farms with internet-facing collaboration sites are the canonical exposure surface. The CVE was **not** featured in the BleepingComputer / The Hacker News / SecurityWeek headline coverage of Microsoft's 2026-05 Patch Tuesday (2026-05-13) — fitting the **Patch Tuesday CVE-list relayer divergence** pattern documented in MEMORY 2026-05-14 (where MDASH-attributed Patch Tuesday CVEs do not consistently appear in single-relayer summary feeds). THN surfaced CVE-2026-45659 explicitly in its 2026-05-25 / 2026-05-26 daily coverage as a late-attention disclosure. No public PoC yet, no in-the-wild exploitation confirmed; treat as imminent-tooling-class.

**Mitigation:** Apply 2026-05 Patch Tuesday updates to all SharePoint Server farms (every product version per MSRC affected-products table). Until patch: (1) review Web Part deployment permissions — only Site Collection Administrators and Farm Administrators should be able to upload deserialization-capable Web Parts; (2) audit SharePoint farm authentication-event logs for unusual `/_layouts/15/` access from non-baseline accounts; (3) for SharePoint farms with public-internet-facing collaboration sites, consider geo / IP-allowlist segmentation on the on-prem WAF until patch. Treat any SharePoint farm with on-prem deployment as on the "ToolShell-class quarterly Patch Tuesday RCE" cadence — schedule quarterly Web Part inventory + permission audits independent of patch tempo.

**Sources:** [NVD — CVE-2026-45659 SharePoint Deserialization RCE (CVSS 8.8)](https://nvd.nist.gov/vuln/detail/CVE-2026-45659) | [Microsoft MSRC — CVE-2026-45659 Update Guide](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45659) | [TheHackerNews — Microsoft SharePoint CVE-2026-45659 (2026-05-25 / 2026-05-26)](https://thehackernews.com/)

---

### FUXA Industrial SCADA Multi-CVE Pre-Auth RCE Batch (CVE-2026-43945 / 43946 / 43947) — Open-Source SCADA / HMI Platform
**Product:** FUXA (open-source web-based SCADA / HMI / IIoT platform — frangoteam/FUXA) | **CVE:** CVE-2026-43945, CVE-2026-43946, CVE-2026-43947 (high) plus three companion critical advisories reserved as GHSA | **CVSS:** to be confirmed (NVD entries in RESERVED status as of 2026-05-26) | **Published:** 2026-05-26 (GitHub Security Advisory database)

GitHub Security Advisory database surfaced 2026-05-26 a coordinated multi-CVE batch on the **FUXA** open-source SCADA / HMI / IIoT platform: **CVE-2026-43947 Pre-Auth RCE via Script Test Mode Authorization Bypass**, **CVE-2026-43946 Unauthenticated Arbitrary Tag Value Disclosure via `/api/getTagValue`**, **CVE-2026-43945 Pre-Auth RCE via Path Manipulation & Configuration Injection**, plus three additional **critical** GHSA advisories on the same project: unauthenticated RCE via arbitrary file write in the upload API, unauthenticated remote arbitrary device-tag write, and unauthenticated remote arbitrary scheduler write — totaling **10 disclosed FUXA vulnerabilities across critical + high severity** since February 2026 (per the GitHub-advisories page). Researcher credit: **unocelli** for most of the batch. FUXA is purpose-built for industrial control system / HMI / IIoT deployments where it is commonly stood up on shop-floor networks with reduced authentication assumptions — pre-auth RCE on an industrial-OT platform is treated as critical-class regardless of CVSS even before NVD enrichment lands.

**Mitigation:** Upgrade every FUXA instance in scope to the patched version (consult github.com/frangoteam/FUXA/releases for the latest tag; the security advisories cluster suggests version > 1.3.0-XXXX is required). Until patch: (1) restrict FUXA's web UI to OT-isolated networks only — **never internet-facing**; (2) deploy network-level egress restrictions on the FUXA host to its required upstream device protocols only; (3) audit FUXA's `scripts/` directory for unexpected user-supplied JavaScript snippets; (4) audit FUXA's project-store directory for unexpected file additions / configuration overrides since 2026-05-01; (5) for any FUXA deployment reachable from anything other than OT operator-station workstations, assume pre-compromise possible. Add this to the recurring **self-hosted-OT-platform-default-no-auth** pattern alongside FastNetMon (today's Noted), Kopia (MEMORY 2026-05-22), Open WebUI (MEMORY recurring), nginx-ui (MEMORY recurring).

**Sources:** [GitHub Security Advisories — FUXA frangoteam/FUXA (10 advisories)](https://github.com/frangoteam/FUXA/security/advisories) | [GitHub Advisories Database — FUXA filter (2026-05-26)](https://github.com/advisories?query=FUXA)

---

## 📋 Noted / Monitoring

**MCP Server Server-Side Request Forgery Batch — Anthropic mcp-server-fetch + Microsoft playwright-mcp (Full Disclosure, 2026-05-25)** — Coordinated disclosure of SSRF (CVSS 7.5) in two widely-deployed Model Context Protocol server implementations from Anthropic and Microsoft — both reachable via WebFetch / Playwright primitives, fetching attacker-controlled URLs from the server-process's network context. Already public via GitHub issues per the original disclosure. Extends MEMORY 2026-04 pattern: **MCP-server unauth RCE / authz bypass** — now nine documented MCP-server CVEs in 60 days. Defensive priority: review every MCP server in fleet for default-no-auth and network-egress restrictions; treat all MCP-server processes as if they had server-side-fetch privileges by default.

**FastNetMon BGP NLRI Decoder Stack-Based Buffer Overflow Batch — CVE-2026-48686 (CVSS 9.8) + 48688 + 48692 + 48695 (2026-05-26 NVD)** — FastNetMon Community Edition (open-source BGP-based DDoS detection platform) has multiple pre-auth memory-safety + auth-bypass + OS-command-injection vulnerabilities; CVE-2026-48686 (CVSS 9.8 stack overflow in `decode_bgp_subnet_encoding_ipv4_raw()`) is the headline primitive — an unauthenticated BGP packet with an oversized `prefix_bit_length` (uncapped at 32 for IPv4) triggers a controllable up-to-28-byte stack overflow with arbitrary code execution on the FastNetMon host. CVE-2026-48692 is an unauthenticated gRPC API on port 50052 (no auth required for DoS / script execution); CVE-2026-48695 is OS command injection in the MikroTik router plugin. FastNetMon is deployed by ISPs / hosting providers / large enterprises for transit-level DDoS detection — successful compromise yields a position in the BGP control-plane visibility layer. Limited deployment scope keeps this at Noted unless ITW exploitation surfaces.

**Apache Flink Kubernetes Operator SSRF + Local File Access — CVE-2026-40564 (oss-security, 2026-05-26)** — Gyula Fora posted server-side request forgery + local file access issues in the Apache Flink Kubernetes Operator. Continues the May 2026 Apache CVE wave (MINA / CXF / HTTP / Tomcat / OFBiz / Wicket / Syncope / Shiro / Flink) — the Apache project's coordinated disclosure cadence remains the highest-signal monthly rhythm. K8s-shops running Flink should track this for patched-version detail; impact is K8s-Operator-scope (cluster admin authority subset).

**Perl Archive::Tar Triple-CVE Path-Traversal + Memory-Exhaustion Batch — CVE-2026-42496 / 42497 / 9538 (oss-security, 2026-05-26)** — Stig Palmquist disclosed three Archive::Tar (Perl) vulnerabilities below version 3.08 / 3.10: symlink extraction to attacker-controlled targets (CVE-2026-42496), hardlink extraction to attacker-controlled paths (CVE-2026-42497), and memory exhaustion via crafted tar header size field (CVE-2026-9538). Joins **CVE-2026-31802 npm tar path traversal** (noted 2026-05-26) in the broader tarball-handling-library symlink-class pattern — defenders should treat any toolchain that extracts attacker-supplied tarballs (CI/CD, package managers, backup software) as in-scope until patches land.

**Perl Regex Heap Buffer Overflow — CVE-2026-8376 (oss-security, 2026-05-26)** — Timothy Legge disclosed a heap buffer overflow in Perl regex compilation through 5.43.10 — repeated-pattern compilation triggers the overflow. Reachable from any environment where Perl compiles attacker-influenced regex; relevant for CGI / log-processing / data-pipeline workloads. Tracking for patched-version detail.

**XWiki Platform Critical-Severity Pair — CVE-2026-33137 (Unauth XAR Import via REST `/wikis/{wikiName}`) + CVE-2026-23734 (Path Traversal in ssx/jsx Endpoints) (GitHub Advisories, 2026-05-26)** — XWiki has shipped multiple critical advisories in 2026 (joins prior XWiki-platform-REST CVE clusters); pre-auth XAR-import + path-traversal pair on an enterprise wiki / knowledge-management platform. Tracking — XWiki is well-deployed at large research/education institutions; watch for KEV escalation if exploitation surfaces.

**FBI Kali365 OAuth Device-Code Phishing-as-a-Service Advisory (BleepingComputer 2026-05-25)** — FBI alert republished in BleepingComputer 2026-05-26 daily cycle; same content as our 2026-05-26 Noted entry (no material change). Skipping.

**ZTE Router Multi-CVE Batch — CVE-2026-34472 / 34473 / 34474 + CVE-2021-21735 (Full Disclosure 2026-05-25)** — m.nageh disclosed 17+ ZTE ZXHN router models with ~140,000 publicly-exposed devices affected by oversized POST body unauthenticated DoS (CVE-2026-34473 CVSS 7.5), H188A V6 pre-login wizard credential leak (CVE-2026-34472), and H298A/H108N admin credential exposure (CVE-2026-34474); ZTE H108N marked end-of-life with no patch planned. Consumer-grade ISP-distributed router scope; track in case Mirai-variant operators integrate (historical pattern: Ubiquiti / Hikvision / Dahua CVEs enrolled within days, MEMORY 2026-05-22).

**Charter Communications Breach Confirmed by ShinyHunters Extortion (BleepingComputer 2026-05-26)** — Charter Communications confirmed a breach after ShinyHunters extortion threat. Customer-data-class breach; pattern continuation of the CoinbaseCartel cluster (Grafana / Salesforce / Drupal-PSA wave 2026-05). Not vulnerability-class but worth tracking for credential reuse / phishing-pretext exposure on shared-employee identity material.

**7-Eleven 185,000-Record Breach Confirmed (BleepingComputer 2026-05-26)** — 7-Eleven confirmed exposure of 185,000 individuals' personal data attributed to ShinyHunters; consistent with the 2026-05-19 600K-record 7-Eleven Salesforce breach (MEMORY 2026-05-19). The 185K number is a subset / re-attribution. Tracking for additional breach scope expansion.

**MuddyWater (Iran) DLL Side-Loading Campaign Across 9 Countries (THN 2026-05-26)** — MuddyWater (Iran/MOIS) ran a DLL-side-loading campaign targeting industrial / electronics manufacturing, education, and financial sectors across 9 countries. Adversary-tradecraft Noted; joins MEMORY 2026-05-07 Teams-helpdesk MuddyWater attribution and confirms continuing operational tempo from this cluster.

**Nimbus Manticore (Iran) MiniFast Backdoor — Allegedly AI-Assisted Development (THN 2026-05-26)** — Iranian Nimbus Manticore cluster shipped MiniFast backdoor; deployment included code patterns researchers attribute to AI-assisted development. Joins MEMORY 2026-05-12 Google GTIG **first ITW AI-generated 0-day** disclosure — second documented AI-assisted-development attribution against an active threat-actor cluster. Tracking AI-assisted offensive operations as a recurring class.

**Lazarus RemotePE Memory-Only RAT (THN 2026-05-25 / 2026-05-26)** — DPRK-attributed multi-stage attack chain deploying memory-resident-only RAT against DeFi / crypto sector financial institutions; covered in our 2026-05-26 report, no material change.

**Kimwolf IoT Botnet Botmaster Arrest — Record 30 Tbps DDoS (Krebs 2026-05-26)** — Krebs reported the arrest of a 23-year-old Ottawa resident operating the Kimwolf IoT botnet; >25,000 attack commands, peak 30 Tbps DDoS attack volume (record), >$1M aggregate victim losses. Law-enforcement Noted; expect short-term shifts in IoT-botnet-as-a-service supply / pricing for booter / stresser services.

**Scattered Spider Member Tyler Buchanan Guilty Plea (Krebs 2026-05-26)** — British national Tyler Buchanan, senior member of Scattered Spider, pleaded guilty to wire fraud + identity theft tied to 2022 phishing campaigns targeting major tech companies; >$8M stolen cryptocurrency. Law-enforcement Noted; consistent with sustained legal pressure on The Com ecosystem.

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
**Supplemental sources hit (not counted in 30):** openwall.com/lists/oss-security (2026-05-26 archive ✅ — primary source for Perl Archive::Tar batch + Perl regex CVE-2026-8376 + Apache Flink K8s Operator CVE-2026-40564 + qSnapper D-Bus batch + Mojolicious::Plugin::Statsd metric injection); github.com/advisories (Critical/High filter on 2026-05-26 ✅ — primary source for FUXA, XWiki, Joomla cross-reference); nvd.nist.gov detail pages (used as fallback for CVE enrichment on Joomla 48898 + SharePoint 45659 + FastNetMon 48686); github.com/frangoteam/FUXA/security/advisories (FUXA project portal); thehackernews.com/search (Ghost CMS active-exploitation campaign detail); kb.cert.org/vuls (no new VU# since 2026-05-20 VU#980487 Dirty Frag).
**CISA KEV:** Gateway 403 unchanged — no new additions confirmed since 2026-05-22 (Drupal CVE-2026-9082 federal deadline 2026-05-27 = today, mass exploitation continues per BleepingComputer relay). Tomorrow's report should re-attempt KEV REST API.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-27/night | Next: 2026-05-28/night*
