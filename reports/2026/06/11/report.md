# Watchtower Night Report — 2026-06-11
**Cycle:** Night | **Generated:** 2026-06-11 00:14 UTC (2026-06-11T00:14:00Z)
**Sources checked:** 22/30 | **CISA KEV total:** 3 new additions 2026-06-09 | **New KEV additions:** CVE-2026-20245 (Cisco SD-WAN Manager), CVE-2026-11645 (Chrome V8 — browser-scope OOS), CVE-2026-7473 (Arista EOS)

---

## 🔴 CRITICAL

### Langflow CVE-2026-5027 — Unpatched Path-Traversal + Default Auto-Login → Unauthenticated RCE; Active Exploitation Observed (CVSS 8.8)
**Product:** Langflow (open-source LangChain workflow IDE) ≤ 1.8.4 | **CVE:** CVE-2026-5027 | **Status:** 0-Day (Unpatched) — Active Exploitation

The POST `/api/v2/files` endpoint does not sanitize the `filename` parameter from multipart form data, allowing path-traversal arbitrary file writes outside the upload directory. Because Langflow ships with **auto-login enabled by default**, a single unauthenticated request is sufficient to obtain a valid session token before file-write — chaining directly to RCE on the Langflow host. Tenable Research (TRA-2026-26) disclosed publicly on 2026-03-27 after three unanswered vendor contacts in Jan/Feb 2026. As of 2026-06-10, exploitation in the wild has been observed (test-file writes preceding full RCE attempts) against approximately **7,000 internet-exposed Langflow instances** per Censys, majority in North America.

**Timeline:** Tenable vendor-contact Jan/Feb 2026 → CVE-2026-5027 published 2026-03-27 (Tenable advisory) → CISA / mainstream pickup 2026-06-10 with active-exploitation evidence → still unpatched 2026-06-11.

**Why it matters:** This is the second active-exploitation Langflow disclosure in three months (after CVE-2025-34291 added to KEV with MuddyWater attribution per Watchtower 2026-05-23), confirming the durable pattern that self-hosted AI workflow platforms with default-no-auth posture are first-class state-actor and opportunistic initial-access surfaces. ~7K exposed instances is a large opportunistic target pool.

**Discovered by:** Tenable Research (TRA-2026-26)

**Mitigation:**
- Remove Langflow from internet-facing exposure today; firewall to internal management network only
- Disable auto-login (`LANGFLOW_AUTO_LOGIN=False`) and require an authenticated proxy/VPN layer
- If Langflow must remain reachable, front it with a reverse proxy enforcing strict auth + URL pattern restrictions (deny `/api/v2/files` from untrusted networks)
- Audit the Langflow host filesystem for unexpected files written under user-controlled paths
- Block known Tenable-published Langflow exploitation IOCs at egress and on WAF

**Sources:** [The Hacker News — Unpatched Langflow Flaw CVE-2026-5027 Exploited for Unauthenticated RCE](https://thehackernews.com/2026/06/unpatched-langflow-flaw-cve-2026-5027.html) | [Tenable TRA-2026-26](https://www.tenable.com/security/research/tra-2026-26) | [BleepingComputer 2026-06-10](https://www.bleepingcomputer.com/news/security/)

---

### Cisco Catalyst SD-WAN Manager CVE-2026-20245 — KEV-Added 2026-06-09 With 13-Day Federal Deadline; Confirms Active Exploitation of Unpatched Root-RCE Zero-Day (UPDATE, prev score 8 → 9)
**Product:** Cisco Catalyst SD-WAN Manager (vManage) | **CVE:** CVE-2026-20245 | **CVSS:** 7.8 | **First reported:** 2026-06-05

Originally newsed by Watchtower 2026-06-06 as an emergency Cisco advisory for an unpatched zero-day yielding root command execution on the SD-WAN control plane. CISA added CVE-2026-20245 to the Known Exploited Vulnerabilities catalog on 2026-06-09 with a 13-day FCEB deadline of **2026-06-23**, alongside two other adds (Chrome V8 CVE-2026-11645 and Arista EOS CVE-2026-7473). KEV inclusion formalises active in-the-wild exploitation. Cisco still ships no patch — only hardening guidance — so the operational posture is unchanged but the urgency tier moves up. Seventh SD-WAN zero-day Cisco has confirmed in 2026 (joining CVE-2026-20127 KEV, CVE-2026-20182 + four earlier).

**Mitigation:**
- Apply Cisco's published hardening guidance for vManage / Catalyst SD-WAN Manager today
- Audit perimeter exposure of vManage `/dataservice` URLs — restrict to internal management network only
- Audit access logs and command-execution telemetry on Catalyst SD-WAN Manager hosts for IOC patterns consistent with the Cisco advisory
- For FCEB / FCEB-equivalent customers: comply with the 2026-06-23 KEV deadline

**Sources:** [The Hacker News — CISA Adds Cisco, Chrome, and Arista Flaws to KEV](https://thehackernews.com/2026/06/cisa-adds-cisco-chrome-and-arista-flaws.html) | [CISA Alert 2026-06-09](https://www.cisa.gov/news-events/alerts/2026/06/09/cisa-adds-three-known-exploited-vulnerabilities-catalog)

---

### Ivanti Sentry CVE-2026-10520 (CVSS 10.0) Unauthenticated Pre-Auth Root RCE + CVE-2026-10523 (CVSS 9.9) Auth-Bypass Admin Creation — Vendor Advisory + watchTowr PoC Published 2026-06-09/10 (UPDATE from 2026-06-10 NOTED, prev score 3 → 9)
**Product:** Ivanti Sentry (mobile-gateway) 10.5.1, 10.6.1, 10.7.0 and earlier | **CVE:** CVE-2026-10520, CVE-2026-10523 | **Status:** Patched 10.5.2 / 10.6.2 / 10.7.1, Public PoC, No In-Wild Yet

CVE-2026-10520 is an unauthenticated OS-command-injection in the `/mics/api/v2/sentry/mics-config/handleMessage` endpoint — a crafted HTTP request is interpreted as a MICS configuration command and executed by the backend `handleExecute()` routine, yielding root RCE without auth. CVE-2026-10523 is a paired authentication-bypass that lets an unauthenticated attacker create administrator accounts. Ivanti published the advisory 2026-06-09 with fixes in Sentry 10.5.2 / 10.6.2 / 10.7.1; watchTowr published a working PoC for CVE-2026-10520 on 2026-06-10 — promoting yesterday's NOTED entry (which had only the PT-Security indexing of CVE-2026-10523 without public technical detail) to a full UPDATE now that the unauth-RCE chain and PoC are public.

**Timeline:** PT-Security dbugs index of CVE-2026-10523 2026-06-09 (yesterday's NOTED, no public detail) → Ivanti advisory + patches 2026-06-09 → watchTowr PoC for CVE-2026-10520 (root RCE chain) 2026-06-10 → Watchtower promotion 2026-06-11.

**Why it matters:** Ivanti Sentry has prior CISA KEV history (multiple in 2023), exploitation is trivial with the PoC, and Sentry sits at the edge of enterprise mobile / EMM environments — expect KEV add within 72h and ransomware-affiliate uptake within 14d. Lack of confirmed in-wild today does not buy meaningful patch slack.

**Mitigation:**
- Patch to Sentry 10.5.2 / 10.6.2 / 10.7.1 today
- Audit access logs for HTTP requests to `/mics/api/v2/sentry/mics-config/handleMessage` since 2026-06-09
- Audit Sentry admin-account creation events for anomalous new accounts
- Restrict Sentry MICS API exposure to internal management networks pending patch deployment

**Sources:** [Rapid7 ETR — Ivanti Sentry CVE-2026-10520/10523](https://www.rapid7.com/blog/post/etr-cve-2026-10520-cve-2026-10523-multiple-critical-vulnerabilities-affecting-ivanti-sentry/) | [Help Net Security 2026-06-10](https://www.helpnetsecurity.com/2026/06/10/ivanti-sentry-cve-2026-10520-cve-2026-10523/) | [The Register](https://www.theregister.com/patches/2026/06/10/ivanti-urges-sentry-users-to-patch-two-critical-bugs/5253428) | [SOCRadar](https://socradar.io/blog/ivanti-sentrys-cve-2026-10520-rce/)

---

## 🟠 HIGH

### Arista EOS CVE-2026-7473 — Tunnel-Traffic Comparison Bypass Actively Exploited, Added to CISA KEV 2026-06-09; Arista Says NO Patches Planned
**Product:** Arista EOS on 7020R, 7280R/R2, 7500R/R2 series | **CVE:** CVE-2026-7473 | **CVSS:** 6.9 | **First reported:** 2026-06-09

Incomplete-comparison-with-missing-factors vulnerability in tunnel-traffic processing causes EOS to forward non-configured tunnel traffic on the affected router series — exploitable for ACL / segmentation bypass and tunnel-traffic interposition. CISA added to KEV 2026-06-09 with FCEB deadline 2026-06-23 confirming in-wild exploitation. Arista has **formally declined to ship a patch**, citing the risk that fixing the comparison could break existing customer configurations on deployed devices. The recommended mitigation is upstream-ACL filtering — operationally painful and easy to misconfigure.

**Mitigation:**
- Deploy ACLs on upstream-of-affected and on-affected Arista devices per the CISA / Arista guidance to deny non-configured tunnel traffic from reaching the affected interfaces
- Audit BGP / overlay topologies for unintended tunnel reachability
- For FCEB customers: comply with 2026-06-23 deadline
- For corporate carrier-grade fleets: consider whether the 7020R / 7280R / 7500R series should be in scope for accelerated refresh given Arista's no-patch posture

**Sources:** [SecurityWeek — No Patch Planned for Exploited Arista EOS Vulnerability](https://www.securityweek.com/no-patch-planned-for-exploited-arista-eos-vulnerability/) | [CISA Alert 2026-06-09](https://www.cisa.gov/news-events/alerts/2026/06/09/cisa-adds-three-known-exploited-vulnerabilities-catalog) | [The Hacker News](https://thehackernews.com/2026/06/cisa-adds-cisco-chrome-and-arista-flaws.html)

---

### Oracle PeopleSoft Mass-Extortion Campaign — ShinyHunters Claims Data Theft From 300 Instances Across 100+ Organisations Via 'Gadget Chain of Old + Zero-Day' Vulnerabilities
**Product:** Oracle PeopleSoft (HR / payroll / finance / SCM / student admin) | **CVE:** Multiple (chain of older PeopleSoft CVEs + undisclosed zero-day primitives) | **First reported:** 2026-06-10

ShinyHunters confirmed to BleepingComputer 2026-06-10 they have breached approximately **300 PeopleSoft instances across 100+ organisations** in an ongoing data-theft + extortion campaign. The group describes their exploitation chain as a 'gadget chain' combining older PeopleSoft CVEs with one or more undisclosed zero-day primitives. The campaign is weighted toward the **education sector** with many previously-extorted victims being re-targeted — Nottingham University publicly confirmed today their PeopleSoft data is already on the ShinyHunters leak site. ShinyHunters' stated initial goal was breaching an FBI PeopleSoft portal (unsuccessful) which provides the timeline grounding. This continues ShinyHunters' 2025-2026 cadence of targeting Oracle business software (NetSuite April 2026, SuiteCRM July 2025).

**Why it matters:** PeopleSoft is widely deployed at universities, government, and large enterprises with substantial PII / financial data; the 'gadget chain' framing implies any unpatched 2024-2025 CPU advisories are exploitation-viable today. The education-sector concentration suggests opportunistic CPU-lag exploitation rather than targeted zero-day burn, but the zero-day component limits the protection patching alone provides.

**Mitigation:**
- Inventory all PeopleSoft instances — internet-facing and internal — and confirm 2024 / 2025 Oracle CPU advisories are fully applied (especially July 2024 CPU which had multiple critical PeopleSoft items)
- For internet-facing PeopleSoft UI / IB endpoints: deploy WAF rules tuned for known PeopleSoft RCE patterns, monitor for outbound data egress from PeopleSoft servers
- Audit PeopleSoft user / privilege creation and ad-hoc-query usage for last 30 days
- Verify backup integrity and offline-copy availability of PeopleSoft databases
- Review whether PeopleSoft really needs internet exposure or whether a VPN / Zero Trust front is feasible

**Sources:** [BleepingComputer — Oracle PeopleSoft servers hacked in ShinyHunters data theft](https://www.bleepingcomputer.com/news/security/oracle-peoplesoft-servers-hacked-in-shinyhunters-data-theft-attacks/) | [TechCrunch — Cybercriminals claim breach of Oracle PeopleSoft at 100+ orgs](https://techcrunch.com/2026/06/10/cybercriminals-claim-breach-of-oracle-peoplesoft-servers-at-100-plus-organizations/) | [CryptoBriefing](https://cryptobriefing.com/shinyhunters-oracle-peoplesoft-bitcoin-ransom/)

---

### Microsoft Exchange Server CVE-2026-42897 OWA XSS — June 2026 Patch Tuesday Ships First Permanent Code Patch After 26 Days of Mitigations-Only Posture (UPDATE, prev score 9 → 8)
**Product:** On-prem Microsoft Exchange Server 2016 / 2019 / Subscription Edition | **CVE:** CVE-2026-42897 | **CVSS:** 8.1 | **First reported:** 2026-05-13

OWA cross-site scripting via crafted email — a recipient opens the message in Outlook Web Access and arbitrary JavaScript executes in their authenticated browser session, enabling session-token theft and mailbox impersonation without touching the Exchange server itself. Watchtower newsed 2026-05-14, updated to score 9 on 2026-05-17 when CISA added to KEV with a 2026-06-06 federal deadline. Microsoft shipped configuration-level mitigations only for 26 days while in-wild exploitation continued, mirroring the ProxyNotShell / ProxyShell operational pain pattern. **June 9 Patch Tuesday provides the first permanent code-level patch.** Score reduces to 8 because patch path is now available, but exploitation activity is unchanged so anything not patched today remains a CVSS 8.1 hostile-mail recipient away from token theft.

**Mitigation:**
- Deploy the June 2026 Exchange Cumulative Update or Security Update to all Exchange 2016 / 2019 / SE hosts immediately
- After patch deployment, remove the temporary OWA configuration mitigations Microsoft published in May 2026
- Audit OWA session-token use for the past 30 days for anomalous IP geographies / device fingerprints
- Force OWA session re-authentication for sensitive mailboxes (executive, finance, IT-admin)

**Sources:** [BleepingComputer — Microsoft patches Exchange Server zero-day](https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-exchange-server-zero-day-exploited-in-attacks/) | [SecurityWeek — Microsoft Warns of Exchange Server Zero-Day](https://www.securityweek.com/microsoft-warns-of-exchange-server-zero-day-exploited-in-the-wild/)

---

### Fortinet FortiSandbox CVE-2026-25089 (CVSS 9.1) — Pre-Auth OS Command Injection via 'Start VNC' Web UI JSON Parameter; Patched 5.0.6 / 4.4.9 (FG-IR-26-141, 2026-06-09)
**Product:** Fortinet FortiSandbox 5.0.0–5.0.5, 4.4.0–4.4.8, 4.2 (all); FortiSandbox Cloud / PaaS 5.0.4–5.0.5 | **CVE:** CVE-2026-25089 | **CVSS:** 9.1 | **First reported:** 2026-06-09

Improper neutralization of OS-command special elements (CWE-78) in the FortiSandbox Web UI 'start VNC' feature — specially-crafted JSON input triggers second-order command injection. Remote, unauthenticated attacker can execute commands on the underlying system via crafted HTTP requests. Internally discovered by Fortinet PSIRT (Adham El Karn) and disclosed 2026-06-09 as FG-IR-26-141. No observed in-wild exploitation yet but Fortinet appliance disclosures have historically seen scanner-template weaponisation within days; FortiSandbox sits inside enterprise security perimeters and a compromise gives attackers a privileged pivot point.

**Mitigation:**
- Upgrade FortiSandbox to 5.0.6 or 4.4.9 (or FortiSandbox Cloud / PaaS 5.0.6) today
- Audit FortiSandbox Web UI access for the 'start VNC' feature usage by unexpected source IPs
- Restrict FortiSandbox management UI exposure to internal management network only (it should never have been internet-facing)
- Retire FortiSandbox 4.2 (end-of-vulnerability-support); upgrade to 4.4 or 5.0 branch

**Sources:** [SecurityWeek — Critical Vulnerabilities Patched in Fortinet, Ivanti Products](https://www.securityweek.com/critical-vulnerabilities-patched-in-fortinet-ivanti-products/) | [Cybersecurity News — Fortinet FortiSandbox Vulnerability](https://cybersecuritynews.com/fortinet-fortisandbox-vulnerability-exploited/) | [Fortinet Advisory FG-IR-26-141](https://www.fortiguard.com/psirt/FG-IR-26-141)

---

## 🟡 MEDIUM

*No standalone medium-severity entries this cycle — see Noted section for the broader patch-cycle batch (Apache OFBiz, Jenkins, ldns DNS-poisoning, Apache Answer, OpenSSL amplification, ImageMagick).*

---

## 📋 Noted / Monitoring

**Apache OFBiz CVE-2026-47342 + CVE-2026-50223** — pre-24.09.07 authenticated privilege escalation (`updateOrRemove` authorization bypass) + Content/DataResource FreeMarker template-injection RCE (oss-security 2026-06-10); patch to 24.09.07. Relevant where partner / low-trust users have content-editing capabilities on internet-facing OFBiz ERP.

**Jenkins CVE-2026-53435 – CVE-2026-53442** — 8-CVE June 10 batch including Stapler arbitrary-type deserialization (CVE-2026-53435) chaining to impersonation / Script Console RCE / arbitrary file read, plus open-redirect (CVE-2026-53436/37), login-flow phishing redirect (CVE-2026-53440), stored XSS in offline cause descriptions (CVE-2026-53441), and plaintext secret persistence in config.xml (CVE-2026-53442). Patch to Jenkins 2.568 / LTS 2.555.3; Jenkins controllers are typically broadly-readable so the deserialization path warrants priority across CI/CD fleets.

**ldns CVE-2026-10846 (CVSS 8.2)** — stub-resolver UDP responses not verified against query (ID, address/port, question section) — classic off-path DNS poisoning class issue, affects ldns 1.2.0–1.9.0; upgrade to 1.9.1. Distro-rebuild blast radius across services / containers that link ldns rather than getaddrinfo (oss-security 2026-06-10).

**Microsoft Defender 'RoguePlanet' SMB-share race condition — public PoC released 2026-06-10** by Nightmare Eclipse / Chaotic Eclipse, still no Microsoft patch (Watchtower NOTED 2026-06-10). EoP-class outcome (SYSTEM on fully June-2026-patched Windows) keeps this in NOTED despite remote-SMB trigger — application allow-listing / ThreatLocker remains the recommended mitigation pending vendor fix.

**Apache Answer CVE-2026-25700** — AdminToken not invalidated after admin deactivation; continuation of yesterday's Apache Answer 6-CVE batch. Only relevant where Answer is in internal use as a Q&A platform.

**KVM/arm64 CVE-2026-46316 ITScape Guest-to-Host Escape** (oss-security 2026-06-10, Hyunwoo Kim) — VM isolation scope is out of Watchtower core scope per policy, but tracked for IaaS substrate operators since cloud providers commonly run KVM on Arm Graviton-class fleets.

**FreeBSD kTLS-RX CVE-2026-45257** (oss-security 2026-06-10) — local root via in-place AES-GCM decrypt over `sendfile(2)` EXTPG mbufs to page-cache write; out of Watchtower remote-component scope, tracked only for FreeBSD-fleet operators.

**Node.js June 2026 security release scheduled 2026-06-17** (oss-security 2026-06-10, Rafael Gonzaga) — all supported release lines; CVE list / severity withheld until 2026-06-17; pre-stage maintenance windows for Node.js-based service fleets.

**Pi-Hole FTL CVE-2026-44693 CVSS 8.8** (dbugs.ptsecurity.com 2026-06-10) — limited corporate blast radius given Pi-Hole's home-network footprint, meaningful for any internal DNS sinkhole deployments built on Pi-Hole.

**Fission CVE-2026-50566 CVSS 9.9** (dbugs.ptsecurity.com 2026-06-10) — Fission Kubernetes-native serverless framework critical issue; niche enterprise scope but anyone running Fission for FaaS workloads should patch on priority.

**Palo Alto Cortex XSIAM CVE-2026-0274 CVSS 8.1** (dbugs.ptsecurity.com 2026-06-10) — affects enterprise XSIAM customers; tracked only for asset-DB / SOAR platform operators.

**ImageMagick June 2026 batch CVE-2026-49218 + CVE-2026-53460..53465** — DCM decoder dimension validation + memory allocation OOM cluster; patched in 6.9.13-48/50 and 7.1.2-24/25 (opencve.io 2026-06-10). DoS-class but distro-rebuild blast radius — relevant where ImageMagick is in the user-supplied-content image-processing path (CMS / ticketing / helpdesk).

**SEC Consult SA-20260608-0 — Genetec-provided RabbitMQ Binary Planting EoP** (Full Disclosure 2026-06-08) — limited to Genetec physical-security customers, no remote path.

**Anthropic Project Glasswing transparency concerns** (Schneier 2026-06-08) — thousands of vulnerabilities reportedly found by Anthropic's AI vuln-discovery initiative but few patched, no methodology / findings disclosure; calibration data point for the AI-vulnerability-discovery scaling pattern (Microsoft attributing PT volume to AI-assisted bug finding per Watchtower MEMORY 2026-06-10).

**NSO Group resumed WhatsApp spear-phishing in violation of permanent injunction** (BleepingComputer + Schneier + THN 2026-06-08/10) — continuation reporting only, no new IOC or capability change beyond what was already covered 2026-06-08.

**ShinyHunters / Wynn Resorts data theft** (eSecurity Planet) — adjacent context to today's PeopleSoft NEWS finding; older event but ShinyHunters' surfacing of new evidence aligns with the same group's June 2026 PeopleSoft extortion push.

**Zcash Orchard fraudulent-fund-creation bug, patched** (Schneier 2026-06-08) — cryptocurrency-economic-impact research bug; tracked only as calibration for AI-assisted vuln-research signal (found by AI researcher Taylor Hornby).

**OpenSSL June 2026 16-CVE Security Advisory** (oss-security 2026-06-09) — amplification of yesterday's NOTED on CVE-2026-45447 PKCS7_verify UAF, plus 15 additional CVEs (CVE-2026-34182 CMS AuthEnvelopedData, CVE-2026-34183 / CVE-2026-42764 QUIC, CVE-2026-35188 OCSP double-free, CVE-2026-45445 AES-OCB IV bypass). PKCS7_verify UAF is the most concerning given S/MIME signed-message exposure on mail gateways; distro-rebuild cadence applies.

**GitHub Security Lab GHSL-2025-009 / CVE-2026-29075 — Mesa benchmarks.yml workflow code execution** (securitylab.github.com) — relevant to teams running forks of Mesa with CI on untrusted PRs; limited corporate blast radius.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | BleepingComputer, The Hacker News, SecurityWeek, Krebs, Schneier | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ⚠️ — 403 (catalog), reachable via `cisa.gov/news-events/alerts/2026/06/09/cisa-adds-three-known-exploited-vulnerabilities-catalog` fallback URL pattern |
| Vendor advisories | rapid7.com, fortinet.com/blog/threat-research, blog.cloudflare.com/tag/security, msrc.microsoft.com/blog | ⚠️ (msrc redirect) |
| Research / OSINT | seclists.org/fulldisclosure, openwall.com/lists/oss-security, securitylab.github.com, kb.cert.org/vuls, googleprojectzero.blogspot.com, dbugs.ptsecurity.com, avleonov.com | ⚠️ (googleprojectzero redirect, securitylab old data) |
| Supply chain | github.com/0xMarcio/cve, packetstormsecurity.com | ⚠️ (packetstorm redirect to packetstorm.news) |
| Threat intel | opencve.io / app.opencve.io, nvd.nist.gov, cve.mitre.org / cve.org, attackerkb.com, hackerone.com/hacktivity, bugcrowd.com/disclosures, habr.com/ru/companies/tomhunter, teletype.in/@cyberok, cert.gov.ua | ⚠️ / ❌ (multiple unreachable / no June content) |

**Errors:** cisa.gov 403, cisa.gov/known-exploited-vulnerabilities-catalog 403, attackerkb.com 403, bugcrowd.com/disclosures 404, hackerone.com/hacktivity JS-only, cve.mitre.org JS-only, cve.org JS-only, cert.gov.ua empty response. **Degraded:** packetstormsecurity.com (redirect), msrc.microsoft.com/blog (redirect), nvd.nist.gov (redirect), googleprojectzero.blogspot.com (redirect to projectzero.google/), securitylab.github.com (latest 2026-05-22), habr.com/ru/companies/tomhunter/articles (no June content), teletype.in/@cyberok (no June content).
**CISA KEV:** 3 new additions 2026-06-09 (CVE-2026-20245 Cisco SD-WAN Manager, CVE-2026-11645 Chrome V8 — browser-scope out of Watchtower core scope, CVE-2026-7473 Arista EOS). All with FCEB deadline 2026-06-23. Detected via news-events alert URL fallback per Watchtower MEMORY 2026-06-08 pattern.

---

*Watchtower vulnerability-researcher | Cycle: 2026-06-11/night | Next: 2026-06-12/night*
