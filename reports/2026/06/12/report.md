# Watchtower Night Report — 2026-06-12
**Cycle:** Night | **Generated:** 2026-06-12 00:30 UTC (2026-06-12T00:30:00Z)
**Sources checked:** 19/30 | **CISA KEV total:** Check Point CVE-2026-50751 KEV-add 2026-06-08 belatedly surfaced | **New KEV additions:** CVE-2026-50751 (Check Point VPN — promoted to today's CRITICAL News, federal deadline 2026-06-11 now lapsed)

---

## 🔴 CRITICAL

### Check Point Remote Access VPN CVE-2026-50751 — IKEv1 Certificate-Validation Bypass Actively Exploited Since 2026-05-07; KEV-Added 2026-06-08 With Federal Deadline 2026-06-11 (Now Lapsed); Qilin Ransomware Affiliate Attribution (CVSS 9.3)
**Product:** Check Point Remote Access VPN, Mobile Access blade, and Spark Firewall product lines (R80.20.X / R80.40 / R81 / R81.10 / R81.10.X / R81.20 / R82 / R82.00.X / R82.10) | **CVE:** CVE-2026-50751 | **Status:** Patched + Active Exploitation + KEV (federal deadline LAPSED)

A logic flaw in how Remote Access and Mobile Access components validate certificates during IKEv1 key exchange allows an unauthenticated attacker to establish a fully-authorised VPN session without any credentials. The vulnerability is exploitable in deployments using the deprecated IKEv1 protocol AND accepting legacy Remote Access clients AND not requiring machine certificates — a configuration that remains widespread in long-running Check Point estates. Check Point first observed suspicious activity 2026-06-04 and traced the earliest exploitation to **2026-05-07**. Rapid7 MDR confirmed two customer incidents (high confidence) attributed to a **Qilin ransomware affiliate** using VPS infrastructure for geographically targeted ingress; Check Point itself attributes a broader campaign (medium confidence) of "several dozen targeted organisations globally." Companion CVE-2026-50752 (CVSS 7.4) MITM on site-to-site VPN was published in the same advisory but is not exploited.

**Timeline:** earliest observed exploitation 2026-05-07 → Check Point detects suspicious activity 2026-06-04 → vendor hotfixes published → CISA KEV add 2026-06-08 with federal deadline 2026-06-11 → Rapid7 ETR publication and broader mainstream pickup 2026-06-11.

**Why it matters:** This is a **Watchtower miss**: the KEV add landed 2026-06-08 (the same day cisa.gov direct WebFetch returned 403 and the KEV-fallback URL also failed to surface it via search). Federal civilian agencies were already overdue by 2026-06-11. With Qilin attribution confirmed and at least several-dozen-org scope, this is functionally equivalent to the highest-priority perimeter VPN exposures seen this year (PAN-OS, Ivanti) and warrants immediate hunt + remediation regardless of agency status.

**Discovered by:** Check Point internal telemetry + Rapid7 MDR forensics; secondary Qilin attribution by Check Point Incident Response + Rapid7 MDR.

**Mitigation:**
- Apply Check Point hotfixes on every R80.20.X through R82.10 branch today; treat the four EoS branches (R80.20.X / R80.40 / R81 / R81.10) as decommission candidates if hotfix-eligible support contracts have lapsed
- Disable IKEv1 entirely on Remote Access and Mobile Access gateways; force IKEv2-only authentication
- Require machine certificates for every external VPN connection — refuse legacy Remote Access clients
- Hunt VPN session logs from 2026-05-07 forward for sessions established without an associated successful authentication audit record
- Search EDR / endpoint telemetry for Qilin ransomware affiliate TTPs (rapid lateral movement from VPN ingress IPs to file servers, encryption activity)
- Confirm internet-reachable IKE / Remote-Access endpoints are inventoried (Shodan / Censys) and verified patched

**Sources:** [The Hacker News — Critical Check Point VPN Flaw Exploited](https://thehackernews.com/2026/06/critical-check-point-vpn-flaw-exploited.html) | [Rapid7 ETR — Critical Check Point VPN Zero-Day Exploited in the Wild (CVE-2026-50751)](https://www.rapid7.com/blog/post/etr-critical-check-point-vpn-zero-day-exploited-in-the-wild-cve-2026-50751/)

---

### Oracle PeopleSoft PeopleTools 8.61/8.62 CVE-2026-35273 — Specific CVE Now Assigned + Oracle Releases Emergency Mitigations 2026-06-11; ShinyHunters 300-Instance Campaign 68% Higher-Ed Concentrated, Nottingham 450K Confirmed (UPDATE, prev score 8 → 9, CVSS 9.8)
**Product:** Oracle PeopleSoft Enterprise PeopleTools 8.61 and 8.62 | **CVE:** CVE-2026-35273 (newly assigned) | **CVSS:** 9.8 | **First reported:** 2026-06-10

Yesterday's Watchtower NEWS covered the ShinyHunters mass-extortion campaign with `cve='Multiple'` — Oracle has now assigned **CVE-2026-35273** to the zero-day primitive at the centre of the campaign, confirmed it is remotely exploitable without authentication and may result in remote code execution, and released **emergency mitigations via its support portal on 2026-06-11** with a full patch forthcoming. Mandiant published recommendations for affected customers including restricting access to sensitive PeopleSoft endpoints and monitoring for ShinyHunters TTPs: MeshCentral remote-management agents disguised as Microsoft Azure services, SSH brute-force against psoft / oracle / linuxadm accounts, and the `azurenetfiles[.]net` staging domain. PT-Security dbugs published PT-2026-48612 (CVE-2026-35273, CVSS 9.8) the same day. Victim concentration refined to **68% higher-education sector** — Nottingham University (450K students) publicly confirmed.

**Timeline:** ShinyHunters scope-claim 2026-06-10 (Watchtower NEWS, score 8, cve='Multiple') → Oracle emergency advisory + CVE-2026-35273 assignment + portal mitigations 2026-06-11 → Mandiant IOC publication + Watchtower UPDATE 2026-06-12 (score 9, +1).

**Why it matters:** Specific-CVE assignment + portal mitigation + confirmed higher-ed sector concentration moves this from a generic-campaign story to a vendor-acknowledged actively-exploited zero-day with a defined patch path. The 9.8 CVSS + unauth RCE + 100+ org scope justifies treating internet-facing PeopleSoft as Patch-Tuesday-equivalent priority going forward.

**Mitigation:**
- Apply Oracle's emergency portal mitigation on PeopleSoft 8.61 / 8.62 today
- Restrict access to sensitive PeopleSoft endpoints to internal management networks pending full patch
- Hunt SSH logs for brute-force against the psoft / oracle / linuxadm accounts
- Block egress to `azurenetfiles[.]net` and add it to threat-intel feed integration
- Hunt EDR telemetry for MeshCentral agents that masquerade as Microsoft Azure service binaries
- If your organisation operates in higher-ed, assume targeted-victim posture and run IR-style triage on every internet-reachable PeopleSoft instance

**Sources:** [BleepingComputer — Oracle Mitigates PeopleSoft Zero-Day Exploited in Data Theft Attacks](https://www.bleepingcomputer.com/news/security/oracle-mitigates-peoplesoft-zero-day-exploited-in-data-theft-attacks/) | [The Hacker News — ShinyHunters Exploits Oracle PeopleSoft Zero-Day](https://thehackernews.com/2026/06/shinyhunters-exploits-oracle-peoplesoft.html) | [PT-Security dbugs PT-2026-48612](https://dbugs.ptsecurity.com)

---

### Ivanti Sentry CVE-2026-10520 — Shadowserver Confirms Active Exploitation 24 Hours After Vendor Advisory + watchTowr PoC; 2 Of 19 Internet-Exposed Gateways Already Backdoored, Saudi NCA Co-Discovery (UPDATE, prev score 9 → 9 hold, CVSS 10.0)
**Product:** Ivanti Sentry (formerly MobileIron Sentry) — fixed in R10.5.2 / R10.6.2 / R10.7.1 | **CVE:** CVE-2026-10520 (companion CVE-2026-10523 CVSS 9.9) | **Status:** Patched + Active Exploitation Confirmed

Yesterday's Watchtower UPDATE promoted the Ivanti Sentry chain from NOTED to UPDATE on the back of the vendor advisory + watchTowr PoC, with the caveat "no observed exploitation yet but treat as 7-14 day patch SLA on perimeter security infrastructure given Fortinet's PoC-to-scanner-template tempo." That patch SLA has now collapsed. **Shadowserver 2026-06-11** scanning surfaced **19 vulnerable internet-exposed Sentry gateways with at least 2 already backdoored** ("all remaining likely compromised too"). **Saudi NCA (National Cybersecurity Authority)** is credited as a co-discovery source for the active-exploitation detection. Patch-to-confirmed-exploitation gap was **less than 48 hours**. Ivanti's security advisory has not been updated to reflect confirmed in-the-wild status.

**Timeline:** Ivanti advisory + watchTowr PoC 2026-06-09/10 (Watchtower UPDATE) → Shadowserver active-exploitation confirmation 2026-06-11 → Watchtower UPDATE 2026-06-12 (score holds at 9, material change is confirmed in-wild not score adjustment).

**Why it matters:** Sub-48-hour patch-to-confirmed-ITW is at the floor of historical Ivanti perimeter-device tempo (Connect Secure 2024, Standalone Sentry 2023). The fact that **2 of 19 detected Internet-facing instances are already backdoored** implies the unpatched-fleet tail is being processed by automated tooling. Treat any unpatched perimeter Sentry as already-compromised pending IR.

**Mitigation:**
- Patch to Sentry R10.5.2 / R10.6.2 / R10.7.1 immediately if not already done
- IR-hunt every internet-reachable Sentry gateway for backdoor artefacts (unusual /mics/api/v2/sentry/mics-config/handleMessage POST entries, anomalous admin accounts, unexpected outbound network connections from Sentry)
- Audit Sentry admin-account creation events for new accounts since 2026-06-09
- If you cannot patch within 24 hours, isolate Sentry from the internet pending remediation
- Forward IOCs from Shadowserver (when published) to perimeter / SIEM and treat affected gateways as Tier 0 IR scope

**Sources:** [BleepingComputer — Max-Severity Ivanti Sentry Vulnerability Now Exploited in Attacks](https://www.bleepingcomputer.com/news/security/max-severity-ivanti-sentry-vulnerability-now-exploited-in-attacks/) | [Rapid7 ETR — CVE-2026-10520, CVE-2026-10523 Multiple critical vulnerabilities affecting Ivanti Sentry](https://www.rapid7.com/blog/post/etr-cve-2026-10520-cve-2026-10523-multiple-critical-vulnerabilities-affecting-ivanti-sentry/) | Shadowserver 2026-06-11

---

## 🟠 HIGH

### Splunk Enterprise CVE-2026-20253 (CVSS 9.8) — Unauthenticated Arbitrary File Creation / Truncation Via PostgreSQL Sidecar Service Endpoint Missing Auth Controls; Patched 2026-06-11
**Product:** Splunk Enterprise | **CVE:** CVE-2026-20253 | **CVSS:** 9.8 | **First reported:** 2026-06-11

Splunk's PostgreSQL sidecar service exposes a file-operations endpoint that lacks authentication controls, allowing an unauthenticated attacker to invoke arbitrary file creation / truncation on the Splunk host. Classic chaining primitive to Splunk RCE via app-deployment + Splunk's history of post-disclosure ransomware-affiliate uptake within 30-60 days makes this a near-certain priority target as soon as PoC tooling appears. Splunk shipped fixes 2026-06-11 alongside three additional High-severity issues enabling RCE, SSRF, and XSS, plus four Medium issues around saved-search modification and data exfiltration. SecurityWeek reports no observed in-the-wild exploitation yet.

**Mitigation:**
- Apply Splunk Enterprise patches today on every indexer / search head in your fleet
- Audit Splunk hosts for unexpected files written under PostgreSQL sidecar paths since the disclosure date
- Validate PostgreSQL sidecar service is not exposed beyond the trusted Splunk admin network
- Treat as 7-14 day patch SLA on internet-reachable Splunk surfaces (typically search heads behind ALB / WAF)

**Sources:** [SecurityWeek — Splunk, Palo Alto Networks Patch Severe Vulnerabilities](https://www.securityweek.com/splunk-palo-alto-networks-patch-severe-vulnerabilities/) | Splunk advisory 2026-06-11

---

### Veeam Backup & Replication v12 CVE-2026-44963 (CVSS 9.4) — Authenticated Domain-User RCE On Backup Server, Patched 12.3.2.4854 (watchTowr / Sina Kheirkhah); v13 Architecture Not Affected
**Product:** Veeam Backup & Replication 12.3.2.4465 and all earlier v12 builds | **CVE:** CVE-2026-44963 | **CVSS:** 9.4 | **First reported:** 2026-06-09

Authenticated domain-user RCE on the Veeam Backup Server: any AD-joined non-admin domain account suffices to execute arbitrary code on the Veeam host. The Backup Server routinely holds backup-encryption keys + service credentials for every workload it backs up, which is structurally the ideal ransomware-affiliate pivot — neutralise recovery while harvesting credentials for downstream impact. Patched in 12.3.2.4854 (2026-06-09); v13.x architecture eliminated the vulnerable code path so v13 deployments are unaffected. Discovered + reported by **watchTowr researcher Sina Kheirkhah**, who has a multi-year track record of Veeam findings translating to ransomware-affiliate weaponisation within 30-60 days (CVE-2023-27532 → Cuba/Akira; CVE-2024-40711 → Akira/LockBit; CVE-2025-23120 → Black Basta).

**Mitigation:**
- Patch Veeam Backup & Replication v12 to 12.3.2.4854 today
- For v12 deployments that cannot patch within 24 hours, restrict Veeam Backup Server console to a small, audited set of named admin accounts (do not rely on broad domain-user trust)
- Plan v13 migration on a 6-month horizon — v13 architecture is structurally not vulnerable to this class
- Audit Veeam Backup Server access logs for any non-admin domain user authentication patterns
- Ensure Veeam Backup Server backups themselves are stored on an isolated immutable target (object lock, air-gapped tape) — the standard hardening for ransomware-affiliate Veeam compromise

**Sources:** [The Hacker News — Veeam Backup & Replication RCE Flaw Lets Domain Users Take Over](https://thehackernews.com/2026/06/veeam-backup-replication-rce-flaw-lets.html) | watchTowr advisory 2026-06-09

---

### Apache CXF 12-CVE Batch — OAuth2 Token-Introspection Auth Bypass + 7 OAuth2 Issues + 2 JNDI Injection + XXE + Attachment-Header Restriction Gap (oss-security 2026-06-11, Colm O hEigeartaigh)
**Product:** Apache CXF (enterprise Java SOAP/REST framework) | **CVE:** CVE-2026-49875, CVE-2026-50623, CVE-2026-50627, CVE-2026-50628, CVE-2026-50629, CVE-2026-50630, CVE-2026-50631, CVE-2026-50632, CVE-2026-50633, CVE-2026-50634, CVE-2026-50645 | **CVSS:** Multiple (highest-impact items in the OAuth2 cluster) | **First reported:** 2026-06-11

Apache CXF is downstream in Spring Web Services, ServiceMix, Karaf, JBoss Fuse, many Apache pipelines, and most large-enterprise Java service buses. The 12-CVE batch published 2026-06-11 via oss-security by Colm O hEigeartaigh covers four distinct attack classes:

- **OAuth2 (highest impact for any internet-facing CXF-OAuth2 endpoint):** CVE-2026-50623 (TokenIntrospectionService authentication bypass), CVE-2026-50627 (Access Token Validator missing JWT audience/issuer validation), CVE-2026-50628 (inverted IP-binding check defeats security control), CVE-2026-50629 (log injection via unsanitised client identifier), CVE-2026-50630 (HTTP response splitting via WWW-Authenticate realm injection), CVE-2026-50631 (TOCTOU race condition in refresh-token processing)
- **JNDI Injection (classic Log4Shell-class blast radius if reachable):** CVE-2026-50632 (JMSConfigFactory), CVE-2026-50633 (DispatchMDBMessageListenerImpl)
- **XXE / message-validation gaps:** CVE-2026-49875 (XXE in W3CMultiSchemaFactory and EndpointReferenceUtils), CVE-2026-50634 (WS JSON request filter trusts metadata from unvalidated first signature entry), CVE-2026-50645 (no restriction on attachment headers per message)

**Mitigation:**
- Patch Apache CXF on every internet-facing SOAP / REST / OAuth2 surface in your Java estate today
- Inventory transitive dependencies — Spring WS / ServiceMix / Karaf / JBoss Fuse / Camel are common downstream consumers
- For OAuth2 deployments specifically, audit TokenIntrospectionService configuration and verify JWT audience/issuer validation is correctly configured during the upgrade
- Treat the JNDI-injection items as Log4Shell-class for any CXF JMS / MDB deployment; verify Apache CXF's PR 1844 / 1845 fixes are present

**Sources:** [oss-security Apache CXF batch 2026-06-11](https://www.openwall.com/lists/oss-security/2026/06/11/) | Apache CXF security advisories

---

## 🟡 MEDIUM

### protobuf.js "Proto6" 6-CVE Batch — Prototype-Pollution → RCE + Schema-Name Code Injection + Multiple DoS Affecting Node.js Apps, Google Cloud Libraries, Baileys WhatsApp Bots
**Product:** protobuf.js ≤ 7.5.5 / 8.0.0–8.0.1; protobufjs-cli ≤ 1.2.0 / 2.0.0–2.0.1 | **CVE:** CVE-2026-44289, CVE-2026-44290, CVE-2026-44291, CVE-2026-44292, CVE-2026-44294, CVE-2026-44295 | **Published:** 2026-06-10

The de-facto JavaScript/TypeScript Protocol Buffers implementation is used in virtually every Node.js application that consumes gRPC, every Google Cloud client library, and the Baileys WhatsApp bot framework. Six-CVE "Proto6" cluster covers prototype-pollution-then-RCE (CVE-2026-44291 CVSS 8.1), static code injection via malicious schema names (CVE-2026-44295 CVSS 8.7), and four DoS/injection issues. Root pattern is "data can become behavior" when schemas and metadata are treated as trusted. Patched in protobufjs 7.5.6 / 8.0.2 and protobufjs-cli 1.2.1 / 2.0.2. Published attack scenarios include CI/CD pipeline poisoning leaking build secrets and crashing WhatsApp bot fleets via crafted messages.

**Mitigation:**
- Bump protobufjs to 7.5.6 or 8.0.2 across the Node.js fleet and protobufjs-cli to 1.2.1 / 2.0.2 in CI/CD
- Audit Google Cloud SDK dependency trees for affected transitive versions; bump SDK majors where needed
- For Baileys-based WhatsApp bots, treat as critical-path patching given confirmed crafted-message DoS scenarios
- Audit CI/CD pipelines for schema-loading workflows that consume untrusted schema files

**Sources:** [The Hacker News — Six Proto6 Vulnerabilities in protobuf.js](https://thehackernews.com/2026/06/six-proto6-vulnerabilities-in.html) | GHSA advisories for protobufjs 7.5.6 / 8.0.2

---

## 📋 Noted / Monitoring

**CISA BOD 26-04 (no CVE)** — published 2026-06-11; supersedes BOD 19-02 + 22-01; FCEB agencies must remediate KEV-listed full-control items on public assets in **3 days**, partial-control / non-automatable items in **14 days**; 60-day policy update window, 180-day full implementation. Durable calibration point for Watchtower severity scoring going forward.

**Microsoft June 2026 Patch Tuesday** — 206 CVEs (largest ever per Krebs), 39 Critical, 167 Important, 56 RCE, 3 publicly-disclosed zero-days (CVE-2026-50507 BitLocker EoP, CVE-2026-45586 Windows EoP, CVE-2026-49160 HTTP/2 DoS). In Watchtower scope: CVE-2026-45657 (Kernel UAF via crafted network traffic, CVSS 9.8 + no in-wild yet), CVE-2026-47291 (HTTP.sys integer overflow, CVSS 9.8), CVE-2026-44815 (DHCP Client buffer overflow, CVSS 9.8). All patched; no out-of-band action required.

**cPanel / WHM CVE-2026-41940** — Go-based authentication-bypass PoC published 2026-06-12 (`Defacto-ridgepole254/CVE-2026-41940-Exploit-PoC`) ahead of broad mainstream coverage. Monitor for vendor advisory; verify against any internet-facing cPanel control panels.

**CyberArk Privileged Session Manager CVE-2026-45171 (CVSS 9.3)** — PT-2026-48787 dbugs disclosure 2026-06-11. Advisory detail pending. High-leverage for any PAM-fleet operator.

**ServiceNow instance-access vulnerability (no CVE)** — patched 2026-06-05 server-side on hosted customers, known internally since 2026-04-07, no malicious in-wild (security researchers / bug-bounty only). No customer action required.

**Check Point + Cisco + Chrome + Arista KEV-add cluster confirmation** — Check Point CVE-2026-50751 promoted to today's CRITICAL News; Cisco SD-WAN CVE-2026-20245 and Arista EOS CVE-2026-7473 were yesterday's UPDATE/NEWS; Chrome V8 CVE-2026-11645 remains client-only OOS per scope policy. Continues confirmation that cisa.gov direct fetch is unreachable and KEV adds require cross-source relay.

**VU#862559** — crypton-x509-validation Haskell libraries do not enforce X.509 NameConstraints (CERT/CC 2026-06-11). Limited blast radius — only Haskell-based services with custom CAs trusting NameConstraints.

**VU#616257** — Microsoft-signed UEFI shim bootloaders vulnerable to Secure Boot bypass (CERT/CC 2026-06-09). Out of Watchtower core scope per firmware-no-remote-component policy. Refresh DBX revocations and verify shim updates roll through your imaging pipeline.

**GreatXML BitLocker bypass (no CVE)** — Chaotic Eclipse via THN 2026-06-11. Local physical-access exploit placing `unattend.xml` + `Recovery/WindowsRE/ReAgent.xml` on the recovery partition to spawn an unrestricted WinRE shell over the BitLocker volume. Strictly local; second BitLocker bypass from this researcher after YellowKey (CVE-2026-45585, patched June Patch Tuesday).

**ClipBucket V5 CVE-2026-45060 / CVE-2026-42846 (CVSS 9.8)** — PT-Security dbugs 2026-06-11. Niche Macwarrior video-sharing platform.

**JoomSport WP plugin CVE-2026-42647 (CVSS 9.3)** — BearDev, SQL injection through 5.7.7 (PT-2026-48782 via dbugs 2026-06-11). Niche sports-team WordPress sites.

**Hippoo Mobile App for WooCommerce CVE-2026-49060 (CVSS 9.8)** — PT-Security dbugs 2026-06-11. Niche WooCommerce mobile-companion plugin.

**Hermes WebUI CVE-2026-49973 (CVSS 9.4)** — Nesquina, first-run authentication bypass via `_set_password` parameter on settings API (opencve.io 2026-06-11). Niche home-server admin panel scope.

**AsyncRAT campaign using fake AI-document lures** — FortiGuard Labs 2026-06-11 (Cara Lin). Multi-stage chain via fake AI documents → PowerShell → AutoHotkey loader → process injection → AsyncRAT. Joins the AI-themed social-engineering cluster (ChatGPhish / LLMShare / OpenAI-Codex Wrapper malware).

**OceanLotus / APT32 SPECTRALVIPER campaign** — supply-chain compromise of FireAnt forensic tool targeting Vietnam infrastructure / investors (THN 2026-06-11). Limited geographic scope but "compromise the forensic tool the IR team uses" is durable APT tradecraft.

**Microsoft Defender 'RoguePlanet' SMB-share race condition LPE (continuation)** — local SYSTEM EoP on fully June-2026-patched Windows, still out of core Watchtower scope per local-EoP policy; tracked for workstation-hardening teams pending vendor fix.

**npm v12 disables install scripts by default** — GitHub / BleepingComputer 2026-06-11. Major supply-chain hardening that closes the Wave-1 / Wave-2 npm-worm install-time-execution primitive at the package-manager level. Plan npm 12 rollout in CI/CD.

**Maine state breach-portal abuse** — public-facing breach-disclosure portal accepting fraudulent submissions without verification (BleepingComputer 2026-06-11). Operational lesson in trust validation of public-disclosure feeds.

**Coupang $409M data-breach fine (South Korea) + Kyushu Electric 10.9M physical-drive loss** — two large privacy / data-handling incidents; neither involves a CVE-class technical vulnerability.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | BleepingComputer, The Hacker News, SecurityWeek, Krebs on Security, Schneier | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/KEV catalog | ❌ persistent 403 (Check Point KEV add not surfaced before federal deadline lapsed) |
| Vendor advisories | Rapid7 ETR, Fortinet, Cloudflare blog, MSRC blog | ✅ except MSRC (header-only) |
| Research / OSINT | Schneier, GitHub Security Lab, openwall oss-security, github.com/0xMarcio/cve, dbugs.ptsecurity.com, opencve.io | ✅ |
| Supply chain | github.com/search?q=CVE, oss-security batch coverage | ✅ |
| Threat intel | THN, BleepingComputer, Fortinet, schneier | ✅ |
| Full Disclosure | seclists.org/fulldisclosure | ✅ (no new posts since 2026-06-08) |
| Russian / Ukrainian | habr.com/tomhunter, teletype.in/@cyberok, cert.gov.ua | ⚠️ persistent silence + ❌ cert.gov.ua empty |

**Errors:** cisa.gov / cisa.gov/KEV (403), cve.mitre.org / cve.org (JS-only), hackerone.com/hacktivity (JS-only), bugcrowd.com/disclosures (404), googleprojectzero.blogspot.com (redirected, no content), packetstormsecurity.com (redirected to packetstorm.news/, ToS only), msrc.microsoft.com/blog (redirect to header-only page), attackerkb.com (403), cert.gov.ua (empty).

**CISA KEV:** Check Point CVE-2026-50751 KEV-add 2026-06-08 surfaced today via Rapid7 ETR + THN cross-reference — federal deadline 2026-06-11 has already lapsed. The cisa.gov/news-events fallback URL pattern continues to be unreliable for fresh adds.

---

*Watchtower vulnerability-researcher | Cycle: 2026-06-12/night | Next: 2026-06-13/night*
