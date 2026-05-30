# Watchtower Night Report — 2026-05-30
**Cycle:** Night | **Generated:** 2026-05-30 09:00 UTC (2026-05-30T09:00:00Z)
**Sources checked:** 21/30 | **CISA KEV total:** see below | **New KEV additions:** none confirmed in last 24h

---

## 🔴 CRITICAL

### PraisonAI 16-CVE Second-Batch Mass Disclosure — Hardcoded JWT Key, Sandbox Escape, Default-No-Auth Across Core + Platform (CVSS up to ~9.8)
**Product:** PraisonAI (core, pip) + praisonai-platform (enterprise SaaS layer, pip) | **CVE:** CVE-2026-47391, CVE-2026-47392, CVE-2026-47393, CVE-2026-47394, CVE-2026-47396, CVE-2026-47397, CVE-2026-47398, CVE-2026-47399, CVE-2026-47405, CVE-2026-47406, CVE-2026-47407, CVE-2026-47409, CVE-2026-47410, CVE-2026-47414, CVE-2026-47416, CVE-2026-48169 | **Status:** Patched (advisories shipped 2026-05-28/29) — no confirmed ITW yet

GitHub Advisories published a sixteen-CVE coordinated batch against the PraisonAI agent-orchestration ecosystem on 2026-05-28/29. The Critical-class set covers (i) JWT signing-key defaulting to the hardcoded string `dev-secret-change-me` when `JWT_SECRET_KEY` is unset → cross-tenant token forgery for any user (CVE-2026-47410), (ii) cross-workspace IDOR chained with member-role privilege escalation → admin take-over (CVE-2026-47407), (iii) unauthenticated LLM-driven code execution reachable through an official example (CVE-2026-47391), (iv) Python `builtins` leak from the subprocess sandbox enabling escape to host shell (CVE-2026-47392), (v) Flask API server shipping with authentication disabled by default (CVE-2026-47393), and (vi) workspace-member promotion to owner via unguarded PATCH (CVE-2026-47416). The High-class set adds arbitrary file read/write, cross-workspace dependency/label IDORs, unguarded module execution, and role-check gaps across the platform's admin surface.

**Timeline:** Original PraisonAI 3-CVE batch (CVE-2026-40287/40288/40289) → 2026-04-10 disclosure (covered Watchtower 2026-04-14) → second 16-CVE batch → 2026-05-28/29 publication on GitHub Advisories.

**Why it matters:** PraisonAI is an actively used self-hosted AI agent orchestration framework; the platform layer typically holds tenant API keys for OpenAI/Anthropic/Vertex plus business connectors. A single internet-exposed PraisonAI Platform instance now yields cross-tenant token forgery (any user including admin), arbitrary code execution, and sandbox escape — this is the second multi-CVE batch against the same product in 45 days, reinforcing the 2026-Q2 pattern: **self-hosted AI orchestration frameworks ship with hardcoded dev secrets, default-disabled auth, and weak tenancy boundaries — treat every internet-facing AI-platform deployment as presumptive cross-tenant RCE surface**.

**Discovered by:** Researchers credited via GitHub Advisories (multiple GHSA reports under 0xMarcio / praisonai-platform org).

**Mitigation:**
- Inventory all PraisonAI / praisonai-platform deployments — including dev/staging/POC instances that often skip JWT hardening.
- Upgrade to the patched releases referenced in each GHSA (CVE-2026-47391/47392/47393/47394/47396/47397/47398/47399/47405/47406/47407/47409/47410/47414/47416/48169).
- Confirm `JWT_SECRET_KEY` is set to a strong unique value — any instance still on default is presumed token-forged.
- Confirm Flask API authentication is enabled and member-role checks are not bypassed.
- Network-restrict PraisonAI control planes to trusted networks; assume any tenant data accessible from a compromised instance is leaked.

**Sources:** [GitHub Advisories — PraisonAI](https://github.com/advisories?query=is%3Aopen+praisonai) | [CVE-2026-47410 (GHSA-3qg8-5g3r-79v5)](https://github.com/advisories/GHSA-3qg8-5g3r-79v5) | [CVE-2026-47407 (GHSA-h8q5-cp56-rr65)](https://github.com/advisories/GHSA-h8q5-cp56-rr65) | [CVE-2026-47391 (GHSA-vg22-4gmj-prxw)](https://github.com/advisories/GHSA-vg22-4gmj-prxw) | [CVE-2026-47392 (GHSA-4mr5-g6f9-cfrh)](https://github.com/advisories/GHSA-4mr5-g6f9-cfrh)

---

## 🟠 HIGH

### Marimo CVE-2026-39987 UPDATE — Sysdig Confirms Real-World LLM-Agent Post-Compromise: Adaptive Cloud-Cred Harvesting → Parallel-SSH → DB Exfil in Minutes
**Product:** Marimo Python notebook (≤0.20.4 — patched in 0.23.0) | **CVE:** CVE-2026-39987 | **CVSS:** 9.3 | **First reported:** 2026-04-14 (Watchtower)

Sysdig published 2026-05-29 the first confirmed in-wild observation of an LLM agent driving the post-compromise phase after CVE-2026-39987 initial access. The attacker chain: pre-auth WebSocket terminal RCE on a public-facing Marimo instance → AWS instance metadata harvest → credential replay → SSH private key pull from AWS Secrets Manager → eight parallel SSH sessions against a downstream bastion → full PostgreSQL schema discovery + content exfiltration **within two minutes**. Four LLM-agent fingerprints: adaptive recon improvising a DB dump without schema knowledge, a Chinese planning comment "看还能做什么" ("see what else we can do") leaking from command output, machine-optimised delimited command formatting designed for automated parsing, and chained input-from-prior-output flow. This is the first publicly documented **end-to-end LLM-driven post-exploitation chain** observed against a real victim — not a researcher demo.

**Why it matters:** This is the leading edge of an offensive-AI tradecraft transition our scope has been tracking (Nimbus Manticore MiniFast, GreyVibe, GTIG ITW AI-generated 0-day, mouse5212 npm). Post-comp speed (2 minutes from RCE → DB exfil) is now bounded by the LLM API rather than the operator's typing speed; detection windows built around "minutes-to-hours" analyst sessions are misaligned with this tempo. Defenders should assume an AI-agent operator can pivot through cloud credentials and AWS Secrets Manager fast enough that DLP/EDR correlation rules tuned for human-pace operators will miss the chain.

**Mitigation:**
- Patch Marimo to 0.23.0 immediately if not already done (originally tracked since 2026-04-14).
- Tighten IMDSv2 + remove unnecessary IAM role grants from notebook/data-science hosts; treat any Marimo instance as a fully privileged AWS principal.
- Audit AWS Secrets Manager access policies — restrict by source IP/role identity where feasible.
- Tune cloud-trail detection thresholds for sub-minute credential-replay → secret-manager-read → cross-account-SSH chains; these are no longer rare.
- Hunt for the Sysdig-published IOCs and TTPs in cloudtrail / VPC flow logs over the last 30 days.

**Sources:** [TheHackerNews — Attackers Use LLM Agent for Post-Compromise](https://thehackernews.com/2026/05/attackers-use-llm-agent-for-post.html) | [Sysdig — LLM-Driven Post-Exploitation against Marimo CVE-2026-39987](https://sysdig.com/blog/llm-driven-post-exploitation-marimo/) | [Watchtower 2026-04-14 (original disclosure)](https://github.com/0pen-crab/Watchtower/blob/main/reports/2026/04/14/report.md) | [Watchtower 2026-04-17 (NKAbuse weaponisation)](https://github.com/0pen-crab/Watchtower/blob/main/reports/2026/04/17/report.md)

---

### ChatGPhish — Markdown-Image Rendering in ChatGPT Web Summaries Enables Stealth Phishing + IP/UA/Referer Leakage (Permiso Security)
**Product:** OpenAI ChatGPT web client (chatgpt.com response renderer) | **CVE:** None assigned | **CVSS:** n/a | **First reported:** 2026-05-29

Permiso Security disclosed 2026-05-29 a class of prompt-injection-adjacent ChatGPT response-rendering issues. When a user asks ChatGPT to summarise a webpage, malicious Markdown links and images embedded by the attacker are rendered inside ChatGPT's trusted interface: the image fetches leak the user's IP / User-Agent / Referer to the attacker's server, and the rendered links inherit ChatGPT-domain trust for phishing lures (fake security alerts, QR codes pointing to attacker infrastructure). The attack requires only that the attacker control any URL the user asks ChatGPT to read, making it a zero-click phishing-platform conversion of ChatGPT and bypassing email/desktop URL filters. OpenAI's official patch status was not stated at disclosure time.

**Why it matters:** This is the second 2026-Q2 case where the **AI assistant's own response renderer becomes the phishing surface** (joins prior ClaudeBleed-class AI-agent-browser issues). Any defender that allows ChatGPT use against external-URL summarisation must now assume requests can leak end-user network metadata and serve trusted-looking phishing payloads. Treat ChatGPT-summarised links and "alerts that appeared in ChatGPT" as untrusted input categories.

**Mitigation:**
- User-awareness messaging: ChatGPT alerts/QR codes/links are no more trustworthy than the source URL summarised.
- Where feasible, run ChatGPT through enterprise wrappers that strip rendered Markdown image fetches and outbound links from untrusted domains.
- Monitor for outbound HTTP requests originating from end-user browsers to suspicious image hosts whose Referer points to chatgpt.com.

**Sources:** [TheHackerNews — ChatGPhish Vulnerability Turns ChatGPT into a Phishing Platform](https://thehackernews.com/2026/05/chatgphish-vulnerability-turns-chatgpt.html) | [Permiso Security — ChatGPhish Disclosure](https://permiso.io/blog/chatgphish-markdown-rendering-vulnerability)

---

### LLMShare Campaign — chatgpt.com/s/ Share-Pages Abused for Fake-Outage Malware Delivery via Google Ads (Push Security)
**Product:** OpenAI ChatGPT shared-conversation surface (chatgpt.com/s/) | **CVE:** None | **First reported:** 2026-05-29

Push Security disclosed 2026-05-29 an active campaign — internally tracked "LLMShare" — abusing ChatGPT's shared-conversation feature to host attacker-controlled HTML on the trusted chatgpt.com origin. Attackers buy Google Ads on "ChatGPT" / "ChatGPT login" search queries pointing to crafted `chatgpt.com/s/<id>` pages displaying fake "ChatGPT web version unavailable" outage notices and redirecting users to `openew[.]app`, a fake OpenAI download portal serving Windows + macOS malware-laden "desktop clients". Earlier analogous campaigns against AI-platform sharing features distributed infostealers; specific payload attribution was not published.

**Why it matters:** This is the **third AI-platform-trust-surface-abuse pattern in 30 days** (joins ChatGPhish renderer abuse + mouse5212 npm `/mnt/user-data` exfil pattern), but the first to weaponise the genuine `chatgpt.com` origin for in-line phishing. Any URL filter or user-training program that treats chatgpt.com as a uniformly trusted host is now wrong. Enterprise SOC blocklists, web proxies, and email URL-rewriting need to distinguish `chatgpt.com/s/` shared-page paths from the main chat interface.

**Mitigation:**
- Add `chatgpt.com/s/` path-prefix to web proxy/SWG inspection rules; alert on user navigations to share pages reached from external referers (Google ads in particular).
- Block `openew[.]app` and related lookalike domains at DNS/SWG layers.
- Awareness: a chatgpt.com URL is no longer a sufficient trust signal — users must verify the path/canonical content matches an expected conversation.
- Hunt EDR for recent installation of "ChatGPT desktop client" binaries downloaded outside Microsoft Store / official OpenAI channels.

**Sources:** [BleepingComputer — ChatGPT Share Links Abused to Host Fake Outage Pages](https://www.bleepingcomputer.com/news/security/chatgpt-share-links-abused-to-host-fake-outage-pages-to-deliver-malware/) | [Push Security — LLMShare campaign analysis](https://pushsecurity.com/blog/llmshare-chatgpt-share-page-malware)

---

### Asocks 17M-Device Botnet Takedown — 200+ Servers Seized in Netherlands (Dutch NCSC / National Police)
**Product:** Asocks residential-proxy botnet infrastructure (≥17M infected endpoints across Windows/macOS/Android/iOS) | **CVE:** n/a | **First reported:** 2026-05-29

Dutch authorities announced 2026-05-29 a takedown action against the Asocks "universal proxy service" operation: 200+ servers seized at a Netherlands-based hosting provider supporting the C2/coordination layer for an estimated 17 million infected devices spread across 150 advertised locations and 7 million residential IPs. Critically the Dutch NCSC's investigation concluded the bulk of infected device-owners "did not knowingly participate" in the operation — contradicting Asocks' commercial framing as a voluntary bandwidth-share marketplace and confirming it as a covert residential-proxy botnet powered by malware infection. The operation is reported as separate from the 2026-05-25 Stark Industries / MIRhosting / WorkTitans BV seizure (Watchtower 2026-05-29 update).

**Why it matters:** This is the **fourth major adversary-infrastructure disruption in 14 days** (joins Fox Tempest MSaaS 2026-05-19, GlassWorm v2 four-channel C2 severance 2026-05-26, Stark Industries / MIRhosting 2026-05-25, and now Asocks 2026-05-29). Residential-proxy botnets are the primary obfuscation layer for credential-stuffing, account-takeover, bot-management bypass, and scraping campaigns hitting consumer-facing services in our scope; takedown reduces the available exit-IP supply but does not free already-infected endpoints — the malware persists and is likely to be enrolled into the next proxy marketplace within weeks.

**Discovered by:** Dutch National Cyber Security Centre (NCSC) + Dutch National Police, with collaboration noted but unnamed partners.

**Mitigation:**
- Treat any user authentication originating from a known Asocks/residential-proxy exit IP over the last 6 months as potentially attacker-relayed; review high-risk account changes for matching patterns.
- Bot-management vendors should update reputation feeds; expect a short respite then re-emergence under a successor brand (PQ → Stark → MIR → "next").
- For consumer-facing services: confirm IP-reputation + behavioural-bot scoring is layered, not IP-only — assume residential-proxy supply remains structurally available.

**Sources:** [BleepingComputer — Dutch Govt Disrupts 17M-Device Botnet](https://www.bleepingcomputer.com/news/security/dutch-govt-disrupts-malware-botnet-with-17-million-infected-devices/) | [Dutch NCSC announcement (NL)](https://www.ncsc.nl/actueel/nieuws/2026/mei/asocks-takedown)

---

## 🟡 MEDIUM

### Vibe-Coded Apps — Red Access "Shadow Builders" Finds 2,000+ Sensitive-Data Exposures Across AI-No-Code Platforms
**Product:** AI-generated no-code apps deployed on vibe-coding platforms (Cursor projects, v0/Vercel, Bolt, Lovable, Replit Ghostwriter et al.) | **CVE:** n/a | **Published:** 2026-05-29

Red Access's "Shadow Builders" report (covered by THN + Wired + Axios 2026-05-29) catalogued ~380,000 publicly accessible web assets across the leading vibe-coding platforms, ~5,000 of which appear corporate-attached and 2,000+ of which contain sensitive corporate, operational, or personal data — many granting admin access by default to anyone reaching the URL. These applications increasingly connect directly to production CRMs / ERPs / BI systems while bypassing the traditional DLP / CASB / SSO control plane. This is positioned as a distinct **Shadow AI** asset class, larger and faster-growing than classic Shadow IT.

**Mitigation:** Inventory whether any "vibe-coded" prototypes exist inside your perimeter — particularly ones connecting to internal data sources. Mandate that any vibe-platform deployment carrying production data sits behind enterprise SSO and CASB scrutiny. Periodically scan vibe-platform public-app indexes for your brand assets / data fragments.

**Sources:** [TheHackerNews — What 2,000 Exposed Vibe-Coded Apps Reveal](https://thehackernews.com/2026/05/what-2000-exposed-vibe-coded-apps.html) | [Red Access — The Shadow Builders Report](https://redaccess.io/shadow-builders)

---

## 📋 Noted / Monitoring

**CVE-2026-44825 (Apache Solr BasicAuth CLI):** `bin/solr` CLI's BasicAuth enablement path silently configures additional users with insecure defaults (oss-security 2026-05-29). Audit Solr clusters where BasicAuth was enabled via CLI workflow; review `security.json` for unexpected user entries.

**CVE-2026-48840 (Exim 4.99.4 PROXY-protocol):** PROXY-protocol uninitialised-stack disclosure leaks adjacent memory to peer (oss-security 2026-05-29). MTA-level; impact bounded but worth tracking for memory-disclosure-to-bypass chains.

**CVE-2024-13745 (EDK II partition table measurements):** TPM measurement-list issues for partition tables in EDK II firmware (oss-security 2026-05-29) — firmware-tier integrity edge case.

**[vim-security] Vim < 9.2.561 Python omni-completion ACE:** Arbitrary code execution via Python omni-completion in older Vim builds — local client/dev-tool only, OOS for our infra scope but worth flagging given dev-workstation distribution.

**Linux ZCRX DMA-after-unmap (oss-security, Solar Designer 2026-05-29):** Race in `netif_rxq_cleanup_unlease()` ordering inversion; kernel net-stack DMA window. Track for downstream patches.

**JINX-0164 (Wiz, 2026-05-28):** LinkedIn-recruiter-themed social-engineering against cryptocurrency firms + developers, deploying AUDIOFIX (Python infostealer) + MiniRAT (Go) via fake-meeting-app downloads + compromised npm `@velora-dex/sdk`. TTPs mirror BlueNoroff / Contagious Interview but no infrastructure overlap. Threat-actor cluster, OOS for CVE tracking.

**Kimsuky HTTPSpy (THN 2026-05-29):** North-Korean Kimsuky distributing HTTPSpy RAT disguised as Korean security-software installers (nProtect, AhnLab) + fake Cisco Webex camera-fix prompts targeting South Korean military/corporate; no new CVE, social-engineering only.

**Sicoob.Sdk NuGet malicious package (THN 2026-05-29, Sentry endpoint exfil):** Versions 2.0.0–2.0.4 exfiltrate Brazilian-banking PFX certs + passwords + client IDs to hardcoded Sentry endpoint; ~500 downloads, NuGet removed. 11 sibling "sicoob" packages with ~6,000 combined downloads also flagged. Niche, Brazilian-banking-specific.

**stigmem-node federation issues (GHSA-9vp8-3hmv-8fgh, GHSA-jmfc-hfjq-pxcp 2026-05-28):** Federation peer registration lacks out-of-band approval; cleartext non-loopback transport allowed. Niche.

**Carnival Cruise Line — 6M-record breach (SecurityWeek 2026-05-28):** Consumer/PII disclosure with identity-theft risk; details on intrusion vector pending. Tracking only — consumer-PII class, OOS for infra-CVE focus.

**Charter Communications — HIBP-confirmed 4.9M accounts + 85K employee-directory subset (BleepingComputer 2026-05-29):** Extends the 2026-05-29 Noted item; ShinyHunters initial-access remains the April 2026 vishing-via-Entra-account → Salesforce-record-pull chain. No new CVE; tracking the public-data-exposure expansion.

**Google Chrome 148 — 151 CVEs (SecurityWeek 2026-05-29):** 22 critical + 123 high; use-after-free + insufficient-validation classes dominate. Client browser, OOS for our infra scope; noted for fleet-patching ack.

**Google Chrome DBSC general availability (BleepingComputer 2026-05-29):** Device-Bound Session Credentials cryptographically tie session cookies to TPM/Secure-Enclave-backed device keys, mitigating infostealer cookie-theft → MFA-bypass. Mandatory for Workspace tenants; defensive feature note.

**ChatGPT 'Mythos-class' rollout (BleepingComputer 2026-05-28):** Anthropic confirmed Claude Mythos models will roll out to public after security-driven delay; no specific CVE — flagged because next-gen model deployment changes the AI-platform threat model for code-execution agents.

**DDoS-as-a-Service market 2023→2026 (BleepingComputer 2026-05-29):** ~10× growth in service ads, ~4× growth in unique clusters, ~3× growth in active actors, subscription pricing as low as $25/month, premium up to $2,000. Background telemetry; no specific advisory.

**FBI fake-FIFA World Cup fraud sites (BleepingComputer 2026-05-28):** Already noted 2026-05-29 — consumer-fraud advisory only.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer, thehackernews, securityweek, krebsonsecurity, schneier | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog, cert.gov.ua | ⚠️ (all 403 / empty — KEV data sourced via THN/Krebs/SecurityWeek) |
| Vendor advisories | fortinet/threat-research, rapid7/blog, securitylab.github.com, dbugs.ptsecurity.com, msrc.microsoft.com/blog, cloudflare/security | ✅ / ⚠️ (msrc.microsoft.com empty) |
| Research / OSINT | seclists.org/fulldisclosure, openwall.com/lists/oss-security, projectzero.google, opencve.io, github.com/0xMarcio/cve, avleonov.com | ✅ |
| Supply chain | github.com/advisories, github.com/search?q=CVE, packetstormsecurity.com | ✅ / ⚠️ (packetstorm degraded — aggregate counts only, no item index) |
| Threat intel | kb.cert.org/vuls, attackerkb, hackerone/hacktivity, bugcrowd/disclosures, cve.org, cve.mitre.org, nvd.nist.gov, habr.com/tomhunter, teletype.in/cyberok | ✅ / ⚠️ (attackerkb/hackerone/bugcrowd/cve.org/cve.mitre.org JS or 403; habr/teletype degraded — last posts > 1 month old) |

**Errors:** cisa.gov + cisa.gov/known-exploited-vulnerabilities-catalog (403), attackerkb (403), msrc.microsoft.com/blog (empty), hackerone.com/hacktivity (JS), bugcrowd.com/disclosures (404), cve.org (JS), cve.mitre.org (JS redirect), cert.gov.ua (empty).
**Degraded:** packetstormsecurity.com (only aggregate counts), habr.com/ru/companies/tomhunter (last post March 2026), teletype.in/@cyberok (last post February 2026).
**CISA KEV:** No new additions confirmed in last 24h via mainstream relayers (cisa.gov direct continues to 403 via WebFetch).

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-30/night | Next: 2026-05-31/night*
