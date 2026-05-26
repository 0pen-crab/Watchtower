# Source Effectiveness — 2026-05

| Source | Findings | Noted | Empty | Last Hit |
|--------|----------|-------|-------|----------|
| bleepingcomputer.com | 54 | 47 | 1 | 2026-05-26 (FBI Kali365 OAuth device-code PaaS advisory + Netherlands 800-server bulletproof hosting seizure + Chromium background-JS-after-close disclosure — all NOTED) |
| thehackernews.com | 45 | 23 | 0 | 2026-05-26 (Anthropic Project Glasswing / Mythos 10K-vuln milestone update + Lazarus RemotePE memory-only RAT — both NOTED; TrapDoor relay deferred to socket.dev primary credit) |
| cisa.gov | 0 | 0 | 23 | — |
| securityweek.com | 40 | 24 | 4 | 2026-05-26 (Megalodon 5,500+ repo expansion mention — no new technical primitive, already in dedup) |
| github.com/search | 4 | 8 | 11 | 2026-05-26 (CVE-2026-31802 npm tar path traversal symlink-extract — NOTED; client-side but folds into developer-machine supply-chain pattern) |
| schneier.com | 0 | 13 | 10 | 2026-05-26 (Mythos-discovered macOS M5 kernel memory corruption — NOTED, Apple-hardware-specific) |
| krebsonsecurity.com | 1 | 4 | 18 | 2026-05-26 (Netherlands 800-server hosting seizure — NOTED, credit shared with BleepingComputer) |
| rapid7.com | 3 | 0 | 19 | 2026-05-26 (Metasploit Wrap Up 05/22 — no new exploitation escalation in our window) |
| attackerkb.com | 0 | 0 | 22 | — |
| fortinet.com/blog/threat-research | 0 | 1 | 21 | 2026-05-26 (no new May 22-26 content; P2PInfect Kubernetes/Redis still latest at 2026-05-20) |
| securitylab.github.com | 2 | 1 | 21 | 2026-05-26 (redirected to github.blog/tag/github-security-lab/; no new May 22-26 content) |
| seclists.org/fulldisclosure (incl. openwall oss-security) | 36 | 56 | 3 | 2026-05-26 (Apache Syncope CVE-2026-42782 + CVE-2026-42797 NEWS via oss-security; Apache Shiro 4-CVE batch CVE-2026-43827/43828/44598/48589 NEWS via oss-security) |
| packetstormsecurity.com | 0 | 0 | 22 | — (degraded — homepage only; redirects to packetstorm.news) |
| opencve.io | 23 | 28 | 4 | 2026-05-26 (no new — WP-class CVEs surfaced today already credited to dbugs.ptsecurity.com primary) |
| nvd.nist.gov | 0 | 2 | 21 | 2026-05-26 (used detail-page fallback for CVE-2026-42782 + 45217 + 5222 verification; search page nav-only via WebFetch) |
| cve.mitre.org | 0 | 0 | 22 | — (degraded — redirects to cve.org) |
| cve.org | 0 | 0 | 22 | — (JS-required, no content) |
| googleprojectzero.blogspot.com | 0 | 0 | 22 | — (redirects to projectzero.google; no May 22-26 content) |
| blog.cloudflare.com/tag/security | 0 | 2 | 20 | 2026-05-26 (no new content; Project Glasswing initial update still latest at 2026-05-18) |
| msrc.microsoft.com/blog | 0 | 0 | 22 | — (unreachable — redirects to nav-only page) |
| hackerone.com/hacktivity | 0 | 0 | 22 | — |
| bugcrowd.com/disclosures | 0 | 0 | 22 | — |
| kb.cert.org/vuls | 2 | 6 | 17 | 2026-05-26 (no new May 22-26 entries; VU#980487 Dirty Frag still latest at 2026-05-20) |
| avleonov.com | 0 | 1 | 20 | 2026-05-26 ("In the Trend of VM" #27 published 2026-05-25 covering CVE-2026-31431/34197/32201/34621 — all already in dedup) |
| github.com/0xMarcio/cve | 2 | 7 | 15 | 2026-05-26 (Top 10 recent — CVE-2026-31431 still dominates; no new high-signal additions) |
| dbugs.ptsecurity.com | 12 | 38 | 8 | 2026-05-26 (CVE-2026-5222 Rust Cargo + CVE-2026-42773/74/48837/45216 WP-class SQLi batch + CVE-2026-45217 ThemeHigh Stripe Payment Gateway — all NOTED) |
| habr.com/ru/companies/tomhunter/articles | 0 | 0 | 22 | — (degraded — stale content, March 2026 latest) |
| teletype.in/@cyberok | 0 | 0 | 22 | — (degraded — stale content, February 2026 latest) |
| cert.gov.ua | 0 | 0 | 22 | — (unreachable — empty content via WebFetch) |
| socket.dev/blog (NEW for 2026-05) | 5 | 4 | 8 | 2026-05-26 (TrapDoor cross-ecosystem credential stealer — 34+ packages npm/PyPI/Crates with .cursorrules / CLAUDE.md zero-width-Unicode AI-agent manipulation primitive — NEWS, primary disclosure) |
| openwall.com/lists/oss-security (off-list, primary OSS source) | 33 | 49 | 1 | 2026-05-26 (Apache Syncope CVE-2026-42782 + 42797 NEWS + Apache Shiro 4-CVE batch CVE-2026-43827/43828/44598/48589 NEWS — combined with seclists row above) |
| github advisories (off-list, NEW high-value 2026-05-07) | 26 | 73 | 1 | 2026-05-22 (containerd CVE-2026-46680 runAsNonRoot bypass, Twig follow-ups 46639/46640, @boxlite-ai/boxlite 46703/46695, yeswiki 46670, @network-ai 46701) |
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
