# Watchtower Night Report — 2026-07-03
**Cycle:** Night | **Generated:** 2026-07-03 00:00 UTC (2026-07-03T00:00:00Z)
**Sources checked:** 22/30 | **CISA KEV total:** unreached (cisa.gov 403) | **New KEV additions:** CVE-2026-45659 (SharePoint) 2026-07-02, CVE-2026-33825 (BlueHammer/Defender) 2026-06-30 update

---

## 🔴 CRITICAL

### Microsoft SharePoint CVE-2026-45659 (CVSS 8.8) — Deserialization RCE Added to CISA KEV 2026-07-02 With 3-Day BOD 26-04 Federal Deadline; Storm-2603 Warlock Ransomware Attributed Actor
**Product:** Microsoft SharePoint Server (Subscription Edition, 2019, Enterprise 2016) | **CVE:** CVE-2026-45659 | **Status:** Patched (May 2026) | **Active Exploitation** | **KEV**

Microsoft SharePoint Server carries an authenticated RCE via unsafe deserialization of untrusted data. The attacker needs only Site Member (PR:L) permissions and network access — no admin credentials. Microsoft's own advisory rated exploitation "less likely," but CISA added the CVE to KEV on 2026-07-02 after Storm-2603 was seen weaponizing it to deploy Warlock ransomware. Patches shipped 2026-05-21 (initially omitted from the May Patch Tuesday cumulative bundle then added out-of-band). Shadowserver tracks ~10,000 SharePoint servers exposed on the public internet at the time of the KEV add, patch state unknown.

**Timeline:** Patch released 2026-05-21 → mainstream KEV addition 2026-07-02 → BOD 26-04 3-day FCEB deadline 2026-07-04 (Saturday).

**Why it matters:** SharePoint is a canonical enterprise collaboration platform hosting sensitive documents, HR data, and inter-team communications; Storm-2603's Warlock activity has been ransomware-oriented since mid-2025 and the target profile (SharePoint compromise → Warlock deployment) is a clean fit for downstream extortion. This is the **11th** SharePoint CVE on KEV since 2021 (seven previously ransomware-linked) — treat SharePoint on the same 24-48h patch SLA as perimeter VPN/edge appliances.

**Discovered by:** Microsoft (internal); exploitation surfaced by Microsoft Threat Intelligence.

**Mitigation:**
- Confirm the May 2026 SharePoint Server updates (KB5045870 / KB5045871 / KB5045872 depending on edition) are applied on every SharePoint farm, including DR/passive nodes.
- Restrict Site Member creation and audit low-privilege accounts on internet-facing SharePoint tenants; deserialization RCE from Site Member is a "any account = RCE" primitive.
- Enable and archive AntiMalware Scan Interface (AMSI) integration for SharePoint 2019/SE; hunt IIS w3wp.exe → cmd.exe/powershell.exe process chains for the last 60 days.
- For any internet-exposed SharePoint that did not patch in the May → July window, treat the host as **assumed compromised**, isolate, and run a Warlock-specific IR sweep.

**Sources:** [TheHackerNews — SharePoint RCE CVE-2026-45659 Added to CISA KEV](https://thehackernews.com/2026/07/sharepoint-rce-cve-2026-45659-added-to.html) | [BleepingComputer — CISA: Microsoft SharePoint RCE flaw now actively exploited](https://www.bleepingcomputer.com/news/security/cisa-microsoft-sharepoint-rce-flaw-now-actively-exploited/) | [SecurityWeek — CISA Warns of Actively Exploited Microsoft SharePoint Vulnerability](https://www.securityweek.com/cisa-warns-of-actively-exploited-microsoft-sharepoint-vulnerability/)

---

### New CitrixBleed CVE-2026-8451 (CVSS 8.8) NetScaler SAML IDP Memory Disclosure — Exploited Within 24 Hours of Public Disclosure
**Product:** Citrix NetScaler ADC / NetScaler Gateway configured as SAML IDP | **CVE:** CVE-2026-8451 | **Status:** Patched (2026-07-01) | **Active Exploitation** | **PoC Public**

Citrix disclosed a new NetScaler memory-disclosure vulnerability on 2026-06-30 and shipped patches on 2026-07-01. The XML parser inside the SAML IDP handler fails to terminate unquoted XML attribute values that are followed by a newline character; a crafted `<samlp:AuthnRequest>` padded with 476 spaces + newline leaks restricted memory (pointer values, session material) — the same primitive pattern as the original 2023 CitrixBleed and CitrixBleed 2. Lupovis detected two distinct attacker campaigns probing `/saml/login` and delivering payload within 24 hours of vendor disclosure. No authentication is required for the memory read.

**Timeline:** Vendor advisory + PoC-adjacent detail 2026-06-30 → mainstream reporting + first observed in-wild exploitation 2026-07-01 → Citrix out-of-band patches (14.1-72.61, 13.1-63.18, FIPS variants) 2026-07-01.

**Why it matters:** NetScaler is the same class of edge-authentication appliance as the FortiGate SSL VPN cluster that produced FortiBleed — memory-disclosure primitives against these platforms directly convert to session-hijack and MFA-bypass. The 24-hour disclosure-to-exploitation gap makes this a "patch today or unplug" event, and Anubis-affiliate ransomware groups have separately been reported abusing the original CitrixBleed 2 (CVE-2025-5777) alongside this new variant — assume both are in active use.

**Discovered by:** Not publicly attributed at time of writing; detection confirmed by Lupovis.

**Mitigation:**
- Apply Citrix's 2026-07-01 out-of-band patches (NetScaler ADC/Gateway 14.1-72.61 and 13.1-63.18; FIPS 14.1-72.61 FIPS and 13.1-37.272) as an emergency change.
- If patching is delayed even 24 hours, **disable the SAML IDP function** entirely and switch users to an alternate SSO path.
- Monitor NetScaler webserver logs for `/saml/login` requests with unusually large `AuthnRequest` bodies (>500 bytes of whitespace).
- Rotate NSC_TASS cookies and force reauth for all NetScaler-fronted applications; assume session material for the last 72 hours may be in attacker hands.
- Cross-check for indicators of the original CitrixBleed 2 (CVE-2025-5777) which Anubis-linked ransomware is also actively probing.

**Sources:** [SecurityWeek — New CitrixBleed Vulnerability Exploited Immediately After Public Disclosure](https://www.securityweek.com/new-citrixbleed-vulnerability-exploited-immediately-after-public-disclosure/) | [SecurityWeek — Citrix Patches NetScaler Vulnerabilities, Including New 'HTTP/2 Bomb' Attack](https://www.securityweek.com/citrix-patches-netscaler-vulnerabilities-including-new-http-2-bomb-attack/) | [TheHackerNews — Ransomware Groups Turn to Citrix Bleed 2](https://thehackernews.com/2026/07/ransomware-groups-turn-to-citrix-bleed.html)

---

### Oracle E-Business Suite CVE-2026-46817 (CVSS 9.8) — Unauth Pre-Auth RCE In Payments / File Transmission Component; ~950 Instances Exposed, Active Exploitation Confirmed
**Product:** Oracle E-Business Suite Payments — File Transmission component | **CVE:** CVE-2026-46817 | **Status:** Patched (May 2026 CPU) | **Active Exploitation**

Oracle EBS Payments carries an unauthenticated pre-auth code-execution vulnerability in the File Transmission component. CVSS 9.8, low attack complexity, no privileges required, network vector. Oracle patched in the May 2026 Critical Security Patch Update; on 2026-06-27→2026-06-30 Defused observed first active exploitation attempts against exposed instances despite no prior public PoC. Approximately **950 Oracle EBS instances remain internet-facing** and patch status is unknown.

**Timeline:** Oracle May 2026 CPU patch → Defused first-observed exploitation weekend of 2026-06-27 → mainstream reporting 2026-07-01.

**Why it matters:** Oracle EBS runs financial, payments, and HR business processes for a substantial share of large enterprises; a pre-auth RCE in the Payments module is precisely the primitive that Clop / ShinyHunters / other extortion actors used against Oracle EBS in 2023-2024 and against PeopleSoft in May 2026. The 2-month window between patch and observed exploitation continues the pattern: **any Oracle EBS instance still unpatched at 60 days is at material risk**.

**Discovered by:** Not publicly attributed; exploitation surfaced by Defused threat intel.

**Mitigation:**
- Apply the Oracle May 2026 Critical Patch Update to all EBS instances on any of the 12.2, 12.1, 11i lines; verify the Payments / File Transmission component patches are on the applied bundle.
- For internet-facing EBS: front the Payments endpoint with a WAF / reverse-proxy and block unauthenticated File Transmission POSTs pending patch.
- Hunt EBS application logs for File Transmission requests from external IPs during the 2026-05 → present window; treat any successful non-partner-IP transmission call as a compromise indicator.
- Rotate database and integration credentials touched by any potentially-compromised EBS instance; check for the Clop/ShinyHunters pattern of quiet exfil-before-extortion.

**Sources:** [BleepingComputer — Over 900 Oracle E-Business instances exposed to ongoing attacks](https://www.bleepingcomputer.com/news/security/over-900-oracle-e-business-instances-exposed-to-ongoing-attacks/)

---

### Microsoft Defender CVE-2026-33825 'BlueHammer' Now Weaponized By Ransomware Gangs — LPE SAM-Read → SYSTEM Escalation Primitive Confirmed In Multiple Ransomware Chains
**Product:** Microsoft Defender for Endpoint (all supported Windows platforms) | **CVE:** CVE-2026-33825 | **Status:** Patched (April 2026 Patch Tuesday) | **KEV + Ransomware Update**

Originally disclosed April 2026, patched 2026-04-14, and added to CISA KEV on 2026-04-22 (14-day FCEB deadline). On 2026-06-30 CISA updated the KEV entry to flag ransomware-gang exploitation and BleepingComputer / SecurityWeek followed with confirmation. The bug is a Defender-local privilege escalation that grants read access to the SAM database, enabling LSA-secret theft and SYSTEM escalation. Originally leaked by researcher "Nightmare Eclipse" as part of a Microsoft-critical disclosure batch. Ransomware attribution not yet public but the LPE → SYSTEM → domain-compromise chain is the canonical ransomware precursor.

**Timeline:** Patch 2026-04-14 → KEV 2026-04-22 → ransomware exploitation flagged 2026-06-30.

**Why it matters:** Every Windows endpoint in the fleet runs Defender; a local SAM-read escalation weaponized by ransomware gangs closes the "assumed-post-initial-access" chain to SYSTEM on ~any host that missed the April patch. On unpatched fleets, an infostealer or phishing landing that gives one user-level foothold now escalates trivially to domain-wide ransomware deployment.

**Mitigation:**
- Confirm the April 2026 Patch Tuesday updates are applied to every Windows endpoint including offline / rarely-connected devices; report percentage-compliance to leadership.
- Rotate all local admin passwords and re-seed LAPS in the last 60 days on any host that lagged the April patch.
- Hunt Defender exploitation IOCs — Nightmare Eclipse's original PoC and derivative Rust ports have been public since May 2026; endpoint EDR should carry detection.
- Treat any host that took the April patch >30 days late as potentially SAM-compromised — force a domain credential rotation for all accounts that touched that host.

**Sources:** [BleepingComputer — CISA: Windows BlueHammer flaw now exploited by ransomware gangs](https://www.bleepingcomputer.com/news/security/cisa-windows-bluehammer-flaw-now-exploited-by-ransomware-gangs/) | [SecurityWeek — BlueHammer Vulnerability Exploited in Ransomware Attacks](https://www.securityweek.com/bluehammer-vulnerability-exploited-in-ransomware-attacks/)

---

## 🟠 HIGH

### 🔄 UPDATE — Cisco Catalyst SD-WAN CVE-2026-20245: Mandiant Confirms Zero-Day Exploitation ≥ 2 Months Pre-Disclosure With Full Root-Chain Via 'troot' Account Persistence
**Product:** Cisco Catalyst SD-WAN Manager (vManage) | **CVE:** CVE-2026-20245 | **CVSS:** 7.8 (revised down from initial 9.0) | **Previous score:** 9 | **New score:** 9

Mandiant published a follow-up ETR confirming that CVE-2026-20245 (originally covered on 2026-06-06 as an unpatched zero-day and again on 2026-06-11 after KEV addition) was exploited **at least two months before public disclosure** — two distinct campaign windows: late 2025 → January 2026, and again March 2026. Attackers achieved the full root chain: admin-credential acquisition → upload of a crafted `evil_tenant.csv` → command-injection privilege escalation → creation of hidden root account `troot`. Anti-forensics observed: modified files deleted and configuration changes reversed. Target was an unspecified communications service provider. This is a **material change** on our prior coverage: the pre-disclosure exploitation window and the specific persistence artifact (`troot` account) are new operational IoCs.

**Mitigation:**
- Reconfirm CVE-2026-20245 patches applied per Cisco advisory (previously covered) and verify the fixed release train is running on all vManage nodes.
- Hunt every vManage node for hidden root accounts named `troot` or lookalike (`root2`, `_root`, etc.) — the Mandiant IoC is durable and low-effort.
- Search vManage upload logs for filenames matching `evil_tenant.csv` or unauthorized CSV uploads back to late-2025.
- Assume any vManage instance operated as an MSP-shared appliance is potentially compromised — rotate credentials, re-issue certs, and re-baseline configuration.
- Extend hunt window to **≥ 8 months** (late 2025 → present), not the usual 30-day IR window.

**Sources:** [TheHackerNews — Cisco Catalyst SD-WAN Zero-Day CVE-2026-20245 Exploited to Gain Root Access](https://thehackernews.com/2026/06/cisco-catalyst-sd-wan-zero-day-cve-2026.html)

---

### 🔄 UPDATE — Cisco Unified Communications Manager CVE-2026-20230: Cisco Confirms In-The-Wild Exploitation With PoC Available Since June Advisory
**Product:** Cisco Unified Communications Manager | **CVE:** CVE-2026-20230 | **CVSS:** 8.6 | **Previous score:** 6 | **New score:** 8

Cisco updated its June 2026 CVE-2026-20230 advisory on 2026-07-02 to confirm active exploitation in the wild. Original coverage (2026-06-06 report) noted the flaw as an unauthenticated static-credentials root-access issue in the Session Management SSH interface; a public PoC was available at initial disclosure but Cisco had not yet observed exploitation. First in-wild activity now observed. This is a **material change**: adding confirmed exploitation escalates urgency for any UC deployment that has not yet patched.

**Mitigation:**
- Confirm CVE-2026-20230 patches (per Cisco advisory) applied to all UCM 15.0.1 SU2/SU3 nodes; verify fixed release train.
- Rotate SSH keys and administrative credentials on any UCM node that took the patch after the June disclosure window.
- Restrict UCM Session Management SSH endpoint (port 22) to a management VLAN; treat any DMZ/internet-exposed UCM SSH as an emergency P0 misconfiguration.
- Hunt for SSH root logins from non-administrative IPs across the last 60 days on all UCM appliances.

**Sources:** [BleepingComputer — Cisco finally confirms attackers exploiting Unified CM flaw](https://www.bleepingcomputer.com/news/security/cisco-finally-confirms-attackers-exploiting-unified-cm-flaw/) | [SecurityWeek — Cisco Confirms In-the-Wild Exploitation of Unified CM Vulnerability](https://www.securityweek.com/cisco-confirms-in-the-wild-exploitation-of-unified-cm-vulnerability/)

---

### 🔄 UPDATE — FortiBleed Now Directly Fueling INC + Lynx Ransomware; 430,000 FortiGate Compromises, 110M Credentials, 12 Confirmed Ransomware Deployments
**Product:** Fortinet FortiGate SSL VPN | **CVE:** None assigned | **Previous score:** 9 | **New score:** 10

Original FortiBleed coverage (2026-06-18 report) documented ~75K FortiGate URLs and 1.16B credential attempts logged on an exposed attacker server. SOCRadar's follow-up now attributes the campaign to **~20 likely-Russian-based initial-access brokers** operating a FortigateSniffer network sniffer since February 2026, harvesting **>110M credentials** across **>430,000 FortiGates in 150 countries**. Attribution now direct to two ransomware families: **INC Ransom** and **Lynx**. Attack chain: 11,250 portals scanned → 409 admin-level footholds → 354 full attack chains completed (VPN → domain controller → domain admin) → 12 completed ransomware deployments encrypting hundreds of endpoints each. This is a **material change** from the original disclosure: attribution + downstream ransomware pipeline confirmed, and Bob Diachenko's original number (73,932 URLs) is now revised to a wider fleet.

**Mitigation:**
- Continue the credential-rotation and hash-cracking assumption from the original 2026-06-18 advisory; extend the compromise window to **≥ February 2026** (per the FortigateSniffer campaign start), not the original assumed 2025 dump.
- Rotate FortiGate admin credentials, VPN user passwords, MFA seeds, and any credentials that transited FortiGate SSL VPN authentication in the last 5 months.
- Assume domain-controller-adjacent credentials have been exfiltrated on any FortiGate in the affected list; run enterprise-wide krbtgt reset + Golden Ticket hunt.
- Hunt for INC Ransom and Lynx IOCs (public via Huntress, ReliaQuest, SOCRadar) on all internal Windows fleets that historically authenticated through FortiGate SSL VPN.

**Sources:** [BleepingComputer — FortiBleed credential-theft campaign linked to Lynx ransomware](https://www.bleepingcomputer.com/news/security/fortibleed-credential-theft-campaign-linked-to-lynx-ransomware/) | [SecurityWeek — FortiBleed Campaign Linked to INC, Lynx Ransomware Attacks](https://www.securityweek.com/fortibleed-campaign-linked-to-inc-lynx-ransomware-attacks/) | [TheHackerNews — FortiBleed Credential Theft Linked to INC and Lynx Ransomware Operations](https://thehackernews.com/2026/07/fortibleed-credential-theft-linked-to.html)

---

### Adobe ColdFusion + Campaign Classic July 2026 Emergency Patches — Seven CVSS 10/10 CVEs Including CVE-2026-48286 Campaign Classic Auth Bypass + Six ColdFusion Max-Severity Flaws
**Product:** Adobe ColdFusion 2025 / 2023 + Adobe Campaign Classic | **CVE:** CVE-2026-48286 (Campaign Classic, CVSS 10), CVE-2026-48313 + CVE-2026-48315 (ColdFusion path traversal, CVSS 9.3) + 6 additional 10/10 ColdFusion CVEs (unrestricted file upload / input validation / path traversal) | **CVSS:** 10, 9.3, 10x6 | **First reported:** 2026-07-01

Adobe shipped emergency patches on 2026-07-01: eleven ColdFusion CVEs total (six at max severity 10/10 covering unrestricted file upload of dangerous types, improper input validation, and path traversal) plus a single CVSS 10/10 Campaign Classic auth-bypass CVE-2026-48286 (patched in Campaign Classic 7.4.3 build 9397). Additional lesser severity issues: SSRF + XSS in ColdFusion. Adobe rated all patches Priority 1 (patch immediately); no active exploitation known **at time of disclosure**, but ColdFusion has been a repeated targeting-of-choice for Clop / affiliates every time a critical CVE hits.

**Mitigation:**
- Patch ColdFusion 2025 → Update 10, ColdFusion 2023 → Update 21, Campaign Classic → 7.4.3 build 9397 immediately.
- Any internet-facing ColdFusion instance should be treated as a **24-hour patch SLA** — Adobe P1 + CVSS 10 unrestricted upload + zero authentication is the exact primitive Clop uses.
- Audit ColdFusion `.\wwwroot` and application-server temporary directories for unexpected uploaded files during the last 48h; hunt for JSP webshells and cmd/PowerShell child processes.
- For Campaign Classic: rotate admin credentials and audit user-account additions from the disclosure window forward.

**Sources:** [SecurityWeek — Adobe Patches Critical ColdFusion, Campaign Classic Vulnerabilities](https://www.securityweek.com/adobe-patches-critical-coldfusion-campaign-classic-vulnerabilities/)

---

### Langflow CVE-2025-3248 (KEV since May 2025) Weaponized End-To-End By AI Agent — First Publicly-Documented Full-Chain Ransomware Attack Autonomously Run By An LLM Operator ('JADEPUFFER')
**Product:** Langflow (open-source AI application builder) | **CVE:** CVE-2025-3248 | **CVSS:** 9.8 (missing authentication → unauth RCE) | **First reported:** 2026-07-02

Sysdig documented what it believes is **the first ransomware attack run start-to-finish by an AI agent**. The operator (dubbed JADEPUFFER) used an LLM to autonomously chain: (1) exploit unpatched Langflow via CVE-2025-3248 for unauth RCE, (2) harvest OpenAI / Anthropic / DeepSeek / AWS / Azure / Alibaba / Tencent API keys, (3) laterally move via MinIO default credentials and MySQL as root, (4) install a 30-minute callback scheduled task, (5) encrypt 1,342 Nacos config records and demand Bitcoin. Notably, the AI agent generated a decryption key, displayed it once, then never saved it — **making payment ineffective**, which is category-defining sloppiness that would not survive a human operator. Langflow patched in 1.3.0 and CISA KEV-added the CVE in May 2025; the ongoing exposure is unpatched deployments.

**Mitigation:**
- Inventory all self-hosted Langflow instances and confirm ≥ 1.3.0. Any internet-facing Langflow at CVE-2025-3248-vulnerable version is a **24-hour patch SLA**.
- Move any secret / API key out of Langflow-adjacent MinIO / config stores into a secrets manager (Vault / SecretsHub / KMS-referenced envs), especially cloud provider IAM keys.
- Front any internet-exposed Langflow / AI-agent builder with authenticated reverse-proxy, deny anon access to `/api/v1/*` REST endpoints.
- For our detection engineering: the JADEPUFFER 30-minute scheduled-task callback is a durable IoC pattern for LLM-orchestrated ransomware — build hunts for high-frequency, low-variance outbound POSTs to newly registered domains.

**Sources:** [TheHackerNews — AI Agent Exploits Langflow RCE to Automate Database Ransomware Attack](https://thehackernews.com/2026/07/ai-agent-exploits-langflow-rce-to.html)

---

### 81 Million Login Attempts Against Microsoft 365 / Azure CLI In Two Weeks — Password-Spray Campaign From 'LSHIY' Hosting Cluster Targeting Corporate Tenants
**Product:** Microsoft 365 accounts + Azure CLI tenants | **CVE:** None assigned | **First reported:** 2026-07-01

An unnamed campaign generated **81 million login attempts** against Microsoft 365 accounts and Azure CLI tenants in a two-week window, sourced from a hosting-provider cluster researchers labeled "LSHIY." Sourcing infrastructure is consistent with a Russian-nexus initial-access broker profile. Bulk of the traffic targets Azure CLI (`az login` password flow) and Microsoft 365 legacy OAuth flows, not user-facing OWA — this bypasses many phishing-oriented detections. No compromise numbers published; researcher warning framed as "impact-monitoring guidance for corporate tenants."

**Mitigation:**
- Enforce Conditional Access policies that block legacy authentication and require MFA on Azure CLI + Microsoft 365 signins.
- Turn on Entra ID Smart Lockout at the tenant level and lower default thresholds for high-volume signin failures.
- Alert on unusual signin location or IP-cluster patterns for privileged accounts; if you use Sentinel, activate the "Password Spray" and "Impossible Travel" analytic rules for this window.
- Rotate credentials for any service principal or admin account with a legacy-auth-eligible refresh token from before the campaign start.

**Sources:** [BleepingComputer — Hackers target Microsoft 365 accounts with 81 million login attempts](https://www.bleepingcomputer.com/news/security/hackers-target-microsoft-365-accounts-with-81-million-login-attempts/) | [SecurityWeek — Massive Password Spray Campaign Targeting Azure CLI](https://www.securityweek.com/massive-password-spray-campaign-targeting-azure-cli/)

---

### Argo CD repo-server Internal gRPC Unauth Code-Execution — Unpatched 18 Months After January 2025 Report; Trivial Kubernetes Cluster Takeover Via Kustomize `--helm-command` Redirect
**Product:** Argo CD (Kubernetes GitOps continuous deployment) — demonstrated on v2.13.3 | **CVE:** Not yet assigned | **Status:** UNPATCHED | **First reported:** 2026-07-01

Synacktiv disclosed a longstanding unauth code-execution vulnerability in Argo CD's `repo-server` internal gRPC service. The `GenerateManifest` service has no authentication controls; an attacker with pod-to-pod network reach can send a crafted request that abuses kustomize's `--helm-command` flag to redirect helm binary execution to an attacker-supplied script, yielding arbitrary command execution. The report was submitted to maintainers in **January 2025** and remains unpatched at publication 18 months later. Exploitability requires the Kubernetes NetworkPolicy default-off configuration that the Argo CD Helm chart ships by default — meaning any Argo CD install that did not manually add NetworkPolicies is exposed. Full-cluster takeover via Redis poisoning is the natural next hop.

**Mitigation:**
- Add Kubernetes NetworkPolicies to isolate the Argo CD `repo-server` pod — deny all ingress except from the `argocd-server` and `argocd-application-controller` pods. This is the **only available mitigation** with no patch.
- Audit clusters for other pods sharing the same namespace as Argo CD that could reach the repo-server; treat any compromise of a co-tenant pod as a K8s cluster-admin equivalent.
- Consider re-architecting Argo CD onto a dedicated node pool or a separate cluster if you host untrusted workloads in the same tenant.
- Watch Argo CD Github issues / Synacktiv follow-up for an official CVE / patch; treat this as an active-exploitability risk despite no observed in-wild use.

**Sources:** [TheHackerNews — Unpatched Argo CD Repo-Server Flaw Could Let Attackers Take Over Kubernetes Clusters](https://thehackernews.com/2026/07/unpatched-argo-cd-repo-server-flaw.html)

---

### Ubiquiti UniFi Late-June 2026 Multi-CVE Batch — Two CVSS 10 (CVE-2026-13768 Gardyn, CVE-2026-50746 UniFi Connect) + CVE-2026-55115 Protect SSRF + Six Additional Path-Traversal / SQLi / Access-Control Flaws
**Product:** Ubiquiti UniFi OS / UniFi Network / UniFi Protect / UniFi Connect / Gardyn integration | **CVE:** CVE-2026-13768, CVE-2026-50746, CVE-2026-55115, CVE-2026-55116, CVE-2026-54404, CVE-2026-54406, CVE-2026-54408, CVE-2026-55114 | **CVSS:** 10 / 10 / 9.9 / 9 / 8.8 / 8.7 / 8.6 / 8.8 | **First reported:** 2026-06-30

Ubiquiti shipped a large late-June UniFi update batch. Highest-severity items: **CVE-2026-13768** (CVSS 10) exposes a "privileged iothubowner key" in the Gardyn integration allowing unauthorized device access + command execution; **CVE-2026-50746** (CVSS 10) is an improper access-control → command-injection in UniFi Connect on network-reachable devices; **CVE-2026-55115** (CVSS 9.9) SSRF-to-privesc in UniFi Protect. Additional access-control / path-traversal / authenticated-SQLi bugs cover UniFi OS, UniFi Network, and UniFi Protect. No in-wild exploitation observed; PT Security-adjacent researchers Kelly Patterson + Serhat Yapici surfaced most items.

**Mitigation:**
- Patch UniFi OS / Network / Protect / Connect immediately from Ubiquiti's June 2026 update train; UniFi Cloud Gateway users get patches auto-pushed but confirm.
- Restrict UniFi controller UI to a management VLAN; treat any internet-exposed UniFi controller as pre-compromised.
- Audit UniFi Access + Gardyn integration users and rotate cloud API tokens issued from the vulnerable configuration window.
- Roll new IoT/network device credentials in the last 30 days for UniFi-managed fleets to reset any prior iothubowner-key exposure.

**Sources:** [OpenCVE — Ubiquiti June 2026 Batch](https://app.opencve.io/cve) | [PT Security dbugs.ptsecurity.com — PT-2026-55238 / 55251 / 55233](https://dbugs.ptsecurity.com)

---

### DHS Homeland Security Information Network (HSIN) Breach — Federal-Adjacent Information-Sharing Platform Compromised; Impact To Cross-Sector Threat Intel Partners
**Product:** DHS Homeland Security Information Network (HSIN) — federal↔private information-sharing portal | **CVE:** None assigned | **First reported:** 2026-07-01

DHS publicly confirmed a breach of HSIN, the unclassified information-sharing platform used by federal, state, local, tribal, and private-sector partners for cross-jurisdictional threat intelligence sharing. Scope not yet disclosed — DHS statement acknowledged "unauthorized access to a subset of HSIN data" without volume metrics or timeframe. HSIN carries sector-specific ISACs, law-enforcement bulletins, and inter-agency incident summaries; a compromise here likely exposes tradecraft-relevant TI as well as identities of the partner organizations that receive it.

**Mitigation:**
- If your org receives HSIN feeds or has an HSIN account: rotate HSIN credentials, review recent login history via HSIN portal, and treat any HSIN-shared intel product from the affected window as potentially exposed to the adversary.
- Notify legal/privacy of the confirmed federal-adjacent breach — depending on your industry, HSIN-shared items may include cross-sector PII flows.
- Increase monitoring for social-engineering / spear-phishing traffic that references HSIN-shared advisories; attacker-in-the-middle content is a plausible near-term follow-on.

**Sources:** [BleepingComputer — DHS confirms hackers breached HSIN info-sharing platform](https://www.bleepingcomputer.com/news/security/dhs-confirms-hackers-breached-hsin-info-sharing-platform/)

---

## 🟡 MEDIUM

### 'ChocoPoC' Python RAT Distributed Via Trojanized CVE Proof-of-Concept Repositories — Targeted At Vulnerability Researchers
**Product:** GitHub proof-of-concept exploit repositories (vulnerability-research target audience) | **CVE:** None assigned | **Published:** 2026-07-01

Threat actors are hosting fake CVE PoC repositories on GitHub that carry hidden Python dependency injections which install a Python-based RAT the researchers named "ChocoPoC." Victims are security researchers pulling the fake PoCs into test environments. This continues a **6-year pattern** of North-Korea-linked and China-linked actors targeting researchers via fake PoCs (Lazarus 2021, Ministra 2024) — but ChocoPoC's distribution scope is broader (multiple public repos) and its stealer target set includes GitHub / npm tokens which are directly weaponizable for supply-chain propagation.

**Mitigation:**
- Enforce isolated sandbox for any CVE PoC pulled from an untrusted GitHub repository — VM snapshot or container with no network egress to production / registry credentials.
- Rotate GitHub / npm / registry tokens for any researcher account that has pulled PoCs from repositories opened in the last 30 days without vetted maintainer history.
- Update your researcher-machine tooling to require signed / vetted PoC sources (Metasploit modules, watchTowr labs, security-vendor blogs) rather than search-result GitHub repos.

**Sources:** [BleepingComputer — New ChocoPoC malware targets researchers via trojanized PoC exploits](https://www.bleepingcomputer.com/news/security/new-chocopoc-malware-targets-researchers-via-trojanized-poc-exploits/) | [TheHackerNews — New ChocoPoC RAT Targets Vulnerability Researchers via Fake PoC Exploit Repos](https://thehackernews.com/2026/07/new-chocopoc-rat-targets-vulnerability.html)

---

### 'BioShocking' — New Prompt-Injection Attack Class Hijacks AI Browser Data Flow To Exfiltrate User Session Content
**Product:** AI-powered browsers (agent-integrated Chromium forks) | **CVE:** None assigned | **Published:** 2026-06-30

Researchers disclosed "BioShocking," a novel attack class that manipulates an AI-integrated browser's agentic assistant into exfiltrating user data by injecting crafted content into pages the AI browser reads. The prompt-injection primitive is durable across AI browsers currently in preview from Anthropic / OpenAI / Perplexity / Comet-class launchers. This extends the **Agentjacking pattern** (MEMORY 2026-06-13) from third-party-service inputs (Sentry / Jira) to first-party inputs (any website an AI browser opens). Corporate use of AI browsers is currently limited but growing.

**Mitigation:**
- Do not run AI browsers in the same profile / session as production credentials or corporate SSO; keep AI-browser experimentation in an isolated user profile.
- Wait on rolling AI browsers to the general workforce until vendors publish a defense against prompt-injection from third-party page content (assume 6-12 months).
- If piloting internally: instrument AI-browser network egress with content-inspection to flag exfiltration of session tokens or authenticated response bodies.

**Sources:** [BleepingComputer — New BioShocking attack manipulates AI browser into data theft](https://www.bleepingcomputer.com/news/security/new-bioshocking-attack-manipulates-ai-browser-into-data-theft/)

---

### FBI + Google Seize NetNut / 'Popa' Residential-Proxy Network — 2 Million Compromised TV-Box + IoT Devices, Israeli Publicly-Traded NetNut Ltd Named
**Product:** NetNut residential-proxy platform (Popa botnet infrastructure) | **CVE:** None assigned | **Published:** 2026-07-02

FBI, Google, and Black Lotus Labs coordinated a takedown of **NetNut**, an Israeli publicly-traded residential-proxy company Krebs / BleepingComputer connected to the **Popa botnet** enslaving ~**2M** consumer TV-boxes and IoT devices worldwide. Google described "reducing the network's pool of usable devices by millions." NetNut has been a persistent piece of adversarial infrastructure for password-spray, credential-stuffing, and residential-IP-clean campaigns against corporate SSO — the takedown eliminates a category of TI-visible bad-IP infrastructure that will need weeks to rebuild.

**Mitigation:**
- Expect a temporary drop in residential-proxy-sourced bot traffic against your login endpoints over the next 30-60 days; expect the ecosystem to rebuild on alternate providers within 90.
- Monitor for a shift in campaign attribution as attackers relocate to alternate residential-proxy services (Bright Data / Oxylabs / IPRoyal / etc.); update WAF signatures accordingly.
- Krebs earlier reporting on NetNut identifies the Popa botnet as the residential-node source — treat any historical Popa IoCs as high-fidelity for pre-takedown attribution research.

**Sources:** [BleepingComputer + Krebs — FBI Seizes NetNut Proxy Platform, Popa Botnet](https://krebsonsecurity.com/2026/07/fbi-seizes-netnut-proxy-platform-popa-botnet/) | [TheHackerNews — Google Disrupts NetNut Residential Proxy Network](https://thehackernews.com/2026/07/google-disrupts-netnut-residential.html)

---

### 5-CVE OFFIS DCMTK DICOM Toolkit Batch — CISA-Coordinated Disclosure Covering Medical-Imaging Parsing Vulnerabilities
**Product:** OFFIS DCMTK (DICOM Toolkit for medical imaging) | **CVE:** Multiple (CISA-coordinated batch, IDs pending) | **Published:** 2026-07-01

Abhinav Agarwal disclosed five CISA-coordinated DICOM parsing vulnerabilities in OFFIS DCMTK via oss-security. In our scope only for orgs that operate a healthcare-imaging integration point exposed to internet or third-party file input — otherwise these are downstream medical-device concerns.

**Mitigation:**
- Confirm OFFIS DCMTK version on any DICOM-processing pipeline (PACS integration, imaging-archive ingestion, telehealth apps that accept .dcm uploads) and apply vendor fixes as available.
- Isolate DICOM parsers under seccomp + no-egress container the same way MP4Box gets treated (MEMORY 2026-06-14 lesson).

**Sources:** [openwall oss-security — OFFIS DCMTK 5 CISA-coordinated DICOM vulnerabilities](https://www.openwall.com/lists/oss-security/2026/07/)

---

## 📋 Noted / Monitoring

**CVE-2025-5777 (CitrixBleed 2)** — Anubis-affiliate ransomware groups actively abusing the older CitrixBleed 2 alongside the new CVE-2026-8451; treat both as concurrent NetScaler compromise vectors. (thehackernews.com/2026/07/ransomware-groups-turn-to-citrix-bleed)

**Google Chrome 149 → 149.x — 382 CVEs patched 2026-07-01** — 15 rated Critical including CVE-2026-13779 UAF in Chromoting component. Client-side but push to endpoint fleet.

**Apple iOS / macOS / Safari July 2026 patches** — WebKit + kernel + WebRTC + Web Extensions. Apple Safari 26.5.2 addresses web-extension security issues on Sonoma + Sequoia. Fleet update.

**CVE-2026-54428 + CVE-2026-54399 — Apache HttpComponents Core** — HPackDecoder unlimited-header-list-size before SETTINGS ACK + unbounded HTTP header/line-length in default config. HTTP/2 header handling flaws (openwall 2026-07-01).

**CVE-2026-56016 — Perl CGI::Session::ID::md5 < 4.49** — Predictable session ID generation from weak entropy (openwall 2026-07-01).

**CVE-2025-15646 — Perl HTML::Gumbo < 0.19** — Memory disclosure through type confusion (openwall 2026-07-01).

**CVE-2026-50052 — Varnish Cache HTTP/2 parsing** — Parsing deficiency in HTTP/2 protocol handling (openwall 2026-07-01).

**CVE-2026-54161 — NUT upsmon 2.8.3–2.8.x** — Remote OS command injection via `ups.alarm` parameter; fixed in PR #3499 (openwall 2026-07-01).

**CVE-2026-43503 'DirtyClone' — Linux LPE** — Dirty Frag variant analyzed by Or Peles (openwall 2026-07-02); joins CVE-2026-43284/43500 + CVE-2026-46300 kernel-fragmentation family per MEMORY 2026-06-18 pattern.

**Apache NiFi CVE-2026-44911 / 44913 / 44914 / 54665** — Multiple authorization and validation issues (oss-security 2026-06-20→22).

**Apache ActiveMQ 15-CVE batch** — STOMP protocol flaws + memory exhaustion + XSS (oss-security 2026-06-27→30); extends the 2026-06-10 CVE-2026-42588 Jolokia RCE thread.

**Apache Tomcat 7-CVE batch** — XSS + authentication bypass (oss-security 2026-06-27→30).

**Apache Kvrocks 5-CVE batch** — Permission issues + buffer overflow (CVE-2026-41566, 45188, 46751-46752, 54226) via oss-security 2026-06-25→26.

**Apache Shiro CVE-2026-56091** — Authentication bypass in Guice-Web integration (oss-security 2026-06-23→24).

**Apache Doris CVE-2025-66336** — SQL injection enabling authentication bypass (oss-security 2026-06-20→22).

**libssh2 CVE-2026-55200** — Critical authentication bypass + additional high-severity issues (oss-security 2026-06-23→24).

**libxml2 CVE-2026-6653** — Use-after-free in XML parsing (oss-security 2026-06-20→22).

**libexpat 14-CVE batch** — Integer overflow and out-of-bounds issues (oss-security 2026-06-25→26).

**rsyslog CVE-2026-55556** — imhttp Basic Auth heap overflow (oss-security 2026-06-23→24).

**hostapd out-of-bounds write in Wi-Fi 7 parsing** — Pre-authentication DoS (oss-security 2026-06-27→30).

**curl 8.21.0 multi-CVE batch** — Multiple security advisories (oss-security 2026-06-23→24).

**PowerDNS input-validation deficiencies across multiple components** — oss-security 2026-06-25→26.

**Horde Groupware IMP path traversal / LFI** — Could escalate privileges or bypass auth (Full Disclosure 2026-07-02); in-scope for corporate webmail.

**Control Web Panel ≤ 0.9.8.1224 SQLi via `userRes`** — In-scope for hosting-panel deployments (Full Disclosure 2026-07-02).

**PT-2026-55203 Tr7 Cyber Defense WAF-ASP CVSS 9.8** — dbugs.ptsecurity 2026-06-20→07-03.

**PT-2026-55259 Progress Flowmon CVSS 8.7** — dbugs.ptsecurity 2026-06-20→07-03; watch for CVE assignment.

**PT-2026-56004 OpenSUSE Urild Service CVSS 10.0** — dbugs.ptsecurity 2026-06-20→07-03; watch for CVE assignment.

**VU#639124 Little Orbits GameFirst Anti-Cheat** — Local privilege escalation via kernel driver (CERT/CC 2026-07-02); joins the anticheat-driver pattern with SignalRGB (MEMORY 2026-06-18).

**VU#226679 Microsoft WinRE UEFI/BIOS password bypass** — Recovery environment permits UEFI-password enforcement bypass (CERT/CC 2026-06-22); adjacent to the VU#457458 Secure Boot bypass and VU#616257 UEFI shim thread.

**VU#457458 Vendor-signed UEFI applications Secure Boot bypass** — CERT/CC 2026-06-18; expands the VU#616257 (MEMORY 2026-06-12) Microsoft-signed shim bootloader thread to include broader vendor-signed UEFI applications.

**VU#936962 FastStone Image Viewer 8.3.0.0 multi-file-parsing** — CERT/CC 2026-06-22; client-side, out-of-primary-scope.

**Kubota month-long network intrusion** — Agricultural equipment manufacturer disclosed extended intrusion. No CVE / attribution. (BleepingComputer 2026-07-01)

**Medtronic ShinyHunters breach notifications** — Healthcare-device manufacturer notifying customers post-ShinyHunters compromise; continues the 06-16→06-19 ShinyHunters Salesforce campaign per MEMORY 2026-06-19. (BleepingComputer 2026-07-02)

**One million passports leaked online** — Via low-security cannabis dispensary age-verification database (Schneier 2026-06-26). High-value credential compromise for downstream identity abuse.

**Kodak + Council of Europe + iRhythm + Mackay Sugar + Novo Nordisk + Cal Water — ShinyHunters/FulcrumSec extortion cluster continues** — cluster tracked via MEMORY 2026-06-17→06-19 chain remains active into July.

**Scattered Spider — 19-year-old Peter Stokes extradited from Finland to face US charges (2026-07-01)** — plus two UK operators pleaded guilty on trial day 1 (2026-06-23 per Krebs). Legal-track escalation, no infrastructure change.

**Amadey + StealC botnet takedown — 27M credentials recovered (2026-06-24 → 06-28)** — Microsoft + international law enforcement disrupted shared infra.

**SEO-poisoned software sites → ScreenConnect → AsyncRAT** — 90 domain names across 10 languages (thehackernews.com 2026-07-01); extends the AsyncRAT AI-hype thread from MEMORY 2026-06-12.

**VEIL#DROP → PureLogs stealer via Blogger platform** — Multi-stage delivery abusing legitimate hosting (thehackernews.com 2026-07-01).

**ToddyCat 'Umbrij' malware — Shadow-Token-via-Remote-Debug OAuth abuse of Gmail via Google API** — Corporate email compromise pattern (thehackernews.com 2026-07-02).

**Chrome ad blocker with 10M+ installs found with dormant script-injection capability** — Extension supply-chain risk on the Chrome Web Store surface (thehackernews.com 2026-06-30→07-03).

**Gaslight macOS malware uses prompt injection to disrupt AI-assisted analysis** — First publicly-documented macOS malware family targeting the AI-analyst assumption chain (thehackernews.com 2026-06-30→07-03).

**Chinese framework powers 200,000 investment-scam sites** — Chinese DCloud Uni-App toolkit distributed via scam-template pipeline (SecurityWeek 2026-06-27).

**$3M reportedly stolen in Polymarket third-party-vendor hack** — Decentralized-prediction-market compromise via third-party service (SecurityWeek 2026-06-26).

**Fortinet 'Ousaban' Iberian phishing campaign** — Geofenced targeting of Spain/Portugal (FortiGuard 2026-07-01).

**Shai-Hulud CI/CD → AWS Redshift breach research** — Jenkins-credential compromise → AWS escalation → Redshift data exfil (FortiGuard 2026-06-26); continues the Shai-Hulud/Miasma/Hades thread per MEMORY 2026-06-10.

**Amadey/StealC 27M credentials recovery + Microsoft-and-allies disruption** — SecurityWeek 2026-06-24 (already counted above in law-enforcement bucket).

**Cloudflare — Attribution Business Insights + Self-Managed OAuth for all developers** — Cloudflare Blog 2026-06-24→07-01; ecosystem changes, no immediate action.

**White House post-quantum executive order — 2030 government + industry migration deadline** — Cloudflare Blog 2026-06-23; long-horizon planning input.

**openwall CVE-2026-43503 'DirtyClone' Linux LPE analysis** — already noted above but flagged again as calibration anchor for future kernel-LPE-family disclosures.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ 403 |
| Vendor advisories | rapid7.com, fortinet.com/blog/threat-research, blog.cloudflare.com/tag/security, msrc.microsoft.com/blog | ✅ / ⚠️ msrc empty |
| Research / OSINT | seclists.org/fulldisclosure, opencve.io, app.opencve.io, avleonov.com, dbugs.ptsecurity.com, github.com/0xMarcio/cve, github.com/search?q=CVE, kb.cert.org/vuls, openwall.com/lists/oss-security | ✅ |
| CVE databases | nvd.nist.gov, cve.mitre.org, cve.org | ❌ JS-only |
| Research labs | securitylab.github.com, googleprojectzero.blogspot.com → projectzero.google | ⚠️ no items in window |
| Threat intel / research | schneier.com | ✅ |
| Bug bounty | hackerone.com/hacktivity, bugcrowd.com/disclosures, attackerkb.com | ❌ JS/403/404 |
| Aggregators | packetstormsecurity.com → packetstorm.news | ⚠️ nav-only |
| Regional Tier-2 | habr.com/ru/companies/tomhunter, teletype.in/@cyberok, cert.gov.ua | ⚠️ silent >3-4 months |

**Errors:** cisa.gov (403) + cisa.gov/known-exploited-vulnerabilities-catalog (403) + attackerkb.com (403) + bugcrowd.com/disclosures (404) + hackerone.com/hacktivity (JS-only) + nvd.nist.gov (JS-only) + cve.mitre.org (JS-only redirect to cve.org) + cve.org (JS-only)
**Degraded:** msrc.microsoft.com/blog (empty response body) + packetstormsecurity.com (nav-only) + securitylab.github.com (no items in window) + projectzero.google (no items in window) + habr.com/ru/companies/tomhunter (silent 3.4-month per MEMORY) + teletype.in/@cyberok (silent 4.4-month per MEMORY) + cert.gov.ua (empty)
**CISA KEV:** Direct cisa.gov unreachable — KEV signal derived from BleepingComputer + SecurityWeek + TheHackerNews cross-reference. Confirmed adds in period: **CVE-2026-45659** (SharePoint RCE) 2026-07-02, **CVE-2026-33825** (BlueHammer) update flagging ransomware exploitation 2026-06-30.

---

*Watchtower vulnerability-researcher | Cycle: 2026-07-03/night | Next: 2026-07-04/night*
