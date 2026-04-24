# Watchtower Night Report — 2026-04-24
**Cycle:** Night | **Generated:** 2026-04-24 22:45 UTC (2026-04-24T22:45:00Z)
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

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/firestarter-malware-survives-cisco-firewall-updates-security-patches/) | [The Hacker News](https://thehackernews.com) | [SecurityWeek](https://www.securityweek.com)

---

### CVE-2026-32604 — Spinnaker Pre-Auth RCE via gitrepo Artifact Injection (CVSS 10.0)
**Product:** Spinnaker (CI/CD continuous delivery platform) | **CVE:** CVE-2026-32604 | **Status:** Patched, no confirmed exploitation

A critical command injection in Spinnaker's clouddriver pod allows a low-privilege user (any account able to configure artifacts via UI or API) to execute arbitrary commands on the underlying Spinnaker infrastructure. The flaw lives in the `gitrepo` artifact type: branch names and paths supplied by the user are not sanitized before being passed to shell-like operations, allowing trivial command injection. Spinnaker pipelines often hold deployment credentials for every cloud environment the organization runs in, so a single low-privilege account becomes a path to full cloud takeover.

**Timeline:** GitHub Security Advisory and patched releases published 2026-04-23. Publicly indexed in OpenCVE / dbugs.ptsecurity on 2026-04-24.

**Why it matters:** Spinnaker runs in enterprise CI/CD environments for Netflix, Airbnb, Adyen, and many financial institutions; the clouddriver pod holds AWS/GCP/Kubernetes service account tokens. The "low privilege" bar is typically met by any developer with pipeline write access — a lot of people.

**Mitigation:**
- Upgrade to Spinnaker 2026.1.0 / 2026.0.1 / 2025.4.2 / 2025.3.2 or later.
- If immediate upgrade is not possible, disable the `gitrepo` artifact type in clouddriver config.
- Audit audit logs for suspicious gitrepo artifact activity over the last 30 days.
- Rotate cloud service account credentials mounted in clouddriver if a compromise is suspected.

**Sources:** [dbugs.ptsecurity CVE-2026-32604](https://dbugs.ptsecurity.com) | [OpenCVE](https://app.opencve.io/cve/CVE-2026-32604)

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

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/bitwarden-cli-npm-package-compromised-to-steal-developer-credentials/) | [The Hacker News](https://thehackernews.com) | [SecurityWeek](https://www.securityweek.com)

---

### Zimbra XSS Mass Exploitation — 10,000+ Exposed Servers Vulnerable to CVE-2025-66376 (CVSS 7.2)
**Product:** Zimbra Collaboration Suite (ZCS) Classic UI | **CVE:** CVE-2025-66376 | **CVSS:** 7.2 | **Status:** Active Exploitation | KEV

BleepingComputer reported April 24 that over 10,000 internet-exposed Zimbra Collaboration Suite instances remain vulnerable to CVE-2025-66376, a stored XSS in the Classic UI triggered via CSS `@import` directives in HTML email bodies. Exploitation — initially linked to suspected Russian state actors targeting government mail servers — is ongoing across the long tail of unpatched deployments. Zimbra patched the issue in November 2025 (fixed in 10.0.18 and 10.1.13), and the CVE was added to CISA KEV in March 2026.

**Timeline:** Original patch November 2025 → CISA KEV March 2026 → BleepingComputer quantification of exposure April 24, 2026.

**Why it matters:** A simple HTML email delivers the exploit; no user interaction beyond opening the message. Zimbra Classic UI is the legacy default in many universities, ministries, and small enterprises — precisely the organizations slowest to patch. Mail server compromise yields credentials and pivots to Active Directory in typical deployments.

**Mitigation:**
- Upgrade Zimbra to 10.0.18, 10.1.13, or later immediately.
- Inventory internet-exposed ZCS hosts using Shodan / Censys and push laggards to the front of the patch queue.
- Switch users to the Modern UI where possible (not vulnerable to this specific flaw).
- Scan mail archives for inbound messages containing suspicious `@import` CSS directives.

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/) | [The Hacker News March coverage](https://thehackernews.com)

---

### CVE-2026-41248 — Clerk JavaScript Middleware Bypass Across Next.js / Nuxt / Astro (CVSS 9.1)
**Product:** @clerk/nextjs, @clerk/nuxt, @clerk/astro, @clerk/shared | **CVE:** CVE-2026-41248 | **CVSS:** 9.1 | **Status:** Patched, no confirmed exploitation

A middleware-routing flaw in Clerk's `createRouteMatcher` function — the middleware gate that decides whether a request requires authentication — can be bypassed with a crafted query string. Clerk is one of the most widely-deployed authentication-as-a-service providers for modern JavaScript frameworks, so a silent bypass in its Next.js / Nuxt / Astro SDKs directly exposes protected routes on any app that relies on `createRouteMatcher` without additional server-side authorization checks. No public PoC yet, but the advisory is unambiguous and mechanical.

**Mitigation:**
- Upgrade to patched versions: @clerk/astro ≥ 3.0.15 (also 1.5.7, 2.17.10), @clerk/nextjs ≥ 7.2.1 (also 5.7.6, 6.39.2), @clerk/nuxt ≥ 2.2.2 (also 1.13.28), @clerk/shared ≥ 4.8.1 (also 2.22.1, 3.47.4).
- Audit request logs for protected endpoints being hit via unusual query strings.
- Do not rely on middleware alone — add explicit authorization checks in each handler.

**Sources:** [GitHub Security Advisory](https://github.com/clerk) | [OpenCVE](https://app.opencve.io/cve/CVE-2026-41248)

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

### CVE-2026-41428 — Budibase Authentication Middleware Regex Bypass (CVSS 9.1)
**Product:** Budibase (low-code internal tool platform, versions < 3.35.4) | **CVE:** CVE-2026-41428 | **Published:** 2026-04-23

Budibase's authentication middleware uses an unanchored regular expression to determine whether an endpoint is public. An attacker can access any protected endpoint by appending the path of any public endpoint as a query parameter — for example, `POST /api/global/users/search?x=/api/system/status` successfully reaches the protected user search endpoint without authentication. No authentication, no user interaction, network-only. Budibase is commonly deployed as an internal tools platform holding HR, finance, and customer data.

**Mitigation:** Upgrade to Budibase 3.35.4 or later. Add WAF rule to strip query parameters resembling API paths from authentication decisions. Audit access logs for anomalous query-parameter patterns over the last week.

**Sources:** [GitHub Security Advisory GHSA-8783-3wgf-jggf](https://github.com/Budibase/budibase/security/advisories/GHSA-8783-3wgf-jggf)

---

### CVE-2026-41328 — Dgraph GraphQL Database Unauthenticated DQL Injection (CVSS 9.1)
**Product:** Dgraph (distributed graph database, versions < 25.3.3) | **CVE:** CVE-2026-41328 | **Published:** 2026-04-23

An unauthenticated attacker with network access to a Dgraph instance (default port 8080) can exfiltrate the entire database in default configurations (where Dgraph ACLs are disabled). The flaw is DQL injection through the language-tag field: `addQueryIfUnique` builds queries via `fmt.Sprintf` using the raw `pred.Lang` value. Two HTTP requests — one to `/alter` to create a schema predicate, one to `/mutate?commitNow=true` with the payload — are enough. Dgraph runs under many graph-backed knowledge apps and RAG pipelines.

**Mitigation:** Upgrade to Dgraph 25.3.3 or later. Enable Dgraph ACLs immediately (default-off is the dangerous configuration). Front Dgraph with an authenticating proxy if exposed beyond a trusted network.

**Sources:** [GitHub Security Advisory GHSA-x92x-px7w-4gx4](https://github.com/dgraph-io/dgraph/security/advisories/GHSA-x92x-px7w-4gx4)

---

## 📋 Noted / Monitoring

**CVE-2026-41478 — Saltcorn SQLi (CVSS 10.0)** — Vendor advisory GHSA-jp74-mfrx-3qvh now published; authenticated low-priv users can inject arbitrary SQL via mobile-sync routes in versions <1.4.6, 1.5.0-beta.0 through 1.5.5, 1.6.0-alpha.0 through 1.6.0-beta.4. Upgrade to 1.4.6 / 1.5.6 / 1.6.0-beta.5+.

**CVE-2026-21515 — Microsoft Azure IoT Central** — Critical vulnerability (CVSS 9.9) reported by PT Security; no vendor advisory or technical details published yet.

**CVE-2026-41473 — CyberPanel** — Web hosting control panel vulnerability (CVSS 8.8); limited details available, internet-facing by design.

**CVE-2026-2991 — KiviCare WordPress Plugin** — Authentication bypass via patient social-login REST endpoint in versions ≤4.1.2; PoC on GitHub.

**CVE-2026-31802 — npm tar** — Path traversal via symlink extraction enabling arbitrary file overwrite; supply chain implications for any pipeline using npm tar.

**CrowdStrike LogScale** — Critical vulnerability patched; no public technical details yet. Monitor for advisory.

**Tenable Nessus** — High-severity flaw patched; no public technical details. Monitor for advisory.

**VU#748485 — Central Office Services** — Unauthenticated configuration modification in Content Hosting Component; published April 23 by CERT/CC.

**CVE-2026-33193 — Docmost** — GitHub Security Lab GHSL-2026-052 (Man Yue Mo, Apr 24): Stored XSS via MIME type spoofing in the wiki/collaboration platform.

**CVE-2026-39351 — Frappe** — GitHub Security Lab GHSL-2026-012 (Man Yue Mo, Apr 24): Unauthorized data exposure via REST API link expansion; affects Frappe/ERPNext deployments.

**CVE-2026-41651 — PackageKit (Pack2TheRoot)** — Deutsche Telekom Red Team found a 12-year-old auth flaw in pkcon letting local users install packages and escalate to root (CVSS 8.8, Ubuntu/Debian/Rocky/Fedora). Local-only, but a useful lateral-movement primitive after initial foothold. Fixed in PackageKit 1.3.5.

**CVE-2026-32746 — GNU InetUtils telnetd** — Pre-auth buffer overflow RCE (CVSS 9.8) with active PoC on GitHub; sibling of previously-covered CVE-2026-24061.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/kev | ❌ (403 Forbidden) |
| Vendor advisories | rapid7.com, fortinet.com/blog, msrc.microsoft.com/blog, blog.cloudflare.com/tag/security | ✅ / ⚠️ |
| Research / OSINT | schneier.com, securitylab.github.com, projectzero.google, kb.cert.org/vuls, avleonov.com | ✅ |
| Supply chain / PoC | github.com/search, github.com/0xMarcio/cve, seclists.org/fulldisclosure, dbugs.ptsecurity.com | ✅ |
| Threat intel / CVE DB | opencve.io, nvd.nist.gov, habr.com/tomhunter, teletype.in/@cyberok, cert.gov.ua | ⚠️ |

**Errors:** cisa.gov (403), cisa.gov/kev (403), attackerkb.com (403), bugcrowd.com/disclosures (404), hackerone.com/hacktivity (JS-only), cve.org (JS-only), cve.mitre.org (redirects to cve.org)
**Degraded:** opencve.io home (marketing page only — app.opencve.io usable), nvd.nist.gov (no CVE data via WebFetch), msrc.microsoft.com/blog (JS-heavy), packetstormsecurity.com (redirected, ToS page only), teletype.in/@cyberok (stale content — latest post Feb 2026)
**CISA KEV:** Unable to check directly (403); no new KEV additions reported by secondary sources today.

---

*Watchtower vulnerability-researcher | Cycle: 2026-04-24/night | Next: 2026-04-25/night*
