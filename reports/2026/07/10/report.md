# Watchtower Night Report — 2026-07-10
**Cycle:** Night | **Generated:** 2026-07-10 00:14 UTC (2026-07-10T00:14:00Z)
**Sources checked:** 26/30 | **CISA KEV total:** unreachable (403 via WebFetch) | **New KEV additions:** ColdFusion + Langflow + Joomla — federal patch deadline 2026-07-10 (see Noted)

---

## 🔴 CRITICAL

### Palo Alto Networks PAN-OS 2026-07-09 Batch — 13 Vulnerabilities Including User-ID TSA Unauth RCE (CVSS 9.2) and Captive Portal Buffer Overflow (CVSS 9.3)
**Product:** Palo Alto Networks PAN-OS 11.1 / 11.2 / 12.1 (PA-Series firewalls, VM-Series, Panorama) | **CVE:** CVE-2026-0288, CVE-2026-0265, CVE-2026-0300 (+ 10 more) | **Status:** Patched (vendor-highest urgency)

Palo Alto disclosed 13 PAN-OS vulnerabilities on 2026-07-09 with three at the top of the batch. CVE-2026-0288 (CVSS 9.2) is an unauthenticated buffer overflow in the User-ID Terminal Server Agent — an attacker with network access to the TSA IP and port can corrupt memory and gain RCE with no auth or user interaction. CVE-2026-0265 is an authentication bypass in Cloud Authentication Service (CAS) affecting firewalls and Panorama with CAS enabled. CVE-2026-0300 (CVSS 9.3) is a buffer overflow in the User-ID Authentication Portal (Captive Portal). No in-the-wild yet reported, but the vendor's highest urgency flag and the historical pattern of same-week weaponisation for PAN-OS pre-auth bugs makes this a same-day patch decision.

**Timeline:** Vendor advisory 2026-07-09 → mainstream coverage same day (SecurityWeek).

**Why it matters:** PAN-OS firewalls sit at the perimeter of a large fraction of enterprise networks — including ours. User-ID TSA and Captive Portal are commonly reachable from adjacent management segments and, in some deployments, exposed to the DMZ. Two of the three top CVEs are unauth pre-auth primitives at the edge, and PAN-OS bugs have been weaponised within days in prior cycles (CVE-2024-3400 was mass-exploited within 3 days of disclosure).

**Discovered by:** Not disclosed in initial vendor advisory.

**Mitigation:**
- Patch PAN-OS to the fixed versions per the vendor advisory (11.1, 11.2, 12.1 lines) within 24 hours for internet-facing appliances; within 72 hours for internal-Panorama and management-plane exposure.
- Restrict User-ID TSA source-IP scoping to only the required domain controllers / Windows RDS servers — do not leave the TSA listener reachable from user segments.
- If Cloud Authentication Service is enabled, monitor auth logs for anomalous session establishment during the exposure window.
- Confirm Captive Portal is not internet-reachable unless required for a specific use case.

**Sources:** [Palo Alto Networks Security Advisories](https://security.paloaltonetworks.com/) | [SecurityWeek — Palo Alto Networks Patches 13 Vulnerabilities](https://www.securityweek.com/)

---

### Ubiquiti UniFi Connect CVE-2026-50746 (Max Severity) Unauthenticated Command Injection + 6 Additional Critical CVEs Across UniFi Product Line; ~100k Instances Exposed on Censys
**Product:** UniFi Connect Application (≤ 3.4.16), UniFi Talk, Access, Protect, OS Server, routers/gateways/NAS/surveillance | **CVE:** CVE-2026-50746 (max), CVE-2026-50747, CVE-2026-50748, CVE-2026-54400, CVE-2026-54402, CVE-2026-55115, CVE-2026-55116 | **Status:** Patched 2026-07-09

Ubiquiti disclosed a 7-CVE batch on 2026-07-09. The headline flaw is CVE-2026-50746 — an Improper Access Control bug in the UniFi Connect Application (versions 3.4.16 and earlier) that allows a network-adjacent unauthenticated attacker to trigger command injection on the host device. Six additional critical CVEs cover UniFi Talk, Access, Protect, OS Server, and the routers / gateways / NAS / surveillance family, all with low attack complexity and no user interaction required. No confirmed in-the-wild yet, but Censys tracks ~100k exposed UniFi OS instances (~50k in the US), and Ubiquiti products have been in the state-sponsored targeting picture historically (Moobot / GRU-linked Cyclops Blink / U.S. FBI 2024 takedown).

**Timeline:** Vendor advisory + BleepingComputer + SecurityWeek coverage 2026-07-09.

**Why it matters:** UniFi Connect is the network-mgmt bridge that carries admin control of the whole UniFi fleet — an unauth network-adjacent command injection there is effectively a network-wide primitive. Any UniFi Connect Application still on 3.4.16 with reachable management interfaces is candidate-owned within days of PoC release; edge-office / SMB-tenant fleets often lag on UniFi patching.

**Discovered by:** Not disclosed in initial advisory.

**Mitigation:**
- Update UniFi Connect Application to 3.4.20+ within 24 hours; roll fleet-wide UniFi OS / product updates within 72 hours.
- Confirm UniFi Connect and UniFi OS Server management interfaces are not directly internet-reachable; deploy zero-trust access if remote admin is required.
- Segment UniFi-mgmt VLANs from user segments — CVE-2026-50746 requires only network adjacency.
- Audit exposed instances via Censys / Shodan queries against your netblocks for the exposure baseline.

**Sources:** [BleepingComputer — Ubiquiti warns of new max severity UniFi OS vulnerability](https://www.bleepingcomputer.com/news/security/ubiquiti-warns-of-new-max-severity-unifi-os-vulnerability/)

---

## 🟠 HIGH

### GhostApproval (Wiz) — Symlink-Escape Trust-Boundary Bug Across Six AI Coding Agents; Amazon Q CVE-2026-12958, Cursor CVE-2026-50549, Claude Code Fixed in 2.1.173+ After Initial Anthropic Dispute
**Product:** Amazon Q Developer (language server < 1.69.0), Anthropic Claude Code (< 2.1.173), Cursor, Google Antigravity, Windsurf, Augment | **CVE:** CVE-2026-12958 (AWS), CVE-2026-50549 (Cursor) | **CVSS:** not published | **First reported:** 2026-07-08

Wiz on 2026-07-08 disclosed a systematic informed-consent-bypass pattern across six top AI coding assistants. A malicious repository stages a symlink (e.g. `project_settings.json → ~/.zshrc`) and prompts the agent to modify the innocuously-named file; the approval dialog shows the developer the safe filename while the write actually lands on the symlink target, achieving arbitrary file overwrite → RCE on the developer host on next shell / login. In testing Claude Code, Wiz found the agent had already spotted the real target in its own reasoning ("actually a zsh configuration file") yet the approval box still named the harmless file — hence the "informed-consent bypass" framing. Windsurf's variant is worst: writes land on disk *before* the Accept/Reject buttons render, making the confirmation an undo-mechanism not an authorization gate.

**Timeline:** AWS silently fixed 2026-05-27 (language server 1.69.0) → coordinated disclosure 2026-07-08 → Anthropic initially disputed, then shipped fix in Claude Code 2.1.173+; Cursor + Google patched promptly; Augment + Windsurf acknowledged, remediation pending.

**Why it matters:** This is the **4th AI-IDE / coding-agent sandbox-escape primitive in ~60 days** — following Agentjacking (Sentry-DSN prompt injection 2026-06-13), SymJack (Adversa AI symlink hijack 2026-05-28), and DuneSlide (Cursor CVE-2026-50548/50549 2026-07-03). The cadence is now roughly monthly across the AI-IDE category. Any developer running a pre-patched version of Claude Code / Amazon Q / Cursor / Antigravity / Windsurf / Augment against untrusted repos is one prompt away from local RCE. Windsurf's write-before-approval variant means "review the diff before approving" doesn't help.

**Discovered by:** Wiz Research (blog + coordinated disclosure).

**Mitigation:**
- Pin AI IDEs to latest-major-minus-zero: Claude Code 2.1.173+, Amazon Q Developer language server 1.69.0+, Cursor patched build; treat Augment / Windsurf as vulnerable until vendor patches ship.
- Restrict AI-agent execution to sandboxed workspaces without host filesystem write access to `~/.zshrc`, `~/.bashrc`, `~/.ssh/authorized_keys`, `~/.config/*`, or any auto-executed startup path.
- Enforce a policy that developer AI-agent sessions cannot touch production credentials; ensure `git clone` targets from untrusted forks are opened only in disposable containers.
- Audit developer endpoints for AI-IDE binary and language-server versions on 24h cadence during the patch-rollout window.

**Sources:** [Wiz Blog — GhostApproval: A Trust Boundary Gap in AI Coding Assistants](https://www.wiz.io/blog/ghostapproval-a-trust-boundary-gap-in-ai-coding-assistants) | [The Hacker News — GhostApproval Symlink Flaws](https://thehackernews.com/2026/07/ghostapproval-symlink-flaws-could-let.html) | [The Register — Unix-era security headaches never really die](https://www.theregister.com/security/2026/07/08/bug-in-top-ai-coding-agents-shows-that-unix-era-security-headaches-never-really-die/)

---

## 🟡 MEDIUM

### Roundcube In-the-Wild Exploitation — UNK_MassTraction (China-Aligned) Weaponises CVE-2024-42009 XSS + CVE-2025-49113 Deserialization Against US/Canadian Academic Targets Since May 2026
**Product:** Roundcube Webmail (unpatched instances) | **CVE:** CVE-2024-42009, CVE-2025-49113 | **Published:** Proofpoint disclosure 2026-07-08

Proofpoint disclosed on 2026-07-08 that a China-aligned cluster tracked as UNK_MassTraction has been exploiting two known Roundcube flaws — an XSS (CVE-2024-42009) and a deserialization bug (CVE-2025-49113, ~84k exposed instances at time of original disclosure) — since May 2026 against physics, engineering, and national-security researchers at U.S. and Canadian universities. Attack chain: malicious emails trigger the XSS to load stager code, deserialization primitive lands IceCube stealer plus SquareShell/VShell PHP webshells for persistence. Attribution is Proofpoint's assessment (not high-confidence) based on VPS infrastructure overlap, Chinese-language artifacts, and TTPs consistent with Chinese espionage.

**Mitigation:** Confirm every Roundcube instance is on the fixed versions for both CVEs; scan mail archives for the IceCube stealer and SquareShell/VShell webshell indicators shared by Proofpoint; review academic-affiliation mail environments for the campaign's targeting profile (physics / engineering / national-security researchers).

**Sources:** [BleepingComputer — Hackers exploit Roundcube flaw to spy on academic researchers](https://www.bleepingcomputer.com/news/security/hackers-exploit-roundcube-flaw-to-spy-on-academic-researchers/)

---

## 📋 Noted / Monitoring

**CVE-2026-11405 — Tenda router firmware hardcoded backdoor (5 model families)** — undocumented `sys.rzadmin.password` in `/bin/httpd` grants full admin; vendor unreachable per CERT VU#213560, no patch; consumer/SOHO scope but botnet targeting expected (BleepingComputer + SecurityWeek 2026-07-09).

**Apache Airflow 6-CVE batch (CVE-2026-33264 DAG-author RCE + 5 others)** — fixed in 3.3.0 via oss-security 2026-07-07; Airflow rarely internet-exposed but critical for internal-platform hygiene.

**Django CVE-2026-48588 + CVE-2026-53877 + CVE-2026-53878** — all Low severity per Django team; cache Set-Cookie leak (highest impact) requires shared-cache deployments; upgrade to 6.0.7 / 5.2.16 on normal window.

**CVE-2026-53582 OPNsense XPATH Injection** — Full Disclosure 2026-07-06 with minimal technical detail; in-scope for edge/VPN infrastructure, watching for vendor advisory + patch version before promotion.

**Asterisk 20-advisory batch (23.4.1 / 22.10.1 / 21.12.3 / 20.20.1 + certified-22.8-cert3 + certified-20.7-cert11)** — GHSA-tracked (no CVEs assigned) incl. ARI FILE()-write and REST-over-WebSocket module-load RCE; VoIP widely deployed but batch is 8 days old with no in-the-wild yet.

**Forg365 AI-assisted PhaaS platform for Microsoft 365 (ZeroBEC via BleepingComputer 2026-07-09)** — device-code phishing + AiTM proxying + AI-generated lures + persistent browser-extension access; extends the DEBULL/EvilTokens family; Conditional Access blocking `authentication_method=Device Code` remains the durable control.

**CVE-2026-50656 Microsoft Defender 'RoguePlanet' privilege escalation** — patched via mpengine.dll v1.1.26060.3008; 30-day dedup shows this was Noted 2026-06-19, LPE remains out of scope, no promotion.

**GigaWiper Windows destructive backdoor** — combines disk-wipe + spyware; post-exploitation malware with no patch; calibration for destructive-payload IR playbooks (THN 2026-07-09).

**Injective SDK npm cryptocurrency wallet stealer** — malicious SDK exfiltrating wallet private keys + mnemonic seed phrases; supply-chain calibration, developer-workstation scope (BleepingComputer 2026-07-09).

**Fake Paysafe / Skrill SDKs on npm + PyPI** — credential-stealing packages targeting payment-integration developers; supply-chain calibration, monitor developer-workstation package installs (BleepingComputer 2026-07-08).

**KDDI Japanese telecom breach — 12M+ email/password records exposed** — attributed to zero-day in third-party system; credential-stuffing risk for downstream services (BleepingComputer + SecurityWeek 2026-07-09).

**Google Dialogflow CX 'Rogue Agent' AI-conversation-hijack + credential theft** — cross-project AI agent hijack primitive; in-scope AI-platform advisory but early details limited (SecurityWeek 2026-07-08).

**CVE-2026-41042 Apache Gravitino unauth API exploitation** — new Apache in-scope framework but low deployment footprint; calibration for internal-platform hygiene (oss-security 2026-07-08).

**CVE-2026-57111 Apache Helix REST CORS misconfiguration** — cross-origin abuse in Helix REST; internal-cluster-mgmt tool with limited internet exposure.

**Foreman CVE-2026-5135/5136/5138/5142 batch (3.18.2 / 3.19.1)** — Red Hat Satellite / provisioning platform multi-CVE fixes; enterprise Linux mgmt scope, low internet-facing surface (oss-security 2026-07-07).

**HTSlib ≤1.23.1 multiple file-reading vulnerabilities (oss-security 2026-07-09)** — genomics/BAM/CRAM parsing library; niche defensive scope, calibration for bioinformatics research infrastructure.

**CVE-2026-15308 Incremental HTMLParser CPU-exhaustion DoS** — unauthenticated remote CPU DoS via repeated unterminated markup; watch for downstream web-framework consumers (oss-security 2026-07-09).

**CVE-2026-43499 Linux kernel 'GhostLock' stack-UAF LPE (kernels 2.6.39–7.1)** — 15-year-old LPE earning $92k Google bounty; local-only per Watchtower scope but tracked as post-exploit chain from RCE pivots (oss-security 2026-07-08→09, SecurityWeek 2026-07-09).

**CERT VU#734812 Xerte Online Toolkit authentication bypass → RCE** — auth-bypass RCE in e-learning content platform; niche vertical but in-scope for enterprise education deployments (CERT/CC 2026-07-09).

**CISA KEV additions — Adobe ColdFusion + Langflow + Joomla extensions; federal patch deadline 2026-07-10** — 30-day dedup already covers ColdFusion (2026-07-03 News) + Joomla iCagenda (2026-07-06 News); no new material beyond the KEV listing.

**China-linked LapDogs 'Leash' backdoor arsenal expansion on SOHO routers (LongLeash / DogLeash / JarLeash)** — Cisco Talos disclosure documenting expanding campaign; calibration for edge-device baseline hygiene (SecurityWeek 2026-07-08).

**Lurking Lizard fake 7-Zip installer residential-proxy operation** — 230+ lookalike domains + fake 7-Zip installers recruiting residential-proxy nodes; active since Aug 2022; supply-chain and endpoint calibration (THN 2026-07-09).

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | BleepingComputer, TheHackerNews, SecurityWeek, KrebsOnSecurity, Schneier | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/kev, kb.cert.org | ❌ / ❌ / ✅ |
| Vendor advisories | MSRC, Cloudflare, Palo Alto, Ubiquiti (via news) | ⚠️ / ✅ / ✅ / ✅ |
| Research / OSINT | seclists/fulldisclosure, openwall oss-security (via avleonov reference), Rapid7, FortiGuard, GitHub Security Lab, Wiz Research (via news) | ✅ / ✅ / ✅ / ⚠️ / ✅ / ✅ |
| CVE databases | app.opencve.io, NVD, cve.mitre.org, cve.org, opencve.io homepage | ✅ / ⚠️ / ⚠️ / ⚠️ / ⚠️ |
| Exploit tracking | github.com/search?q=CVE, github.com/0xMarcio/cve, packetstorm.news, attackerkb, projectzero.google | ✅ / ✅ / ⚠️ / ❌ / ⚠️ |
| Threat intel / Bounty | dbugs.ptsecurity, hackerone/hacktivity, bugcrowd/disclosures, avleonov, habr/tomhunter, teletype/cyberok, cert.gov.ua | ✅ / ⚠️ / ❌ / ⚠️ / ⚠️ / ⚠️ / ⚠️ |

**Errors:** cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403), attackerkb.com (403), bugcrowd.com/disclosures (404). Degraded/stale: msrc.microsoft.com/blog (no post listing), packetstormsecurity.com (redirect to ToS/marketing), nvd.nist.gov (marketing/nav only), cve.mitre.org (JS-only redirect), cve.org (JS-only), projectzero.google (no July posts), hackerone.com/hacktivity (JS-only), habr.com/ru/companies/tomhunter (stale March 2026), teletype.in/@cyberok (stale Feb 2026), cert.gov.ua (no listing), avleonov.com (no July 7-10 posts), fortinet.com/blog/threat-research (no July 7-10 posts).

**CISA KEV:** Unable to enumerate directly via WebFetch (403). Cross-referenced through SecurityWeek 2026-07-08: KEV additions include Adobe ColdFusion, Langflow, and Joomla extensions with federal patch deadline 2026-07-10.

---

*Watchtower vulnerability-researcher | Cycle: 2026-07-10/night | Next: 2026-07-11/night*
