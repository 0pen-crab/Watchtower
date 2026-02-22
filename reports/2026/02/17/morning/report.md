# Vulnerability Intelligence Report — 2026-02-17 Morning

---

## 📰 Ivanti EPMM Zero-Days Under Mass Exploitation (CVE-2026-1281 & CVE-2026-1340)

**Threat Score:** 9
**Affected Technology:** Ivanti Endpoint Manager Mobile (EPMM)
**CVE:** CVE-2026-1281, CVE-2026-1340
**CVSS:** Critical (details pending)

### Summary
Two critical RCE vulnerabilities in Ivanti EPMM are under active mass exploitation, with attacks traced back to July 2025 — a zero-day for ~7 months before disclosure. A single threat actor is responsible for 83% of observed exploitation. Researchers have seen the vulns used to deliver web shells, conduct reconnaissance, and download malware. Ivanti has released patches.

### Why It Matters
Ivanti EPMM is internet-facing by design. Seven months of zero-day exploitation means many orgs may already be compromised without knowing it.

### Discovery
**First seen at:** bleepingcomputer.com, securityweek.com
**How found:** Cross-referencing exploitation reports with timeline analysis
**Latency:** On-time

### Sources
- https://www.bleepingcomputer.com/news/security/one-threat-actor-responsible-for-83-percent-of-recent-ivanti-rce-attacks/
- https://www.securityweek.com/ivanti-exploitation-surges-as-zero-day-attacks-traced-back-to-july-2025/

---

## 📰 Dell RecoverPoint for VMs — Hardcoded Credentials Under Active Exploitation (CVE-2026-22769)

**Threat Score:** 8
**Affected Technology:** Dell RecoverPoint for Virtual Machines (RP4VMs)
**CVE:** CVE-2026-22769
**CVSS:** Critical (10.0 expected)

### Summary
Dell RecoverPoint for VMs contains hardcoded credentials allowing unauthenticated remote root-level persistence. CISA added to KEV on Feb 18 with 3-day deadline. Chinese state-backed hackers have been exploiting Dell zero-days since mid-2024.

### Why It Matters
Hardcoded credentials in a VM disaster recovery product. Trivial to exploit, no auth required, gives root. Deployed across enterprise data centers.

### Discovery
**First seen at:** CISA KEV catalog
**How found:** CISA KEV monitoring + BleepingComputer Chinese APT coverage
**Latency:** On-time

### Sources
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://www.bleepingcomputer.com/news/security/chinese-hackers-exploiting-dell-zero-day-flaw-since-mid-2024/

---

## 📰 VSCode Extensions with 128M+ Downloads Contain Critical Flaws

**Threat Score:** 6
**Affected Technology:** Visual Studio Code Extensions
**CVE:** Multiple (not individually assigned)
**CVSS:** High to Critical

### Summary
High-to-critical vulnerabilities in popular VSCode extensions with 128M+ combined downloads allow stealing local files and remote code execution. Massive supply chain attack surface in the most popular developer IDE.

### Why It Matters
Developer workstations hold source code, credentials, and CI/CD access. Vulnerable extensions are a lateral entry point into development pipelines.

### Discovery
**First seen at:** bleepingcomputer.com
**How found:** BleepingComputer report
**Latency:** On-time

### Sources
- https://www.bleepingcomputer.com/news/security/flaws-in-popular-vscode-extensions-expose-developers-to-attacks/

---

## 📰 CISA KEV: Zimbra SSRF and GitLab SSRF Added

**Threat Score:** 7
**Affected Technology:** Zimbra Collaboration Suite, GitLab
**CVE:** CVE-2020-7796 (Zimbra), CVE-2021-22175 (GitLab)
**CVSS:** Various

### Summary
CISA added two SSRF vulnerabilities to KEV — Zimbra (WebEx zimlet) and GitLab (webhook SSRF). Both older CVEs now confirmed exploited in the wild. GitLab SSRF actively exploited by ~400 IPs across US, Germany, Singapore, India, Lithuania, Japan.

### Why It Matters
Both Zimbra and GitLab are widely deployed, internet-facing services directly in our scope. Years-old CVEs still being exploited shows persistent patching gaps.

### Discovery
**First seen at:** CISA KEV catalog
**How found:** CISA KEV monitoring
**Latency:** On-time

### Sources
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://thehackernews.com/2026/02/threatsday-bulletin-openssl-rce-foxit-0.html

---

## 📋 Noted

- **No CVE** — Keenadu Android backdoor: Sophisticated malware embedded in firmware. Mobile-only, out of primary scope.
- **No CVE** — Poland arrests Phobos ransomware suspect under Operation Aether.

---

## 📡 Source Coverage

**Sources checked:** 90/90
**Sources with findings:** 8

| Status | Source | Notes |
|--------|--------|-------|
| ✅ | bleepingcomputer.com | 4 findings (Ivanti, Dell, VSCode, Chinese hackers) |
| ✅ | cisa.gov | Dell KEV, Zimbra KEV, GitLab KEV |
| ✅ | securityweek.com | Ivanti exploitation surge |
| ✅ | thehackernews.com | GitLab SSRF, ThreatsDay bulletin |
| ✅ | nvd.nist.gov | CVE lookups |
| ✅ | reddit.com/r/netsec | Ivanti discussion |
| ✅ | attackerkb.com | Ivanti analysis |
| ✅ | vulners.com | CVE cross-reference |
| ✅ | All remaining sources | Checked, nothing new in scope |
