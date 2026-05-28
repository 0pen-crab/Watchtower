# Source Effectiveness — 2026-05

| Source | Findings | Noted | Empty | Last Hit |
|--------|----------|-------|-------|----------|
| bleepingcomputer.com | 56 | 51 | 1 | 2026-05-28 (LiteSpeed cPanel CVE-2026-48172 KEV-listed any-user-to-root — NEWS; GlassWorm botnet takedown — UPDATE; Stark Industries seizure relay — NOTED) |
| thehackernews.com | 49 | 27 | 0 | 2026-05-28 (Gitea CVE-2026-27771 unauth private container image exposure — NEWS; mouse5212-super-formatter Malware-Slop npm targeting Claude /mnt/user-data — NOTED) |
| cisa.gov | 0 | 0 | 25 | — |
| securityweek.com | 43 | 24 | 4 | 2026-05-28 (LiteSpeed cPanel zero-day + Pretalx CVE-2026-41241 100% talk acceptance + SymJack AI-coding-agent supply-chain — all NEWS; GlassWorm takedown — UPDATE) |
| github.com/search | 4 | 8 | 13 | 2026-05-28 (no new high-signal additions) |
| schneier.com | 0 | 13 | 12 | 2026-05-28 (no new vulnerability-class content) |
| krebsonsecurity.com | 1 | 7 | 18 | 2026-05-28 (Stark Industries 800-server seizure 2026-05-25 — NOTED) |
| rapid7.com | 3 | 0 | 21 | 2026-05-28 (no new Metasploit Wrap-Up since 2026-05-22; required retry after initial /blog/ timeout) |
| attackerkb.com | 0 | 0 | 24 | — |
| fortinet.com/blog/threat-research | 0 | 1 | 23 | 2026-05-28 (PureLogs phishing campaign 2026-05-26 — OOS-client) |
| securitylab.github.com | 2 | 3 | 22 | 2026-05-28 (Chatwoot GHSL-2026-059 SQL injection + Mesa CVE-2026-29075 benchmarks.yml workflow — both NOTED; 7-Zip batch dup) |
| seclists.org/fulldisclosure (incl. openwall oss-security) | 36 | 70 | 3 | 2026-05-28 (Samba 4.24.3/4.23.8/4.22.10 unauth-RCE pair surfaced via oss-security 2026-05-27 → NEWS CRITICAL; Jenkins 2026-05-27 advisory 11-CVE batch → NEWS; Perl CPAN batch + Apache Artemis CVE-2026-40914 + OpenStack Swift CVE-2026-49010 + Linux io_uring/zcrx CVE-2026-43121 — all NOTED via oss-security 2026-05-27) |
| packetstormsecurity.com | 0 | 0 | 24 | — (degraded — homepage only; redirects to packetstorm.news) |
| opencve.io | 23 | 32 | 4 | 2026-05-28 (CVE-2026-4802 RHEL Cockpit + CVE-2026-48687 FastNetMon Juniper plugin + CVE-2026-37711 Dolibarr — all NOTED) |
| nvd.nist.gov | 0 | 2 | 23 | 2026-05-28 (search/feed pages return navigation only via WebFetch — JS-heavy. Marked unreachable. Data obtained via opencve.io.) |
| cve.mitre.org | 0 | 0 | 24 | — (degraded — redirects to cve.org) |
| cve.org | 0 | 0 | 24 | — (JS-required, no content) |
| googleprojectzero.blogspot.com | 0 | 0 | 24 | — (redirects to projectzero.google) |
| blog.cloudflare.com/tag/security | 0 | 2 | 22 | 2026-05-28 (no new content; Project Glasswing initial post still latest at 2026-05-18) |
| msrc.microsoft.com/blog | 0 | 0 | 24 | — (unreachable — redirects to nav-only page) |
| hackerone.com/hacktivity | 0 | 0 | 24 | — |
| bugcrowd.com/disclosures | 0 | 0 | 24 | — |
| kb.cert.org/vuls | 2 | 6 | 19 | 2026-05-28 (no new VU# since 2026-05-20 VU#980487 Dirty Frag) |
| avleonov.com | 0 | 1 | 22 | 2026-05-28 (no new post since In the Trend of VM #27 on 2026-05-25) |
| github.com/0xMarcio/cve | 2 | 7 | 17 | 2026-05-28 (no new high-signal additions; Copy Fail Rust PoC gained stars but no material change) |
| dbugs.ptsecurity.com | 13 | 39 | 8 | 2026-05-28 (PT-2026-43573 / CVE-2026-8832 WPCode WordPress plugin CVSS 8.8 — NOTED, continues PT-Security WP-CVE-relay pattern) |
| habr.com/ru/companies/tomhunter/articles | 0 | 0 | 24 | — (degraded — stale content, March 2026 latest) |
| teletype.in/@cyberok | 0 | 0 | 24 | — (degraded — stale content, February 2026 latest) |
| cert.gov.ua | 0 | 0 | 24 | — (unreachable — empty content via WebFetch) |
| socket.dev/blog (NEW for 2026-05) | 5 | 4 | 10 | 2026-05-27 |
| openwall.com/lists/oss-security (off-list, primary OSS source) | 33 | 58 | 1 | 2026-05-28 (Samba CVE-2026-4408 + 4480 CVSS-10 unauth-RCE pair via vendor advisory + Jenkins 2026-05-27 advisory + Perl CPAN batch + Apache Artemis CVE-2026-40914 + OpenStack Swift CVE-2026-49010 + Linux io_uring/zcrx CVE-2026-43121 — all surfaced via this channel) |
| github advisories (off-list, NEW high-value 2026-05-07) | 27 | 75 | 2 | 2026-05-28 (no new posts since 2026-05-26 FUXA batch + XWiki pair) |
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
| securityaffairs.com (NEW 2026-05-12, primary KEV-relay source) | 5 | 2 | 1 | 2026-05-17 (Exchange KEV addition) |
| helpnetsecurity.com (NEW 2026-05-12, breach/news coverage) | 1 | 4 | 2 | 2026-05-15 |
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
