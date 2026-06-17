# Watchtower Night Report — 2026-06-17
**Cycle:** Night | **Generated:** 2026-06-17 23:30 UTC (2026-06-17T23:30:00Z)
**Sources checked:** 20/30 | **CISA KEV total:** Unreachable from session (cisa.gov 403); KEV deltas tracked via vendor + BC/SW/THN amplification | **New KEV additions:** ≥1 confirmed (CVE-2026-54420 LiteSpeed cPanel — see Update below)

---

## 🔴 CRITICAL

*No CRITICAL items today. Three Update items in HIGH carry near-critical defensive urgency.*

---

## 🟠 HIGH

### 🔄 UPDATE — Arch Linux AUR 'Atomic Arch' Mass-Compromise Scope Expansion 400 → 1,500+ Packages; AUR Registrations Suspended 2026-06-16
**Product:** Arch Linux Arch User Repository (AUR) — abandoned packages hijacked + entirely new malicious packages | **CVE:** None assigned | **Previous score:** 8 | **New score:** 8 | **First reported:** 2026-06-13

Watchtower covered this campaign 2026-06-13 as a 400+ package compromise pushing a Rust credential-stealer and eBPF rootkit via the `atomic-lockfile` NPM stage. SecurityWeek + BleepingComputer 2026-06-16 confirm the campaign has expanded materially: **1,500+ malicious AUR packages** identified, attackers have **expanded distribution to Bun-based installation paths** in addition to NPM, and **Arch Linux has suspended new account registrations** while cleanup is in progress. Sonatype + StepSecurity reiterate that any host that ran an `atomic-lockfile`-tainted install must be treated as fully untrusted — rebuild from clean media, rotate every SSH key, every browser session cookie, every Vault token, and every credential the affected user had ambient access to. The eBPF-based hiding primitives mean conventional endpoint scans will not enumerate the implant; rebuild is the only safe remediation. The campaign continues to show the same TTPs Watchtower has tracked across the broader 2026 Shai-Hulud / Miasma / IronWorm developer-supply-chain cluster, but the AUR variant is distinct in its eBPF kernel-rootkit payload and its package-ecosystem (Arch first, NPM and now Bun secondary) targeting.

**Timeline:**
- 2026-06-07/08 — Initial AUR uploads observed (per StepSecurity backtrace).
- 2026-06-11 — Scope reaches 400+ packages; Watchtower 2026-06-13 News at score 8.
- 2026-06-12 — Attackers expand to Bun installation paths.
- 2026-06-16 — Arch Linux suspends new AUR account registrations; scope ≥ 1,500 packages confirmed (SW 2026-06-16, BC 2026-06-16).

**Why it matters:** Every developer workstation that touched a tainted package between 2026-06-07 and 2026-06-16 is a credential-disclosure incident, and the eBPF rootkit means that workstation is not a remediable endpoint — it is a quarantine candidate. For our environment: identify every host that ran `pacman -U`, `yay`, `paru`, or `pikaur` in that window, especially developer + SRE workstations, and treat them as compromised until rebuilt from clean media. Rotate SSH keys, browser tokens, Vault tokens, cloud session cookies.

**Mitigation:**
- Inventory every Arch-based host (workstation, container base image, CI runner) that ran AUR installs since 2026-06-07.
- Pull the public IOC list from Sonatype + StepSecurity; hunt for the documented C2 domains, the `atomic-lockfile` package, and the eBPF artefacts (`bpftool prog list` may not show hidden programs — use kernel-side audit / verified-boot integrity check instead).
- Treat any host with positive hits as fully compromised — rebuild, do not "clean."
- Rotate every credential, key, and cookie ambient to the affected user account.
- Block known C2 hostnames at egress; alert on outbound to the documented exfil endpoints.
- Until AUR re-opens with vetting in place, freeze `yay` / `paru` / `pikaur` on managed Arch hosts; allow only the pacman repos.

**Sources:** [SecurityWeek 2026-06-16 — Atomic Arch Supply Chain Attack Hits 1,500 AUR Packages](https://www.securityweek.com) | [BleepingComputer 2026-06-16 — Arch Linux 400+ → 1500 expansion](https://www.bleepingcomputer.com)

---

### 🔄 UPDATE — LiteSpeed cPanel CVE-2026-54420 Added to CISA KEV With 3-Day BOD 26-04 Federal Deadline; Active Exploitation Re-Confirmed
**Product:** LiteSpeed cPanel user-end plugin (cPanel/WHM hosting platforms) | **CVE:** CVE-2026-54420 | **Previous score:** 7 | **New score:** 8 | **First reported:** 2026-06-15

Watchtower covered CVE-2026-54420 (symlink-following privilege escalation to root) as News on 2026-06-15 at score 7. **CISA added the CVE to the KEV catalog this cycle and invoked the BOD 26-04 three-day federal-agency remediation timer** (BleepingComputer 2026-06-16). This is the second invocation of the new BOD 26-04 three-day window — the first was for Ivanti Sentry CVE-2026-10520 on 2026-06-11 (Watchtower 2026-06-11 News at score 9, 2026-06-13 KEV-promotion Update). The use of the three-day timer rather than the conventional 21-day timer is itself the signal: CISA reserves it for vulnerabilities where they assess that compensating controls are weak and exploitation is straightforward.

**Timeline:**
- 2026-06-09 — LiteSpeed ships patch in plugin v1.x.
- 2026-06-15 — Public technical disclosure; Watchtower News at score 7.
- 2026-06-16 — CISA KEV addition + BOD 26-04 three-day federal deadline; BleepingComputer amplification.

**Why it matters:** cPanel hosts a large fraction of shared-web-hosting infrastructure. Any LiteSpeed-enabled cPanel host where the user-end plugin is installed grants root from any FTP/web-shell foothold — and FTP/web-shell footholds on shared hosting are the default-existence assumption, not an edge case. For our environment: any cPanel/WHM instance under our control or under contract with a managed-hosting provider needs to be confirmed patched within the federal deadline window (effectively by 2026-06-19), regardless of whether we are subject to BOD 26-04.

**Mitigation:**
- Inventory every cPanel/WHM instance under our control or in our supply chain (managed hosting providers, agency partners).
- Confirm LiteSpeed cPanel plugin patched to the 2026-06-09 fix-version or later.
- Where the LiteSpeed plugin is not in use, uninstall it entirely.
- Treat the three-day federal deadline (2026-06-19) as the de-facto industry deadline.
- Hunt for symlink-creation events from FTP and web-shell user accounts to filesystem paths the plugin processes.

**Sources:** [BleepingComputer 2026-06-16 — CISA warns of another cPanel plugin flaw exploited in attacks](https://www.bleepingcomputer.com) | [TheHackerNews 2026-06-16](https://thehackernews.com)

---

### 🔄 UPDATE — Fortinet FortiSandbox CVE-2026-25089 + Sibling CVE-2026-39813 + CVE-2026-39808 Confirmed Actively Exploited By Defused Threat Intel (Was PoC-Only)
**Product:** Fortinet FortiSandbox advanced threat-detection appliance | **CVE:** CVE-2026-25089, CVE-2026-39813, CVE-2026-39808 | **Previous score:** 7 | **New score:** 8 | **First reported:** 2026-06-11

Watchtower covered CVE-2026-25089 (pre-auth OS command injection via 'Start...' parameter, CVSS 9.1) as News on 2026-06-11. **Defused threat intel confirmed active in-the-wild exploitation of all three FortiSandbox CVEs within the 24 hours before 2026-06-16** (BleepingComputer 2026-06-16, TheHackerNews 2026-06-16). The sibling CVEs CVE-2026-39813 and CVE-2026-39808 are also in active exploitation — patches landed 2026-04-14, so the exploitation window is two months wide and any unpatched FortiSandbox is now a viable C2 / pivot foothold. All three flaws are low-complexity command-injection-class issues requiring no user interaction.

**Timeline:**
- 2026-04-14 — Fortinet ships patches for CVE-2026-39813 / 39808 / 25089.
- 2026-06-09 — CVE-2026-25089 disclosure picked up; Watchtower News 2026-06-11 at score 7.
- 2026-06-15/16 — Defused observes ITW exploitation of all three CVEs; BleepingComputer + THN report 2026-06-16.

**Why it matters:** FortiSandbox is an inline / passive-tap detonation appliance that processes attacker-controlled artefacts by design — it sits behind organisations' email + perimeter feeds and ingests malicious files as a feature. A pre-auth RCE on the analysis appliance is functionally a pre-auth RCE on the inspection plane, which makes it both a blind spot (detected malware → owned detector) and a high-value pivot. For our environment: every FortiSandbox in our fleet must be on the 2026-04-14 fix-train; assume any appliance not patched by mid-April is potentially compromised and warrants a forensic image + rebuild rather than an in-place patch.

**Mitigation:**
- Inventory every FortiSandbox (appliance + VM-form-factor) in the fleet.
- Verify firmware is on or above the 2026-04-14 fix-train across all three CVEs (confirm against Fortinet PSIRT advisory; do not rely on a single CVE patch).
- For any unit not patched by mid-April: forensic-image, rebuild from vendor-signed image, rotate any inline credentials.
- Net-isolate the FortiSandbox management interface from the internet; only the inline / span-port path should reach detonation traffic.
- Add alerts for unexpected outbound from the FortiSandbox management VLAN.

**Sources:** [BleepingComputer 2026-06-16 — Critical Fortinet FortiSandbox flaws now exploited in attacks](https://www.bleepingcomputer.com) | [TheHackerNews 2026-06-16](https://thehackernews.com)

---

## 🟡 MEDIUM

### 📰 NEWS — JetBrains Marketplace — 15+ Malicious Plugins Designed to Steal AI API Keys From Developer IDEs
**Product:** JetBrains plugin marketplace (IntelliJ IDEA / PyCharm / WebStorm / Rider / GoLand and other JetBrains IDEs) | **CVE:** None assigned | **First seen:** 2026-06-16

BleepingComputer 2026-06-16 (Lawrence Abrams) reports the discovery of **at least 15 malicious plugins published to the JetBrains Marketplace whose purpose was to extract AI API keys** (Anthropic, OpenAI, Google, and other vendor-issued credentials) from developer environments. The plugins were packaged to imitate legitimate productivity / AI-assistant integrations. The exfiltrated keys grant attackers paid-tier model access — directly monetisable through onward resale or proxy-as-a-service abuse — and, more concerningly, in many organisations the same API keys are granted access to internal proprietary data pipelines via embeddings / RAG endpoints, which converts a key compromise into a data-exfiltration foothold. This is the second 2026 AI-credential-theft cluster against developer-IDE marketplace surfaces after the Mini Shai-Hulud / IronWorm VS Code + Claude Code config-persistence campaign (Watchtower 2026-05-21 / 2026-06-06). The pattern of marketplace plugins as a covert AI-key-collection channel deserves separate tracking from the broader supply-chain-worm cluster.

**Mitigation:**
- Audit every JetBrains plugin installed across developer workstations; cross-check against the IOC list once JetBrains publishes one.
- Default to "trusted publishers only" plugin installation policy on managed IDE installations.
- Rotate every Anthropic / OpenAI / Google / Cohere / Mistral API key that has been resident in a JetBrains workstation environment since 2026-05-01.
- Where API-key-based access can be replaced with workload-identity-based access (e.g. AWS Bedrock IAM role, GCP service account), do so — credential-theft scope shrinks.
- Add anomaly alerts on AI provider billing dashboards (unusual model variants, unusual completion volumes, unusual geolocation of API calls).

**Sources:** [BleepingComputer 2026-06-16 — Malicious JetBrains Marketplace plugins steal AI API keys from developers](https://www.bleepingcomputer.com)

---

### 📰 NEWS — Cacti ≤ 1.2.30 CVE-2026-39949 Authenticated RCE via Host-Notes Variable Injection Into RRDtool Arguments; PoC Public on GitHub
**Product:** Cacti network-monitoring platform ≤ 1.2.30 | **CVE:** CVE-2026-39949 | **First seen:** 2026-06-17

A new public PoC repository surfaced on GitHub (`lukehebe/CVE-2026-39949`, updated within the last 3 hours of report time) for **Cacti ≤ 1.2.30**: user-controlled host-metadata fields (specifically the **device notes** field) are substituted unsanitised into RRDtool command-line arguments via Cacti's variable replacement engine. An authenticated user with device + graph-template creation privileges injects shell metacharacters into the device-notes field, creates a graph template that references `|host_notes|`, and triggers graph rendering — the rendering pipeline executes the injected metacharacters as the web-server user (typically `www-data` / `apache`). PoC supports direct command execution (`--cmd 'id'`) and out-of-band exfiltration (`--oob your.oastify.com`). Authentication is required, which lowers the immediate ceiling, but Cacti instances commonly have default-admin / weak-admin credentials in mid-tier enterprise deployments, and credential-stuffing against Cacti is a known mass-exploitation route (see 2024 Cacti history). Vendor patch status: not yet confirmed at report time — track Cacti GitHub for a fix.

**Mitigation:**
- Confirm Cacti version across the fleet; treat ≤ 1.2.30 as vulnerable until a fix-version is published.
- Audit Cacti accounts: rotate any admin credentials that match leaked-credential lists; remove unused accounts.
- Restrict Cacti web access to a management VLAN; do not internet-expose.
- Hunt RRDtool command-line invocations for shell metacharacters in argument positions that should be filenames or values.
- Monitor outbound from the Cacti host to attacker-controlled out-of-band domains.

**Sources:** [GitHub lukehebe/CVE-2026-39949 PoC 2026-06-17](https://github.com/lukehebe/CVE-2026-39949)

---

### 📰 NEWS — Altium Enterprise Server CVE-2026-11414 (CVSS 9.8) Hard-Coded Key + CVE-2026-11420 (CVSS 9.8) Pre-Auth Path Traversal + CVE-2026-11419 (CVSS 8.8) Authenticated Path Traversal
**Product:** Altium Enterprise Server (PCB / electronics design enterprise vault platform) | **CVE:** CVE-2026-11414, CVE-2026-11420, CVE-2026-11419 | **CVSS:** 9.8 / 9.8 / 8.8 | **First seen:** 2026-06-16

NVD published a three-CVE batch against **Altium Enterprise Server** 2026-06-16: (1) **CVE-2026-11414 (CVSS 9.8)** — the Vault service signs file-download URLs with a **hard-coded cryptographic key**, so any party in possession of the binary can mint download URLs for arbitrary files served by the Vault. (2) **CVE-2026-11420 (CVSS 9.8)** — path traversal in the Network Installation Service permits an unauthenticated attacker to **write arbitrary files** and **read package archives**, which is the typical setup for an installer-replacement-class compromise. (3) **CVE-2026-11419 (CVSS 8.8)** — path traversal in the UploadController via inadequate validation of user-controlled path components in image uploads. Altium Enterprise Server is the central PCB / electronics-design vault used by manufacturers — compromise yields source IP for PCB designs and access to the build/install distribution path for downstream developer workstations. Vendor patch status: published with the advisory; verify the patched build line via Altium's PSIRT page.

**Mitigation:**
- Inventory Altium Enterprise Server deployments — they are typically restricted to engineering teams but are sometimes routable from broader corporate networks.
- Patch to the 2026-06-16 vendor advisory build line.
- Until patched, restrict Vault + Network Installation Service ports to a single jump-host VLAN.
- Audit file-download URL traffic for anomalous mint patterns (the hard-coded key means anyone can mint URLs; logs may show requests for files no human user requested).
- Inventory downstream engineering workstations that pull installer packages from the Altium Network Installation Service — verify package integrity against an out-of-band hash.

**Sources:** [NVD CVE-2026-11414 / CVE-2026-11420 / CVE-2026-11419 — 2026-06-16](https://nvd.nist.gov)

---

### 📰 NEWS — UNK_Deadrop North-Korea-Aligned Developer-Targeted Supply Chain — ~100 Orgs Hit via Fake GitHub Recruitment + Cross-Platform 'Overlord' Loader (macOS/Linux/Windows)
**Product:** Developer-laptop attack surface; cross-platform malware framework (macOS + Linux + Windows) | **CVE:** None assigned | **First seen:** 2026-06-16

TheHackerNews 2026-06-16 reports a North-Korea-aligned cluster — tracked as **UNK_Deadrop** — running a developer-targeted social-engineering supply-chain campaign that has compromised an estimated **~100 organisations to date**. Initial access lure: **fake GitHub recruitment messages** ("we'd like you to review this take-home project / code-review challenge") that route the candidate to a project repository whose build path drops a cross-platform **'Overlord' framework loader** with macOS, Linux, and Windows payloads. The lure family closely matches the prior 2024–2025 Lazarus 'Contagious Interview' cluster but the Overlord framework is a new C2 + loader codebase rather than a reuse of the older BeaverTail / InvisibleFerret stack. Notable: the macOS variant is among the first DPRK loaders to ship native arm64 macOS persistence, indicating substantial dev resources behind the campaign. For our environment: anyone in a recruiting-adjacent or engineering role who has been approached by an unsolicited GitHub recruiter in the last 60 days needs to be reviewed; this is the highest-yield delivery vector currently active against software-engineering targets.

**Mitigation:**
- Brief recruiting, engineering, and management on the fake-GitHub-recruitment lure; treat unsolicited take-home challenges as a credible attack until validated.
- Engineering staff must run unknown projects only in disposable VMs / sandboxes, never on their daily workstation.
- Deploy macOS arm64 + Linux endpoint telemetry capable of catching the Overlord framework IOC set once published.
- Network-isolate engineering laptops from internal credential stores (Vault, AWS SSO, GitHub PATs) by default; require step-up auth for write operations.
- Roll out FIDO2 or WebAuthn-bound credentials for GitHub and the cloud control plane so a stolen developer session is not directly upgradable to a privileged token.

**Sources:** [TheHackerNews 2026-06-16 — UNK_Deadrop / Overlord developer recruitment supply chain](https://thehackernews.com)

---

### 📰 NEWS — DragonForce Ransomware Deploys 'Backdoor.Turn' That Hides C2 Traffic Inside Microsoft Teams Relay Infrastructure
**Product:** Microsoft Teams (as carrier / relay channel — not a vulnerability in Teams itself) | **CVE:** None assigned | **First seen:** 2026-06-16

BleepingComputer 2026-06-16 (Bill Toulas) reports that the **DragonForce ransomware affiliate program** has deployed a new custom backdoor — **'Backdoor.Turn'** — that **conceals its command-and-control communications within Microsoft Teams relay infrastructure**, encoding C2 traffic so that it traverses the Teams media-relay control plane and is indistinguishable from legitimate Teams telemetry to perimeter inspection. The technique is not a Teams vulnerability but a TTP — DragonForce is abusing legitimate Microsoft tenant infrastructure as a covert channel, in the same family as the prior Slack-as-C2 and Discord-as-C2 abuse patterns but materially more difficult to filter because Teams traffic is universally allowed out of corporate networks and uses TLS-pinned endpoints that conventional decryption breaks. For our environment: this is a detection-engineering problem, not a patching problem. Add behavioural detection on the Teams media-relay flow shape (volume + cadence + destination distribution) against per-user baselines, and treat Teams as an exfil-channel surface that needs visibility, not perimeter-trust.

**Mitigation:**
- Onboard Teams traffic flow shape (per-user / per-tenant) into the SIEM with baseline + drift detection.
- Hunt for hosts that initiate outbound to Teams media-relay endpoints from unusual processes (anything that is not Teams.exe / the official mobile / web clients).
- Add an IOC list once Microsoft + the reporting vendor publish detection signatures.
- Restrict DLP egress filtering scope to include Teams chat + file attachment, not just email + cloud storage.
- For high-sensitivity orgs, consider Teams-tenant-isolation or external-tenant-block policies.

**Sources:** [BleepingComputer 2026-06-16 — Ransomware gang abuses Microsoft Teams relays to hide malicious traffic](https://www.bleepingcomputer.com)

---

## 📋 Noted / Monitoring

**Google Vertex AI Python SDK — bucket-squatting** — pre-existing GCS bucket squatting vulnerability lets attackers hijack ML-model uploads (THN 2026-06-16). Fixed in v1.148.0+; no in-wild exploitation observed. Continues the 2026 AI-platform-supply-chain cluster.

**Apache Airflow SFTP Provider CVE-2026-50203** — path traversal in `SFTPHook.retrieve_directory` allows local file write outside the intended directory; oss-security 2026-06-16. Airflow appears in Watchtower regularly — fits the 06-01 16-CVE batch pattern.

**OpenStack Ironic CVE-2026-43003 + companion CVE-2026-54421 (already 2026-06-15 Noted)** — IPA command injection; oss-security 2026-06-16, Jay Faulkner. Bare-metal-provisioning operators only.

**OpenStack Nova OSSA-2026-022** — scheduler-hint injection bypasses Placement resource claims + scheduling constraints (oss-security 2026-06-16). Multi-tenant OpenStack operators only.

**Pacemaker CVE-2026-10649** — DoS via integer overflow in remote message decompression (oss-security 2026-06-16). HA-cluster operators only.

**CPython CVE-2026-12003** — development search paths can be activated without modifying the installation directory (oss-security 2026-06-16). Local / dev-environment scope.

**OpenBSD sppp PAP authentication bypass** — bypass in `sppp_pap_input` (oss-security 2026-06-16). Narrow OpenBSD PPP-link scope.

**Vim < 9.2.x patches** — out-of-bounds write in spell-file processing + code injection via crafted filenames (oss-security 2026-06-16). Continues Vim 2026 cadence.

**gsasl 2.2.4 release** — fixes a heap-disclosure vulnerability (oss-security 2026-06-16). Library affecting SASL implementations.

**CVE-2026-30121 Remotion v4.0.409** — arbitrary file write (CVSS 9.1, opencve.io 2026-06-16). Niche React-video-framework scope.

**Wertheim SafeController for VAULT ROOMS — SEC Consult SA-20260615-0 / -1** — multiple critical vulnerabilities in vault-room safe-deposit locker hardware + software (Full Disclosure 2026-06-15). Physical-security-tech vertical; very narrow scope but a defensive-engineering signal.

**iRhythm digital-health-co ransomware data theft** — confirmed data stolen; ransomware demand made (SecurityWeek 2026-06-16). No CVE / technical detail published. Healthcare sector incident.

**Mackay Sugar (Australia's #2 sugar producer) ransomware — The Gentlemen group** — operational shutdown, no CVE published (SecurityWeek 2026-06-16). Continues Krebs 2026-06-10 'Who runs The Gentlemen' coverage.

**Novo Nordisk — FulcrumSec claims 1.3TB pharmaceutical data theft** (SecurityWeek 2026-06-16). Continues 2026-06-12 Noted (clinical-trial data breach).

**Council of Europe — ShinyHunters extortion claim continues** (BleepingComputer 2026-06-16). Continues 2026-06-15 Noted; investigation ongoing.

**Cal Water California Water Service — Iranian Handala claim** (SecurityWeek 2026-06-16) — operational systems unaffected per Cal Water statement; continues 2026-06-13 Noted.

**NarwhalRAT / ScarCruft (APT37)** — fake-Microsoft-security-alert phishing via LNK-in-ZIP, targets MS-account holders (THN 2026-06-16). Client-side scope but worth tracking for MS-account credential-theft volume.

**SprySOCKS Backdoor — Windows variants** — previously Linux-only China-linked malware now ships Windows kernel-driver variants supporting 30+ commands (THN 2026-06-16). Pattern indicator.

**ClickFix loader expansion — BabaDeda + Lorem Ipsum + Potemkin** — three new ClickFix loader families targeting education + finance via fake-update lures (THN 2026-06-16). Continues 2026 ClickFix tradecraft cluster.

**Rokarolla Android banking trojan** — 217 banking + crypto apps, 137 remote commands, spreads via fake TikTok + Chrome lookalike sites (BC + THN 2026-06-16). Mobile-only — out of Watchtower core scope.

**JetBrains Marketplace IOC list pending** — once JetBrains publishes the full malicious-plugin list, promote to a NEWS UPDATE.

**Tech Coalition 'Athena' OSS-vulnerability triage platform launch** — 24+ organisations share pre-disclosure vulnerability triage (SecurityWeek 2026-06-16). Defensive-infrastructure pattern signal, not an advisory.

**US Government export-control directive to Anthropic (continuation)** — coalition of cybersecurity executives publicly urges Trump administration regarding foreign-national access to Anthropic models (SecurityWeek 2026-06-16). Continues 2026-06-14 Noted.

**npm v12 default-disable of dependency install scripts** — rolling out; continues 2026-06-12 Noted. Major defensive milestone against the Miasma / Mini Shai-Hulud / IronWorm class.

**Flock surveillance-camera misuse for stalking** (Schneier 2026-06-16) — pattern indicator for off-label use of public-safety infrastructure.

**FCC proposes elimination of burner phones** (Schneier 2026-06-15) — regulatory signal.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, schneier.com, krebsonsecurity.com | ✅ (BC/THN/SW with findings; Schneier no security-tech today; Krebs no posts since 06-10) |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (both 403) |
| Vendor advisories | rapid7.com, fortinet.com/blog/threat-research, msrc.microsoft.com/blog, blog.cloudflare.com/tag/security, avleonov.com | ✅ rapid7 / fortinet / cloudflare / avleonov (no fresh posts), ⚠️ msrc.microsoft.com redirect chain to no content |
| CVE databases / research | nvd.nist.gov, cve.mitre.org, cve.org, opencve.io, securitylab.github.com, googleprojectzero.blogspot.com, kb.cert.org/vuls, dbugs.ptsecurity.com | ✅ nvd / opencve / dbugs.pt / googleprojectzero / kb.cert / securitylab; ⚠️ cve.mitre.org → cve.org redirect with no content |
| Full-disclosure / OSINT | seclists.org/fulldisclosure, packetstormsecurity.com, github.com/search?q=CVE, github.com/0xMarcio/cve, attackerkb.com | ✅ seclists / github search / 0xMarcio; ⚠️ packetstormsecurity.com (redirect, no listings); ❌ attackerkb (403) |
| Bug bounty / disclosures | hackerone.com/hacktivity, bugcrowd.com/disclosures | ⚠️ hackerone no content; ❌ bugcrowd 404 |
| Russian-language / regional | habr.com/ru/companies/tomhunter/articles, teletype.in/@cyberok, cert.gov.ua | ⚠️ all three responded but with no recent posts / no content visible |

**Coverage tallies:** total **30**, checked **20**, with findings **9** (bleepingcomputer, thehackernews, securityweek, github/search, github/0xMarcio, seclists/fulldisclosure, opencve.io, nvd.nist.gov, dbugs.ptsecurity.com), unreachable **4** (cisa.gov, cisa.gov KEV catalog, attackerkb.com, bugcrowd.com), degraded **6** (packetstormsecurity.com, hackerone.com/hacktivity, msrc.microsoft.com/blog, cve.mitre.org, cve.org, cert.gov.ua).

**Errors:** cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403), attackerkb.com (403), bugcrowd.com/disclosures (404), packetstormsecurity.com (redirect to packetstorm.news with no usable listings), hackerone.com/hacktivity (no content visible), msrc.microsoft.com/blog (redirect chain to no usable content), cve.mitre.org → cve.org (no usable content), cert.gov.ua (no content visible).

**CISA KEV:** catalog unreachable this cycle. Confirmed addition (via amplification): CVE-2026-54420 LiteSpeed cPanel plugin, BOD 26-04 three-day federal deadline (BleepingComputer 2026-06-16). No other KEV additions surfaced via amplification today.

---

*Watchtower vulnerability-researcher | Cycle: 2026-06-17/night | Next: 2026-06-18/night*
