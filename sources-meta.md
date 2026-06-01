# Source Effectiveness — 2026-05

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
