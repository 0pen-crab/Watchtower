# Watchtower Night Report — 2026-03-29
**Cycle:** Night | **Generated:** 2026-03-29 02:15 EEST (2026-03-29T00:15Z)  
**Sources checked:** 34/36 | **CISA KEV total:** 1,554 | **New KEV additions:** 0

---

## 🔴 CRITICAL

### ZDI-26-226 — Microsoft Azure MCP AzureCliService Command Injection 0-Day (CVSS 9.8)
**Product:** Microsoft Azure / azure-cli-mcp | **CVE:** None assigned | **Status:** 0-Day (Unpatched)

ZDI published an unpatched 0-day advisory on March 24 after Microsoft declined to remediate within the 120-day disclosure window, rating the vulnerability "Moderate" internally. The flaw is in the `azure-cli-mcp` component — Azure's Model Context Protocol (MCP) server for AI agent tooling. **No authentication required.** An attacker can inject arbitrary commands into the MCP server and achieve remote code execution in the MCP server's execution context.

**Timeline:** Reported September 10, 2025 → Microsoft acknowledged → Microsoft rated "Moderate" and declined patch → ZDI 0-day published March 24, 2026.

**Why it matters:** MCP is the backbone of Azure's AI agent platform. Exploitation here means attacker-controlled AI tool calls, cloud credential exfiltration, and lateral movement through any Azure services the MCP server is authorized to access. With AI agents increasingly operating with production cloud credentials, the blast radius of a compromised MCP server is unusually high.

**Discovered by:** Alfredo Oliveira and David Fiser, Trend Research.

**Mitigation:**
- No vendor patch. Disable or restrict exposure of azure-cli-mcp endpoints if not essential.
- Apply network-level access controls to MCP server ports.
- Review MCP server authorization scope — minimize cloud permissions.
- Monitor for anomalous command execution patterns in MCP server logs.
- Watch for Microsoft advisory publication.

**Sources:** [ZDI-26-226](https://www.zerodayinitiative.com/advisories/ZDI-26-226/)

---

## 🟠 HIGH

### Infinity Stealer — New macOS Infostealer via Cloudflare/ClickFix Lure (Nuitka-Packaged Python)
**Product:** macOS (user-side campaign) | **CVE:** None | **First reported:** March 28

A new macOS infostealer called "Infinity Stealer" is spreading via fake Cloudflare CAPTCHA / ClickFix lures — a continuation of a social engineering pattern that has proven increasingly effective against macOS users.

**Infection chain:**
1. Victim lands on fake Cloudflare CAPTCHA page (malvertising / phishing)
2. Page redirects to `update-check[.]com` dropper stage
3. Bash script downloads Nuitka-compiled Python payload
4. Infinity Stealer executes silently, evading most AV (Nuitka packaging defeats signature detection)

**What it steals:** Browser credentials and cookies (Chrome, Safari, Firefox), macOS Keychain contents, crypto wallet files (Exodus, MetaMask, Electrum, etc.), `.env` configuration files, SSH private keys.

**C2:** HTTP POST exfiltration + Telegram channel notification. Cloudflare-fronted infrastructure.

**Mitigation:**
- Block `update-check[.]com` and domains in Malwarebytes IoC list.
- Enforce macOS Gatekeeper (notarized binaries only). Monitor for Nuitka executables in `/tmp/` and `~/.local/`.
- Enable Endpoint Security framework hooks for Keychain access events.
- Educate users: Cloudflare CAPTCHA does not ask you to run terminal commands.

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/new-infinity-stealer-malware-grabs-macos-data-via-clickfix-lures/) | [SecurityWeek](https://www.securityweek.com/cloudflare-themed-clickfix-attack-drops-infiniti-stealer-on-macs/)

---

### CVE-2026-30303 + CVE-2026-30304 — AI Coding Assistant Prompt Injection → OS Command Execution (NVD Confirmed)
**Products:** Axon Code (Windows), 'claude-dev-china' VS Code Extension | **CVSS:** 9.6 / 9.8 | **CWE:** 78, 20

Two AI coding assistant vulnerabilities confirmed on NVD this cycle, elevated from the previous cycle's "noted" queue. Research by Secsys-FDU (Fudan University Security Systems Lab).

**CVE-2026-30303 — Axon Code (Windows), CWE-78:**  
Command auto-approval whitelist uses the Unix `shell-quote` library to parse commands on Windows. Attackers construct payloads like `git log ^" & malicious_command ^"`. Axon Code's parser (using shell-quote) sees the `&` as within a quoted string → auto-approves. Windows CMD ignores the `^` escapes → executes the injected command directly. Full RCE bypass of the whitelist.

**CVE-2026-30304 — AI Code ('claude-dev-china' on VSCode Marketplace), CWE-20:**  
A generic prompt injection template wraps any malicious command with context that misleads the LLM into classifying it as "safe for auto-execution." The approval requirement is bypassed; the command runs directly. The 'claude-dev-china' extension is unofficial and not published by Anthropic — it should be removed immediately.

**Why it matters now:** AI coding assistants with auto-approval features are proliferating rapidly. These CVEs demonstrate that safety classifiers in AI tools can be reliably bypassed with simple prompt templates — the attack is reproducible, not theoretical.

**Mitigation:**
- Disable auto-approve command execution in all AI coding assistants.
- Remove 'claude-dev-china' extension; use only official extensions from verified publishers.
- Apply vendor patch for Axon Code or disable auto-approval until patched.
- Require explicit user confirmation for all shell commands regardless of AI safety assessment.
- Audit VS Code extension inventory; flag extensions from unverified publishers with system-call capabilities.

**Sources:** [NVD CVE-2026-30303](https://nvd.nist.gov/vuln/detail/CVE-2026-30303) | [NVD CVE-2026-30304](https://nvd.nist.gov/vuln/detail/CVE-2026-30304) | [Secsys-FDU GitHub](https://github.com/Secsys-FDU/LLM-Tool-Calling-CVEs)

---

### GitLab 18.10.1 / 18.9.3 / 18.8.7 — Four HIGH-Severity Security Fixes
**Products:** GitLab CE/EE 18.8.x, 18.9.x, 18.10.x | **Published:** March 25, 2026

GitLab released three simultaneous patch versions fixing four HIGH-severity vulnerabilities. GitLab.com and Dedicated are already patched. **All self-managed GitLab instances must upgrade immediately.**

| CVE | Title | Severity |
|-----|-------|----------|
| CVE-2026-2370 | Improper Handling of Parameters in Jira Connect → unauthorized access | HIGH |
| CVE-2026-3857 | CSRF in GLQL (GitLab Query Language) API | HIGH |
| CVE-2026-2995 | HTML Injection in vulnerability report (GitLab EE only) | HIGH |
| CVE-2026-3988 | Denial of Service via malformed GraphQL API queries | HIGH |

Also patched: CVE-2026-2745 (Improper Access Control in WebAuthn 2FA — MEDIUM), CVE-2026-1724 (Improper Access Control in GraphQL query — MEDIUM).

Full CVE technical details become public April 25 (30-day disclosure policy).

**Mitigation:** Upgrade to 18.10.1, 18.9.3, or 18.8.7. If upgrade is delayed, rate-limit GraphQL API and restrict Jira Connect integration to known-good sources.

**Sources:** [GitLab Release Blog](https://about.gitlab.com/releases/2026/03/25/patch-release-gitlab-18-10-1-released/)

---

## 🟡 MEDIUM

### Mass GitHub Discussions Campaign — Fake VS Code Security Alerts Delivering Developer-Targeted Malware
**Product:** GitHub Discussions / Developer workstations | **First reported:** March 27, 2026

A large-scale spam campaign is flooding GitHub Discussions with fake VS Code security alerts that reference fabricated CVE identifiers. Clicking the link (hosted on Google Drive) delivers a JavaScript payload that profiles the victim's environment (OS, browser, installed tools, language settings) and applies TDS (Traffic Distribution System) filtering — legitimate users receive the malware while security sandboxes are served benign content.

The campaign targets software developers specifically — a high-value population with production credentials, API keys, and cloud access. GitHub has been notified; campaign scale and rotating infrastructure mean takedown is lagging.

**Mitigation:** Verify all VS Code security advisories through official channels only (marketplace.visualstudio.com, code.visualstudio.com). Block Google Drive downloads at corporate egress. Treat unexpected GitHub Discussions notifications with elevated suspicion. Report to GitHub Trust & Safety.

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/fake-vs-code-alerts-on-github-spread-malware-to-developers/)

---

### TeamPCP Update 003 — Supply Chain Campaign Enters Monetization Phase
**Product:** npm, PyPI, GitHub Actions ecosystems | **SANS ISC:** Update 003, March 28, 2026

The most operationally significant TeamPCP development in this cycle is **what didn't happen**: no new package compromise has been confirmed since Telnyx on March 27 — the first 48-hour window without a new supply chain attack since the campaign began March 19.

Analyst assessment (SANS ISC, Palo Alto): TeamPCP has **shifted from supply chain expansion to monetization** of existing stolen credentials (~300 GB trove, est. 8,000+ unique credentials per GitGuardian). The Vect RaaS affiliate announcement from the prior cycle is now confirmed as the monetization vehicle.

**New defensive resources published this cycle:**
- **Palo Alto Networks:** Behavioral CI/CD detection rules (focus: anomalous `/proc/mem` reads, `tpcp.tar.gz`-pattern archive creation, outbound HTTPS to newly registered domains during workflow runs)
- **CSA:** Kubernetes wiper lab analysis with admission controller mitigation playbook (blocking privileged DaemonSet deployment pattern)

**Recommended:** Complete credential rotations. This window may be brief — TeamPCP explicitly stated long-term intent, and stolen credentials enable future package compromise at any time.

**Sources:** [SANS ISC Diary March 28](https://isc.sans.edu/diaryarchive.html?year=2026&month=3&day=28) | [Palo Alto Blog](https://www.paloaltonetworks.com/blog/cloud-security/trivy-supply-chain-attack/)

---

### AITM Phishing Kit Targeting TikTok for Business Accounts — Malvertising and Ad Fraud
**Product:** TikTok for Business / Google Workspace | **Research:** Push Security, March 27

A new AITM (Adversary-in-the-Middle) phishing campaign is hijacking TikTok for Business accounts to run malicious ads, commit ad fraud, and steal credentials. 

**Chain:** Email → legitimate Google Storage redirect (trust anchor) → Cloudflare Turnstile bot check → fake TikTok/Google page → AITM session token theft. Domains registered seconds before deployment; Cloudflare-hosted; rapid rotation makes IOC-matching ineffective.

**Why TikTok Business?** Accounts link to corporate ad budgets. One compromise = immediate revenue through fraudulent ad spend + credential reuse (most users log in via Google SSO, so one theft exposes both platforms).

Campaign links to prior Google Careers impersonation attacks — persistent threat actor, evolving targets.

**Mitigation:** Enable FIDO2/passkey MFA on TikTok Business and Google Workspace. Set ad spending alerts and daily budget caps. Monitor for new admin users added to ad accounts. Block newly registered domain categories in mail filtering.

**Sources:** [Push Security Blog](https://pushsecurity.com/blog/tiktok-phishing) | [SecurityAffairs](https://securityaffairs.com/190058/security/new-aitm-phishing-wave-hijacks-tiktok-business-accounts.html)

---

### UK FCDO Sanctions Xinbi — $19.9B Telegram Crime Marketplace (DPRK Laundering, Asian Scam Compounds)
**Sanctions Date:** March 26, 2026 | **Source:** UK FCDO, Chainalysis, Elliptic

The UK sanctioned Xinbi, a Telegram-based Chinese-language illicit marketplace that processed **$19.9 billion** in transactions between 2021–2025. Xinbi sold stolen personal databases, unlicensed OTC crypto trades, and satellite internet equipment to scam centers across Southeast Asia.

Critically, **North Korean threat actors** (DPRK-affiliated groups) used Xinbi to launder cryptocurrency stolen from major heists. Also sanctioned: **#8 Park** (Cambodia — described as the largest scam compound in the country, capacity 20,000 trafficked workers) and its operator Legend Innovation Co (Prince Group crime ring, per Elliptic).

The UK is the **first country to sanction Xinbi.** Sanctions cut Xinbi from the legitimate cryptocurrency ecosystem (following the effective precedent of Byex Exchange shutdown after UK sanctions in 2025).

**Compliance action:** Screen Xinbi-linked wallet addresses (Chainalysis/Elliptic published address clusters) against transaction monitoring systems immediately.

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/uk-sanctions-xinbi-marketplace-linked-to-asian-scam-centers/) | [UK FCDO](https://www.gov.uk/government/news/uk-crackdown-on-vile-scam-centres-steps-up-with-sanctions-on-illicit-crypto-network) | [Chainalysis](https://www.chainalysis.com/blog/xinbi-designation-chinese-language-crypto-scam-infrastructure/)

---

## 📋 Noted / Monitoring

**⏰ F5 BIG-IP CVE-2025-53521 — CISA KEV Deadline TOMORROW (March 30)**  
Federal agencies must patch or discontinue F5 BIG-IP AMP by EOD March 30 (Eastern). No new public PoC observed this cycle. Active exploitation confirmed.

**Coruna / DarkSword iOS — Kaspersky Confirms Operation Triangulation Evolution**  
SecurityAffairs (March 26) + Kaspersky Securelist confirmed Coruna's kernel exploit is an updated version of the Operation Triangulation exploit — "an updated version of the same exploitation framework." Five exploit chains, 23 total exploits. Patched in iOS 18.4.1. DarkSword zero-click sub-component remains unconfirmed; Coruna parent tracking sufficient. Removing from active monitoring queue — finding fully reported across prior cycles.

**Ajax Football Club Breach — 300K Fan Records, 42K Season Tickets Accessible**  
Dutch researcher found exposed API keys and shared keys in Ajax Amsterdam's systems. 300K fan accounts, 42K season tickets transferable, 538 stadium bans modifiable. No malicious exploitation; all patched; DPA and police notified. Low operational relevance.

**Dutch Police Internal Phishing Breach**  
Successful phishing against Dutch Police internal systems (March 27). No citizen data, no operational data. Limited impact — noted for completeness.

**Rapid7 2026 Global Threat Landscape Report**  
Third cycle attempting to access full content — URL variants returning 404. Will retry with direct PDF link next morning cycle.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | BleepingComputer, THN, SecurityWeek, SecurityAffairs, TheRecord, Wired, Ars Technica, TechCrunch, Krebs, Schneier, The Register | ✅ |
| CISA / US Gov | CISA KEV, CISA Alerts (funding lapse 404) | ✅ / ⚠️ |
| Vendor advisories | GitLab, Cisco (JS-rendered), Microsoft MSRC (JS-rendered), VMware/Broadcom, Fortinet (404) | ✅ / ⚠️ |
| Research / OSINT | ZDI, NVD, SANS ISC, CERT/CC, OpenCVE, AttackerKB (500), Rapid7, Palo Alto, watchTowr | ✅ / ⚠️ |
| Supply chain | Secsys-FDU, GitHub Advisory DB, Palo Alto XSIAM, SANS ISC | ✅ |
| Threat intel | SecurityAffairs, Push Security, Chainalysis, Elliptic | ✅ |

**Errors:** AttackerKB (500 error), Fortinet PSIRT blog (404), Rapid7 report URL (404)  
**CISA KEV:** 1,554 total entries — no new additions since March 27 (CVE-2025-53521 F5 BIG-IP)

---

*Watchtower vulnerability-researcher agent | Cycle: 2026-03-29/night | Next: 2026-03-29/morning*
