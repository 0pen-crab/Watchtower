# Source Effectiveness — 2026-06

| Source | Findings | Noted | Empty | Last Hit |
|--------|----------|-------|-------|----------|
| bleepingcomputer.com | 19 | 18 | 1 | 2026-06-10 (+3 FINDINGS: Check Point CVE-2026-50751 ZDI + KEV relay → CRITICAL; Veeam CVE-2026-44963 → HIGH; MS June Patch Tuesday 200 CVEs → CRITICAL. +5 NOTED: Chrome V8 ZDI CVE-2026-11645; ServiceNow API auth-bypass; Tchap French govt breach; WhatsApp/NSO disruption; Shai-Hulud/Miasma 73-repo + PyPI supply chain) |
| thehackernews.com | 21 | 17 | 0 | 2026-06-10 (+2 FINDINGS: LiteLLM CVE-2026-42271 KEV add — primary discovery channel; Veeam RCE corroboration. +5 NOTED: Linux nf_tables CVE-2026-23111 LPE+container escape; WinRAR CVE-2025-8088 Russia-aligned continued; FROST SSD-timing attack; UofT self-replicating LLM worm; Hades/Miasma PyPI cross-coverage) |
| securityweek.com | 11 | 16 | 1 | 2026-06-10 (+2 FINDINGS: MS Patch Tuesday 200 CVEs corroborated BC; SAP NetWeaver/Commerce June 4-critical batch. +3 NOTED: Adobe 123 CVEs / AEM-heavy with CVE-2026-34691 9.3 callout; OpenSSL 18 CVEs AI-found high-sev; Chrome 5th ZDI of 2026 corroboration) |
| krebsonsecurity.com | 2 | 1 | 4 | 2026-06-10 (+1 FINDING: "A Record-Breaking Patch Tuesday for June 2026" — 200 CVEs, AI-bug-finding angle, 3 publicly-disclosed ZDI emphasis; useful corroboration + framing for the MS batch entry) |
| rapid7.com | 2 | 2 | 5 | 2026-06-10 (+2 FINDINGS: em-patch-tuesday-june-2026 post = MS batch corroboration; Metasploit Wrap-Up "Apache ActiveMQ RCE + Gogs Rebase RCE + Windows Kernel Pointer Enum" — direct trigger for Tomcat Tribes CVE-2026-34486 UPDATE escalation 7→9. +1 NOTED: Gogs CVE-2026-52806 authenticated RCE patched 06-07) |
| schneier.com | 0 | 4 | 4 | 2026-06-10 (no digest-relevant content — Zcash Orchard Claude-Opus-4.8-found vuln + Anthropic Glasswing critique both off-topic for vendor-advisory digest, calibration only) |
| fortinet.com/blog/threat-research | 0 | 2 | 5 | 2026-06-10 (no new content — FIFA WC 2026-06-04 still latest, no 06-08→10 posts) |
| securitylab.github.com | 0 | 0 | 7 | 2026-06-10 (no new advisories — GHSL-2026-140 7-Zip 2026-05-22 still latest) |
| github.com/search (advisories) | 1 | 1 | 5 | 2026-06-10 (+1 NOTED bucket: CVE-2026-2 search surfaces ActiveMQ Jolokia PoC repo + cPanel CVE-2026-41940 + Linux Copy Fail CVE-2026-31431 Rust PoC + Frigate CVE-2026-25643 + Gogs CVE-2026-52806 + Tomcat Tribes confirmed — primary discovery channel for the two UPDATE escalations) |
| seclists.org/fulldisclosure | 1 | 3 | 5 | 2026-06-10 (+1 FINDING surfaced: SYSS-2026-004 SAP NetWeaver SAML XML Signature Wrapping by Moritz Bechler 2026-06-08 — folded into the SAP June Patch Day entry. +1 NOTED: SEC Consult SA-20260608-0 Genetec RabbitMQ binary planting — niche) |
| openwall.com/lists/oss-security | 4 | 27 | 1 | 2026-06-10 (+1 FINDING: Apache HTTP Server June 13-CVE batch 06-08 — folded into Noted as enterprise-edge fleet maintenance. +5 NOTED: CPython CVE-2026-9669 bz2; Apache Airflow Samba+GCS CVE-2026-49818; Apache Answer 6-CVE batch; Xen XSA-491→494; OpenSSL advisory thread) |
| kb.cert.org/vuls | 0 | 6 | 3 | 2026-06-10 (+1 NOTED: VU#616257 Microsoft-signed UEFI shim Secure Boot bypass 2026-06-09 — flag for SOC threat-model preboot-integrity claims) |
| opencve.io | 0 | 10 | 4 | 2026-06-10 (degraded continuing — returned 2023-era Malwarebytes CVEs only, no June 2026 data; PT-Security dbugs covers this gap) |
| dbugs.ptsecurity.com | 1 | 8 | 2 | 2026-06-10 (+4 NOTED: PT-2026-47807 Ivanti Sentry CVE-2026-10523 CVSS 9.9 — high-priority watchlist as Ivanti edges have KEV history; PT-2026-47844 OpenSSL CVE-2026-45447 — corroboration; PT-2026-48038 Azure Stack Edge CVE-2026-47643 CVSS 9.8; PT-2026-48130 Adobe AEM Forms CVE-2026-34691 CVSS 9.3) |
| github.com/0xMarcio/cve | 2 | 1 | 5 | 2026-06-10 (+2 FINDINGS via index updates: CVE-2026-42588 Apache ActiveMQ Jolokia PoC publication — UPDATE trigger 6→8; CVE-2026-34486 Apache Tomcat Tribes PoC confirmation overlapping Rapid7 Metasploit module — UPDATE trigger 7→9. Also fingerprints for Netlogon 41089, Linux CVE-2026-31431 Copy Fail, Windows RegPwn CVE-2026-24291) |
| blog.cloudflare.com/tag/security | 0 | 0 | 7 | 2026-06-10 (+0 — Frontier Cyber Models customer-zero defensive architecture + Cloudforce One real-time WAF rules posts both Cloudflare-product marketing, not vendor-advisory content) |
| avleonov.com | 0 | 0 | 7 | 2026-06-10 (PAN-OS CVE-2026-0300 RCE retrospective 2026-06-05 still latest — no 06-08→10 posts) |
| cisa.gov (incl. /KEV) | 0 | 0 | 7 | 2026-06-10 (403 Forbidden on both /KEV catalog AND news-events/alerts/2026/06/09/cisa-adds-* fallback today — KEV adds for CVE-2026-50751 + CVE-2026-42271 sourced entirely via THN/BleepingComputer relay; news-events fallback worked 2026-06-03 for Mirasvit but failed today) |
| attackerkb.com | 0 | 0 | 7 | — (403 Forbidden persistent) |
| cve.org / cve.mitre.org | 0 | 0 | 7 | — (JS-required, no content via WebFetch) |
| googleprojectzero.blogspot.com | 0 | 0 | 7 | — (redirects to projectzero.google; Pixel 10 2026-05-13 still latest) |
| msrc.microsoft.com/blog | 1 | 1 | 6 | 2026-06-10 (homepage still nav-only after redirect; MS Patch Tuesday content sourced via BleepingComputer + Krebs + SecurityWeek + Rapid7 relay — direct MSRC blog post listing remains degraded) |
| hackerone.com/hacktivity | 0 | 0 | 7 | — (JS-required) |
| bugcrowd.com/disclosures | 0 | 0 | 7 | — (404 persistent since 2026-04 — flag for SOURCES.md drop in sources-review-2026-06.md) |
| packetstormsecurity.com | 0 | 0 | 7 | — (degraded — redirects to packetstorm.news, homepage nav only) |
| nvd.nist.gov | 0 | 0 | 7 | 2026-06-10 (degraded — WebFetch returns API-transition timeline document, not CVE listing; opencve.io/dbugs.ptsecurity.com cover gap) |
| habr.com/ru/companies/tomhunter | 0 | 0 | 7 | — (degraded — stale through 2026-03-06, ~3-month silence) |
| teletype.in/@cyberok | 0 | 0 | 7 | — (degraded — stale through 2026-02-04, ~4-month silence) |
| cert.gov.ua | 0 | 0 | 7 | — (degraded — empty content) |

## Score Calibration
*(Updated monthly)*

May 2026: pending — sources-review-2026-05.md still owed per MEMORY 2026-06-01 ("deferred to a dedicated run because the MEMORY/sources-meta deltas alone are substantial"). Write at next opportunity.

April 2026: pending — see sources-review-2026-04.md.

## Archive — 2026-05

Top-10 sources by findings (May 2026):
1. bleepingcomputer.com — 63 findings, 57 noted
2. thehackernews.com — 56 findings, 31 noted
3. securityweek.com — 44 findings, 25 noted
4. seclists.org/fulldisclosure (incl. openwall oss-security) — 36 findings, 82 noted
5. openwall.com/lists/oss-security (off-list primary) — 36 findings, 79 noted
6. github advisories (off-list) — 28 findings, 80 noted
7. opencve.io — 23 findings, 35 noted
8. dbugs.ptsecurity.com — 14 findings, 48 noted
9. securityaffairs.com — 5 findings, 3 noted
10. socket.dev/blog — 5 findings, 5 noted; vulncheck.com/advisories — 5 findings, 7 noted (tied)

Bottom-10 (zero findings, persistent silence in May 2026):
- cve.mitre.org, cve.org, googleprojectzero.blogspot.com, msrc.microsoft.com/blog, hackerone.com/hacktivity, bugcrowd.com/disclosures, attackerkb.com, packetstormsecurity.com, nvd.nist.gov, habr.com/ru/companies/tomhunter, teletype.in/@cyberok, cert.gov.ua, schneier.com (calibration-only), fortinet.com/blog/threat-research (1 noted), cisa.gov (relay-only)
- Recommendation: defer formal drop/keep decisions to sources-review-2026-05.md.

---

# Source Effectiveness — 2026-05 (archived row state at end of cycle)

| Source | Findings | Noted | Empty | Last Hit |
|--------|----------|-------|-------|----------|
| bleepingcomputer.com | 63 | 57 | 1 | 2026-06-01 (WP Maps Pro CVE-2026-8732 — NEWS HIGH actively-exploited WordPress plugin admin-creation; Carnival Cruise 6M breach — NOTED) |
| thehackernews.com | 56 | 31 | 0 | 2026-05-31 (PAN-OS GlobalProtect CVE-2026-0257 — NEWS CRITICAL corroborates BC; older 2026-05-29 articles already covered) |
| cisa.gov | 0 | 0 | 27 | — |
| securityweek.com | 44 | 25 | 4 | 2026-05-31 (Flowise CVE-2026-40933 CVSS 9.9 PoC published by Obsidian Security — NEWS HIGH) |
| github.com/search | 5 | 8 | 14 | 2026-05-31 (login required for code search — treated as degraded; github.com/advisories used as substitute, no new high-signal items beyond previously covered PraisonAI + stigmem-node) |
| schneier.com | 0 | 14 | 13 | 2026-05-31 (Chilling Effects + Wi-Fi sensing + FBI 2025 Internet Crime Report — calibration NOTED only) |
| krebsonsecurity.com | 1 | 7 | 20 | 2026-05-31 (still no new post since 2026-05-25 arrests follow-up) |
| rapid7.com | 3 | 0 | 23 | 2026-05-31 (Metasploit Wrap-Up 05/29/2026 still the latest — no new posts) |
| attackerkb.com | 0 | 0 | 25 | — |
| fortinet.com/blog/threat-research | 0 | 1 | 24 | 2026-05-31 (still PureLogs 2026-05-26 latest — no new posts) |
| securitylab.github.com | 2 | 3 | 23 | 2026-05-31 (still GHSL-2026-140 7-Zip 2026-05-22 latest — no new advisories) |
| seclists.org/fulldisclosure (incl. openwall oss-security) | 36 | 82 | 3 | 2026-05-31 (oss-security 2026-05-30 batch: Apache MINA SSHD CVE-2026-48827 + Apache Fluss CVE-2026-49361 + Vim < 9.2.565 + CVE-2026-8594 Text::LineFold + CVE-2025-70103 libjxl + CVE-2025-70116 GPAC — all NOTED; sshfs CVE-2026-47187 + 48711 — NEWS HIGH; seclists/fulldisclosure no new posts since 2026-05-25; oss-security 2026-05-31 empty Sunday) |
| packetstormsecurity.com | 0 | 0 | 25 | — (degraded — homepage only; redirects to packetstorm.news) |
| opencve.io | 23 | 35 | 4 | 2026-05-31 (Synology BeeStation OS CVE-2025-12686 CVSS 9.8 + libjxl CVE-2025-70103 + GPAC/MP4Box CVE-2025-70116 — all NOTED; lower-priority Netis/Tasmota/Dolibarr items skipped) |
| nvd.nist.gov | 0 | 2 | 24 | 2026-05-31 (still JS-heavy; data obtained via opencve.io) |
| cve.mitre.org | 0 | 0 | 25 | — (degraded — redirects to cve.org) |
| cve.org | 0 | 0 | 25 | — (JS-required, no content) |
| googleprojectzero.blogspot.com | 0 | 0 | 25 | 2026-05-31 (Pixel 10 exploit 2026-05-13 still latest — no new content; redirects to projectzero.google) |
| blog.cloudflare.com/tag/security | 0 | 2 | 23 | 2026-05-31 (no new content; Project Glasswing 2026-05-18 still latest) |
| msrc.microsoft.com/blog | 0 | 0 | 25 | — (unreachable — redirects to nav-only page) |
| hackerone.com/hacktivity | 0 | 0 | 25 | — |
| bugcrowd.com/disclosures | 0 | 0 | 25 | — |
| kb.cert.org/vuls | 3 | 6 | 20 | 2026-05-31 (still VU#780781 Casdoor latest — no new VU#) |
| avleonov.com | 0 | 1 | 23 | 2026-05-31 (no new post since Fragnesia on 2026-05-28) |
| github.com/0xMarcio/cve | 2 | 8 | 17 | 2026-05-31 (Apache Tomcat CVE-2026-34486 PoC repos gaining stars — NOTED tooling momentum; Copy Fail Rust PoC continues) |
| dbugs.ptsecurity.com | 14 | 48 | 8 | 2026-06-01 (Tenda W12 4-CVE stack-overflow batch + Edimax BR-6478AC pair + Totolink N300RH CVSS 9.0+ batch — NOTED commodity SOHO router scope) |
| habr.com/ru/companies/tomhunter/articles | 0 | 0 | 25 | — (degraded — stale content, March 2026 latest) |
| teletype.in/@cyberok | 0 | 0 | 25 | — (degraded — stale content, February 2026 latest) |
| cert.gov.ua | 0 | 0 | 25 | — (unreachable — empty content via WebFetch) |
| socket.dev/blog (NEW for 2026-05) | 5 | 5 | 10 | 2026-05-31 (OSV.dev 157 false-positive malware report withdrawal across npm + PyPI — NOTED; no new 2026-05-28→31 posts) |
| openwall.com/lists/oss-security (off-list, primary OSS source) | 36 | 79 | 2 | 2026-06-01 (2026-05-31 archive: Apache Airflow 16-CVE batch incl. CVE-2026-42359 authenticated RCE + CVE-2026-42252 BashOperator Jinja2 — NEWS HIGH; Apache ActiveMQ 6-CVE batch incl. CVE-2026-42588 Jolokia addNetworkConnector RCE — NEWS HIGH; 2026-06-01 archive empty) |
| github advisories (off-list, NEW high-value 2026-05-07) | 28 | 80 | 3 | 2026-06-01 (5 new noted: yamcs-core 3-CVE batch CVE-2026-46621/46562/44632 mission-control RCE; liquidjs CVE-2026-45618 template-engine RCE; nezha CVE-2026-46716 cross-tenant RCE; vm2 5 additional sandbox-escape CVEs CVE-2026-47131/47137/47140/47208/47210; langroid CVE-2026-25879 prompt-to-SQL → RCE) |
| samba.org/samba/security (NEW 2026-05-28, vendor PSIRT direct) | 1 | 1 | 0 | 2026-05-28 (CVE-2026-4408 + CVE-2026-4480 CVSS-10 unauth-RCE pair on file/print servers — NEWS CRITICAL; 4 lower-severity companions — NOTED) |
| jenkins.io/security (NEW 2026-05-28, vendor PSIRT direct) | 1 | 0 | 0 | 2026-05-28 (11-CVE plugin advisory 2026-05-27 incl. LDAP/AD referral RCE — NEWS) |
| adversa.ai/blog (NEW 2026-05-28, AI-coding-agent disclosure channel) | 1 | 0 | 0 | 2026-05-28 (SymJack symlink-hijack against 6 AI coding agents — NEWS, second Adversa AI publication after 2026-05-07 TrustFall) |
| noscope.com (NEW 2026-05-28, novel disclosure channel) | 1 | 0 | 0 | 2026-05-28 (Gitea CVE-2026-27771 private container image exposure — NEWS) |
| crowdstrike.com/blog (NEW 2026-05-28) | 1 | 0 | 0 | 2026-05-28 (GlassWorm botnet takedown disruption announcement — UPDATE) |
| drupal.org/security (off-list, surfaced 2026-05-20 via search) | 3 | 0 | 0 | 2026-05-22 (SA-CORE-2026-004 / CVE-2026-9082 PostgreSQL SQL injection — active exploitation confirmed within 48h of patch) |
| microsoft.com/security/blog (off-list, MSRC blog redirect target — actually-reachable, unlike msrc.microsoft.com/blog homepage which returns nav-only) | 1 | 0 | 0 | 2026-05-20 (Fox Tempest MSaaS disruption — Vanilla Tempest / Storm-0501 / Storm-2561 / Storm-0249 affiliates) |
| vulncheck.com/advisories (off-list, NEW 2026-05-09) | 5 | 7 | 4 | 2026-05-14 |
| wiz.io/blog (off-list) | 1 | 0 | 6 | 2026-05-13 |
| scworld.com (off-list) | 0 | 1 | 4 | 2026-05-04 |
| labs.watchtowr.com (off-list) | 0 | 0 | 9 | 2026-04-29 |
| trendmicro.com (off-list) | 1 | 0 | 6 | 2026-05-06 |
| kaspersky / securelist.com (off-list) | 2 | 0 | 5 | 2026-05-10 |
| safedep.io (off-list) | 0 | 2 | 4 | 2026-05-10 |
| aikido.dev (off-list, KEY hit 2026-05-12 Mini Shai-Hulud 169-pkg) | 1 | 1 | 5 | 2026-05-12 |
| snyk.io/blog (off-list) | 0 | 1 | 5 | 2026-04-30 |
| hiddenlayer.com (off-list, via BleepingComputer relay) | 1 | 0 | 2 | 2026-05-10 |
| securityaffairs.com (NEW 2026-05-12, primary KEV-relay source) | 5 | 3 | 1 | 2026-05-31 (Signal recovery-key SMS phishing campaign — NOTED novel platform-trust-abuse tradecraft; Charter/Asocks/GreyVibe already covered) |
| helpnetsecurity.com (NEW 2026-05-12, breach/news coverage) | 1 | 4 | 3 | 2026-05-31 (Carnival/Asocks/FortiClient EMS already covered — no new leads) |
| fortiguard.com/psirt (NEW 2026-05-13, vendor PSIRT direct) | 1 | 1 | 3 | 2026-05-16 |
| endorlabs.com (NEW 2026-05-13 via BleepingComputer relay, Mini Shai-Hulud Wave 2 attribution) | 1 | 0 | 2 | 2026-05-13 |
| hunt.io (NEW 2026-05-14 via SecurityAffairs relay — discovered Quest KACE SMA active exploitation) | 1 | 1 | 0 | 2026-05-17 (FIRESCALE C2 research) |

## Score Calibration
*(Updated monthly)*

April 2026: pending review — see sources-review-2026-04.md.

## Archive — 2026-04

Top-10 sources by findings (April 2026):
1. bleepingcomputer.com — 27 findings, 13 noted
2. thehackernews.com — 22 findings, 6 noted
3. securityweek.com — 12 findings, 9 noted
4. dbugs.ptsecurity.com — 11 findings, 33 noted
5. opencve.io — 7 findings, 8 noted
6. github.com/search — 4 findings, 9 noted
7. rapid7.com — 3 findings, 3 noted
8. github.com/0xMarcio/cve — 3 findings, 2 noted
9. kb.cert.org/vuls — 2 findings, 5 noted
10. cisa.gov — 1 finding, 0 noted (relayed; direct fetch 403)

Bottom-10 (zero findings, persistent silence):
- cve.mitre.org, cve.org, googleprojectzero.blogspot.com, blog.cloudflare.com/tag/security, msrc.microsoft.com/blog, hackerone.com/hacktivity, bugcrowd.com/disclosures, habr.com/ru/companies/tomhunter/articles, teletype.in/@cyberok, cert.gov.ua, attackerkb.com, packetstormsecurity.com, nvd.nist.gov, fortinet.com/blog/threat-research (only 2 noted), securitylab.github.com (only 2 noted)
- Recommendation: see sources-review-2026-04.md.

## Archive — 2026-03

Top-10 sources by findings (March 2026):
1. bleepingcomputer.com — 3 findings, 3 noted
2. thehackernews.com — 3 findings, 1 noted
3. cisa.gov — 2 findings
4. github.com/0xMarcio/cve — 2 findings, 1 noted
5. securitylab.github.com — 1 finding, 2 noted
6. krebsonsecurity.com — 1 finding
7. github.com/search — 1 finding, 1 noted

Bottom-10 (zero findings 2+ months):
- cve.mitre.org, cve.org, googleprojectzero.blogspot.com, blog.cloudflare.com/tag/security, msrc.microsoft.com/blog, hackerone.com/hacktivity, bugcrowd.com/disclosures, habr.com/ru/companies/tomhunter/articles, teletype.in/@cyberok, cert.gov.ua
- Recommendation: Keep all — these are authoritative sources even if infrequently yielding novel findings. bugcrowd.com/disclosures returned 404 on April 14; verify URL is still valid.
