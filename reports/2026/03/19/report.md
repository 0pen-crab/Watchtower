# Watchtower — 2026-03-19 / Night Cycle

**Generated:** 2026-03-19 00:00 Athens (2026-03-18 22:00 UTC)  
**Sources checked:** 28 of 31 (3 unreachable, 9 degraded)  
**New findings:** 6 news · 1 update  

---

## 🔴 CRITICAL — IMMEDIATE ACTION REQUIRED

### 1. CVE-2026-20963 — Microsoft SharePoint RCE via Deserialization (CISA KEV, Deadline 2026-03-21)
- **Threat Score:** 9/10
- **CVSS:** High/Critical (NVD pending; network-accessible unauthenticated RCE)
- **EPSS:** 1.63% (81.7th percentile)
- **Affected:** Microsoft SharePoint on-premises (all unpatched versions)
- **Status:** Added to CISA KEV 2026-03-18 · **Patch due: 2026-03-21 (2 days from now)**

CISA added CVE-2026-20963 to the Known Exploited Vulnerabilities catalog with an emergency 3-day federal deadline. The vulnerability is a **deserialization of untrusted data** flaw in SharePoint that allows an **unauthenticated attacker over the network** to execute arbitrary code. CISA's confirmed exploitation status means in-the-wild attacks are already occurring.

**Action:** Apply Microsoft's security update immediately. If patching is not immediately possible, isolate SharePoint from untrusted networks and monitor for deserialization exploitation indicators. Treat as P0 with executive visibility.

---

## 🟠 HIGH PRIORITY

### 2. CVE-2025-32463 — Sudo chroot Privilege Escalation to Root (CVSS 9.3, EPSS 26.5%)
- **Threat Score:** 8/10
- **CVSS:** 9.3
- **EPSS:** 26.52% (96.3rd percentile — top 4% of all CVEs for exploitation probability)
- **Affected:** sudo 1.9.14 through 1.9.17 (all patch revisions) — Ubuntu, RHEL, SUSE, Debian, and most Linux distributions
- **PoC Status:** Multiple public PoCs, 950+ GitHub stars collectively since disclosure

Discovered by Rich Mirch at Stratascale, this vulnerability in sudo's `-R` (chroot) flag allows any user with sudo permissions to trivially obtain a **full root shell**. The attack is a one-liner: `sudo -R /tmp/woot woot` exploits a logic flaw in the `vbond_proc_challenge_ack_ack` state handler.

The EPSS score of 26.5% is extraordinary for a local privilege escalation — placing it in the 96th percentile for exploitation probability across all tracked CVEs. Three separate PoC repositories appeared within 24 hours of disclosure, with the leading repo already at 509 GitHub stars.

**Affected versions:** sudo 1.9.14, 1.9.14p1–p3, 1.9.15, 1.9.15p1–p5, 1.9.16, 1.9.16p1–p2, 1.9.17, 1.9.17p1-beta1  
**Fix:** Upgrade to sudo ≥ 1.9.17p1 (patched). Ubuntu, RHEL, SUSE packages available now.

**Action:** Check sudo version on all Linux systems. Prioritize servers with internet exposure or shared user access. Deploy patches via automated configuration management (Ansible/Chef/Puppet).

---

### 3. CVE-2026-3564 — ConnectWise ScreenConnect Signature Bypass, ASP.NET Machine Key Abuse Observed
- **Threat Score:** 8/10
- **CVSS:** Critical (vendor-rated; NVD pending)
- **EPSS:** 0.046% (low model score, but active exploit attempts observed)
- **Affected:** ConnectWise ScreenConnect on-premises < version 26.1

ConnectWise patched CVE-2026-3564 — a cryptographic signature verification bypass in ScreenConnect that enables session hijacking. Alongside the patch, researchers observed attempts to **abuse leaked/exposed ASP.NET machine keys** in the wild targeting ScreenConnect deployments. ScreenConnect is the platform of choice for many MSPs managing thousands of client endpoints, making it a high-value supply-chain attack vector.

Context: Chinese APT groups have previously weaponized ScreenConnect vulnerabilities (2024's CVE-2024-1709 was one of the most exploited CVEs of that year) to pivot into MSP client environments.

**Action:** Update all on-premises ScreenConnect instances to 26.1 immediately. Rotate ASP.NET machine keys. Review ScreenConnect access logs for anomalous session creation events since March 10, 2026.

---

## 🟡 MEDIUM PRIORITY

### 4. CVE-2025-66376 — Zimbra ZCS CSS @import XSS, Exploited in Wild (CISA KEV, Due 2026-04-01)
- **Threat Score:** 7/10
- **CVSS:** High (NVD pending)
- **EPSS:** 0.049% (low statistical score despite confirmed active exploitation)
- **Affected:** Synacor Zimbra Collaboration Suite (ZCS) Classic UI
- **KEV:** Added 2026-03-18, due 2026-04-01

Attackers are crafting HTML emails containing CSS `@import` directives that, when rendered in Zimbra's Classic UI, trigger cross-site scripting. This enables session token theft, credential harvesting, or payload delivery against Zimbra users who read malicious email in the Classic UI. CISA confirmation means active exploitation is underway.

**Action:** Apply Zimbra patch immediately. As a workaround, disable CSS imports in email rendering or migrate users from Classic UI to Modern UI (if available). Monitor Zimbra logs for unexpected session tokens or external CSS load attempts.

---

### 5. IP KVM Vulnerabilities (CVE-2026-32297, CVE-2026-32298) — Two Unfixed Critical Flaws in Angeet ES3 KVM
- **Threat Score:** 7/10
- **CVSS:** 9.8 (CVE-2026-32297, NO FIX); 8.8 (CVE-2026-32298, NO FIX)
- **Affected:** Angeet/Yeeso ES3 KVM (no patch available); GL-iNet Comet RM-1, Sipeed NanoKVM, JetKVM (fixes available)
- **CVEs:** CVE-2026-32290 through CVE-2026-32298 (9 total)

Researchers disclosed 9 vulnerabilities across four IP KVM vendors. The most dangerous are in the **Angeet/Yeeso ES3 KVM** for which **no patches exist**:

- **CVE-2026-32297** (CVSS 9.8): Missing authentication allows unauthenticated attacker to gain root access
- **CVE-2026-32298** (CVSS 8.8): Command injection via authenticated (low-privilege) access

IP KVM devices by design provide full physical-level console access to servers. An attacker compromising an IP KVM can effectively own the attached server regardless of OS-level controls.

**Action:** If Angeet/Yeeso ES3 KVM is deployed, immediately firewall the management interface to restrict access to jump hosts only, or air-gap it from networks pending vendor patch availability. For GL-iNet, Sipeed, and JetKVM — apply available updates.

---

### 6. Apple WebKit CVE-2026-20643 — Silent SOP Bypass Fix via New Background Security Improvements
- **Threat Score:** 6/10
- **CVSS:** High (Apple: "may allow remote attacker to break out of Web Content sandbox")
- **Affected:** iOS, iPadOS, macOS, Safari — all versions prior to Background Security Improvements update (2026-03-11)

Apple deployed its first-ever "Background Security Improvements" silent update to fix WebKit CVE-2026-20643 — a same-origin policy bypass allowing malicious web content to escape the Web Content sandbox. The update applied automatically without requiring user restart or explicit approval, marking a new Apple security delivery capability.

**Action:** Verify all managed Apple devices have received the update (Settings → General → About → check iOS version, or confirm BSI delivery via MDM). Corporate devices on older iOS versions that missed the BSI delivery should be updated via standard MDM patch.

---

## 🔁 THREAT INTELLIGENCE UPDATE

### 7. UPDATE: Interlock Ransomware Used Cisco FMC (CVE-2026-20131) as Zero-Day for 36 Days (Jan 26 → Mar 4)
- **Threat Score:** 9/10 (↑ from 8)
- **CVSS:** 10.0 (Critical)
- **Previous Coverage:** 2026-03-08 (Cisco FMC max-severity flaws)

Amazon/AWS threat intelligence has confirmed that the Interlock ransomware group was **actively exploiting CVE-2026-20131** (Cisco Secure Firewall Management Center remote Java code execution as root) as a **zero-day from January 26, 2026** — a full 36 days before Cisco's March 4 patch.

Cisco FMC instances that were internet-facing or reachable from compromised internal networks during this window should be treated as **potentially compromised**. The Interlock group used FMC access to enumerate managed firewall topologies, extract VPN credentials, and deploy ransomware laterally.

Fortinet's incident response report adds that Interlock has evolved its toolchain with new defense-evasion techniques since January.

**Action:** If Cisco FMC was deployed and unpatched before March 4, 2026, treat as a potential breach. Conduct forensic investigation of FMC configuration changes, administrator account activity, and any policy changes since January 26. Rotate all VPN/firewall credentials managed through the FMC.

---

## 📌 NOTED (Low Actionability / Out of Scope)

| CVE / Item | Product | Notes |
|---|---|---|
| CVE-2026-22812 | OpenCode IDE | Unauthenticated RCE, EPSS 2.64%; niche dev tool, limited enterprise exposure |
| CVE-2026-24769, CVE-2026-24768 | NocoDB | XSS + unvalidated redirect; GitHub Security Lab; no active exploitation |
| CVE-2025-26399 | SolarWinds Web Help Desk | CISA KEV added 2026-03-09, due 2026-03-12 (expired); late catch |
| DarkSword iOS Kit | State-sponsored iOS spyware | 6-vuln chain for full iOS compromise; targets individuals, not enterprise infra |
| WhatsApp View Once bypass #4 | Meta WhatsApp | Meta won't patch; modified client saves one-time media; OPSEC concern |

---

## 📊 Source Coverage

| Status | Count | Sources |
|---|---|---|
| ✅ OK | 19 | bleepingcomputer, thehackernews, cisa.gov/kev, krebsonsecurity, rapid7, fortinet, securitylab.github, seclists.org, opencve, schneier, googleprojectzero, cloudflare blog, talosintelligence, unit42, mandiant, attackerkb, first.org/epss, github.com/0xMarcio, github.com/advisories |
| ⚠️ Degraded | 9 | securityweek (403), packetstormsecurity (ToS), msrc blog (minimal), kb.cert.org/vuls (minimal), exploit-db (interface), crowdstrike (minimal), recordedfuture (minimal), cert.gov.ua (minimal), cve.org (minimal) |
| ❌ Unreachable | 3 | nvd.nist.gov (redirect loop), cisa.gov/alerts (404 — federal lapse), darkreading (403) |
