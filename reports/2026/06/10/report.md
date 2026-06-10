# Watchtower Night Report — 2026-06-10
**Cycle:** Night | **Generated:** 2026-06-10 03:00 UTC (2026-06-10T03:00:00Z)
**Sources checked:** 23/30 | **CISA KEV total:** ~1,542 | **New KEV additions:** 2 (CVE-2026-50751 Check Point RA-VPN added 2026-06-09 with 3-day deadline; CVE-2026-42271 BerriAI LiteLLM added 2026-06-08/09)

---

## 🔴 CRITICAL

### Check Point Remote Access VPN / Mobile Access / Spark Firewalls — CVE-2026-50751 Unauthenticated Authentication Bypass Exploited as Zero-Day by Qilin Ransomware (CISA Emergency 3-Day Deadline, Due 2026-06-11)
**Product:** Check Point Remote Access VPN, Mobile Access / SSL VPN, Spark firewalls (only deployments using deprecated IKEv1 key exchange without machine-certificate requirements) | **CVE:** CVE-2026-50751 | **Status:** Patched 2026-06-08 | KEV (added 2026-06-09) | Active Exploitation (Qilin RaaS) Confirmed

An unauthenticated remote attacker can bypass authentication on vulnerable Check Point Remote Access VPNs, Mobile Access / SSL VPN portals, and Spark firewalls — establishing a working remote-access VPN session without credentials. The condition is configuration-gated to deployments still using deprecated IKEv1 key exchange that do not enforce machine-certificate authentication. Check Point published the patched advisory Monday 2026-06-08, CISA added the CVE to the KEV catalog on 2026-06-09 with a 3-day (rather than the standard 21-day BOD 22-01) deadline of 2026-06-11, and BleepingComputer confirms Qilin ransomware affiliates have already used the bug for initial access in at least one observed incident. No authentication, special tooling, or insider access required.

**Timeline:** Check Point advisory + patches released 2026-06-08 → CISA KEV addition + 3-day Emergency-style deadline 2026-06-09 → Qilin post-compromise activity observed and reported alongside KEV add → ongoing.

**Why it matters:** Remote-access VPN concentrators are the single highest-leverage initial-access surface for a ransomware affiliate: an unauthenticated bypass means scanner-driven mass exploitation, no credential phishing required, and a foothold inside the perimeter network. Qilin is a current-tempo RaaS operator with mature post-compromise tooling. Federal civilian deadline is 24 hours from this report; commercial defenders should be on the same clock.

**Discovered by:** Not publicly attributed; Check Point credits coordinated disclosure with CISA and downstream partners.

**Mitigation:**
- Apply Check Point hotfixes to all Remote Access VPN, Mobile Access / SSL VPN, and Spark firewalls today.
- Disable legacy remote-access clients and enforce IKEv2-only authentication on the gateway.
- Mandate machine-certificate authentication; remove any IKEv1 fallback in the SmartConsole policy.
- Enable IPS with the latest signature pack on the gateway.
- Hunt for unexpected VPN session establishment, new SSL VPN portal logins, and Qilin TTP indicators (rapid lateral SMB scans, Cobalt Strike beaconing, SystemBC, RDP-tunneled-over-SSH activity) on internal segments reachable from VPN client subnets.
- Federal civilian agencies: KEV deadline 2026-06-11.

**Sources:** [BleepingComputer — CISA orders feds to patch Check Point flaw exploited by ransomware gangs](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-check-point-flaw-exploited-by-ransomware-gangs/) | [CISA KEV alert (news-events fallback)](https://www.cisa.gov/news-events/alerts/2026/06/09/cisa-adds-one-known-exploited-vulnerability-catalog)

---

### Microsoft June 2026 Patch Tuesday — Record ~200 CVEs Including Three Publicly Disclosed Zero-Days (CTFMON EoP "GreenPlasma", HTTP/2 Bomb DoS, BitLocker "YellowKey") and 28 Critical RCEs
**Product:** Microsoft Windows / Windows Server (CTFMON, HTTP.sys, BitLocker TPM-only, Kerberos KDC, Active Directory Domain Services, Hyper-V, DHCP Client, Deployment Services, Graphics, Media, RDP Client), Azure Kubernetes Service, Exchange Server (6 CVEs), SharePoint Server (20+ CVEs), Nuance PowerScribe | **CVE:** CVE-2026-45586, CVE-2026-49160, CVE-2026-50507 (plus ~197 others) | **Status:** Patched 2026-06-09 | Three Publicly Disclosed Pre-Patch | Exchange / SharePoint / RDP / ADDS Critical Surface

Microsoft's June 2026 Patch Tuesday is a record-setting ~200 CVE batch (per Krebs) — Microsoft attributes the volume to AI-assisted bug-finding by engineering and researchers. Three CVEs were publicly disclosed before the fix shipped: **CVE-2026-45586** (Windows CTFMON link-following elevation of privilege to SYSTEM — researcher Nightmare Eclipse, marketed as "GreenPlasma"), **CVE-2026-49160** (HTTP/2 header-compression "HTTP/2 Bomb" denial of service forcing disproportionately large memory allocation on the server), and **CVE-2026-50507** (Windows BitLocker security-feature bypass — physical attacker can defeat encryption on TPM-only-protected volumes, "YellowKey"). The batch contains 28 critical-severity RCEs spanning Active Directory Domain Services, Azure Kubernetes Service, Hyper-V (two flaws), Windows Deployment Services, DHCP Client, HTTP.sys, Windows Kerberos KDC, Remote Desktop Client (multiple), and the Windows Graphics + Media components. Exchange Server receives 6 CVEs (spoofing / info disclosure / EoP / RCE) and SharePoint Server 20+ (primarily spoofing). No in-wild exploitation reported in the batch yet, but the three pre-disclosed CVEs raise the patch-tempo expectation substantially.

**Timeline:** Microsoft Update Guide releases 2026-06-09 → BleepingComputer, SecurityWeek, Krebs, Rapid7 coverage published same day → three publicly disclosed zero-days had researcher PoCs in advance (CTFMON / GreenPlasma by Nightmare Eclipse most notable).

**Why it matters:** Patch-Tuesday weeks at this volume saturate engineering bandwidth and force prioritisation. The three pre-disclosed CVEs are the obvious starting point but the 28 critical RCEs — especially HTTP.sys, Kerberos KDC, ADDS, RDP Client, and Hyper-V — represent fleet-wide blast radius. Exchange and SharePoint are durable initial-access surfaces; treat the 6 Exchange CVEs as monthly priority even when "only" spoofing-tier on paper.

**Mitigation:**
- Stage the June 2026 cumulative updates across patch-management rings starting today; aim for full domain-controller and Exchange / SharePoint coverage within 7 days.
- Prioritise the three publicly disclosed zero-days: CVE-2026-45586 (CTFMON EoP), CVE-2026-49160 (HTTP/2 DoS — load-balancer / IIS / Exchange front-ends), CVE-2026-50507 (BitLocker TPM-only — laptop fleet).
- Apply Kerberos KDC, HTTP.sys, and RDP Client critical RCEs ahead of standard cadence on any internet-reachable surface.
- HTTP/2 Bomb (CVE-2026-49160): enable HTTP/2 memory guards / connection limits at the edge load balancer in addition to the Windows patch.
- Confirm BitLocker laptop fleet uses TPM + PIN (not TPM-only) where threat model includes physical access.

**Sources:** [BleepingComputer — Microsoft June 2026 Patch Tuesday fixes 3 zero-day, 200 flaws](https://www.bleepingcomputer.com/news/microsoft/microsoft-june-2026-patch-tuesday-fixes-3-zero-day-200-flaws/) | [SecurityWeek — Microsoft patches 200 vulnerabilities](https://www.securityweek.com/microsoft-patches-200-vulnerabilities/) | [Krebs on Security — A record-breaking Patch Tuesday for June 2026](https://krebsonsecurity.com/2026/06/a-record-breaking-patch-tuesday-for-june-2026/) | [Rapid7 — Patch Tuesday – June 2026](https://www.rapid7.com/blog/post/em-patch-tuesday-june-2026/)

---

## 🟠 HIGH

### Veeam Backup & Replication CVE-2026-44963 — Any Low-Privilege Domain User Achieves RCE on Domain-Joined VBR ≤12.3.2.4465 (Patched 12.3.2.4854)
**Product:** Veeam Backup & Replication 12.x (all builds up to and including 12.3.2.4465; v13.x unaffected) | **CVE:** CVE-2026-44963 | **CVSS:** 9.4 | **First reported:** 2026-06-09

Veeam published an out-of-band advisory for CVE-2026-44963 on 2026-06-09: any authenticated Active Directory user with no special privilege can achieve remote code execution on the Veeam Backup & Replication server, provided the VBR server is joined to the domain. The vendor explicitly calls out that v13.x is unaffected due to architectural changes that landed in the v13 baseline. No in-wild exploitation is reported yet, but Veeam warns publicly that patch-diff weaponisation is the standard timeline for VBR bugs. Backup-server compromise is a ransomware end-state — destruction of recovery capability is the leverage that converts an intrusion into a paid ransom.

**Mitigation:**
- Upgrade Veeam Backup & Replication to 12.3.2.4854 across all VBR servers immediately.
- Strongly consider Veeam's documented architectural guidance to keep VBR off the production AD domain — separate-forest, workgroup, or dedicated management-tier identity reduces the blast radius of this entire vulnerability class.
- Audit who has any domain-user account that can authenticate to the VBR server's network surface — that is the actual exploit precondition.
- Hunt for unexpected child processes from the Veeam Backup Service account and unexpected outbound connections from the VBR server.

**Sources:** [BleepingComputer — New Veeam vulnerability exposes backup servers to RCE attacks](https://www.bleepingcomputer.com/news/security/new-veeam-vulnerability-exposes-backup-servers-to-rce-attacks/) | [TheHackerNews — Veeam Backup & Replication RCE Flaw](https://thehackernews.com/2026/06/veeam-backup-replication-rce-flaw-lets.html)

---

### BerriAI LiteLLM CVE-2026-42271 — MCP-Test Endpoint Command Injection (CVSS 8.7, Chains to 10.0 with CVE-2026-48710 Starlette Host Bypass) Added to CISA KEV with Confirmed Active Exploitation
**Product:** BerriAI LiteLLM ≥1.74.2 and <1.83.7 | **CVE:** CVE-2026-42271 (chains with CVE-2026-48710) | **CVSS:** 8.7 (10.0 chained) | **First reported:** 2026-06-09 (KEV add 2026-06-08/09)

LiteLLM's preview MCP-test endpoints (`POST /mcp-rest/test/connection` and `POST /mcp-rest/test/tools/list`) accept attacker-controlled `command`, `args`, and `env` fields and, when given a stdio configuration, spawn the supplied command as a subprocess on the proxy host. Any authenticated user with a valid proxy API key can therefore execute arbitrary code on the LiteLLM proxy server. The flaw chains with CVE-2026-48710 (Starlette host-header bypass) for a combined unauthenticated RCE rated CVSS 10.0. CISA added CVE-2026-42271 to the Known Exploited Vulnerabilities catalog on 2026-06-08/09 citing observed in-wild exploitation. This is the first AI-platform CVE in the 2026 KEV catalog and a notable validation of the threat model around LLM-gateway / agent-tooling infrastructure: AI proxies sit in the middle of identity, secrets, and outbound network access, making them a high-value lateral-movement pivot.

**Mitigation:**
- Upgrade LiteLLM to 1.83.7 or later across all proxy deployments today.
- Block `/mcp-rest/test/*` at the reverse proxy / API gateway in front of LiteLLM until the upgrade is confirmed in production.
- Treat any LiteLLM proxy historically exposed to untrusted networks as compromised: rotate API keys, model-provider credentials, and any stored env-var secrets reachable from the proxy.
- Audit egress from LiteLLM proxy hosts for unexpected destinations and subprocess execution by the proxy process.
- Add Host-header anomaly monitoring to detect the chained CVE-2026-48710 path.

**Sources:** [TheHackerNews — LiteLLM Flaw CVE-2026-42271 Exploited](https://thehackernews.com/2026/06/litellm-flaw-cve-2026-42271-exploited.html)

---

### SAP June 2026 Security Patch Day — 15 CVEs Including Four Critical Flaws in NetWeaver and Commerce Cloud
**Product:** SAP NetWeaver, SAP Commerce Cloud | **CVE:** Multiple (June 2026 Patch Day batch) | **CVSS:** Critical for 4 of 15 | **First reported:** 2026-06-09

SAP's June 2026 Security Patch Day fixes 15 vulnerabilities, four of them rated critical, affecting NetWeaver and Commerce Cloud. The critical issues span information disclosure, memory corruption, and system disruption. The companion oss-security thread `[SYSS-2026-004]` (Moritz Bechler, 2026-06-08) covers an additional SAP NetWeaver SAML XML Signature Wrapping vulnerability disclosed in the same window — the precise overlap with the Patch Day batch was not yet clarified by SAP at the time of this report.

**Mitigation:**
- Apply SAP June 2026 Security Patch Day updates to all NetWeaver and Commerce Cloud landscapes, prioritising any internet-reachable systems.
- Review NetWeaver SAML federation endpoints in light of SYSS-2026-004; validate XML signature processing libraries are current.
- Confirm SAP gateway / message-server ACLs are restrictive — a common precondition for NetWeaver RCE families.

**Sources:** [BleepingComputer — SAP fixes critical flaws in NetWeaver and Commerce Cloud](https://www.bleepingcomputer.com/news/security/sap-fixes-critical-flaws-in-netweaver-and-commerce-cloud/) | [SecurityWeek — SAP Patches Critical NetWeaver, Commerce Vulnerabilities](https://www.securityweek.com/sap-patches-critical-netweaver-commerce-vulnerabilities/) | [Full Disclosure — SYSS-2026-004 SAP NetWeaver SAML XML Signature Wrapping](https://seclists.org/fulldisclosure/2026/Jun/)

---

### 🔄 Update — Apache ActiveMQ Jolokia RCE CVE-2026-42588: Public Python PoC Lands on GitHub (Material Escalation)
**Product:** Apache ActiveMQ Jolokia management endpoint | **CVE:** CVE-2026-42588 | **Previous score:** 6 (Watchtower News 2026-06-01) | **New score:** 8 | **Trigger:** Public PoC publication

The 0xMarcio CVE-PoC index added a public Python proof-of-concept exploit for the ActiveMQ Jolokia RCE CVE-2026-42588 within the 2026-06-08→09 window. Watchtower originally newsed this CVE on 2026-06-01 at score 6 (pre-PoC). With the PoC now public, the bar for opportunistic exploitation drops to running a script — historically a 7-10-day window before scanner integration. Any ActiveMQ Jolokia endpoint reachable from untrusted networks should now be considered hostile-reachable.

**Mitigation:**
- Patch Apache ActiveMQ to the fixed version per the vendor advisory.
- If patching is delayed, disable or firewall the Jolokia management endpoint (default `/api/jolokia/*` on the ActiveMQ web console port).
- Add a WAF rule blocking Jolokia POST bodies containing serialized-Java markers.
- Search web access logs for the Jolokia PoC's request patterns.

**Sources:** [github.com/0xMarcio/cve (recently updated index)](https://github.com/0xMarcio/cve)

---

### 🔄 Update — Apache Tomcat Tribes Unauth Java-Deserialization RCE CVE-2026-34486: Metasploit Module Lands (Rapid7 Weekly Wrap-Up 2026-06-09)
**Product:** Apache Tomcat Tribes (clustering / replication channel) | **CVE:** CVE-2026-34486 | **Previous score:** 7 (Watchtower News 2026-05-20) | **New score:** 9 | **Trigger:** Metasploit module published

Rapid7's 2026-06-09 Metasploit Weekly Wrap-Up announces a new module covering CVE-2026-34486, the unauthenticated Java-deserialization RCE in Apache Tomcat Tribes. Watchtower originally newsed the CVE on 2026-05-20 at score 7. Framework-module availability historically correlates with broader opportunistic exploitation within days — Tomcat is widely deployed and the Tribes channel is occasionally exposed by misconfiguration to networks the operator did not intend.

**Mitigation:**
- Apply the Tomcat update fixing CVE-2026-34486 across the fleet.
- Audit every Tomcat cluster for the Tribes channel port (`org.apache.catalina.tribes.transport.ReceiverBase.port`, default `4000`) reachable from anything other than the intended cluster peer subnet.
- Set / verify Tomcat replication channel ACLs.
- Add Tomcat Tribes exploit-attempt detection (deserialised-Java markers on the Tribes port) to network monitoring.

**Sources:** [Rapid7 Metasploit Weekly Wrap-Up — Apache ActiveMQ RCE, Gogs Rebase RCE, Windows Kernel Pointer Enum](https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-05-06-2026/)

---

## 🟡 MEDIUM

*(No standalone MEDIUM items today — see Noted for tracking-only entries; today's signal is dominated by the Critical / High batch above.)*

---

## 📋 Noted / Monitoring

**CVE-2026-11645 — Chrome V8 zero-day patched (5th of 2026)** — Out-of-bounds R/W in V8 actively exploited via crafted HTML; ASLR-bypass + sandbox-execute primitive. Browser-sandbox scope only (out of Watchtower core scope per browser-only exclusion) but the 5-zero-day-in-six-months cadence is itself a calibration signal. Patched Chrome 149.0.7827.102 (Windows / Linux) and 103 (Mac).

**CVE-2026-23111 — Linux kernel nf_tables UAF (LPE + container escape, public PoCs)** — Single-character inverted check in nf_tables creates a UAF; Ubuntu 22.04/24.04, Debian Bookworm/Trixie, RHEL 10, Amazon Linux, SUSE all affected; kernel-patched upstream 2026-02-05 but multi-distro reboot rollouts lag. Exodus Intelligence (2026-06-08) + FuzzingLabs (April 2026) PoCs both public. Local component only — relevant for shared-tenant container hosts running cgroup-v1 or namespaces-enabled kernels; confirm distro kernel package is current and reboots scheduled.

**Microsoft Defender "RoguePlanet" SMB-share race condition — researcher PoC, no CVE, no patch** — Nightmare Eclipse released a PoC exploiting a Defender race condition during handling of remote SMB-share files; on success the exploit spawns a SYSTEM-level command prompt (EoP not RCE). Microsoft silently hardened related Defender APIs in mid-May to block earlier junction vectors but this race remains unpatched. ThreatLocker recommends application allow-listing as compensating control.

**CVE-2026-52806 — Gogs authenticated RCE via argument injection (Rapid7 2026-06-08)** — Authenticated Git-server users can chain argument injection in Gogs to RCE; patch shipped 2026-06-07. Corporate-fleet relevance only if Gogs is used as an internal Git server (rather than GitLab / Gitea / GitHub Enterprise).

**CVE-2026-10523 — Ivanti Sentry CVSS 9.9 (PT-2026-47807 / dbugs.ptsecurity.com 2026-06-09)** — PT Security DB indexes a CVSS 9.9 Ivanti Sentry CVE on 2026-06-09 with no public technical detail yet. Ivanti edge-gateway components have a strong history of CISA KEV adds; flag for promotion when an Ivanti advisory or PoC surfaces.

**CVE-2026-47643 — Microsoft Azure Stack Edge CVSS 9.8 (PT-2026-48038 / dbugs.ptsecurity.com 2026-06-09)** — Azure Stack Edge CVSS 9.8 published alongside the broader Microsoft Patch Tuesday batch; niche to teams running Azure Stack Edge appliances at the corporate edge — not core fleet but check asset DB.

**CVE-2026-34691 — Adobe Experience Manager Forms CVSS 9.3 (Adobe June 2026 — 123 CVEs total, ~half RCEs)** — Adobe's June 2026 batch addresses 123 vulnerabilities with Experience Manager dominating; AEM is a frequent public-facing CMS, so prioritise updates on any internet-reachable AEM Forms or Sites endpoints.

**CVE-2026-45447 + OpenSSL June batch — 18 CVEs including high-severity AI-discovered flaw (PT-2026-47844)** — OpenSSL's June 2026 batch addresses 18 vulnerabilities including a high-severity issue reportedly identified by AI; broad-blast-radius distro-rebuild rollout — pin to your distro patch-cadence for the week.

**Apache HTTP Server June 2026 batch — 13 CVEs (oss-security 2026-06-08)** — CVE-2026-29167 mod_ldap UAF, CVE-2026-29170 mod_proxy_ftp XSS, CVE-2026-34355 mod_proxy_html buffer overflow, CVE-2026-34356 ProxyPassReverseCookieMap buffer overflow, CVE-2026-42535 mod_dav_fs protected directory access, CVE-2026-42536 mod_xml2enc heap overflow, CVE-2026-43951 OOB read merge_response_headers, CVE-2026-44119 .htaccess expression EoP, CVE-2026-44185 mod_ssl OCSP stack over-read, CVE-2026-44186 mod_proxy_ftp loop, CVE-2026-44631 regex heap underflow, CVE-2026-48913 mod_http2 memory corruption, CVE-2026-49975 mod_http2 DoS. No in-wild exploitation reported — apply httpd rebuilds across edge fleets.

**CVE-2026-9669 — CPython bz2.BZ2Decompressor stack buffer overflow (oss-security 2026-06-08)** — Stack corruption triggered by reusing a BZ2Decompressor after an error condition; flag if Python build artifacts surface in product SBOMs.

**CVE-2026-49818 — Apache Airflow Samba provider GCS-object-name path traversal (oss-security 2026-06-09)** — Niche scope — affects only Airflow deployments using both Samba + GCS providers; patch when Samba-provider bump lands.

**Apache Answer multi-CVE batch CVE-2026-34905 → CVE-2026-25688 (oss-security 2026-06-09)** — Six issues in the Apache Answer Q&A platform including unlisted-question access, HTML / XSS injection, avatar validation, TIFF processing, and authorization bypass.

**Xen Security Advisories XSA-491 → XSA-494 (oss-security 2026-06-09)** — x86 HVM port traversal, domctl lock abuse, ARM memory completion, mapcache metadata; VM-isolation scope is out of Watchtower core scope per the scope note but Xen XSAs propagate into multiple cloud-IaaS substrates — track via your IaaS provider's CVE feed.

**CERT/CC VU#616257 — Microsoft-signed UEFI shim bootloaders vulnerable to Secure Boot bypass (2026-06-09)** — Firmware-rollout cadence is months-long but track for any preboot integrity claims in the SOC threat model.

**CVE-2025-8088 — WinRAR path-traversal continued Russia-aligned exploitation against Ukrainian orgs (THN 2026-06-09)** — Russia-aligned actors continue exploiting the July-2025-patched NTFS-ADS path traversal; incremental campaign-continuation reporting, no scope or capability change since Watchtower NOTED 2026-06-03.

**Shai-Hulud / Miasma / Hades supply-chain campaign — 73 compromised Microsoft GitHub repos + 19 PyPI packages (BleepingComputer + THN 2026-06-08/09)** — Information-stealer / credential-harvester payload distributed via 73 compromised repos across Microsoft GitHub orgs (Miasma) plus 19 PyPI packages using setup.pth + obfuscated JS (Hades / Shai-Hulud). Remove cached dependencies and rotate developer secrets if any of the listed packages were installed since 2026-06-04.

**ServiceNow customer-instance data exposure via /api/now/related_list_edit/create unauthenticated endpoint (BleepingComputer 2026-06-09)** — Patched 2026-06-05, ServiceNow evaluating CVE assignment. requires_authentication=false misconfiguration allowed unauthenticated queries against customer instance tables; affected customers were notified via support cases — verify whether your tenant received a notice and review IP 51.159.98.241 in API access logs.

**Tchap French government encrypted messaging breach (BleepingComputer 2026-06-09)** — Account-hijack of a Tchap (Matrix-based) user; no protocol-level CVE. Flag for org-policy / threat-model parallels if your team runs Matrix / Element infrastructure.

**WhatsApp / Meta blocks NSO Group spear-phishing + files contempt motion (BleepingComputer + THN 2026-06-08)** — Meta detected and disrupted an NSO spear-phishing campaign targeting WhatsApp users and filed contempt-of-court motion for permanent-injunction violation. Useful policy signal for executive-protection programs.

**Self-replicating AI worm research PoC on open-weight LLMs (University of Toronto, THN 2026-06-09)** — Academic PoC of an autonomous LLM-driven worm that identifies vulnerabilities and replicates across networks using open-weight models; calibration data point for AI-enabled-attack threat model entries — no live deployment observed.

**FROST attack — JavaScript SSD-timing side-channel for cross-site tracking (THN 2026-06-09)** — In-browser JS leaks which sites are open / which apps are running via SSD contention timing, no permissions required; privacy-side-channel research with limited corporate-defender action.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog, cisa.gov/news-events/alerts/* fallback | ❌ catalog 403 / ✅ news-events fallback worked (KEV add for CVE-2026-50751 confirmed) |
| Vendor advisories | msrc.microsoft.com/blog, fortinet.com/blog/threat-research, rapid7.com, securitylab.github.com | ⚠️ msrc / ✅ rapid7 (Patch Tuesday + Metasploit wrap-up) / ⚠️ fortinet (no June 8-10 content) / ⚠️ securitylab (no June 8-10 content) |
| Research / OSINT | schneier.com, krebsonsecurity.com, googleprojectzero.blogspot.com, blog.cloudflare.com/tag/security, avleonov.com, dbugs.ptsecurity.com, opencve.io | ✅ schneier, krebs, cloudflare, dbugs.ptsecurity / ⚠️ projectzero, avleonov, opencve |
| Supply chain | github.com/search?q=CVE, github.com/0xMarcio/cve | ✅ both |
| Threat intel | seclists.org/fulldisclosure, packetstormsecurity.com, kb.cert.org/vuls, attackerkb.com, hackerone.com/hacktivity, bugcrowd.com/disclosures, nvd.nist.gov, cve.mitre.org, cve.org, habr.com/ru/companies/tomhunter, teletype.in/@cyberok, cert.gov.ua | ✅ seclists (SYSS-2026-004 + SEC Consult Genetec) / ✅ kb.cert.org (VU#616257) / ❌ unreachable: attackerkb, hackerone, bugcrowd, cve.mitre.org, cve.org / ⚠️ degraded: packetstorm, nvd, habr, teletype, cert.gov.ua |

**Errors:**
- cisa.gov — 403 Forbidden (persistent; KEV info obtained via news-events fallback URL and THN / BleepingComputer relay)
- cisa.gov/known-exploited-vulnerabilities-catalog — 403 Forbidden (persistent)
- attackerkb.com — 403 Forbidden (recurrent)
- bugcrowd.com/disclosures — 404 Not Found (page structure persistently changed)
- hackerone.com/hacktivity — JS-only listing (no content via WebFetch)
- cve.mitre.org — JS-only redirect to cve.org (no content via WebFetch)
- cve.org — JS-only (no listing data via WebFetch)
- Degraded (reachable but no June 8-10 content or stale): packetstorm.news (advisory-page redirect / homepage only), msrc.microsoft.com/blog (navigation only, no post listing), nvd.nist.gov (only API-deprecation timeline returned), googleprojectzero / projectzero.google (latest 2026-05-13), fortinet.com/blog/threat-research (latest 2026-06-04), securitylab.github.com (latest 2026-05-22), opencve.io (returned 2023 CVE results), avleonov.com (latest 2026-06-05), habr.com/ru/companies/tomhunter (latest 2026-03-06), teletype.in/@cyberok (latest 2026-02-04), cert.gov.ua (no listing visible)

**CISA KEV:** ~1,542 entries total. New since Watchtower 2026-06-08:
- **CVE-2026-50751 (Check Point Remote Access VPN / Mobile Access / Spark) — added 2026-06-09 with 3-day deadline 2026-06-11** — promoted to CRITICAL above.
- **CVE-2026-42271 (BerriAI LiteLLM MCP-test command injection) — added 2026-06-08/09** — promoted to HIGH above. First AI-platform CVE in 2026 KEV catalog.

---

*Watchtower vulnerability-researcher | Cycle: 2026-06-10/night | Next: 2026-06-11/night*
