# Watchtower Night Report — 2026-06-04
**Cycle:** Night | **Generated:** 2026-06-04 06:00 UTC (2026-06-04T06:00:00Z)
**Sources checked:** 16/30 | **CISA KEV total:** unreachable (cisa.gov 403) | **New KEV additions:** CVE-2022-0492 Linux cgroup added 2026-06-02 (federal deadline 2026-06-05)

---

## 🔴 CRITICAL

### HTTP/2 Bomb (CVE-2026-49975 Apache; companion CVEs pending) — Remote DoS Against Apache httpd / NGINX / IIS / Envoy / Cloudflare Pingora, Three Major Implementations UNPATCHED, Public PoC
**Product:** Web servers and edge proxies — Apache httpd (mod_http2), NGINX, Microsoft IIS, Envoy, Cloudflare Pingora | **CVE:** CVE-2026-49975 (Apache mod_http2); companion CVEs pending for other implementations | **Status:** Partially Patched (Public PoC)

A new HTTP/2 denial-of-service class — branded the **"HTTP/2 Bomb"** — combines HPACK header-compression amplification with HTTP/2 flow-control stalling to take a target web server offline from a single client in under a minute, against default configurations. The technique was discovered by **OpenAI's Codex software agent** under the guidance of researchers at offensive security firm Calif (researcher Quang Luong, full details at the upcoming Real World AI Security conference) — making this the second high-impact infrastructure vulnerability surfaced by an autonomous AI tool this cycle (Redis CVE-2026-23479 below is the other). **PoC code is publicly available on GitHub.** NGINX patched in **1.29.8** (new `max_headers` directive); Apache httpd patched in **mod_http2 2.0.41** (CVE-2026-49975). **Microsoft IIS, Envoy, and Cloudflare Pingora remain unpatched** at time of report — vendors recommend either disabling HTTP/2 or fronting affected servers with a proxy/firewall that strips abusive header streams.

**Timeline:** Internal disclosure to vendors → simultaneous coordinated patches in Apache mod_http2 2.0.41 + NGINX 1.29.8 (2026-06-03) → public technique disclosure 2026-06-03 with PoC → IIS / Envoy / Pingora unpatched.

**Why it matters:** HTTP/2 is the dominant transport for public-facing web infrastructure (~70% of top-1M sites). A single-client DoS against the dominant edge proxies (Envoy, Pingora) and the dominant Windows web server (IIS) means an attacker with one machine can knock production-edge services offline — and three of the five named implementations have no patch yet. This is the first AI-discovered defensive infrastructure DoS class to hit production-edge in 2026 and the discovery cadence of AI-tool-found vulnerabilities is now sustained (Redis below + Linux kernel CVE-2026-31431 PoC drop + HTTP/2 Bomb in a single week).

**Discovered by:** OpenAI Codex agent + researcher Quang Luong, offensive security firm Calif.

**Mitigation:**
- Patch Apache httpd mod_http2 to **2.0.41+** and NGINX to **1.29.8+** immediately on every internet-facing instance; the NGINX patch introduces a `max_headers` directive that should be tuned conservatively for production workloads.
- For IIS, Envoy, and Cloudflare Pingora (no patch yet): disable HTTP/2 fallback to HTTP/1.1 where possible, OR front-end with a patched NGINX/Apache that strips abusive HTTP/2 frame patterns.
- Add HTTP/2 frame-rate and HPACK-decompression-ratio thresholds to WAF / DDoS-mitigation policy; the public PoC is the baseline traffic shape to alert on.
- Monitor edge-server CPU and connection-table metrics for sudden saturation from low-source-count clients — the attack signature is a single client driving the server to 100% CPU within seconds.
- Subscribe to vendor advisory channels for IIS / Envoy / Pingora — patches expected within 7-14 days given the public PoC.

**Sources:** [BleepingComputer — New 'HTTP/2 Bomb' DoS attack crashes web servers in under a minute](https://www.bleepingcomputer.com/news/security/new-http-2-bomb-dos-attack-crashes-web-servers-in-under-a-minute/) | [TheHackerNews — New HTTP/2 Bomb Vulnerability Allows Remote DoS on NGINX, Apache, IIS, Envoy & Cloudflare](https://thehackernews.com/2026/06/new-http2-bomb-vulnerability-allows.html) | [SecurityWeek — 'HTTP/2 Bomb' Exploit Knocks Web Servers Offline in Seconds](https://www.securityweek.com/http-2-bomb-exploit-knocks-web-servers-offline-in-seconds/) | [oss-security — HTTP/2 Bomb affects Apache httpd, nginx, envoy, & pingora (Alan Coopersmith, 2026-06-03)](https://www.openwall.com/lists/oss-security/2026/06/)

---

## 🟠 HIGH

### Linux Kernel CVE-2022-0492 (cgroups v1 release_agent) Added to CISA KEV — Active Container-Escape Exploitation Confirmed by Kaspersky, 3-Day Federal Deadline 2026-06-05
**Product:** Linux kernel (cgroups v1 subsystem) | **CVE:** CVE-2022-0492 | **CVSS:** 7.8 | **First reported:** 2026-06-02 (KEV addition)

CISA added the 3-year-old Linux kernel CVE-2022-0492 to the **Known Exploited Vulnerabilities catalog on 2026-06-02** with a **compressed 3-day federal remediation deadline of 2026-06-05**, after **Kaspersky published in-the-wild exploitation reporting this week** describing attacks targeting containerized environments. The flaw is an improper-authentication bug in `cgroup_release_agent_write()` that allows a local attacker inside a container with elevated capabilities (or with access to a vulnerable `cgroup_release_agent` write path) to **bypass namespace isolation, escalate privileges, and escape from the container to gain root-level access on the host**. Affected: kernel 2.6 through 4.20 and 5.5 through 5.17. Fixed in 4.9.301+, 4.14.266+, 5.4.177+, and subsequent stable branches. Multiple public PoCs have existed since 2022 — Kaspersky is the first authoritative confirmation of active in-the-wild abuse.

**Timeline:** Disclosed and patched 2022-Q1 → public PoCs throughout 2022-2025 → Kaspersky in-wild exploitation reporting 2026-06-02 → CISA KEV addition 2026-06-02 → federal deadline 2026-06-05.

**Why it matters:** Every Kubernetes / Docker / containerd / nerdctl host running an unpatched kernel ≤5.17 in the affected range is exposed. The bug requires initial container access but is the canonical container-escape primitive — once Kaspersky-reported activity ramps, expect ransomware and crypto-mining operators to bundle it into their post-compromise toolchains. Joins the 2026 KEV pattern of belated additions for pre-existing CVEs after sustained in-the-wild operator interest (parallels Oracle WebLogic CVE-2024-21182 KEV add 2026-06-01, Watchtower 2026-06-03 score 7). The compressed 3-day deadline indicates CISA has high-confidence incident-response visibility into ongoing exploitation.

**Mitigation:**
- Confirm kernel version on every container host; upgrade kernel beyond the affected range (≥5.17 stable or backport-patched 5.4.177+/5.10.97+/5.15.20+) immediately.
- Audit container `securityContext` for unnecessary `CAP_SYS_ADMIN` / privileged-mode containers — the exploit requires elevated capabilities; tightening this neutralizes most in-wild variants.
- Enable Falco / runtime-security rules to detect cgroup release_agent writes from inside container namespaces (the canonical exploit signature).
- For Kubernetes fleets: confirm PodSecurityPolicy / Pod Security Admission baseline disallows privileged pods; spot-audit clusters that allow privileged workloads (CI runners, monitoring agents).
- Hunt EDR / cloud-audit logs for unexpected `release_agent` writes or sudden privilege transitions from container PIDs since 2026-05-25 (start of Kaspersky-reported window).

**Sources:** [SecurityWeek — Organizations Warned of Exploited Linux Kernel Vulnerability](https://www.securityweek.com/organizations-warned-of-exploited-linux-kernel-vulnerability/) | [BleepingComputer — CISA warns of active attacks exploiting Android, Linux bugs](https://www.bleepingcomputer.com/news/security/cisa-warns-of-active-attacks-exploiting-android-linux-bugs/)

---

### Visual Studio Code Unpatched Zero-Day — One-Click GitHub OAuth Token Theft via Malicious Extension Auto-Install (Full Disclosure)
**Product:** Microsoft Visual Studio Code (all currently shipping versions) | **CVE:** Not yet assigned | **First reported:** 2026-06-03

Researcher **Ammar Askar** published **full technical disclosure** of an unpatched VS Code zero-day that allows an attacker to **steal a victim's GitHub OAuth token with a single click on a malicious link**. The flaw exploits VS Code's handling of OAuth token passing to **github.dev** (the browser-based VS Code variant): a crafted link runs malicious JavaScript inside a sandboxed webview that **simulates keypresses in the main editor to auto-install a malicious extension**, which then exfiltrates the GitHub OAuth token. Critically, the stolen token grants **"full access to every other repo that you have access to,"** not just the targeted repository — making this a clean **developer-to-repository-scope pivot** primitive. Askar chose **full public disclosure due to frustration with Microsoft's security response** (citing prior bugs that were silently patched without credit) — this lands in the middle of the broader Microsoft-vulnerability-disclosure controversy (Watchtower 2026-06-03 noted item on Microsoft's legal threats to researchers).

**Timeline:** Internal report to Microsoft (date unspecified) → silent patches of related bugs without credit → researcher frustration → **full public disclosure 2026-06-03 with PoC** → no patch yet.

**Why it matters:** Developer credentials are the highest-leverage pivot in 2026 — the Miasma supply-chain worm (Watchtower 2026-06-02 / 2026-06-03 update) demonstrated that one compromised developer account can publish 96 trojanized packages in 72 seconds. A one-click full-OAuth-scope GitHub token theft is the natural delivery vector for the next Miasma-class operator. Combined with the unpatched status and public PoC, every developer workstation with VS Code installed and GitHub access is a single click away from full repo control. Score 7 reflects the developer-credential pivot weight and full-disclosure status — would be 8 if in-wild exploitation were confirmed.

**Discovered by:** Ammar Askar (independent researcher).

**Mitigation:**
- Clear cookies + local site data for **github.dev** in every browser used by developers (forces re-auth, which surfaces unexpected sign-in dialogs as exploitation attempts).
- Restrict GitHub OAuth scopes: where possible, use fine-grained PATs scoped to individual repos rather than classic broad-scope OAuth tokens.
- Disable automatic extension installation in VS Code (`extensions.autoInstall: false`) and audit currently installed extensions for unfamiliar publishers.
- For organizations: enforce GitHub Enterprise SSO + IP allowlisting on developer accounts so a stolen OAuth token cannot be used outside corporate egress IPs.
- Monitor GitHub audit logs for anomalous repo-clone / repo-fork / repo-secret-read activity from developer accounts since 2026-06-03.

**Sources:** [BleepingComputer — VS Code zero-day lets hackers steal GitHub tokens in one click](https://www.bleepingcomputer.com/news/security/vs-code-zero-day-lets-hackers-steal-github-tokens-in-one-click/) | [TheHackerNews — One-Click GitHub Dev Attack Lets Attackers Steal Full GitHub OAuth Tokens](https://thehackernews.com/2026/06/one-click-github-dev-attack-lets.html)

---

### CISA + FBI + EPA Joint Advisory — Internet-Exposed Automatic Tank Gauges Actively Exploited Across US Gas Stations, Iran-Linked Per CNN
**Product:** Automatic Tank Gauge (ATG) systems — gas-station and fuel-storage telemetry, internet-exposed | **CVE:** None assigned (multi-class) | **First reported:** 2026-06-03

CISA, the FBI, and the EPA issued a **joint advisory** confirming **active in-the-wild exploitation of internet-exposed Automatic Tank Gauge (ATG) systems** at gas stations across multiple US states, with **CNN reporting Iranian-hacker attribution**. Attackers chained authentication bypass + hardcoded credentials + OS command injection + SQL injection + privilege escalation to reach the management plane, then **modified network settings, product identifiers, tank-volume readings, and pump controls**, and **disabled alerts** — a combination that hides fuel loss / leak conditions and can cause **physical equipment damage**. Sectors affected: Energy, Chemical, Food & Agriculture, Transportation Systems.

**Why it matters:** This is the second 2026 cycle of Iran-attributed ICS-targeting in CONUS (Verizon VoLTE / Polycom + earlier 2025 water-utility campaigns are the comparable precedents). For our scope, the corporate angle is **third-party fuel-delivery infrastructure for fleet operations and on-site fuel storage at corporate campuses / data centers** — many of these tanks are managed by contractors who exposed them via Internet for remote telemetry without considering they were exposed to the public Internet. Score 6 reflects the joint-advisory active-exploitation status balanced against the OT/contractor scope (mostly out of direct corporate-perimeter scope but in third-party-risk scope).

**Mitigation:**
- Inventory every contractor-managed fuel-storage tank / ATG system attached to corporate-owned facilities; require contractor attestation of patch / segmentation status.
- Block ATG management ports (Veeder-Root TLS-450 default `TCP/10001`, similar protocols) at corporate edge.
- Audit corporate VPN logs for unexpected access from fuel-delivery contractor accounts to ATG management interfaces since 2026-04-01.
- Coordinate with facilities / fleet teams to ensure any ATG with internet exposure is moved behind a VPN with MFA; replace default passwords; enable MFA on management consoles.
- Tabletop the scenario "fuel-storage telemetry compromised by adversary" with facilities + IR teams.

**Sources:** [BleepingComputer — CISA warns of cyberattacks targeting fuel tank monitoring systems](https://www.bleepingcomputer.com/news/security/cisa-warns-of-cyberattacks-targeting-fuel-tank-monitoring-systems/)

---

## 🟡 MEDIUM

### Django Security Release — Five-CVE Batch Patched in 6.0.6 / 5.2.15 (CVE-2026-6873, 7666, 8404, 35193, 48587)
**Product:** Django web framework | **CVE:** CVE-2026-6873, CVE-2026-7666, CVE-2026-8404, CVE-2026-35193, CVE-2026-48587 | **Published:** 2026-06-03

Django Software Foundation announced security releases **6.0.6 and 5.2.15** on 2026-06-03 (Natalia Bidart) patching **five CVEs** — disclosed in the standard oss-security pre-disclosure window. The advisory headlines are still propagating to mainstream coverage; oss-security carries the canonical CVE list (CVE-2026-6873, CVE-2026-7666, CVE-2026-8404, CVE-2026-35193, CVE-2026-48587). Individual severity assignments and exploitation-precondition detail still pending — historical Django security release batches have ranged from moderate (account-enumeration, header-injection) to high (template-injection, ORM-injection) classes. No PoC and no in-wild exploitation reported yet.

**Why it matters:** Django is a tier-1 Python web framework with significant deployment across enterprise marketing-property, e-commerce, and SaaS-backend footprints — every batch of Django CVEs needs to be rolled out to every Django-fronted internet-facing service within the patch window. The fact that this was a coordinated 5-CVE batch (not a one-off) means at least one of the five is likely a moderate/high-impact bug worth scheduling around. Default: schedule patch deployment for this week; revisit severity score upward if individual CVEs disclose template-injection or ORM-injection class.

**Mitigation:**
- Upgrade Django to **6.0.6** (on 6.0.x) or **5.2.15** (on 5.2.x LTS) on every internet-facing Django deployment.
- Subscribe to django-announce for the per-CVE severity advisories due in the next 48-72 hours.
- For deployments unable to patch immediately: enumerate the per-CVE preconditions when individual advisories land; mitigate any that affect admin or auth paths first.

**Sources:** [oss-security — Django CVE-2026-6873, CVE-2026-7666, CVE-2026-8404, CVE-2026-35193, and CVE-2026-48587 (Natalia Bidart, 2026-06-03)](https://www.openwall.com/lists/oss-security/2026/06/) | [Django security release announcement (2026-06-03)](https://www.djangoproject.com/weblog/)

---

### Redis CVE-2026-23479 — 2-Year-Old Use-After-Free RCE Discovered by Autonomous AI Tool Xint Code, Patched May 5 But Long-Tail Patch Adoption
**Product:** Redis (in-memory data store) | **CVE:** CVE-2026-23479 | **CVSS:** 8.8 (CVSS 3.1) | **Published:** 2026-06-03 (research publication)

Theori's **Xint Code autonomous security tool** discovered a use-after-free vulnerability in Redis's blocking-client code that had been **present in every stable branch since Redis 7.2.0 (introduced 2 years ago) and undetected** until the AI-led research. The bug is in `unblockClientOnKey()`: when a queued command is dispatched through `processCommandAndResetClient()`, that function can free the client as a side effect — yet the caller continues using the freed pointer. **Exploitation requires authenticated access** with permissions spanning the `@admin`, `@scripting`, `@stream`, and `@read/@write` ACL categories; the **default Redis user is granted these permissions**, so the bug is exploitable in default configurations. Affected: 7.2.0–7.2.13, 7.4.0–7.4.8, 8.2.0–8.2.5, 8.4.0–8.4.2, 8.6.0–8.6.2. Patched May 5, 2026 in 7.2.14, 7.4.9, 8.2.6, 8.4.3, 8.6.3.

**Why it matters:** Redis is the canonical caching / session-store backplane for ~30-50% of enterprise web stacks. The patches landed May 5 but the public RCE-class disclosure landed 2026-06-03, meaning the patch-to-public-PoC interval is ~28 days — long enough that Redis instances on default ACL configurations on outdated minor versions are now broadly exposed. This is the **third AI-discovered defensive infrastructure vulnerability this cycle** (HTTP/2 Bomb above + Linux kernel CVE-2026-31431 PoC released this week + Redis) and the trend is now operationally confirmed: AI tools are clearing 2-3-year-old technical debt out of common infrastructure projects at a sustained cadence.

**Mitigation:**
- Upgrade Redis to a patched minor: **7.2.14 / 7.4.9 / 8.2.6 / 8.4.3 / 8.6.3** on every cache / session-store deployment.
- For environments running default ACL: review the `default` user's command permissions; constrain to read-only or remove `@admin` / `@scripting` from any internet-adjacent Redis (best practice anyway, but enforced as result of this CVE).
- Confirm Redis is not internet-exposed (canonical TCP/6379 should never be on a public IP); if internet-exposed by accident, treat as fully compromised post-disclosure window.
- Hunt Redis logs for unusual `BLPOP` / `BRPOPLPUSH` / `XREAD BLOCK` patterns from authenticated clients since 2026-05-05 (patch window) — the use-after-free trigger sits on the blocking-command path.

**Sources:** [TheHackerNews — Autonomous AI Tool Finds 2-Year-Old RCE Flaw in Redis (CVE-2026-23479)](https://thehackernews.com/2026/06/autonomous-ai-tool-finds-2-year-old-rce.html) | [oss-security — 5 CVEs in Redis (Alan Coopersmith, 2026-06-03)](https://www.openwall.com/lists/oss-security/2026/06/)

---

### Acer Wave 7 Routers — CVE-2026-49200 (Plaintext Credential Exposure) + CVE-2026-49201 (Hardcoded Crypto Key for Backup-Backdoor Injection), Vendor Says Patch By End of June
**Product:** Acer Wave 7 mesh routers (firmware ≤ T7c_GBL_1.01.000055) | **CVE:** CVE-2026-49200, CVE-2026-49201 | **Severity:** Vendor "maximum" rating | **Published:** 2026-06-03

Acer disclosed two **vendor-rated "maximum severity" zero-days** in its Wave 7 mesh-router line, discovered by researcher **Gergo Pap**. **CVE-2026-49200** is a broken-access-control bug allowing **unauthenticated remote retrieval of plaintext credentials from log archives**. **CVE-2026-49201** is a **hardcoded cryptographic key** that allows an attacker to **inject a persistent backdoor into device backup files** which the device will accept on restore. Acer states the patches are scheduled for "**deployment by the end of June 2026**" — meaning every Wave 7 router on the affected firmware is exposed for ~4 weeks. No active exploitation reported yet.

**Why it matters:** Wave 7 is a consumer-tier mesh-router line; the corporate-defensive angle is **employee home/remote-work network attack surface + small-office router fleet**. The combination of plaintext-credential exposure + backup-backdoor primitive is the same primitive class abused by VPN-Filter / Cyclops Blink against home routers in prior campaigns — once a PoC drops (likely within the patch window), expect crimeware operators to incorporate this into mass-scanning toolchains. Score 5 reflects the consumer/SOHO scope (mostly out of direct corporate perimeter) balanced against the unpatched-status and zero-day disclosure.

**Mitigation:**
- For corporate-managed home / SOHO router fleets: identify Acer Wave 7 devices via asset inventory; disable WAN management interfaces until patches ship.
- Communicate to remote workforce: do not expose home-router admin interfaces to WAN; review for default credentials.
- When the patch ships (vendor target: end of June 2026), coordinate fleet-wide push via vendor cloud-management if available.

**Sources:** [BleepingComputer — Acer working to patch max severity zero-days in Wave 7 routers](https://www.bleepingcomputer.com/news/security/acer-warns-of-max-severity-zero-days-affecting-wave-7-routers/)

---

### Atlas RAT Campaign — TA4922 (Chinese-Speaking Cybercrime, Silver Fox / Void Arachne Overlap) Expanding From East Asia Into Germany / Italy / UK / South Africa
**Product:** Atlas RAT — feature-rich Windows RAT with anti-sandbox / anti-Defender-Application-Guard checks, keylogging, screenshot/audio/webcam recording, plugin loader | **CVE:** None (phishing-delivered) | **First reported:** 2026-06-03

Proofpoint published research on **TA4922**, a Chinese-speaking cybercrime cluster (overlapping with **Silver Fox** and **Void Arachne** indicator-of-compromise sets but tracked separately due to financial-motivation framing) that has **expanded global operations** beyond historical East Asia targeting and is now **conducting more unique campaigns than any other tracked cybercrime threat actor** as of 2026-Q2. Recent campaigns target **Germany, Italy, the United Kingdom, and South Africa** with **localized phishing lures** (payroll notices, tax audits, VAT filings, HR communications) delivering the new **Atlas RAT** family — which includes anti-sandbox checks, anti-Microsoft-Defender-Application-Guard evasion, and a plugin/loader architecture for follow-on payloads. No CVE involved; pure social-engineering delivery.

**Why it matters:** TA4922's cadence (most-active cybercrime group of 2026-Q2 per Proofpoint) + the Europe-region targeting expansion makes this a high-volume noise generator that will hit corporate inboxes with regional-language phishing. The Atlas RAT's anti-Defender-Application-Guard evasion is the noteworthy defensive bit — this is a class of RAT that explicitly avoids the canonical Microsoft sandboxing primitive that orgs deploy as a phishing mitigation. Score 4-5 reflects the no-CVE phishing nature balanced against the high campaign volume.

**Mitigation:**
- Enable Microsoft Defender Application Guard (MDAG) for Office documents on managed endpoints if not already; tune Defender for Endpoint to detect Atlas RAT anti-MDAG checks (publicly available IoCs from Proofpoint).
- Geo-flag region-specific phishing lures: payroll-notice / tax-audit / VAT-filing lures in DE / IT / UK / ZA inbox patterns should trigger elevated phishing analysis.
- Ingest Proofpoint Atlas RAT IoCs into SIEM / EDR; block C2 domains / IPs at corporate egress.
- Reinforce phishing training in DE / IT / UK / ZA subsidiaries; emphasize HR / payroll / tax-document lures.

**Sources:** [BleepingComputer — Chinese hackers use new Atlas RAT malware in European cyberattacks](https://www.bleepingcomputer.com/news/security/chinese-hackers-use-new-atlas-rat-malware-in-european-cyberattacks/)

---

### Global Stock Exchange Espionage — 150-Day Senior-Executive Outlook Mailbox Compromise, Adobe / OneDrive Masquerade
**Product:** Unnamed major stock exchange (researcher withheld attribution); Microsoft Outlook / Windows endpoint | **CVE:** Not disclosed | **First reported:** 2026-06-03

Unspecified researchers disclosed a **150-day undetected espionage operation** against a **major global stock exchange** running from **October 2025 through March 2026**. Attackers compromised a **senior executive's Outlook mailbox**, deployed malware **disguised as Adobe and OneDrive applications**, **re-registered scheduled tasks disguised as Adobe / Lenovo / OneDrive system services** for persistence, and exfiltrated data in **small batches via Dropbox and OneDrive** cloud channels. The initial-access vector and threat-actor attribution are **deliberately withheld**. SecurityWeek characterizes the operation as **"most likely espionage"** targeting **negotiations and market-moving event intelligence**.

**Why it matters:** The 150-day dwell time and the LotL persistence-via-legit-cloud-storage pattern (Adobe / Lenovo / OneDrive masquerade + Dropbox/OneDrive exfil) is the canonical 2026 mature-APT signature. For our scope, this is a **calibration data point** on senior-executive-mailbox-targeting tradecraft — particularly the **Adobe / Lenovo / OneDrive scheduled-task masquerade** which is detectable as anomaly in Windows scheduled-task creation logs. Score 4 reflects no-CVE-no-attribution-no-name calibration value rather than direct actionable defense.

**Mitigation:**
- Audit corporate Windows scheduled tasks for entries impersonating Adobe / Lenovo / OneDrive system services that do not correspond to currently installed software builds; baseline expected legitimate tasks.
- Monitor for executive Outlook mailbox download / forward-rule anomalies — 150 days of small-batch data exfiltration is the signature.
- Constrain Dropbox + OneDrive corporate egress to known approved tenants; alert on exfiltration to personal Dropbox / OneDrive accounts.
- Reinforce executive-mailbox MFA + Conditional Access policies; treat senior-executive mailboxes as crown-jewel assets in tabletop exercises.

**Sources:** [SecurityWeek — Hackers Target Global Stock Exchange in Espionage Operation](https://www.securityweek.com/hackers-target-global-stock-exchange-in-espionage-operation/)

---

### Windows Search URI Handler — Unpatched NTLMv2 Hash-Leak via `search:` Crumb-Location Parameter, Microsoft Declined to Patch (Moderate Rating)
**Product:** Windows Search URI handler (`search:` protocol) | **CVE:** Not assigned (Microsoft declined to issue) | **First reported:** 2026-06-03

**Huntress** published full disclosure of an **unpatched Windows Search URI vulnerability** that allows an attacker to **leak the victim's Net-NTLMv2 hash to an attacker-controlled SMB server** with a single click on a crafted link. The technique abuses the `search:` and `crumb=location:` parameters in a way structurally identical to **CVE-2026-33829 (Snipping Tool)** and **CVE-2023-35636 (Outlook)** — both of which Microsoft did patch. Microsoft **declined to address this variant**, stating "only Important and Critical severity cases meet our bar for servicing" — assigning it a Moderate rating. Captured Net-NTLMv2 hashes can be **relayed for network access** or **offline-cracked for password recovery**.

**Why it matters:** This is the third Microsoft-NTLM-hash-leak primitive in the post-CVE-2023-35636 era — and each iteration becomes a fresh phishing payload until the SMB-egress hygiene is enforced organization-wide. The combination of **Huntress full-disclosure + Microsoft refusal to patch + public PoC** means this is now an off-the-shelf phishing-payload component. Defensive angle: **outbound SMB egress (TCP/445, TCP/139) should already be blocked at the corporate edge** — this CVE class continues to recur until that hygiene is universally enforced.

**Mitigation:**
- Block outbound SMB (TCP/445, TCP/139) at every corporate egress point — including remote-worker VPN / SASE / ZTNA tunnels.
- Enforce SMB signing org-wide to prevent NTLM-relay attacks against any captured hashes that do leak.
- Consider disabling NTLM authentication entirely where feasible (Kerberos-only); for environments unable to disable, enforce Channel Binding Tokens and Extended Protection for Authentication.
- Block / strip `search:` URI handler in browser / email-client URL-handler policy where business operations allow.
- Reinforce phishing training: any link with an unexpected URI scheme (`search:`, `ms-search:`, `ms-help:`, etc.) is suspicious.

**Sources:** [TheHackerNews — Unpatched Windows Search URI Vulnerability Lets Attackers Steal NTLMv2 Hashes](https://thehackernews.com/2026/06/unpatched-windows-search-uri.html)

---

## 📋 Noted / Monitoring

**FortiGuard C0XMO Gafgyt variant** — New Gafgyt-derived IoT botnet variant leveraging DD-WRT exploitation for multi-arch propagation (FortiGuard 2026-06-03); IoT-botnet calibration only.

**DesckVB RAT — Google DoubleClick malspam campaign** — .NET RAT (active since 2026-02) delivered via Google DoubleClick redirect → personalized phishing PDF lure → ZIP/JS loader; ~80K endpoint footprint reported by THN.

**Linux Kernel CVE-2026-31431 "Copy Fail" PoC drop** — Multiple GitHub PoCs (Rust + C) for the Theori-Xint-Code-discovered Linux kernel LPE; LPE-only (no remote vector) but indicates active exploit-tool development.

**Iran Nobitex Crypto Exchange OFAC Sanction** — US Treasury sanctioned Iran's largest crypto exchange used for terror-financing-adjacent ransomware payments (BleepingComputer 2026-06-03); sanctions / policy calibration.

**Europol — 9 organized-crime groups dismantled in EU-wide illegal-streaming bust** — 29 arrests; law-enforcement calibration data point.

**Schneier — Microsoft tries to calm legal-threat fears after zero-day disclosure backlash** — Follow-up on Watchtower 2026-06-03 noted item (Microsoft legal threats to Windows-exploit researcher); Microsoft attempting damage control but disclosure policy unchanged.

**WhatsApp / Slack / Gemini notification prompt-injection (SafeBreach)** — "Invitation Is All You Need" successor demonstrating Gemini voice-assistant hijack via poisoned notifications from messaging apps; patched server-side by Google in 2025-11; novel prompt-injection technique data point.

**OpenStack Ironic CVE-2026-46447 / CVE-2026-48681 / CVE-2026-44917 + Mistral policy bypass** — Script injection + ISO path traversal + pxe_template file extraction in Ironic; Mistral policy enforcement bypass; patches in coordinated errata (Goutham Pacha Ravi / Jay Faulkner, oss-security 2026-06-03).

**Linux Kernel TLS UAF in tls_sk_proto_close() (Oleg Sevostyanov, oss-security 2026-06-02)** — Persistent on day-two coverage; CVE pending; LPE-class.

**VU#595768 Securly Chrome Extension — multiple weak-encryption + access-control vulnerabilities** — Browser extension family; weak crypto + ACL issues; education-segment Chrome-extension scope.

**Oracle Java CVE-2026-47065 (PT-Security PT-2026-45913, CVSS 9.8)** — Pre-disclosure of an Oracle Java CVSS 9.8; researcher Keda; vendor-advisory page expected closer to July 2026 Oracle CPU.

**Oracle REST Data Services CVE-2026-46775 (opencve, CVSS 9.9) + Oracle Database CVE-2026-46833 (opencve, CVSS 9.0)** — Pre-published Oracle CVE assignments visible on opencve (vendor-advisory page pending); watch for July 2026 Oracle CPU bundling.

**Microsoft 365 Android Token-Theft via Debug Flag (SecurityWeek exclusive expanded)** — One development flag left enabled on production builds; mobile-only and OOS for direct corporate defense unless BYOD-exposed; logged in Watchtower 2026-06-03 noted, expanded today with detailed SecurityWeek writeup.

**Google Android June 2026 Security Bulletin — actively exploited CVE-2025-48595 + 123 additional flaws** — Mobile-only and OOS but pre-disclosure window opened today; CVE-2025-48595 KEV-add expected.

**IMA Diligence Services breach — 525,000 records** — Third-party diligence vendor breach via legacy-server compromise (SecurityWeek 2026-06-03); supply-chain / third-party-risk calibration.

**Google Android AI deepfake-call protection (defensive feature)** — Android feature that detects AI-impersonated personal-contact phone calls; defensive control rollout calibration data point.

**Hackers Used Meta AI Bot to Seize Instagram Accounts (Krebs follow-up)** — Krebs published deeper analysis of the 2026-06-02 NEWS Meta AI / Instagram account-takeover (Obama White House, US Space Force defaced with pro-Iranian content); Meta deployed emergency patch.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (403 Forbidden — KEV-add inferred from BC/SW relay) |
| Vendor advisories | fortinet.com/blog/threat-research, blog.cloudflare.com/tag/security, msrc.microsoft.com/blog | ✅/⚠️ |
| Research / OSINT | schneier.com, krebsonsecurity.com, rapid7.com, avleonov.com, googleprojectzero.blogspot.com, securitylab.github.com, kb.cert.org/vuls, attackerkb.com | ✅/❌ (attackerkb 403) |
| CVE databases | opencve.io, nvd.nist.gov, cve.org, cve.mitre.org, dbugs.ptsecurity.com, github.com/0xMarcio/cve, github.com/search?q=CVE | ✅/⚠️ |
| Full Disclosure / OSS | seclists.org/fulldisclosure, packetstormsecurity.com, oss-security (via openwall) | ⚠️ (seclists/packetstorm degraded; oss-security via openwall fully checked) |
| Bug bounty | hackerone.com/hacktivity, bugcrowd.com/disclosures | ⚠️/❌ (bugcrowd 404) |
| Russian / Ukrainian | habr.com/ru/companies/tomhunter/articles, teletype.in/@cyberok, cert.gov.ua | ⚠️ (no June content surfaced) |

**Errors:** cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403), attackerkb.com (403), bugcrowd.com/disclosures (404), cve.mitre.org (no usable content surfaced).

**Degraded (page reachable but no actionable June 2-3 content):** seclists.org/fulldisclosure (redirects), packetstormsecurity.com (redirect to packetstorm.news, only aggregate stats), nvd.nist.gov (homepage only), cve.org (no usable content), msrc.microsoft.com/blog (no content), hackerone.com/hacktivity (no public hacktivity feed), habr.com/ru/companies/tomhunter/articles (no June content), teletype.in/@cyberok (no June content), cert.gov.ua (no usable content).

**CISA KEV:** cisa.gov pages 403-blocked all cycle — KEV-add inference from BleepingComputer + SecurityWeek + TheHackerNews relay coverage. CVE-2022-0492 Linux kernel cgroup added 2026-06-02 with federal deadline 2026-06-05 (3-day compressed deadline indicating high CISA confidence in active exploitation).

---

*Watchtower vulnerability-researcher | Cycle: 2026-06-04/night | Next: 2026-06-05/night*
