# Watchtower Night Report — 2026-06-03
**Cycle:** Night | **Generated:** 2026-06-03 06:00 UTC (2026-06-03T06:00:00Z)
**Sources checked:** 22/30 | **CISA KEV total:** unreachable (cisa.gov 403) | **New KEV additions:** Oracle WebLogic CVE-2024-21182 added 2026-06-01 (federal deadline 2026-06-04, surfaced via SW/BC/THN relay)

---

## 🔴 CRITICAL

### 🔄 Miasma Supply-Chain Worm Scope Expanded 4.5× — Now 32 @redhat-cloud-services npm Packages, 96 Malicious Versions Published in a 72-Second Window, ~10 Million Total Downloads
**Product:** npm @redhat-cloud-services namespace (Hybrid Cloud Console ecosystem) | **CVE:** None assigned | **Status:** Patched (clean versions released) + Compromise Forensics Expanding

Yesterday's disclosure (Watchtower 2026-06-02 NEWS, score 8) listed seven trojanized @redhat-cloud-services packages with ~117K weekly downloads. SecurityWeek's follow-on coverage today (citing Socket / Ox Security / JFrog / StepSecurity / Wiz forensics) puts the true blast radius at **32 packages with 96 malicious versions published within a 72-second window** — clear automated-tooling signature — and **~10 million total cumulative downloads** across the affected packages. Ox Security has identified **210 distinct repositories carrying stolen Miasma-exfiltrated credentials** so far, meaning at least 210 developer environments executed the malicious `preinstall` hook before the packages were yanked. Researchers now believe the initial-access path was a compromised `@redhat-cloud-services` npm scope publishing credential — most likely abused via GitHub Actions OIDC pivot from the previously reported Red Hat employee GitHub account — rather than a workstation-level token theft.

**Material change vs. 2026-06-02:** (a) affected-package count expanded 7 → 32 (4.5×); (b) malicious-version count quantified at 96 with a 72-second burst (automated push); (c) total-download blast radius reframed from "~117K weekly" to "~10M cumulative" (one-to-two orders of magnitude larger); (d) confirmed-compromise count quantified at 210 downstream repos already.

**Why it matters:** The 72-second burst confirms the attacker was operating an automated multi-package push tool, not manual commits — fully consistent with the Wave-2-class supply-chain class predicted in MEMORY 2026-05-19 ("3-7 distinct Wave-2-class compromises by 2026-06-15"). The 210-repo downstream-compromise count is the load-bearing number: every one of those repos likely now has compromised CI tokens that can be used for additional package publishing, and ~10M cumulative downloads means the trojanized versions were in active dependency trees during the exposure window even though the malicious window was short. Hold the score at 8 — scope expansion deepens existing defensive priority but does not change the action posture (rotate-everything-touched-2026-05-29-to-2026-06-01 is unchanged).

**Mitigation (delta vs. 2026-06-02):**
- Re-audit `package-lock.json` / `pnpm-lock.yaml` / `yarn.lock` for the full 32-package list (not just yesterday's seven); SecurityWeek + Socket has the full inventory.
- For every GHA workflow that pulled any @redhat-cloud-services package between 2026-05-29 and 2026-06-01, assume credential exfiltration — rotate GitHub PATs, npm tokens, GCP/Azure/AWS keys, Vault tokens, K8s SA tokens, SSH keys, Docker registry creds, GPG keys.
- If you maintain a private repo and you find your credentials in the Ox Security 210-repo dataset (request via Socket/Ox), treat the entire upstream identity surface as compromised, not just the secret material.
- Block egress to `api.anthropic[.]com` (the typosquat domain, distinct from the legitimate `api.anthropic.com`) on every dev/CI runner as a durable preventive control — this is now established Wave-2 derivative TTP.

**Sources:** [SecurityWeek — Supply Chain Attack Hits 32 Red Hat NPM Packages](https://www.securityweek.com/supply-chain-attack-hits-32-red-hat-npm-packages/) | [TheHackerNews — Miasma Supply Chain Attack Compromises Red Hat npm Packages](https://thehackernews.com/2026/06/miasma-supply-chain-attack-compromises.html) | [BleepingComputer — Red Hat npm packages compromised to steal developer credentials](https://www.bleepingcomputer.com/news/security/red-hat-npm-packages-compromised-to-steal-developer-credentials/)

---

## 🟠 HIGH

### Kirki WordPress Plugin CVE-2026-8206 — REST API Password-Reset Address-Substitution → Unauthenticated Admin Account Takeover, Active Exploitation Against ~500,000 Sites
**Product:** Kirki WordPress plugin (Theme customization framework) | **CVE:** CVE-2026-8206 | **CVSS:** Not assigned (Wordfence rates Critical) | **First reported:** 2026-06-02

The Kirki plugin (≈500,000 active installs, used by a wide swath of premium WordPress themes for customizer extensions) ships a REST API password-reset endpoint that accepts an arbitrary `email` parameter alongside the target `username`. When called, the plugin **generates a valid password-reset link for the named account but sends it to the attacker-supplied email address** instead of the account-owner's registered address — making this a clean unauthenticated-to-administrator account-takeover primitive on any vulnerable site. Affected versions 6.0.0–6.0.6; patched in **6.0.7** released 2026-05-18. Discovered by researcher CHOIGYENGMIN, reported to Wordfence 2026-05-04, vendor notified 2026-05-16, patch 2026-05-18 — but Wordfence reported **active exploitation by 2026-06-02 with 222+ blocked attempts in a 24-hour window**, indicating attackers reverse-engineered the patch to craft the exploit.

**Timeline:** Reported 2026-05-04 → vendor notified 2026-05-16 → patched 2026-05-18 → active in-the-wild exploitation observed 2026-06-02 (15-day patch-to-exploit window).

**Why it matters:** Kirki is bundled by hundreds of premium and free WordPress themes (it is one of the most depended-on customizer libraries in the ecosystem), so the real install base is larger than the headline 500K — most affected admins do not know they have it installed. This is the third active-exploitation WordPress-plugin disclosure in a week (joins WP Maps Pro CVE-2026-8732 MEMORY 2026-06-01 + Funnel Builder MEMORY 2026-05-16), continuing the WP-plugin-as-AVP-vector trend. The patch-to-exploit window is short enough that an asset-management team relying on monthly inventory cadence is structurally exposed.

**Discovered by:** CHOIGYENGMIN (independent researcher, via Wordfence Bug Bounty program).

**Mitigation:**
- Upgrade Kirki to 6.0.7+ on every WordPress installation immediately; check theme bundles for embedded Kirki copies (many themes carry an internal copy that is not auto-updated by the wp.org channel).
- If patching is blocked, disable the plugin entirely or block the vulnerable REST API endpoint at the WAF / reverse proxy.
- Audit WordPress administrator accounts for any unexpected entries created since 2026-05-18; force a password reset for all administrators.
- Run a Wordfence / WPScan scan against the public-facing WordPress fleet to detect vulnerable Kirki versions.

**Sources:** [BleepingComputer — Critical Kirki flaw exploited to hijack WordPress admin accounts](https://www.bleepingcomputer.com/news/security/critical-kirki-flaw-exploited-to-hijack-wordpress-admin-accounts/)

---

### Oracle WebLogic CVE-2024-21182 Added to CISA KEV — Pre-Auth RCE Patched July 2024 Still Widely Unpatched, 3-Day Federal Deadline
**Product:** Oracle WebLogic Server (all 12c / 14c versions through 2024-07 CPU) | **CVE:** CVE-2024-21182 | **CVSS:** 7.5 (NVD) | **First reported:** 2026-06-01 (KEV addition)

CISA added **CVE-2024-21182** to the Known Exploited Vulnerabilities catalog on 2026-06-01 with a 3-day federal remediation deadline of 2026-06-04. The vulnerability — disclosed and patched in Oracle's July 2024 Critical Patch Update — allows an **unauthenticated remote attacker to take over a vulnerable WebLogic Server with no user interaction** via the T3/HTTP protocols. Multiple public PoCs have existed since mid-2024; CISA is the first authoritative warning of in-the-wild exploitation, but SecurityWeek notes that no specific incident reporting has surfaced publicly yet — CISA likely has incident-reporting visibility that has not flowed into the open-source feeds.

**Timeline:** Disclosed and patched 2024-07 Oracle CPU → multiple public PoCs in late 2024 / 2025 → CISA KEV addition 2026-06-01 → federal deadline 2026-06-04 (3-day compressed deadline indicating high confidence in exploitation).

**Why it matters:** Oracle WebLogic is one of the canonical "long-tail" enterprise Java application servers — disproportionately deployed in financial services, healthcare, and government, and disproportionately under-patched (the 2024-07 CPU is nearly two years old). A KEV add with a compressed 3-day federal deadline is CISA's strongest "patch this now" signal, especially on a CVE this old. Joins the 2026 pattern of pre-existing CVEs getting belated KEV adds after sustained in-the-wild operator interest — comparable to CVE-2023-46604 ActiveMQ HelloKitty path (MEMORY context) and CVE-2024-32114 ActiveMQ Jolokia. Different bug from CVE-2026-21962 (Oracle WebLogic Server Proxy Plug-in, MEMORY 2026-04-18 — that is the CVSS 10 plug-in bug). Both bugs need the 2024-07 or later CPU rolled out.

**Mitigation:**
- Apply Oracle's July 2024 Critical Patch Update (or any later CPU) on every WebLogic Server instance.
- Audit the WebLogic fleet for direct internet exposure on T3 (default 7001/7002) — close at the network boundary if not strictly required.
- Hunt EDR/SIEM logs for `oc4j.admin` or `weblogic.t3` deserialization activity since 2024-08.
- Confirm WebLogic Patch Status Tool (PSAT) inventory is current; the long-tail CPU posture of WebLogic deployments is the durable risk.

**Sources:** [SecurityWeek — Oracle WebLogic Vulnerability Exploited in the Wild](https://www.securityweek.com/oracle-weblogic-vulnerability-exploited-in-the-wild/) | [BleepingComputer — CISA flags two-year-old Oracle flaw as actively exploited](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-oracle-weblogic-flaw/) | [TheHackerNews — Oracle WebLogic CVE-2024-21182 Added to KEV Catalog](https://thehackernews.com/2026/06/oracle-weblogic-cve-2024-21182-added-to.html)

---

## 🟡 MEDIUM

### Progress Sitefinity CMS — Multi-CVE Critical Batch Including CVE-2026-7312 (CVSS 10.0)
**Product:** Progress Sitefinity CMS | **CVE:** CVE-2026-7312 (CVSS 10.0), CVE-2026-7198 (CVSS 9.8), CVE-2026-7201 (CVSS 8.8), CVE-2026-7195 (CVSS 8.8) | **Published:** 2026-06-02 (Positive Technologies dbugs)

Positive Technologies' dbugs database surfaced a four-CVE batch against Progress Sitefinity — a widely-deployed enterprise .NET CMS (commonly internet-facing, used by mid-market and enterprise marketing teams). The headline CVE-2026-7312 carries CVSS 10.0 (network-vector, no auth, no UI). CVE-2026-7198 is the CVSS 9.8 secondary, with two 8.8 supporting CVEs (CVE-2026-7195, CVE-2026-7201). Detailed advisories are still in the staging pipeline — PT's research-publication tempo typically translates to mainstream pickup within 7-10 days, and Sitefinity historically has a long tail of unpatched public instances. No PoC has dropped yet; no in-the-wild exploitation reported.

**Why it matters:** Sitefinity sits in the "second-tier widely-deployed CMS" cluster alongside Sitecore and Kentico — visible on internet scanners as `Sitefinity` server-header in tens of thousands of US/EU enterprise marketing-property deployments. CVSS 10.0 against a CMS this widely-deployed is a leading indicator that an exploitation wave is plausibly 1-2 weeks out; the urgency for our scope is "patch the fleet before PoC publication." No exploitation yet, so a Medium tier (5-6) is right — this would shift to High the moment a PoC drops or vendor patches escalate the advisory.

**Mitigation:**
- Inventory all internet-facing Sitefinity instances (HTTP `X-Powered-By: Sitefinity` or `Server: ASP.NET` + `/Sitefinity/` path response).
- Monitor Progress Security Advisory page (`docs.progress.com`) for the patched release announcement; pre-stage the patch rollout.
- For non-internet-facing instances, audit identity-provider integrations and admin UI exposure — Sitefinity CVE classes historically include auth bypass.

**Sources:** [Positive Technologies dbugs — PT-2026-45762 / 45760 / 45761 / 45759](https://dbugs.ptsecurity.com)

---

### Dashlane Confirms Encrypted Vault Downloads for <20 Users After Brute-Force / 2FA-Bypass Wave
**Product:** Dashlane password manager (consumer plan) | **CVE:** None assigned | **Published:** 2026-06-02

Dashlane updated its 2026-05-31 brute-force disclosure (previously reported as "no platform compromise") to confirm that **fewer than 20 personal-plan users had their encrypted vaults successfully downloaded** after attackers cleared 2FA on those specific accounts via credential-stuffing + device-registration. Master Password decryption is not bypassed — the vaults remain encrypted client-side, and Dashlane emphasizes that without the user's master password the contents are not directly recoverable. The campaign was detected by Dashlane's rate-limit and anomalous-login telemetry (the same telemetry that caused the user-visible login slowness reported yesterday).

**Why it matters:** First publicly-disclosed password-manager-vault exfiltration (vs. LastPass-class historical precedent in 2022). Even with encrypted contents, an offline brute-force of the master password is a credible follow-on against any of the <20 affected users — particularly because the password-manager-target class incentivizes patient cracking. This is a material escalation from the 2026-06-02 "no compromise" framing — the attacker now has cipher material in hand and can grind. Defensive implications: every Dashlane personal-plan corporate-managed account needs a password rotation, regardless of whether the user is on the affected-20 list (Dashlane has not yet published the affected-account criteria).

**Mitigation:**
- For any corporate-managed Dashlane personal-plan account: enforce a master-password rotation; remind users that vault contents pre-rotation should be treated as offline-crackable.
- Audit Dashlane device-registration history for unexpected entries since 2026-05-25 (start of attack window).
- Reinforce master password complexity training; consider mandatory migration to enterprise SSO-fronted password managers for shared accounts.
- For incident response: assume all entries in the downloaded vaults are subject to long-tail credential rotation in the highest-value vaults (financial, IdP, infrastructure).

**Sources:** [TheHackerNews — Dashlane Discloses Brute-Force Attack, Encrypted Vaults of Fewer Than 20 Users Downloaded](https://thehackernews.com/2026/06/dashlane-discloses-brute-force-attack.html) | [SecurityWeek — Dashlane Brute-Force Attack Leads to Vault Access](https://www.securityweek.com/dashlane-brute-force-attack-leads-to-limited-encrypted-vault-downloads/) | [BleepingComputer — Dashlane password manager users locked out by brute force attacks](https://www.bleepingcomputer.com/news/security/dashlane-password-manager-users-locked-out-by-brute-force-attacks/)

---

### Sophos Discloses AI-Built Ransomware Toolkit — Claude Opus + Multi-Agent Pipeline With 80 Modules vs. 70+ EDR-Evasion Techniques
**Product:** Threat-actor capability (not a CVE) | **Published:** 2026-06-02

Sophos researchers detailed a threat actor running an **agentic AI-assisted ransomware development pipeline** that uses Claude Opus and other frontier models as iterative payload designers. The framework includes a Python payload generator (emitting Rust and Go binaries), an automated AD-enumeration panel, Cobalt Strike profiles, and a Telegram-bot C2 plane. The toolkit iteratively tests payloads against Sophos, CrowdStrike, and Microsoft Defender, refining ~80 modules against 70+ evasion techniques per cycle.

**Why it matters:** The novelty is not "AI in malware" — that's been Arkanix-class for a year (MEMORY 2026-02-23) — but rather the **agentic AI-development pipeline as an offensive capability**, where the iteration-to-publication cadence from a new public defensive-research blog → working evasion in deployed payloads compresses to days. Joins the MEMORY cluster of "AI-as-attacker-development-tool" entries (Bluekit phishing kit MEMORY 2026-05-08, Arkanix Stealer 2026-02-23, OpenAI/Anthropic Mythos defensive cluster MEMORY 2026-04-25 / 05-22 / 05-26) but is the first specific-actor toolkit using Claude Opus iteratively for ransomware build-test-deploy. Defensive implication: behavioral / EDR-telemetry detection (not signature) becomes the load-bearing primitive; pure-signature EDR rules now have a structurally short useful lifespan.

**Mitigation:**
- Prioritize behavioral-detection rules over signature-based ones; assume any documented evasion technique will be operationalized within days.
- Track Sophos IOC bundle (URLs, hashes, Telegram-bot identifiers) for the specific actor's infrastructure; block at network egress.
- For high-value-target organizations, accelerate EDR-baseline-drift detection (the toolkit's iterative output produces payloads that look "near-baseline" rather than novel).
- Detection-engineering org review: shrink the "research publication to detection-rule deployment" cycle as a KPI.

**Sources:** [BleepingComputer — AI-built ransomware toolkit automates EDR evasion, AD discovery](https://www.bleepingcomputer.com/news/security/ai-built-ransomware-toolkit-automates-edr-evasion-ad-discovery/)

---

### ChatGPT Share-Link Abuse — Google-Ads → ChatGPT-Hosted Fake Outage Page → `openew[.]app` Cross-Platform Malware
**Product:** ChatGPT share feature (chatgpt.com) abused for renderer-trust attack | **Published:** 2026-06-02

Push Security disclosed a campaign that **buys Google Ads for "chatgpt" search terms, redirects victims to a legitimate chatgpt.com share URL that renders attacker-controlled HTML/CSS impersonating an "OpenAI service outage" page**, and directs users to download a "fix" from `openew[.]app` — a cloaked typosquat that serves Windows and macOS malware variants. Because the user lands on a real chatgpt.com URL, traditional URL-reputation-based controls and corporate sandboxes treat the page as trusted; the lure renders entirely through the legitimate share-rendering pipeline.

**Why it matters:** Direct extension of the LLMShare campaign class (MEMORY 2026-05-30) and ChatGPhish trusted-renderer class — both predicted to scale. The new TTP here is the **Google-Ads top-of-funnel into a legitimate-share-link redirect** that bypasses the "is this URL trusted" check entirely; the macOS variant continues the cross-platform-targeting trend documented in 2026-06-02 DriveSurge. Confirms the durable defensive ask in MEMORY 2026-06-02: monitor AI platform share-URL paths in web filters and corporate sandboxes; the legitimate-trust signal of the chatgpt.com origin is now structurally adversary-exploitable.

**Mitigation:**
- Add ChatGPT share-URL paths (`/share/`, `/c/share/`) and similar Claude Artifacts / Gemini share endpoints to web-proxy heuristic-inspection rules; do not exempt because of the legitimate-domain origin.
- Block egress to `openew[.]app` and adjacent typosquat domains (Push Security has the bundle).
- User training: legitimate ChatGPT outage notices come through `status.openai.com`, never via a share-link service-down rendering.
- Review Google Ads brand-protection / lookalike-monitoring posture for AI-vendor search-term abuse.

**Sources:** [BleepingComputer — ChatGPT share links abused to host fake outage pages to deliver malware](https://www.bleepingcomputer.com/news/security/chatgpt-share-links-abused-to-host-fake-outage-pages-to-deliver-malware/)

---

## 📋 Noted / Monitoring

**CIFSwitch — CVE-2026-46243 now assigned** to the 19-year-old Linux CIFS-spnego-upcall LPE covered as CVE-pending in Watchtower 2026-05-31; checker script `MrForkBomb/CIFSwitch-Checker-CVE-2026-46243` now circulating on GitHub. Defensive posture unchanged from prior advisory — patch the kernel commit `3da1fdf` or blacklist the CIFS module on hosts that do not need it.

**Windows Netlogon CVE-2026-41089 — Microsoft pushes back on Belgian CCB exploitation claim.** Microsoft told BleepingComputer it has "no evidence" supporting the active-exploitation framing CCB published 2026-06-01 (Watchtower 2026-06-02 NEWS, score 9). Operationally no change — patch posture and KEV-watch posture remain the same; CCB and CISA have shared incident-reporting visibility Microsoft does not have, and patch-now is the correct stance regardless of which read prevails.

**Apache Kafka CVE-2026-41115** — Improper authorization on the `CONSUMER_GROUP_DESCRIBE` API allowing cross-group consumer-state disclosure. Patched in 4.0.1 / 3.9.2; broad Apache pipeline blast radius, low-but-nonzero data-exposure risk. (oss-security 2026-06-02)

**BIRD / BIRD2 BGP — stack-buffer overflow in AS_PATH mask matching** (CVE pending). Routing-daemon vector — DoS-class via crafted BGP UPDATE in route-filter context. Patch when assigned; OOS for most environments but BGP-edge operators should track. (oss-security 2026-06-02)

**OpenStack — Swift proxy DoS + Neutron policy bypass** (two-errata batch from Goutham Pacha Ravi). Routine OpenStack errata, both with patches available; affects clouds running Swift object-storage or Neutron networking. (oss-security 2026-06-02)

**Linux kernel TLS — use-after-free in `tls_sk_proto_close()`** (Oleg Sevostyanov disclosure). UAF on socket-close path in kernel TLS; local-process trigger requires CAP_NET_ADMIN or a vulnerable userspace, so likely LPE-class. CVE pending. (oss-security 2026-06-02)

**X.Org X server + Xwayland — multi-CVE advisory** (Peter Hutterer disclosure). Standard X.Org security batch; mostly LPE/client-side. Patch on desktop fleet through distribution channels. (oss-security 2026-06-02)

**CERT VU#615987 — Verizon VoLTE deployments missing IPsec integrity protection for IMS SIP signaling.** Telecom critical infrastructure; not a corporate-perimeter item but a calibration-data point for the carrier-VoLTE risk surface. Affected: Verizon network deployments.

**CERT VU#873170 — Collibra Agent improper authentication + path traversal.** Enterprise data-governance product; if your environment runs Collibra Agent on internal endpoints, patch when vendor publishes.

**CERT VU#265691 — Appsmiths SQL Query autocomplete renderer XSS.** Low-deployment SaaS internal-tooling builder; included for completeness.

**Google Android June 2026 update — CVE-2025-48595 (CVSS 8.4) actively exploited zero-day + 124 additional flaws.** Mobile-only and OOS for our scope (no defensive-relevant remote-protocol surface beyond MDM/MAM), but the active-exploitation framing and the existence of an MDM-policy-bypass CVE (CVE-2025-48652) is worth a calibration logging.

**Gamaredon (Russia-aligned) weaponizes WinRAR CVE-2025-8088** to deliver GammaWorm + GammaSteel against Ukrainian targets. Older WinRAR CVE re-monetized for a specific targeting campaign — track but no general-deployment urgency.

**SideCopy (Pakistan-aligned) Operation XENOFISCAL — Afghanistan Finance Ministry targeted with Xeno RAT** via spear-phishing. Regional APT operation; calibration only for our scope.

**Microsoft Android app single-line-of-code account-token exposure** (SecurityWeek "exclusive"). Mobile-only but high-visibility for app-vendor secure-development calibration; "billions of Microsoft Android app downloads" framing is on the marketing-claim side, defensive impact is limited unless your environment runs the affected Microsoft Android apps in BYOD.

**Microsoft sends legal threats to security researcher publishing Windows exploits (incl. BitLocker bypass)** (Schneier). Vulnerability-disclosure-policy data point; track for whether this becomes a disclosure-chilling-effect trend. Not actionable today.

**Trump signs Executive Order on AI Model Vetting for national-security risks.** Policy / governance item; calibration data point for the regulatory side of AI-model risk that has been a Watchtower MEMORY recurring track since 2026-04-25.

**Anthropic Mythos preview expanded to 150 additional organizations.** Calibration data point on the Mythos / Project Glasswing track (MEMORY 2026-04-25 / 05-22 / 05-26); expect a corresponding wave of vendor advisories in the next 30 days as the partner pool's research outputs hit coordinated disclosure.

**Garmin Empirbus Wireless Display Unit CVE-2025-27851 (CVSS 9.3).** OT/marine-IoT; OOS for corporate perimeter but logged for OT-fleet calibration.

**NVIDIA NVTabular CVE-2026-24237 — unsafe pickle deserialization → RCE.** ML pipeline library; low corporate-deployment but watch for ML-team usage on internal NVTabular notebooks.

**Red Hat 389 Directory Server CVE-2026-9064 — LDAP-control bound-check missing → CPU/heap DoS.** Patch when vendor errata land; enterprise LDAP impact is DoS-only.

**Anthropic Claude HUD (`jarrodwatts/claude-hud`) CVE-2026-47092 — COMSPEC env-var command injection → RCE on Windows.** Niche desktop AI-HUD utility; included as another data point for the AI-coding-assistant local-RCE class (MEMORY 2026-05-27 mouse5212 etc.).

**WeedHack Minecraft infostealer — 116K systems infected since January 2026.** Gamer-targeting infostealer with corporate-spillover potential if BYOD endpoints are unmanaged; OOS but worth a single-line awareness note for SecOps user-awareness teams.

**Dragos acquires xIoT security firm Phosphorus.** Industry consolidation in OT/IoT defense; calibration on the OT-security tooling ecosystem.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (both 403 via WebFetch; KEV add for CVE-2024-21182 surfaced via SW/BC/THN relay) |
| Vendor advisories | rapid7.com (blog), fortinet.com/blog/threat-research, securitylab.github.com, blog.cloudflare.com/tag/security, msrc.microsoft.com/blog | ⚠️ (rapid7/fortinet/securitylab no new since last week; cloudflare degraded; msrc degraded) |
| Research / OSINT | schneier.com, krebsonsecurity.com, avleonov.com, dbugs.ptsecurity.com, opencve.io / app.opencve.io | ✅ |
| CVE feeds | seclists.org/fulldisclosure, openwall oss-security, kb.cert.org/vuls, github.com/0xMarcio/cve, github.com/search?q=CVE, nvd.nist.gov, cve.org, cve.mitre.org | ✅ / ❌ mixed (nvd/cve.org/cve.mitre.org JS-only) |
| Supply chain | GitHub Security Advisories (PraisonAI/Vitest dedup; nothing fresh in window) | ✅ |
| Threat intel | fortinet/blog/threat-research, googleprojectzero.blogspot.com, packetstormsecurity.com | ⚠️ / ❌ (gpz redirects, packetstorm degraded) |
| Russian-language | habr.com/tomhunter, teletype.in/@cyberok, cert.gov.ua | ⚠️ (all degraded / stale / empty per MEMORY) |
| Bounty platforms | hackerone.com/hacktivity, bugcrowd.com/disclosures, attackerkb.com | ❌ (JS / 404 / 403 per MEMORY) |

**Errors:** cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403), attackerkb.com (403), cve.org (JS), cve.mitre.org (redirects to cve.org), googleprojectzero.blogspot.com (redirects), hackerone.com/hacktivity (JS), bugcrowd.com/disclosures (404).

**Degraded:** packetstormsecurity.com (homepage returns nav only), nvd.nist.gov (homepage no CVE listing), msrc.microsoft.com/blog (empty / nav-only), habr.com/ru/companies/tomhunter (stale through 2026-03-06), teletype.in/@cyberok (stale through 2026-02-04), cert.gov.ua (empty).

**CISA KEV:** Endpoint still unreachable via WebFetch; today's new add is **Oracle WebLogic CVE-2024-21182 (KEV 2026-06-01, federal deadline 2026-06-04)** surfaced via SW/BC/THN relay. Windows Netlogon CVE-2026-41089 expected addition (per Watchtower 2026-06-02 forecast) has not landed yet; PAN-OS CVE-2026-0257 federal deadline 2026-06-01 has lapsed and remains tracked.

---

*Watchtower vulnerability-researcher | Cycle: 2026-06-03/night | Next: 2026-06-04/night*
