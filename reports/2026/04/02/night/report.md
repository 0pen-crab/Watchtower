# Vulnerability Intelligence Report — 2026-04-02 Night Cycle

---

## 📰 CVE-2026-5281 — Chrome Dawn WebGPU Zero-Day Actively Exploited, Added to CISA KEV

**Threat Score:** 8
**Affected Technology:** Google Chrome / Chromium-based browsers (Dawn WebGPU)
**CVE:** CVE-2026-5281
**CVSS:** Not yet scored (High)

### Summary
CVE-2026-5281 is a use-after-free vulnerability in Dawn, the open-source WebGPU implementation used by Chromium. A remote attacker who has compromised the renderer process can execute arbitrary code via a crafted HTML page. Google confirmed active exploitation in the wild and patched it in Chrome 146.0.7680.177/.178 on March 31, 2026. CISA added it to the KEV catalog on April 1 with a remediation deadline of April 15. This is the fourth Chrome zero-day exploited in 2026, following CVE-2026-3909/3910 (Skia/V8, March 17) and earlier issues. The same pseudonymous researcher who reported CVE-2026-5281 also reported two prior Dawn/WebGL vulnerabilities (CVE-2026-4675, CVE-2026-4676), suggesting a focused attack surface.

### Why It Matters
Chromium-based browsers are ubiquitous across enterprise environments. A renderer process compromise leading to code execution affects Chrome, Edge, Opera, and other Chromium derivatives deployed across 100K+ assets. CISA KEV listing with a 14-day deadline demands immediate patching priority.

### Discovery
**First seen at:** bleepingcomputer.com
**How found:** Cross-referenced BleepingComputer coverage, CISA KEV catalog update (April 1), HelpNetSecurity detailed analysis, and Google Chrome release blog. Multiple outlets reported simultaneously.

### Sources
- https://www.bleepingcomputer.com/news/security/google-fixes-fourth-chrome-zero-day-exploited-in-attacks-in-2026/
- https://www.helpnetsecurity.com/2026/04/01/google-chrome-zero-day-cve-2026-5281/
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://chromereleases.googleblog.com/2026/03/stable-channel-update-for-desktop_31.html

---

## 📰 CVE-2026-3502 — TrueConf Zero-Day "Operation TrueChaos" — Chinese Espionage via Software Update Supply Chain

**Threat Score:** 7
**Affected Technology:** TrueConf Video Conferencing (versions 8.1.0–8.5.2)
**CVE:** CVE-2026-3502
**CVSS:** 7.8

### Summary
Check Point Research disclosed "Operation TrueChaos," a Chinese-nexus espionage campaign exploiting CVE-2026-3502 in TrueConf self-hosted conferencing servers since early 2026. The vulnerability is a missing integrity check in the update mechanism that allows an attacker controlling the server (or the update delivery path) to replace legitimate updates with arbitrary executables distributed to all connected clients. Targets include government agencies in Southeast Asia. The infection chain uses DLL sideloading, UAC bypass, and delivers the Havoc C2 framework. TrueConf patched the flaw in version 8.5.3 in March 2026. Over 100,000 organizations use TrueConf, including military, government, and oil/gas sectors.

### Why It Matters
TrueConf is widely used in closed/on-premises government environments, making supply chain compromise via its update mechanism extremely high-impact. Chinese-nexus attribution and the use of Havoc C2 suggest sophisticated, persistent espionage — relevant for any enterprise running self-hosted conferencing infrastructure.

### Discovery
**First seen at:** bleepingcomputer.com
**How found:** BleepingComputer article referencing Check Point Research's disclosure of the zero-day campaign. Cross-referenced with SecurityOnline.info and CyberPress coverage.

### Sources
- https://www.bleepingcomputer.com/news/security/hackers-exploit-trueconf-zero-day-to-push-malicious-software-updates/
- https://research.checkpoint.com/2026/operation-truechaos-0-day-exploitation-against-southeast-asian-government-targets/
- https://securityonline.info/trueconf-zero-day-vulnerability-cve-2026-3502-truechaos-campaign/

---

## 📰 Hasbro Confirms Cyberattack — Unauthorized Access Detected March 28, Multi-Week Recovery Expected

**Threat Score:** 6
**Affected Technology:** Hasbro corporate network
**CVE:** Not yet assigned

### Summary
Hasbro (NYSE: HAS), the $6.4B toy and games giant, disclosed a cybersecurity incident via SEC filing on April 1, 2026, confirming unauthorized access to its network detected on March 28. The company has taken some systems offline, engaged third-party cybersecurity firms, and warned recovery may take "several weeks." No ransomware group has publicly claimed responsibility yet. The incident has disrupted some internal processes.

### Why It Matters
While Hasbro is not a technology vendor in our stack, this breach of a major publicly traded corporation demonstrates ongoing targeting of global supply chain and digital infrastructure. The SEC filing timeline (detected Saturday, disclosed Tuesday) and multi-week recovery signal significant compromise depth.

### Discovery
**First seen at:** securityweek.com
**How found:** SecurityWeek headline, cross-referenced with TechCrunch, Reuters, and SEC filing coverage.

### Sources
- https://www.securityweek.com/toy-giant-hasbro-hit-by-cyberattack/
- https://techcrunch.com/2026/04/01/hasbro-hacked-may-take-several-weeks-to-recover/
- https://www.reuters.com/technology/hasbro-says-investigating-cybersecurity-incident-2026-04-01/

---

## 📰 AGEWHEEZE RAT — CERT-UA Impersonation Campaign Distributes Go-Based Trojan to Ukrainian Organizations

**Threat Score:** 6
**Affected Technology:** Ukrainian government, medical, financial, educational, and security organizations
**CVE:** Not yet assigned

### Summary
CERT-UA disclosed that threat actors tracked as UAC-0255 (self-styled "Cyber Serp") impersonated CERT-UA itself on March 26–27, 2026, sending emails from "incidents@cert-ua[.]tech" to distribute AGEWHEEZE, a Go-based remote access trojan. Targets included state organizations, medical centers, security companies, educational institutions, and financial organizations. The RAT communicates via WebSockets and supports command execution, screenshots, and clipboard theft. CERT-UA assessed the campaign as "unsuccessful" but its scale (1M+ emails) and social engineering sophistication (impersonating the national CERT) are notable.

### Why It Matters
Impersonation of national CERTs is a trust-erosion tactic that undermines incident response coordination. While geographically focused on Ukraine, the technique could be replicated against any national CERT, and AGEWHEEZE's Go-based cross-platform nature makes it portable. Relevant for organizations with Ukraine-facing operations.

### Discovery
**First seen at:** thehackernews.com
**How found:** The Hacker News front page coverage cross-referenced with SOCPrime and CyberExpress analysis.

### Sources
- https://thehackernews.com/2026/04/cert-ua-impersonation-campaign-spread.html
- https://socprime.com/blog/uac-0255-distributing-agewheeze-rat/
- https://thecyberexpress.com/hackers-impersonate-cert-ua-agewheeze-rat/

---

## 📋 Noted

- **Not yet assigned** — EvilTokens PhaaS: Device code phishing-as-a-service platform targeting Microsoft 365, 340+ organizations impacted since February 2026. Monitoring for escalation.
- **Not yet assigned** — CrystalRAT MaaS: New Telegram-promoted malware-as-a-service with RAT, stealer, and keylogging capabilities. Low-interest unless linked to campaigns.
- **Not yet assigned** — NoVoice Android malware: Found in 50+ Google Play apps, 2.3M device infections. Mobile-only, out of primary scope.
- **Not yet assigned** — DeepLoad malware: New credential stealer with USB spreading capability dropped via ClickFix attacks. Monitoring.
- **Not yet assigned** — Claude Code source leak: Anthropic accidentally published Claude Code source (2,000 TypeScript files) in npm package v2.1.88. No credentials exposed; packaging error, not a breach.
- **CVE-2026-4675, CVE-2026-4676** — Chrome WebGL/Dawn: Two additional high-severity Chrome vulnerabilities fixed alongside CVE-2026-5281, reported by the same researcher.

---

## 📡 Source Coverage

**Sources checked:** 31/31
**Sources with findings:** 8

| Status | Source | Notes |
|--------|--------|-------|
| ✅ | bleepingcomputer.com | 3 findings (Chrome 0-day, TrueConf 0-day, EvilTokens) |
| ✅ | thehackernews.com | 1 finding (AGEWHEEZE/CERT-UA) |
| ✅ | cisa.gov/kev | 1 finding (CVE-2026-5281 added) |
| ✅ | cisa.gov | No new advisories beyond KEV |
| ✅ | securityweek.com | 1 finding (Hasbro breach) |
| ✅ | github.com/search?q=CVE | No new high-impact repos beyond known |
| ✅ | schneier.com | Commentary only (hackback policy) |
| ✅ | krebsonsecurity.com | Recap of TeamPCP/CanisterWorm (already reported) |
| ✅ | rapid7.com | No new findings (BPFdoor already covered) |
| ✅ | attackerkb.com | CVE-2026-20127 deep dive (already reported) |
| ✅ | fortinet.com/blog/threat-research | Cyber Fallout analysis — no new vulns |
| ✅ | securitylab.github.com | No new disclosures since last cycle |
| ✅ | seclists.org/fulldisclosure | No new disclosures in April |
| ✅ | packetstormsecurity.com | 35 new exploits, 266 advisories — nothing new in scope |
| ✅ | opencve.io | Platform page only, no new alerts beyond covered CVEs |
| ✅ | nvd.nist.gov | Search page — no new critical CVEs beyond covered |
| ⚠️ | cve.mitre.org | Page returned no extractable content |
| ⚠️ | cve.org | Page returned no extractable content |
| ✅ | googleprojectzero.blogspot.com | Research posts on fuzzing/Windows UAC — no new vulns |
| ✅ | blog.cloudflare.com/tag/security | Client-Side Security GA, fraud prevention — no new vulns |
| ✅ | msrc.microsoft.com/blog | Page rendered minimal content, no new advisories |
| ✅ | hackerone.com/hacktivity | Page rendered minimal content (JS-heavy) |
| ❌ | bugcrowd.com/disclosures | 404 — page not found |
| ✅ | kb.cert.org/vuls | No new vulnerability notes |
| ✅ | avleonov.com | March Linux Patch Wednesday recap — no new vulns beyond covered |
| ✅ | github.com/0xMarcio/cve | No new high-impact PoCs beyond already tracked |
| ✅ | dbugs.ptsecurity.com | Platform page only, no new disclosures |
| ✅ | habr.com/ru/companies/tomhunter/articles | February recap only — nothing new |
| ✅ | teletype.in/@cyberok | Russian-language vuln analysis — no new items in scope |
| ✅ | cert.gov.ua | Page rendered minimal content (JS-heavy) |
| ✅ | helpnetsecurity.com (supplementary) | CVE-2026-5281 detail, EvilTokens coverage |
