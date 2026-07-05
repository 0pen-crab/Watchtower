# Source Effectiveness — 2026-07

| Source | Findings | Noted | Empty | Last Hit |
|--------|----------|-------|-------|----------|
| bleepingcomputer.com | 6 | 4 | 1 | 2026-07-05 (no new; JADEPUFFER mainstream repackaging already in dedup, PolinRider primary attribution goes to THN — noted latency calibration) |
| thehackernews.com | 9 | 8 | 0 | 2026-07-05 (+1 FINDING: PolinRider DPRK 108-package supply-chain campaign HIGH promoted from Rollup polyfill Noted; +2 NOTED: Kairos $1M extortion case study, PamStealer macOS Rust infostealer) |
| securityweek.com | 5 | 4 | 0 | 2026-07-05 (+1 NOTED: SharePoint CVE-2026-45659 FCEB deadline expired 2026-07-04; all other cross-refs in dedup) |
| krebsonsecurity.com | 1 | 1 | 1 | 2026-07-05 (no new posts since 2026-07-02 NetNut) |
| rapid7.com | 1 | 0 | 1 | 2026-07-05 (no new posts since 2026-07-03 Metasploit wrap-up) |
| schneier.com | 0 | 2 | 1 | 2026-07-05 (no new posts since 2026-07-03 calibration batch) |
| fortinet.com/blog/threat-research | 0 | 2 | 1 | 2026-07-05 (no new posts since 2026-07-01 Ousaban) |
| securitylab.github.com | 0 | 0 | 2 | 2026-07-05 (still 2026-05-22 batch — 44-day silence; drop candidate confirmed) |
| github.com/search (advisories) | 3 | 2 | 0 | 2026-07-05 (+1 FINDING: CVE-2026-24061 GNU inetutils-telnetd active-exploitation CRITICAL late catch-up; +1 NOTED: CVE-2026-2472 Vertex AI SDK stored XSS AI-platform) |
| seclists.org/fulldisclosure | 0 | 4 | 0 | 2026-07-05 (+2 NOTED: CVE-2026-58451 Horde Groupware IMP path traversal, Zig std.http chunked reader DoS) |
| openwall.com/lists/oss-security | 2 | 22 | 1 | 2026-07-05 (not directly checked; no 2026-07-04 ripple via cross-source references) |
| kb.cert.org/vuls | 0 | 4 | 1 | 2026-07-05 (no new VU# since 2026-07-02 GameFirst) |
| opencve.io / app.opencve.io | 1 | 1 | 1 | 2026-07-05 (marketing page only — no per-CVE data; Chrome 150 batch already in 2026-07-04 dedup) |
| dbugs.ptsecurity.com | 1 | 5 | 0 | 2026-07-05 (+1 NOTED grouped: 2026-07-04 batch n8n CVE-2025-71380 + Fickling CVE-2026-14534/14535 + Vesta CVE-2026-12195 + HestiaCP CVE-2026-12196 + Picklescan 13-CVE CVSS 8.1 cluster) |
| github.com/0xMarcio/cve | 0 | 1 | 1 | 2026-07-05 (+1 NOTED: CVE-2026-31431 "Copy Fail" Linux kernel LPE 9-year-old post-exploit chain material; other entries in dedup) |
| blog.cloudflare.com/tag/security | 0 | 2 | 1 | 2026-07-05 (no new posts since 2026-07-01 Attribution Business Insights) |
| avleonov.com | 0 | 0 | 2 | 2026-07-05 (no new posts since 2026-07-02 Exchange XSS) |
| cisa.gov (incl. /KEV) | 0 | 1 | 2 | 2026-07-05 (403 persistent; SharePoint CVE-2026-45659 FCEB deadline expired Saturday 2026-07-04 via SW cross-reference) |
| attackerkb.com | 0 | 0 | 2 | 2026-07-05 (403 persistent) |
| cve.org / cve.mitre.org | 0 | 0 | 2 | 2026-07-05 (JS-required) |
| googleprojectzero.blogspot.com → projectzero.google | 0 | 0 | 2 | 2026-07-05 (still 2026-05-13; 53-day silence) |
| msrc.microsoft.com/blog | 0 | 0 | 2 | 2026-07-05 (redirect+nav-only persistent) |
| hackerone.com/hacktivity | 0 | 0 | 2 | 2026-07-05 (JS-required) |
| bugcrowd.com/disclosures | 0 | 0 | 2 | 2026-07-05 (404 persistent) |
| packetstormsecurity.com → packetstorm.news | 0 | 0 | 2 | 2026-07-05 (nav-only + TOS persistent) |
| nvd.nist.gov | 0 | 0 | 2 | 2026-07-05 (JS-required — data surfaced via opencve.io) |
| habr.com/ru/companies/tomhunter | 0 | 0 | 2 | — (silent through 2026-03-06, ~4.0-month silence — drop candidate confirmed) |
| teletype.in/@cyberok | 0 | 0 | 2 | — (silent through 2026-02-04, ~5.0-month silence — drop candidate confirmed) |
| cert.gov.ua | 0 | 0 | 2 | — (empty) |

## Missed 2026-07-01 monthly review

sources-review-2026-06.md was owed on 2026-07-01 per MEMORY 2026-06-11 chain but skipped due to the 2026-06-19 → 2026-07-03 reporting-gap window. Also sources-review-2026-05.md still owed per MEMORY 2026-06-01 deferral. Both should be written when time permits — priority items to include:
- **Drop candidates:** habr.com/ru/companies/tomhunter (silent ~4 months), teletype.in/@cyberok (silent ~5 months), bugcrowd.com/disclosures (404 since April), attackerkb.com (403 persistent), packetstormsecurity.com (nav-only persistent).
- **Promote candidates:** openwall.com/lists/oss-security (canonical primary Apache/Perl/Linux batch source per MEMORY 2026-05-04 + 06-11 + 06-13); github.com/advisories (off-list, 28 findings + 82 noted in May).
- **New source signal:** avleonov.com "In the Trend of VM" monthly digest is a durable early-warning channel for Defender/PAN-OS/Linux-kernel active-exploitation flags per MEMORY 2026-06-18.

---

# Source Effectiveness — 2026-06 (archived)

| Source | Findings | Noted | Empty | Last Hit |
|--------|----------|-------|-------|----------|
| bleepingcomputer.com | 36 | 42 | 2 | 2026-06-19 (+4 FINDINGS: F5 NGINX OOB CVE-2026-42530/42055 HIGH, ShapedPlugin CVE-2026-10735 WP build-pipeline backdoor HIGH, Klue→Icarus Salesforce OAuth campaign MEDIUM, SocGholish Operation Endgame takedown MEDIUM; +4 NOTED: Gentlemen RaaS EDR-killer suite, USB-worm crypto-clipper LNK+Tor, Klue integration shutdown HubSpot/SharePoint/Zoom/Gong/Slack, RoguePlanet no-change) |
| thehackernews.com | 35 | 35 | 1 | 2026-06-19 (+2 FINDINGS: F5 NGINX corroborate BC HIGH, Arch AUR 400+ npm 'atomic-lockfile'/bun 'js-digest' postinstall hijack with Rust stealer + eBPF rootkit HIGH; +3 NOTED: INC Ransomware Rust rewrite + Veeam DPAPI dumper, DragonForce 'Backdoor.Turn' MS Teams C2 abuse, REDCap legacy-version UNC6508 InfiniteRed) |
| securityweek.com | 18 | 31 | 2 | 2026-06-19 (+4 FINDINGS: Cisco ISE CVE-2026-20181/20190 admin-RCE HIGH, Splunk AI Toolkit CVE-2026-20266/20265 MEDIUM, Atlassian 100-bulletin Axios/Tomcat/Netty critical-deps MEDIUM, REDCap/UNC6508 relay; +1 NOTED: Klue/Icarus corroboration) |
| krebsonsecurity.com | 2 | 2 | 12 | 2026-06-19 ('Popa' botnet residential-proxy post 2026-06-18 — recent but out of vuln scope; treat as checked-no-finding) |
| rapid7.com | 4 | 3 | 11 | 2026-06-19 (Weekly Metasploit Update + Oracle PeopleSoft/Ivanti/Check Point reruns — all previously covered) |
| schneier.com | 0 | 10 | 9 | 2026-06-19 (+1 NOTED: 2026-06-18 'Embedding Forbidden Text in Spyware to Discourage AI Analysis' — anti-LLM-triage tradecraft, not a vuln) |
| fortinet.com/blog/threat-research | 0 | 3 | 13 | 2026-06-19 (no new posts since 2026-06-11 AsyncRAT — 8-day silence) |
| securitylab.github.com | 0 | 2 | 14 | 2026-06-19 (no new advisories beyond 2026-05-22 batch — 28-day silence) |
| github.com/search (advisories) | 2 | 4 | 9 | 2026-06-19 (recently updated repos all already-covered CVEs: LiteLLM 42208, FortiSandbox 39808, Joomla JCE 48907 detection, Ivanti Sentry 10520, CheckPoint 50751/50752, telnetd 24061, OpenWrt 46368, Form Maker 3359 — no new high-signal items) |
| seclists.org/fulldisclosure | 1 | 5 | 12 | 2026-06-19 (no new posts since 2026-06-15) |
| openwall.com/lists/oss-security | 10 | 56 | 2 | 2026-06-19 (+6 NOTED from 2026-06-18 batch: Linux MediaTek t7xx CVE-2026-43495, Mojolicious::Sessions::Storable CVE-2026-9692, Vim < 9.2.0671 libsodium OOB, Node.js June 2026 cross-line security releases; no NEWS-grade FINDINGS today) |
| kb.cert.org/vuls | 0 | 11 | 8 | 2026-06-19 (no new VU# since 06-17 SignalRGB; treated as checked-no-new) |
| opencve.io | 2 | 22 | 7 | 2026-06-19 (+1 NOTED: InHand IoT routers IR912/IR915 CVE-2026-38716 CVSS 9.8 — moved to grouped Oracle CPU + InHand noted entry; Oracle Coherence 35307 / WebCenter 46781/35286/35296 / MySQL Shell 46850 cluster surfaced) |
| dbugs.ptsecurity.com | 1 | 20 | 8 | 2026-06-19 (general overview only; no per-CVE detail extractable this cycle) |
| github.com/0xMarcio/cve | 3 | 6 | 11 | 2026-06-19 (no new high-signal entries beyond CVE-2026-31431/41089/24061/21858 dedup) |
| blog.cloudflare.com/tag/security | 0 | 1 | 15 | 2026-06-19 (+1 NOTED: Cloudflare 'Build your own vulnerability harness' 2026-06-18 — defender tooling, not vuln) |
| avleonov.com | 1 | 4 | 15 | 2026-06-19 (RedSun CVE-2026-41091 re-mention skipped per dedup — already covered in 2026-05-22 + 2026-05-29 reports; no material change) |
| cisa.gov (incl. /KEV) | 0 | 0 | 16 | 2026-06-19 (403 persistent) |
| attackerkb.com | 0 | 0 | 14 | — (403 Forbidden persistent) |
| cve.org / cve.mitre.org | 0 | 0 | 14 | — (JS-required, no content via WebFetch) |
| googleprojectzero.blogspot.com | 0 | 0 | 14 | — (404 persistent — escalate for drop in sources-review-2026-06.md) |
| msrc.microsoft.com/blog | 1 | 1 | 15 | 2026-06-19 (redirect+nav-only persistent — no in-window blog posts surfaced) |
| hackerone.com/hacktivity | 0 | 0 | 15 | — (JS-required) |
| bugcrowd.com/disclosures | 0 | 0 | 15 | — (404 persistent since 2026-04 — flag for SOURCES.md drop in sources-review-2026-06.md) |
| packetstormsecurity.com | 0 | 0 | 15 | 2026-06-19 ('site under maintenance' splash page returned — degraded → effectively unreachable today) |
| nvd.nist.gov | 1 | 1 | 13 | 2026-06-19 (search interface returned navigation page only; data obtained via opencve.io) |
| habr.com/ru/companies/tomhunter | 0 | 0 | 15 | — (degraded — stale through 2026-03-06, ~3.4-month silence — escalate for drop) |
| teletype.in/@cyberok | 0 | 0 | 15 | — (degraded — stale through 2026-02-04, ~4.4-month silence — escalate for drop) |
| cert.gov.ua | 0 | 0 | 15 | — (degraded — empty content) |
| github.com/advisories (off-list, NEW high-value 2026-05-07) | 28 | 82 | 7 | 2026-06-19 (no new entries surfaced today; consider promoting to SOURCES.md formally per sources-review-2026-06.md) |

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
