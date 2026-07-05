# Watchtower Night Report — 2026-07-05
**Cycle:** Night | **Generated:** 2026-07-05 00:30 UTC (2026-07-05T00:30:00Z)
**Sources checked:** 26/30 | **CISA KEV total:** unreached (cisa.gov 403) | **New KEV additions:** none confirmed via BC/SW/THN cross-reference in 24h window; SharePoint CVE-2026-45659 BOD 26-04 FCEB deadline expired Saturday 2026-07-04

---

## 🔴 CRITICAL

### GNU inetutils-telnetd CVE-2026-24061 (CVSS 9.8) — Unauthenticated Remote Root via USER Env Var Injection; GreyNoise Confirms Active Mass Scanning, 212k+ Devices Exposed on Shodan
**Product:** GNU InetUtils `telnetd` (versions 1.9.3 through 2.7) | **CVE:** CVE-2026-24061 | **Status:** Patched (InetUtils 2.7-2 or later) | **Active Exploitation Confirmed | Public Mass Scanners on GitHub**

An unauthenticated remote attacker can obtain a root shell by exploiting unsafe handling of the `USER` environment variable transmitted through the NEW_ENVIRON telnet option (RFC 1572). The variable is interpolated into `/usr/bin/login`'s command line without validation, so a client that sets `USER=-f root` produces `/usr/bin/login -h <host> "-f root"` — the `-f` flag tells `login` to skip authentication and immediately hand over a root shell. No credentials, no user interaction, no prior system access required. GreyNoise telemetry cited by TXOne and CyCognito shows 18–21 unique scanning IPs within 24 hours of disclosure, escalating to 52 distinct source IPs across 16 countries. Public mass-exploitation frameworks are live on GitHub (`ekomsSavior/telnet_scan`, `Chocapikk/CVE-2026-24061`, SafeBreach Labs PoC). Shodan reports ~212,000 hosts running Telnet servers with roughly one million listening on port 23.

**Timeline:** Disclosure 2026-01-20 (Shivam Bathla / SafeBreach) → PoC + scanner published within 24 hours → GreyNoise observed 18–21 IPs day-1, expanding to 52 IPs across 16 countries → CISA KEV addition per reporting (date not independently confirmed — CISA.gov 403 blocked verification).

**Why it matters:** Telnet is a legacy protocol we should not still be seeing on the public internet, yet six-figure exposed footprint remains — heavily concentrated in embedded systems, OT/ICS bump-in-the-wire boxes, network appliances, and low-end SOHO gear that rarely receives firmware updates. This is a "trivial remote impact without credentials" scenario at scale with mature mass-tooling. Any host in our environment that exposes port 23 needs to be assumed compromised until proven otherwise; our third-party OT/ICS supply chain (managed service providers, industrial-network vendors) should be surveyed same-day.

**Discovered by:** Shivam Bathla (SafeBreach Labs).

**Mitigation:**
- Disable `telnetd` entirely and migrate to `sshd`. Telnet is plaintext regardless of this CVE and has no business on any production surface.
- If disabling is not immediately possible: upgrade GNU InetUtils to 2.7-2 or later.
- Firewall port 23 at every perimeter — internet-facing, DMZ boundary, and OT segmentation zones. Egress-block the port from workstation VLANs.
- Hunt syslog / auth.log for `telnetd` process entries and `login` invocations with `-f` in the arg vector for the last 90 days; treat any match as candidate compromise.
- Survey managed OT / ICS suppliers for exposure and demand attestation.
- Add GreyNoise or equivalent scanner-IP block-lists to perimeter deny rules.

**Sources:** [SafeBreach Labs — Root Cause Analysis & PoC Exploit for CVE-2026-24061](https://www.safebreach.com/blog/safebreach-labs-root-cause-analysis-and-poc-exploit-for-cve-2026-24061/) | [TXOne — Root via Telnet: Active Exploitation of CVE-2026-24061](https://www.txone.com/blog/cve-2026-24061-gnu-inetutils-telnet-exploitation/) | [SOC Prime — CVE-2026-24061 Detection Content](https://socprime.com/blog/cve-2026-24061-vulnerability/) | [GitHub — ekomsSavior/telnet_scan mass-exploitation framework](https://github.com/ekomsSavior/telnet_scan) | [GitHub — Chocapikk/CVE-2026-24061](https://github.com/Chocapikk/CVE-2026-24061)

---

## 🟠 HIGH

### PolinRider DPRK Supply-Chain Campaign — 108 Malicious Packages Across npm, Packagist, Go, Chrome; Compromised Maintainer Accounts + Git History Rewriting Push OmniStealer + DEV#POPPER
**Product:** developer tooling (npm, Packagist / Composer, Go modules, Chrome Web Store) | **CVE:** None assigned | **First reported:** 2026-07-04 (Socket.dev + The Hacker News)

Socket.dev published comprehensive coverage on 2026-07-04 of what it names the PolinRider campaign — a North Korea-linked supply-chain operation tied to the broader Contagious Interview / Famous Chollima cluster. Scope: 162 malicious release artifacts spanning 108 unique packages and extensions — **19 npm libraries, 10 Composer packages, 61 Go modules, and one Google Chrome extension.** Attackers abused compromised maintainer accounts on legitimate repositories to publish infected releases, and used **git history rewriting** (force pushes and anti-dated commits) to disguise malicious changes as old. Loaders reach out to blockchain / public RPC infrastructure (TRON, Aptos, BNB Smart Chain) to retrieve encrypted second-stage payloads, decrypt with embedded XOR keys, and execute via `eval()`. Observed follow-on payloads include DEV#POPPER and OmniStealer — capabilities span command execution, socket.io-based C2, credential theft, browser data theft, and cryptocurrency wallet exfiltration. Yesterday's report noted only a small Rollup polyfill subset in the Noted list; today's Socket.dev reveal establishes the campaign as far larger and structurally coherent, warranting promotion to a full News entry.

**Mitigation:**
- Push emergency SCA / package-audit scans against the 108-package Socket.dev IOC list; block the offending versions at the enterprise npm / Composer / Go proxy.
- Cross-check developer workstations, CI/CD runners, and build agents that resolved dependencies in the last 30 days against the Socket.dev IOC list; if any match, rebuild the host clean and rotate every secret the developer touched (SSH keys, cloud tokens, VPN creds, git access tokens, code-signing certificates).
- Enforce lockfile-only builds in CI — no unpinned installs from any registry. Fail the build on missing lockfile.
- Verify Chrome Web Store extension inventory against the listed IOC; managed-enterprise Chrome should push a policy allowlist rather than deny.
- Watch outbound network flows for TRON / Aptos / BNB Smart Chain RPC endpoints from developer hosts and CI runners; these are unusual on corporate egress and make good high-signal detection.
- Given git history rewriting: run `git fsck` and check for unusual forced-push events in the last 60 days against all managed repositories, and instrument for force-push events going forward.

**Sources:** [Socket.dev — PolinRider: North Korea-Linked Supply Chain Campaign Expands](https://socket.dev/blog/polinrider-north-korea-linked-supply-chain-campaign-expands) | [The Hacker News — North Korean Hackers Publish 108 Malicious Packages in PolinRider Campaign](https://thehackernews.com/2026/07/north-korean-hackers-publish-108.html) | [GBHackers — Hackers Compromise GitHub Maintainer Accounts to Publish PolinRider-Infected Package Versions](https://gbhackers.com/github-maintainer-accounts/)

---

## 🟡 MEDIUM

*(No new MEDIUM-tier news items in the 24-hour window — most cross-referenced items were already in the 30-day dedup index. See Noted for calibration items.)*

---

## 📋 Noted / Monitoring

**CVE-2026-31431 ("Copy Fail") 9-year-old Linux kernel LPE** — Theori Xint disclosed an LPE in a Linux kernel copy path present since 2017. Local elevation without a remote component — out of scope for our primary bulletins per the CLAUDE.md rules — but tracked because it may chain from any RCE we do care about (e.g. as post-exploit in Chrome-renderer-sandbox pivots). Multiple PoCs already surfaced on GitHub. Distro patch tracking in progress.

**CVE-2026-2472 — Google Cloud Vertex AI Python SDK unauthenticated stored XSS (versions 1.98.0 → 1.130.9)** — In-scope per our AI-platform advisory rule; landed on GitHub the same day. Client-side within the Vertex AI notebook / console UI, so blast radius is data-science workstations plus any web-front-end that renders Vertex artifacts unsanitized. Upgrade guidance pending from Google; interim mitigation is CSP and DOM-purify on any tenant tooling that surfaces Vertex-authored strings.

**CVE-2026-58451 — Horde Groupware IMP path traversal (seclists/fulldisclosure 2026-07-02)** — Email/collab platform, in scope. Post-only advisory with no technical detail beyond path traversal in IMP. Horde deployments should apply the current maintenance release; monitoring for downstream vendor advisories.

**Zig `std.http` chunked reader integer overflow → unauthenticated remote DoS (seclists/fulldisclosure 2026-07-02)** — Zig is not widely deployed in our surface; noted for calibration. Anyone shipping Zig-based HTTP frontends should upgrade.

**Kairos $1M extortion case study (Union County, OH June-2025 payment)** — Ransom-ISAC and CYJAX published deep-dive analysis on 2026-07-04 based on a leaked negotiation chat and blockchain forensics. Kairos is a *data-theft-only* extortion group — no encryptor, no locker, no decryption key. Calibration signal for our incident-response playbooks: model the negotiation and payment-decision surface for pure-exfil incidents distinctly from encrypt-and-extort ransomware.

**Avalon / CrownX modular malware framework — additional details** — Yesterday's noted entry now has expanded coverage: Rust-lifted browser data theft (Chromium + Firefox), DPAPI credential collection, VPN / SSH key theft, Wi-Fi profile exfil, targeted evasion against Defender / SentinelOne / CrowdStrike / Sophos / Elastic Endpoint / FortiEDR / ESET / McAfee / Bitdefender, delivered via Proton Drive password-protected ISO. Reporters note AI-assisted development signals in the tooling. Endpoint fleet impact — not primary infrastructure — but the DPAPI + browser-material collection is the exfil path most likely to intersect our SaaS session tokens.

**PamStealer macOS Rust infostealer** — Client-only, out of scope, noted for engineering-workstation calibration. Impersonates Maccy clipboard manager; validates victim password via PAM before capturing credentials.

**JADEPUFFER agentic-ransomware mainstream coverage on BleepingComputer 2026-07-04** — Delayed mainstream coverage of the Sysdig JADEPUFFER report already captured on 2026-07-03. No new technical detail vs. Sysdig's original; noted as latency calibration (mainstream lag ≈48h behind Sysdig / oss-security for this class of report).

**dbugs.ptsecurity.com 2026-07-04 batch (fresh medium/high severity)** — CVE-2025-71380 (n8n, CVSS 8.8), CVE-2026-14534 + CVE-2026-14535 (Fickling / Trail of Bits Python-pickle security tool, CVSS 8.8 each), CVE-2026-12195 (Vesta by MyVesta, CVSS 8.5), CVE-2026-12196 (HestiaCP, CVSS 8.3) plus 13x Picklescan issues at CVSS 8.1. Fickling / Picklescan are security-adjacent tools — worth watching for supply-chain-tooling risk but do not represent immediate ops action. Vesta / HestiaCP control panels are in-scope internet-facing infrastructure but detail is minimal — monitoring for vendor advisories.

**SharePoint CVE-2026-45659 FCEB deadline expired 2026-07-04** — Federal patch window closed Saturday. Any internet-facing SharePoint that missed the May patch + July 2 KEV addition should now be treated as candidate-compromised. Storm-2603 activity continues per Microsoft.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com, schneier.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/KEV | ❌ 403 (persistent) |
| Vendor advisories | msrc.microsoft.com/blog, fortinet.com/blog/threat-research, blog.cloudflare.com/tag/security, rapid7.com | ⚠️ (MSRC nav-only) / ✅ |
| Research / OSINT | github.com/search?q=CVE, github.com/0xMarcio/cve, projectzero.google, securitylab.github.com, attackerkb.com, kb.cert.org/vuls, avleonov.com, dbugs.ptsecurity.com, seclists.org/fulldisclosure, packetstormsecurity.com, opencve.io | ✅ / ⚠️ (P0/SLab silent) / ❌ (attackerkb 403) |
| CVE indices | nvd.nist.gov, cve.mitre.org, cve.org | ⚠️ (JS-required) |
| Bug bounty | hackerone.com/hacktivity, bugcrowd.com/disclosures | ⚠️ / ❌ 404 |
| Regional / Ru+UA | habr.com/ru/companies/tomhunter, teletype.in/@cyberok, cert.gov.ua | ⚠️ (silent) |

**Errors:** cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403), attackerkb.com (403), bugcrowd.com/disclosures (404) — all persistent per MEMORY.

**Degraded (attempted, empty / nav-only / silent):** msrc.microsoft.com/blog (nav-only), packetstormsecurity.com (redirect + terms only), securitylab.github.com (silent since 2026-05-22), opencve.io (marketing only), nvd.nist.gov (JS-required), cve.mitre.org (JS-required, redirects to cve.org), cve.org (JS-required), projectzero.google (silent since 2026-05-13), hackerone.com/hacktivity (JS-required), habr.com/ru/companies/tomhunter (silent since 2026-03-06 — 4.0-month silence), teletype.in/@cyberok (silent since 2026-02-04 — 5.0-month silence), cert.gov.ua (empty content).

**CISA KEV:** unreached (cisa.gov 403 persistent). Cross-referenced BC / SW / THN: no *new* KEV additions confirmed in the 24h window; SharePoint CVE-2026-45659 FCEB deadline expired 2026-07-04.

---

*Watchtower vulnerability-researcher | Cycle: 2026-07-05/night | Next: 2026-07-06/night*
