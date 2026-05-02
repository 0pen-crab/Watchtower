# Watchtower Night Report — 2026-05-02
**Cycle:** Night | **Generated:** 2026-05-02 00:30 UTC (2026-05-02T00:30:00Z)
**Sources checked:** 22/30 | **CISA KEV total:** unreachable (cisa.gov 403) | **New KEV additions:** none confirmed since 2026-04-29

---

## 🔴 CRITICAL

*No new CRITICAL items today. Yesterday's CRITICAL set (cPanel CVE-2026-41940 commodity-PoC update, Mini Shai-Hulud PyTorch Lightning expansion, Gemini CLI CVSS 10, MOVEit Automation CVE-2026-4670/5174) all remain the highest defensive priorities — see 2026-05-01 entry. The 24-hour news cycle into 2026-05-02 was comparatively quiet on patch-now items.*

---

## 🟠 HIGH

### SHADOW-EARTH-053 — China-Aligned Espionage Campaign Exploiting N-Day Microsoft Exchange + IIS Across Asia and Poland
**Product:** Microsoft Exchange Server (ProxyLogon-class chain), Microsoft IIS, Linux servers via CVE-2025-55182 (React2Shell) | **CVE:** ProxyLogon (CVE-2021-26855 chain referenced generically), CVE-2025-55182 | **Threat score:** 6 | **First reported:** 2026-05-01

A China-aligned espionage cluster tracked as SHADOW-EARTH-053 has been running an active, multi-month campaign against government and defense organisations in Pakistan, Thailand, Malaysia, India, Myanmar, Sri Lanka, and Taiwan, plus one NATO member (Poland). The intrusion chain is the well-worn but still-effective "patch the perimeter and they walk in" pattern: SHADOW-EARTH-053 scans for unpatched, internet-facing Microsoft Exchange and IIS servers and exploits N-day vulnerabilities — the ProxyLogon chain is named explicitly, and CVE-2025-55182 (React2Shell) is used for Linux pivots — to drop Godzilla web shells, then DLL-side-loads ShadowPad implants for persistence. Post-exploitation tooling: AnyDesk for hands-on-keyboard, Mimikatz for credential dumping, Sharp-SMBExec for lateral movement, IOX/GOST/Wstunnel for tunnelling. Researchers found that nearly half of victims in Malaysia, Sri Lanka, and Myanmar were also being worked by a related group (SHADOW-EARTH-054), suggesting parallel collection ops on the same target set.

**Why it matters:** Our scope contains Exchange and IIS by default. Even if your perimeter is patched, this campaign is an operational reminder that 2021-era ProxyLogon and similar Exchange-chain CVEs are still being weaponised against unpatched edge mailservers in 2026; any forgotten on-prem Exchange node — common in M&A-acquired subsidiaries, lab environments, or "we'll migrate next quarter" backlogs — is a viable initial-access vector for a state-aligned actor. The Polish targeting is also the operational signal that this campaign is not strictly Asia-focused — NATO members are in the threat aperture.

**Discovered by:** Trend Micro Threat Intelligence (campaign attribution and SHADOW-EARTH-053 / 054 cluster naming).

**Mitigation:**
- Re-audit the inventory of internet-reachable Exchange and IIS hosts; confirm the full ProxyLogon / ProxyShell / ProxyNotShell patch chain is applied (CVE-2021-26855, CVE-2021-26857, CVE-2021-26858, CVE-2021-27065 baseline).
- Patch CVE-2025-55182 (React2Shell) on any affected Linux deployments — this CVE is being actively used as a Linux-side initial-access vector by this group.
- Hunt for Godzilla web shell artifacts on Exchange and IIS (.aspx anomalies, suspicious child processes of `w3wp.exe` / `umworkerprocess.exe`).
- Detect ShadowPad's typical DLL side-loading pattern: legitimate signed binaries in unusual paths loading unsigned companion DLLs. AnyDesk in non-IT environments is a high-value detection.
- Tunnel-tool egress hunt for IOX, GOST, and Wstunnel default beacon patterns; any persistent outbound from Exchange to non-business IPs warrants triage.

**Sources:** [The Hacker News — China-Linked Hackers Target Asian Governments](https://thehackernews.com/2026/05/china-linked-hackers-target-asian.html) | [SecurityWeek — Sophisticated Deep#Door Backdoor Enables Espionage](https://www.securityweek.com)

---

### BlackFile / Cordial Spider + Snarky Spider — UPDATE: Attribution Confirmed and AiTM SSO Mechanics Now Public (Threat score 7, previously 7)
**Product:** Google Workspace, Microsoft SharePoint, HubSpot, Salesforce — accessed via compromised IdP / SSO credentials | **CVE:** None | **Threat score:** 7 (unchanged) | **First reported:** 2026-04-26

The retail/hospitality vishing campaign Watchtower covered as BlackFile on 2026-04-26 has been attributed to two distinct e-crime clusters — Cordial Spider (BlackFile, CL-CRI-1116, O-UNC-045, UNC6671) and Snarky Spider (O-UNC-025, UNC6661) — both linked to "The Com" e-crime ecosystem and active since October 2025. Today's reporting fills in the technical mechanics: vishing impersonates IT to lure the victim onto an attacker-controlled SSO login page; an adversary-in-the-middle (AiTM) phishing proxy captures the user's password and MFA code in real time; the attacker registers a new MFA device, removes the legitimate one, and creates inbox rules to suppress the email notifications that normally accompany those changes; the attacker then scrapes the corporate directory to identify privileged accounts, pivots into Salesforce / HubSpot / SharePoint / Workspace, and exfiltrates business-critical files — sometimes within the first hour of initial access. Both groups operate "almost exclusively within trusted SaaS environments" using residential proxies to look like the victim's own user.

**Why this is an update vs. the 2026-04-26 News:** trigger is "technical detail newly published" — attribution to two named e-crime clusters and the full AiTM-MFA-bypass mechanic were not in the original advisory. Threat score stays at 7 because the campaign was already understood to have material business-impact potential; the change is operational visibility, not severity escalation.

**Mitigation (incremental):**
- Move IdP/SSO logins behind FIDO2 / phishing-resistant MFA wherever possible — SMS- and TOTP-MFA are bypassable via this exact AiTM proxy pattern.
- Alert on MFA device additions paired with deletions of the prior device within the same session (the attacker's blind-MFA-rotation tell).
- Alert on new inbox rules that filter, forward, or delete identity / security notification emails — a near-deterministic signal of post-AiTM persistence.
- Tighten SaaS audit-log monitoring: bulk file downloads from Salesforce / SharePoint / HubSpot / Workspace by accounts that are normally read-only, especially from residential-proxy IP ranges, should page the SOC.
- Train front-line IT helpdesk on the impersonation pattern: any inbound caller asking the helpdesk to enrol a new MFA device must trigger out-of-band verification.

**Sources:** [The Hacker News — Cybercrime Groups Using Vishing and SSO Abuse in Rapid SaaS Extortion](https://thehackernews.com/2026/05/cybercrime-groups-using-vishing-and-sso.html) | [Watchtower 2026-04-26 — original BlackFile entry](../../04/26/report.md)

---

## 🟡 MEDIUM

*No new MEDIUM items today.*

---

## 📋 Noted / Monitoring

**CVE-2026-31431 (Linux "Copy Fail" `algif_aead` LPE) — PoC sprawl exploded from ≥6 to 168 repos in 24h** — Out-of-remote-services scope (still LPE only), but the PoC-repo count went from "≥6 in past hour" yesterday to **168 repositories** searchable on GitHub today, including five fresh exploit implementations updated within the last hour (Rust, C, Python, Zig, Go variants) plus defensive tooling (BPF LSM blocker `atgreen/block-copyfail`, Ansible remediation, scanner inventory tools). Every Linux server / CI runner / jump host on a kernel since 4.14 (Aug 2017) is in scope. Schedule the kernel update window now — patched in 5.10.254+, 5.15.204+, 6.1.170+, 6.6.137+. Do not promote to a full Update because the bug remains pure LPE (no remote component); but the operational urgency on internal infra has materially increased.

**Mini Shai-Hulud `/proc/<pid>/mem` secret-extraction technique** — Today's BleepingComputer follow-up on yesterday's Mini Shai-Hulud SAP CAP / PyTorch Lightning campaign disclosed an additional technique not in earlier reporting: the worm reads `/proc/<pid>/maps` and `/proc/<pid>/mem` for the GitHub Actions `Runner.Worker` process and extracts every `key=value` secret directly from runner memory, bypassing the GitHub Actions log-masking that normally redacts secrets. Defenders running self-hosted GitHub Actions or any container CI must assume that any compromised job has had every secret in process memory exfiltrated — token rotation guidance from yesterday's entry remains; this is purely an additional detection / IR signal, not a new severity. Track the `/proc/*/maps` + `/proc/*/mem` read pattern as a worm IOC on CI runners.

**Instructure (Canvas LMS) cyber incident** — Disclosed 2026-05-01; no scope, no attribution, no root cause yet ("actively investigating with outside forensics"). Instructure's prior 2025 incident (social engineering → Salesforce data, ShinyHunters) is the relevant comparison. Universities and K-12 districts using Canvas should brief their IR teams and pre-position log-collection in case Canvas data flows downstream into student-facing systems. Will promote to a full entry once technical detail or scope is published.

**SHADOW-EARTH-053 sister-cluster SHADOW-EARTH-054** — Co-victimisation noted in the same Trend Micro report; nearly half of Malaysian, Sri Lankan, and Myanmar SHADOW-EARTH-053 victims also showed SHADOW-EARTH-054 implants. Treat as the same threat aperture for IR purposes.

**Deep#Door Python backdoor framework** — SecurityWeek 2026-05-01 reported a new sophisticated Python-based backdoor deploying persistent Windows implants for espionage; full advisory text was 403 to direct fetch (paywall/CDN). No CVE, no specific delivery vector confirmed in available coverage. Track for vendor advisories or YARA rules in the next 48h.

**AccountDumpling Facebook phishing-via-Google-AppSheet (≈30,000 accounts compromised)** — Out of corporate-infrastructure scope; primarily a consumer Facebook attack and a research curiosity around phishing infrastructure abusing Google AppSheet (`noreply@appsheet.com`), Netlify, Vercel, and Google Drive. Brief anti-phishing detection if your SOC tracks consumer-side abuse for typosquat / brand-impersonation reasons; otherwise informational.

**CVE-2026-7546 (Totolink NR1800X lighttpd `find_host_ip` stack overflow, CVSS 9.3)** — Pre-auth RCE via `Host:` header overflow on Totolink consumer routers; PoC public, no vendor patch. Niche IoT / SOHO router population; relevant only if you have Totolink in your fleet (uncommon in enterprise).

**CVE-2026-7538 (Totolink A8000RU, CVSS 10.0) and CVE-2026-7548 (Totolink NR1800X, CVSS 9.0)** — Two more Totolink consumer router CVEs published 2026-05-01; same niche population as 7546.

**CVE-2026-7567 (WordPress Temporary Login plugin, CVSS 9.8)** — WordPress plugin authentication flaw. Worth checking your plugin inventory for "Temporary Login" / "Temporary Login Without Password"; not a top-tier WordPress plugin by install base, but a 9.8 score with public details.

**CVE-2026-42473 (Mixphp Framework, CVSS 9.8)** — Niche Chinese PHP framework; very small deployment footprint outside its origin region. Mention for completeness.

**CVE-2026-7590 (Branch Monkey MCP server, CVSS 7.5) and CVE-2026-7591 (Astro MCP server, CVSS 6.5)** — Two more MCP-server CVEs published 2026-05-01, continuing the MCP-server-as-attack-surface trend (mcp-atlassian, nginx-ui, OpenHarness, chatgpt-mcp-server, Intina47 context-sync earlier this cycle). Niche right now but the pattern is durable — add MCP-server inventory to internal AppSec tracking.

**15-year-old detained for French govt agency (France Titres / ANTS) data breach** — Operational/judicial item; the underlying breach is what produced the resold data. Brief reference for IR-pattern reading on minor-attribution.

**US ransomware negotiators (Goldberg + Martin) sentenced to 4 years for BlackCat/ALPHV insider attacks** — Judicial/insider-threat reference; useful for IR-program insider-risk policy work, no new defensive action.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (403) |
| Vendor advisories | rapid7.com, fortinet.com/blog/threat-research, msrc.microsoft.com/blog | ✅ / ⚠️ / ⚠️ |
| Research / OSINT | schneier.com, krebsonsecurity.com, googleprojectzero.blogspot.com, securitylab.github.com | ✅ / ⚠️ / ⚠️ / ⚠️ |
| CVE feeds | opencve.io, nvd.nist.gov, cve.org, cve.mitre.org, kb.cert.org/vuls | ✅ / ⚠️ / ❌ / ❌ / ✅ |
| GitHub / PoC | github.com/search, github.com/0xMarcio/cve | ✅ |
| Disclosure programs | hackerone.com/hacktivity, bugcrowd.com/disclosures, seclists.org/fulldisclosure | ❌ / ❌ / ✅ |
| Russian-language | dbugs.ptsecurity.com, avleonov.com, habr.com/ru/companies/tomhunter, teletype.in/@cyberok | ✅ / ⚠️ / ⚠️ / ⚠️ |
| Other | attackerkb.com, packetstormsecurity.com, blog.cloudflare.com/tag/security, cert.gov.ua | ❌ / ⚠️ / ⚠️ / ❌ |

**Errors:** cisa.gov + KEV (403), attackerkb.com (403), bugcrowd.com/disclosures (404), hackerone.com/hacktivity (JS-only, empty), cve.org (JS-only, empty), cve.mitre.org (redirects to cve.org, JS-only), cert.gov.ua (no content returned)
**Degraded (returned content but no recent / relevant data):** fortinet.com/blog/threat-research (latest 2026-04-17), securitylab.github.com (latest 2026-04-24), googleprojectzero.blogspot.com → projectzero.google (latest 2026-03-05), packetstorm.news (homepage only — feedback-page data only), msrc.microsoft.com/blog (navigation only), avleonov.com (latest 2026-04-22), habr.com/ru/companies/tomhunter (latest 2026-03-06), teletype.in/@cyberok (latest 2026-02-04), nvd.nist.gov (search UI not directly fetchable, used opencve.io instead), blog.cloudflare.com/tag/security (latest 2026-04-30, no security posts today)
**CISA KEV:** No new KEV additions confirmed via THN / SecurityWeek / Krebs / BleepingComputer in the past 24h. Yesterday's additions (CVE-2024-1708 ConnectWise ScreenConnect, CVE-2026-32202 Windows Shell) remain the latest known entries.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-02/night | Next: 2026-05-03/night*
