# Vulnerability Intelligence Report
**Date:** 2026-03-24 | **Cycle:** Night | **Generated:** 02:00 Europe/Athens

---

## Executive Summary

Four high-priority findings tonight. The standout is an extended-impact analysis of CVE-2026-32746, the pre-authentication root RCE in GNU InetUtils telnetd — a 32-year-old bug now confirmed present in FreeBSD, NetBSD, Citrix NetScaler, Apple macOS Tahoe, TrueNAS Core, Ubuntu, and Debian, with no patch until April 1. Citrix dropped a paired advisory (CVE-2026-3055 / CVE-2026-4368) for NetScaler ADC/Gateway, and a PoC for Wazuh Cluster deserialization RCE surfaced today. A significant update to the TeamPCP threat actor picture: the same infrastructure behind the Trivy supply chain attack is now being used to deploy a geofenced Iran-targeting wiper that destroys Kubernetes cluster nodes and local machines.

**Threat score range:** 7–8 | **Sources checked:** 31/31 | **Dedup suppressed:** 7

---

## Findings

---

### 1. CVE-2026-32746 — GNU InetUtils / BSD Telnetd Pre-Auth Root RCE — Blast Radius Extends to Citrix, FreeBSD, Apple, TrueNAS
**Threat Score:** 8/10 | **Type:** vuln | **CVSS:** 9.8 (Critical)

**What happened:** WatchTowr Labs published a detailed impact analysis today (PoC repo updated ~5 hours ago) revealing that CVE-2026-32746 — a BSS-based buffer overflow in the LINEMODE SLC negotiation handler of GNU InetUtils telnetd — is present in dozens of downstream projects, far beyond the originally-announced GNU InetUtils scope. An unauthenticated attacker connects to port 23 and, *before any login prompt*, sends a crafted SLC suboption with 40+ triplets, corrupting ~400 bytes of adjacent BSS memory and achieving arbitrary write primitives. Because telnetd typically runs as root under inetd/xinetd, successful exploitation yields root access.

**Confirmed affected beyond GNU InetUtils:**
- Ubuntu, Debian (all major versions)
- FreeBSD 13 / 15 Port
- NetBSD 10.1
- **Citrix NetScaler** (telnetd implementation based on same BSD codebase)
- Apple Mac Tahoe
- Haiku OS
- TrueNAS Core
- uCLinux
- libmtev (Circonus)
- DragonFlyBSD

**Timeline:** CVE first disclosed March 11, 2026 by Dream Security Research Team. Patch for GNU InetUtils expected **no later than April 1, 2026** — no patch yet available for downstream forks. WatchTowr notes "reliable RCE is difficult" due to binary protections on modern systems, but on legacy or IoT deployments it is more feasible. Censys data (March 18) shows ~3,362 exposed telnetd hosts on the internet.

**IOCs / References:**
- PoC: github.com/jeffaf/cve-2026-32746 (non-destructive, verifies via BSS leak)
- WatchTowr analysis: labs.watchtowr.com/a-32-year-old-bug-walks-into-a-telnet-server-gnu-inetutils-telnetd-cve-2026-32746/
- Dream advisory: dreamgroup.com/vulnerability-advisory-pre-auth-remote-code-execution-via-buffer-overflow-in-telnetd-linemode-slc-handler/
- Compare: CVE-2026-24061 (prior InetUtils auth bypass, now CISA KEV) showed similar exploitation timeline

**Remediation:**
1. **Disable telnetd immediately** if not required — use SSH instead
2. Block port 23 at firewall perimeter and host-based firewall
3. If telnetd is required: run without root privileges where possible
4. Watch for GNU InetUtils patch release (~April 1) and patch all downstream forks promptly
5. Citrix customers: monitor for NetScaler-specific advisory from Citrix

---

### 2. CVE-2026-3055 + CVE-2026-4368 — Citrix NetScaler ADC/Gateway Dual Advisory: Memory Leak + Session Hijack
**Threat Score:** 7/10 | **Type:** vuln | **CVSS:** 9.3 / 7.7

**What happened:** On March 23, Citrix published security bulletin CTX696300 covering two vulnerabilities affecting NetScaler ADC and NetScaler Gateway.

**CVE-2026-3055 (CVSS 9.3):** Out-of-bounds read in the SAML Identity Provider (SAML IDP) stack. An unauthenticated remote attacker can leak potentially sensitive information from the appliance's memory. Internally discovered by Citrix security review. Directly analogous to "CitrixBleed" (CVE-2023-4966). No known in-the-wild exploitation and no public PoC, but Citrix's history makes pre-emptive exploitation highly likely once PoC becomes available.

**CVE-2026-4368 (CVSS 7.7):** Race condition in appliances configured as Gateway (SSL VPN, ICA Proxy, CVPN, RDP Proxy) or AAA virtual server, leading to user session mixup. A low-privilege attacker can trigger the race and potentially access another user's authenticated session.

**Affected versions:**
- NetScaler ADC and NetScaler Gateway 14.1 before 14.1-66.59
- NetScaler ADC and NetScaler Gateway 13.1 before 13.1-62.23
- NetScaler ADC 13.1-FIPS and 13.1-NDcPP before 13.1-37.262
- Cloud-managed instances: NOT affected

**Configuration check for CVE-2026-3055 exposure:**
```
grep "add authentication samlIdPProfile" /nsconfig/ns.conf
```
If any results, patch immediately.

**Remediation:**
- Upgrade to 14.1-66.59 or 13.1-62.23 (or 13.1-37.262 for FIPS)
- Treat as emergency patching, particularly for CVE-2026-3055 (SAML IDP instances)
- Rapid7 InsightVM/Nexpose authenticated check expected in March 24 content release

---

### 3. CVE-2026-25769 — Wazuh Cluster Remote Code Execution via Insecure Deserialization
**Threat Score:** 7/10 | **Type:** vuln

**What happened:** Hakai Security (QuimeraX Intelligence) published a PoC exploit today (github.com/hakaioffsec/CVE-2026-25769, 30 stars, updated ~7 hours ago) for CVE-2026-25769, a Remote Code Execution vulnerability in the Wazuh cluster protocol. The vulnerability arises from insecure deserialization in the cluster communication stack — an attacker targeting Wazuh cluster ports can send a crafted payload to trigger arbitrary code execution.

Wazuh is a widely deployed open-source SIEM and XDR platform used across enterprise environments for security monitoring and incident response. Organizations running Wazuh in cluster mode are exposed; exploitation requires network access to the cluster communication port (TCP 1516 by default).

**Affected:** Wazuh (versions not fully specified in PoC readme; see upstream advisory GHSA-3gm7-962f-fxw5)
**CVE Reference:** cve.org/CVERecord?id=CVE-2026-25769

**Remediation:**
1. Review GHSA-3gm7-962f-fxw5 on github.com/wazuh/wazuh/security/advisories for fixed version
2. Restrict access to Wazuh cluster port 1516 to cluster member IPs only via firewall rules
3. Update to the patched version immediately
4. Monitor Wazuh logs for unexpected cluster connection attempts

---

### 4. [UPDATE] TeamPCP CanisterWorm → "TerrorPlant" Iran-Targeting Wiper Deployed via Trivy Infrastructure
**Threat Score:** 7/10 | **Type:** threat | **Update to:** 2026-03-22/night CanisterWorm finding

**What happened:** Over the past 48 hours, the same TeamPCP threat actor infrastructure used in the March 19 Trivy supply chain attack was leveraged to deploy a new geofenced wiper payload. The wiper (documented by Aikido Security researcher Charlie Eriksen) executes a destructive attack if the victim system's timezone corresponds to Iran or Farsi is set as the default locale.

**Wiper behavior:**
- If Iran timezone/Farsi detected AND system has access to a Kubernetes cluster: destroys ALL data on every node in the cluster
- If no Kubernetes access: wipes the local machine
- Deployed via the same compromised Trivy CI/CD infrastructure (force-pushed GitHub Actions tags)

**FortiGuard context (March 23):** Following U.S.-Israeli strikes on Iran, FortiGuard Labs reports no large-scale cyber retaliation observed yet, but regional cyber activity is rising. Organizations operating in or with ties to the Iran-Israel conflict theater should review exposure and credential hygiene, especially for cloud environments previously touched by Trivy.

**TeamPCP TTPs recap:**
- Targets: Exposed Docker APIs, Kubernetes clusters, Redis servers, React2Shell vuln
- Cloud focus: Azure (61%), AWS (36%) per Flare research
- C2: typosquatted scan.aquasecurtiy[.]org (note: deliberate typo)
- Data exfil: SSH keys, AWS/GCP/Azure creds, Kubernetes tokens, TLS private keys, crypto wallets, CI/CD secrets

**Action items:**
- Review all systems running Trivy for compromise indicators (check for ~/.config/systemd/user/sysmon.py, public GitHub repos named "tpcp-docs", C2 comms to scan.aquasecurtiy[.]org)
- Audit GitHub Actions workflows using trivy-action tags — verify all are pointing to known-good commits
- Rotate all secrets that may have been exposed in CI/CD pipelines
- Set timezone/locale checks are not a reliable defense; patch the root cause (remove compromised Trivy versions)
- Organizations in Iran-adjacent geopolitical context: heightened vigilance for destructive malware

---

## Noted (Below Threshold / Monitor)

| CVE | Product | CVSS | Note |
|-----|---------|------|------|
| CVE-2026-32954 | ERPNext ≤ 15.99.x / ≤ 16.7.x | 7.1 | Blind SQL injection via insufficient parameter validation. Fixed in 15.100.0 and 16.8.0. No exploitation reported. |
| CVE-2026-0828 | Safetica DLP + CVE-2025-7771 ThrottleStop | N/A | BYOVD PoC (28 stars, updated 3h ago) for Ring 0 process termination + physical memory R/W. Associated with MedusaLocker and EDR-killer patterns. Watch for ransomware operator adoption. |
| — | PEGA Infinity Platform | N/A | SEC Consult SA-20260317-0 discloses multiple vulns in PEGA Infinity. No CVE IDs or CVSS visible yet. PEGA is widely deployed BPM/CRM in financial sector. Monitor for advisories. |

---

## Source Coverage

| Tier | Sources | Status |
|------|---------|--------|
| 1 | bleepingcomputer, thehackernews, cisa.gov/kev, securityweek, rapid7, attackerkb, packetstorm, schneier, krebs, opencve | 9/10 OK (packetstorm ToS redirect) |
| 2 | nvd.nist.gov, cve.org, googleprojectzero, cloudflare blog, msrc blog, hackerone, bugcrowd, seclists, kb.cert.org, avleonov | 6/10 OK (msrc blank, hackerone/bugcrowd login, cert.gov.ua blank, cve.org blank) |
| 2 | 0xMarcio/cve (GitHub), dbugs.ptsecurity, habr/tomhunter, teletype/@cyberok, cert.gov.ua, github.com/search CVE, fortinet, securitylab.github, attackerkb | 9/11 OK |

**Total:** 31/31 sources attempted | 22 returned content | 9 failed/empty/login-required

---

## Intel Notes

- **Iran cyber situation:** FortiGuard and Krebs both reporting elevated activity following U.S.-Israeli strikes. No confirmed large-scale retaliation but defensive posture warranted for organizations in affected sectors.
- **Telnet exposure:** CVE-2026-32746 is a reminder that legacy protocols carry catastrophic risk. The Citrix NetScaler telnetd inclusion is particularly notable — organizations may not realize Citrix appliances run telnetd.
- **Supply chain hygiene:** TeamPCP activity demonstrates CI/CD pipeline compromise as a primary delivery vector. Verify all GitHub Actions pinning by commit SHA rather than mutable tags.
