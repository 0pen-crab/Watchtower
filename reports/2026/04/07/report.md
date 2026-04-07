# Vulnerability Intelligence Report — 2026-04-07 (night)

## 📰 AI Agent Traps — Google DeepMind Maps Web Attacks Against Visiting AI Agents

**Threat Score:** 7
**Affected Technology:** AI browsing agents (Anthropic, OpenAI, Google, Claude Code-style tools)
**CVE:** Not yet assigned
**CVSS:** n/a

### Summary
Google DeepMind researchers released a paper systematizing web-based attacks against AI agents that browse the web on behalf of users. The work names a class of attack primitives they call "AI Agent Traps" — malicious DOMs, hidden instructions, tool-argument smuggling and data-exfiltration sinks — that let a visited page manipulate or deceive a visiting agent into running unintended tool calls. No single CVE, but the research dramatically lowers the bar for abuse of browser-enabled agents. No confirmed in-the-wild exploitation yet, but proof-of-concept traps are demonstrated against multiple major agents.

### Why It Matters
Any AI-agent-enabled workflow reachable from the internet becomes a new attack surface. Our scope includes attacks on OpenClaw-style bots and hosted agent platforms — this research is a playbook for adversaries targeting exactly that.

### Discovery
**First seen at:** securityweek.com — "Google DeepMind Researchers Map Web Attacks Against AI Agents"
**How found:** SecurityWeek front page + cross-reference against prior Claude Code / Anthropic AI-world coverage in our 30-day dedup index (no overlap).

### Sources
- https://www.securityweek.com/google-deepmind-researchers-map-web-attacks-against-ai-agents/

---

## 📰 LiteLLM Supply Chain Attack Turns Developer Machines Into Credential Vaults

**Threat Score:** 8
**Affected Technology:** LiteLLM (Python AI proxy library), downstream AI apps and CI runners
**CVE:** Not yet assigned
**CVSS:** n/a

### Summary
A threat cluster tracked as TeamPCP trojanized releases of LiteLLM — a popular open-source AI proxy used by thousands of enterprises and downloaded millions of times. The malicious payload specifically harvests plaintext API keys, cloud credentials and local secrets from developer workstations and build pipelines. The Hacker News reports broad, active infection and notes the library's deep integration with local agents means credentials "already sitting on disk" are the target rather than any remote interaction. A patched release exists; every machine that pulled the malicious versions must assume credential compromise.

### Why It Matters
LiteLLM is widely embedded in the AI dev stack our engineering teams rely on. This is a credential-theft grade supply chain hit against any org running AI tooling — rotate API keys for every AI provider, cloud account and internal service referenced on affected machines.

### Discovery
**First seen at:** thehackernews.com — "How LiteLLM Turned Developer Machines Into Credential Vaults for Attackers"
**How found:** THN front page, cross-referenced with securityweek.com coverage of npm/supply-chain ecosystem attacks (Strapi, Axios, Trivy). Not present in dedup index.

### Sources
- https://thehackernews.com/2026/04/ (LiteLLM / TeamPCP writeup)

---

## 📰 European Commission Confirms 300GB Breach Linked to Trivy Supply Chain Compromise

**Threat Score:** 7
**Affected Technology:** Aqua Security Trivy (vulnerability scanner) → AWS victim environments
**CVE:** Not yet assigned
**CVSS:** n/a

### Summary
SecurityWeek reports the European Commission has formally confirmed a data breach tied to the earlier Trivy supply chain compromise. Attackers exfiltrated over 300GB of data from the Commission's AWS environment, including personal information. This is the first major named victim of the Trivy campaign and confirms the compromise reached at least one tier-1 target with production cloud access.

### Why It Matters
Trivy is deployed inside our CI/CD and scanning stacks. A named, successful exfiltration from an EU flagship customer escalates this from "concerning supply chain story" to "assume compromise of any environment that ran affected Trivy versions since late March." Hunt AWS IAM abuse, rotate pipeline credentials.

### Discovery
**First seen at:** securityweek.com — "European Commission Confirms Data Breach Linked to Trivy Supply Chain Attack"

### Sources
- https://www.securityweek.com/european-commission-confirms-data-breach-linked-to-trivy-supply-chain-attack/

---

## 📰 North Korean Axios-Linked Actor Targets High-Profile Node.js Maintainers

**Threat Score:** 7
**Affected Technology:** Node.js / npm maintainer ecosystem
**CVE:** Not yet assigned
**CVSS:** n/a

### Summary
SecurityWeek reports the DPRK threat actor behind the prior Axios npm supply chain attack has pivoted to targeted social engineering against additional high-profile Node.js package maintainers. Tactics mirror the Axios case — fake recruiter / collaborator outreach delivering trojanized code samples — suggesting an ongoing campaign to chain multiple maintainer takeovers into downstream supply chain compromise.

### Why It Matters
Our stack relies on hundreds of npm packages. A single successful maintainer hijack in a popular dependency becomes a mass-RCE primitive against our build and runtime environments. Remind engineering of maintainer-targeting TTPs and enforce dependency pinning + provenance checks.

### Discovery
**First seen at:** securityweek.com — "North Korean Hackers Target High-Profile Node.js Maintainers"

### Sources
- https://www.securityweek.com/north-korean-hackers-target-high-profile-node-js-maintainers/

---

## 📋 Noted

- **[No-CVE] — Microsoft Windows (BlueHammer):** Disgruntled researcher "Chaotic Eclipse" publicly leaked a working LPE zero-day exploit on GitHub after an MSRC handling dispute. LPE-only so out of primary scope, but watch for remote chaining.
- **[No-CVE] — NVIDIA GPU / GDDR6 (GPUBreach):** University of Toronto Rowhammer PoC corrupts GPU page tables, grants arbitrary GPU memory R/W from unprivileged CUDA kernels, chains into CPU-side escalation. IEEE S&P presentation April 13. Local vector, out of primary scope.
- **[No-CVE] — Microsoft 365 (Iran password spraying):** Check Point attributes three-wave password spraying against 300+ Israeli and 25+ UAE M365 tenants to an Iran-nexus actor (March 3/13/23, 2026). Relevant for global exposure tracking.
- **CVE-2026-25994 — PJSIP:** Public buffer overflow PoC on GitHub; affects VoIP stacks embedded in many comms platforms.
- **CVE-2026-31802 — npm tar:** Symlink path-traversal arbitrary file overwrite with public PoC.

---

## 📡 Source Coverage

**Sources checked:** 27/31
**Sources with findings:** 11

| Status | Source | Notes |
|--------|--------|-------|
| ✅ | bleepingcomputer.com | GPUBreach, BlueHammer, REvil IDs |
| ✅ | thehackernews.com | LiteLLM supply chain, Iran spraying |
| ✅ | cisa.gov KEV | No new additions beyond CVE-2026-35616/3502 already tracked |
| ✅ | securityweek.com | AI Agent Traps, Trivy/EC, DPRK Node.js, Strapi/Guardarian, ShareFile (dup) |
| ✅ | github.com/search (CVE) | PJSIP, tar, Dolibarr, KiviCare, Frigate, Chrome — noted/skipped |
| ✅ | schneier.com | No in-scope vulns (Meta/encryption commentary) |
| ✅ | krebsonsecurity.com | REvil/GandCrab attribution (not a vuln) |
| ✅ | rapid7.com/blog | Metasploit wrap-up 04/03, BPFdoor — no new CVEs |
| ✅ | fortinet.com/blog/threat-research | DPRK LNK/GitHub C2, Agent Tesla — intel only |
| ✅ | securitylab.github.com | No new in-scope advisories |
| ✅ | seclists.org/fulldisclosure | April archive, nothing high-signal |
| ✅ | packetstormsecurity.com | 40 new exploits, 221 advisories — no unique in-scope findings beyond above |
| ✅ | opencve.io | No in-scope standout beyond existing coverage |
| ✅ | nvd.nist.gov | Search page loaded (degraded — no direct recent feed) |
| ✅ | blog.cloudflare.com/tag/security | Client-side security product update only |
| ⚠️ | msrc.microsoft.com/blog | Landing page only — no recent posts surfaced |
| ✅ | googleprojectzero.blogspot.com | Mutational grammar fuzzing post — research, no in-scope CVE |
| ✅ | kb.cert.org/vuls | Landing page, no new notes |
| ❌ | attackerkb.com/recent | 404 |
| ❌ | hackerone.com/hacktivity | JS-only, no content returned |
| ❌ | cve.mitre.org | Unreachable (chronic) |
| ❌ | cve.org | Unreachable (chronic) |
| ✅ | packetstorm news | Covered via packetstormsecurity.com redirect |
| ✅ | avleonov.com | No new post |
| ✅ | github.com/0xMarcio/cve | No standout new items |
| ✅ | dbugs.ptsecurity.com | No updates |
| ✅ | habr.com (tomhunter) | No new vuln posts |
| ✅ | teletype.in/@cyberok | No new posts |
| ✅ | cert.gov.ua | No new advisories this cycle |
| ✅ | bugcrowd.com/disclosures | No new disclosures |
| ✅ | fortinet psirt (via KEV ref) | CVE-2026-35616 tracked prior cycle |

Statuses: ✅ checked, ⚠️ partial/degraded, ❌ unreachable.
