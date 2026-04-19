# Watchtower Night Report — 2026-04-19
**Cycle:** Night | **Generated:** 2026-04-19 06:00 UTC (2026-04-19T06:00:00Z)
**Sources checked:** 23/30 | **CISA KEV total:** N/A (403) | **New KEV additions:** N/A

---

## 🔴 CRITICAL

No critical findings today.

---

## 🟠 HIGH

### 📰 CVE-2026-41242 — Protobuf.js Code Injection RCE Affects Millions of Node.js Applications (CVSS 9.4)
**Product:** protobufjs (protobuf.js) | **CVE:** CVE-2026-41242 | **Status:** Patched | **CVSS:** 9.4

The most popular Protocol Buffers implementation for JavaScript/Node.js contains a critical code injection vulnerability. The library builds JavaScript functions from protobuf schemas by concatenating strings and executing them via the `Function()` constructor without validating schema-derived identifiers. Attackers can inject arbitrary code within protobuf "type" fields, achieving remote code execution whenever a vulnerable application decodes objects using a malicious definition. A minimal PoC exists and exploitation is described as "straightforward." Patches are available in versions 7.5.5 and 8.0.1.

**Timeline:** March 2 — vulnerability reported by Cristian Staicu (Endor Labs). March 11 — patch committed on GitHub. April 4 — npm fix for 8.x. April 15 — npm fix for 7.x. April 16 — GHSA published. April 18 — BleepingComputer public disclosure.

**Why it matters:** Protobuf.js is a foundational dependency across the Node.js ecosystem with massive transitive adoption — any server processing untrusted protobuf schemas is vulnerable. The attack surface includes gRPC services, microservice communication layers, and any application accepting user-supplied protobuf definitions. Supply chain risk is high because most consumers pull this as a transitive dependency and may not realize they're exposed.

**Discovered by:** Cristian Staicu (Endor Labs)

**Mitigation:**
- Upgrade protobufjs to >= 7.5.5 or >= 8.0.1 immediately
- Audit transitive dependencies (`npm ls protobufjs`) to identify all instances
- Never process untrusted protobuf schema definitions — treat schema-loading as untrusted input
- Prefer precompiled/static `.proto` schemas in production over dynamic loading

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/critical-flaw-in-protobuf-library-enables-javascript-code-execution/) | [GitHub Advisory GHSA-xq3m-2v4x-88gg](https://github.com/advisories/GHSA-xq3m-2v4x-88gg) | [dbugs.ptsecurity.com](https://dbugs.ptsecurity.com)

---

## 🟡 MEDIUM

No medium findings today.

---

## 📋 Noted / Monitoring

**CVE-2026-6518 — CMP WordPress Plugin (CVSS 8.8)** — Arbitrary file upload and RCE via improper validation of downloaded ZIP files in theme update functionality of CMP Coming Soon & Maintenance plugin. WordPress plugins are widely deployed but this is a niche maintenance plugin.

**CVE-2026-41253 — iTerm2 Code Execution (CVSS 6.9)** — iTerm2 processes SSH conductor protocol from untrusted terminal output sources, enabling code execution. Client-side only, but relevant for developer machine compromise chains.

**CVE-2026-40489 — EditorConfig-Core-C Stack Buffer Overflow (CVSS 8.6)** — Stack buffer overflow in glob function via crafted directory structures and .editorconfig files. Requires local access to directory structure.

**CVE-2026-35465 — SecureDrop Client File Overwrite (CVSS 7.5)** — Compromised SecureDrop server can exploit improper gzip filename validation to overwrite critical files on journalist workstations. Requires prior server compromise.

**Apache Airflow Multiple Authorization Issues (CVE-2026-30898 et al.)** — Five CVEs addressing authorization and information disclosure: improper variable redaction and DAG access controls. No RCE; authorization boundary issues in widely deployed ML pipeline platform.

**Nexcorium Mirai Variant UPDATE** — THN and FortiGuard published full analysis of Nexcorium targeting TBK DVRs (CVE-2024-3721) and EOL TP-Link routers. DDoS over UDP/TCP/SMTP with crontab/systemd persistence. IoT-focused; limited enterprise exposure.

**Metasploit Wrap-Up 04/17 — New RCE Modules** — Four new RCE exploit modules added: AVideo (SQLi chain), openDCIM (SQLi to RCE), ChurchCRM (file upload), and Selenium Grid/Selenoid instances. Selenium Grid is commonly exposed in CI/CD environments.

**Operation PowerOFF** — International law enforcement seized 53 DDoS-for-hire domains across 21 countries, arrested 4 individuals, and obtained 3M+ criminal user accounts. Warning communications sent to identified offenders.

**NIST CVE Enrichment Changes** — NIST now prioritizes CVE enrichment for CISA KEV entries, federal software flaws, and critical infrastructure vulnerabilities due to 263% surge in submissions. May slow enrichment for lower-priority CVEs.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | BleepingComputer, The Hacker News, SecurityWeek, Schneier, Krebs | ✅ |
| CISA / US Gov | cisa.gov, CISA KEV | ❌ (403 Forbidden) |
| Vendor advisories | Rapid7, Fortinet, Cloudflare, MSRC | ✅ / ⚠️ |
| Research / OSINT | GitHub CVE search, 0xMarcio/cve, dbugs.ptsecurity, seclists.org, NVD | ✅ / ⚠️ |
| Supply chain | GitHub Security Lab, PacketStorm | ✅ / ⚠️ |
| Threat intel | OpenCVE, CERT/CC, avleonov.com | ✅ / ⚠️ |
| Regional | CERT-UA, Habr/TomHunter, Cyberok, Project Zero | ⚠️ / ✅ |

**Errors:**
- cisa.gov / CISA KEV: 403 Forbidden (persistent)
- attackerkb.com: 403 Forbidden (persistent)
- bugcrowd.com/disclosures: 404 Not Found (persistent)
- hackerone.com/hacktivity: Requires JavaScript
- cve.org / cve.mitre.org: Requires JavaScript
- MSRC blog: Redirect, content not accessible
- CERT-UA: Empty content returned
- PacketStorm: Degraded (redirect to packetstorm.news, ToS page only)
- OpenCVE: Degraded (marketing page, no CVE data — requires app.opencve.io)
- NVD: Degraded (empty results page)

**CISA KEV:** Unable to access directly (403); no new KEV additions identified from secondary sources today.

---

*Watchtower vulnerability-researcher | Cycle: 2026-04-19/night | Next: 2026-04-20/night*
