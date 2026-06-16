# Watchtower Night Report — 2026-06-16
**Cycle:** Night | **Generated:** 2026-06-16 00:45 UTC (2026-06-16T00:45:00Z)
**Sources checked:** 22/30 | **CISA KEV total:** Catalog unreachable (cisa.gov 403) | **New KEV additions:** Unknown — KEV catalog endpoint returned 403; cross-referenced via THN / SecurityWeek / Rapid7

---

## 🔴 CRITICAL

### Palo Alto Networks PAN-OS GlobalProtect CVE-2026-0257 (CVSS 7.8) — Authentication Bypass Actively Exploited Since 2026-05-17, CISA KEV-Added With Federal Deadline 2026-06-01 (Already Lapsed); Palo Alto PSIRT Advisory Lands 2026-06-15
**Product:** Palo Alto Networks PAN-OS GlobalProtect portal/gateway | **CVE:** CVE-2026-0257 | **Status:** Patched + Active Exploitation + KEV

Authentication bypass affecting both the GlobalProtect portal and gateway components — an unauthenticated attacker bypasses authentication controls and initiates a VPN session against an affected PA-Series / VM-Series device. Palo Alto Networks PSIRT confirms active in-the-wild exploitation beginning 2026-05-17, with the CISA KEV catalog already adding the entry and a federal-agency remediation deadline of 2026-06-01 that is now past. PAN states only a "small portion" of probed devices successfully established VPN sessions and "no post-access behavior or lateral movement has been identified" — but the foothold is one credential-prompt away from internal network access on a perimeter VPN appliance. Palo Alto published associated IOCs (IPs, hostnames including `WINDOWS-LAPTOP-001`, `DESKTOP-GP01`, MAC addresses) on 2026-06-15. Distinct from CVE-2026-0300 (PAN-OS RCE per avleonov 2026-06-05) — different code path, different perimeter surface.

**Timeline:** Active ITW exploitation observed beginning 2026-05-17 → CISA KEV addition (date not stated by THN but federal deadline 2026-06-01) → Palo Alto PSIRT public advisory + IOC release 2026-06-15 → Watchtower 2026-06-16 (late — KEV addition occurred prior to our previous reports; defensive-coverage gap to investigate).

**Why it matters:** PAN-OS GlobalProtect is one of the highest-density public-perimeter VPN gateways in our scope (~ tens of thousands of internet-facing PAN devices visible per Shodan tracking historically). Active exploitation against the VPN gateway surface (paired with CVE-2026-50751 Check Point KEV from 06-08 and the Cisco SD-WAN cluster ongoing) makes this a "patch every VPN gateway you operate this week" situation, especially since the federal deadline has already lapsed and PAN now has IOCs published.

**Discovered by:** Palo Alto Networks PSIRT — internal detection of ITW exploitation beginning 2026-05-17.

**Mitigation:**
- Patch every PA-Series / VM-Series PAN-OS device with GlobalProtect enabled to the PSIRT-listed fixed versions immediately.
- Pull Palo Alto's published IOCs (IPs, hostnames `WINDOWS-LAPTOP-001` / `DESKTOP-GP01`, MAC addresses) into SIEM and EDR.
- Audit GlobalProtect VPN-session logs back to 2026-05-17 for any session establishment whose endpoint signature matches the listed MAC/hostname IOCs, or short-lived sessions from non-corporate IP ranges.
- Until patched, treat GlobalProtect portals as compromised — restrict source-IP allowlists, force MFA on every GlobalProtect-backed user, and consider taking gateways offline if patching is blocked.
- Pair this with the Watchtower VPN-gateway hardening checklist already triggered by Check Point CVE-2026-50751 (06-08 NEWS) — same review pass, same control set.

**Sources:** [The Hacker News 2026-06-15](https://thehackernews.com/2026/06/palo-alto-warns-of-active-exploitation.html) | [Palo Alto Networks PSIRT advisory](https://security.paloaltonetworks.com/CVE-2026-0257)

---

## 🟠 HIGH

### Cisco Catalyst SD-WAN Manager (vManage) CVE-2026-20262 — Authenticated Arbitrary-Command Execution As Root Via File-Upload Validation Gap, Actively Exploited In Zero-Day Attacks, Patched 2026-06-15
**Product:** Cisco Catalyst SD-WAN Manager (vManage) — multiple branches 20.9 / 20.12 / 20.15 / 20.18 / 26.1 | **CVE:** CVE-2026-20262 | **CVSS:** Cisco rating not yet stated, treat as High based on impact/exploit signal | **First reported:** 2026-06-15 (Cisco PSIRT advisory + BleepingComputer)

The flaw stems from insufficient validation of user-supplied input during file uploads — an authenticated remote attacker sends a crafted HTTP request to an affected API endpoint and executes arbitrary commands as root on the vManage controller. Cisco PSIRT confirms it became aware of active exploitation earlier in June 2026, ahead of the patch landing 2026-06-15. Affected: 20.9.9.1 and earlier, 20.12.7.1 and earlier, 20.15.4.4 and earlier, 20.15.5.2 and earlier, 20.18.3, and 26.1.1.1 and earlier — patches available for every affected branch. Distinct from but adjacent to CVE-2026-20245 (root-cmd-exec zero-day from 2026-06-06 NEWS, KEV-added 2026-06-09), CVE-2026-20182 (auth bypass), CVE-2026-20128/20122/20133 (info disclosure) — the SD-WAN Manager cluster is the third sustained burst of Cisco SD-WAN zero-days in 2026.

**Timeline:** Active exploitation observed by Cisco PSIRT earlier in June 2026 → Cisco PSIRT advisory + patches across all affected branches published 2026-06-15 → BleepingComputer write-up 2026-06-15 → Watchtower 2026-06-16.

**Why it matters:** vManage is the centralised orchestration plane for an enterprise SD-WAN fabric — root on vManage means control of every SD-WAN edge in the fleet. The "seventh SD-WAN zero-day of 2026" pattern (called out 2026-06-06) keeps holding; vManage is now the third Cisco SD-WAN component with confirmed ITW exploitation in 2026. The authentication requirement lowers the immediate ceiling versus the unauth CVE-2026-20245 vector, but any post-credential-spray foothold becomes fleet-root compromise.

**Mitigation:**
- Upgrade Cisco Catalyst SD-WAN Manager (vManage) to the fixed version for your branch (per Cisco PSIRT — 20.9.9.x, 20.12.7.x, 20.15.4.x / 5.x, 20.18.x, 26.1.1.x patched releases).
- Audit vManage HTTP API logs for unusual file-upload requests against API endpoints, especially over the past 30 days. Cisco has not yet published IOCs; high-volume / non-baseline file-upload activity is the signal.
- Restrict vManage management-plane reachability to an out-of-band admin network — the BOD-pattern hardening Cisco SD-WAN deployments should already be applying after the 06-06 CVE-2026-20245 NEWS.
- Rotate vManage operator credentials — exploitation requires authentication; assume any vManage admin credential exposed via leaked logs is in play.
- Inventory: pair this fix with the CVE-2026-20245 patch — same controller, different code path; you need both.

**Sources:** [BleepingComputer 2026-06-15](https://www.bleepingcomputer.com/news/security/cisco-fixes-sd-wan-vmanage-flaw-exploited-in-zero-day-attacks/) | [Cisco PSIRT advisory for CVE-2026-20262](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-mgr-cmdinj)

---

### Awesome Motive CDN Supply-Chain Compromise — OptinMonster / TrustPulse / PushEngage WordPress Plugin JS Tampered Via Stolen CDN API Key, Plants Hidden Backdoor Plugin On 1.2M+ Sites, Self-Hiding Admin Account Creation Chain
**Product:** OptinMonster (1.2M+ sites) + TrustPulse + PushEngage (Awesome Motive WordPress plugins) — JavaScript served via Awesome Motive CDN | **CVE:** None assigned (CDN-side credential theft / supply-chain JS tamper) | **CVSS:** N/A | **First reported:** 2026-06-12 (incident) / 2026-06-13 (Sansec disclosure) / 2026-06-15 (BleepingComputer + THN write-up)

Attackers exploited a known UpdraftPlus vulnerability to compromise an Awesome Motive marketing server hosting CDN API credentials, then used the stolen CDN API key to silently modify JavaScript files distributed via Awesome Motive's CDN — the JS payload activates when a WordPress administrator visits a page on a site running an affected plugin. The injected code harvests authentication tokens / nonces, creates a rogue administrator account (e.g. `developer_api1`, `dev_xxxxxx`), installs a self-hiding backdoor plugin disguised as "Content Delivery Helper" or "Database Optimizer" (Sansec: "operator rotates the disguise while keeping the logic byte-identical across renames"), exposes a PHP web shell, and beacons out to a Tidio-lookalike attacker-controlled domain. Window of malicious-script distribution: OptinMonster + TrustPulse served bad JS 2026-06-12 22:17–22:42 UTC; PushEngage continued serving malicious code until 2026-06-13 19:02 UTC. Sansec discovered the campaign over the weekend.

**Timeline:** Awesome Motive credentials lifted via UpdraftPlus vuln exploit (precise date not disclosed) → Malicious JS pushed to Awesome Motive CDN 2026-06-12 22:17 UTC → TrustPulse + OptinMonster JS cleaned 22:42 UTC, PushEngage JS continued to serve until 2026-06-13 19:02 UTC → Sansec public disclosure 2026-06-13 → BleepingComputer + THN write-up 2026-06-15 → Watchtower 2026-06-16.

**Why it matters:** OptinMonster alone is on 1.2M+ WordPress sites; the byte-identical backdoor logic across renamed plugin filenames means once installed, removal at the plugin-name layer alone fails. Continues the WordPress / supply-chain attack chain documented across our prior reports — Polyfill.io Round 2 (06-06), Mini Shai-Hulud + Miasma (Apr–Jun ongoing), Arch AUR mass-compromise (06-13) — and is the **first** confirmed CDN-API-key theft → live JS-tamper distribution of malicious code on a per-admin-visit basis to a multi-million-site footprint.

**Discovered by:** Sansec (e-commerce security firm).

**Mitigation:**
- Search every WordPress instance with OptinMonster / TrustPulse / PushEngage installed for rogue admin accounts named `developer_api1` or `dev_xxxxxx` — delete and rotate.
- Scan `wp-content/plugins/` for plugins named "Content Delivery Helper" or "Database Optimizer" (or sibling rebrands) that look auto-installed; remove and audit.
- Run a server-side malware scan against all instances. The self-hiding plugin pattern means front-end audits alone miss it.
- Rotate all WP credentials AND WordPress security salts (`wp-config.php`) on any affected instance — token-harvesting was part of the payload.
- Pull the Tidio-lookalike C2 indicator from Sansec's disclosure into outbound DNS / proxy block-lists.
- Investigate any UpdraftPlus footprint anywhere across the estate — the initial-access vector lifted Awesome Motive's CDN key; the same vuln is likely useful elsewhere.

**Sources:** [BleepingComputer 2026-06-15](https://www.bleepingcomputer.com/news/security/optinmonster-wordpress-plugin-hacked-in-cdn-supply-chain-attack/) | [The Hacker News 2026-06-15](https://thehackernews.com/2026/06/popular-wordpress-plugin-scripts.html) | [Sansec disclosure](https://sansec.io/research)

---

### BerriAI LiteLLM 3-CVE Chain CVE-2026-47101 + CVE-2026-47102 + CVE-2026-40217 (Full Chain CVSS 9.9) — Low-Privilege User Mints Allowed-Routes-Wildcard API Key → Self-Promotes To `proxy_admin` → Custom-Code-Guardrail `exec()` Sandbox Escape To RCE, Fixed In v1.83.14-stable
**Product:** BerriAI/LiteLLM (AI gateway proxy for OpenAI / Anthropic / Gemini / Bedrock / Azure) — versions prior to v1.83.14-stable | **CVE:** CVE-2026-47101 / CVE-2026-47102 / CVE-2026-40217 | **CVSS:** 9.9 (full chain, per Obsidian Security); CVE-2026-47102 alone 8.7–8.8 | **First reported:** 2026-06-15 (THN + Obsidian Security writeup of patch shipped in v1.83.14-stable on 2026-05-02)

Three architectural authorization bugs chain to full-RCE-on-the-AI-gateway from a low-privilege LiteLLM user account. Stage 1 (CVE-2026-47101): a regular user generates a virtual API key passing `allowed_routes: ["/*"]` — server accepts the wildcard without validation, granting access to admin-only endpoints. Stage 2 (CVE-2026-47102): the `/user/update` endpoint permits self-modification without field restrictions — attacker sends `user_role: "proxy_admin"` and gains full administrative access. Stage 3 (CVE-2026-40217): the Custom Code Guardrail executes Python via `exec()` without source filtering; passing a `globals` dict missing `__builtins__` causes Python to auto-inject the full builtins (`__import__`, `open`, `eval`), opening a reverse-shell-grade RCE primitive. End-to-end impact: master keys, credential decryption salts, database credentials, all upstream provider API keys (OpenAI / Anthropic / Gemini / Bedrock / Azure), and every prompt and response transiting the proxy. Distinct from CVE-2026-42271 (06-10 NEWS, stdio-MCP subprocess spawn, CVSS 8.7, KEV-added) — same product, different code paths, fixed in the same v1.83.x series.

**Timeline:** Discovered + disclosed by Obsidian Security → patches landed in LiteLLM v1.83.14-stable 2026-05-02 → public Obsidian Security write-up + THN amplification 2026-06-15 → Watchtower 2026-06-16. The fix is six weeks old at writeup time; the technical disclosure today is the action-forcing event.

**Why it matters:** LiteLLM is one of the two or three default AI-gateway proxies any team running multi-provider Claude / OpenAI / Gemini workloads is likely to be hosting. Self-hosted AI-gateway compromise = full provider-API-key theft + every prompt and response in the clear. The pattern (low-priv user → self-promote admin → guardrail sandbox escape) repeats the MEMORY 2026-05-05 finding that "self-hosted AI infrastructure default-no-auth posture is industry-wide" — Obsidian's chain shows even when auth *is* present, the per-endpoint authorization model is the soft underbelly. This is the second material LiteLLM advisory in 7 days following CVE-2026-42271 — assume any LiteLLM deployment running pre-v1.83.14 has been profiled by attackers.

**Mitigation:**
- Upgrade LiteLLM to ≥ v1.83.14-stable immediately. Don't drop the v1.83.x branch from prod over the LiteLLM-MCP changes; the fix for this chain *and* CVE-2026-42271 are both there.
- Rotate every credential the LiteLLM proxy has ever held: LiteLLM master key, every upstream provider API key (OpenAI / Anthropic / Gemini / Bedrock / Azure / other), DB password, credential-decryption salt.
- Audit virtual-key creation logs for any key whose `allowed_routes` field contains `/*` or matches admin-route patterns; revoke and investigate.
- Audit `/user/update` request logs for any payload containing `user_role` — that is the privilege-escalation signature.
- Audit Custom Code Guardrail definitions for any user-supplied Python — any pre-v1.83.14 guardrail definition is suspect, regardless of "trusted operator" framing.
- Treat AI-gateway proxies as crown-jewel infrastructure: model permissions accordingly, segment network access, monitor outbound from the proxy host for anomalous destinations.

**Sources:** [The Hacker News 2026-06-15](https://thehackernews.com/2026/06/litellm-vulnerability-chain-lets-low.html) | [Obsidian Security technical writeup](https://www.obsidiansecurity.com/blog/litellm-chain) | [LiteLLM v1.83.14-stable release](https://github.com/BerriAI/litellm/releases)

---

## 🟡 MEDIUM

### SimpleHelp CVE-2026-48558 — Unauthenticated Rogue-Technician Account Creation Via OIDC Identity Assertion Validation Gap, Bypasses MFA; Patched In 5.5.16 / 6.0RC2; ~14k Shodan-Exposed Servers
**Product:** SimpleHelp remote-management server ≤ 5.5.15 and 6.0 pre-release | **CVE:** CVE-2026-48558 | **Published:** 2026-06-09 (patches) / 2026-06-15 (BleepingComputer writeup)

The vulnerability sits in improper validation of identity assertions returned from OpenID Connect (OIDC) identity providers. When OIDC authentication is enabled, an unauthenticated attacker can create and log in as a new Technician user **without** going through MFA — the rogue technician account gains the default privileges of remoting into managed endpoints, executing scripts, and the standard MSP-tooling action set. Exploitation requires three conditions in combination: OIDC authentication enabled, at least one Technician Group associated with the OIDC provider, and "Allow group authenticated logins" enabled. Shodan tracks ~14k publicly exposed SimpleHelp servers, of which about 7.2% (~1k) use OIDC authentication and are likely candidates for exploitation against the affected configurations. SimpleHelp says no ITW exploitation confirmed at disclosure; patched 2026-06-09 in 5.5.16 and 6.0RC2. SimpleHelp is the RMM tool historically linked to the 2025 Akira ransomware affiliate cluster — RMM-tool footholds compound rapidly.

**Mitigation:**
- Upgrade SimpleHelp to 5.5.16 or 6.0RC2 (or later) on every server in the fleet — internal and public.
- Audit Technician account creation logs since 2026-05-15 (≥ 30 days back, covering pre-patch attacker recon) for any account created without an MFA challenge — that is the exploitation signature.
- If OIDC is enabled and "Allow group authenticated logins" is set, treat the configuration as compromised pending audit: every Technician account list should be reconciled against your IdP's actual user roster.
- Disable OIDC for now if patching is blocked — this is the only positive control until upgrade.
- Pull Technician-session remoting logs over the past 30 days for any session whose target endpoint is unusual for that technician.

**Sources:** [BleepingComputer 2026-06-15](https://www.bleepingcomputer.com/news/security/simplehelp-bug-lets-hackers-create-rogue-remote-support-accounts/) | [SimpleHelp security advisory](https://simple-help.com/blog/security)

---

### UNC6508 (China-Nexus Espionage) "InfiniteRed" — REDCap Medical-Research Server Compromise With Custom Persistence + Credential Harvester + Backdoor And Google Workspace Auto-Forwarding "Patroit" Rule, 2-Year Undetected Dwell, North American Research Institution Target
**Product:** REDCap-class medical research database platforms + downstream Google Workspace mailboxes | **CVE:** None assigned (incident) | **Published:** 2026-06-15 (BleepingComputer + THN, Google + Mandiant disclosure)

China-linked espionage group UNC6508 compromised a North American medical research institution in September 2023, deployed a custom three-component malware suite "InfiniteRed" (persistence/update module + credential harvester + backdoor for command execution, file transfer, and ad-hoc SQL queries against the REDCap database) by December 2023, and ran activity through November 2025 — over two years undetected. The initial-access vector targeted older vulnerable REDCap installations; researchers observed probing of those versions but could not confirm the exact initial-access CVE. The novel post-compromise tradecraft is Google Workspace abuse: attackers created a content-compliance rule named "Patroit" that auto-forwards mail matching specific keywords (medical research, advanced technology, military, geo-strategic policy) to an external exfil mailbox — a workflow-level persistence that survives endpoint clean-up. Google + Mandiant disclosed 2026-06-15 with YARA rules + IOCs in the underlying report. Continues the Chinese-APT-on-research-orgs cluster (Velvet Ant "Operation Highland" PAM/OpenSSH backdoor from 2026-06-13 NEWS, UAT-8302 from 2026-05-07 NOTED).

**Mitigation:**
- Inventory every REDCap server in the estate — patch to latest, restrict internet exposure where possible.
- In Google Workspace: audit every Content Compliance / Routing / Forwarding rule across all OUs and domains for any rule whose action is "forward to external address." This is the IoC class.
- Hunt for the specific rule name "Patroit" across the Workspace tenant, and for any rule referencing keyword lists matching the named topics (medical research / advanced technology / military / geo-strategic policy).
- Pull Mandiant + Google's YARA rules + IOCs from the underlying report and run them across host telemetry + log retention.
- Treat any research mailbox with an external-forwarding compliance rule as compromised until proven otherwise.
- For research-org defenders: pair this hunt with the Velvet Ant PAM-backdoor IOC sweep from 2026-06-13 — same threat-actor pattern, different surfaces.

**Sources:** [BleepingComputer 2026-06-15](https://www.bleepingcomputer.com/news/security/chinese-hackers-breach-redcap-servers-steal-medical-research/) | [The Hacker News 2026-06-15](https://thehackernews.com/2026/06/chinese-hackers-abused-google-workspace.html) | [Google + Mandiant Threat Intelligence report](https://cloud.google.com/blog/topics/threat-intelligence)

---

### Microsoft 365 Copilot Enterprise CVE-2026-42824 "SearchLeak" — 3-Stage Chain (Parameter Prompt-Injection + Render-Race Sanitization Gap + Bing-SSRF CSP Bypass) Yields One-Click Data Theft Of Email + MFA Codes + Files Via Microsoft.com-Domain Link; Mitigated Server-Side
**Product:** Microsoft 365 Copilot Enterprise Search | **CVE:** CVE-2026-42824 | **Published:** 2026-06-15 (Varonis Threat Labs + THN + BleepingComputer)

Varonis Threat Labs chained three vulnerabilities in M365 Copilot Enterprise Search into a one-click exfiltration primitive: (1) the `q` URL parameter accepts natural-language queries that Copilot processes as instructions (parameter-to-prompt injection); (2) Copilot's safety guardrail wraps response output in `<code>` blocks, but there's a sanitization race — the browser renders the response stream before sanitization completes, allowing injected `<img>` tags to fire; (3) the page's CSP allowlists `*.bing.com`, and Bing's "Search by Image" feature makes server-side requests on behalf of Bing — attackers smuggle exfiltration through Bing-as-SSRF-proxy, completely outside the CSP envelope ("a classic SSRF hiding in plain sight behind a CSP allowlist"). Victim clicks a `microsoft.com`-domain link → Copilot is instructed to extract email/calendar/SharePoint/OneDrive content → response embeds attacker-controlled `<img>` → browser sends request through Bing → attacker reads logs. Exfiltrated data classes: email content + subjects, MFA + one-time codes, password-reset links, calendar invites + meeting notes, SharePoint + OneDrive files. Microsoft (CVSS 6.5) and NVD (CVSS 7.5) disagree on severity. Microsoft mitigated server-side; **no customer patch required** because Copilot Enterprise is a managed service. **No ITW exploitation observed; PoC-only at disclosure.** Distinct from CVE-2026-45497 (06-08 NEWS, Copilot RCE via command-injection + service-container scope change).

**Mitigation:**
- No customer patch action required — Microsoft mitigated on the backend.
- Audit Microsoft 365 Copilot Enterprise activity logs over the past ~30 days for any session whose source URL contained a non-trivial `q=` parameter — that is the exploitation channel. Microsoft's mitigation closes the chain, but pre-mitigation telemetry is the only way to confirm no successful exploitation occurred.
- Block outbound requests to `bing.com/images/search` from corporate-managed browsers if your data-loss-prevention posture supports it — this is the actual exfiltration channel.
- Internal threat-modelling pass: treat any Microsoft-domain link in inbound email as the prompt-injection delivery vector for Copilot-class tooling. Repeat for Google's Gemini equivalents.
- Update your AI assistant security catalogue: this is the second major M365 Copilot CVE in 8 days (paired with CVE-2026-45497 from 06-08) — assume more chains exist in the same envelope.

**Sources:** [The Hacker News 2026-06-15](https://thehackernews.com/2026/06/one-click-microsoft-365-copilot-flaw.html) | [BleepingComputer 2026-06-15](https://www.bleepingcomputer.com/news/security/new-attack-turned-microsoft-365-copilot-into-1-click-data-theft-tool/) | [Varonis Threat Labs writeup](https://www.varonis.com/blog/searchleak)

---

## 📋 Noted / Monitoring

**CVE-2026-11645 (Google Chrome V8 zero-day, CVSS 8.8)** — Out-of-bounds memory access in V8 JS/Wasm engine, in-wild exploitation confirmed by Google, patched in Chrome 149.0.7827.102/.103 (Win/Mac/Linux). Fifth Chrome zero-day in 2026 (after CVE-2026-2441 / 3909 / 3910 / 5281). Client-only browser scope — out of Watchtower core, but tracked for AI-coding-assistant / Electron-app dependency chains. Reported by `303f06e3` for $55k bounty.

**CVE-2026-12205 (Perl Crypt::DSA < 1.21)** — Nonce reused across signatures → private-key recovery primitive. oss-security 2026-06-15 disclosure by Timothy Legge. Niche Perl-stack scope but cryptographic-failure-class — worth tagging for any legacy Perl signing infrastructure.

**CVE-2026-46447 (OpenStack Ironic < 35.0.2, OSSA-2026-017)** — Script injection during node boot via Linux command-line override (iPXE script). oss-security 2026-06-15 by Jay Faulkner. Bare-metal-provisioning operators only; companion to CVE-2026-54421 from 2026-06-15 NOTED.

**CVE-2026-52806 (Gogs authenticated argument-injection RCE — UNFIXED)** — Rapid7 disclosure 2026-06-13/15, no vendor patch. Authentication required, but self-hosted Git server compromise = source-code repo compromise. Track for patch availability; in the interim, ensure Gogs is not internet-exposed to untrusted users.

**CVE-2026-11623 (tmux < 3.6b)** — Security fix shipped in tmux 3.6b 2026-06-15. Widely deployed terminal multiplexer; technical detail not yet public — track upstream advisory.

**Microsoft Defender "RoguePlanet" zero-day (no CVE assigned)** — Fourth Defender zero-day disclosed by researcher "Chaotic Eclipse" (after BlueHammer / UnDefend / RedSun); race-condition LPE to SYSTEM, confirmed ITW exploitation per THN 2026-06-15. Local privilege elevation without remote component = out of Watchtower core scope, but the pattern of repeat-publish-after-MS-coordination-breakdown is worth tracking for Microsoft-PSIRT posture analysis.

**VU#862559 (crypton-x509-validation Haskell libraries do not enforce X.509 NameConstraints)** — CERT/CC 2026-06-11; no CVE assigned. Niche Haskell-stack scope but X.509 NameConstraint enforcement bypass is a classic certificate-chain failure pattern.

**CVE-2026-49776 (GPTranslate WordPress plugin)** — Unauthenticated SQL injection now confirmed via GitHub Security Advisory 2026-06-15. Promotes earlier placeholder CVE-2026-9109 from 2026-06-15 NOTED (where technical detail was pending) — technical detail now public. WordPress AI-translation plugin cluster (the "AI-WP-plugin" attack surface).

**CVE-2026-39502 (Form Maker by 10Web ≤ 1.15.38, CVSS 9.3)** — Unauthenticated SQL injection in widely-deployed WordPress form plugin. opencve.io 2026-06-15.

**WP plugin "PHP Object Injection" cluster 2026-06-15 (GitHub Advisory Database)** — Happyforms (CVE-2026-49768) + WP Travel Engine (CVE-2026-49770) + Integration for Mailchimp (CVE-2026-49765) + wpForo Forum (CVE-2026-49769) — all unauthenticated PHP Object Injection in the same advisory batch. Same root-cause class pattern indicates a common library or boilerplate dependency.

**Council of Europe ShinyHunters extortion (SecurityWeek + BleepingComputer 2026-06-15)** — ShinyHunters claims 297 GB of stolen data including employee PII. Continues the ShinyHunters 2026 campaign cluster (Oracle PeopleSoft 06-11/06-12, Salesforce/Infinite Campus 06-15) — no specific CVE for this incident yet.

**NPM 12 script-execution change (SecurityWeek 2026-06-15)** — `npm install` will no longer execute scripts from dependencies unless explicitly allowed. Major supply-chain defence milestone — relevant for the Miasma / Mini Shai-Hulud / IronWorm worm class.

**152 Chrome wallpaper extensions, 105k installs linked to adware + fake-traffic networks (THN 2026-06-15)** — 38 publisher accounts in the Chrome Web Store distributing PUPs across 152 extensions. Browser-extension PUP scope, but worth tracking for endpoint-allowlist policies.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com (root only — /category/vulnerabilities 403), krebsonsecurity.com, schneier.com | ✅ |
| CISA / US Gov | cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403) | ❌ |
| Vendor advisories | fortinet.com/blog/threat-research, blog.cloudflare.com/tag/security, msrc.microsoft.com/blog (redirect → microsoft.com/en-us/msrc/blog, content unavailable), litespeedtech.com (advisory page reached directly via THN/BC) | ⚠️ |
| Research / OSINT | securitylab.github.com (May entries only, no fresh June), googleprojectzero.blogspot.com (redirect → projectzero.google), avleonov.com, schneier.com, kb.cert.org/vuls | ✅ / ⚠️ |
| CVE databases | nvd.nist.gov (search broken), opencve.io / app.opencve.io, dbugs.ptsecurity.com, cve.org (limited), cve.mitre.org (not tested — historically broken), github.com/advisories (bonus), openwall.com/lists/oss-security (bonus) | ⚠️ |
| Exploit / PoC | github.com/search?q=CVE, github.com/0xMarcio/cve, packetstormsecurity.com (redirect → packetstorm.news, limited), seclists.org/fulldisclosure (degraded — only first half of June archive populated), attackerkb.com (403) | ⚠️ |
| Bug bounty | hackerone.com/hacktivity (sparse / JS-rendered), bugcrowd.com/disclosures (404) | ❌ |
| Vendor PSIRT | rapid7.com (Metasploit wrap-up + ETR) | ✅ |
| Russia / CIS | habr.com/ru/companies/tomhunter/articles (no June 2026 content), teletype.in/@cyberok (no June 2026 content), cert.gov.ua (content unavailable) | ⚠️ |

**Errors:** cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403), attackerkb.com (403), bugcrowd.com/disclosures (404), hackerone.com/hacktivity (no data), msrc.microsoft.com/blog (redirect — content unavailable), cert.gov.ua (content unavailable), cve.mitre.org (not tested — historical degraded).
**Degraded:** rapid7.com (no date metadata on blog index), seclists.org/fulldisclosure (no messages 2026-06-10 onward), googleprojectzero.blogspot.com (sparse), nvd.nist.gov (search interface broken), packetstormsecurity.com (host moved to packetstorm.news; limited), habr.com/ru/companies/tomhunter/articles (no June 2026 content), teletype.in/@cyberok (no June 2026 content), cve.org (limited).
**CISA KEV:** Catalog endpoint unreachable (403) — could not enumerate June 14–16 additions; cross-referenced via THN (CVE-2026-0257 PAN-OS GlobalProtect KEV with 2026-06-01 deadline already lapsed) and Rapid7 ETRs. Recommend defensive review of why CVE-2026-0257 (May 17 ITW + KEV with June 1 deadline) was not previously surfaced — calibration gap.

---

*Watchtower vulnerability-researcher | Cycle: 2026-06-16/night | Next: 2026-06-17/night*
