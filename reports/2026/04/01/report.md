# Vulnerability Intelligence Report — 2026-04-01 Night Cycle

---

## 📰 Axios npm Supply Chain Attack — North Korean BlueNoroff Delivers Cross-Platform RAT via Compromised Package

**Threat Score:** 10
**Affected Technology:** Axios (npm package, 100M+ weekly downloads)
**CVE:** Not yet assigned
**CVSS:** N/A

### Summary
North Korean threat actor UNC1069 (BlueNoroff) hijacked the npm account of the primary Axios maintainer and published two malicious versions (1.14.1 and 0.30.4) that inject a trojanized dependency delivering cross-platform RATs targeting Windows, macOS, and Linux. The attack was live for approximately 3 hours on March 31, 2026. Given Axios has ~400 million monthly downloads, the blast radius is potentially enormous. Platform-specific payloads include PowerShell-based persistence on Windows, AppleScript-based binary execution on macOS, and Python-based implants on Linux. The RAT supports shell command execution, directory enumeration, and secondary payload delivery. Google GTIG attributed the attack to UNC1069, a DPRK financial-theft group.

### Why It Matters
Axios is one of the most widely used JavaScript HTTP client libraries in existence. Any enterprise with Node.js-based applications in CI/CD or production likely has Axios as a direct or transitive dependency. The 3-hour window was enough for automated build systems to pull the malicious version.

### Discovery
**First seen at:** bleepingcomputer.com
**How found:** Multiple supply chain security firms (Endor Labs, Socket, Aikido, StepSecurity) independently flagged the malicious versions within hours. Cross-referencing BleepingComputer, The Hacker News, and SANS confirmed the scope.

### Sources
- https://www.bleepingcomputer.com/news/security/hackers-compromise-axios-npm-package-to-drop-cross-platform-malware/
- https://thehackernews.com/2026/03/axios-supply-chain-attack-pushes-cross.html
- https://www.sans.org/blog/axios-npm-supply-chain-compromise-malicious-packages-remote-access-trojan
- https://www.endorlabs.com/learn/npm-axios-compromise

---

## 🔄 Update: TeamPCP Supply Chain Campaign — Cisco Breached, Source Code Stolen via Trivy Credentials

**Previous Threat Score:** 10 → **Updated Threat Score:** 10
**CVE:** CVE-2026-33634

### What Changed
TeamPCP's Trivy supply chain compromise has now resulted in a confirmed breach of Cisco's internal development environment. Attackers used credentials stolen via the malicious Trivy GitHub Action to exfiltrate 300+ GitHub repositories including source code for Cisco's AI products (AI Assistants, AI Defense) and unreleased products. AWS keys were also stolen and used for unauthorized activities across Cisco AWS accounts. Some stolen repos reportedly belong to government agencies and banks. This represents the most significant downstream impact from the TeamPCP campaign to date.

### Sources
- https://www.bleepingcomputer.com/news/security/cisco-source-code-stolen-in-trivy-linked-dev-environment-breach/
- https://www.securityweek.com/teampcp-moves-from-oss-to-aws-environments/

---

## 📰 Vim and GNU Emacs RCE via Crafted File — AI-Discovered Zero-Days Affect Default Linux Installs

**Threat Score:** 8
**Affected Technology:** Vim (≤9.2.0271) and GNU Emacs (all versions)
**CVE:** Not yet assigned (Vim patched in 9.2.0272; Emacs unpatched)
**CVSS:** N/A

### Summary
Researcher Hung Nguyen of Calif demonstrated that Claude AI could identify zero-day RCE vulnerabilities in both Vim and Emacs by analyzing their source code. The Vim flaw exploits missing security checks in modeline handling combined with sandbox bypass, allowing arbitrary command execution when a victim opens a crafted file. The Emacs vulnerability exploits automatic vc-git integration that reads attacker-controlled .git/config files to execute arbitrary programs. Vim has been patched; Emacs maintainers consider it a Git responsibility and refuse to fix it.

### Why It Matters
Vim is installed by default on virtually every Linux server, embedded system, and macOS machine. A file-open-to-RCE primitive is an ideal payload delivery mechanism — email attachment, shared drive, cloned repository. The Emacs variant specifically affects developers who clone untrusted repos.

### Discovery
**First seen at:** bleepingcomputer.com
**How found:** BleepingComputer article on March 31 detailing the Calif research blog post. Cross-referenced with cyberpress.org confirmation.

### Sources
- https://www.bleepingcomputer.com/news/security/claude-ai-finds-vim-emacs-rce-bugs-that-trigger-on-file-open/
- https://blog.calif.io/p/mad-bugs-vim-vs-emacs-vs-claude
- https://github.com/vim/vim/security/advisories/GHSA-2gmj-rpqf-pxvh

---

## 📰 CrewAI Multi-Vulnerability Chain — RCE, SSRF, and File Read via Prompt Injection in AI Agent Framework

**Threat Score:** 7
**Affected Technology:** CrewAI (multi-agent AI framework)
**CVE:** CVE-2026-2275, CVE-2026-2285, CVE-2026-2286, CVE-2026-2287
**CVSS:** N/A

### Summary
CERT/CC disclosed four vulnerabilities in CrewAI that can be chained via prompt injection to achieve RCE, SSRF, and arbitrary file read on systems running CrewAI agents with the Code Interpreter Tool enabled. CVE-2026-2275 allows sandbox escape via SandboxPython fallback when Docker is unreachable; CVE-2026-2287 causes insecure fallback when Docker stops during runtime; CVE-2026-2286 enables SSRF via unvalidated URLs in RAG tools; CVE-2026-2285 allows arbitrary file reads via the JSON loader. No complete patch is available — the vendor has only committed to partial mitigations.

### Why It Matters
As AI agent frameworks proliferate in enterprise environments, these vulnerabilities represent a class of AI-infrastructure attacks that allow prompt injection to escape the AI sandbox and compromise the underlying host — a critical risk for any organization deploying CrewAI-based agents.

### Discovery
**First seen at:** kb.cert.org
**How found:** CERT/CC advisory VU#221883, cross-referenced with SecurityWeek coverage and security research blog posts.

### Sources
- https://kb.cert.org/vuls/id/221883
- https://www.securityweek.com/crewai-vulnerabilities-expose-devices-to-hacking/
- https://securityonline.info/crewai-vulnerabilities-rce-ssrf-sandbox-escape-cve-2026/

---

## 📰 StrongSwan CVE-2026-25075 — 15-Year-Old VPN DoS Vulnerability Enables Unauthenticated Service Crash

**Threat Score:** 7
**Affected Technology:** StrongSwan (versions 4.5.0 through 6.0.4)
**CVE:** CVE-2026-25075
**CVSS:** N/A (High severity per vendor)

### Summary
Bishop Fox researchers discovered an integer underflow vulnerability in StrongSwan's EAP-TTLS AVP parser that allows an unauthenticated remote attacker to crash VPN services with a single malformed packet. The flaw has existed for 15 years across all versions from 4.5.0 to 6.0.4. The crash is delayed — triggered on the next incoming connection after the malicious packet — making the attack extremely difficult to trace forensically. Fixed in StrongSwan 6.0.5.

### Why It Matters
StrongSwan is one of the most widely deployed open-source IPsec VPN solutions, used in enterprise gateway appliances, cloud VPN termination, and site-to-site connectivity. Unauthenticated remote DoS against VPN infrastructure can isolate remote workers and disrupt business operations with no trace.

### Discovery
**First seen at:** securityweek.com
**How found:** SecurityWeek article referencing Bishop Fox research and strongSwan vendor advisory.

### Sources
- https://www.securityweek.com/strongswan-flaw-allows-unauthenticated-attackers-to-crash-vpns/
- https://www.strongswan.org/blog/2026/03/23/strongswan-vulnerability-(cve-2026-25075).html

---

## 📰 CVE-2026-4415 — GIGABYTE Control Center Remote Arbitrary File Write to Code Execution (CVSS 9.2)

**Threat Score:** 6
**Affected Technology:** GIGABYTE Control Center (≤25.07.21.01)
**CVE:** CVE-2026-4415
**CVSS:** 9.2

### Summary
GIGABYTE Control Center, pre-installed on all GIGABYTE laptops and motherboards, contains a critical vulnerability in its network pairing feature that allows unauthenticated remote attackers to write arbitrary files to any location on the OS, leading to code execution or privilege escalation. The flaw was discovered by SilentGrid researcher David Sprüngli and disclosed by Taiwan CERT. Users must update to version 25.12.10.01.

### Why It Matters
GCC comes pre-installed on GIGABYTE hardware, meaning affected systems include corporate workstations and developer machines that may have the pairing feature enabled by default. Remote unauthenticated file write is a direct path to code execution.

### Discovery
**First seen at:** bleepingcomputer.com
**How found:** BleepingComputer article referencing Taiwan CERT advisory and GIGABYTE security bulletin.

### Sources
- https://www.bleepingcomputer.com/news/security/gigabyte-control-center-vulnerable-to-arbitrary-file-write-flaw/
- https://www.twcert.org.tw/en/cp-139-10804-689cd-2.html
- https://www.cve.org/CVERecord?id=CVE-2026-4415

---

## 📰 OpenAI Codex Command Injection — GitHub Token Compromise Across Shared Repositories

**Threat Score:** 7
**Affected Technology:** OpenAI Codex (cloud-based AI coding agent)
**CVE:** Not yet assigned
**CVSS:** N/A

### Summary
Security researchers discovered a critical command injection vulnerability in OpenAI's Codex coding agent that could be exploited to steal GitHub authentication tokens. The flaw allowed attackers to compromise tokens across multiple users interacting with a shared repository, enabling supply chain attacks. OpenAI has patched the vulnerability. The disclosure was coordinated alongside a separate ChatGPT data exfiltration fix.

### Why It Matters
AI coding agents are rapidly being adopted in enterprise development workflows. A vulnerability that allows GitHub token theft through a shared repo effectively turns the AI assistant into an attack vector — any developer who uses Codex on a poisoned repo could have their credentials stolen.

### Discovery
**First seen at:** securityweek.com
**How found:** SecurityWeek and The Hacker News coverage of the researcher's disclosure and OpenAI's patch.

### Sources
- https://www.securityweek.com/critical-vulnerability-in-openai-codex-allowed-github-token-compromise/
- https://thehackernews.com/2026/03/openai-patches-chatgpt-data.html
- https://siliconangle.com/2026/03/30/openai-codex-vulnerability-enabled-github-token-theft-via-command-injection-report-finds/

---

## 📋 Noted

- **CVE-2026-33989** — Mobile Next MCP Server: Path traversal in screenshot and screen recording tools allows arbitrary file write. Low priority — niche tool.
- **CVE-2026-32846** — OpenClaw (< 2026.3.23): Path traversal in media parsing allows arbitrary file read. Already noted in prior cycle.
- **CVE-2026-33442 / CVE-2026-33468** — Kysely TypeScript SQL Query Builder: SQL injection via backslash escape bypass on MySQL. Niche ORM library.
- **CVE-2026-33438 / CVE-2026-34071** — Stirling-PDF: DoS in watermark functionality and XSS in EML-to-PDF conversion. Self-hosted PDF tool.
- **Not yet assigned** — Venom Stealer: Licensed malware-as-a-service with built-in persistence and continuous credential harvesting. Monitoring for wider adoption.
- **Not yet assigned** — Silver Fox / AtlasCross RAT: Chinese-speaking campaign using typosquatted domains for VPN/messenger brands to deliver RAT. Targets in Asia primarily.

---

## 📡 Source Coverage

**Sources checked:** 31/31
**Sources with findings:** 14

| Status | Source | Notes |
|--------|--------|-------|
| ✅ | bleepingcomputer.com | 4 findings (Axios, Cisco/Trivy, Vim/Emacs, GIGABYTE) |
| ✅ | thehackernews.com | 2 findings (Axios, Silver Fox/AtlasCross RAT) |
| ✅ | cisa.gov/kev | Confirmed KEV additions — no new in-scope |
| ✅ | cisa.gov | Emergency directives, public service announcements — no new findings |
| ✅ | securityweek.com | 4 findings (CrewAI, StrongSwan, OpenAI Codex, TeamPCP/AWS) |
| ✅ | github.com/search?q=CVE | Confirmed trending repos — no new unique findings |
| ✅ | schneier.com | No in-scope findings (quantum crypto, Apple camera, AI regulation) |
| ✅ | krebsonsecurity.com | TeamPCP/CanisterWorm Iran wiper (already reported), botnet takedown (already reported) |
| ✅ | rapid7.com | BPFDoor, Citrix CVE-2026-3055 (already reported), Metasploit wraps |
| ✅ | attackerkb.com | CVE-2026-20127 deep dive (already reported) |
| ✅ | fortinet.com/blog/threat-research | Iran cyber fallout, Agent Tesla, Winos 4.0 — no new in-scope |
| ✅ | securitylab.github.com | Confirmed known CVEs (Sylius, Spree, Rocket.Chat, NocoDB) — already tracked |
| ✅ | seclists.org/fulldisclosure | 26 messages in March — CrewAI, Apple SAs, snap-confine (already reported), Dovecot (already reported) |
| ✅ | packetstormsecurity.com | 35 exploits, 246 advisories in last 7 days — no unique new findings |
| ✅ | opencve.io | Platform landing — no new unique findings |
| ✅ | nvd.nist.gov | Recent CVEs reviewed — Mobile Next, OpenClaw, Kysely, Stirling-PDF noted |
| ✅ | cve.mitre.org | Unreachable (empty extraction) |
| ❌ | cve.org | Extraction failed — no content returned |
| ✅ | googleprojectzero.blogspot.com | Grammar fuzzing research, Windows UAC bypasses — out of scope |
| ✅ | blog.cloudflare.com/tag/security | Client-side security, account abuse protection, AI security — no vulns |
| ✅ | msrc.microsoft.com/blog | Minimal content extracted — no new findings |
| ⚠️ | hackerone.com/hacktivity | JavaScript-rendered, minimal content — no findings extractable |
| ❌ | bugcrowd.com/disclosures | 404 — page not found |
| ✅ | kb.cert.org/vuls | CrewAI VU#221883 finding |
| ✅ | avleonov.com | March Linux Patch Wednesday, trending VM CVEs — cross-referenced, no new unique |
| ✅ | github.com/0xMarcio/cve | Trending PoC repos — confirmed known CVEs, no new unique |
| ✅ | dbugs.ptsecurity.com | Landing page only — no actionable content |
| ✅ | habr.com/ru/companies/tomhunter | February/January roundups — no new March/April findings |
| ✅ | teletype.in/@cyberok | Russian-language roundups — December/January, no new |
| ⚠️ | cert.gov.ua | Minimal content extracted — no findings |
| ✅ | seclists.org/fulldisclosure (duplicate) | Same as above — counted once |
