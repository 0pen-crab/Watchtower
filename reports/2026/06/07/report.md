# Watchtower Night Report — 2026-06-07
**Cycle:** Night | **Generated:** 2026-06-07 00:30 UTC (2026-06-07T00:30:00Z)
**Sources checked:** 25/30 | **CISA KEV total:** N/A (catalog unreachable) | **New KEV additions:** None confirmed since 2026-06-05 Serv-U / Linux cgroups batch

---

## 🔴 CRITICAL

*No CRITICAL items today.*

---

## 🟠 HIGH

### 🔄 Miasma Supply-Chain Worm Hits 73 Microsoft GitHub Repositories Across Azure / Azure-Samples / Microsoft / MicrosoftDocs Organizations and Targets Claude Code / Gemini CLI / Cursor / VS Code AI Coding Environments
**Product:** Microsoft GitHub organizations (Azure, Azure-Samples, Microsoft, MicrosoftDocs); 73 repositories disabled by GitHub; durabletask PyPI / .NET / Go / Java / JavaScript / MSSQL ecosystem; AI coding environments (Claude Code, Gemini CLI, Cursor, VS Code) | **CVE:** None | **CVSS:** N/A | **Threat score:** 9 (was 8) | **First reported:** 2026-06-02

The Miasma supply-chain worm — first surfaced 2026-06-02 (7 @redhat-cloud-services npm packages) and expanded to 32 npm packages / 96 versions / ~10M downloads on 2026-06-03 — escalated again on 2026-06-06 with confirmed compromise of 73 repositories across four official Microsoft GitHub organizations (Azure, Azure-Samples, Microsoft, MicrosoftDocs). The operator used legitimate maintainer credentials and pushed malicious updates through normal release channels, which the worm propagates further by injecting a 4.3 MB payload that auto-executes inside Claude Code, Gemini CLI, Cursor, and VS Code AI coding environments. Researcher Paul McCarty (Ox Security) reports that this is a re-compromise of the durabletask PyPI ecosystem first hit by TeamPCP in May 2026, with credentials "plausibly never fully lost" — suggesting persistent attacker access never revoked. Stolen credentials were published in attacker-controlled GitHub repos labeled "Miasma: The Spreading Blight" and "Hades — The End for the Damned." GitHub disabled the affected Microsoft repositories with TOS-violation notices.

**Timeline:**
- 2026-06-02 — JFrog / GitGuardian: 7 @redhat-cloud-services npm packages trojanized via compromised Red Hat employee GitHub account (Watchtower 2026-06-02 NEWS, score 8)
- 2026-06-03 — SecurityWeek / Ox: scope expansion to 32 npm packages, 96 versions in 72-second automated burst, ~10M cumulative downloads, 210 downstream-credential-leak repos (Watchtower 2026-06-03 UPDATE, score 8)
- 2026-06-06 — THN: 73 official Microsoft GitHub repos compromised across Azure / Azure-Samples / Microsoft / MicrosoftDocs; AI-coding-env payload-injection vector confirmed; entire Durable Task ecosystem (.NET, Go, Java, JS, MSSQL) taken offline simultaneously

**Why it matters:** Miasma now spans the npm registry (10M downloads), Red Hat trusted-publisher namespace, the durabletask PyPI ecosystem, and four official Microsoft GitHub orgs — and adds AI coding agents as a new propagation vector. Any developer or CI pipeline that pulled an Azure SDK sample, MicrosoftDocs example, or durabletask package in the past 30 days needs credential audit and rebuild-from-clean. The pattern of "credentials plausibly never lost" across the May TeamPCP and June Miasma waves indicates an attacker who continues to round-trip compromised maintainer access through multiple campaigns — credential rotation must be assumed insufficient without account re-creation.

**Mitigation:**
- Audit any dependency on @redhat-cloud-services npm packages, Azure / Azure-Samples / Microsoft / MicrosoftDocs repo content, or durabletask PyPI / .NET / Go / Java / JS / MSSQL packages installed since 2026-05-01; rebuild from known-clean upstream
- Treat any Claude Code / Gemini CLI / Cursor / VS Code workspace that loaded a Miasma-tagged package as compromised; revoke and re-issue developer tokens, npm publish tokens, GitHub PATs, and AWS / Azure / GCP credentials
- Egress-block the published Miasma C2 domains and inspect for the 4.3 MB AI-coding-env payload signature
- Require re-creation (not rotation) of any maintainer account believed to have been compromised in the May 2026 TeamPCP wave

**Discovered by:** Ox Security (Paul McCarty); JFrog; GitGuardian

**Sources:** [Miasma Worm Hits 73 Microsoft GitHub Repositories — THN](https://thehackernews.com/2026/06/miasma-worm-hits-73-microsoft-github.html)

---

### depthfirst AI Agent Discloses 21 Zero-Days in FFmpeg — CVE-2026-39210 → CVE-2026-39218 Plus Unnumbered Companions, Heap / Stack Overflows in Parsers and Demuxers (TS Demuxer, VP9 Decoder, etc.); Patched Upstream
**Product:** FFmpeg ~1.5M LOC C codebase; widely bundled in media pipelines, Python wheels, container images, hardware appliances; affects parsers and demuxers across TS, VP9, and other formats; 9 CVEs assigned (CVE-2026-39210 through CVE-2026-39218), additional bugs fixed but not yet numbered | **CVE:** CVE-2026-39210, CVE-2026-39211, CVE-2026-39212, CVE-2026-39213, CVE-2026-39214, CVE-2026-39215, CVE-2026-39216, CVE-2026-39217, CVE-2026-39218 | **CVSS:** Not yet published | **Threat score:** 5 | **First reported:** 2026-06-06

depthfirst's autonomous security agent identified 21 confirmed zero-day vulnerabilities in FFmpeg's ~1.5M-line C codebase for ~$1,000 in compute, with 9 CVE-2026-3921X assignments and the remaining bugs patched but un-numbered. The flaws are primarily heap or stack overflows in parsers and demuxers spanning the TS demuxer through the VP9 decoder; several were latent 15-20 years (one introduced in 2003). All bugs are now patched upstream and the researcher published per-bug PoC inputs on GitHub. No active in-the-wild exploitation is described, but the deployment footprint — FFmpeg ships inside countless media-processing pipelines, Python wheels, container images, video-platform back ends, transcoder appliances, and CDN edge nodes — means defenders should pull the patched upstream build or distribution security update before triage attention shifts to the public PoCs.

**Why it matters:** FFmpeg parsers run in nearly every server-side transcoder, podcast pipeline, security-camera NVR appliance, video-conferencing backend, container thumbnailer, and CDN ingest node. A pre-auth memory-corruption primitive in a TS or VP9 demuxer reachable via uploaded media is a plausible RCE vector against media-handling services. PoC inputs are public; expect security scanners and fuzz follow-ups to surface additional bugs in the same code paths within days.

**Mitigation:**
- Inventory FFmpeg footprint across media pipelines, transcoders, NVRs, video-conferencing servers, container thumbnailers, and CDN ingest layers
- Upgrade to the patched FFmpeg builds (pull upstream master or distribution security update covering CVE-2026-39210 → CVE-2026-39218)
- For services that accept user-uploaded media, place transcoding behind a sandbox / network-isolated namespace until patched
- Monitor for novel PoC follow-on releases; depthfirst published per-bug PoC inputs on GitHub

**Sources:** [AI Agent Uncovers 21 Zero-Days in FFmpeg — THN](https://thehackernews.com/2026/06/ai-agent-uncovers-21-zero-days-in.html)

---

## 🟡 MEDIUM

### Bright Data Residential-Proxy SDK in Free Smart TV and Mobile Apps — 400M Residential IPs Repurposed for AI-Scraper Anti-Bot Bypass, Bypasses iOS VPN, "Weaker Than Most Malware" Per Researcher
**Product:** Bright Data (formerly Luminati) residential-proxy SDK; embedded in free smart-TV apps (PlayWorks Digital, CloudTV, Longvision) plus iOS and Android consumer apps; carrier traffic routed via proxyjs.brdtnet.com / proxyjs.luminatinet.com / proxyjs.bright-sdk.com / clientsdk.bright-sdk.com / clientsdk.brdtnet.com | **CVE:** None | **Published:** 2026-06-06

Include Security and independent researcher Buchodi reverse-engineered Bright Data's iOS SDK and disclosed that free smart-TV and mobile apps embedding the SDK silently convert consumer devices into residential exit nodes for the world's largest commercial proxy network (~400M residential IPs, 200 GB/month per device with higher caps in Uzbekistan / Oman / select markets). The peer channel carrying scraping jobs has "none of the usual security checks" and operates "weaker than the controls built into most malware." Traffic explicitly bypasses configured iOS VPN profiles. The vector matters defensively because AI scrapers and credential-stuffing operators routinely buy Bright Data residential bandwidth to evade Cloudflare / DataDome anti-bot defenses — and corporate networks now host smart TVs (conference rooms, lobbies, executive offices) and BYOD iOS devices that may be unknowingly running the SDK.

**Mitigation:**
- Egress-block the published Bright Data domains: `proxyjs.brdtnet.com`, `proxyjs.luminatinet.com`, `proxyjs.bright-sdk.com`, `clientsdk.bright-sdk.com`, `clientsdk.brdtnet.com`
- Audit conference-room / lobby / executive smart-TV installs against the partner list (PlayWorks Digital, CloudTV, Longvision et al.) and remove unknown free apps
- Treat smart TVs as untrusted devices on a quarantined VLAN; never give them corporate-credential or directory access
- For anti-bot teams: residential-IP detection must shift from heuristic ASN scoring toward per-session behavioral signals given the volume of residential exits now available

**Sources:** [Free Apps Are Quietly Turning Smart TVs Into Web-Scraping Proxies for AI — THN](https://thehackernews.com/2026/06/free-apps-are-quietly-turning-smart-tvs.html)

---

## 📋 Noted / Monitoring

**OpenAI ChatGPT "Lockdown Mode" defensive feature launch (THN 2026-06-06)** — Optional advanced setting disables live browsing, image retrieval, deep research, agent mode, canvas networking, and file downloads to reduce prompt-injection / data-exfiltration blast radius. OpenAI acknowledges residual risk via enabled Apps and "unforeseen combinations of capabilities." Defensive AI-platform hardening calibration data point — recommend enabling for sensitive-data analyst workflows.

**Project Zero discloses 4 bugs in FreeType (oss-security 2026-06-06)** — Google's security team published four FreeType font-rendering library vulnerabilities. Client-side / font-rendering scope reachable via document and PDF handlers; flag for endpoint-fleet patch cadence and PDF-processing-server fleets bundling FreeType.

**CVE-2026-10725 — Perl Protocol::HTTP2 ≤ 1.12 HTTP/2 Bomb (oss-security 2026-06-06)** — The HPACK-amplification + flow-control-stalling HTTP/2 Bomb pattern (Watchtower 2026-06-04 HIGH covering Apache CVE-2026-49975 / NGINX / IIS / Envoy / Pingora) now confirmed in Perl's Protocol::HTTP2 implementation. Limited Perl-HTTP/2 production deployment, but mod_perl + Mojolicious shops should patch.

**CVE-2026-50589 — OpenStack Ironic DoS under reduced process stack size (OSSN-0099, oss-security 2026-06-06)** — OpenStack Ironic DoS triggered under constrained stack conditions; limited deployment footprint to OpenStack-Ironic-running private clouds.

**CVE-2026-10879 — Perl DBI < 1.648 heap overflow (oss-security 2026-06-06)** — Perl database-interface library memory overflow on SQL statement parsing. Legacy Perl scope, calibration only.

**CVE-2026-9270 + CVE-2026-11362 — Perl DataDog::DogStatsd ≤ 0.07 metric injection (oss-security 2026-06-06)** — Metric-injection issues in the DataDog statistics Perl library covering both base parsing and event-tag handling. Observability-stack pollution risk, low blast radius.

**SOC-CMM 2026 report — only ~10% of SOCs say AI delivers excellent value (THN 2026-06-06)** — Industry-survey calibration data point on enterprise AI security-tooling adoption; not an advisory.

**Day-2 amplification — SolarWinds Serv-U CVE-2026-28318 (Watchtower 2026-06-06 NEWS)** — THN 2026-06-06 republishes the 2026-06-05 KEV addition with patched-version (15.5.4 HF1) and Content-Encoding: deflate POST mitigation details already in yesterday's NEWS entry; no new info, no update warranted.

**libinput device-group udev-properties injection follow-up (oss-security 2026-06-06)** — Continued discussion of the previously disclosed libinput flaw; no new CVE, calibration / fix-tracking only.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com, schneier.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (403 — unreachable) |
| Vendor advisories | rapid7.com, fortinet.com/blog/threat-research, securitylab.github.com, msrc.microsoft.com/blog, blog.cloudflare.com/tag/security | ✅ / ⚠️ |
| Research / OSINT | openwall.com/lists/oss-security, projectzero.google, github.com/search?q=CVE, github.com/0xMarcio/cve, avleonov.com, dbugs.ptsecurity.com | ✅ |
| Supply chain | seclists.org/fulldisclosure, packetstormsecurity.com, opencve.io, app.opencve.io | ⚠️ (degraded — homepage / marketing content only) |
| Threat intel | hackerone.com/hacktivity, bugcrowd.com/disclosures, nvd.nist.gov, cve.mitre.org, cve.org, kb.cert.org/vuls, habr.com/ru/companies/tomhunter, teletype.in/@cyberok, cert.gov.ua, attackerkb.com | ⚠️ / ❌ |

**Errors:**
- ❌ cisa.gov — 403 Forbidden
- ❌ cisa.gov/known-exploited-vulnerabilities-catalog — 403 Forbidden
- ❌ attackerkb.com — 403 Forbidden
- ❌ bugcrowd.com/disclosures — 404 Not Found
- ❌ cve.mitre.org — historically unreachable, not retried

**Degraded (returned but content stale / no recent posts / homepage only):** seclists.org/fulldisclosure, packetstormsecurity.com, opencve.io, nvd.nist.gov, cve.org, msrc.microsoft.com/blog, hackerone.com/hacktivity, habr.com/ru/companies/tomhunter, teletype.in/@cyberok, cert.gov.ua, blog.cloudflare.com/tag/security, kb.cert.org/vuls, dbugs.ptsecurity.com

**CISA KEV:** Catalog page unreachable (403); no new KEV additions confirmed since 2026-06-05 SolarWinds Serv-U CVE-2026-28318 / Linux cgroups CVE-2022-0492 / Android CVE-2025-48595 batch.

---

*Watchtower vulnerability-researcher | Cycle: 2026-06-07/night | Next: 2026-06-08/night*
