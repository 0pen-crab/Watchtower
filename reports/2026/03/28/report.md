# Vulnerability Research Report
**Date:** 2026-03-28 | **Cycle:** Night (02:00 Europe/Athens)
**Sources Checked:** 34 / 34 | **New Findings:** 22 | **Updates:** 1

---

## 🚨 CRITICAL FINDINGS

### 1. TeamPCP Evolves Into Mass-Scale Ransomware Syndicate: Vect RaaS + BreachForums 300K Affiliate Program
**Threat Score: 10/10**
- TeamPCP has formally partnered with Vect ransomware-as-a-service and BreachForums, announcing that all ~300,000 registered BreachForums users will receive personal Vect affiliate keys.
- Operational model: TeamPCP provides stolen credentials/initial access from supply chain packages → Vect provides encryption and extortion tooling → BreachForums provides the operator base.
- Analysts (SANS ISC, Cybernews, Infosecurity Magazine) assess this as an unprecedented convergence: supply chain compromise + RaaS + dark web forum mobilization at scale never before observed.
- **Action:** Organizations exposed to ANY TeamPCP-compromised component (Trivy, KICS, LiteLLM, Telnyx) must treat all credentials as distributed to 300,000 potential threat actors. Credential rotation is no longer optional — it is critical and urgent.
- **Sources:** SANS ISC Diary 32838, Cybernews, Infosecurity Magazine, Halcyon

### 2. LAPSUS$ Claims 3GB AstraZeneca Breach Using TeamPCP Stolen Credentials (UPDATE)
**Threat Score: 10/10 (was: 8 — TeamPCP/Lapsus$ alliance)**
- LAPSUS$ has publicly claimed a 3GB breach of AstraZeneca, identified as the first confirmed victim from the TeamPCP/LAPSUS$ partnership.
- Claimed stolen data includes internal code repositories, cloud infrastructure configs (AWS, Azure, Terraform), Spring Boot configs, GitHub Enterprise user data, and employee PII.
- LAPSUS$ is offering access/data for sale via Session encrypted messaging.
- AstraZeneca has not confirmed or denied as of publication. DOJ declined immediate comment.
- **Action:** All organizations should not wait for public victim disclosures — if you had TeamPCP-compromised software in your environment, assume breach.
- **Sources:** SecurityWeek, CSO Online, SANS ISC Diary 32838

### 3. CVE-2026-21858 "Ni8mare" — n8n Unauthenticated RCE (CVSS 10.0)
**Threat Score: 10/10**
- **Product:** n8n workflow automation platform (versions 1.65.0–1.120.x)
- **CVE:** CVE-2026-21858 | **CVSS:** 10.0 (Critical)
- A Content-Type confusion vulnerability in n8n's webhook middleware (parseRequestBody()) allows unauthenticated attackers to trigger arbitrary code execution on n8n server instances.
- Combined with CVE-2025-68613 (CVSS 9.9), the full chain allows file read-to-RCE without credentials.
- Estimated impact: ~100,000 n8n servers globally (>100 million Docker pulls). n8n is trending on GitHub today.
- **Patch:** Upgrade to n8n version 1.121.0 immediately.
- **PoC:** Public exploit chain published by Cyera Research (cyera.com), PoC repo on 0xMarcio/cve (259 stars in 24h).
- **Sources:** Cyera Research, NVD, GitHub/0xMarcio

### 4. TeamPCP Telnyx PyPI Compromise — WAV Steganography Delivers Platform-Specific Credential Stealer
**Threat Score: 9/10**
- **Package:** telnyx (PyPI) — 670,000+ monthly downloads
- TeamPCP compromised the Telnyx Python SDK (used by telecom/voice API developers) on March 27, 2026 at ~03:51 UTC, publishing malicious versions 4.87.1 and 4.87.2.
- **Novel TTP:** Payloads hidden in WAV audio files using steganography — "hangup.wav" (Windows) and "ringtone.wav" (Linux/macOS) — a deliberate blend with Telnyx's voice API purpose.
  - Windows: Persistent binary dropped as msbuild.exe in Startup folder
  - Linux/macOS: In-memory credential harvester, self-destructing temp directory
- Exfiltration target: 83.142.209[.]203:8080 via tpcp.tar.gz HTTP POST (same RSA-4096 key as LiteLLM)
- Attribution: Credentials likely obtained by harvesting liteLLM-exposed CI/CD pipelines.
- **Action:** Downgrade to telnyx 4.87.0. Hunt for msbuild.exe in Startup folders, unexpected .wav files, and outbound connections to 83.142.209[.]203.
- PyPI has quarantined both malicious versions.
- **Sources:** THN, BleepingComputer, Aikido, Endor Labs, Ossprey Security, SafeDep, Socket, JFrog, StepSecurity, SANS ISC

### 5. CVE-2025-53521 — F5 BIG-IP CISA KEV Addition (3-Day Patch Deadline: March 30)
**Threat Score: 9/10**
- **Product:** F5 BIG-IP (multiple versions)
- **CVE:** CVE-2025-53521 | Details: unspecified vulnerability class, CISA KEV addition confirms active exploitation.
- CISA added this to the Known Exploited Vulnerabilities catalog on March 27, 2026.
- **Federal agencies must patch by March 30, 2026 (3 days from now).**
- All organizations with internet-facing F5 BIG-IP appliances should treat this as emergency priority.
- **Action:** Apply F5 patches immediately. Check F5 advisory portal for affected versions and patch guidance.
- **Sources:** CISA KEV catalog, NVD

---

## 🔴 HIGH SEVERITY

### 6. LangChain + LangGraph — Three Enterprise Data Exposure CVEs
**Threat Score: 8/10**
- Three independent vulnerabilities in the world's most widely used AI framework (LangChain: 52M+ downloads/week; LangGraph: 9M+/week):
  - **CVE-2026-34070** (CVSS 7.5): Path traversal in langchain_core/prompts/loading.py — reads arbitrary files via prompt template API without authentication.
  - **CVE-2025-68664** "LangGrinch" (CVSS 9.3): Deserialization of untrusted data — attacker can extract API keys and environment secrets via prompt injection crafted as serialized LangChain objects.
  - **CVE-2025-67644** (CVSS 7.3): SQL injection in LangGraph's SQLite checkpoint implementation — arbitrary SQL via metadata filter keys.
- Exploitation grants access to Docker configs, API secrets, cloud credentials, and entire conversation histories.
- **Patches:** langchain-core ≥1.2.22 (CVE-2026-34070), langchain-core 0.3.81/1.2.5 (CVE-2025-68664), langgraph-checkpoint-sqlite 3.0.1 (CVE-2025-67644).
- **Sources:** THN, Cyera Research

### 7. Handala (Iran MOIS) Hacks FBI Director Kash Patel's Personal Email — Confirmed by DOJ
**Threat Score: 8/10**
- Handala (Iran MOIS), previously responsible for the Stryker wiper attack, leaked photographs and emails allegedly stolen from FBI Director Kash Patel's personal email account on March 27.
- The FBI confirmed the breach (calling content "historical in nature") and DOJ confirmed document authenticity.
- Handala claims the hack was retaliation for: (1) FBI's $10M bounty and domain seizure of Handala sites, (2) the sinking of Iranian frigate IRIS Dena by U.S. submarine (March 4).
- Earlier this week, Handala also leaked alleged personal data of Lockheed Martin officials.
- Note: Handala has also released credentials via BreachForums from prior Stryker campaign, but as of this cycle they appear to have a separate operational track.
- **Sources:** The Record, Reuters, SecurityWeek

### 8. CVE-2025-12548 — Eclipse Che machine-exec Unauthenticated RCE (Red Hat OpenShift DevSpaces)
**Threat Score: 8/10**
- **Product:** Eclipse Che machine-exec service (Red Hat OpenShift DevSpaces)
- **CVE:** CVE-2025-12548
- Attacker can connect over WebSocket on port 3333 and execute arbitrary commands via JSON-RPC without authentication.
- Red Hat OpenShift DevSpaces environments are specifically affected — this is a developer environment service with broad network access.
- Metasploit module (`linux/http/eclipse_che_machine_exec_rce`) added to Metasploit Framework in the 03/27 weekly release.
- Public PoC now available; exploitation window is open.
- **Action:** Patch immediately, ensure port 3333 is not internet-exposed, audit DevSpaces environments.
- **Sources:** Rapid7 Metasploit Wrap-Up 03/27, AttackerKB

### 9. CVE-2026-4681 — PTC Windchill Critical ICS Vulnerability (CISA Flagged, German Police Mobilized)
**Threat Score: 8/10**
- **Product:** PTC Windchill (industrial PLM/CAD data management platform)
- **CVE:** CVE-2026-4681 | **Severity:** Critical
- CISA issued an ICS advisory flagging this as a critical vulnerability in PTC Windchill, a widely deployed industrial product lifecycle management platform.
- The vulnerability severity and ICS-wide deployment triggered mobilization of German industrial cybersecurity authorities (BSI/German police), indicating suspected active exploitation or proof-of-concept in the wild.
- **Action:** Patch immediately; isolate PTC Windchill from public internet; audit access logs.
- **Sources:** SecurityWeek, CISA ICS advisories

### 10. Coruna iOS Exploit Kit — Likely Successor to Operation Triangulation
**Threat Score: 8/10**
- SecurityWeek and SANS ISC (podcast 03/27) are reporting a new iOS exploit kit dubbed "Coruna" / "DarkSword," identified as a likely evolution of the Operation Triangulation campaign (APT group suspected: Russian FSB adjacent).
- The exploit kit targets iOS zero-click vulnerabilities including components related to CoreText/MobileSafari and Secure Enclave access (unverified; SANS podcast referenced "DarkSword" as related to Apple's recent iOS patches and "zero-click iOS exploit with Secure Enclave theft").
- Apple has reportedly silently patched related issues in iOS 18.4.1 / iOS 26.4.
- **Action:** Update all Apple devices to the latest iOS version immediately.
- **Sources:** SecurityWeek, SANS ISC Stormcast 03/27

---

## 🟡 MEDIUM SEVERITY

### 11. watchTowr: 150 Abandoned AWS S3 Buckets Received 8M+ Requests — Supply Chain at Scale
**Threat Score: 7/10**
- watchTowr Labs published research demonstrating registration of ~150 abandoned AWS S3 buckets previously used by commercial/open source software products, governments, and CI/CD pipeline infrastructure.
- Over a 2-month period, these buckets received 8 million+ HTTP requests for: software updates, pre-compiled binaries (unsigned), VM images, JavaScript files, CloudFormation templates, and SSLVPN configs.
- Requestors included governments, militaries, space agencies, and major enterprises — if exploited, attackers could have served backdoored updates to all of them.
- This research demonstrates that the SolarWinds-style supply chain attack surface exists at massive scale, driven purely by abandoned cloud storage references in deployed software.
- **Sources:** watchTowr Labs

### 12. Talos: 10 TP-Link AX53 Vulnerabilities + 19 Canva Affinity Vulns + HikVision (All Patched)
**Threat Score: 7/10**
- **TP-Link Archer AX53:** 10 vulnerabilities including CVE-2025-62673 (stack-based buffer overflow in tdpServer via network packet) and 8 vulns in tmpServer opcode — critical for router-based network attacks.
- **Canva Affinity:** 19 vulnerabilities — 18 OOB reads in EMF parsing + CVE-2025-66342 (type confusion → arbitrary code execution via crafted EMF file). Affects graphic designers/document editors.
- **HikVision:** 1 vulnerability (undisclosed class, patched).
- All patched by respective vendors per Cisco's third-party disclosure policy.
- Snort rules available for detection.
- **Sources:** Cisco Talos Blog (03/26/2026)

### 13. European Commission Investigating Breach After Amazon Cloud Account Hack
**Threat Score: 7/10**
- The European Commission launched a formal investigation after an Amazon Web Services cloud account associated with EC infrastructure was compromised.
- Scope: potentially includes internal EU Commission documents and communications stored in AWS environments.
- No attribution confirmed yet. Timing correlates with TeamPCP campaign period.
- **Sources:** BleepingComputer

### 14. CVE-2026-23767 — Epson ESC/POS Network Printer Command Injection
**Threat Score: 6/10**
- **Product:** Epson-compatible networked receipt printers
- **CVE:** CVE-2026-23767
- Unauthenticated attackers can send crafted network packets to inject arbitrary ESC/POS print commands over the network.
- Metasploit module (`admin/printer/escpos_tcp_command_injector`) added to Metasploit Framework 03/27.
- Primarily affects retail/point-of-sale/logistics environments with networked printers.
- **Sources:** Rapid7 Metasploit Wrap-Up 03/27

### 15. HackerOne Employee Data Breach After Navia HR System Hack
**Threat Score: 6/10**
- HackerOne disclosed that employee personal data was exposed following a hack of Navia, a third-party benefits/HR platform used by HackerOne.
- No indication that vulnerability or program data was exposed; limited to employee HR records.
- Raises concerns about supply chain attacks targeting HR/benefits providers to get researcher/employee data.
- **Sources:** BleepingComputer

### 16. Infinite Campus Warns of Breach After ShinyHunters Claims Data Theft
**Threat Score: 6/10**
- Infinite Campus (student information system used by K-12 schools across the US) warned of a data breach after ShinyHunters claimed to have stolen student/staff data.
- ShinyHunters is responsible for prior high-profile breaches (Ticketmaster, Santander, etc.).
- Potentially millions of student records at risk.
- **Sources:** BleepingComputer

### 17. Bearlyfy — Pro-Ukraine Ransomware Group Targeting Russian Companies
**Threat Score: 6/10**
- A new pro-Ukraine hacking group calling itself "Bearlyfy" has emerged, deploying custom ransomware against Russian companies.
- Uses custom-built ransomware tooling, not a known RaaS platform.
- Targets appear to be Russian industrial and financial sector companies.
- Geopolitical escalation: cyber conflict is intensifying on both sides.
- **Sources:** The Record (03/26)

### 18. CVE-2026-31381, CVE-2026-31382 — Gainsight Assist Information Disclosure + XSS (Fixed)
**Threat Score: 5/10**
- **Product:** Gainsight Assist (customer success platform browser extension/SaaS)
- CVE-2026-31381: Information disclosure vulnerability
- CVE-2026-31382: Cross-site scripting (XSS)
- Both are fixed. Gainsight is widely used in enterprise customer success/CRM workflows.
- **Sources:** Rapid7 Blog

### 19. Port of Vigo (Spain) Disrupted by Ransomware Attack
**Threat Score: 6/10**
- A ransomware attack disrupted operations at the Port of Vigo, Spain — one of Europe's largest fishing and cargo ports.
- Operational disruption confirmed; no group has publicly claimed responsibility.
- Follows trend of critical maritime infrastructure being targeted (Port of Seattle, previously).
- **Sources:** The Record (03/25)

### 20. RedLine Malware Developer Extradited to United States (Faces 30 Years)
**Threat Score: 5/10**
- An alleged developer of RedLine malware (one of the most prolific credential stealers) has been extradited to the United States, facing up to 30 years in prison.
- RedLine is a stealer-as-a-service platform that has compromised tens of millions of credentials.
- Significant law enforcement win; may disrupt ongoing RedLine operations.
- **Sources:** The Record, Jonathan Greig (03/26)

### 21. LeakBase Cybercrime Forum Admin Arrested in Russia
**Threat Score: 5/10**
- Russian authorities arrested the alleged administrator of LeakBase, a dark web forum specializing in credential data, weeks after a global law enforcement crackdown on the platform.
- Rare instance of Russian law enforcement action against domestic cybercrime infrastructure.
- **Sources:** The Record, Daryna Antoniuk (03/26)

---

## 📋 NOTED (Lower Priority / Context)

- **DarkSword iOS (unconfirmed):** Referenced in SANS ISC Stormcast 03/27 as Apple iOS zero-click involving Secure Enclave theft; BleepingComputer forum discussion suggests silent patch in iOS 18.4.1. Insufficient article confirmation for scoring — monitor closely.
- **Synacktiv cross-domain/cross-forest RBCD research** (03/23): Detailed exploration of cross-domain RBCD attacks in Active Directory — valuable offensive security research.
- **CVE-2026-30303, CVE-2026-30304** (AI code tools prompt injection → RCE, CVSS 9.6/9.8): Spotted on OpenCVE; insufficient corroboration from primary sources this cycle — flagged for next cycle verification.
- **Coruna iOS Exploit Kit details:** Insufficient technical detail confirmed; tracking alongside DarkSword.
- **Rapid7 2026 Global Threat Landscape Report:** Released this cycle; full read scheduled for next cycle.

---

## 🔄 ONGOING WATCH ITEMS
- TeamPCP campaign: expanding package list, Vect RaaS affiliate mobilization, AstraZeneca breach confirmation
- F5 BIG-IP CVE-2025-53521: Federal patch deadline March 30
- n8n CVE-2026-21858: Monitor for exploitation in the wild
- DarkSword/Coruna iOS: Watch for Apple advisory or CISA disclosure
- Handala retaliation cycle: Group is in escalatory mode after domain seizures and $10M bounty

---

*Cycle: Night | Generated: 2026-03-28T00:07:00Z*
*Dedup: 8 items skipped (already reported in prior 24h cycles)*
