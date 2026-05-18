# Watchtower Night Report — 2026-05-18
**Cycle:** Night | **Generated:** 2026-05-18 02:30 UTC (2026-05-18T02:30:00Z)
**Sources checked:** 20/30 | **CISA KEV total:** ~1,420 (KEV portal 403 via WebFetch — cross-checked via THN/SW) | **New KEV additions:** none confirmed since CVE-2026-20182 (Cisco SD-WAN) 2026-05-14 / CVE-2026-42897 (Exchange) 2026-05-16

---

## 🟠 HIGH

### Grafana Labs GitHub Codebase Theft — Pwn-Request workflow misconfig stolen tokens → 4 private repos pivoted → CoinbaseCartel (ShinyHunters/Scattered Spider/LAPSUS$ offshoot) extortion attempt refused
**Product:** Grafana Labs source repositories on GitHub (corporate, not customer-facing) | **CVE:** Not assigned (process incident, not a product CVE) | **CVSS:** N/A | **Status:** Disclosed 2026-05-16, source-code theft confirmed, ransom rejected, response from FBI engaged

Grafana Labs disclosed on 2026-05-16 that a recently-enabled GitHub Action workflow on a public Grafana repo contained a **Pwn Request** misconfiguration — `pull_request_target` triggered on forks, giving external contributors access to production secrets during CI runs. The attacker forked a Grafana repo, injected a curl payload that dumped runner environment variables to a file encrypted with the attacker's public key, then deleted the fork to cover tracks. With the harvested privileged GitHub token the attacker then replicated the workflow trigger against four additional private Grafana repos and downloaded their source code. Detection came from a **canary token** tripping inside the stolen credentials — defenders should note this as the working control. The attacker (attributed by Hackmanac/Ransomware.live to **CoinbaseCartel**, an offshoot of the ShinyHunters/Scattered Spider/LAPSUS$ ecosystem that emerged 2025-09) demanded payment to prevent publishing the codebase; Grafana refused and engaged the FBI. No customer data or production systems were impacted.

**Timeline:** Workflow enabled (recent, exact date not disclosed) → fork-and-inject attack → canary token tripped → IR + token rotation (mid-May 2026) → public disclosure 2026-05-16 → ransom rejection statement 2026-05-17.

**Why it matters:** This is the **same Pwn Request → pull_request_target → OIDC-token-theft chain** Endor Labs documented on 2026-05-13 as the root primitive of Mini Shai-Hulud Wave 2 (TanStack origin point). The Grafana incident proves the pattern is being reused by adjacent extortion crews against Grafana-class enterprise targets — observability, telemetry, and infrastructure-as-code vendors should treat this as a **branch-class** rather than incident-class signal. Two concrete asks for our environment: (1) inventory every public repo for `pull_request_target` workflows that access secrets and require maintainer approval for fork PRs; (2) deploy canary tokens inside CI runner secrets — the only thing that caught this incident was a canary, not gate-checking.

**Discovered by:** Grafana Labs security team (internal canary token trip); attribution to CoinbaseCartel by Hackmanac and Ransomware.live.

**Mitigation:**
- Audit all GitHub repos for `pull_request_target` workflows; if found, ensure they do NOT execute fork-supplied code with access to secrets.
- Enable "Require approval for first-time contributors" / "Require approval for all outside collaborators" on Actions for public repos.
- Deploy canary tokens (e.g., Thinkst Canarytokens, GitHub-issued tripwire credentials) inside CI runner environment-variable contexts as a tripwire for token exfiltration.
- Rotate any GitHub Apps / fine-grained PATs accessed through CI within the past 60 days as a precaution if you cannot fully audit workflow history.
- Cross-reference your private-repo download logs for unusual API call patterns from authorized tokens — the attacker used legitimate credentials.

**Sources:** [The Hacker News — Grafana GitHub Token Breach](https://thehackernews.com/2026/05/grafana-github-token-breach-led-to.html) | [StepSecurity Incident Analysis](https://www.stepsecurity.io/blog/grafana-github-actions-security-incident) | [Hackread — Ransom Refusal](https://hackread.com/grafana-source-code-theft-rejected-ransom-demand/)

---

## 🟡 MEDIUM

### Frigate NVR CVE-2026-25643 — config.yaml `exec:` directive command injection → go2rtc shell RCE on internet-exposed video-recorder appliances (CVSS 9.1)
**Product:** Frigate NVR ≤ 0.16.3 (local-object-detection network video recorder integrating with IP cameras and Home Assistant) | **CVE:** CVE-2026-25643 | **Published:** 2026-05-17 (CISA Vulnrichment + NVD)

Frigate's video-stream configuration parser passes user-supplied values from the `exec:` directive directly to the shell context used by the bundled `go2rtc` streaming service, with no escaping or allowlisting. An authenticated administrator — OR ANY UNAUTHENTICATED VISITOR ON A FRIGATE INSTANCE EXPOSED TO THE PUBLIC INTERNET WITHOUT AUTHENTICATION — can write a `config.yaml` payload that executes arbitrary system commands on the host. Public exploits and PoCs are already on GitHub (DyniePro/CVE-2026-25643 and jduardo2704/CVE-2026-25643-Frigate-RCE), both published within hours of the advisory. Patched in 0.16.4.

**Why it matters:** Frigate is widely deployed by both home-lab/SMB users (often misconfigured public-exposure) and by enterprises that run it as a low-cost local-vision layer in front of IP-camera fleets. The "admin OR no-auth" exploitation model is the same shape as numerous IoT/NVR mass-compromise campaigns (Hikvision, Dahua) — expect Shodan-driven mass scanning within days. Look for Frigate exposing port 5000 / 1984 on internet-facing IP space.

**Mitigation:**
- Upgrade to Frigate 0.16.4 immediately.
- If immediate upgrade is not possible: ensure Frigate is behind authenticated reverse proxy (nginx basic-auth, Authelia, Traefik forward-auth, etc.) — never expose to the internet directly.
- Restrict `config.yaml` write permissions; review admin-account scope.
- Hunt for unexpected go2rtc child processes or unusual shell invocations.

**Sources:** [NVD — CVE-2026-25643](https://nvd.nist.gov/vuln/detail/CVE-2026-25643) | [SentinelOne Vulnerability Database](https://www.sentinelone.com/vulnerability-database/cve-2026-25643/) | [PoC: DyniePro/CVE-2026-25643](https://github.com/DyniePro/CVE-2026-25643)

---

## 📋 Noted / Monitoring

**Apple iOS 26.5 / iPadOS 26.5 / macOS Tahoe 26.5 / Safari 26.5 release (2026-05-17, Full Disclosure)** — broad multi-OS security update; per Watchtower scope these are mobile / client-only and out of focus, but flagging here for awareness. Defenders responsible for managed Apple fleets should pull Apple support pages individually.

**Vim — multiple vimscript code injection (oss-security 2026-05-17)** — editor-side, requires opening untrusted modeline/script; client-only, but worth note for ops users running Vim on production hosts as root.

**Dovecot OXDC-2026-0002 (CVE-2026-40020 CVSS 3.1 + CVE-2026-42006 CVSS 4.3) — IMAP SETACL `anyone` ACL injection + imap-login memory-exhaustion DoS** — published 2026-05-05, re-disseminated to Full Disclosure 2026-05-17. Low severity; patched in OX Dovecot Pro core 3.1.5 / CE core 2.4.4.

**Chaotic Eclipse "MiniPlasma" Cloud Filter LPE PoC (2026-05-17, BleepingComputer)** — fifth Windows zero-day drop in the same Chaotic Eclipse disclosure spree (after BlueHammer CVE-2026-33825, RedSun, UnDefend, YellowKey, GreenPlasma). Abuses undocumented `CfAbortHydration` in `cldflt.sys`; LPE only (out of scope), but the spree itself is a calibration data point — researcher operates outside coordinated disclosure and consistently drops working PoCs.

**Tycoon2FA + Trustifi-URL device-code phishing campaign (BleepingComputer 2026-05-17)** — Microsoft 365 account takeover via device-code phishing using legitimate Trustifi URLs to defeat link reputation. Not a vuln; defenders should review device-code sign-in conditional-access policies and look for non-interactive `urn:ietf:params:oauth:grant-type:device_code` sign-ins.

**Secret Blizzard "Kazuar" backdoor evolved to modular P2P botnet (BleepingComputer 2026-05-16)** — Russian SVR-aligned actor transformed an existing backdoor into a P2P-resilient botnet for persistence; IOC value rather than a defensive priority.

**CVE-2026-8768 — Vercel AI SDK SSRF in download functionality (CVSS 7.3, ≤ 3.0.97)** — niche but in the AI-infra-tooling scope; if you use the Vercel AI SDK server-side, upgrade.

**CVE-2026-31222 / CVE-2026-31223 / CVE-2026-31224 — Snorkel library insecure-deserialization RCE via malicious model files (CVSS 8.8 each)** — joins the broad "ML library that uses pickle/torch.load() unsafely on user-supplied artifacts" pattern; not specifically exploited but ML/AI engineering teams should audit Snorkel-based pipelines.

**CVE-2026-31214 — ml-engineering unsafe `torch.load()` of untrusted PyTorch checkpoints (CVSS 9.8)** — generic instance of the well-known pickle-in-checkpoint pattern. Anchored under the AI-platform scope as an avoid-trusting-untrusted-model-artifacts reminder.

**CVE-2026-1184 (GitLab EE unauthenticated DoS via crafted uploads, CVSS 7.5) + CVE-2026-1322 (read_api OAuth scope creation bypass, CVSS 8.1) — patched in 18.9.7 / 18.10.6 / 18.11.3 (2026-05-14)** — internet-exposed GitLab instances should apply.

**CVE-2026-44501 — DataHub frontend unsafe-deserialization of Java objects via OIDC callback cookie (CVSS 7.1)** — DataHub metadata platforms exposing OIDC SSO at < 1.5.0.3 should patch.

**CVE-2024-39847 (4D Server SOAP XXE) + CVE-2024-13971 (Lobster Pro XXE) — re-published via Schutzwerk SA-2024-002 / SA-2024-005 on Full Disclosure 2026-05-17** — older 2024 advisories getting their public-write-up; niche enterprise software but worth a check if either is in your inventory.

**CVE-2026-46720 (Net::Statsd::Tiny metric injection, Perl < 0.3.8) + CVE-2026-8507/8721 (Crypt::OpenSSL::PKCS12 OOB write & NULL truncation, Perl ≤ 1.94) — oss-security 2026-05-17** — Perl-ecosystem niche; mention only because the metric-injection class has historically been used to poison Prometheus/Grafana dashboards.

**PT-2026-41513 (WordPress AI Engine plugin, CVSS 8.8, reported by Daroo) + PT-2026-41465 (WordPress backup/restore plugin, CVSS 8.8, reported by Murat Demirci)** — PT-Security dbugs published these 2026-05-17 ahead of the corresponding WPVulnDB/Patchstack entries; defenders running the AI Engine plugin (~100k installs; previously had CVE-2025-11749 MCP bearer-token exposure) should treat as second-round exposure and accelerate patching when published.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | BleepingComputer, The Hacker News, SecurityWeek, Krebs | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (403 via WebFetch) |
| Vendor advisories | MSRC blog, Fortinet, Rapid7, Cloudflare | ⚠️ MSRC (footer only); ✅ others |
| Research / OSINT | Schneier, Project Zero, Avleonov, GitHub Security Lab, openwall oss-security | ✅ |
| CVE feeds | NVD, OpenCVE (app), 0xMarcio/cve, dbugs.ptsecurity.com | ✅ |
| Mailing lists | Full Disclosure (seclists), openwall oss-security | ✅ |
| Bug bounty | HackerOne, Bugcrowd | ❌ (JS-only / 404) |
| RU-language | Habr Tom Hunter, Teletype CyberOK, CERT-UA | ⚠️ (no recent posts in window) |

**Errors:** cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403), attackerkb.com (403), packetstormsecurity.com (no content), cve.mitre.org (JS-only redirect), cve.org (JS-only), msrc.microsoft.com/blog (footer only via WebFetch), hackerone.com/hacktivity (JS-only), bugcrowd.com/disclosures (404), cert.gov.ua (header only)
**CISA KEV:** ~1,420 entries — no new additions verified in 2026-05-17→2026-05-18 window; last confirmed adds were CVE-2026-20182 (Cisco SD-WAN, 2026-05-14, 3-day deadline) and CVE-2026-42897 (Microsoft Exchange OWA, 2026-05-16, 21-day deadline 2026-06-06).

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-18/night | Next: 2026-05-19/night*
