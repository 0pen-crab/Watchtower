# Sources Review — April 2026

## Top sources by findings

| Rank | Source | Findings | Noted | Notes |
|------|--------|----------|-------|-------|
| 1 | bleepingcomputer.com | 27 | 13 | Strongest single source — first to surface most major incidents (cPanel, Mini Shai-Hulud, OpenEMR campaign coverage). Keep. |
| 2 | thehackernews.com | 22 | 6 | Second-largest producer; consistent fast turnaround on KEV additions and AI-platform stories. Keep. |
| 3 | securityweek.com | 12 | 9 | Best at vendor-roll-ups (SonicWall, OpenEMR coverage, AppSec breach reporting). Keep. |
| 4 | dbugs.ptsecurity.com | 11 | 33 | Strong CVE-feed coverage of EU/Russian advisories often missed by US-centric outlets. Keep. |
| 5 | opencve.io | 7 | 8 | Indispensable for cross-vendor CVE discovery; faster than NVD. Keep. |
| 6 | github.com/search?q=CVE | 4 | 9 | Good for fresh PoCs and disclosure-coordination drift. Keep. |
| 7 | rapid7.com | 3 | 3 | Authoritative ETR (Emergent Threat Response) write-ups; best for cPanel-class headline events. Keep. |
| 8 | github.com/0xMarcio/cve | 3 | 2 | High-signal PoC tracker; surfaced active-exploitation hints repeatedly. Keep. |
| 9 | kb.cert.org/vuls | 2 | 5 | Lower volume but coverage of academic / less-publicised vulnerabilities. Keep. |
| 10 | cisa.gov | 1 | 0 | Authoritative but cisa.gov + KEV catalog return 403 to WebFetch — relay via THN/SecurityWeek. Keep on list as canonical reference even though direct fetch is broken. |

## Dead weight (zero findings April + zero or near-zero in March)

These produced **no findings in April** and were similarly silent in March. Recommendations below — present to user, do not auto-modify SOURCES.md.

| Source | April | March | Issue | Recommendation |
|--------|-------|-------|-------|----------------|
| cve.mitre.org | 0/0 | 0/0 | Redirects to cve.org; JS-only, returns empty via WebFetch | **Drop** — duplicate of cve.org and not fetchable. |
| cve.org | 0/0 | 0/0 | JS-only, empty via WebFetch | **Drop** — opencve.io covers the same upstream feed and is fetchable. |
| googleprojectzero.blogspot.com | 0/0 | 0/2 | Redirects to projectzero.google; very low post frequency | **Keep** — when they post, it matters. Low cost, retain for deep technical bug-class coverage. |
| msrc.microsoft.com/blog | 0/0 | 0/0 | Redirects to www.microsoft.com/.../msrc/blog; navigation-only via WebFetch | **Replace URL with msrc.microsoft.com/update-guide** — the update-guide endpoint provides the actual advisory content. |
| hackerone.com/hacktivity | 0/0 | 0/0 | JS-only, returns empty | **Drop** — disclosure programs surface in BleepingComputer/THN within days anyway. |
| bugcrowd.com/disclosures | 0/0 | 0/0 | Returns 404 since 2026-04-14 | **Drop or fix** — URL appears stale; investigate replacement endpoint. |
| habr.com/ru/companies/tomhunter/articles | 0/0 | 0/0 | Latest is March 6 (February analyses); monthly cadence too slow | **Move to monthly check** — no daily value. |
| teletype.in/@cyberok | 0/0 | 0/0 | Latest is February 2026 | **Drop** — appears abandoned. |
| cert.gov.ua | 0/0 | 0/0 | No content returned via WebFetch | **Drop or fix** — investigate endpoint. |
| blog.cloudflare.com/tag/security | 0/0 | 0/0 | Mostly product announcements, not vuln disclosures | **Keep** — useful for traffic-trend signals (DDoS waves, post-quantum rollout) even if vuln density is low. |
| attackerkb.com | 0/0 | 0/0 | Returns 403 to WebFetch consistently | **Drop or replace** — Rapid7's blog covers most attackerkb-relevant content. |
| packetstormsecurity.com → packetstorm.news | 0/0 | 0/0 | Homepage-only via WebFetch; 313 advisories/week per their stats but not surfaced in fetch | **Investigate** — try `/files/latest/1` URL instead of homepage. |
| nvd.nist.gov | 0/0 | 0/0 | Returns sparse data via WebFetch | **Keep** — authoritative CVE source even if WebFetch is suboptimal; opencve.io covers the practical query case. |
| fortinet.com/blog/threat-research | 0/2 | — | Latest April 17 (Mirai); low cadence | **Keep** — when active, surfaces threat-actor research that's hard to get elsewhere. |
| securitylab.github.com | 0/2 | 1/2 | Latest April 24; low cadence | **Keep** — authoritative on supply-chain / open-source vulns when they post. |

**Summary recommendation:** Drop 5 (cve.mitre.org, cve.org, hackerone.com/hacktivity, teletype.in/@cyberok, attackerkb.com), fix-or-drop 2 (bugcrowd.com/disclosures, cert.gov.ua), URL-update 1 (msrc.microsoft.com/blog → /update-guide), URL-investigate 1 (packetstorm.news), move 1 to monthly (habr.com/ru/companies/tomhunter). Net: SOURCES.md goes from 30 entries to ~22 daily + 1 monthly. Faster runs, less degraded-noise, no signal lost.

## New source candidates discovered during April

These appeared as primary references inside major advisories or were repeatedly cited as the "first" source on a story, but are not currently in SOURCES.md:

| Candidate | Surfaced via | Recommendation |
|-----------|-------------|----------------|
| labs.watchtowr.com | Disclosed cPanel CVE-2026-41940 (the highest-impact bug of April); also frequently first on Citrix / Ivanti / Palo Alto edge-bug deep-dives | **Add to Tier 1** — first-discovery source for management-plane bugs. |
| wiz.io/blog | First-source on Mini Shai-Hulud SAP CAP supply-chain analysis; consistently fast on cloud + supply-chain stories | **Add to Tier 1** — strongest cloud + supply-chain research org of 2026 to date. |
| socket.dev / blog.aikido.dev / safedep.io | First-source on PyPI/npm package compromises (PyTorch Lightning, Mini Shai-Hulud, Bitwarden CLI) | **Add one to Tier 2** — pick whichever has best fetch reliability (Socket has the most coverage volume). |
| snyk.io/blog | First on Qinglong CVE-2026-3965/4047 with-in-the-wild correlation; consistent ecosystem-wide CVE write-ups | **Add to Tier 2** — covers what dbugs.ptsecurity.com covers but in English. |
| stepsecurity.io / blog | Co-discovered Mini Shai-Hulud; specialises in CI/CD supply-chain | **Add to Tier 2** — niche but high-relevance for the AI-agent-config attack surface that emerged this month. |
| onapsis.com/blog | First-source on SAP-specific supply-chain (Mini Shai-Hulud SAP CAP) | **Tier 3 / on-demand** — only matters when SAP is involved; not daily. |
| vulncheck.com/advisories | Co-published the cPanel ETR; consistent advisory-pipeline | **Add to Tier 2** — cleaner advisory format than CVE.org. |
| aisle.com/blog | Published the OpenEMR 38-CVE batch (largest single AI-discovered CVE batch of April); ongoing programme | **Add to Tier 2** — first AI-vuln-finder lab with sustained output; expect monthly drops. |

## Coverage gaps (technologies that appeared in reports but had no dedicated source)

- **Healthcare-vertical advisories** — OpenEMR 38-CVE batch, Sandhills Medical, Medtronic breach all surfaced via general news outlets. Consider adding **HIPAA Journal** + **GovInfoSecurity** for healthcare-specific signal.
- **AI / MCP supply chain** — emerging as a major attack surface (nginx-ui MCP, Mini Shai-Hulud .claude/settings.json, Gemini CLI .gemini/, mcp-atlassian, OpenHarness, FastGPT/Langflow/KubeAI command-injection patterns). No dedicated source. Candidates: **Anthropic security advisories** (claude.com/security or model-card disclosures), **Google AI security bulletins**, **modelcontextprotocol.org/security**, and **mcp.guard.io** if it exists. Worth adding 1–2 dedicated trackers.
- **NPM / PyPI ecosystem-level intelligence** — Socket / Aikido / SafeDep / StepSecurity collectively cover this but none are in SOURCES.md.
- **Russian-language coverage** — habr.com/teletype/cyberok all gone quiet; CyberOK was historically the best Russian-perimeter signal. Consider adding **bi.zone/blog** or **kaspersky.com/blog/securelist** as replacements.
- **Edge-device / firewall vendor bulletins** — SonicWall published an 8-CVE roll-up directly today; we caught it via SecurityWeek + OpenCVE. Consider a watchlist of vendor security pages: **psirt.fortinet.com**, **psirt.paloaltonetworks.com**, **sec.cloudapps.cisco.com/security/center**, **psirt.juniper.net**.

## Score Calibration — April 2026

To be filled in: review whether any item Noted in April later became a 7+ News in May (under-call), or any 7+ Item turned out to have no real defensive urgency (over-call). Empty for now; revisit at end of May.

## Discovery Latency — April 2026 News items at score 7+

Spot-check from April reports of all News items with threat_score >= 7:
- **early**: 0
- **on-time**: ~85% (cPanel, Mini Shai-Hulud, OpenEMR, n8n CVE-2026-21858, BPFDoor, OpenClaw batches)
- **late**: ~15% (Qinglong CVE-2026-3965/4047 — covered 2026-04-30, in-the-wild since 2026-02; was on Snyk before our previous check)

Goal of ≥80% early/on-time for score 7+ entries: **MET** for April. Investigate the Qinglong miss — Snyk wasn't yet in SOURCES.md, hence the late call. Adding snyk.io/blog to Tier 2 (see above) closes that gap.
