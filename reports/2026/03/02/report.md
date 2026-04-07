# Watchtower Report — 2026-03-02 Night Cycle

**Generated:** 2026-03-02T02:00:00+02:00 (Europe/Athens)
**Sources checked:** 72/90 (16 unreachable, 6 degraded)
**New findings:** 4 | **Updates:** 1

---

## 🔄 Update: CVE-2026-20127 — Cisco Catalyst SD-WAN Exploited in the Wild

| Field | Value |
|---|---|
| **Threat Score** | 🔴 10 (↑ from 9) |
| **CVE** | CVE-2026-20127 |
| **Affected** | Cisco Catalyst SD-WAN Controller & Manager |
| **Status** | ACTIVELY EXPLOITED — CISA Emergency Directive ED-26-03 |

The auth bypass in Cisco Catalyst SD-WAN Controller/Manager is now confirmed exploited in the wild. Australian ACSC identified real-world attacks and published a hunt guide. Cisco Talos documented threat actor UAT-8616 chaining CVE-2026-20127 with CVE-2022-20775 — after gaining admin access via the auth bypass, attackers downgraded firmware to exploit the older privilege escalation for root access. CISA issued Emergency Directive ED-26-03 requiring all FCEB agencies to patch by February 27. All deployment types are affected: on-prem, Cisco-hosted cloud, managed cloud, and FedRAMP. No workaround available — upgrade is required.

**Action:** Patch immediately per Cisco advisory. Hunt for indicators of compromise per ACSC guide.

---

## 📰 Chrysalis Backdoor — Lotus Blossom APT Hijacked Notepad++ Update Infrastructure

| Field | Value |
|---|---|
| **Threat Score** | 🟠 8 |
| **CVE** | None |
| **Affected** | Notepad++ update delivery infrastructure |
| **Attribution** | Lotus Blossom (Chinese state-aligned APT) |

Rapid7 published detailed analysis of the Chrysalis backdoor, a previously undocumented implant deployed via compromised Notepad++ hosting infrastructure. The attackers did not compromise Notepad++ source code or build systems — they hijacked the hosting provider's update delivery pipeline, selectively redirecting traffic to deliver Chrysalis only to targeted victims. The attack persisted for months undetected. Lotus Blossom (active since 2009) primarily targets government, telecom, aviation, and critical infrastructure in Southeast Asia and Latin America. This incident highlights that supply chain risk now extends to update mechanisms and hosting providers beyond an organization's direct control.

**Action:** Verify Notepad++ installations against known-good hashes. Review update mechanisms for all software distributed via third-party hosting.

---

## 📰 QuickLens Chrome Extension — Supply Chain Compromise, Crypto Theft & ClickFix

| Field | Value |
|---|---|
| **Threat Score** | 🟠 7 |
| **CVE** | None |
| **Affected** | Chrome/Chromium browsers (QuickLens extension, ~7K users) |

The Google-featured QuickLens Chrome extension was sold on ExtensionHub (ownership transferred Feb 1, 2026) and backdoored in version 5.8 (pushed Feb 17). The malicious update:
- Strips CSP, X-Frame-Options, and X-XSS-Protection headers from all visited sites
- Communicates with C2 at `api.extensionanalyticspro[.]top` every 5 minutes
- Deploys ClickFix fake "Google Update" alerts on every page (domain: `google-update[.]icu`)
- Steals seed phrases from 11+ crypto wallets (MetaMask, Phantom, Coinbase Wallet, Trust Wallet, Solflare, etc.)
- Harvests login credentials, payment data, Gmail inbox, Facebook Business Manager, and YouTube channel data
- Windows payload signed by "Hubei Da'e Zhidao Food Technology Co., Ltd." drops `googleupdate.exe`

Extension removed from Chrome Web Store. IOCs: `api.extensionanalyticspro[.]top`, `google-update[.]icu`, `drivers[.]solutions`.

**Action:** Check for QuickLens installation. If found, assume credential and wallet compromise. Rotate all passwords and move crypto assets.

---

## 📰 Canadian Tire Data Breach — 38 Million Accounts

| Field | Value |
|---|---|
| **Threat Score** | 🟡 6 |
| **CVE** | None |
| **Affected** | Canadian Tire (retail, 38M customer accounts) |

Names, addresses, email addresses, phone numbers, and encrypted passwords were compromised. Limited details available at this time.

---

## 📰 South Korean National Tax Service Exposes Crypto Seed Phrase — $4.8M Stolen

| Field | Value |
|---|---|
| **Threat Score** | 🟡 5 |
| **CVE** | None |
| **Affected** | South Korean NTS (operational security failure) |

South Korea's National Tax Service published photos of a seized Ledger hardware wallet alongside its handwritten mnemonic recovery phrase during a press release about confiscating crypto from tax evaders. Within hours, an attacker deposited ETH for gas fees and exfiltrated 4 million PRTG tokens (~$4.8M) in three transactions. The press release has been removed. This incident serves as a stark reminder about seed phrase handling — anyone with the seed phrase has complete wallet control regardless of hardware, PINs, or permissions.

---

## Noted (Not Full Findings)

- **DoJ Tether seizure:** $61M in Tether seized linked to pig butchering scams
- **Iran internet shutdown:** Most severe in history, disrupted NIN domestic intranet and blocked Starlink
- **Gardyn Smart Gardens:** CISA IoT advisory (already noted Feb 28)

---

## Previously Reported (Confirmed Still Active)

- CVE-2026-21902 Juniper PTX RCE (Feb 28)
- ClawJacked OpenClaw WebSocket hijack (Mar 1)
- FreePBX 900+ web shell infections (Feb 28)
- Aeternum Blockchain C2 botnet (Feb 28)
- CVE-2025-25249 FortiOS heap overflow (Mar 1)
- CVE-2026-22153 FortiOS LDAP auth bypass (Mar 1)

---

## Source Coverage

| Status | Source | Notes |
|---|---|---|
| ✅ | nvd.nist.gov | No new critical CVEs |
| ✅ | cisa.gov/kev | CVE-2026-20127 added, ED-26-03 |
| ✅ | bleepingcomputer.com | QuickLens, Korean NTS seed |
| ✅ | thehackernews.com | ClawJacked (dedup), Gemini API (dedup), Rekoobe (dedup) |
| ✅ | securityweek.com | Canadian Tire, Claude Code Mexico (update angle) |
| ⚠️ | darkreading.com | 403 Cloudflare |
| ✅ | helpnetsecurity.com | Editorial only |
| ✅ | krebsonsecurity.com | Starkiller (dedup), Kimwolf (dedup) |
| ✅ | packetstormsecurity.com | No new specific disclosures |
| ⚠️ | reddit.com/r/netsec | Minimal content rendered |
| ✅ | reddit.com/r/cybersecurity | DNS mystery (info only) |
| ✅ | seclists.org/fulldisclosure | No standout new disclosures |
| ⚠️ | exploit-db.com | JS-rendered, minimal |
| ✅ | blog.talosintelligence.com | UAT-8616 SD-WAN report |
| ✅ | unit42.paloaltonetworks.com | IR report promo only |
| ✅ | fortinet.com/blog | Older campaigns (dedup) |
| ✅ | security.googleblog.com | Android theft protection |
| ⚠️ | msrc.microsoft.com | Minimal content |
| ✅ | blog.cloudflare.com | PQ transparency, DDoS Q4 |
| ✅ | projectzero.google | Windows Admin Protection series |
| ✅ | securitylab.github.com | No new advisories |
| ✅ | welivesecurity.com | PromptSpy (dedup), editorial |
| ⚠️ | blog.qualys.com | Minimal content |
| ✅ | rapid7.com | Cisco ITW update, Chrysalis |
| ✅ | schneier.com | Iran analysis, squid |
| ✅ | grahamcluley.com | Speaking schedule only |
| ⚠️ | crowdstrike.com/blog | Minimal content |
| ⚠️ | vulners.com | 403 |
| ✅ | isc.sans.edu | No new handlers diary |
| ✅ | cert.europa.eu | CVE-2026-20127 (dedup) |
| ✅ | abnormal.ai | Starkiller (dedup) |
| ❌ | x.com, t.me, discord.gg | Require auth |
| ❌ | 0day.today, threatpost.com, securityfocus.com | Defunct/restricted |
| ❌ | Various subscription sources | Require paid access |
