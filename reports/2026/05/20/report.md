# Watchtower Night Report — 2026-05-20
**Cycle:** Night | **Generated:** 2026-05-20 00:00 UTC (2026-05-20T00:00:00Z)
**Sources checked:** 19/30 | **CISA KEV total:** unverified (KEV catalog 403 via WebFetch) | **New KEV additions:** unverified

---

## 🔴 CRITICAL

### Drupal Core Highly Critical Patch SA-CORE-2026-004 — Pre-announced via PSA, Released 2026-05-20 (NIST score 20/25)
**Product:** Drupal core (11.3.x / 11.2.x / 10.6.x / 10.5.x; 8.9 / 9.5 manual patches) | **CVE:** Not yet published | **Status:** Patch dropping today between 17:00-21:00 UTC

Drupal Security Team published a Public Service Announcement (PSA-2026-05-18) on 2026-05-18 warning that an upcoming highly critical core release on 2026-05-20 fixes a vulnerability scoring **20/25 on NIST's standard scoring methodology** — trivially easy to exploit, no privilege level required, capable of making all non-public data accessible and modifiable. Not all configurations are affected. The Drupal team has explicitly told site operators that "exploits may be developed within hours or days" of patch publication; no CVE assignment is published until the patch ships. Patches will be released for Drupal versions 11.3.x, 11.2.x, 10.6.x and 10.5.x; manually-applied patches will also be provided for end-of-life 8.9 and 9.5 — the inclusion of EOL branches is itself a signal of severity.

**Timeline:** PSA released 2026-05-18 → patches scheduled 2026-05-20 17:00-21:00 UTC → exploit development expected within hours/days of patch.

**Why it matters:** Drupal powers a long tail of high-traffic government, education, and enterprise sites (drupal.gov, drupal.org's own customer set across federal/.edu/.org). Score 20/25 on a CMS pre-announcement places this in the same defensive tier as the 2018 Drupalgeddon (CVE-2018-7600) — same playbook of "patch on the day; expect automated mass exploitation 24-72h later." Any Drupal site that is internet-facing, including marketing sites and intranet portals fronted by CDN, is in scope.

**Discovered by:** Not disclosed pre-release (standard Drupal Security Team practice).

**Mitigation:**
- Plan ~30-60 minute maintenance window on 2026-05-20 17:00-21:00 UTC; have on-call resources ready when the SA-CORE-2026-004 advisory drops.
- For 8.9 and 9.5 sites: prepare manual patch-application process (these branches are EOL — strongly consider an upgrade path to 10.6 or 11.3 as the long-term answer).
- After patching, monitor web access logs for the next 14 days for the exploitation indicators that will surface once the advisory ships.
- If patching is delayed: pull the site behind an authenticated reverse proxy or WAF until patched — assume mass-scanning within 72h.

**Sources:** [Drupal PSA-2026-05-18](https://www.drupal.org/psa-2026-05-18) | [The Hacker News](https://thehackernews.com/2026/05/drupal-to-release-urgent-core-security.html) | [SecurityWeek](https://www.securityweek.com/drupal-to-patch-highly-critical-vulnerability-at-risk-of-quick-exploitation/) | [The Register](https://theregister.com/patches/2026/05/19/drupal-warns-admins-to-brace-for-highly-critical-core-patch/5242728)

---

### SEPPMail Secure E-Mail Gateway — CVE-2026-2743 Path-Traversal RCE (CVSS 10.0) + CVE-2026-44125 Missing-Authz (CVSS 9.3) + CVE-2026-7864 Info Leak (CVSS 6.9)
**Product:** SEPPMail Secure E-Mail Gateway (User Web Interface, GINA UI) | **CVE:** CVE-2026-2743, CVE-2026-44125, CVE-2026-7864 | **Status:** Patched (15.0.4) — no in-the-wild reports yet

InfoGuard Labs disclosed three critical-class vulnerabilities in SEPPMail Secure E-Mail Gateway on 2026-05-19. **CVE-2026-2743 (CVSS 10.0)** is a path-traversal-to-arbitrary-file-write in the User Web Interface's large-file-transfer feature; the chained exploit demonstrated by InfoGuard overwrites `/etc/syslog.conf` and yields a Perl reverse shell, full appliance takeover, and indefinite persistence with cleartext access to all gateway-routed mail. **CVE-2026-44125 (CVSS 9.3)** is a missing-authorization-check on multiple new-GINA-UI endpoints, letting unauthenticated attackers reach functions that should require a session. **CVE-2026-7864 (CVSS 6.9)** leaks server environment variables via an unauthenticated GINA UI endpoint. Patches in 15.0.4 (with intermediate fixes in 15.0.2.1 and 15.0.3).

**Timeline:** InfoGuard Labs research → vendor patches (15.0.2.1 → 15.0.3 → 15.0.4) → public disclosure 2026-05-19.

**Why it matters:** Email gateways are the canonical "compromise once, read everything forever" target — joining the Roundcube and Zimbra pattern. SEPPMail is widely deployed in German-speaking enterprise (DACH region, financial services, healthcare). The CVE-2026-2743 single-shot syslog-write-to-reverse-shell technique is a portable primitive likely to be incorporated into automated scanners. Any internet-exposed SEPPMail appliance with the User Web Interface reachable is presumed-compromised once a public exploit lands.

**Discovered by:** Stephan Berger / InfoGuard Labs.

**Mitigation:**
- Upgrade to SEPPMail 15.0.4 immediately; do not delay to next maintenance window.
- Restrict User Web Interface and GINA UI to VPN or office IP allow-list while patching propagates.
- Audit gateway logs for unexpected POSTs to LFT endpoints and unexpected `/etc/syslog.conf` modifications over the last 60 days.
- Rotate any administrative credentials and TLS certificates resident on the appliance — compromise of CVE-2026-2743 yields full file-system access.

**Sources:** [InfoGuard Labs](https://labs.infoguard.ch/posts/seppmail_secure_e-mail_gateway_rce_vulnerabilities_cve-2026-2743_cve-2026-7864_cve-2026-44127_cve-2026-44128/) | [The Hacker News](https://thehackernews.com/2026/05/seppmail-secure-e-mail-gateway.html) | [CyberSecurityNews](https://cybersecuritynews.com/seppmail-gateway-flaws/)

---

### Mini Shai-Hulud Wave 3 — 600+ npm Packages Compromised via @antv / atool Maintainer + Sigstore Provenance Abuse [UPDATE]
**Product:** npm ecosystem (@antv/* family, timeago.js, third-party transitive deps) | **CVE:** Multiple (incl. CVE-2026-46412 @beproduct/nestjs-auth) | **Status:** Active campaign; npm has begun removing affected versions

Socket and Aikido reported on 2026-05-19 that 639 malicious versions across 323 unique packages were published to npm within a single hour starting 01:56 UTC. The compromised maintainer account **`atool`** is the primary publisher across the @antv family (charting / graph visualisation / flowchart libraries) plus **`timeago.js`** (1.5M weekly downloads). The payload is the previously-leaked Shai-Hulud worm primitive — but now with a critical new evolution: **the payload generates valid Sigstore provenance attestations by abusing OIDC tokens from compromised CI environments**, causing malicious npm packages to **pass standard provenance verification** despite containing credential-stealing malware. This is the cryptographic-trust escalation foreshadowed by Wave 2's SLSA-attested malicious TanStack versions on 2026-05-13. Parallel disclosures: GitHub Advisory Database tagged @beproduct/nestjs-auth versions 0.1.2-0.1.19 (CVE-2026-46412) as a Mini Shai-Hulud variant; 4 separate "non-TeamPCP clone" packages were already covered yesterday (chalk-tempalte + axios typosquats). The worm targets GitHub / npm / cloud / Kubernetes / Vault / Docker / database / SSH credentials.

**Threat score change:** 8 → 9. **What changed materially:** package count jumped from 4 (yesterday) to 600+ within 24h; Sigstore provenance generation is a novel defense-bypass primitive on top of the previously-documented SLSA-attestation abuse; the worm has propagated through a major chart-library ecosystem (@antv is widely used in enterprise data-visualisation stacks).

**Timeline:** TeamPCP source release 2026-05-15 → first non-TeamPCP clones 2026-05-19 (4 packages) → atool maintainer compromise 2026-05-19 01:56 UTC → Sigstore provenance abuse confirmed by Wiz / Socket / Aikido 2026-05-19.

**Why it matters:** Sigstore provenance attestation has been the recommended "verify the package came from a known publisher" defence layer since 2024. **Both SLSA attestation (Wave 2) and Sigstore provenance (Wave 3) are now demonstrably forgeable when an attacker controls a CI runner with OIDC token access** — verification-only defences are no longer sufficient. Any Node.js project that depends on the @antv family or timeago.js, even transitively, has a presumptive-compromise window of ~24h on 2026-05-19. If your dependency-resolution allows minor/patch auto-upgrades, you are presumed-compromised until proven otherwise.

**Discovered by:** Socket, Aikido, Wiz Research; npm advisory database.

**Mitigation:**
- Run `npm audit` against all repos; specifically check @antv/* family and timeago.js for installed versions matching the 2026-05-19 01:56-02:56 UTC window.
- Lock down CI to deny outbound network access during `npm install` for the next 30 days; assume any new package install attempts credential exfiltration.
- Rotate GitHub PATs, npm publish tokens, cloud credentials (AWS / GCP / Azure), Vault tokens, Kubernetes service-account tokens, Docker registry tokens, database credentials, and SSH keys for any developer workstation or CI runner that ran an unpinned `npm install` since 2026-05-19 01:56 UTC.
- Re-baseline any private package mirror; do not rely on provenance verification as the sole defence — combine with publish-time hash audit and behavioural CI runner monitoring.
- Brief incident-response leadership: cryptographic-trust signals (SLSA, Sigstore) are now insufficient for npm; manual review of dependency changes is the floor.

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/new-shai-hulud-malware-wave-compromises-600-npm-packages/) | [The Register](https://www.theregister.com/cyber-crime/2026/05/19/shai-hulud-keeps-burrowing-314-npm-packages-infected-after-another-account-compromise/5242601) | [Wiz Research](https://www.wiz.io/blog/shai-hulud-2-0-ongoing-supply-chain-attack) | [Snyk](https://snyk.io/blog/mini-shai-hulud-antv-npm-supply-chain-attack/) | [CyberScoop](https://cyberscoop.com/mini-shai-hulud-malware-npm-packages-compromised-again/)

---

## 🟠 HIGH

### Apache OFBiz — 17-CVE Mass Advisory: Multiple Pre-Auth & Authenticated RCE / Auth-Bypass / SSTI Vulnerabilities
**Product:** Apache OFBiz (ERP / CRM / e-commerce) | **CVE:** CVE-2026-29207, CVE-2026-31986, CVE-2026-35086, CVE-2026-41919, CVE-2026-45434, CVE-2026-46586 (key items in a 17-CVE batch) | **CVSS:** Multiple critical (pre-auth RCE highest) | **First reported:** 2026-05-19 (oss-security)

Apache OFBiz shipped a 17-CVE security advisory on 2026-05-19 via the oss-security mailing list. The standout items are:
- **CVE-2026-31986** — unauthenticated RCE via default JWT signing key combined with widget template injection (no authentication required when default secret is in place — high probability of unpatched real-world deployments).
- **CVE-2026-45434** — authentication bypass via flawed password-change logic leading to RCE.
- **CVE-2026-41919** — authentication bypass via improper LDAP special-character neutralisation (LDAP injection on the auth flow).
- **CVE-2026-29207** / **CVE-2026-35086** / **CVE-2026-46586** — multiple authenticated/low-priv RCE primitives via SSTI in content/email/template-expansion components and unsafe Groovy execution.

These 17 advisories collectively give attackers a layered attack surface: unauthenticated RCE on default-config instances (CVE-2026-31986), auth-bypass-to-RCE chains for hardened instances (CVE-2026-45434), and low-priv-to-RCE for authenticated attackers. OFBiz has been in CISA KEV before (CVE-2024-45195) and is regularly exploited within days of advisory.

**Mitigation:**
- Upgrade to the latest OFBiz security release immediately. Apache OFBiz's prior CVE-2024-45195 (also unauth RCE) was actively exploited within ~7 days of advisory — assume the same tempo for CVE-2026-31986.
- Rotate the JWT signing key on every OFBiz deployment — even if you believe you set a custom one, audit the configuration to confirm it is not the documented default.
- Audit OFBiz access logs for the last 30 days for any unauthenticated POSTs to template-handling endpoints.
- If patching cannot happen within 48h: place OFBiz behind a WAF with virtual-patch rules for the disclosed exploit paths.

**Sources:** [oss-security 2026-05-19](https://www.openwall.com/lists/oss-security/2026/05/19/) | [Apache OFBiz Security Page](https://ofbiz.apache.org/security.html)

---

### Microsoft Disrupts "Fox Tempest" Malware-Signing-as-a-Service — 1,000+ Fraudulent Code-Signing Certs Revoked; Ransomware Affiliates Identified (Vanilla Tempest, Storm-0501, Storm-2561, Storm-0249)
**Product:** Microsoft Artifact Signing service (abused) | **CVE:** None | **CVSS:** N/A | **First reported:** 2026-05-19

Microsoft's Digital Crimes Unit (DCU) and Microsoft Threat Intelligence announced on 2026-05-19 the disruption of **Fox Tempest**, a financially motivated cybercriminal cluster that operated a malware-signing-as-a-service (MSaaS) abusing Microsoft's Artifact Signing service to generate short-lived, fraudulent code-signing certificates on behalf of paying ransomware operators. Microsoft seized the `signspace[.]cloud` domain, took offline hundreds of attacker-operated Azure VMs and tenants, and revoked **over a thousand code-signing certificates** attributed to Fox Tempest customers. Threat-intelligence attribution links the service's downstream customers to **Vanilla Tempest, Storm-0501, Storm-2561, and Storm-0249** — all of which have shipped Fox Tempest-signed payloads as part of active ransomware intrusions.

**Why it matters:** This is a defensive operational event — the certs are already revoked, and the takedown is complete — but it materially changes ransomware actor TTP expectations for the next 30-90 days. Defenders should treat any Authenticode-signed binary in EDR/AV decision logic as "signature is signal but not authoritative" for the foreseeable future; ransomware operators will shift to alternative MSaaS providers or different signing-cert acquisition mechanisms (cf. DigiCert support-channel pattern 2026-05-04, DAEMON Tools installer compromise 2026-04-08). A list of revoked thumbprints from Microsoft can drive retroactive hunts in EDR / WDAC / Defender ASR logs for the last 60-90 days.

**Mitigation:**
- Pull the revoked-thumbprint list from Microsoft's Fox Tempest disclosure and run retroactive EDR / AV / WDAC log hunts for the last 90 days. Treat any hit as confirmed-malicious activity that bypassed signature-based controls.
- Validate that your endpoint controls actually enforce certificate revocation (CRL / OCSP) rather than relying on cached trust decisions.
- Brief leadership: the "Authenticode signed = probably safe" mental model has been further weakened; behavioural and runtime controls are the durable layer.

**Sources:** [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/05/19/exposing-fox-tempest-a-malware-signing-service-operation/) | [Microsoft On the Issues](https://blogs.microsoft.com/on-the-issues/2026/05/19/disrupting-fox-tempest-a-cybercrime-service/) | [SecurityWeek](https://www.securityweek.com/microsoft-disrupts-malware-signing-service-run-by-fox-tempest/) | [BleepingComputer](https://www.bleepingcomputer.com/news/security/cybercrime-service-disrupted-for-abusing-microsoft-platform-to-sign-malware/)

---

### Apache Tomcat Tribes — CVE-2026-34486 Unauthenticated RCE via EncryptInterceptor Fail-Open Bypass; Public PoC Now Available
**Product:** Apache Tomcat 11.0.19–11.0.20 / 10.1.53 / 9.0.116 (Tribes clustering, EncryptInterceptor) | **CVE:** CVE-2026-34486 | **CVSS:** Critical (unauth RCE class) | **First reported:** Patch 2026-04-04; Public PoC 2026-05-19

The Tomcat Tribes clustering module's `EncryptInterceptor` ships a fail-open regression introduced during a refactor — the `super.messageReceived(msg)` call moved from inside a try block to outside, so a decryption failure (which previously dropped the message) now passes the **attacker-controlled, undecrypted bytes** straight into Tomcat's Java deserialization routine. With a vulnerable gadget chain on the classpath (Commons-Collections etc.), this is unauthenticated RCE against any Tomcat cluster receiver port (default 4000). Patch shipped 2026-04-04 in 11.0.21 / 10.1.54 / 9.0.117. On 2026-05-19, multiple public PoC repositories appeared on GitHub (striga-ai/CVE-2026-34486; 404-src/CVE-2026-34486) along with a detailed writeup at striga.ai's research blog — converting this from "patched advisory" to "operationally exploitable for any attacker with classpath visibility."

**Mitigation:**
- Upgrade to Tomcat 11.0.21 / 10.1.54 / 9.0.117 immediately; specifically check classpath for Commons-Collections 3.x or other known gadget chains.
- Firewall the Tribes receiver port (default 4000) to cluster-internal traffic only — never expose to the perimeter.
- Audit Tomcat cluster receiver logs for unexpected connections / decryption-failure entries since 2026-04-04.

**Sources:** [striga.ai research](https://www.striga.ai/research/tomcat-tribes-unauth-rce) | [GitHub PoC repo](https://github.com/striga-ai/CVE-2026-34486) | [NVD CVE-2026-34486](https://nvd.nist.gov/vuln/detail/CVE-2026-34486) | [Cyber Kendra writeup](https://www.cyberkendra.com/2026/04/apache-tomcats-security-fix-opened-door.html)

---

### Panabit PAP-XM320 CVE-2026-36829 — Unauthenticated HTTP Server Auth Bypass via Session-Cookie + Directory Traversal (CVSS 9.8)
**Product:** Panabit PAP-XM320 (network appliance, v7.7 and earlier) | **CVE:** CVE-2026-36829 | **CVSS:** 9.8 | **First reported:** 2026-05-19 (OpenCVE / NVD)

OpenCVE surfaced CVE-2026-36829 — an unauthenticated auth-bypass in the embedded HTTP server of Panabit PAP-XM320 (Chinese-vendor application-control / network-traffic-management appliance) via improper session-cookie validation combined with a directory-traversal primitive. Network/management appliance, internet-facing administration interface, CVSS 9.8. Deployment is heavily concentrated in the Chinese market and Asia-Pacific carrier infrastructure; Western deployment is non-trivial but smaller. Treat as "actively exploited within days" for anyone with this appliance in fleet — Panabit appliances have featured in prior APT-attributed pre-positioning campaigns.

**Mitigation:**
- Inventory whether any Panabit appliances are present (often under "application control" / "DPI" / "traffic management" inventory categories).
- Block the management interface from internet exposure; require VPN access for administrative paths.
- Monitor for vendor patch — if not yet released, escalate to vendor procurement contact.

**Sources:** [NVD CVE-2026-36829](https://nvd.nist.gov/vuln/detail/CVE-2026-36829) | [OpenCVE](https://app.opencve.io/cve/)

---

## 🟡 MEDIUM

### PenPot MCP REPL CVE-2026-45805 + MCP Gateway Authority-Injection (GHSA-g53w-w6mj-hrpp) — Two More MCP-Server Unauth-RCE / Authz-Bypass Issues
**Product:** PenPot MCP REPL (npm); MCP Gateway (Go) | **CVE:** CVE-2026-45805; GHSA-g53w-w6mj-hrpp | **Published:** 2026-05-19 (GitHub Advisory Database)

Two more MCP-server-class vulnerabilities surfaced via GitHub Advisory Database on 2026-05-19. **CVE-2026-45805** in PenPot MCP REPL is an **unauthenticated RCE via an unprotected `/execute` endpoint** — the MCP server exposes a code-execution interface with no auth check. **GHSA-g53w-w6mj-hrpp** in MCP Gateway (Go) is a JWT / session bypass via the unauthenticated router, letting an attacker reach functionality that should require a valid session. Both fit the broader MEMORY-tracked pattern of MCP-server projects shipping unauthenticated administrative interfaces (now 8+ MCP server CVEs in 60 days: mcp-atlassian, nginx-ui, OpenHarness, chatgpt-mcp-server batch, Branch Monkey MCP, Astro MCP, NextChat MCP, and now PenPot + MCP Gateway).

**Mitigation:** Inventory MCP servers in your environment (typically run on developer workstations, AI-agent backends, and integration-tier infrastructure). Treat every MCP server as "default-no-auth" until proven otherwise — never expose MCP endpoints to the internet or even to broad internal networks without an explicit auth layer.

**Sources:** [GitHub Advisory Database 2026-05-19](https://github.com/advisories?query=type%3Areviewed+published%3A2026-05-19)

---

### Coder PKCS#7 Signature Bypass CVE-2026-46354 — Azure Instance Identity Validation Yields Unauthenticated Agent Token Theft
**Product:** Coder (Go-based self-hosted remote-dev-environment platform) | **CVE:** CVE-2026-46354 | **Published:** 2026-05-19

Coder (self-hosted Cloud Development Environment platform, used in enterprise dev-platform teams) shipped a fix for a PKCS#7 signature-bypass in Azure-instance-identity validation. The exploit allows an **unauthenticated attacker to steal agent tokens**, granting access to the dev workspace tier. The Coder server typically sits between developer workstations and corporate-credential-laden CI / cloud / GitHub integrations — agent-token theft is a foothold into the dev-tooling fabric. Joins the broader pattern of agentic / dev-platform credential-theft surfaces (Anodot 2026-05-07, Braintrust 2026-05-08, Anthropic Code MCP 2026-05-07).

**Mitigation:** Upgrade Coder to the patched release; rotate all Coder agent tokens; audit workspace activity logs for the last 30 days for unexpected agent connections.

**Sources:** [GitHub Advisory Database](https://github.com/advisories) — CVE-2026-46354 entry.

---

## 📋 Noted / Monitoring

**Linux Kernel "DirtyDecrypt" CVE-2026-31635** — page-cache-corruption LPE in `rxgk` subsystem; public PoC released 2026-05-19. LPE-only per current scope, but per MEMORY pattern *Linux kernel page-cache LPE bugs become container-escape primitives within 14 days* — watch for K8s-escape PoC by 2026-06-02. Promote if CISA KEV-added.

**Universal Robots PolyScope 5 CVE-2026-8153 (CVSS 9.8)** — unauth OS command injection in Dashboard Server of `cobot` industrial-robot controller. Patched in 5.25.1. Out of scope for our public-facing service inventory (OT / industrial robotics), but worth a one-line note for any OT-adjacent teams reading.

**Apache Airflow CVE-2026-27173** — Kubernetes provider JWT-token exposure; widely deployed, in scope but no confirmed exploitation; monitor.

**@angular/platform-server CVE-2026-46417** — SSRF via hostname hijacking; in-scope (widely deployed Angular SSR), no exploitation reported; standard SSRF mitigations apply.

**SQLFluff CVE-2026-46374 + CVE-2026-46373** — parser resource-exhaustion / stack-overflow; lint/DevOps tooling, narrow blast radius.

**haveged CVE-2026-41054** — local root via command socket; LPE-only, present on a non-trivial fraction of Linux servers (entropy daemon) but no remote vector.

**Evince / Atril / Xreader CVE-2026-46529** — command injection in document viewers (oss-security 2026-05-19); client desktop, out of scope.

**DFIR-IRIS 6-CVE batch** — open-redirect, file-upload, CSRF in DFIR platform; narrow deployment, no exploitation, monitor.

**SHub macOS infostealer** — new variant spoofing Apple security updates via AppleScript (Bleeping 2026-05-19); client-side, out of scope.

**INTERPOL Operation Ramz** — 201 arrests / 53 servers seized in MENA region; law enforcement disruption, not a vulnerability.

**Discord default-on E2EE for voice/video calls (2026-05-19)** — product feature rollout, defensive positive but not a vuln advisory.

**B1ack's Stash credit-card dump (4.6M cards, leak by seller misconduct)** — marketplace incident, not in scope but useful as a calibration data point on stolen-card market dynamics.

**Apache OFBiz CVE-2026-44919 (OpenStack Ironic DoS via crafted deployment requests)** — DoS only, lower priority than the OFBiz RCE batch.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer, thehackernews, securityweek, krebsonsecurity, schneier | ✅ |
| CISA / US Gov | cisa.gov (general), cisa.gov/KEV | ❌ (403 both) |
| Vendor advisories | rapid7, fortinet/threat-research, msrc/blog, blog.cloudflare/security, drupal.org (substitute) | ✅/⚠️ (msrc nav only) |
| Research / OSINT | securitylab.github, github.com/0xMarcio/cve, kb.cert.org/vuls, avleonov, habr/tomhunter, teletype/cyberok, dbugs.ptsecurity, cert.gov.ua | ✅ |
| Supply chain | seclists/fulldisclosure, github.com/advisories (substitute for github.com/search), openwall/oss-security (substitute for nvd) | ✅ |
| Threat intel | opencve.io (app.opencve.io) | ✅ |

**Errors:** cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403), attackerkb.com (403), bugcrowd.com/disclosures (404), hackerone.com/hacktivity (JS-only), cve.mitre.org (redirect to cve.org, JS-only), cve.org (JS-only), googleprojectzero.blogspot.com (redirect, JS), msrc.microsoft.com/blog (nav-only via WebFetch), nvd.nist.gov (nav-only via WebFetch), packetstormsecurity.com (homepage stats only, no advisories surfaced)

**CISA KEV:** Catalog unreachable via WebFetch (403). The Drupal SA-CORE-2026-004 patch dropping today is the most likely KEV-adjacent item this cycle; no confirmed new KEV additions surfaced via downstream-source relays. Track Microsoft Exchange CVE-2026-42897 (KEV-added 2026-05-17, federal deadline 2026-06-06) and Cisco SD-WAN CVE-2026-20182 (KEV-added 2026-05-14) for follow-on developments.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-20/night | Next: 2026-05-21/night*
