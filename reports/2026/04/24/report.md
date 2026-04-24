# Watchtower Night Report — 2026-04-24
**Cycle:** Night | **Generated:** 2026-04-24 03:45 UTC (2026-04-24T03:45:00Z)
**Sources checked:** 23/30 | **CISA KEV total:** N/A (cisa.gov unreachable) | **New KEV additions:** N/A

---

## 🔴 CRITICAL

### Firestarter Backdoor — Cisco ASA/FTD Firmware-Level Persistence Survives Patches (CISA+NCSC Joint Alert) (CVSS 9.9)
**Product:** Cisco Adaptive Security Appliance (ASA) / Firepower Threat Defense (FTD) | **CVE:** CVE-2025-20333, CVE-2025-20362 | **Status:** Active Exploitation | KEV

CISA and the UK NCSC issued a joint alert on April 24 warning that the threat actor UAT-4356 (ArcaneDoor) is deploying custom malware dubbed "Firestarter" on Cisco Firepower and Secure Firewall devices. The attack chain begins with exploitation of CVE-2025-20333 (missing authorization, CVSS 9.9) to deploy Line Viper, a shellcode loader that harvests admin credentials, certificates, and private keys via VPN sessions. Firestarter is then deployed as a persistent ELF backdoor that executes attacker-supplied shellcode via WebVPN requests.

**Timeline:** Compromise traced to early September 2025. CISA/NCSC joint alert issued April 24, 2026 (AR26-113A).

**Why it matters:** Cisco ASA/FTD devices are the perimeter firewall for a significant fraction of internet-facing networks globally. The malware survives firmware updates and security patches through LINA process hooking, boot file modification (`CSP_MOUNT_LIST`), self-restoration from hidden backup paths, and signal-triggered reinstallation. A cold reboot removes it but risks database corruption. The only reliable remediation is full device reimaging — this means potential downtime on internet-facing firewalls.

**Discovered by:** Cisco Talos (UAT-4356 tracking), CISA, UK NCSC

**Mitigation:**
- Run `show kernel process | include lina_cs` on all Cisco ASA/FTD devices — any output indicates compromise.
- Compromised devices: reimage and upgrade to fixed firmware releases immediately.
- Non-compromised devices: Cisco "strongly recommends" reimaging as a precaution.
- Do NOT rely on cold restart alone (risk of database/disk corruption).
- Apply YARA rules from CISA alert AR26-113A to disk images and core dumps.
- Rotate all credentials that transited the compromised devices (VPN, admin, certificates).

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/firestarter-malware-survives-cisco-firewall-updates-security-patches/) | [The Hacker News](https://thehackernews.com)

---

## 🟠 HIGH

### 🔄 TeamPCP Supply Chain Expands — Bitwarden CLI npm Package Compromised via Checkmarx GitHub Action
**Product:** @bitwarden/cli (npm) / Checkmarx CI/CD tooling | **CVE:** Not yet assigned | **CVSS:** N/A | **First reported:** 2026-03-26

TeamPCP, the North Korea–linked threat actor behind the LiteLLM, Trivy, and Checkmarx KICS supply chain compromises, has now pivoted through a compromised Checkmarx GitHub Action to inject a malicious version (2026.4.0) of the Bitwarden CLI package on npm. The package was live for approximately 90 minutes (April 22, 5:57–7:30 PM ET) and contained a loader (`bw_setup.js`) that stole npm tokens, GitHub tokens, SSH keys, and AWS/Azure/GCP credentials. Data was encrypted with AES-256-GCM and exfiltrated by creating public GitHub repositories under the victim's account. Critically, the malware self-propagates by using stolen npm credentials to inject malicious code into other packages the victim can publish.

**Mitigation:**
- If you installed `@bitwarden/cli@2026.4.0`, treat all systems and credentials as compromised.
- Rotate npm tokens, GitHub tokens, SSH keys, and cloud credentials immediately.
- Audit GitHub repositories for suspicious activity or unauthorized public repos.
- Review CI/CD pipelines for Checkmarx GitHub Action dependencies.
- Bitwarden confirms no end-user vault data was at risk.

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/bitwarden-cli-npm-package-compromised-to-steal-developer-credentials/) | [The Hacker News](https://thehackernews.com)

---

## 🟡 MEDIUM

### CVE-2026-33626 — LMDeploy Vision-Language Module SSRF Exploited Within 13 Hours of Disclosure (CVSS 7.5)
**Product:** LMDeploy (open-source LLM serving toolkit) | **CVE:** CVE-2026-33626 | **Published:** 2026-04-24

A server-side request forgery vulnerability in LMDeploy's vision-language module allows unauthenticated attackers to access cloud metadata services and internal networks. All versions through 0.12.0 are affected. Exploitation was observed within 13 hours of public disclosure, indicating automated scanning. LMDeploy is widely used for deploying large language models in production environments.

**Mitigation:** Upgrade LMDeploy to a patched version. If upgrade is not immediately possible, restrict network access to the vision-language API endpoint and block outbound requests to metadata services (169.254.169.254).

**Sources:** [The Hacker News](https://thehackernews.com)

---

### CVE-2026-25895 — FUXA SCADA HMI Unauthenticated Path Traversal to RCE (PoC Public)
**Product:** FUXA (web-based SCADA/HMI platform) | **CVE:** CVE-2026-25895 | **Published:** 2026-04-24

A public exploit (FUXAPWN) for CVE-2026-25895 was published on GitHub, chaining an unauthenticated path traversal with arbitrary file write to achieve remote code execution on FUXA SCADA HMI servers. FUXA is a web-based process visualization platform commonly exposed to the internet for remote monitoring. No patch information is available yet.

**Mitigation:** Remove FUXA instances from public internet exposure immediately. Apply network-level access controls. Monitor for the FUXAPWN exploit tool.

**Sources:** [GitHub](https://github.com/search?q=CVE-2026-25895)

---

## 📋 Noted / Monitoring

**CVE-2026-41478 — Saltcorn** — Critical flaw (CVSS 9.9) in open-source no-code database application builder; details from dbugs.ptsecurity.com only, awaiting vendor advisory.

**CVE-2026-21515 — Microsoft Azure IoT Central** — Critical vulnerability (CVSS 9.9) reported by PT Security; no vendor advisory or technical details published yet.

**CVE-2026-41473 — CyberPanel** — Web hosting control panel vulnerability (CVSS 8.8); limited details available, internet-facing by design.

**CVE-2026-2991 — KiviCare WordPress Plugin** — Authentication bypass via patient social-login REST endpoint in versions ≤4.1.2; PoC on GitHub.

**CVE-2026-31802 — npm tar** — Path traversal via symlink extraction enabling arbitrary file overwrite; supply chain implications for any pipeline using npm tar.

**CrowdStrike LogScale** — Critical vulnerability patched; no public technical details yet. Monitor for advisory.

**Tenable Nessus** — High-severity flaw patched; no public technical details. Monitor for advisory.

**VU#748485 — Central Office Services** — Unauthenticated configuration modification in Content Hosting Component; published April 23 by CERT/CC.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/kev | ❌ (403 Forbidden) |
| Vendor advisories | rapid7.com, fortinet.com/blog, msrc.microsoft.com/blog, blog.cloudflare.com/tag/security | ✅ / ⚠️ |
| Research / OSINT | schneier.com, securitylab.github.com, googleprojectzero.blogspot.com, kb.cert.org/vuls, avleonov.com | ✅ |
| Supply chain | github.com/search, github.com/0xMarcio/cve, seclists.org/fulldisclosure, dbugs.ptsecurity.com | ✅ |
| Threat intel | opencve.io, nvd.nist.gov, habr.com/tomhunter, teletype.in/@cyberok, cert.gov.ua | ⚠️ |

**Errors:** cisa.gov (403), cisa.gov/kev (403), attackerkb.com (403), bugcrowd.com/disclosures (404), hackerone.com/hacktivity (JS-only), cve.org (JS-only), cve.mitre.org (redirects to cve.org)
**Degraded:** opencve.io (marketing page only), nvd.nist.gov (no CVE data via WebFetch), msrc.microsoft.com/blog (JS-heavy, no content), packetstormsecurity.com (redirected, ToS page only), cert.gov.ua (JS-only)
**CISA KEV:** Unable to check directly (403); no new KEV additions reported by secondary sources today.

---

*Watchtower vulnerability-researcher | Cycle: 2026-04-24/night | Next: 2026-04-25/night*
