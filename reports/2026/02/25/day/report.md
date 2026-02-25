# Vulnerability Report — 2026-02-25 (Day Cycle)

## 📰 Frigate NVR ≤0.16.3 Blind RCE via go2rtc Exec Injection

**Threat Score:** 7
**Affected Technology:** Frigate NVR (≤0.16.3)
**CVE:** CVE-2026-25643
**CVSS:** Not yet scored (estimated Critical)

### Summary
Frigate NVR versions up to 0.16.3 are vulnerable to blind remote code execution through go2rtc exec injection. An attacker can inject a malicious go2rtc stream and a fake camera entry into the Frigate configuration, triggering arbitrary command execution as the Frigate process during service restart. Both authenticated and unauthenticated attack paths exist depending on deployment configuration. A full Python exploit PoC has been published on GitHub by joshuavanderpoll.

### Why It Matters
Frigate NVR is widely deployed in home automation and small business CCTV setups, often exposed to the internet. The availability of a weaponized PoC and both auth/unauth attack paths makes this immediately actionable.

### Discovery
**First seen at:** github.com (joshuavanderpoll/CVE-2026-25643)
**How found:** Found via GitHub CVE-2026 repository search and cross-referenced with 0xMarcio/cve trending PoC tracker.

### Sources
- https://github.com/joshuavanderpoll/CVE-2026-25643
- https://github.com/0xMarcio/cve

---

## 📰 Lanscope Endpoint Manager Path Traversal — Unauthenticated RCE

**Threat Score:** 7
**Affected Technology:** Lanscope Endpoint Manager (On-Premises) (≤9.4.7.3)
**CVE:** CVE-2026-25785
**CVSS:** 9.8 (CVSS v3.1) / 9.3 (CVSS v4.0)

### Summary
MOTEX Inc.'s Lanscope Endpoint Manager (On-Premises) Sub-Manager Server version 9.4.7.3 and earlier contains a path traversal vulnerability (CWE-22) that allows unauthenticated remote attackers to tamper with arbitrary files on the Windows system, potentially leading to arbitrary code execution. CVSS v3.1 scores this at 9.8 (Critical) with network attack vector, no privileges required, and no user interaction needed. A patch is available. Cloud version is not affected.

### Why It Matters
Endpoint management platforms are high-value targets as they control large fleets of devices. The CVSS 9.8 unauthenticated network-accessible attack vector makes this critical for organizations running the on-premises version.

### Discovery
**First seen at:** jvn.jp (JVN#79096585)
**How found:** JVN (Japan Vulnerability Notes) advisory published 2026-02-25, discovered during routine CERT source scan.

### Sources
- https://jvn.jp/en/jp/JVN79096585/index.html

---

## 📰 Langflow Remote Code Execution

**Threat Score:** 6
**Affected Technology:** Langflow (AI workflow platform)
**CVE:** CVE-2026-0770
**CVSS:** Not yet scored

### Summary
Langflow, an open-source AI workflow automation platform, contains a remote code execution vulnerability. A PoC exploit has been published on GitHub. Langflow is commonly deployed as an internet-facing service for building and deploying AI agents and workflows. The vulnerability allows an attacker to execute arbitrary code on the server. Detailed technical analysis is pending.

### Why It Matters
AI workflow platforms like Langflow are increasingly deployed internet-facing and represent a growing attack surface in the AI/LLM infrastructure space — directly in our scope.

### Discovery
**First seen at:** github.com (0xgh057r3c0n/CVE-2026-0770)
**How found:** Found via GitHub CVE-2026 repository search during systematic source scanning.

### Sources
- https://github.com/0xgh057r3c0n/CVE-2026-0770

---

## 📰 OpenEMR 7.0.4 SQL Injection

**Threat Score:** 5
**Affected Technology:** OpenEMR 7.0.4
**CVE:** CVE-2026-25746
**CVSS:** Not yet scored

### Summary
A SQL injection vulnerability has been discovered in OpenEMR version 7.0.4, a widely deployed open-source electronic health records system. A PoC has been published on GitHub. OpenEMR instances are frequently internet-facing for patient portal access. SQL injection in a healthcare records system can lead to data exfiltration of protected health information and potentially further exploitation.

### Why It Matters
OpenEMR is one of the most widely deployed open-source healthcare platforms with internet-facing portals, making SQL injection a direct risk to patient data confidentiality.

### Discovery
**First seen at:** github.com (ChrisSub08/CVE-2026-25746)
**How found:** Found via GitHub CVE-2026 repository search during systematic scanning.

### Sources
- https://github.com/ChrisSub08/CVE-2026-25746_SqlInjectionVulnerabilityOpenEMR7.0.4

---

## 📰 GitLab 18.9.1 Security Patch Release

**Threat Score:** 5
**Affected Technology:** GitLab CE/EE (all versions before 18.9.1)
**CVE:** Multiple (pending full advisory)
**CVSS:** Not yet published

### Summary
GitLab released version 18.9.1 on February 25, 2026, as a security patch release addressing multiple vulnerabilities including XSS and DoS issues. GitLab strongly recommends immediate upgrade for all self-managed installations. Full CVE details and severity scores are expected in the forthcoming advisory. GitLab is a critical developer infrastructure component commonly exposed to the internet.

### Why It Matters
GitLab self-managed instances are among the most commonly internet-exposed enterprise applications and are frequently targeted. Security patch releases should be applied immediately.

### Discovery
**First seen at:** about.gitlab.com (releases page)
**How found:** Discovered during routine vendor advisory monitoring.

### Sources
- https://about.gitlab.com/releases/2026/02/25/patch-release-gitlab-18-9-1-released/

---

## 🔄 Update: n8n Ni8mare Unauthenticated RCE Chain

**Previous Threat Score:** 8 → **Updated Threat Score:** 9
**CVE:** CVE-2026-21858

### What Changed
The n8n Ni8mare exploit (CVE-2026-21858 + CVE-2025-68613) has gained significant traction with 222 GitHub stars and LeakIX now tracking exposed vulnerable instances. The exploit was AI-automated from patch diff to full weaponized PoC in ~9 hours post-disclosure. Multiple forks and clones are appearing, indicating widespread adoption by scanners. Organizations running n8n should treat this as an emergency if not already patched to 1.121.0+.

### Sources
- https://github.com/Chocapikk/CVE-2026-21858
- https://github.com/0xMarcio/cve

---

## 📋 Noted

- **CVE-2026-3118** — Red Hat Developer Hub (Backstage): DoS via GraphQL injection, authenticated user can crash platform. Medium severity (6.5).
- **CVE-2026-26104** — udisks (Linux): Unprivileged users can export LUKS headers without authorization. Local only, no remote vector.
- **CVE-2026-21962** — Unknown product: New PoC on GitHub (Ashwesker), details pending investigation.
- **Multiple CVEs** — Firefox 148 (MFSA 2026-13): Multiple high-severity security fixes released Feb 24. Browser-only, out of primary scope unless chained in campaign.
- **CVE-2026-0229** — PAN-OS: DoS in Advanced DNS Security feature. Requires specific config, patched in 12.1.4+ and 11.2.10+.
- **PAN-SA-2026-0002** — Prisma Browser: Chromium monthly vulnerability update (Feb 2026). Routine update.
- **N/A** — Lazarus/DPRK + Medusa Ransomware: Symantec confirms North Korean Lazarus group using Medusa RaaS targeting healthcare. Already reported in evening 02/24 cycle; no new technical details.

---

## Source Coverage

| # | Source | Status | Findings |
|---|--------|--------|----------|
| 1 | nvd.nist.gov | ✅ Checked | No new in-scope |
| 2 | cve.mitre.org / cve.org | ✅ Checked | Redirects to cve.org, minimal content |
| 3 | vuldb.com | ⚠️ Degraded | Login required for RSS |
| 4 | osv.dev | ✅ Checked | MinimOS/ztunnel entries, low relevance |
| 5 | exploit-db.com | ✅ Checked | No new in-scope |
| 6 | cnvd.org.cn | ❌ Unreachable | JS challenge blocked |
| 7 | euvd.enisa.europa.eu | ✅ Checked | JS-rendered, minimal content |
| 8 | packetstormsecurity.com | ✅ Checked | Domain redirected, checked alternate |
| 9 | cisa.gov (KEV) | ✅ Checked | No new additions today |
| 10 | cisa.gov (advisories) | ✅ Checked | No new advisories today |
| 11 | vulndb.cyberriskanalytics.com | ⚠️ Degraded | Requires subscription |
| 12 | googleprojectzero.blogspot.com | ✅ Checked | No new posts |
| 13 | securitylab.github.com | ✅ Checked | No new posts |
| 14 | blog.cloudflare.com/tag/security | ✅ Checked | No new vulnerability posts |
| 15 | msrc.microsoft.com/blog | ✅ Checked | No new advisories |
| 16 | blog.talosintelligence.com | ✅ Checked | No new vulnerability posts |
| 17 | unit42.paloaltonetworks.com | ✅ Checked | No new vulnerability posts |
| 18 | aws.amazon.com/blogs/security | ✅ Checked | FortiGate post (already covered) |
| 19 | confluence.atlassian.com/security | ✅ Checked | No new advisories |
| 20 | securityblog.redhat.com | ✅ Checked | No new vulnerability posts |
| 21 | hackerone.com/blog | ✅ Checked | No new vulnerability disclosures |
| 22 | security.googleblog.com | ✅ Checked | No new posts |
| 23 | acunetix.com/blog | ✅ Checked | Educational content only |
| 24 | blog.qualys.com | ✅ Checked | No new vulnerability posts |
| 25 | welivesecurity.com | ✅ Checked | No new vulnerability posts |
| 26 | symantec-enterprise-blogs.security.com | ✅ Checked | Lazarus/Medusa (already covered) |
| 27 | fortinet.com/blog/threat-research | ✅ Checked | No new posts |
| 28 | x.com/maddiestone | ❌ Unreachable | X/Twitter inaccessible via web_fetch |
| 29 | x.com/cyb3rops | ❌ Unreachable | X/Twitter inaccessible |
| 30 | x.com/likethecoins | ❌ Unreachable | X/Twitter inaccessible |
| 31 | x.com/craiu | ❌ Unreachable | X/Twitter inaccessible |
| 32 | x.com/ProjectZeroIO | ❌ Unreachable | X/Twitter inaccessible |
| 33 | x.com/GossiTheDog | ❌ Unreachable | X/Twitter inaccessible |
| 34 | x.com/hackerfantastic | ❌ Unreachable | X/Twitter inaccessible |
| 35 | x.com/thegrugq | ❌ Unreachable | X/Twitter inaccessible |
| 36 | x.com/vxunderground | ❌ Unreachable | X/Twitter inaccessible |
| 37 | x.com/campuscodi | ❌ Unreachable | X/Twitter inaccessible |
| 38 | x.com/BleepinComputer | ❌ Unreachable | X/Twitter inaccessible |
| 39 | x.com/0xdea | ❌ Unreachable | X/Twitter inaccessible |
| 40 | x.com/Shadow0pz | ❌ Unreachable | X/Twitter inaccessible |
| 41 | x.com/MalwareTechBlog | ❌ Unreachable | X/Twitter inaccessible |
| 42 | x.com/RedTeamVillage_ | ❌ Unreachable | X/Twitter inaccessible |
| 43 | reddit.com/r/netsec | ⚠️ Degraded | JS-rendered, limited content |
| 44 | reddit.com/r/blueteamsec | ⚠️ Degraded | JS-rendered, limited content |
| 45 | reddit.com/r/cybersecurity | ⚠️ Degraded | JS-rendered, limited content |
| 46 | reddit.com/r/ReverseEngineering | ⚠️ Degraded | Not checked (same JS issue) |
| 47 | reddit.com/r/bugbounty | ⚠️ Degraded | Not checked (same JS issue) |
| 48 | owasp.org/slack | ⚠️ Degraded | Requires Slack auth |
| 49 | t.me/bugbountyradar | ⚠️ Degraded | Requires Telegram auth |
| 50 | discord.gg/infosecprep | ⚠️ Degraded | Requires Discord auth |
| 51 | t.me/redteamsec | ⚠️ Degraded | Requires Telegram auth |
| 52 | 0day.today | ✅ Checked | Domain hijacked/spam |
| 53 | hackerone.com/hacktivity | ✅ Checked | JS-rendered, no content |
| 54 | bugcrowd.com/disclosures | ✅ Checked | Blog content only |
| 55 | github.com/search?q=CVE | ✅ Checked | Multiple findings |
| 56 | thehackernews.com | ✅ Checked | No new in-scope vulns |
| 57 | bleepingcomputer.com | ✅ Checked | No new in-scope vulns today |
| 58 | krebsonsecurity.com | ✅ Checked | No new vulnerability posts |
| 59 | threatpost.com | ❌ Unreachable | Domain defunct |
| 60 | securityweek.com | ✅ Checked | VMware Aria Ops (checked, no CVE yet) |
| 61 | darkreading.com | ✅ Checked | No new in-scope vulns |
| 62 | helpnetsecurity.com | ✅ Checked | No new in-scope vulns |
| 63 | schneier.com | ✅ Checked | Commentary only |
| 64 | grahamcluley.com | ✅ Checked | No new vulnerability posts |
| 65 | tldrsec.com | ✅ Checked | Newsletter format, no new vulns |
| 66 | sans.org/newsletters/newsbites | ✅ Checked | No accessible content |
| 67 | risky.biz | ✅ Checked | No new vulnerability posts |
| 68 | cybersecuritydispatch.com | ⚠️ Degraded | Not separately checked |
| 69 | seclists.org/fulldisclosure | ✅ Checked | NesterSoft WorkTime vulns (low interest) |
| 70 | cert.europa.eu | ✅ Checked | No new advisories today |
| 71 | cert.gov.ua | ✅ Checked | Minimal content rendered |
| 72 | crowdstrike.com | ✅ Checked | No new vulnerability posts |
| 73 | rapid7.com | ✅ Checked | Grandstream analysis (already covered) |
| 74 | securitylabs.datadoghq.com | ✅ Checked | No new vulnerability posts |
| 75 | strobes.co | ✅ Checked | OpenClaw exposure article (already covered) |
| 76 | securityscorecard.com | ✅ Checked | OpenClaw risk articles (already covered) |
| 77 | cvedetails.com | ❌ Unreachable | Cloudflare blocked |
| 78 | avleonov.com | ✅ Checked | Feb Linux Patch Wednesday (findings integrated) |
| 79 | dbugs.ptsecurity.com | ✅ Checked | No accessible vuln data |
| 80 | habr.com/tomhunter | ✅ Checked | Russian-language recap, no new vulns |
| 81 | teletype.in/@cyberok | ⚠️ Degraded | Not separately checked |
| 82 | github.com/0xMarcio/cve | ✅ Checked | Multiple findings (Frigate, n8n, osTicket, etc.) |
| 83 | attack.mitre.org | ✅ Checked | No new updates (v18 current) |
| 84 | kb.cert.org/vuls | ✅ Checked | No new advisories |
| 85 | vulners.com | ✅ Checked | JS-rendered, limited content |
| 86 | securityfocus.com | ❌ Unreachable | Domain defunct |
| 87 | opencve.io | ✅ Checked | CVE-2026-3118, CVE-2026-26104 found |
| 88 | attackerkb.com | ✅ Checked | No new content rendered |
| 89 | GitHub Advisory Database | ✅ Checked | Multiple advisories, cross-referenced |
| 90 | Vendor advisories (PAN, Cisco, etc.) | ✅ Checked | PAN-OS advisories noted |
| 91 | labs.watchtowr.com | ✅ Checked | Supply chain research, no new vulns |
| 92 | blog.assetnote.io | ✅ Checked | No new vulnerability posts |
| 93 | jvn.jp | ✅ Checked | CVE-2026-25785 Lanscope finding |
| 94 | ubuntu.com/security/notices | ✅ Checked | Routine kernel/package updates |
| 95 | openwall.com/oss-security | ✅ Checked | No new in-scope advisories |
| 96 | github.com/advisories (critical) | ✅ Checked | Multiple reviewed advisories |
| 97 | mozilla.org/security/advisories | ✅ Checked | Firefox 148 / MFSA 2026-13 (noted) |
| 98 | chromereleases.googleblog.com | ✅ Checked | Chrome stable update Feb 23 (routine) |
| 99 | jenkins.io/security/advisories | ✅ Checked | No new advisories |
| 100 | about.gitlab.com/releases | ✅ Checked | GitLab 18.9.1 finding |
| 101 | openssh.com/security | ✅ Checked | No new advisories |
| 102 | security.paloaltonetworks.com | ✅ Checked | PAN-OS advisories noted |
| 103 | auscert.org.au/bulletins | ✅ Checked | VMware, kernel, PostgreSQL bulletins |
| 104 | synology.com/security/advisory | ✅ Checked | No new advisories |
| 105 | sonicwall.com | ❌ Unreachable | No content rendered |
| 106 | ivanti.com/blog/security-advisory | ✅ Checked | No new advisories |
| 107 | projectdiscovery.io/blog | ✅ Checked | AppSec report, no vulns |
| 108 | blog.aquasec.com | ✅ Checked | No new vulnerability posts |
| 109 | nuclei-templates (GitHub) | ✅ Checked | No readable commit content |
| 110 | zerodayinitiative.com/blog | ✅ Checked | Windows Notepad CVE-2026-20841 (out of scope - desktop only) |
| 111 | securelist.com | ✅ Checked | No new vulnerability posts |
| 112 | blog.sonatype.com | ✅ Checked | No new vulnerability posts |
| 113 | sentinelone.com/labs | ✅ Checked | No new vulnerability posts |
| 114 | trendmicro.com/research | ✅ Checked | No new vulnerability posts |
| 115 | checkpoint.com/research | ✅ Checked | No new vulnerability posts |
| 116 | mandiant.com/blog | ✅ Checked | No new vulnerability posts |
| 117 | recordedfuture.com/blog | ✅ Checked | No new vulnerability posts |
| 118 | tenable.com/blog | ✅ Checked | No new vulnerability posts |
| 119 | broadcom.com/security-advisory | ✅ Checked | No content rendered |
| 120 | jpcert.or.jp | ✅ Checked | No new alerts for Feb |
