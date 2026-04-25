# Watchtower Night Report — 2026-04-25
**Cycle:** Night | **Generated:** 2026-04-25 03:30 UTC (2026-04-25T03:30:00Z)
**Sources checked:** 19/30 | **CISA KEV new additions:** 4 (April 24)

---

## 🟠 HIGH

### Samsung MagicINFO + SimpleHelp Added to CISA KEV — Three Enterprise RCE/Path Traversal Flaws Under Active Exploitation
**Product:** Samsung MagicINFO 9 Server (≤21.1050); SimpleHelp RMM (≤5.5.7) | **CVE:** CVE-2024-7399, CVE-2024-57726, CVE-2024-57728 | **CVSS:** 8.8 / 9.9 / 7.2 | **First reported:** 2026-04-24

CISA added four vulnerabilities to the Known Exploited Vulnerabilities catalog on April 24. Three are widely deployed enterprise-facing services. **CVE-2024-7399** is an unauthenticated path traversal in Samsung MagicINFO 9 Server that allows JSP file upload and arbitrary code execution as system; PoC code became public last week and SANS ISC plus Arctic Wolf have observed Mirai botnet operators using the flaw to recruit MagicINFO servers as bots. **CVE-2024-57726** and **CVE-2024-57728** are a pair of SimpleHelp RMM flaws (privilege escalation via API key forgery, plus zip-slip path traversal to RCE) that initial access brokers and ransomware affiliates have been chaining since early 2025; SimpleHelp is heavily used by managed service providers, so a single SimpleHelp compromise typically cascades into multiple downstream customer networks. The fourth KEV addition, CVE-2025-29635 (D-Link DIR-823X), is covered as an update below.

**Timeline:** Samsung patched MagicINFO in August 2024; SimpleHelp 5.5.8 shipped early 2025. Both have been intermittently exploited but reached the CISA bar this week. PoC for CVE-2024-7399 published April 2026 triggered the Mirai campaign.

**Why it matters:** MagicINFO is internet-exposed across retail, hospitality, transit and corporate signage estates — a public-facing surface most security teams under-track. SimpleHelp is a privileged admin tool with reach into every environment it manages; one unpatched server is sufficient to compromise dozens of MSP downstream customers, the same pattern that drove the Kaseya 2021 incident.

**Mitigation:**
- Samsung MagicINFO: Upgrade to v21.1051 or later. Ensure WAF rules block JSP uploads to non-allowlisted paths. Hunt for unexpected `.jsp` files under MagicINFO web roots.
- SimpleHelp: Upgrade to 5.5.8 or later. Audit API keys created by non-admin accounts. Inspect upload directories for unusual zip-derived files. Review SimpleHelp logs for technician account elevation events.
- Treat any SimpleHelp instance as critical infrastructure: restrict management plane to VPN, enable MFA on all technician accounts, rotate all stored credentials.
- CISA federal patch deadline for these KEVs is May 15, 2026 — applicable to FCEB agencies but a useful private-sector benchmark.

**Sources:** [BleepingComputer — Samsung MagicINFO 9 Server RCE flaw now exploited in attacks](https://www.bleepingcomputer.com/news/security/samsung-magicinfo-9-server-rce-flaw-now-exploited-in-attacks/) | [CISA KEV alert](https://www.cisa.gov/news-events/alerts/2026/04/24/cisa-adds-four-known-exploited-vulnerabilities-catalog) | [Arctic Wolf — Campaign Exploiting SimpleHelp RMM](https://arcticwolf.com/resources/blog/arctic-wolf-observes-campaign-exploiting-simplehelp-rmm-software-for-initial-access/) | [Help Net Security — Samsung MagicINFO exploited](https://www.helpnetsecurity.com/2025/05/06/exploited-vulnerability-software-managing-samsung-digital-displays-cve-2024-7399/)

---

## 🟡 MEDIUM

### 🔄 D-Link DIR-823X CVE-2025-29635 Added to CISA KEV — Mirai Campaign Now Federally Mandated
**Product:** D-Link DIR-823X (multiple firmware) | **CVE:** CVE-2025-29635 | **Published:** 2026-04-24 | **Previous score:** 6 | **Current score:** 7

D-Link's command-injection flaw, covered as a News item on April 23 in the context of Nexcorium Mirai exploitation, was added to the CISA KEV catalog on April 24 alongside the Samsung and SimpleHelp additions. Federal patch deadline is May 15. The router is end-of-life in many regions, so the practical answer is replacement, not patching. Increased weight reflects formal KEV status and the deadline pressure on FCEB networks.

**Mitigation:** Replace EOL DIR-823X devices. Where replacement is not yet feasible, take the management plane off the WAN, restrict to LAN-side, and segment any IoT routed through these devices.

**Sources:** [CISA KEV alert](https://www.cisa.gov/news-events/alerts/2026/04/24/cisa-adds-four-known-exploited-vulnerabilities-catalog) | [BleepingComputer — CISA flags new SD-WAN flaw as actively exploited](https://www.bleepingcomputer.com/news/security/cisa-flags-new-sd-wan-flaw-as-actively-exploited-in-attacks/)

---

## 📋 Noted / Monitoring

**Tropic Trooper trojanized SumatraPDF (Zscaler, April 24)** — Chinese-speaking APT (APT23 / Earth Centaur) using military-themed ZIP lures with a backdoored SumatraPDF reader to deploy AdaptixC2 over GitHub C2. Targeted geographic scope and desktop-client delivery vector keeps it out of our News tier, but worth tracking for organizations with PRC-adjacent regional offices.

**CVE-2026-41651 — PackageKit "Pack2TheRoot" LPE** — Cross-distro local privilege escalation via TOCTOU race in PackageKit transaction state machine; 12-year-old bug, all distros (Debian, Ubuntu, Fedora, RHEL) affected. **No remote component**, so out of our standard scope, but operationally relevant for any multi-tenant Linux host. Patched in PackageKit 1.3.5.

**Linux kernel batch — CVE-2026-31584 through CVE-2026-31654 (April 24)** — ~70-CVE bulk disclosure pushed to NVD; CVSS scores not yet populated. Watch for individual high-impact items as scoring lands.

**CVE-2026-41043, CVE-2026-40466 — Apache ActiveMQ** — Two new ActiveMQ CVEs disclosed April 24 (CVSS 6.5 and 8.8). Distinct from CVE-2026-34197 (Jolokia RCE, KEV) but on the same exposed message-broker surface; combine for review.

**CVE-2026-41907 — UUID.js (CVSS 8.1)** — High-severity issue in widely-imported JS library; details pending.

**CVE-2026-23902 — Apache DolphinScheduler (CVSS 8.1)** — Workflow scheduler, sometimes internet-exposed in data-eng pipelines.

**ADT data breach (ShinyHunters, April 24)** — Customer data lost; not a vulnerability but the latest in the ShinyHunters extortion run that has touched Vercel, McGraw-Hill, Infinite Campus and HackerOne in recent reports — same actor cluster.

**Fast16 ICS sabotage malware (April 24)** — Pre-Stuxnet-era industrial sabotage tool surfaces in US-Iran tension reporting. Targets precision-calculation software with self-propagation. Limited deployment scope; ICS/OT shops with Iranian threat exposure should brief.

**108 malicious Chrome extensions (April 24)** — 20K users impacted, harvest Google + Telegram credentials. Browser-extension surface is largely out of our standard scope but enterprise GPO can enforce extension allowlists.

**Apple iOS CVE-2026-28950** — Notification database retains "deleted" Signal messages, allowed FBI iPhone forensic recovery. Mobile-only / out of scope.

**Mythos / Project Glasswing** — Anthropic's restricted internal model finds vulnerabilities at scale (271 in Firefox, more in OS kernels). Methodology disclosure rather than a defensive item; track for false-positive rate transparency.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com, schneier.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (403, used THN/BC for KEV data) |
| Vendor advisories | msrc.microsoft.com, fortinet.com/blog/threat-research | ❌ / ⚠️ |
| Research / OSINT | securitylab.github.com, seclists.org/fulldisclosure, kb.cert.org/vuls, avleonov.com, schneier.com | ✅ |
| CVE databases | app.opencve.io, dbugs.ptsecurity.com, github.com/0xMarcio/cve, github.com/search | ✅ |
| Cloud / vendor blogs | blog.cloudflare.com/tag/security, rapid7.com | ✅ / ⚠️ |
| Bug bounty | hackerone.com/hacktivity, bugcrowd.com/disclosures, attackerkb.com | ❌ (JS/404/403) |
| Russian / non-English | habr.com, teletype.in/@cyberok, cert.gov.ua | ⚠️ (no recent posts / no extract) |
| Authoritative DBs | nvd.nist.gov, cve.org, cve.mitre.org | ❌ (JS / no API extract) |
| Research labs | googleprojectzero.blogspot.com (now projectzero.google), packetstormsecurity.com (now packetstorm.news) | ❌ / ⚠️ |

**Errors:** cisa.gov + cisa.gov/known-exploited-vulnerabilities-catalog (403); attackerkb.com (403); bugcrowd.com/disclosures (404); hackerone.com/hacktivity (JS); cve.org, cve.mitre.org (JS); googleprojectzero.blogspot.com (404 on /2026 path); nvd.nist.gov (no API extract via fetch); msrc.microsoft.com (no extract); opencve.io (marketing only — used app.opencve.io); cert.gov.ua (no extract).
**CISA KEV:** 4 new additions on 2026-04-24 (Samsung MagicINFO CVE-2024-7399, SimpleHelp CVE-2024-57726/57728, D-Link DIR-823X CVE-2025-29635). Federal patch deadline May 15, 2026.

---

*Watchtower vulnerability-researcher | Cycle: 2026-04-25/night | Next: 2026-04-26/night*
