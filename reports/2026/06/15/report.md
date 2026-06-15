# Watchtower Night Report — 2026-06-15
**Cycle:** Night | **Generated:** 2026-06-15 00:30 UTC (2026-06-15T00:30:00Z)
**Sources checked:** 22/30 | **CISA KEV total:** Catalog unreachable (cisa.gov 403) | **New KEV additions:** Unknown — KEV catalog endpoint returned 403

---

## 🟠 HIGH

### LiteSpeed cPanel Plugin CVE-2026-54420 (CVSS 8.5) — Symlink-Following Privilege Escalation To Root On CloudLinux/CageFS Shared Hosting, Actively Exploited In May 2026, CVE Formally Assigned 2026-06-14, Patched In Plugin v2.4.8 / WHM v5.3.2.1; Reported By Namecheap
**Product:** LiteSpeed cPanel user-end plugin < 2.4.8 (LiteSpeed WHM Plugin < 5.3.2.0) | **CVE:** CVE-2026-54420 | **CVSS:** 8.5 (CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H) | **First reported:** 2026-06-01 (LiteSpeed vendor blog, CVE-pending) / 2026-06-14 (CVE-2026-54420 formally assigned via GitHub Advisory GHSA-3g44-c4qc-cxm8)

The user-end plugin on a shared host running CloudLinux/CageFS does not adequately guard against attacker-created symbolic links during the cert-generation + package-sizing API path (`generateEcCert` → `packageUserSize`). A user with FTP or web-shell access on a single tenant follows a symlink off the CageFS-jailed tenant root and onto the host root — CWE-61 UNIX Symbolic Link Following — escalating to root on the shared hosting server. The LiteSpeed vendor advisory of 2026-06-01 already flagged active in-wild exploitation with a specific call pattern (chained `generateEcCert` then `packageUserSize`, 7–10 concurrent calls per attempt, from one source IP); the CVE was only formally assigned on 2026-06-14 when the GitHub Security Advisory was published. Distinct from the 2026-05-28 LiteSpeed cPanel chain CVE-2026-48172 (KEV-listed, `lsws.redisAble` any-authenticated-cPanel-user-to-root) — same product family, different code path, second LiteSpeed cPanel plugin shared-host-tenant-escape CVE in 18 days. Patched in plugin v2.4.8 / WHM plugin v5.3.2.1.

**Timeline:** Active exploitation observed in May 2026 → LiteSpeed vendor advisory 2026-06-01 with patch (CVE-pending) → CVE-2026-54420 formally assigned via GitHub Security Advisory 2026-06-14 → Watchtower entry 2026-06-15.

**Why it matters:** Any tenant on a CloudLinux/CageFS shared hosting fleet that allowed shell/FTP access to even a single low-priv customer becomes a root-on-host pivot — the cluster of LiteSpeed shared-hosting CVEs in May/June 2026 (CVE-2026-48172 KEV + CVE-2026-54420) is a structural pattern, not a one-off. Anyone hosting customer / partner / agency cPanel tenants on internet-facing infrastructure is affected; the 7-10 concurrent calls / single-source-IP exploitation signature is detection-friendly.

**Discovered by:** Namecheap security team.

**Mitigation:**
- Upgrade LiteSpeed cPanel user-end plugin to ≥ 2.4.8; WHM plugin to ≥ 5.3.2.1.
- Pending the upgrade, audit `generateEcCert` and `packageUserSize` API call logs for 7–10 concurrent invocations from a single source IP per user account — that is the in-wild exploitation signature.
- Disable cPanel FTP / web-shell access on tenants that don't strictly need it; this is the precondition.
- Inventory every shared-hosting host: pair this fix with the 2026-05-28 KEV-listed CVE-2026-48172 patch — both required, neither sufficient.
- For multi-tenant shared-hosting MSPs, treat any single confirmed tenant compromise as host-root compromise pending audit of attacker's symlink artefacts under the tenant tree.

**Sources:** [LiteSpeed vendor advisory 2026-06-01](https://blog.litespeedtech.com/2026/06/01/security-update-for-litespeed-cpanel-plugin-2/) | [GitHub Security Advisory GHSA-3g44-c4qc-cxm8 (CVE-2026-54420, 2026-06-14)](https://github.com/advisories/GHSA-3g44-c4qc-cxm8)

---

### Google genai-toolbox MCP Server CVE-2026-11624 (CVSS v4 9.4) — Missing Origin Header Validation Yields DNS Rebinding Compromise Of MCP Server Cross-Origin From Operator's Browser; Patched In v0.25.0 With Two New `--allowed-hosts` / `--allowed-origins` Startup Flags; 7th MCP-Server Critical CVE Since April 2026
**Product:** Google genai-toolbox MCP server (googleapis/genai-toolbox) < v0.25.0 | **CVE:** CVE-2026-11624 | **CVSS:** 9.4 v4 (AV:N/AC:L/AT:N/PR:N/UI:A/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H) | **First reported:** 2026-06-13 (GitHub Security Advisory GHSA-76g7-m3xw-x9gr)

Google's genai-toolbox is an MCP server that exposes database / Cloud SQL / BigQuery / Looker / Snowflake / PostgreSQL / Trino / Spanner sources as MCP tools to AI agents (Claude, Cursor, IDE assistants). Prior to v0.25.0 the server's HTTP listener does not validate the `Origin` header on incoming connections — CWE-346 Origin Validation Error — which lets an attacker who tricks the operator into loading a malicious page in a browser sharing the operator's localhost route the page's `fetch` calls through DNS rebinding back at the locally-listening MCP server. The page then invokes any registered MCP tool (DB queries, file writes, credential exposure) under the operator's identity. The fix in v0.25.0 introduces two startup flags — `--allowed-hosts` (host allowlist) and `--allowed-origins` (origin allowlist) — both defaulting to `*` (unrestricted) with a startup warning when left at default, so the bug is mitigable only by operators who explicitly set non-default values. Continues the durable MCP-server-unauth-RCE / authz-bypass pattern documented in MEMORY: 6+ MCP servers compromised in 35 days (mcp-atlassian CVE-2026-27825, nginx-ui CVE-2026-33032, OpenHarness CVE-2026-7551, chatgpt-mcp-server CVE-2026-7061/62/64, Branch (2026-05-12)) — this is the 7th critical MCP server / toolbox CVE since April 2026, and the first one with Google's name on the advisory.

**Timeline:** Discovered by Jonathan Leitschuh (known DoorDash-zoom-bug researcher) → Google released v0.25.0 fix → published as GitHub Security Advisory GHSA-76g7-m3xw-x9gr 2026-06-13 → Watchtower 2026-06-15. No public PoC at disclosure; no confirmed in-wild exploitation; 1st-percentile EPSS.

**Why it matters:** Any team that runs `genai-toolbox` locally to connect agent IDEs (Claude Code / Cursor / Copilot) to internal databases is exposing those databases to any web page the operator visits unless they explicitly set the two new allowlist flags. The default-permissive posture (the `*` defaults with only a startup-warning) repeats the broader pattern called out in MEMORY 2026-05-05: "Self-hosted AI infrastructure default-no-auth posture is industry-wide, not vendor-specific." Treat the upgrade as gating: a fresh v0.25.0 binary without explicit allowlists is still vulnerable.

**Discovered by:** Jonathan Leitschuh (independent researcher, known for DoorDash / Zoom screen-share bugs).

**Mitigation:**
- Upgrade `genai-toolbox` to ≥ v0.25.0 AND start the binary with both `--allowed-hosts <internal-only>` and `--allowed-origins <specific-allowlist>` — the default `*` is still unsafe.
- Audit existing genai-toolbox processes (`pgrep / ps`) for startup arguments and force a restart if either flag is missing or set to `*`.
- Bind the MCP listener to `127.0.0.1` and a non-default high port — defence-in-depth against the DNS-rebinding primitive.
- Treat any agent operator who runs `genai-toolbox` locally as a trusted operator on the linked database — model permissions accordingly.
- Build / acquire an MCP-server inventory: this is the 7th critical MCP-server CVE since April 2026; an inventory makes the next one a 10-minute exercise instead of a re-research project.

**Sources:** [GitHub Security Advisory GHSA-76g7-m3xw-x9gr (CVE-2026-11624)](https://github.com/advisories/GHSA-76g7-m3xw-x9gr) | [NVD CVE-2026-11624](https://nvd.nist.gov/vuln/detail/CVE-2026-11624) | [googleapis/mcp-toolbox PR #2254](https://github.com/googleapis/mcp-toolbox/pull/2254)

---

## 🟡 MEDIUM

### Google Cloud Vertex AI Python SDK CVE-2026-2472 (CVSS v4 8.6) — Stored XSS In `_genai/_evals_visualization` Component Executes In Operator's Jupyter / Colab Notebook When Rendering Crafted Model-Evaluation / Dataset JSON; Affects Versions 1.98.0 → 1.130.x, Fixed In 1.131.0; PoC Public On GitHub
**Product:** Google Cloud Vertex AI Python SDK (`google-cloud-aiplatform`) versions 1.98.0–1.130.x | **CVE:** CVE-2026-2472 | **Published:** 2026-06-13/14 (NVD + Google Cloud Support Bulletin gcp-2026-011)

The `_genai/_evals_visualization` component in the Vertex AI Python SDK renders model-evaluation results and dataset JSON inside a notebook environment without escaping HTML/script content (CWE-79). An attacker who controls evaluation output (poisoned model card, malicious dataset, third-party eval result imported into a notebook) injects JavaScript that executes in the operator's Jupyter or Google Colab notebook session — leaking GOOGLE_APPLICATION_CREDENTIALS, OAuth refresh tokens, project metadata, and any kernel-local secrets, and pivoting to other notebook tabs sharing the same browser origin. CVSS v4 8.6 (network, low PR, user-interaction required). PoC publicly available on GitHub (JoshuaProvoste/CVE-2026-2472-Vertex-AI-SDK-Google-Cloud). Continues the MEMORY 2026-05-09 ClaudeBleed / Mini Shai-Hulud SessionStart / AI-agent-control attack-surface cluster — the latest twist is the eval-output surface (rather than agent-control config or extension config) as the injection point.

**Mitigation:**
- Upgrade `google-cloud-aiplatform` to ≥ 1.131.0 in all notebook environments (Colab, Jupyter, Vertex AI Workbench, Kubeflow pipelines that import the SDK).
- For Colab estates: invalidate workflow / runtime credentials issued during the 1.98.0 → 1.130.x window if untrusted eval outputs (3rd-party model cards, shared dataset JSON) were ever rendered.
- Audit Vertex AI Workbench logs for `gcp-2026-011`-style Google Cloud Support Bulletin advisories before treating Colab-shared notebooks as safe.
- Block notebook auto-render of untrusted JSON until the SDK upgrade completes; treat shared eval results as untrusted input.

**Sources:** [NVD CVE-2026-2472](https://nvd.nist.gov/vuln/detail/CVE-2026-2472) | [Google Cloud Support Bulletin gcp-2026-011](https://docs.cloud.google.com/support/bulletins#gcp-2026-011) | [Public PoC repository](https://github.com/JoshuaProvoste/CVE-2026-2472-Vertex-AI-SDK-Google-Cloud)

---

### KiviCare WordPress Plugin CVE-2026-2991 (CVSS 7.3) — `patientSocialLogin()` Accepts Any Email + Arbitrary Access Token, Authenticating Attacker As Any Patient (And Setting Auth Cookie Before Role Check, So Admin Email Yields Admin Session); Affects KiviCare ≤ 4.1.2; PoC Public On GitHub
**Product:** KiviCare clinic / patient-management WordPress plugin ≤ 4.1.2 | **CVE:** CVE-2026-2991 | **Published:** 2026-06-12/14 (Wordfence + NVD)

The `patientSocialLogin()` REST endpoint authenticates a user purely on (email, access_token) pairs without verifying the access_token with the claimed social provider. Any unauthenticated attacker submits any patient's email plus a junk token string and is logged in as that patient — full access to their medical records, appointments, prescriptions, billing. An additional flaw sets the WordPress auth cookie *before* checking the user's role, so submitting an administrator email yields an authenticated administrator session. PoC public on GitHub. Plugin scope is healthcare-sector WordPress deployments (clinics, private practices, telehealth front-ends) — high HIPAA / GDPR-health-data sensitivity even though the volume is modest. NVD notes the CVE is not being prioritized for NVD enrichment — Wordfence is the primary technical source.

**Mitigation:**
- Upgrade KiviCare to the latest patched release (vendor patch in progress; check Wordfence advisory page for fixed version).
- Until patched, restrict access to the `kc/v1/users/social-login` REST endpoint at the WP REST router / WAF layer.
- For HIPAA-regulated deployments: force a password reset for all KiviCare accounts AND audit access logs to `/kc/v1/users/social-login` for unrecognised email values — that is the IoC.

**Sources:** [NVD CVE-2026-2991](https://nvd.nist.gov/vuln/detail/CVE-2026-2991) | [Wordfence advisory](https://www.wordfence.com/threat-intel/vulnerabilities/id/) | [Public PoC repository](https://github.com/)

---

## 📋 Noted / Monitoring

**CVE-2026-11526 (Perl GD < 2.86)** — OS command injection via 2-arg `open()` of filename argument; primary disclosure on openwall oss-security 2026-06-14 by Paul Johnson; CGI-era Perl image-processing module, niche.

**CVE-2026-11527 (Perl Config::IniFiles < 3.001000)** — OS command injection via 2-arg `open()`; companion to CVE-2026-11526, same Perl 2-arg-open() footgun; niche Perl-stack scope.

**CVE-2026-9641 (Perl Crypt::PBKDF2 < 0.261630)** — Weak default algorithm and iteration count; oss-security thread continued 2026-06-14 with Jacob Bachmeyer + Peter Gutmann + Harry Sintonen discussion; previously in 06-13 NEWS, no material change.

**CVE-2026-54421 (OpenStack Ironic ≤ 35.0.1, CVSS 6.8)** — `PATCH` to volume properties leaks unredacted iSCSI credentials in response; POST path unaffected; bare-metal-provisioning operators only.

**CVE-2026-54411 (Linux-PAM ≤ 1.7.2 pam_userdb)** — Observable timing discrepancy enables password recovery via timing side-channel; classic but real; low-priority for general fleet, relevant where pam_userdb is the active PAM module.

**CVE-2026-54410 (nanoMODBUS v1.23.0)** — Off-by-one buffer overflow in `recv_msg_header()`; ICS / OT scope, niche library; CVSS 8.6.

**CVE-2026-54412 (LiamBindle MQTT-C v1.1.6)** — Heap-based OOB read + integer underflow in MQTT handler; embedded MQTT client library; CVSS 8.2.

**CVE-2026-54413 (driftregion iso14229 v0.9.0)** — Integer underflow in UDS security access handler; UDS (vehicle CAN-bus) automotive scope, out of Watchtower core.

**FBI / Black Lotus Labs / Google "Outsider Enterprise" takedown (BleepingComputer 2026-06-14)** — Chinese phishing-as-a-service operator dismantled (9k fake sites, 1M+ URLs, 3.8M cards, $1.9B losses, 2.5M SMS/month). Operational takedown, no CVE. Calibration data point for SMS-phishing infrastructure scale.

**CVE-2026-31431 (Linux kernel "Copy Fail" page-cache LPE)** — Fresh PoC published 2026-06-14 in github.com/0xMarcio/cve (Rust implementation); already in 05-16 / 05-19 NEWS + 06-04 UPDATE (K8s container-escape primitive within 14 days); not a fresh material change at score level — escalation watch only.

**CVE-2026-41089 (Windows Netlogon CLDAP)** — Fresh PoC drop in github.com/0xMarcio/cve labelled "CVSS 9.8 CRITICAL stack buffer overflow"; already in 05-13 NEWS + 06-02/06-03/06-13 UPDATE chain; PoC release is consistent with the existing exploitation-confirmed posture, no score change.

**CVE-2026-9109 (GPTranslate WordPress plugin, High)** — AI translation plugin vulnerability; tracking as part of AI-WP-plugin cluster alongside Wordfence's WP-plugin advisory series; technical detail pending.

**CVE-2025-15546 (Iptanus File Upload WordPress < 5.1.7)** — Improper file handling; classic WP file-upload class; standard patch cadence.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com (root only — /category/vulnerabilities 403), krebsonsecurity.com, schneier.com | ✅ |
| CISA / US Gov | cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403) | ❌ |
| Vendor advisories | fortinet.com/blog/threat-research, blog.cloudflare.com/tag/security, msrc.microsoft.com/blog (redirect → microsoft.com/en-us/msrc/blog, content unavailable), litespeedtech.com (advisory page reached directly) | ⚠️ |
| Research / OSINT | securitylab.github.com, googleprojectzero.blogspot.com (redirect → projectzero.google, sparse), avleonov.com, schneier.com, kb.cert.org/vuls | ✅ |
| CVE databases | nvd.nist.gov (search broken), opencve.io / app.opencve.io, dbugs.ptsecurity.com, cve.org (limited), cve.mitre.org (not tested — historically broken), github.com/advisories (bonus), openwall.com/lists/oss-security (bonus) | ⚠️ |
| Exploit / PoC | github.com/search?q=CVE, github.com/0xMarcio/cve, packetstormsecurity.com (redirect → packetstorm.news, limited), seclists.org/fulldisclosure (degraded — May/early-June archive only), attackerkb.com (403) | ⚠️ |
| Bug bounty | hackerone.com/hacktivity (sparse), bugcrowd.com/disclosures (404) | ❌ |
| Vendor PSIRT | rapid7.com (no date stamps visible) | ⚠️ |
| Russia / CIS | habr.com/ru/companies/tomhunter/articles (no June 2026 content), teletype.in/@cyberok (no June 2026 content), cert.gov.ua (content unavailable) | ⚠️ |

**Errors:** cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403), attackerkb.com (403), bugcrowd.com/disclosures (404), hackerone.com/hacktivity (no data), msrc.microsoft.com/blog (redirect — content unavailable), cert.gov.ua (content unavailable), cve.mitre.org (not tested — historical degraded).
**Degraded:** rapid7.com (no date metadata), seclists.org/fulldisclosure (early-June archive only — no June 13-15 messages), googleprojectzero.blogspot.com (sparse), nvd.nist.gov (search interface broken), packetstormsecurity.com (host moved to packetstorm.news; limited data), habr.com/ru/companies/tomhunter/articles (no June 2026 content), teletype.in/@cyberok (no June 2026 content), cve.org (limited).
**CISA KEV:** Catalog endpoint unreachable (403) — could not enumerate June 12–15 additions; cross-referenced via BleepingComputer (Ivanti Sentry BOD 26-04 already in 06-13 report).

---

*Watchtower vulnerability-researcher | Cycle: 2026-06-15/night | Next: 2026-06-16/night*
