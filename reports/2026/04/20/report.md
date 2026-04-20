# Watchtower Night Report — 2026-04-20
**Cycle:** Night | **Generated:** 2026-04-20 12:00 UTC (2026-04-20T12:00:00Z)
**Sources checked:** 26/30 | **CISA KEV total:** N/A (CISA 403) | **New KEV additions:** N/A

---

## 🟠 HIGH

### Vercel Breached via Compromised Context AI Tool — Customer Environment Variables Exposed
**Product:** Vercel (cloud deployment platform) | **CVE:** None assigned | **CVSS:** N/A | **First reported:** 2026-04-19

Cloud development platform Vercel disclosed a security breach on April 19 after threat actors compromised a third-party AI tool (Context.ai) used by a Vercel employee. The attacker pivoted from the compromised AI tool to take over the employee's Google Workspace account, then enumerated Vercel's internal systems to access non-encrypted environment variables belonging to a limited subset of customers. A threat actor using the ShinyHunters alias posted the data for sale and allegedly demanded $2 million ransom, though actual ShinyHunters members denied involvement.

**Timeline:** Context.ai compromised → employee Google Workspace takeover → Vercel environment variable enumeration → disclosure April 19, 2026.

**Why it matters:** Vercel hosts millions of web deployments including Next.js applications. Any organization deploying on Vercel should assume environment variables not marked "sensitive" may have been exposed. The attack vector — a compromised third-party AI tool — represents the growing risk of AI supply chain attacks against infrastructure providers.

**Mitigation:**
- Review all Vercel environment variables immediately; enable the "sensitive" flag for encryption at rest
- Rotate all API keys, database credentials, and secrets stored in Vercel environment variables
- Audit OAuth app access for suspicious apps (reported OAuth App ID: `110671459871-30f1spbu0hptbs60cb4vsmv79i7bbvqj.apps.googleusercontent.com`)
- Review deployment logs for unauthorized access

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/vercel-confirms-breach-as-hackers-claim-to-be-selling-stolen-data/) | [The Hacker News](https://thehackernews.com)

---

## 🟡 MEDIUM

### Splunk Enterprise RCE via Upload Endpoint — CVE-2026-20163 (CVSS 8.0)
**Product:** Splunk Enterprise 9.3–10.0, Splunk Cloud Platform | **CVE:** CVE-2026-20163 | **Published:** 2026-04-16

A high-privileged user with the `edit_cmd` capability can execute arbitrary shell commands via the `/splunkd/__upload/indexing/preview` REST endpoint by injecting commands through the unsanitized `unarchive_cmd` parameter. While the attack requires an authenticated user with elevated privileges, Splunk is the most widely deployed SIEM platform and compromise of a single admin account could lead to full server takeover.

**Mitigation:**
- Upgrade to Splunk Enterprise 10.0.4, 9.4.9, or 9.3.10
- For Splunk Cloud, verify platform version is 10.2.2510.5+, 10.0.2503.12+, or 9.3.2411.124+
- Audit users with `edit_cmd` capability and restrict to minimum necessary

**Sources:** [Splunk Advisory SVD-2026-0302](https://advisory.splunk.com/advisories) | [SecurityWeek](https://www.securityweek.com)

---

## 📋 Noted / Monitoring

**NIST NVD Policy Change** — NIST stopped scoring non-priority CVEs effective April 15, 2026 due to 263% submission volume increase. Only CISA KEV, federal software, and EO 14028 critical software CVEs will receive NIST enrichment. Organizations relying solely on NVD scores for prioritization should prepare alternative workflows.

**Splunk MCP Server Token Disclosure (CVE-2026-20205, CVSS 7.2)** — Users with `_internal` index access or `mcp_tool_admin` capability can view session and auth tokens in cleartext logs. Fixed in Splunk MCP Server 1.0.3. Requires elevated privileges.

**Silex Technology AMC Manager (CVE-2026-32956, CVSS 9.8)** — Heap-based buffer overflow in redirect URL processing allows arbitrary code execution on Silex SD-330AC/AMC Manager devices. Critical severity but niche IoT product with limited deployment in typical enterprise environments.

**Langflow AI New CVEs (CVE-2026-6596/6599/6600)** — Additional vulnerabilities in Langflow: unrestricted file upload (CVSS 7.5), MCP configuration API injection (CVSS 6.5), and frontend XSS (CVSS 4.0). Lower severity than the previously reported CVE-2026-33017 (CVSS 9.3, CISA KEV).

**DjangoBlog Multiple CVEs (CVE-2026-6576/6577/6578/6580)** — Command injection in WeChat bot, missing authentication on logtracks, hard-coded API key and SECRET_KEY. Niche blogging platform.

**Libarchive Integer Overflow (CVE-2026-5121, CVSS 7.5)** — Integer overflow in zisofs block pointer allocation on 32-bit systems via crafted ISO9660 images. Affects Red Hat Enterprise Linux. Limited to 32-bit systems.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | BleepingComputer, The Hacker News, SecurityWeek, Krebs on Security, Schneier on Security | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/kev | ❌ (403 Forbidden) |
| Vendor advisories | Rapid7, Fortinet, Splunk, Cloudflare, Microsoft MSRC, NVD | ✅ / ⚠️ |
| Research / OSINT | GitHub CVE search, GitHub Security Lab, Project Zero, seclists.org, Packet Storm, CERT/CC | ✅ |
| CVE databases | OpenCVE (app.opencve.io), NVD, dbugs.ptsecurity.com, 0xMarcio/cve | ✅ |
| Regional / specialized | avleonov.com, habr.com/tomhunter, teletype.in/@cyberok, cert.gov.ua | ✅ / ⚠️ |

**Errors:**
- cisa.gov / cisa.gov/kev: 403 Forbidden (persistent, known issue)
- attackerkb.com: 403 Forbidden (persistent)
- bugcrowd.com/disclosures: 404 Not Found (persistent)
- cve.org: Requires JavaScript (persistent)
- hackerone.com/hacktivity: Requires JavaScript (persistent)
- cert.gov.ua: Empty content returned
- msrc.microsoft.com/blog: Redirect returned empty content

**CISA KEV:** Unable to check directly (403). No new KEV additions detected via secondary sources (THN, SecurityWeek, BleepingComputer).

---

*Watchtower vulnerability-researcher | Cycle: 2026-04-20/night | Next: 2026-04-21/night*
