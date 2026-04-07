# Vulnerability Intelligence Report — 2026-03-03 Night

---

## 📰 CISA Flags VMware Aria Operations RCE as Exploited in Attacks (CVE-2026-22719)

**Threat Score:** 9
**Affected Technology:** VMware Aria Operations (vRealize Operations)
**CVE:** CVE-2026-22719
**CVSS:** 8.1

### Summary
CISA added CVE-2026-22719 to KEV — a command injection vulnerability in VMware Aria Operations allowing unauthenticated RCE during support-assisted migration. Two additional flaws also patched: stored XSS (CVE-2026-22720) and privilege escalation to admin (CVE-2026-22721). Affects VMware Cloud Foundation, Telco Cloud, and standalone Aria Operations.

### Why It Matters
VMware Aria Operations is deployed in enterprise and telco environments for infrastructure monitoring. Unauthenticated RCE with CISA KEV designation means active exploitation — patch immediately.

### Discovery
**First seen at:** bleepingcomputer.com, thehackernews.com
**How found:** CISA KEV addition + simultaneous coverage
**Latency:** On-time

### Sources
- https://www.bleepingcomputer.com/news/security/cisa-flags-vmware-aria-operations-rce-flaw-as-exploited-in-attacks/
- https://thehackernews.com/2026/03/cisa-adds-actively-exploited-vmware.html

---

## 📰 Microsoft: Hackers Abuse OAuth Error Flows to Spread Malware

**Threat Score:** 7
**Affected Technology:** Microsoft OAuth / Azure AD
**CVE:** Not applicable (protocol abuse)
**CVSS:** N/A

### Summary
Attackers abuse legitimate OAuth redirection error mechanisms to bypass phishing protections in email and browsers, redirecting users to malicious pages that deploy malware. This bypasses URL scanning and email security because the OAuth URLs are from legitimate Microsoft domains.

### Why It Matters
OAuth abuse is a growing trend that bypasses traditional email and URL security controls. The technique uses Microsoft's own infrastructure as a trusted redirect, making detection extremely difficult.

### Discovery
**First seen at:** bleepingcomputer.com (Mar 3)
**How found:** BleepingComputer coverage of Microsoft report
**Latency:** On-time

### Sources
- https://www.bleepingcomputer.com/news/security/microsoft-hackers-abuse-oauth-error-flows-to-spread-malware/

---

## 📰 Android Patches Qualcomm Zero-Day Exploited in Attacks

**Threat Score:** 7
**Affected Technology:** Android (Qualcomm display driver)
**CVE:** Not specified
**CVSS:** High

### Summary
Google released security updates patching 129 Android vulnerabilities including an actively exploited zero-day in a Qualcomm display component. The flaw was used in targeted attacks before the patch.

### Why It Matters
While primarily mobile (edge of scope), Qualcomm chipset zero-days affect a massive install base and could be used to target executives' devices for espionage.

### Discovery
**First seen at:** bleepingcomputer.com (Mar 3)
**How found:** BleepingComputer coverage of Android Security Bulletin
**Latency:** On-time

### Sources
- https://www.bleepingcomputer.com/news/security/google-patches-android-zero-day-actively-exploited-in-attacks/

---

## 📰 Fake IT Support Deploys Havoc C2 — Lateral Movement in 11 Hours

**Threat Score:** 7
**Affected Technology:** Enterprise Windows environments
**CVE:** Not applicable
**CVSS:** N/A

### Summary
Huntress identified a campaign where attackers use email spam followed by fake IT support calls to deploy customized Havoc C2 framework payloads. In one case, the adversary moved from initial access to nine endpoints in 11 hours using custom Havoc Demon payloads and legitimate RMM tools, targeting data exfiltration or ransomware deployment.

### Why It Matters
11 hours from initial access to 9 endpoints is extremely fast lateral movement. The social engineering vector (fake IT support calls) bypasses technical controls entirely, making this a pure human-layer attack.

### Discovery
**First seen at:** thehackernews.com (Mar 3)
**How found:** Huntress research via The Hacker News
**Latency:** On-time

### Sources
- https://thehackernews.com/2026/03/fake-tech-support-spam-deploys.html

---

## 📋 Noted

- **No CVE** — LexisNexis: Data breach confirmed, hackers leaked stolen files. Legal/analytics data exposure.
- **No CVE** — Star Citizen (CIG): Game developer discloses breach affecting user data from January.
- **No CVE** — UH Cancer Center: Ransomware breach affects 1.2 million people. Healthcare impact.
- **No CVE** — AkzoNobel: Paint manufacturer confirms cyberattack on U.S. site.
- **No CVE** — CyberStrikeAI: Open-source AI security tool adopted by the FortiGate hacker for AI-powered attacks.

---

## 📡 Source Coverage

**Sources checked:** 90/90
**Sources with findings:** 6

| Status | Source | Notes |
|--------|--------|-------|
| ✅ | bleepingcomputer.com | VMware Aria, OAuth abuse, Android 0day, LexisNexis, AkzoNobel |
| ✅ | thehackernews.com | VMware Aria KEV, Havoc C2, CyberStrikeAI |
| ✅ | cisa.gov | VMware Aria KEV addition |
| ✅ | securityweek.com | Nothing new in scope |
| ✅ | nvd.nist.gov | CVE-2026-22719 |
| ✅ | All remaining sources | Checked, nothing new in scope |
