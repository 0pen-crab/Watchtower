# Watchtower Night Report — 2026-06-18
**Cycle:** Night | **Generated:** 2026-06-18 00:00 UTC (2026-06-18T00:00:00Z)
**Sources checked:** 21/30 | **CISA KEV total:** 1,431+ (estimate via downstream relays) | **New KEV additions:** 2 (Joomla JCE, LiteSpeed cPanel — both confirmed in mainstream-relay path)

---

## 🔴 CRITICAL

### Joomla JCE Extension CVE-2026-48907 — CISA KEV-Added 2026-06-17 With BOD 26-04 3-Day FCEB Deadline 2026-06-20; Automated Mass-Exploitation Active (CVSS 10.0)
**Product:** Widget Factory Joomla Content Editor (JCE Pro) — all versions before 2.9.99.6 | **CVE:** CVE-2026-48907 | **Status:** Patched + KEV + Actively Exploited (automated)

Improper access control in the editor-profile creation flow lets an unauthenticated remote attacker upload and execute arbitrary PHP code by creating new editor profiles — no credentials, low complexity, no user interaction. Working exploit code is public, attacks are automated, and Widget Factory explicitly warned that all Joomla instances reachable on the public internet are at risk regardless of whether public registration is enabled. CISA added the CVE to KEV on 2026-06-17 with a Binding Operational Directive 26-04 3-day federal-civilian-executive-branch (FCEB) remediation deadline of 2026-06-20 (Friday) — the second-ever invocation of the new BOD 26-04 3-day-tier-equivalent after Ivanti Sentry CVE-2026-10520 on 2026-06-11.

**Timeline:** Patched 2026-06-03 → 2026-06-06 in JCE Pro 2.9.99.6 → public PoC released → automated exploitation observed in the wild → CISA KEV add 2026-06-17 → BOD 26-04 3-day federal deadline 2026-06-20.

**Why it matters:** Joomla powers an estimated 1.3M+ live sites globally including a long tail of marketing / community / partner-portal properties typically not in the same patch cadence as the core stack. With automated public exploit code and only a 3-day federal deadline, every public-facing Joomla instance running JCE Pro should be treated as 24-hour patch SLA. Patching closes the entry point but does not clean an already-compromised host — assume forensic / IR effort for any unpatched instance.

**Discovered by:** Widget Factory engineering team (vendor-discovered) with downstream confirmation via Joomla Security Strike Team and CISA KEV team.

**Mitigation:**
- Upgrade JCE Pro to 2.9.99.6 or later **today**.
- Rotate all Joomla administrative and editor-profile passwords.
- Forensic review of `tmp/`, `images/`, and any editor-profile-writeable directory for webshells (look for unexpected `.php` files created after 2026-06-06).
- Full server-side malware scan and integrity check on every patched instance.
- If patching cannot occur within the BOD 26-04 window, decommission the public-facing instance behind WAF / IP-allowlist until patched.

**Sources:** [BleepingComputer 2026-06-17](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-max-severity-joomla-plugin-flaw-by-friday/) | [The Hacker News 2026-06-17](https://thehackernews.com/) | [SecurityWeek 2026-06-17](https://www.securityweek.com/joomla-litespeed-vulnerabilities-exploited-in-attacks/)

---

### FortiBleed — 73,932 Fortinet SSL VPN URLs / ~75K FortiGate Devices Exposed With Plaintext Credentials + Configuration Data (Russian-Speaking Multi-Operator Group, 1.16B Credential Attempts)
**Product:** Fortinet FortiGate SSL VPN + management interfaces | **CVE:** None assigned (operational compromise + credential exfil dataset, not a single advisory) | **Status:** Active Exploitation Confirmed + Mass-Scale Credential Exposure

Researcher Bob Diachenko discovered an exposed attacker-controlled server containing a dataset documenting ~1.16 billion FortiGate SSL VPN credential-attack attempts and 73,932 unique firewall URLs across 194 countries, dubbed "FortiBleed" by the press. The threat group — assessed as Russian-speaking multi-operator — used a 45-GPU cluster to crack intercepted SSL VPN authentication hashes, then logged plaintext usernames, email addresses, passwords, firewall configuration data, and verified administrative credentials for organizations including **Chevron, Samsung, Foxconn, Comcast, AT&T, Oracle**, a Turkish NATO defense contractor (with classified documents extracted), plus organizations in Japan, Taiwan, Vietnam, Iraq, and Turkey. Independent SOCRadar telemetry corroborates ~30,000 distinct compromised Fortinet firewalls actively used as listening posts. Kevin Beaumont confirmed "almost all are still online."

**Timeline:** Diachenko discovery 2026-06-16 → Hudson Rock free FortiBleed lookup tool published 2026-06-17 → BleepingComputer + SecurityWeek primary coverage 2026-06-17 → no Fortinet PSIRT response at time of writing.

**Why it matters:** This is the largest single-vendor perimeter-VPN credential-exposure incident of 2026 by an order of magnitude, surpassing every prior Fortinet leak (DarkRaaS 2024, Belsen Group 2025). 21,632 unique impacted domains means the long-tail exposure is enormous: any organization with FortiGate SSL VPN today should assume credentials may be in the dataset, rotate immediately, and check Hudson Rock's lookup tool for exposure. The dataset also includes Fortune-100-scale Industrial-Control-System-adjacent organizations (Chevron, Samsung Display, Oracle) — initial-access brokers (IABs) and ransomware affiliates are likely to actively monetize this dataset within 30 days, matching the Qilin / PAN-OS cadence pattern (MEMORY 2026-06-12).

**Discovered by:** Bob Diachenko (independent researcher) with corroboration from SOCRadar (~30K active compromised devices), Kevin Beaumont (online verification), and Hudson Rock (lookup tool).

**Mitigation:**
- **Immediately** rotate all Fortinet SSL VPN user credentials AND administrative credentials across every FortiGate appliance.
- Enforce MFA on all SSL VPN access — anything without MFA in this dataset is presumed compromised.
- Check Hudson Rock's FortiBleed lookup tool for organization-level exposure.
- Review gateway authentication logs back at least 90 days for suspicious successful logins.
- Pull configuration backups and check for unauthorized policy / admin / API changes.
- Monitor for FortiGate-originated egress to known C2 / Tor / unusual destinations.

**Sources:** [BleepingComputer 2026-06-17](https://www.bleepingcomputer.com/news/security/fortibleed-leak-exposes-fortinet-vpn-credentials-for-73-000-devices/) | [SecurityWeek 2026-06-17](https://www.securityweek.com/3-recently-patched-fortinet-fortisandbox-vulnerabilities-in-hacker-crosshairs/)

---

## 🟠 HIGH

### Mastra npm Supply-Chain Compromise — 144 @mastra/* Packages Backdoored Via Hijacked Contributor Account + "easy-day-js" Trojanized Dependency
**Product:** @mastra/* npm packages (144 in the @mastra namespace, including @mastra/core at ~918K weekly downloads) | **CVE:** Not yet assigned | **CVSS:** Pending | **First reported:** 2026-06-17

Threat actors compromised the npm account of a legitimate former maintainer ("ehindero") in the @mastra namespace and within an 88-minute window injected a malicious dependency named `easy-day-js` — a typo-trojanized clone of the legitimate `dayjs` library — into 144 packages. `easy-day-js` runs obfuscated code via a postinstall hook acting as a dropper / loader: it harvests browser history and data from 160+ cryptocurrency wallet extensions, establishes cross-platform persistence (Windows, macOS, Linux), then polls attacker-controlled C2 servers for additional second-stage modules to fetch and execute under detached `node` processes. The campaign combines clean decoy package versions, obfuscated postinstall loader, runtime payload download, detached execution, self-deletion, Node-themed persistence, and a remote module system.

This is the fifth Wave-2-class Rust+eBPF / npm-supply-chain compromise within 30 days (Arch Linux AUR 06-13 → 1,500+ packages 06-17, IronWorm 06-04, Miasma 06-02, chalk-template 05-19 — MEMORY 2026-06-06/13/17), confirming AUR + npm Trusted Publishing + maintainer-handover workflows are now the primary Wave-2 entry-points. The Mastra namespace's central role in the AI-agent-framework ecosystem (`@mastra/core` ~918K weekly downloads) means the blast radius extends across multiple downstream agentic-framework consumers.

**Mitigation:**
- Audit `package-lock.json` / `pnpm-lock.yaml` / `yarn.lock` for any `@mastra/*` versions resolved between 2026-06-17 00:00 UTC and the rollback-to-safe-version time.
- If detected, roll back to a known-good pre-2026-06-17 version per Mastra advisory.
- Rotate all credentials accessible from any host that ran `npm install` against an affected lockfile — crypto wallet keys, SSH keys, gh CLI tokens, browser-stored credentials.
- Hunt for the postinstall-spawned detached `node` process tree and persistence artifacts (LaunchAgents on macOS, scheduled tasks on Windows, systemd user units on Linux).
- Set `npm config set ignore-scripts true` as the default policy across CI/CD and developer fleet (npm 12 default-disable rollout — MEMORY 2026-06-16/17 — is the long-term mitigation).

**Sources:** [The Hacker News 2026-06-17](https://thehackernews.com/) | [BleepingComputer 2026-06-17](https://www.bleepingcomputer.com/)

---

## 🟡 MEDIUM

### Apache DolphinScheduler 6-CVE Batch — Authorization / Privilege-Escalation / Permission-Check-Bypass Cluster Via Apache Security Mailing List
**Product:** Apache DolphinScheduler (workflow scheduler) | **CVE:** CVE-2026-32966, CVE-2026-32967, CVE-2026-42357, CVE-2026-47340, CVE-2026-49050, CVE-2026-41280 | **Published:** 2026-06-17

Apache disclosed six independent authorization-class vulnerabilities in DolphinScheduler via openwall oss-security on 2026-06-17: missing authorization in the DataSource API exposes data-source metadata (CVE-2026-32966); the `/v2` experimental interface lacks permission checks (CVE-2026-32967); incorrect authorization lets users view workflow-instance details beyond their permissions (CVE-2026-42357); authenticated users can improperly access alert information (CVE-2026-47340); a regular user can generate administrative access tokens via the `/access-tokens` endpoint (CVE-2026-49050); and system-login users bypass authorization to delete workflows (CVE-2026-41280). Combined, these effectively collapse the role-based access control posture of any multi-tenant DolphinScheduler deployment to "anyone with a login can act as admin." Open public-facing DolphinScheduler instances expose this cluster directly; the CVE-2026-49050 "regular user → admin token" path is the highest-value chain link.

This continues the openwall-as-canonical-primary-source pattern for Apache batch disclosures (MEMORY 2026-05-04 / 06-11 / 06-13) and is the latest in the Apache batch-disclosure cadence — typically 1-3 days ahead of mainstream pickup.

**Mitigation:**
- Upgrade DolphinScheduler per the Apache project's fixed-version-list at apache.org (see project's GitHub releases for current).
- Until patched, restrict access to DolphinScheduler UI / API endpoints behind authenticated VPN / SSO / IP-allowlist.
- Audit `/access-tokens` endpoint usage logs back to 2026-05-01 for unexpected admin-token generation.
- Review existing user-role assignments and disable the experimental `/v2` interface in production.

**Sources:** [openwall oss-security 2026-06-17](https://www.openwall.com/lists/oss-security/2026/06/17/)

---

## 📋 Noted / Monitoring

**Microsoft Defender 'RoguePlanet' CVE-2026-50656 (CVSS 7.8)** — yesterday's NOTED 'RoguePlanet zero-day' (06-16) now has CVE assigned, Microsoft confirmed patch in development, and Positive Technologies attributes active in-the-wild exploitation. Local-only LPE → SYSTEM via race condition in Malware Protection Engine — scope-borderline (out of scope by strict local-LPE rule) but kept in monitoring because Defender is on every Windows host. Watch for permanent code patch in next Patch Tuesday.

**Apache Shiro CVE-2026-49268** — Directory-name (LDAP DN) injection in `DefaultLdapRealm` authentication. Affects multi-tenant deployments using Shiro for LDAP-backed auth. Disclosed via openwall oss-security 2026-06-17. Pending CVSS — watch for upgrade guidance.

**Linux kernel "Dirty Frag" CVE-2026-43284 + CVE-2026-43500** — LPE chain to root, public exploit code, evidence of in-the-wild exploitation per Positive Technologies 'In the Trend of VM' #28 (avleonov 2026-06-17). Pure local-LPE = strict-scope skip; monitoring only.

**Linux kernel "Fragnesia" CVE-2026-46300** — LPE with public exploit, per avleonov 2026-06-17. Lab repository at `BenedictEjepu/CVE-2026-46300-Fragnesia` on GitHub. Strict-scope skip; monitoring only.

**Palo Alto Networks PAN-OS CVE-2026-0300** — unauthenticated RCE on PAN-OS appliances per avleonov 2026-06-17 'In the Trend of VM' #28; publicly available exploit. Pending mainstream-news cross-reference before promotion to NEWS — this would land in the same 2026-Q2 perimeter-VPN cluster as CVE-2026-0257 (06-16) and CVE-2026-50751 (Check Point, 06-12).

**libtiff CVE-2026-36849** — Denial-of-service via large `SamplesPerPixel` tag (openwall 2026-06-17). Affects image-processing pipelines that ingest user-supplied TIFFs — watch the multimedia-parser pipeline isolation pattern (MEMORY 2026-06-14 GPAC/MP4Box).

**Vim < 9.2.0670** — Out-of-bounds read in Text Property count (openwall 2026-06-17). Bounded impact; relevant only to plugin-rich Vim setups loading untrusted files.

**SignalRGB kernel driver VU#380058** — Improper access control and IOCTL vulnerabilities (CERT/CC 2026-06-17). Local-LPE class; relevant to gaming-PC / kernel-driver attack surface but strict-scope skip for Watchtower-grade fleets.

**Kodak ShinyHunters breach** — Kodak acknowledged a breach claimed by the ShinyHunters extortion gang (BleepingComputer 2026-06-17). Continues the ShinyHunters PeopleSoft / Council of Europe / Salesforce campaign cadence (MEMORY 2026-06-11/13/16).

**Oracle June 2026 Critical Patch Update — 245 patches** (SecurityWeek 2026-06-17) — Oracle's second monthly CPU under the new accelerated cadence; covers Communications, EBS, Enterprise Manager. PeopleSoft fix-pack drop already absorbed in 06-12 reports; watch the Communications and EBS CVE list for any KEV-grade items in the next 48h triage.

**Crypto Clipper VirusTotal abuse** — Threat actors leveraged paid posts on legitimate news sites, fake reviews, and coordinated VirusTotal "trusted comment" accounts to inflate download counts and ratings (THN 2026-06-17). New tradecraft data point: VirusTotal community comments are now actively gamed as a social-engineering signal — defenders should not rely on community comments as a reputation signal.

**JetBrains Marketplace AI-plugin malware — Aikido telemetry expansion** — Follow-up on 2026-06-17 NEWS: Aikido published expanded telemetry showing 7 vendor accounts, ~70K total installs (DeepSeek AI Assist 27,727 + CodeGPT AI Assistant 25,571 as top two), unencrypted HTTP exfil to 39.107.60[.]51. Same incident; no material score change.

**GhostTree NTFS junction Defender-bypass** — Threat actors leveraged recursive NTFS junctions to generate an unbounded number of valid file paths, causing Microsoft Defender scans to never complete (BleepingComputer 2026-06-16). New evasion tradecraft — relevant to EDR posture review but not a vulnerability per se.

**Microsoft Office launch issues post-June-Patch-Tuesday** — Microsoft confirmed an issue preventing third-party applications from launching Office or opening documents on updated Windows (BleepingComputer 2026-06-17). Operational, not a security advisory — but security teams should anticipate user-facing tickets attributing this to Defender / EDR misconfiguration.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer, thehackernews, securityweek, krebsonsecurity | ✅ (BC/THN/SW with findings; Krebs no in-window posts) |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ both 403 — KEV adds (Joomla JCE, LiteSpeed cPanel) confirmed via THN/BC/SW mainstream-relay path |
| Vendor advisories | msrc.microsoft.com/blog, blog.cloudflare.com/tag/security, fortinet.com/blog/threat-research, rapid7.com/blog | ⚠️ MSRC reachable but no in-window posts; Cloudflare last post 06-09; Fortinet last post 06-11; Rapid7 reachable but no in-window dated posts |
| Research / OSINT | schneier.com, avleonov.com, dbugs.ptsecurity.com, securitylab.github.com, kb.cert.org/vuls, github.com/0xMarcio/cve, github.com/search?q=CVE | ✅ avleonov + dbugs + kb.cert + 0xMarcio + github CVE search with findings; schneier no in-scope; securitylab.github.com only stale advisories |
| Supply chain | seclists.org/fulldisclosure, packetstorm.news | ⚠️ fulldisclosure last activity 06-15; packetstorm.news reachable but no listings extracted |
| Threat intel | opencve.io, app.opencve.io | ✅ opencve.io with findings (WordPress plugin CVSS 9.x cluster routed to Noted) |
| CVE primary | nvd.nist.gov, cve.org, cve.mitre.org, googleprojectzero.blogspot.com | ❌ NVD policy page; cve.org + cve.mitre.org JS-only; projectzero.google 404 |
| Bug bounty / public disclosure | hackerone.com/hacktivity, bugcrowd.com/disclosures, attackerkb.com | ❌ all three blocked (JS-only / 404 / 403) |
| Tier-2 Russian-language | habr.com/ru/companies/tomhunter, teletype.in/@cyberok | ⚠️ habr last post 03-06 (~3.4-month silence); teletype last post 02-04 (~4.4-month silence) — flag for drop in sources-review-2026-06.md |
| Tier-2 Ukrainian-language | cert.gov.ua | ⚠️ reachable but empty content (consistent with prior weeks) |

**Errors:** cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403), attackerkb.com (403), bugcrowd.com/disclosures (404), googleprojectzero.blogspot.com (404), cve.org (JS-only / empty body), cve.mitre.org (redirects to cve.org, JS-only), hackerone.com/hacktivity (JS-only / empty body), nvd.nist.gov (returned policy/timeline page, not vulnerability listings)

**CISA KEV:** 2 confirmed adds in 2026-06-17 cycle — CVE-2026-48907 (Joomla JCE, CVSS 10.0, BOD 26-04 3-day FCEB deadline 2026-06-20) and CVE-2026-54420 (LiteSpeed cPanel, KEV-add confirmed via BleepingComputer 2026-06-16 follow-up; previous full coverage 2026-06-15 NEWS / 2026-06-17 UPDATE).

---

*Watchtower vulnerability-researcher | Cycle: 2026-06-18/night | Next: 2026-06-19/night*
