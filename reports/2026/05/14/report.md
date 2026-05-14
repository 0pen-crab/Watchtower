# Watchtower Night Report — 2026-05-14
**Cycle:** Night | **Generated:** 2026-05-14 00:30 UTC
**Sources checked:** 19/30 | **CISA KEV total:** unchanged (gateway 403) | **New KEV additions:** none surfaced via mirrors today

---

## 🔴 CRITICAL

### Quest KACE SMA CVE-2025-32975 — Authentication Bypass (CVSS 10.0) Actively Exploited Via MSP To Pivot Into 60+ Downstream Organizations (10-Month Unpatched Window)
**Product:** Quest KACE Systems Management Appliance (K1000) | **CVE:** CVE-2025-32975 | **Status:** Active Exploitation

Quest KACE SMA's SSO handler accepts attacker-supplied user identity without credential verification, letting a network-reachable attacker impersonate any user — including administrators — on the on-premises endpoint-management appliance that pushes software, patches, and remote commands to every managed endpoint. Quest shipped the patch in May 2025 (10 months before this disclosure), but Hunt.io discovered an unauthenticated, internet-exposed attacker staging server holding 308 MB of intrusion materials and a 512 MB victim database; the operators had used the bug to compromise HIQ, a Boston-area managed-service provider, and then pivoted into 60+ downstream HIQ-managed organizations spanning law enforcement, government, healthcare, education, and private-sector. Hunt.io's scanning shows 12,000+ K1000 appliances still internet-facing with pre-patch version banners.

**Timeline:** Patch released 2026-05-2025 → Hunt.io detects active exploitation cluster → public disclosure 2026-05-13 (securityaffairs / Hunt.io blog).

**Why it matters:** KACE compromises are EDR-equivalent — once the appliance is owned, the attacker can push any binary to every managed endpoint in the customer fleet. The MSP→customer chain here is the same playbook Kaseya/ConnectWise/SimpleHelp/ScreenConnect have been weaponised through over the past four years; the KACE installed base in mid-market US enterprise (especially state/local government, healthcare, education) means a single MSP compromise yields multi-tenant access. The fact that 12k+ instances remain unpatched ten months after vendor disclosure is a defensive-priority signal in its own right.

**Discovered by:** Hunt.io threat intelligence (intrusion-set discovery from exposed staging server). Vendor advisory dates to May 2025.

**Mitigation:**
- Patch KACE SMA / K1000 to the May 2025 fix release immediately — no exceptions.
- Inventory all KACE appliances; remove any internet-exposed K1000 from public access and place behind VPN+MFA.
- For MSPs and orgs consuming MSP-managed KACE: assume compromise on the appliance if it was internet-facing and pre-patch at any point since May 2025; hunt for SSO impersonation events, anomalous admin actions, and unexpected agent push jobs.
- Rotate all credentials accessible to the KACE service account, including LDAP/AD binds.
- Block SSO endpoints from the public internet via WAF/firewall ACL as a temporary compensating control.

**Sources:** [SecurityAffairs — Quest KACE SMA flaw CVE-2025-32975](https://securityaffairs.com/192067/security/quest-kace-sma-flaw-cve-2025-32975-when-one-unpatched-tool-opens-the-door-to-60-organizations.html)

---

## 🟠 HIGH

### OPNsense Core CVE-2026-44193 — XMLRPC `restore_config_section` Unauthenticated RCE On Widely-Deployed Open-Source Firewall (CVSS 9.1)
**Product:** OPNsense (open-source firewall platform, FreeBSD-based) | **CVE:** CVE-2026-44193 | **CVSS:** 9.1 | **First reported:** 2026-05-13

The OPNsense XMLRPC endpoint `opnsense.restore_config_section` fails to sanitize user-supplied input, allowing an unauthenticated remote attacker reaching the management plane to inject arbitrary configuration that executes as the privileged firewall daemon — yielding RCE on the firewall itself. Patched in OPNsense 26.1.7. No public exploitation reported yet; expect the same disclosure→ransomware tempo seen with cPanel CVE-2026-41940 (5-day window) and PAN-OS CVE-2026-0300 (Volt-Typhoon-class actors landed within days).

**Mitigation:**
- Upgrade to OPNsense 26.1.7 immediately.
- Restrict the OPNsense web UI / API to management VLAN only; never expose port 443 management to the public internet (this is a long-standing OPNsense best practice that many smaller orgs ignore).
- Audit web-server access logs for unauthenticated `xmlrpc.php` POSTs and inspect for `restore_config_section` calls.
- Inventory any pfSense forks running parallel XMLRPC handlers — the same code-path may exist.

**Sources:** [OpenCVE — CVE-2026-44193](https://app.opencve.io/cve/CVE-2026-44193) | [dbugs.ptsecurity.com](https://dbugs.ptsecurity.com)

---

### Microsoft May 2026 Patch Tuesday — MDASH Agentic AI System Disclosed As Source Of 16 Critical-Class Bugs, Including CVE-2026-33824 IKEv2 Pre-Auth RCE (CVSS 9.8) On Windows IPSec Stack — Update On 2026-05-13 Coverage
**Product:** Windows (ikeext.dll IKEv2 implementation, TCP/IP IPSec, Outlook, Office) | **CVE:** CVE-2026-33824, CVE-2026-33827, CVE-2026-40361 (plus prior 17-CVE batch covered 2026-05-13) | **CVSS:** 9.8 (CVE-2026-33824)

Two material disclosures landed 2026-05-13 on top of yesterday's Patch Tuesday entry. (1) Microsoft published the architecture of MDASH ("multi-model agentic scanning harness"), an internal AI vulnerability-discovery system that orchestrates 100+ specialized agents across frontier and distilled models with separate "auditor" and "debater" stages — and credited it with finding 16 of the May Patch Tuesday CVEs in the Windows networking/authentication stack. (2) The MDASH-disclosed list includes **CVE-2026-33824, a CVSS 9.8 pre-authentication double-free RCE in ikeext.dll** reachable via crafted IKE version 2 packets — a direct hit on the Windows IPSec stack which is internet-facing on any Windows Server, Windows VPN endpoint, or RRAS deployment with IKEv2 enabled. CVE-2026-33827 is a TCP/IP IPSec race condition (CVSS 8.1). SecurityWeek separately characterised CVE-2026-40361 in Outlook as "BadWinmail-class" zero-click — BleepingComputer's coverage contradicts the zero-click framing, so treat with caution pending Microsoft's own writeup.

**Why this is a material update vs. yesterday's entry:** Yesterday's report enumerated the Patch Tuesday CVE list from BleepingComputer; that list did **not** include CVE-2026-33824 or CVE-2026-33827. These two bugs are the most defensively-urgent of the May batch and need to be on the patching priority list before generic-OS rollout. The MDASH narrative joins OpenAI Daybreak (covered 2026-05-09) and Google Project Glasswing as the third frontier-lab AI vuln-finder pipeline disclosed in 60 days; the durable industry implication is that **automated agentic vuln-discovery is now standard at every major Windows / Linux / browser vendor** — defensively, expect Patch Tuesday batch sizes to grow 30-50% for the rest of 2026, and assume any internet-facing surface has at least one undisclosed bug in the AI-discovery pipeline at any given time.

**Mitigation:**
- Push CVE-2026-33824 (IKEv2 ikeext.dll) and CVE-2026-33827 (TCP/IP IPSec) to the front of the patching queue for any Windows host that handles IKE/IPSec inbound (VPN endpoints, RRAS, Windows Server with site-to-site IPSec, Azure Files SMB-over-QUIC chains).
- For Windows Server hosts that do not need IKEv2: temporarily disable the IKE and AuthIP IPsec Keying Modules service (`stop-service IKEEXT`) as a compensating control until patched.
- Audit any internet-facing Windows VPN concentrators — perimeter-class pre-auth RCE on Windows-side IKE is the same threat-class as PAN-OS CVE-2026-0300 / Ivanti CVE-2026-6973.
- Use yesterday's Patch Tuesday entry for the full 17-CVE batch coverage; this update augments rather than replaces it.

**Sources:** [TheHackerNews — Microsoft's MDASH AI System Finds 16 Windows Flaws](https://thehackernews.com/2026/05/microsofts-mdash-ai-system-finds-16.html) | [TheHackerNews — Microsoft Patches 138 Vulnerabilities](https://thehackernews.com/2026/05/microsoft-patches-138-vulnerabilities.html) | [HelpNetSecurity — MDASH agentic AI security system](https://www.helpnetsecurity.com/2026/05/13/microsoft-mdash-agentic-ai-security-system/) | [SecurityWeek — Microsoft Patches Critical Zero-Click Outlook Vulnerability](https://www.securityweek.com/microsoft-patches-critical-zero-click-outlook-vulnerability-threatening-enterprises/)

---

### F5 NGINX Open Source CVE-2026-42945 — ngx_http_rewrite_module Vulnerability (CVSS 8.1)
**Product:** F5 NGINX Open Source (and NGINX Plus, by inheritance pending vendor confirmation) | **CVE:** CVE-2026-42945 | **CVSS:** 8.1 | **First reported:** 2026-05-13

A vulnerability in NGINX's `ngx_http_rewrite_module` was disclosed via the oss-security mailing list on 2026-05-13 (Mark Cox / F5 advisory chain). Technical details are limited in the initial post; CVSS 8.1 score on a core HTTP module reachable on any NGINX deployment that uses `rewrite` / `if` / `return` directives (effectively all production NGINX) makes this defensively important even before the full exploit primitive is published. NGINX is the most-deployed reverse proxy and web server in the world — the blast radius on this class of bug is comparable to the 2026-05-05 Apache HTTP Server 9-CVE batch (which included a HTTP/2 double-free RCE-class issue) covered in this digest.

**Mitigation:**
- Track F5 vendor advisory page for the patched NGINX Open Source release that includes the fix; deploy as soon as available.
- For NGINX Plus subscribers: F5 typically ships the parallel fix within 48 hours of OSS disclosure — coordinate with TAM if not.
- In the interim, audit `nginx.conf` for unusual `rewrite` chains; reduce attack surface by removing unnecessary rewrite rules and complex `if` blocks where possible.
- Patch coordination with the broader NGINX-derivative ecosystem (OpenResty, Tengine, Angie, Kong, NGINX Ingress Controller) since they share the upstream rewrite-module code.

**Sources:** [openwall oss-security 2026/05/13 — CVE-2026-42945](https://www.openwall.com/lists/oss-security/2026/05/13) | [dbugs.ptsecurity.com](https://dbugs.ptsecurity.com)

---

### FamousSparrow (UAT-9244) Targets Azerbaijani Energy Firm Via ProxyNotShell Microsoft Exchange Chain — Three Intrusion Waves Across 60+ Days Despite Vendor Remediation Attempts
**Product:** Microsoft Exchange Server (on-premises, ProxyNotShell chain) | **CVE:** ProxyNotShell chain (CVE-2022-41040 / CVE-2022-41082 historical baseline) | **CVSS:** Historical | **First reported:** 2026-05-13

Bitdefender published an attribution and TTP report on a multi-wave intrusion campaign run by FamousSparrow (also tracked as UAT-9244, with tactical overlap to Earth Estries and Salt Typhoon) against an Azerbaijani energy company between late December 2025 and late February 2026. The actor exploited a ProxyNotShell Exchange chain to gain initial access, deployed Deed RAT (Snappybee) on 2025-12-25, then returned across two further waves (TernDoor in late January, Deed RAT again in late February) using the same Exchange entry point despite the company's remediation attempts in between. The pattern: actors will re-exploit the same access path until **the original vulnerability is patched, the compromised credentials are rotated, and the attacker's lateral persistence is fully evicted** — partial remediation invites repeat compromise.

This is the second China-aligned ProxyNotShell-chain campaign disclosed in 12 days after SHADOW-EARTH-053 (Trend Micro, 2026-05-02) running React2Shell + IIS + Exchange against Pakistan/Thailand/Malaysia/India/Myanmar/Sri Lanka/Taiwan/Poland. The implication: unpatched on-prem Exchange is **the** PRC-aligned 2026-Q2 initial-access vector, not a tail-end issue.

**Mitigation:**
- If running on-prem Exchange: confirm the May 2026 cumulative + all 2022/2023/2024/2025 security updates are installed end-to-end; the ProxyNotShell chain itself is 2022 but the post-exploit chains assume mature OWA / EWS surface that has been hardened across multiple patch cycles.
- Migrate to Exchange Online or hybrid where feasible; this is the second AOL-era-protocol legacy-server compromise in two weeks.
- Hunt for Deed RAT (Snappybee) and TernDoor IOCs from the Bitdefender writeup; correlate with any OWA process-tree anomalies (`w3wp.exe` spawning `powershell.exe` / `cmd.exe`).
- If a prior Exchange compromise was remediated only by patching: assume the access path remains warm; rotate all service-account credentials, OAuth tokens, and any cached Kerberos golden-ticket material.

**Sources:** [TheHackerNews — Azerbaijani Energy Firm Hit by Repeated Microsoft Exchange Exploitation](https://thehackernews.com/2026/05/azerbaijani-energy-firm-hit-by-repeated.html)

---

### GemStuffer — 150+ Malicious RubyGems Used As Data-Exfil Channel For Scraped UK Local Government Portal Data
**Product:** RubyGems ecosystem (distinct campaign from the 2026-05-12 RubyGems mass-upload + sign-up suspension) | **CVE:** N/A (no software vulnerability — abuse-of-feature) | **First reported:** 2026-05-13

Socket researchers identified a campaign dubbed GemStuffer that uses RubyGems as a **data-exfiltration channel** rather than a malware-delivery channel: scripts fetch pages from UK local-government democratic-services portals (council meeting agendas, member rosters, ward profiles, FOI request logs), package the responses into valid `.gem` archives, and publish those gems back to RubyGems via newly-created publisher accounts. 150+ such gems were observed. The defensive interpretation is novel — the attacker isn't compromising RubyGems users; they are using the public, free, anonymous gem-publishing service as a free CDN / data-store for staged-out scraping. This is the same pattern as DNS-tunneling exfiltration but at the package-registry layer, and it sets a precedent that other public package registries (npm, PyPI, NuGet, Hugging Face, Maven Central) will need to defend against.

The campaign is distinct from yesterday's "RubyGems mass malicious upload — sign-ups suspended" entry: yesterday's was bulk-uploaded malicious-payload gems; GemStuffer is benign-looking gems used as exfil packaging.

**Mitigation:**
- For UK local government / public-sector orgs: monitor egress to `rubygems.org` from any non-Ruby-development network segment; legitimate gem traffic is well-correlated with developer workstations and CI infrastructure, not with web-scraper IP space.
- For RubyGems maintainers: precedent for needing content-classification on gem uploads (not just malware detection) — text-content gems with no Ruby code should be flagged.
- This pattern will repeat on npm / PyPI / Hugging Face Datasets — track and propose policy.

**Sources:** [Socket — GemStuffer Campaign Abuses RubyGems as Exfiltration Channel](https://socket.dev/blog/gemstuffer) | [TheHackerNews — GemStuffer Abuses 150+ RubyGems](https://thehackernews.com/2026/05/gemstuffer-abuses-150-rubygems-to.html)

---

### SPIP CVE-2026-8429 + CVE-2026-8430 — Twin Remote Code Execution Vulnerabilities In Widely-Deployed French-Origin CMS
**Product:** SPIP CMS (open-source PHP-based, French gov / education / cultural sector default CMS) | **CVE:** CVE-2026-8429, CVE-2026-8430 | **First reported:** VulnCheck 2026-05-12 (we are late by one day — see Discovery)

SPIP < 4.4.14 shipped two distinct RCE primitives. CVE-2026-8429 is RCE via "Private Space" (the authenticated editor-side interface, but the chain is reachable through low-privilege editor accounts which most SPIP sites give out liberally). CVE-2026-8430 is an RCE chain "via nginx" — the public summary indicates a misconfiguration-amplified primitive where a default nginx reverse-proxy configuration exposes a SPIP internal endpoint that should not be reachable externally. Both fixed in SPIP 4.4.14.

SPIP is in scope because of its public-sector footprint in France (`.gouv.fr` subdomains, French municipal / departmental sites, education-sector deployments) — the same scope-class as Drupal in US federal civilian / Joomla in Italian government.

**Discovery:** Late by one day vs. VulnCheck. SPIP advisories don't surface on our top-tier feeds (BleepingComputer / THN / SecurityWeek) and we only caught this via VulnCheck on the 2026-05-13 sweep. Pattern to set: add SPIP security tracker (`https://contrib.spip.net/Securite`) as a watched feed if SPIP volume continues.

**Mitigation:**
- Upgrade SPIP to 4.4.14 immediately.
- Audit nginx reverse-proxy configs in front of SPIP for any direct-pass-through to internal SPIP paths (`/ecrire/`, internal API endpoints).
- Restrict editor-role account provisioning until upgraded; rotate editor credentials post-upgrade.

**Sources:** [VulnCheck — SPIP 4.4.14 advisories](https://www.vulncheck.com/advisories)

---

### Langflow CVE-2026-3345 — Path Traversal Via File Upload API (High) On Widely-Used Open-Source AI Workflow Builder
**Product:** Langflow (open-source visual workflow builder for LangChain-based AI apps) | **CVE:** CVE-2026-3345 | **CVSS:** High (≥7) | **First reported:** VulnCheck 2026-05-12

Langflow < 1.9.0 contains a path-traversal vulnerability in its file-upload API allowing an attacker to write arbitrary files outside the intended upload directory. Langflow is widely deployed in self-hosted AI workflow stacks and is one of the recurring "default-no-auth" AI infrastructure platforms tracked in the MEMORY pattern library — combined with this filewrite primitive, the chain is path-traversal → arbitrary file overwrite → RCE on the Langflow host.

This is the fourth AI-infrastructure CVE in the past 30 days (after Open WebUI 4-CVE batch, FastGPT CVE-2026-42302 unauth RCE, Ollama Bleeding Llama CVE-2026-7482) — same default-no-auth + permissive code path code-quality issue.

**Mitigation:**
- Upgrade Langflow to ≥ 1.9.0 immediately.
- Audit network exposure of Langflow — never expose to public internet; gate behind VPN + SSO.
- Inventory any other "no-auth-by-default" self-hosted AI infrastructure (Open WebUI, FastGPT, Ollama, Flowise, LiteLLM) for the same posture-review.

**Sources:** [VulnCheck — Langflow CVE-2026-3345](https://www.vulncheck.com/advisories)

---

### Strapi CVE-2026-22599 — SQL Injection In Content Type Builder (Critical) On Popular Open-Source Headless CMS
**Product:** Strapi (`@strapi/content-type-builder` npm package) | **CVE:** CVE-2026-22599 | **GHSA:** GHSA-3xcq-8mjw-h6mx | **Severity:** Critical | **First reported:** 2026-05-13

Strapi's Content Type Builder allows SQL injection through a crafted request, yielding database-level read/write on the Strapi instance — direct impact on any application built on Strapi as its data layer. Strapi is one of the top-3 open-source headless CMSes in the JavaScript ecosystem and is widely used for marketing-site backends, internal admin panels, and IoT-data-collection backends.

**Mitigation:**
- Upgrade `@strapi/content-type-builder` to the fixed release per the GHSA advisory.
- Audit Strapi-managed databases for unusual query patterns or unexpected admin-table inserts.
- Restrict Content Type Builder admin UI to internal management network until upgraded.

**Sources:** [GHSA-3xcq-8mjw-h6mx](https://github.com/advisories/GHSA-3xcq-8mjw-h6mx)

---

## 🟡 MEDIUM

### Foxconn Confirms North American Factory Compromise By Nitrogen Ransomware — 8TB / 11M Files Exfil, Customer Schematics (Intel / Apple / Google / Dell / Nvidia)
**Product:** Foxconn (Hon Hai Precision Industry) North American manufacturing infrastructure | **CVE:** N/A | **Published:** 2026-05-13

Foxconn confirmed on 2026-05-13 the cyberattack that was first listed on Nitrogen ransomware group's Tor leak site on 2026-03-12. The compromise resulted in 8TB / 11M+ files exfiltrated, including confidential documents and schematics related to Intel, Apple, Google, Dell, and Nvidia. Affected factories are now resuming normal production. The two-month gap between attacker disclosure and victim confirmation is the notable pattern here — and the customer-list overlap means downstream-customer threat-intel teams should be assessing potential schematic / supply-chain-design leak impact.

**Mitigation:** For organizations with Foxconn as a manufacturing partner — request specific impact assessment from Foxconn account team; review what design IP, BOM, or production-test data was shared with Foxconn after 2025-Q4 and assume potential disclosure. Refresh any embedded secrets / signing keys included in shared firmware / hardware design files.

**Sources:** [SecurityWeek — Foxconn Confirms North American Factories Hit by Cyberattack](https://www.securityweek.com/foxconn-confirms-north-american-factories-hit-by-cyberattack/)

---

### OpenLoop Health January 2026 Data Breach Confirmed — 716,000 Patients Affected (Telehealth Infrastructure Provider)
**Product:** OpenLoop Health (telehealth infrastructure platform serving multiple consumer-facing telehealth brands) | **CVE:** N/A | **Published:** 2026-05-13

OpenLoop confirmed a January 2026 intrusion affecting 716,000 individuals. As a B2B telehealth infrastructure provider rather than a consumer-facing brand, the disclosed records likely span multiple telehealth-service partners (consumer-facing names typically released as separate downstream notifications). This continues the pattern of healthcare-adjacent SaaS infrastructure as a high-value target — same class as Change Healthcare (2024), Kaiser ad-tech (2024), Ascension (2024).

**Mitigation:** Patient identity / medical-record threat-monitoring for affected populations; healthcare orgs that consume OpenLoop infrastructure should request specific impact attestation.

**Sources:** [SecurityAffairs — OpenLoop Health confirms January 2026 Data breach](https://securityaffairs.com/192066/uncategorized/openloop-health-confirms-january-2026-data-breach-affecting-716000.html)

---

## 📋 Noted / Monitoring

**dnsmasq multi-issue advisory (VU#471747, 2026-05-11)** — CERT/CC published a multi-bug advisory covering DNS redirect, privilege escalation, and heap manipulation in dnsmasq; no CVE numbers surfaced via WebFetch yet. Track for CVE assignment + distro patch chain — dnsmasq runs on most consumer/SOHO routers and many enterprise resolvers.

**Casdoor arbitrary file write VU#937808 (2026-05-11)** — CERT/CC arbitrary-file-write advisory on Casdoor (open-source IdP/IAM platform). Track for CVE assignment + Casdoor advisory chain — small but growing self-hosted IdP footprint.

**Linux kernel "fragnesia" / copyfail 3.0 LPE (oss-security 2026-05-13)** — Local privilege escalation on Linux kernel, sequel to the CopyFail family. LPE-only and out-of-scope by default, but the CopyFail lineage previously escalated to KEV (CVE-2026-31431, 2026-05-03); track for escalation signal.

**GNU sed CVE-2026-5958 TOCTOU race (oss-security 2026-05-13)** — `sed -i --follow-symlinks` race; local-only, niche but ubiquitous binary so worth a distro-tracking note.

**Crypt::Argon2 CVE-2026-8463 heap OOB read (oss-security 2026-05-13)** — Perl Argon2 verification on empty input has a heap out-of-bounds read; affects Perl auth stacks. Low severity but auth-library category warrants visibility.

**Kata Containers CVE-2026-41326 CopyFile policy symlink bypass (oss-security 2026-05-13)** — Kata-specific isolation bypass; niche but relevant to cloud-native isolation stacks.

**Web::Passwd CVE-2026-8500 Perl RCE (oss-security 2026-05-13)** — Niche Perl module, low deployment, RCE class.

**JetBrains TeamCity CVE-2026-44413 privilege escalation + API exposure (helpnetsecurity 2026-05-12)** — Authenticated privilege escalation and API credential exposure in TeamCity self-hosted CI. Track for federal-employer / financial-vertical patching cadence; not currently exploited but TeamCity is a recurring credential-theft pivot point (2024 SolarWinds-adjacent activity).

**Wing FTP Server CVE-2026-44403 authenticated RCE via session serialization (vulncheck 2026-05-12)** — Wing FTP is widely deployed for SMB-vertical FTP/SFTP; authenticated-only requirement keeps this in noted but the session-serialization class often escalates to unauth via secondary primitives.

**Frappe / ERPNext CVE-2026-44447 SQL injection (CVSS 8.8, OpenCVE 2026-05-13)** — ERPNext is a widely-deployed open-source ERP; SQL injection on tenant data. Track for downstream Frappe / Bench deployment patches.

**siyuan Bazaar marketplace stored-XSS → Electron RCE CVE-2026-45375 + ungated config-write CVE-2026-45371 (GHSA 2026-05-13)** — Self-hosted Electron note-taking app with package marketplace; Electron RCE on user workstations. Niche but the marketplace-rendering vector mirrors the JDownloader / PyPI / RubyGems supply-chain pattern.

**langchain (npm) CVE-2026-45134 — public prompt pull deserializes untrusted manifests (GHSA 2026-05-13)** — LangChain JS deserializes prompt-hub manifests without trust-boundary warnings; matches the Apache OpenNLP model-loading + Hugging Face pickle pattern (MEMORY: model-loading code paths as attack surface).

**systeminformation (npm) CVE-2026-44724 — Linux command injection via NetworkManager profile names (GHSA 2026-05-13)** — Command injection in widely-used Node.js system-info package; attacker-controllable NetworkManager profile names yield local command execution.

**Nautobot REST API SSRF + writable internal field — CVE-2026-44797 / CVE-2026-44798 (GHSA 2026-05-13)** — Two distinct authz/SSRF issues in Nautobot (network-automation DCIM platform). Network-automation tools are credential warehouses; track.

**Grav CMS CVE-2026-44738 — Twig sandbox escape allows editor-role users to exfiltrate plugin secrets (GHSA 2026-05-13)** — Editor-role sandbox bypass; in-scope CMS class.

**uniget CLI CVE-2026-45152 — command injection in tool.Check (GHSA 2026-05-13)** — Self-hosted tool-installer command-injection; niche.

**OPNsense CVE-2026-29205 / CVE-2026-29206 (CVSS 8.6 / 8.1) — additional adminbin file-read and SQL-injection issues alongside CVE-2026-44193** — Multiple OPNsense-companion CVEs published in the same window; defenders patching OPNsense should treat 26.1.7 as the umbrella fix.

**linux-kernel NTB driver shift-out-of-bounds CVE-2026-43141 (CVSS 7.1, OpenCVE 2026-05-13)** — Kernel NTB hardware-driver bug; niche hardware path, primarily DoS-class.

**Sandyaa open-source autonomous bug hunter (helpnetsecurity 2026-05-13)** — Newly-released open-source autonomous bug-discovery tool — defensive-pattern data point in the AI-bug-finder column alongside MDASH / Daybreak / Project Glasswing. Watch for first ITW outputs.

**Arqit Symmetric Key Agreement Platform CVE-2026-33583 (CVSS 8.7, dbugs.ptsecurity 2026-05-13)** — Cryptographic key management platform; niche vendor but classification (key-management) makes any high-severity issue worth following.

**Zoom Workplace VDI Plugin CVE-2026-30905 + Zoom Rooms CVE-2026-30906 (CVSS 7.8 each, dbugs 2026-05-13)** — Local-privilege-class issues in widely-deployed conferencing endpoints; out-of-scope by severity tier rules but track for any remote-component pivot.

**Cleanuparr CVE-2026-44183 followup** — Yesterday's News item — confirmed Cleanuparr's response and proxy-aware default mitigation guidance; no patch breakthrough yet, repository now publishes a `cleanuparr-secure` deployment template.

**Hermes WebUI CVE-2026-22677 + Quark Drive CVE-2026-45229 / CVE-2026-45228 (vulncheck 2026-05-13)** — Niche self-hosted web apps; tracking only.

**Ecommerce Systempay ≤ 1.0 CVE-2020-37168 + 12 other historic 2020 CVEs (vulncheck 2026-05-13)** — Backfill of historic CVEs in old e-commerce / WordPress / Joomla / IoT-router code published this week; no defensive urgency, but the rate of n-day catalog backfills is itself a calibration data point for any defender wondering if "CVSS 9 on a 2020 router" should still warrant action.

**Chipmaker Patch Tuesday — Intel + AMD ~70 CVEs (SecurityWeek 2026-05-13)** — Two-dozen advisories covering recently-discovered chip defects; primarily microcode + driver-side. ICS Patch Tuesday (Siemens, Schneider, CISA, dozen-plus advisories) also published. Most are LPE / DoS class.

**FortiOS CVE-2025-53844 CAPWAP out-of-bounds-access (HIGH, FG-IR-26-123)** — Disclosed alongside the FortiSandbox + FortiAuthenticator critical batch covered 2026-05-13; CAPWAP is the wireless-controller-to-AP protocol so the attack surface is internal-AP-tier rather than internet-facing.

**Mythos availability note (Schneier 2026-05-13)** — UK AISI evaluated GPT-5.5 as on-par with Claude Mythos for vulnerability discovery. Tracking-only — informs the AI-bug-finder pattern.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, securityaffairs.com, helpnetsecurity.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (403, used securityaffairs + bleepingcomputer relay) |
| Vendor advisories | fortiguard.com/psirt, msrc.microsoft.com/blog | ✅ / ⚠️ (MSRC empty content) |
| Research / OSINT | schneier.com, krebsonsecurity.com (no new 5/13-5/14), rapid7.com (no new 5/13-5/14), securelist.com (no new 5/13-5/14), securitylab.github.com (no new 5/13-5/14), labs.watchtowr.com (no new 5/13-5/14), wiz.io/blog, trendmicro.com | ✅ / ⚠️ |
| Supply chain | socket.dev/blog, aikido.dev (no new 5/13-5/14), safedep.io | ✅ |
| Threat intel | github.com/0xMarcio/cve, kb.cert.org/vuls, opencve.io, dbugs.ptsecurity.com, github.com/advisories, vulncheck.com/advisories, openwall.com/lists/oss-security | ✅ |

**Errors:**
- cisa.gov / cisa.gov/known-exploited-vulnerabilities-catalog → 403 (persistent, documented in MEMORY)
- attackerkb.com → 403 (persistent, documented in MEMORY)
- seclists.org/fulldisclosure → 302 to seclists.org root (fulldisclosure feed degraded)
- packetstormsecurity.com / packetstorm.news → returns summary stats only via WebFetch, no per-item titles
- msrc.microsoft.com/blog → page header only, no body content
- hackerone.com/hacktivity → JS-only (documented)
- bugcrowd.com/disclosures → 404 (documented)
- cve.mitre.org / cve.org → JS-only (documented)
- googleprojectzero.blogspot.com → redirected to projectzero.google/ (documented)
- nvd.nist.gov → JS-only (documented)
- habr.com/ru/companies/tomhunter/articles, teletype.in/@cyberok, cert.gov.ua, avleonov.com → degraded / no recent posts

**CISA KEV:** No new additions surfaced via primary or relay sources for 2026-05-13 / 2026-05-14. The 2026-05-12 KEV addition of CVE-2026-42208 (LiteLLM) was the most recent.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-14/night | Next: 2026-05-15/night*
