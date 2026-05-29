# Watchtower Night Report — 2026-05-29
**Cycle:** Night | **Generated:** 2026-05-29 00:30 UTC (2026-05-29T00:30:00Z)
**Sources checked:** 21/30 | **CISA KEV total:** confirmed +3 supply-chain additions 2026-05-27 | **New KEV additions:** 0 since last report

---

## 🔴 CRITICAL

### FortiClient EMS CVE-2026-35616 — Pre-Auth API Bypass Exploited In-Wild to Push PowerShell Stealer Fleet-Wide (CVSS 9.1)
**Product:** Fortinet FortiClient Endpoint Management Server (EMS) | **CVE:** CVE-2026-35616 | **Status:** Patched + Active Exploitation

Pre-authentication API access bypass in FortiClient EMS lets a remote unauthenticated attacker modify EMS configuration, defer firmware updates, alter Remote Access Profiles, and inject malicious PowerShell scripts into endpoint policies that are then pushed to every managed endpoint as if they were legitimate operations. Arctic Wolf detected active in-the-wild exploitation in May 2026; the campaign drops a previously unreported Windows information stealer (`FortiEndpoint_Patch.exe`) that harvests browser passwords, cookies, and autofill data from Chromium and Gecko, exfiltrating to 83.138.53[.]110. Fortinet shipped a fix in EMS 7.4.7+.

**Timeline:** Active exploitation observed May 2026 → vendor advisory + hotfix 7.4.7 → THN/SecurityWeek public reporting 2026-05-28.

**Why it matters:** EMS is the canonical control plane for FortiClient endpoint fleets in enterprise — a single compromise propagates to every managed endpoint with no per-host intrusion, no credential reuse, no lateral movement footprint. This is the same multi-tenant central-console pivot class as Trend Micro Apex One CVE-2026-34926 (KEV 2026-05-21) and the Quest KACE SMA precedent — "central management plane → fleet-wide PowerShell push" is now an established 2026 tradecraft pattern that defenders must explicitly model.

**Discovered by:** Arctic Wolf Labs (in-the-wild detection).

**Mitigation:**
- Upgrade FortiClient EMS to 7.4.7 or later **immediately** — this is the only supported fix.
- Hunt: review EMS audit logs for unexplained Remote Access Profile / Endpoint Policy changes; cross-reference against your change-management ticket history.
- Hunt: scan every managed endpoint for `FortiEndpoint_Patch.exe` or any unexpected `FortiEndpoint_*.exe`; block C2 IP `83.138.53.110`.
- Hunt: review PowerShell logs on managed endpoints for unsanctioned script execution sourced from EMS policy push within the exposure window.
- Until patched, restrict EMS server inbound to management network only — no internet exposure.

**Sources:** [The Hacker News](https://thehackernews.com/2026/05/threat-actors-exploit-critical.html) | [SecurityWeek](https://www.securityweek.com/critical-forticlient-ems-vulnerability-exploited-in-fresh-attacks/)

---

## 🟠 HIGH

### Gogs — Unpatched 0-Day RCE via Branch-Name Argument Injection into `git rebase --exec` (CVSS 9.4, Metasploit Module Available)
**Product:** Gogs (self-hosted Git platform) | **CVE:** Not yet assigned | **CVSS:** 9.4 | **First reported:** 2026-03-17 (to maintainers), public 2026-05-28

Any authenticated Gogs user who can create a pull request can trigger remote code execution by crafting a malicious branch name that injects `--exec` into the `git rebase` command executed during a "Rebase before merging" merge operation. Disclosed to maintainers on 2026-03-17 and **still unpatched as of public disclosure 72 days later**. A Metasploit module automating the exploit is available, lowering the bar to script-kiddie level. Researcher Jonah Burgess (Rapid7) walked through the argument-injection sink in the public write-up. Attack precondition is minimal: authenticated user with repository-creation permission **or** write access to an existing repo where rebase merging is enabled (single toggle in repo settings).

**Why it matters:** Gogs is widely deployed as a self-hosted alternative to GitHub/GitLab/Gitea in companies that prefer lightweight Git infrastructure. RCE on the Gogs server yields all credentials, SSH keys, signing keys, and source code in every repo on the instance — equivalent in blast radius to the Gitea CVE-2026-27771 private-image exposure of two days ago, but as an active RCE rather than a confidentiality leak. Default-enabled user-registration instances are immediately at risk; even auth-required instances are at risk from any insider or compromised account.

**Mitigation:**
- **Disable user self-registration** if enabled; restrict repository creation to trusted users.
- **Disable rebase merging** in every repository until a vendor fix lands (`Settings → Merge Options → Rebase before merging: off`).
- Audit repository settings fleet-wide for `rebase` merge enablement.
- Monitor Gogs HTTP logs for PR-creation events with suspicious branch names (containing `--exec`, semicolons, backticks, shell metacharacters).
- Track the Gogs GitHub issues / mailing list for patched release availability.

**Sources:** [The Hacker News](https://thehackernews.com/2026/05/critical-gogs-rce-vulnerability-lets.html)

---

### Casdoor VU#780781 — Nine-CVE Identity-Provider Bypass Batch (CVE-2026-9090…9098), No Patch, Vendor Coordination Failed
**Product:** Casdoor (open-source IAM / SAML / OAuth provider) | **CVE:** CVE-2026-9090 through CVE-2026-9098 | **CVSS:** Not assigned | **First reported:** 2026-05-28 (CERT/CC)

CERT/CC published VU#780781 covering nine distinct identity-management bypasses in Casdoor ≤2.362.0: arbitrary SAML signing-certificate acceptance (9090), MFA bypass via social-login binding flow (9091), account takeover via unverified email binding (9092), missing SAML audience restriction (9093), cross-organization token exchange (9094), missing SAML assertion replay protection (9095), unenforced SAML assertion time bounds (9096), missing JWT revocation checks during token exchange (9097), and unsolicited SAML response acceptance without request correlation (9098). **No patches are available; CERT/CC notes vendor coordination was unsuccessful and lists vendor status as "Unknown" for all nine CVEs.** Composite impact: full unauthenticated SAML/JWT identity forgery and cross-org privilege escalation.

**Timeline:** Disclosure 2026-05-28. This is the **second Casdoor batch in 16 days** — VU#937808 (MEMORY 2026-05-12) was the first. Cadence pattern suggests continued researcher interest with no vendor response.

**Why it matters:** Casdoor is a widely deployed open-source SSO/IAM provider used as the identity backbone for many smaller SaaS deployments and internal corporate apps. Nine concurrent unpatched bypasses against the SAML + JWT + MFA primitives means **any Casdoor instance reachable from an attacker (or any service trusting Casdoor SSO) should be treated as an authentication-bypass-as-a-service for the attacker**. This is materially worse than the typical "missing patch" scenario — vendor non-response means no fix is on the horizon.

**Mitigation:**
- **Treat any Casdoor SSO assertion as potentially forged** until vendor patches land.
- Migrate critical applications off Casdoor SSO to Keycloak / Authentik / Auth0 / Okta on an emergency timeline.
- If migration is impossible: restrict Casdoor to specific IdP allow-lists at network boundaries; enforce additional auth factors (mTLS, IP allow-list, hardware key) on every high-privilege account; alert on every cross-org token exchange.
- Treat all existing Casdoor sessions as compromised; force re-authentication and rotate any service tokens that were issued via Casdoor JWTs.

**Sources:** [CERT/CC VU#780781](https://www.kb.cert.org/vuls/id/780781)

---

### Veeam Backup & Replication 13 + Service Provider Console — Triple-CVE Batch with CVSS-9.4 MSP-Console Unauth Script Exec (CVE-2026-32996/32997/32998)
**Product:** Veeam Backup & Replication 13.0.1, Veeam Service Provider Console ≤9.2.1, Veeam Agent for Windows | **CVE:** CVE-2026-32996, CVE-2026-32997, CVE-2026-32998 | **CVSS:** 9.4 / 8.6 / High | **First reported:** 2026-05-28

CVE-2026-32998 (CVSS 9.4) in Veeam Service Provider Console enables remote code execution via unsafe script-execution parameters in the platform's automated alarm-management system — VSPC is the multi-tenant console MSPs use to manage Veeam deployments for downstream customers, so this is **EDR-equivalent multi-tenant pivot class** (joining Trend Micro Apex One CVE-2026-34926 + Quest KACE SMA precedent). CVE-2026-32997 (CVSS 8.6) lets an authenticated Backup Administrator write arbitrary files on Linux-based Veeam Software Appliance backup servers. CVE-2026-32996 is a Windows local privilege escalation in Veeam Agent for Windows. Fixed in VBR 13.0.2.29 and VSPC 9.2.1.33875. No confirmed in-the-wild exploitation yet; Veeam VSPC + B&R servers are top-of-list ransomware targets historically.

**Why it matters:** Veeam backup infrastructure is the primary ransomware-recovery dependency — every ransomware affiliate cluster has a Veeam-credential-harvest + Veeam-volume-encrypt step in its playbook. A pre-patch RCE on the MSP console (VSPC) means a single compromised MSP yields ransomware-affiliate access to every downstream customer's backup environment. Patch tempo here should match the August 2024 Veeam VBR CVE-2024-40711 ransomware tempo (KEV-add within 14 days, deployed by Akira/Fog/Frag affiliates within 30 days).

**Mitigation:**
- VSPC operators: upgrade to 9.2.1.33875 immediately; pre-patch workaround is to flip `AlarmManagement_ScriptExecution` to `false` in the local config JSON.
- VBR 13 operators: upgrade to 13.0.2.29.
- Hunt: review VSPC alarm-script audit logs for any unexpected script registrations within the exposure window.
- Hunt: review Veeam Agent for Windows logs on every endpoint for unexpected service modifications.
- Long-term: ensure Veeam backup repositories are immutable (S3 Object Lock / hardened repos) so a Veeam-server compromise cannot delete backups.

**Sources:** [SecurityOnline](https://securityonline.info/veeam-security-vulnerabilities-patches/) | [Veeam KB4853](https://www.veeam.com/kb4853) | [PT Security dbugs](https://dbugs.ptsecurity.com)

---

### DAEMON Tools Lite Supply-Chain Compromise (CVE-2026-8398) — Signed Trojanized Installers + KEV-Added 2026-05-27
**Product:** DAEMON Tools Lite (Windows 12.5.0.2421 → 12.5.0.2434) | **CVE:** CVE-2026-8398 | **CVSS:** Not specified | **First reported:** Kaspersky Securelist + CISA KEV 2026-05-27

AVB Disc Soft's official DAEMON Tools Lite distribution from `daemon-tools.cc` was compromised between approximately 2026-04-08 and 2026-05-05, with attackers trojanizing three binaries (`DTHelper.exe`, `DiscSoftBusServiceLite.exe`, `DTShellHlp.exe`) and re-signing them with the legitimate AVB Disc Soft code-signing certificate so they bypass signature-based detection. Implant runs at logon → HTTP GET to remote server → executes shell commands via cmd.exe → downloads further payloads. Kaspersky observed several thousand infection attempts across 100+ countries. CISA added CVE-2026-8398 to KEV on 2026-05-27 alongside the TanStack/Nx Console additions.

**Why it matters:** This is the **third major Windows-installer-supply-chain compromise of 2026 against widely-distributed legitimate signed binaries** — joins the SymJack symlink-hijack class (MEMORY 2026-05-27) and Mini Shai-Hulud Wave 2 TanStack/Nx Console (MEMORY 2026-05-21). Code-signing-cert trust is no longer sufficient to assume installer integrity. Any endpoint that installed DAEMON Tools Lite in the April 8 → May 5 window should be treated as potentially backdoored. The malware family is interactive — full RCE control over each infected host.

**Mitigation:**
- Hunt: query EDR for `DTHelper.exe`, `DiscSoftBusServiceLite.exe`, `DTShellHlp.exe` with binary hashes matching the trojanized versions (Kaspersky has published IOC hash list).
- Affected hosts: uninstall DAEMON Tools Lite, full AV scan, treat the host as breach-suspect (rotate any creds typed or auto-filled on host during exposure window).
- Block known C2 destinations from Kaspersky IOC list.
- Policy: add DAEMON Tools to your software-baseline exclusion list pending vendor remediation evidence.
- Long-term: do not trust code-signing certificates as sole installer-integrity gate; require reputational vendor evidence (e.g., Microsoft SmartScreen telemetry, VirusTotal historical reputation) before installing freeware utilities.

**Sources:** [The Hacker News](https://thehackernews.com/2026/05/daemon-tools-supply-chain-attack.html) | [BleepingComputer](https://www.bleepingcomputer.com/news/security/daemon-tools-trojanized-in-supply-chain-attack-to-deploy-backdoor/) | [Securelist (Kaspersky)](https://securelist.com/tr/daemon-tools-backdoor/119654/)

---

## 🟡 MEDIUM

### GreyVibe (Russia-Aligned) Threat Cluster — Industrial-Scale ChatGPT/Gemini/Ideogram-Powered Phishing + AI-Assisted RAT Development against Ukraine
**Product:** Threat-actor activity (not a CVE) — affects Ukrainian government / military / civilian targets | **CVE:** Not applicable | **Published:** 2026-05-28

BleepingComputer and SecurityWeek published joint analysis of "GreyVibe," a likely-Russian threat cluster active since August 2025 that has now scaled AI-tool usage to industrial levels: ChatGPT + Google Gemini + Ideogram AI for phishing-lure generation, plus assistance in developing custom obfuscators (LOOKVALPS, LOOKVALJS, DAYLIGHT, TEASOUP) and the LegionRelay / PhantomRelay PowerShell RATs, with FallSpy Android spyware module and PhantomMail / PhantomClick / PrincessClub / Nebo decoy infrastructure. Targets are Ukrainian gov / military / civilian + Ukraine-related orgs; lures impersonate Ukrainian emergency services, telecom, and energy entities. Novel TTP: AI-generated fake Telegram personas with WebRTC live calls capturing audio/video from victims.

**Why it matters:** **Fourth AI-assisted offensive-ops attribution of 2026** — joins MEMORY 2026-05-11 GTIG ITW AI-generated 0-day, MEMORY 2026-05-26 Nimbus Manticore MiniFast backdoor (Iran), and MEMORY 2026-05-27 mouse5212 malware-slop. Pattern: AI-assistance is now baseline tradecraft across geographic threat-actor clusters (Russia / Iran / commodity-cybercrime), not an exotic edge case. Defenders should assume every phishing campaign uses AI-generated lures going forward; signature-based "look for grammatical errors / unusual phrasing" guidance is obsolete.

**Mitigation:**
- Hunt: review email gateway logs for inbound communication impersonating Ukrainian gov/telecom/emergency services entities — IOC lists from Recorded Future / BleepingComputer references.
- Hunt: review PowerShell logs for behavior matching LegionRelay / PhantomRelay C2 patterns.
- Strategy: do not deprioritize "well-written" phishing — assume all spear-phishing now passes basic linguistic-quality filters.
- Strategy: enforce hardware-key MFA on email + collaboration accounts in any org with Ukraine-related operations or supply-chain exposure.
- Strategy: review WebRTC use across collaboration tooling — Telegram-via-WebRTC live-call decoys are a novel social-engineering vector.

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/greyvibe-hackers-use-chatgpt-gemini-to-power-cyberattacks/) | [SecurityWeek](https://www.securityweek.com/russia-linked-greyvibe-attackers-use-ai-to-supercharge-cyberattacks/)

---

## 🔄 Updates

### TanStack + Nx Console KEV-Added 2026-05-27 (CVE-2026-45321 + CVE-2026-48027) — Federal Deadline 2026-06-10
**Previous coverage:** 2026-05-21/22 (Mini Shai-Hulud Wave 2 cluster); **Previous threat_score:** 7

CISA added CVE-2026-45321 (TanStack OIDC/cache-poisoning supply-chain) and CVE-2026-48027 (Nx Console malicious extension version 18.95.0 published briefly to VS Marketplace + OpenVSX 2026-05-19) to KEV on 2026-05-27, alongside CVE-2026-8398 (DAEMON Tools). This is the official federal-action confirmation that the Wave 2 monetization paths (Megalodon 5,718-commits + GitHub-internal 3,800-repo trojanized Nx Console + Grafana token re-use) are deemed actively exploited at scale by US gov. **Material change:** KEV addition + federal patch deadline establishes formal compliance pressure on Federal Civilian Executive Branch agencies (2026-06-10).

**New threat_score:** 8 (KEV-listed + federal deadline + cross-vendor monetization confirmed).

**Sources:** [Security Affairs](https://securityaffairs.com/192776/security/u-s-cisa-adds-daemon-tools-tanstack-and-nx-console-flaws-to-its-known-exploited-vulnerabilities-catalog.html) | [CISA Cyber X post](https://x.com/CISACyber/status/2059697669157609976)

---

### Netherlands Stark Industries Infrastructure Seizure — Arrests Named: Andrey Nesterenko (MIRhosting, 39, Russian) + Youssef Zinad (WorkTitans BV, 57)
**Previous coverage:** 2026-05-26 (BleepingComputer initial server-seizure note) + 2026-05-28 (Krebs Stark Industries piece); **Previous threat_score:** 5

Krebs follow-up names the two arrested operators behind the 800+ servers seized 2026-05-27 across five Netherlands locations (three Enschede/Almere business sites + Dronten and Schiphol-Rijk data centers): **Andrey Nesterenko (39, Russian, operator of MIRhosting)** and **Youssef Zinad (57, Amsterdam, controller of WorkTitans BV)**. The two also control `the[.]hosting`, the entity created after PQHosting was sanctioned (PQHosting was the Moldovan Neculiti brothers' operation, sanctioned May 2025). Stark Industries Solutions used MIRhosting/WorkTitans infrastructure for the pro-Russian Danish-municipal-election attacks 2025-11-13 → 19. **Material change:** named arrests + corporate-structure mapping + PQHosting lineage confirms a single contiguous bulletproof-hosting cluster spanning sanctioned-Moldovan → sanctioned-Russian Dutch fronts.

**New threat_score:** 5 (named arrests are useful attribution but not a defensive action item).

**Sources:** [KrebsOnSecurity](https://krebsonsecurity.com/2026/05/netherlands-seizes-800-servers-arrests-2-for-aiding-cyberattacks/)

---

## 📋 Noted / Monitoring

**Apache Ignite CVE-2025-48977** — REST HTTP default-configuration arbitrary file read (oss-security 2026-05-28). Monitor for unauth-RCE escalation given Ignite's typical internal-network deployment posture.

**Apache Artemis/ActiveMQ CVE-2026-40914** — STOMP protocol handler can modify address routing-type (oss-security 2026-05-27). Likely a multi-tenant authz boundary issue rather than RCE.

**CryptX <0.088_001 CVE-2026-41565** — Stack buffer overflow in four AEAD `decrypt_verify` helpers (oss-security 2026-05-28). Used in Perl crypto stack; track for Perl ecosystem batch absorption.

**Mojolicious::Plugin::Statsd ≤0.04 CVE-2026-46740** — Metric injection (oss-security 2026-05-28). Continues the long-tail Perl/CPAN ecosystem batch pattern.

**Plack::Middleware::Security::Common <0.13.1 CVE-2026-9658** — Header injection in request processing (oss-security 2026-05-28). Perl PSGI middleware, niche.

**Crypt::ScryptKDF ≤0.010 CVE-2026-8647** — Insecure RNG fallback when CSPRNG modules unavailable (oss-security 2026-05-26). Quietly weakens KDF strength.

**Open Babel 3.2.0 — 24 CVEs in file-format parsers** (oss-security 2026-05-28). Open-source chemistry data toolkit; primarily client-side parsing, OOS for Watchtower unless exposed via SaaS file-conversion endpoints.

**qSnapper D-Bus CVE-2026-41045/41046/41047/41048** — Privileged D-Bus service issues on Linux (oss-security 2026-05-26). Local-only, OOS.

**CIFSwitch local root via cifs-utils forged spnego upcall** (oss-security 2026-05-28). Linux LPE, OOS but worth absorbing if container-escape primitive emerges.

**OpenStack Keystone credential-delegation / authorization bypass** + **OpenStack Neutron tagging-policy bypass** (oss-security 2026-05-28). Multi-tenant cloud platform authz bugs; impact depends on tenant model.

**Microsoft "slams" Chaotic Eclipse / Nightmare-Eclipse — GitHub + GitLab account removals (THN 2026-05-28)** — Coverage refers to already-disclosed BlueHammer (CVE-2026-33825, KEV April 2026) + RedSun (CVE-2026-41091, KEV 2026-05-20) + UnDefend (CVE-2026-45498, KEV 2026-05-20) + YellowKey/GreenPlasma/MiniPlasma (MEMORY 2026-05-15/18). No new vulnerability; disclosure-policy drama only.

**TinyMCE CVE-2026-47759** — Stored XSS in widely-deployed WYSIWYG editor (CVSS 8.7, PT-2026-44388, dbugs 2026-05-28). Client-side script-context, but TinyMCE is embedded in many SaaS admin panels — monitor for escalation reports.

**Nautobot CVE-2026-44798 (NVD published 2026-05-28)** — Already noted 2026-05-14; NVD HIGH-severity assignment confirms tier but is not material change.

**FBI fake-FIFA World Cup fraud sites warning (BleepingComputer 2026-05-28)** — Consumer-fraud alert; defensive interest only as a phishing-lure-watchlist input.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | BleepingComputer, The Hacker News, SecurityWeek, KrebsOnSecurity, Schneier | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited (via secondary reporting) | ⚠️ |
| Vendor advisories | Fortinet (via THN), Veeam KB4853, MSRC (no content) | ⚠️ |
| Research / OSINT | GitHub Security Lab, Rapid7 (Gogs), Project Zero, Cloudflare, avleonov, 0xMarcio/cve | ✅ |
| Vulnerability DBs | OpenCVE, NVD, dbugs.ptsecurity.com, CERT/CC kb.cert.org, oss-security openwall | ✅ |
| Mailing lists | seclists/fulldisclosure, oss-security openwall | ✅ |
| Russian-language | habr/tomhunter (stale to March), teletype/cyberok (stale to February) | ⚠️ |
| Other | packetstorm.news (redirect, limited enum), cert.gov.ua (no content) | ⚠️ |

**Errors:** cisa.gov + cisa.gov/known-exploited-vulnerabilities-catalog (403 Forbidden via WebFetch — covered via THN/Krebs/BleepingComputer relay); attackerkb.com (403); msrc.microsoft.com/blog (empty); hackerone.com/hacktivity (JS-required); bugcrowd.com/disclosures (404); cve.org + cve.mitre.org (JS-required); cert.gov.ua (no content extractable).

**Degraded:** packetstormsecurity.com (redirect to packetstorm.news, advisory enum requires deep navigation not possible via WebFetch); habr/tomhunter (no May 2026 content); teletype/cyberok (no May 2026 content).

**CISA KEV:** 3 supply-chain additions confirmed 2026-05-27 (CVE-2026-8398 DAEMON Tools, CVE-2026-45321 TanStack, CVE-2026-48027 Nx Console) — all promoted to today's News/Update sections. No new additions identified for 2026-05-28 or 2026-05-29.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-29/night | Next: 2026-05-30/night*
