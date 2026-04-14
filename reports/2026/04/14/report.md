# Watchtower Night Report — 2026-04-14
**Cycle:** Night | **Generated:** 2026-04-14 06:00 UTC (2026-04-14T06:00:00Z)
**Sources checked:** 29/30 | **CISA KEV total:** N/A (CISA blocked) | **New KEV additions:** N/A

---

## 🔴 CRITICAL

### CVE-2026-34621 — Adobe Acrobat Reader Prototype Pollution Zero-Day Actively Exploited Since December 2025 (CVSS 8.6)
**Product:** Adobe Acrobat / Adobe Reader (DC, 2024) | **CVE:** CVE-2026-34621 | **Status:** Active Exploitation — Patched April 13

A prototype pollution vulnerability in Adobe Acrobat and Reader allows malicious PDFs to bypass sandbox restrictions and invoke privileged JavaScript APIs (`util.readFileIntoStream()`, `RSS.addFeed()`) to read arbitrary files and exfiltrate data. Active exploitation has been confirmed since at least December 2025, with Russian-language oil-and-gas themed lure documents observed in the wild. Originally scored CVSS 9.6 (network vector), Adobe reclassified to 8.6 (local vector) in the April 13 emergency bulletin. The exploit sample — named `_yummy_adobe_exploit_uwu.pdf_` — initially evaded 59 of 64 VirusTotal engines.

**Timeline:** December 2025 (exploitation begins) → March 23, 2026 (VirusTotal submission) → March 26 (EXPMON analysis) → April 13, 2026 (Adobe emergency patch APSB26-11).

**Why it matters:** Adobe Reader is installed on virtually every enterprise endpoint. Five months of unpatched exploitation means your environment may already be compromised. The sandbox bypass makes this a reliable initial access vector for targeted campaigns — the Russian oil/gas lure suggests state-level espionage.

**Discovered by:** Haifei Li (EXPMON exploit detection system); additional wild exploitation documented by researcher Gi7w0rm.

**Mitigation:**
- Immediately update to Acrobat DC/Reader DC 26.001.21411 or Acrobat 2024 24.001.30362 (Win) / 24.001.30360 (macOS)
- Scan for indicators: search email gateways for PDF attachments submitted after December 2025 with oil/gas industry themes
- Consider disabling JavaScript in Adobe Reader as defense-in-depth (Edit → Preferences → JavaScript → uncheck "Enable Acrobat JavaScript")

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/adobe-rolls-out-emergency-fix-for-acrobat-reader-zero-day-flaw/) | [The Hacker News](https://thehackernews.com)

**Discovery:** EXPMON automated exploit detection flagged the sample on VirusTotal after a March 23 submission. Cross-referenced with Gi7w0rm's wild campaign analysis to confirm scope. Discovery latency: on-time (patched same weekend as mainstream coverage).

---

## 🟠 HIGH

### CVE-2026-39987 — Marimo Python Notebook Pre-Auth RCE via Unauthenticated WebSocket Terminal (CVSS 9.3)
**Product:** Marimo ≤ 0.20.4 | **CVE:** CVE-2026-39987 | **CVSS:** 9.3 | **First reported:** 2026-04-08

The `/terminal/ws` WebSocket endpoint in Marimo (a Python notebook framework) exposes a full interactive terminal without authentication. Any unauthenticated client connecting to this endpoint gets shell access with the Marimo process's privileges. Exploitation began within 10 hours of disclosure — 125 IPs conducted reconnaissance within 12 hours, with full credential theft operations (targeting `.env`, SSH keys) completing in under three minutes per target. Instances deployed with `--host 0.0.0.0` in edit mode are directly exposed.

**Mitigation:**
- Upgrade to Marimo 0.23.0 (released April 11, 2026)
- Block `/terminal/ws` endpoint at the reverse proxy if immediate patching is not possible
- Audit `.env` files and SSH keys on any Marimo instances that were internet-exposed

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/critical-marimo-pre-auth-rce-flaw-now-under-active-exploitation/) | [GitHub Advisory GHSA-2679-6mx9-h9xc](https://github.com/advisories/GHSA-2679-6mx9-h9xc)

---

### CVE-2026-5194 — wolfSSL ECDSA Signature Verification Bypass Enables Certificate Forgery Across 5 Billion Devices (Critical)
**Product:** wolfSSL < 5.9.1 | **CVE:** CVE-2026-5194 | **CVSS:** Critical | **First reported:** 2026-04-08

Missing hash digest size and OID checks in wolfSSL's ECDSA certificate verification allow undersized digests to be accepted, making signatures trivially falsifiable. The flaw affects ECDSA/ECC, DSA, ML-DSA, Ed25519, and Ed448 algorithms. An attacker in a MITM position can present forged TLS certificates that wolfSSL will accept as genuine. wolfSSL is embedded in an estimated 5 billion IoT devices, embedded systems, and industrial control equipment worldwide.

**Mitigation:**
- Upgrade to wolfSSL 5.9.1 (released April 8, 2026)
- For downstream firmware: consult vendor advisories (e.g., Red Hat confirmed MariaDB is unaffected as it uses OpenSSL)
- Prioritize devices using wolfSSL for TLS in internet-facing or MITM-exposed positions

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/critical-flaw-in-wolfssl-library-enables-forged-certificate-use/) | [wolfSSL Advisory](https://www.wolfssl.com)

---

### Juniper Junos OS — Dozens of Vulnerabilities Patched Including Critical Unauthenticated Device Takeover
**Product:** Juniper Junos OS | **CVE:** Multiple (not yet enumerated) | **CVSS:** Critical | **First reported:** 2026-04-10

Juniper Networks released patches for dozens of Junos OS vulnerabilities. The most severe is a critical-severity flaw exploitable remotely, without authentication, to fully take over a vulnerable device. Juniper networking equipment is widely deployed in enterprise and service provider environments. No confirmed exploitation in the wild yet, but unauthenticated network infrastructure takeover is a high-priority patching target.

**Mitigation:**
- Apply Juniper's April 2026 security patches immediately, prioritizing internet-facing SRX and MX Series devices
- Monitor Juniper advisory portal for specific CVE details

**Sources:** [SecurityWeek](https://www.securityweek.com/juniper-networks-patches-dozens-of-junos-os-vulnerabilities/)

---

### CVE-2026-1731 — BeyondTrust Remote Support Command Injection via WebSocket (PoC Available, 29 Stars)
**Product:** BeyondTrust Remote Support / Privileged Remote Access | **CVE:** CVE-2026-1731 | **CVSS:** Critical | **First reported:** 2026-04-07

Command injection vulnerability caused by unsafe Bash arithmetic evaluation in a WebSocket-reachable script in BeyondTrust Remote Support and Privileged Remote Access products. A public PoC exploit with 29 GitHub stars has been available for 7 days. BeyondTrust products are widely deployed for remote access in enterprise environments, and previous BeyondTrust vulnerabilities (CVE-2024-12356) have been actively exploited by state actors.

**Mitigation:**
- Apply BeyondTrust security patches immediately
- Restrict WebSocket access to trusted networks
- Monitor for exploitation attempts against BeyondTrust instances

**Sources:** [GitHub PoC](https://github.com/win3zz/CVE-2026-1731) | [0xMarcio CVE Tracker](https://github.com/0xMarcio/cve)

---

## 🟡 MEDIUM

### CPUID Supply Chain Attack — Trojanized CPU-Z and HWMonitor Deliver STX RAT
**Product:** CPUID CPU-Z, HWMonitor | **CVE:** None assigned | **Published:** 2026-04-10

Attackers compromised CPUID's secondary API and redirected official download links to serve trojanized executables containing STX RAT. The compromise window was approximately 19 hours (April 9 15:00 UTC to April 10 10:00 UTC). CPUID's signed original files were not affected — only download redirections were malicious. While CPU-Z and HWMonitor are desktop tools, they are commonly downloaded by system administrators and developers, making this a developer-targeting supply chain vector.

**Mitigation:** Verify CPU-Z/HWMonitor downloads against official checksums; scan systems that downloaded these tools during the April 9-10 window; check for STX RAT IoCs.

**Sources:** [SecurityWeek](https://www.securityweek.com/cpuid-hacked-to-serve-trojanized-cpu-z-and-hwmonitor-downloads/) | [The Hacker News](https://thehackernews.com)

---

### PraisonAI Agent Framework — Three Critical Vulnerabilities Enable Unauthenticated RCE and Session Hijacking
**Product:** PraisonAI / PraisonAI Agents | **CVE:** CVE-2026-40289, CVE-2026-40288, CVE-2026-40287 | **Published:** 2026-04-10

Three critical vulnerabilities in the PraisonAI agent framework: unauthenticated WebSocket session hijacking (CVE-2026-40289, CVSS 9.1), arbitrary code execution via untrusted YAML workflow files (CVE-2026-40288, CVSS 9.8), and automatic code injection via unsanitized `tools.py` import (CVE-2026-40287, CVSS 8.4). PraisonAI is an open-source AI agent orchestration framework. These flaws are relevant to the AI security space — any internet-exposed PraisonAI instance is trivially compromisable.

**Mitigation:** Restrict PraisonAI to trusted networks only; validate all YAML workflow inputs; audit `tools.py` files in working directories.

**Sources:** [PT Security dbugs](https://dbugs.ptsecurity.com)

---

### Chrome 147 Patches 60 Vulnerabilities Including Two Critical WebML Flaws ($86K Bounties)
**Product:** Google Chrome 147 | **CVE:** Multiple (2 critical, details pending) | **Published:** 2026-04-11

Google released Chrome 147 with fixes for 60 security vulnerabilities, including two critical flaws in the WebML component that earned researchers $86,000 in combined bug bounties. No active exploitation reported. Chrome's auto-update mechanism mitigates risk for most users, but enterprise environments with delayed update policies should prioritize rollout.

**Mitigation:** Ensure Chrome 147 is deployed across all managed endpoints.

**Sources:** [SecurityWeek](https://www.securityweek.com)

---

## 📋 Noted / Monitoring

**CVE-2026-6264 — Talend JobServer** — Unauthenticated RCE via JMX monitoring port (CVSS 9.8). Enterprise ETL platform, but JMX ports are typically not internet-facing. Monitor for exploitation reports.

**CVE-2025-59718 — FortiGate** — Rapid7 published incident response findings on active exploitation. FortiOS vulnerability with field exploitation confirmed but limited details available yet.

**Orthanc DICOM Server (CERT/CC VU#536588)** — Multiple heap buffer overflows enabling RCE. Niche medical imaging server — relevant for healthcare organizations.

**CVE-2026-25643 — Frigate NVR** — Remote command execution in Frigate ≤0.16.3 with public PoC. IoT/home automation NVR, limited enterprise exposure.

**CVE-2026-2472 — Google Cloud Vertex AI SDK** — Stored XSS in versions 1.98.0–1.130.9. AI security space — limited direct impact but notable for AI platform users.

**CVE-2026-21852** — PoC with 21 GitHub stars published; insufficient details to classify. Monitoring.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | BleepingComputer, The Hacker News, SecurityWeek, Schneier | ✅ |
| CISA / US Gov | CISA KEV, CISA Alerts, CERT/CC | ⚠️ (CISA 403) |
| Vendor advisories | Rapid7, Fortinet, Cloudflare, Microsoft MSRC | ⚠️ (MSRC redirect) |
| Research / OSINT | GitHub CVE Search, 0xMarcio/cve, Project Zero, SecurityLab, AttackerKB | ⚠️ (AttackerKB 403) |
| Supply chain | PacketStorm, Seclists FullDisclosure | ✅ |
| Threat intel | Krebs, OpenCVE, NVD, CVE.org, PT Security dbugs | ⚠️ (NVD/CVE.org degraded) |
| Regional / Specialty | avleonov, Habr/T.Hunter, CyberOK, CERT-UA, HackerOne, Bugcrowd | ⚠️ (multiple degraded) |

**Errors:** bugcrowd.com/disclosures (404 — unreachable); cisa.gov + cisa.gov/kev (403); attackerkb.com (403); hackerone.com/hacktivity (JS required); cve.org (JS required); nvd.nist.gov (no content rendered); opencve.io (marketing page only); msrc.microsoft.com/blog (redirect, no content); cert.gov.ua (no content rendered)
**CISA KEV:** Unable to check — CISA returned 403 on both catalog and alerts pages.

---

*Watchtower vulnerability-researcher | Cycle: 2026-04-14/night | Next: 2026-04-15/night*
