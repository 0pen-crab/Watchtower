# Watchtower Night Report — 2026-06-06
**Cycle:** Night | **Generated:** 2026-06-06 06:00 UTC (2026-06-06T06:00:00Z)
**Sources checked:** 25/30 | **CISA KEV total:** unreachable (403 — inferred via BC/SW/THN relay) | **New KEV additions:** SolarWinds Serv-U CVE-2026-28318 (federal deadline 2026-06-19)

---

## 🔴 CRITICAL

*(No tier-9+ items today. The Cisco SD-WAN unpatched zero-day below sits at 8 — close to CRITICAL given active exploitation and root-equivalence on SD-WAN management, but the blast radius is bounded by SD-WAN Manager exposure rather than the general internet.)*

---

## 🟠 HIGH

### Cisco Catalyst SD-WAN Manager CVE-2026-20245 — Unpatched Zero-Day, Active Exploitation, Root Command Execution (Seventh SD-WAN Zero-Day in 2026)
**Product:** Cisco Catalyst SD-WAN Manager (formerly vManage) | **CVE:** CVE-2026-20245 | **CVSS:** not yet published | **Status:** 0-Day (Unpatched) — Active Exploitation Confirmed

Cisco PSIRT issued an emergency advisory on 2026-06-05 warning of in-the-wild exploitation of CVE-2026-20245 in Catalyst SD-WAN Manager. The vulnerability allows an unauthenticated remote attacker to execute arbitrary OS commands with root privileges on the SD-WAN management plane. No patch is currently available; Cisco's recommended mitigation is to restrict management-plane access to trusted IPs and disable internet-facing administrative interfaces. This is the **seventh SD-WAN zero-day Cisco has confirmed in 2026** — joining CVE-2026-20127 (KEV March 2026), CVE-2026-20182 (Rapid7 advisory), and four earlier 2026 CVEs.

**Timeline:** 2026-06-05 Cisco PSIRT emergency advisory → BC + SW relay same day → patch ETA "as soon as possible" per Cisco; threat-research team confirmed exploitation in customer telemetry pre-disclosure.

**Why it matters:** SD-WAN Manager is the control plane for an entire SD-WAN fabric — a compromised vManage host hands an attacker policy-push, certificate, and edge-device-config authority across the customer's WAN. A 2026 cadence of seven SD-WAN zero-days (more than one every other month) confirms Cisco SD-WAN is now a tier-1 attacker target in line with Fortinet FortiGate and PAN-OS GlobalProtect. Audit perimeter exposure of /dataservice and similar SD-WAN Manager URLs immediately.

**Discovered by:** Cisco's own threat-research team identified exploitation in customer telemetry.

**Mitigation:**
- Restrict SD-WAN Manager management-plane access to a small allow-list of admin source IPs (jump hosts / management VPN only).
- Block internet ingress to SD-WAN Manager HTTPS interfaces at the edge until patched.
- Hunt for anomalous root-shell processes spawning from SD-WAN Manager web services (`tomcat`, `nginx`).
- Review SD-WAN policy/template changes since 2026-05-01 for unexpected modifications.
- Treat the SD-WAN Manager host as compromised if it has been internet-reachable in the past 30 days; rotate platform certs and edge-device shared secrets after patching.

**Sources:** [BleepingComputer — Cisco SD-WAN zero-day](https://www.bleepingcomputer.com/news/security/cisco-warns-of-unpatched-sd-wan-zero-day-exploited-in-attacks/) | [SecurityWeek — Cisco's 7th SD-WAN zero-day of 2026](https://www.securityweek.com)

---

### IronWorm npm Supply-Chain Attack — Rust Infostealer with eBPF Kernel Rootkit, Tor C2, and Self-Propagation via npm Trusted Publishing (36 Packages)
**Product:** npm registry, asteroiddao publisher (compromised); 36 packages contaminated | **CVE:** None assigned | **CVSS:** N/A | **First reported:** 2026-06-04

JFrog (with Ox Security, Endor Labs, and StepSecurity corroborating) disclosed a self-replicating Rust-based worm dubbed **IronWorm** propagating across npm via a compromised publisher account "asteroiddao." The malware ships an **eBPF kernel rootkit** for evasion and exfiltrates **86 environment variables + 20 credential files** including OpenAI, Anthropic, AWS, npm, SSH, and crypto-wallet secrets to a Tor hidden service. The novel propagation mechanism abuses **npm's Trusted Publishing OIDC workflow** — stolen GitHub Actions tokens are used to publish trojanized package versions back to npm, enabling automatic lateral movement across the npm graph without operator interaction. Commit timestamps are backdated up to 13 years to evade triage heuristics, and exfiltrated secrets are uploaded as fake "lint output" build artifacts via GitHub Actions. The operators hardcoded their own crypto-wallet recovery phrase to prevent the worm from stealing it during testing.

**Timeline:** 2026-06-04 JFrog disclosure → THN + BC + Socket relay same day → npm package removals + GHSA advisories rolling 06-04→06-05.

**Why it matters:** IronWorm is the **third Wave-2-class supply-chain worm in 30 days** (chalk-template clone 05-19, Miasma @redhat-cloud-services 06-02, IronWorm 06-04), confirming the MEMORY 2026-05-19 prediction of 3-7 distinct Wave-2 supply-chain compromises by mid-June. Two new durable patterns: (i) **npm Trusted Publishing OIDC tokens are now a Wave-2 propagation primitive** — the same OIDC-from-CI-runner that gives "passwordless publishing" gives the worm passwordless lateral movement; treat OIDC-based npm publish workflows as code-execution paths from CI to the public registry, scope them as tight as deploy keys; (ii) **eBPF kernel rootkits are now standard in mature Wave-2 worm payloads** — endpoint-detection telemetry that doesn't see syscalls (because eBPF intercepts them in-kernel) will miss the next generation; deploy eBPF-rootkit-detection tooling (e.g. tracee, eBPFGuard) on dev/CI workstations alongside conventional EDR.

**Discovered by:** JFrog Security Research; Ox Security, Endor Labs, StepSecurity (corroborating).

**Mitigation:**
- Audit GitHub Actions workflows for any npm publish step using Trusted Publishing OIDC; restrict environment protection rules so publish jobs can only run from `main` after manual approval.
- Block egress to Tor hidden-service entry guards from dev/CI workstations.
- Rotate any OpenAI / Anthropic / AWS / npm / SSH credentials present on dev workstations that pulled npm packages between 2026-05-25 and 2026-06-04.
- Inspect package.json files for newly-added `preinstall` script hooks against any direct-or-transitive dependency from `asteroiddao` (or any newly-active publisher with a 13-year-backdated commit history).
- Deploy eBPF-aware rootkit detection (tracee / bpftool inspection of attached programs) on dev/CI workstations.
- Review GitHub Actions artifact uploads for files masquerading as "lint output" but containing serialized secrets.

**Sources:** [BleepingComputer — IronWorm npm 36 packages](https://www.bleepingcomputer.com/news/security/new-ironworm-malware-hits-36-packages-in-npm-supply-chain-attack/) | [The Hacker News — IronWorm](https://thehackernews.com) | [JFrog Security Research](https://jfrog.com)

---

### Everest Forms Pro CVE-2026-3300 (CVSS 9.8) — Unauthenticated Remote Code Execution via eval() Injection, Active Mass Exploitation
**Product:** Everest Forms Pro WordPress plugin (Calculation Addon), all versions ≤ 1.9.12; patched in 1.9.13 | **CVE:** CVE-2026-3300 | **CVSS:** 9.8 | **First reported:** 2026-06-05

THN published 2026-06-05 confirming active mass exploitation of CVE-2026-3300 in Everest Forms Pro, a popular premium WordPress form plugin. The Calculation Addon concatenates user-submitted form field values directly into a PHP code string and passes it to `eval()` without escaping, yielding unauthenticated remote code execution on any site using a form with the Calculation Addon enabled. Patched in 1.9.13.

**Timeline:** Vendor patch 1.9.13 published ahead of public disclosure → THN reporting confirms attempted mass exploitation visible in WordPress security firm telemetry as of 2026-06-05.

**Why it matters:** Joins the 2026-Q2 WordPress-plugin-as-AVP cluster (WP Maps Pro CVE-2026-8732 06-01, Kirki CVE-2026-8206 06-03, Funnel Builder MEMORY 2026-05-16) — fourth active-exploit WordPress plugin disclosure in 8 days. The pattern is now structurally durable: any plugin handling user-submitted data with a calculation / template / eval primitive is a near-certain unauth-RCE candidate. WordPress operators with form/calculator/template-engine plugins should treat the next 14 days as elevated risk and pre-stage patch deployment SLAs.

**Discovered by:** Reported via Wordfence threat intelligence (vendor unattributed in initial coverage).

**Mitigation:**
- Upgrade Everest Forms Pro to ≥ 1.9.13 immediately.
- WAF rule: block form-submit POST bodies containing PHP code patterns (`system(`, `passthru(`, `<?php`, backticks) targeting plugin AJAX endpoints.
- Hunt webroot for newly-created PHP files under `wp-content/uploads/` and `wp-content/plugins/` from the past 14 days; review admin user table for unfamiliar accounts.
- Audit WordPress estate for other plugins implementing user-controlled formula/template/eval primitives; pre-emptively disable un-needed calculator add-ons.

**Sources:** [The Hacker News — Everest Forms Pro CVE-2026-3300](https://thehackernews.com) | Wordfence threat intelligence

---

## 🟡 MEDIUM

### SolarWinds Serv-U CVE-2026-28318 — KEV-Added, Active Exploitation, Resource-Exhaustion DoS via Crafted POST Requests
**Product:** SolarWinds Serv-U file transfer (HTTP/HTTPS/FTP/FTPS/SFTP) prior to 15.5.4 Hotfix 1; ~12,000 internet-exposed instances per Shodan | **CVE:** CVE-2026-28318 | **CVSS:** not yet published | **Published:** 2026-06-05

CISA added CVE-2026-28318 to the KEV catalog on 2026-06-05 with a federal remediation deadline of 2026-06-19 following confirmed exploitation in the wild. The vulnerability is uncontrolled resource consumption triggered by unauthenticated POST requests bearing `Content-Encoding: deflate` headers; impact is denial-of-service via server crash, not RCE. SolarWinds released Serv-U 15.5.4 Hotfix 1 on 2026-06-05 alongside the advisory.

**Mitigation:** Upgrade to 15.5.4 Hotfix 1; restrict Serv-U HTTP/HTTPS management-plane access to a small allow-list; block POST requests with `Content-Encoding: deflate` headers at the edge proxy / WAF until patched; hunt for unexpected Serv-U process restarts in the past 14 days as a low-confidence indicator of probing.

**Sources:** [BleepingComputer — CISA flags Serv-U CVE-2026-28318](https://www.bleepingcomputer.com/news/security/cisa-hackers-now-exploit-solarwinds-serv-u-flaw-to-crash-servers/) | SolarWinds advisory

---

### Cisco Unified Communications Manager CVE-2026-20230 — SSRF → Arbitrary File Write → Root Escalation, Public PoC Available, WebDialer Default-Off
**Product:** Cisco Unified Communications Manager with WebDialer service enabled; fixed in 14SU6 / 15SU5 | **CVE:** CVE-2026-20230 | **CVSS:** 8.6 | **Published:** 2026-06-04

Cisco disclosed CVE-2026-20230 in Unified CM 2026-06-04. An unauthenticated SSRF in the WebDialer Web Service allows attackers to coerce HTTP requests inside the OS, write files to disk, and chain to root privilege escalation. A public PoC was released within 24 hours; no confirmed in-the-wild exploitation yet. WebDialer is disabled by default, limiting blast radius to operators who explicitly enabled it.

**Mitigation:** Patch to 14SU6 or 15SU5; until then disable Cisco WebDialer Web Service in Service Activation if not actively used; review Unified CM webroot for unexpected file writes since 2026-06-04; restrict management-plane access to known admin IPs.

**Sources:** [BleepingComputer — Cisco Unified CM PoC](https://www.bleepingcomputer.com/news/security/cisco-warns-of-critical-unified-cm-flaw-with-poc-exploit-code/) | The Hacker News

---

### Polyfill.io Domain Takeover Round 2 — Toshiba / Muji / Samsung / Multiple Japanese Brands Serving Fake Login Prompts Across Long-Tail Legacy References
**Product:** Web pages with legacy `polyfill[.]io` script tags; brands include Toshiba, Muji, Zojirushi, FiNC Technologies, Ishiyaku Publishers, Hobonichi, Samsung Smart TVs | **CVE:** None assigned | **First reported:** 2026-06-05

Following the 2024 polyfill.io supply-chain compromise (Chinese-entity injection on 100K+ sites), the domain has changed hands again — the most recent owner is responding with HTTP 401 challenges that surface browser-native authentication prompts on every legacy-referencing page. Major brands including Toshiba, Muji, and Samsung have advised users to ignore the prompts and rotate credentials. No confirmed harvested-credential exfiltration, but the prompts are credible enough to be a working credential-phishing primitive against any visitor who types into them.

**Mitigation:** Audit organisational webroots and CDN-hosted brand pages for any reference to `polyfill[.]io`, `polyfill[.]com`, or `cdn.polyfill[.]io`; replace with `polyfill.top` (the original maintainer's legitimate relaunch) or self-host the polyfill bundle; if your CSP allow-lists `*.polyfill.io` remove that entry now; communicate to brand-protection teams that a Polyfill.io reference on any owned property is a credential-phishing exposure as of 2026-06-05.

**Sources:** [BleepingComputer — Polyfill prompts on Toshiba/Muji](https://www.bleepingcomputer.com/news/security/suspicious-polyfill-login-prompts-pop-up-on-toshiba-muji-websites/)

---

### UNC5221 / VerdantBamboo "Brickstorm" — 18-Month Edge-Device Persistence Campaign, Plenet + AgentPSD Fallback Implants, MSP Lateral Movement
**Product:** Edge devices and storage-sync (Egnyte); Microsoft 365 environments; victim sectors: legal services, SaaS providers, BPOs, technology firms (primarily US) | **CVE:** None assigned | **First reported:** 2026-06-05

BleepingComputer / Volexity disclosed a UNC5221 (a.k.a. VerdantBamboo) campaign in which the Brickstorm Golang/Rust implant maintained persistence on edge devices for **18+ months undetected** (initial access circa Q1 2025). Secondary implants include Plenet (.NET shell-and-file backdoor) and AgentPSD (Python reverse-shell fallback). TTPs: edge-device + Egnyte zero-day exploitation, stolen-credential SSL-VPN access, MSP-infrastructure lateral movement, targeting hosts without EDR. The campaign infrastructure went dark mid-September 2025, then reactivated under new tooling earlier in 2026.

**Mitigation:** Audit edge devices (firewalls, VPN concentrators, file-sync gateways) for unexpected WebSocket persistence callbacks and Golang/Rust unsigned binaries; deploy EDR to MSP-managed hosts (Volexity assessment: lack of EDR was the single highest-correlation factor for victim retention); hunt M365 audit logs for stolen-credential SSL-VPN logins from MSP IP ranges; pull IoCs from [Volexity threat-intel repo](https://github.com/volexity/threat-intel) for 2026-06-04 VerdantBamboo release.

**Sources:** [BleepingComputer — UNC5221 Brickstorm](https://www.bleepingcomputer.com/news/security/chinese-apt-deploys-new-malware-to-keep-access-to-hacked-networks/) | Volexity threat intel

---

### PCPJack — 230 AWS / GCP / Azure Servers Hijacked into Covert SMTP Relay Network for Spam/Phishing Email Delivery
**Product:** Compromised public-cloud-tenant SMTP-capable servers across AWS, Google Cloud, Microsoft Azure (US, Europe, Asia) | **CVE:** None assigned | **First reported:** 2026-06-05

Hunt.io documented the **PCPJack** operation (initially flagged by SentinelOne in April 2026 as a cloud-credential-theft framework): ~230 cloud-tenant servers compromised across the three major hyperscalers and converted into authenticated SMTP relays, then verified for mail-delivery capability and synced to a downstream consumer every 5 minutes. Researchers identified the C2 at 213.136.80[.]73 through unprotected open directories exposing source code, compiled binaries, and live operator configs.

**Mitigation:** Audit cloud-tenant outbound SMTP usage — any tenant sending email from previously-non-mail-server hosts is suspicious; monitor for repeated 5-minute outbound HTTPS posts to non-cloud-resident endpoints (the operator's sync interval); block egress to 213.136.80[.]73 and pull Hunt.io IoCs for related infrastructure; rotate credentials for any cloud-tenant principal active in the PCPJack timeframe (April-June 2026).

**Sources:** [The Hacker News — PCPJack cloud hijack](https://thehackernews.com) | Hunt.io

---

### CPython CVE-2026-7774 — tarfile.data_filter Path-Traversal Bypass Allowing Write Outside Extraction Directory
**Product:** CPython tarfile module, multiple Python versions (full version matrix pending vendor advisory) | **CVE:** CVE-2026-7774 | **CVSS:** pending | **Published:** 2026-06-04

Oss-security 2026-06-04: A bypass in CPython's `tarfile.data_filter` (the default-since-3.12 sandboxing filter for tar extraction) allows path traversal yielding writes outside the intended extraction directory. Broad blast radius — `tarfile` is a default-import primitive used by package managers, model-weights loaders, CI artifact extractors, container runtimes, and (notably) AI/ML model-distribution pipelines. Pre-3.12 environments using the new filter as a backport are also affected.

**Mitigation:** Upgrade to vendor-released patched CPython point releases as soon as they ship (3.11.x, 3.12.x, 3.13.x patches expected within 7 days); until then, audit any extraction pipeline that processes externally-supplied tar archives (model-weights loaders, plugin/extension installers, CI build artifacts) and apply explicit pre-extraction tar-member-name validation; treat archives sourced from public package mirrors / model hubs as untrusted.

**Sources:** [openwall oss-security 2026-06-04](https://openwall.com/lists/oss-security/2026/06/) | CPython advisory

---

## 🔄 Updates to Previously Reported

### TA4922 / Atlas RAT — Expanded Tooling, RomulusLoader + SilentRunLoader Added to Campaign (Previous Score 4 → 4, Material Tooling Change)
**Product:** Same as 2026-06-04 entry — Windows endpoints in DE/IT/UK/SA targeted with localized lures | **CVE:** None | **CVSS:** N/A | **Previous threat score:** 4 → **Current:** 4

THN reporting 2026-06-05 expands the TA4922 (Silver Fox / Void Arachne overlap) campaign first reported in Watchtower 2026-06-04. Two new loader families surfaced — **RomulusLoader** and **SilentRunLoader** — running alongside the existing Atlas RAT family, plus continued use of ValleyRAT. Target-geography list now confirmed as UK, Germany, Italy, and South Africa. Threat score holds at 4 (cybercrime, not destructive APT) but defenders should treat IOC sets from 2026-06-04 as incomplete — Proofpoint additions expected within a week.

**Mitigation:** Re-ingest IoCs from THN 2026-06-05 piece into EDR/SIEM, supplement with Proofpoint's expected TA4922 IoC release; existing 2026-06-04 mitigations (localized payroll/tax/VAT lure detection, Application Guard bypass hunting) remain valid.

**Sources:** [The Hacker News — TA4922 expansion](https://thehackernews.com)

---

## 📋 Noted / Monitoring

**Chrome 149 — 429 vulns including CVE-2026-10881 ANGLE OOB write (CVSS 9.6, $97K bounty) sandbox escape, CVE-2026-10882 Network UAF, CVE-2026-10883 ANGLE OOB write; CVE-2026-11282 sandbox-escape on Linux** — Browser client OOS for direct corporate defense, but Linux sandbox bypass relevant to dev workstations; no in-wild exploitation flagged.

**Hola Browser Windows supply-chain compromise — Monero miner injected as me.exe → HolaMonitorService.exe, persisted via hola_monitor_svc Windows service** — Israeli VPN/proxy browser distribution channel compromised; ~0.1% userbase impact per vendor; Defender exclusion added by payload (durable IOC); calibration data point for "non-mainstream browser vendor supply-chain compromise" class.

**Mirasvit Magento Full Page Cache Warmer — Unauthenticated PHP-object-deserialization RCE on Magento/Adobe Commerce servers, no CVE assigned yet** — SecurityWeek 2026-06-04; e-commerce-only blast radius but high-value targets; vendor patch ETA pending.

**Stripe-as-payload-host Magecart campaign (Sansec)** — Skimmer JS hosted in Stripe customer-metadata field at `cus_TfFjAAZQNOYENR`, loaded via Google Tag Manager containers, exfil via Stripe API trusted-domain bypass of CSP; Firestore variant uses `braintree-payment-app` project; e-commerce-skimmer class but **durable pattern: payment-processor APIs as CSP-trusted-domain skimmer hosts**.

**OP-512 — Fourth China-aligned IIS-targeting cluster in 12 months (ReliaQuest)** — Custom IIS web shell framework; similar targeting profile to CL-STA-0048 / DragonRank / GhostRedirector; calibration data point for sustained Chinese IIS-web-shell campaign tempo.

**SolarWinds Serv-U CVE-2026-28318 KEV-add (covered above in MEDIUM)** — Federal deadline 2026-06-19.

**CISA KEV addition — Android CVE-2025-48595 + Linux CVE-2022-0492** — Joint KEV announcement 2026-06-04/05; the Linux CVE-2022-0492 entry is already covered in Watchtower 2026-06-04 HIGH; Android CVE-2025-48595 was covered in 2026-06-03 and 2026-06-04 Noted (mobile OOS for our scope; KEV-add does not change defensive posture).

**ATG Joint Advisory — Shadowserver scan confirms 909 US ATG systems exposed on port 10001/tcp (BC 2026-06-05)** — Day-two amplification of Watchtower 2026-06-04 CRITICAL coverage; no new vendor or CVE info, scope-confirmation only.

**Brave Origin (paid bloat-free browser launch)** — 2026-06-04; not a security advisory; calibration data point for "browser-of-choice for security-conscious users" market shift.

**DentaQuest data breach — 2.6M accounts exposed (BC 2026-06-04)** — Dental benefits administrator; third-party-risk and notification calibration; no CVE.

**UN World Food Programme — Palestine self-registration application breach exposing 600K Gaza households (BC 2026-06-04)** — Humanitarian-targeting calibration; supply-chain implications for any third-party using the same registration platform.

**Apache Fory CVE-2026-50076 — Java ReplaceResolverSerializer deserialization checks bypass (oss-security 2026-06-04, Chaokun Yang)** — Apache serialization-engine class; deserialization-RCE primitive; watch for downstream adoption pickup over the next 30 days.

**Vim < 9.2.597 — Arbitrary Code Execution via Python Omni-Completion (oss-security 2026-06-04, Christian Brabandt)** — Follow-up to similar Vim 9.2.561 issue (Watchtower 2026-05-30 noted); client-side / dev-workstation OOS but worth flagging to dev-fleet patch cadence.

**CPython CVE-2026-7774 tarfile.data_filter (covered above in MEDIUM)** — Cross-listed for source-traceability.

**Net::Async::Statsd / Net::Statsd / Etsy::StatsD Perl — Multi-CVE metric-injection batch (oss-security 2026-06-04, Robert Rothenberg)** — CVE-2026-8722, 46739, 46741; metric-injection primitive against downstream Statsd-consuming dashboards; legacy Perl scope, low blast radius but check internal Statsd pipelines.

**HTML::Entities CVE-2026-8829 — Use-of-freed-memory in _decode_entities (Paul Johnson)** — Pre-3.84 Perl; legacy-Perl client-side; low priority.

**Net::CIDR::Set CVE-2026-49940/49941/49942 — IP/netmask validation issues** — Same Perl batch; low priority calibration.

**FortiGuard — FIFA World Cup 2026 fraud wave, 4,300+ fraudulent domains, GHOST STADIUM operation distributing banking malware** — 2026-06-04; brand-impersonation / awareness-campaign data point; pre-position phishing-domain takedown SLAs for World Cup window.

**SafeBreach Gemini-voice-via-notification hijack (covered in Watchtower 2026-06-04 noted as "Invitation Is All You Need")** — SecurityWeek 2026-06-04 follow-up; already patched server-side by Google 2025-11; no change.

**Securly Chrome Extension multi-issue batch — CVE-2026-8889 (SHA-1 weak hash), CVE-2026-8881 (MD5 weak KDF), plus VU#595768 (Watchtower 2026-06-04)** — Education-segment Chrome deployments; browser-extension scope OOS for most enterprises.

**D-Link DWR-M920 CVE-2026-10878 (PT-2026-46838, CVSS 8.8)** — SOHO router; Mirai-variant tracking; OOS for corporate perimeter.

**Havelsan Geographic Tracking System CVE-2026-6207 + CVE-2026-6209 (CVSS 9.1)** — Turkish military/civilian GIS platform; OT/specialized-system scope; OOS for typical corporate defense but flagged for sector relevance.

**Markdown Preview Enhanced CVE-2026-49492 (CVSS 8.8) — Command injection on Windows via unvalidated external-file open from markdown documents** — Dev-workstation client-side; relevant to dev-fleet patch cadence.

**Asin Android spyware — Arabic-targeting via govlens[.]net, pdf-reader[.]help, live-war-map[.]com (THN 2026-06-05)** — Mobile-only OOS; sector-targeting calibration.

**Krebs — "AI Worm" prototype (Schneier 2026-06-05)** — Research prototype carrying an LLM payload and executing it on compromised hosts; LLM-augmented-malware-class calibration (joins MEMORY 2026-06-02 LLM-driven post-exploitation tempo class).

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/KEV | ❌ (403 — KEV inferred via BC/SW/THN relay) |
| Vendor advisories | msrc.microsoft.com/blog, securitylab.github.com, blog.cloudflare.com/security, fortinet.com/blog/threat-research, openwall.com/lists/oss-security (supplemental), djangoproject.com (supplemental) | ✅ / ⚠️ |
| Research / OSINT | schneier.com, krebsonsecurity.com, rapid7.com, securityweek.com, dbugs.ptsecurity.com, kb.cert.org/vuls, avleonov.com, googleprojectzero.blogspot.com | ✅ / ⚠️ |
| CVE registries | opencve.io, nvd.nist.gov, cve.org, cve.mitre.org, attackerkb.com, github.com/0xMarcio/cve, github.com/search?q=CVE | ✅ / ❌ |
| Full disclosure | seclists.org/fulldisclosure, packetstormsecurity.com | ⚠️ |
| Bounty / hacktivity | hackerone.com/hacktivity, bugcrowd.com/disclosures | ❌ / ⚠️ |
| Region-specific | habr.com/ru/companies/tomhunter, teletype.in/@cyberok, cert.gov.ua | ⚠️ |

**Errors:** cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403), attackerkb.com (403), bugcrowd.com/disclosures (404), cve.mitre.org (no usable content). Degraded: seclists.org/fulldisclosure (302 redirect, June archive unreachable), packetstormsecurity.com (301 to packetstorm.news, homepage stats only), nvd.nist.gov (homepage only), cve.org (no usable content), msrc.microsoft.com/blog (redirect chain), hackerone.com/hacktivity (no feed content), habr.com/ru/companies/tomhunter (no June content), teletype.in/@cyberok (no June content), cert.gov.ua (no usable content), rapid7.com (no June 2026 posts visible), googleprojectzero.blogspot.com (latest is May 2026 Pixel 10 0-click).

**CISA KEV:** SolarWinds Serv-U CVE-2026-28318 (federal deadline 2026-06-19) confirmed via BC relay. Android CVE-2025-48595 + Linux CVE-2022-0492 KEV-add covered in Watchtower 2026-06-04 already (no material change).

---

*Watchtower vulnerability-researcher | Cycle: 2026-06-06/night | Next: 2026-06-07/night*
