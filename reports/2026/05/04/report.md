# Watchtower Night Report — 2026-05-04
**Cycle:** Night | **Generated:** 2026-05-04 00:20 UTC (2026-05-04T00:20:00Z)
**Sources checked:** 22/30 | **CISA KEV total:** no new additions confirmed since 2026-05-01 | **New KEV additions:** none observed today

---

## 🟠 HIGH

### Instructure / Canvas LMS Data Breach — ShinyHunters Claims ~275M Records Across 9,000 Schools, Vulnerability-Driven
**Product:** Instructure Canvas Learning Management System | **CVE:** None disclosed | **CVSS:** N/A | **First reported:** 2026-05-01 (vendor disclosure) → 2026-05-03 (scope confirmation)

Instructure confirmed a cybersecurity incident on 2026-05-01 and updated 2026-05-02 to acknowledge personal-information exposure. ShinyHunters is now extorting the company on its leak site, claiming a dataset spanning ~9,000 schools / nearly 15,000 institutions across North America, Europe, and Asia-Pacific — approximately 275 million students, teachers, and staff. Confirmed exposed: names, email addresses, student ID numbers, and **private user-to-user messages**. Confirmed not exposed: passwords, dates of birth, government IDs, financial data. ShinyHunters claims theft via "a vulnerability in their systems" that has since been patched; Instructure has rotated application keys and increased monitoring but has not disclosed the vulnerability class, attack window, or whether content uploaded to courses (assignments, gradebook content, recorded conferences) was accessed.

**Timeline:** Friday 2026-05-01 — Instructure disclosure → Saturday 2026-05-02 — personal-information confirmation → Sunday 2026-05-03 — ShinyHunters listing on leak site, scope claims publicised by BleepingComputer / The Hacker News.

**Why it matters:** Canvas is the dominant higher-ed LMS in North America (Harvard, MIT, U.Michigan, hundreds of K-12 districts, plus large corporate-training Canvas tenants). Even though our org may not run Canvas, the dataset is going to be cross-referenced against existing breach corpora for credential-stuffing and SE-pretext lists targeting our employees who have children/students or run Canvas-using SaaS for training. Treat as a third-party-exposure incident: if any of your IDP, password-manager, or contractor-access flows touch a Canvas-tenanted partner, refresh the SE-pretext briefing for helpdesk and check for unusual account-recovery volume.

**Discovered by:** ShinyHunters extortion group (claim of compromise); confirmed by Instructure.

**Mitigation:**
- If you operate a Canvas tenant, push Instructure for the disclosure of vulnerability class, attack window, and whether your tenant data is in the published manifest; rotate any API tokens issued to Canvas integrations; review LTI / OAuth integration logs for the suspected exposure window.
- Tighten helpdesk-account-recovery flows that accept "I'm a parent / student / teacher" identity claims for the next 30 days — expect targeted SE using the leaked names + student IDs + private-message excerpts.
- Add "Canvas / Instructure" to the credential-stuffing watch list on every employee-facing login surface; the email + name corpus will be rented to credential-stuffing brokers within days.
- For any vendor that ingests Canvas data (analytics, proctoring, SSO bridges), confirm whether they hold copies of the same dataset and whether their controls were affected by the same vulnerability.

**Sources:** [BleepingComputer — Instructure confirms data breach, ShinyHunters claims attack](https://www.bleepingcomputer.com/news/security/) | [The Hacker News — coverage 2026-05-03](https://thehackernews.com)

---

### Apache OpenNLP Triple Advisory — Arbitrary Class Instantiation, XXE, and OOM via Malicious Model Files (CVE-2026-42027 / CVE-2026-40682 / CVE-2026-42440)
**Product:** Apache OpenNLP (Java NLP toolkit, embedded across data-pipeline / ML serving / search-relevance stacks) | **CVE:** CVE-2026-42027, CVE-2026-40682, CVE-2026-42440 | **CVSS:** Not yet scored by NVD | **First reported:** 2026-05-01 (oss-security)

Apache OpenNLP shipped 2.5.9 (and 3.0.0-M3 for the 3.x branch) on 2026-05-01 fixing three independent flaws all reachable via a single attack pattern — an attacker-supplied model archive:

- **CVE-2026-42027 — Arbitrary class instantiation in `ExtensionLoader`.** The loader calls `Class.forName(<name from model manifest>)` *before* checking against an allowlist; static initializers of attacker-named classes execute pre-validation. JNDI / network / file-side-effect classes already on the classpath become triggers. The fix introduces an `OPENNLP_EXT_ALLOWED_PACKAGES` allowlist that's checked first.
- **CVE-2026-40682 — XXE in `DictionaryEntryPersistor`.** XML reader has only namespace support enabled; external entity resolution and DOCTYPE remain on. Malicious dictionary file → `file://` exfil + `http://` SSRF.
- **CVE-2026-42440 — Out-of-memory DoS in `AbstractModelReader`.** `getOutcomes()` / `getOutcomePatterns()` / `getPredicates()` allocate arrays from unsigned-int counts in the binary `.bin` model with no bound. Setting count to `Integer.MAX_VALUE` triggers OOM at allocation. Fix gates allocations on `OPENNLP_MAX_ENTRIES` (default 10M).

All three are pre-auth from the model-loading code path's perspective. Real-world exploitability depends on whether your application accepts user-uploaded models (e.g. ML-as-a-Service, "bring your own corpus" features in support tooling, search-relevance test harnesses).

**Why it matters:** OpenNLP is a default pick for tokenisation / NER / sentence detection inside Java data pipelines (Solr, Elasticsearch enrichment, Spark NLP wrappers, customer-support search), and the model-file attack vector is the same pattern weaponised against Hugging Face by April's LeRobot / Marimo incidents. Any product that loads `.bin` model files from outside your control — including from collaborators, partners, or "model marketplaces" — should be considered exposed.

**Discovered by:** Subramanian S (CVE-2026-42440 credit); other CVE attribution pending.

**Mitigation:**
- Upgrade `opennlp-tools` to **2.5.9** or **3.0.0-M3** immediately.
- Inventory which products bundle OpenNLP (transitive in many enterprise search stacks); patch transitive dependencies.
- Pending patch: source models exclusively from trusted origins, validate dictionary files reject DOCTYPE before parsing, restrict the JVM classpath of model-loading services.
- Configure `OPENNLP_EXT_ALLOWED_PACKAGES` = `opennlp.*` only; explicit allow-list any custom extension class needed.
- Cap `OPENNLP_MAX_ENTRIES` per your real model sizes (default 10M is very generous).

**Sources:** [oss-security 2026-05-01 #19/20/21 — OpenNLP CVE-2026-40682, CVE-2026-42027, CVE-2026-42440](https://www.openwall.com/lists/oss-security/2026/05/01/19) | [oss-security index — May 2026](https://www.openwall.com/lists/oss-security/)

---

## 🟡 MEDIUM

### Apache Polaris Metadata Path Validation Bypass — CVE-2026-42809 / 42810 / 42811 / 42812 (Iceberg Catalog)
**Product:** Apache Polaris (open-source Iceberg REST catalog for cloud data lakes) | **CVE:** CVE-2026-42809, CVE-2026-42810, CVE-2026-42811, CVE-2026-42812 | **Published:** 2026-05-02

CVE-2026-42812 — the most concrete of the four — describes a logic gap where `ALTER TABLE` updates that touch only the `write.metadata.path` property bypass Polaris's commit-time storage-location validation. When `polaris.config.allow.unstructured.table.location=true` (a common opt-in for "bring your own bucket" deployments) and `allowedLocations` is broad, a user with table-modify permission can redirect metadata writes — and the temporary cloud-storage credentials Polaris issues for them — to attacker-chosen storage paths shared with other tenants/tables. The remaining three CVEs (42809–42811) cover related metadata-path / authentication-bypass scenarios in the same advisory bundle. Patched in **Apache Polaris 1.4.1**.

**Why it matters:** Polaris is the catalog layer that brokers IAM-authenticated access to Iceberg tables on S3/GCS/Azure Blob — i.e., it's the trust boundary between dozens of consumer warehouses and the underlying cloud-object storage. A cross-tenant metadata-write + credential-issuance bug is precisely the class of flaw that turns a multi-tenant data lake into a lateral-movement substrate.

**Mitigation:**
- Patch Polaris to **1.4.1**.
- Audit your Polaris configuration: if `allow.unstructured.table.location=true`, immediately review `allowedLocations` to be tight per-namespace prefixes; do not allow bucket-wide wildcards.
- Review who has `TABLE_WRITE_PROPERTIES` privilege — keep the surface small.
- Egress-restrict Polaris-issued temporary credentials to the specific table-prefix paths (defence in depth in case validation slips again).

**Sources:** [oss-security 2026-05-02 — Apache Polaris vulnerabilities](https://www.openwall.com/lists/oss-security/2026/05/02/13)

---

### Microsoft Defender Wrongly Flags DigiCert Root Certificates as `Trojan:Win32/Cerdigent.A!dha`
**Product:** Microsoft Defender (consumer + Defender for Endpoint) on Windows | **CVE:** None | **Published:** 2026-05-03

Microsoft Defender's signature update misclassifies legitimate DigiCert root and intermediate CA certificates as `Trojan:Win32/Cerdigent.A!dha` and is removing them from the Windows certificate store on detection, breaking TLS chains for any Windows-side service that validates against an affected DigiCert anchor (browsers, .NET apps, OS-channel updates, signed-binary verification). No exploitation is involved — this is an AV false-positive — but the operational impact across an enterprise Windows fleet is meaningful: failed software updates, SaaS auth chain breakage, smart-card flow failures, and local cert-pinning failures.

**Why this is medium not high:** Pure operational disruption, no security exposure (the attack-side equivalent — an actual Cerdigent trojan — is not what's deployed). But the mass-signature removal of root CA trust at fleet scale is exactly the prep step a sophisticated actor would want, so triage and confirm there's no in-flight Defender-platform abuse.

**Mitigation:**
- Pause Defender signature autoroll on a control group; verify next signature update reverts the false positive before deploying broadly.
- Re-import affected DigiCert certs from a clean Windows reference image where deletion has happened.
- Subscribe to Microsoft 365 Service Health for the Defender false-positive resolution; expect a corrected signature within 24–48 h based on prior Cerdigent-class FPs.
- Audit Defender Action history for which endpoints quarantined / removed certs and prioritise re-import on those hosts.

**Sources:** [BleepingComputer — Microsoft Defender wrongly flags DigiCert certs as Trojan:Win32/Cerdigent.A!dha](https://www.bleepingcomputer.com/news/microsoft/)

---

## 📋 Noted / Monitoring

**CVE-2026-40563 Apache Atlas — Script injection in DSL search endpoint (Apache Atlas 0.8 → 2.4.0)** — Disclosed via oss-security 2026-05-03; technical detail thin on the public mailing list, but Atlas is the Hadoop-ecosystem metadata governance system and a script-injection reaching DSL-evaluated queries is a familiar pattern. If you run Atlas anywhere in your data platform, watch for the upstream advisory and patch path.

**CVE-2026-40561 Starlet Perl HTTP Request Smuggling (≤0.31)** — `Content-Length` is incorrectly prioritised over `Transfer-Encoding: chunked`, violating RFC 7230 §3.3.3. Niche Perl PSGI server, but classic request-smuggling primitive — anyone running a reverse proxy in front of a Starlet-backed app is exposed; patch shipped, upgrade.

**Linux kernel `io_uring zcrx` freelist OOB write (CVE pending)** — Reported on oss-security 2026-05-03; LPE-class. Adding to the watchlist alongside the recently-KEV'd CopyFail (CVE-2026-31431) — io_uring continues to be a fertile LPE source. Track for KEV addition.

**Vim CVE pending — OS command injection via `path` completion in Vim < 9.2.0435** — Local-only desktop-tool issue; out of remote-services scope but worth flagging because Vim is everywhere on Linux ops boxes and any exploit chain that lands shell on a developer/ops workstation can pivot via `vim`.

**Vietnamese-linked Facebook account compromise via Google AppSheet (Push Security et al.)** — ~30,000 Facebook accounts harvested using AppSheet as a phishing-relay platform — adds Google's no-code automation surface to the SaaS-platform-as-phishing-relay pattern (alongside Pipedream / Zapier / Power Automate noted in earlier reports). Tune phishing-URL rules to include `*.appsheet.com` redirects.

**Microsoft Entra ID — AI-agent role privilege-escalation patched (per SCWorld 2026-05-02 reporting)** — Microsoft patched a flaw in the Entra ID AI-agent role that enabled privilege escalation / role takeover scenarios. CVE not surfaced in the snippet observed; primary MSRC source returned no detail via WebFetch. Continues the AI-agent-as-attack-surface theme; track for the formal MSRC advisory and CVE.

**SonicWall firmware roll-up referenced on SC Media 2026-05-02** — Three CVEs patched; appears to be follow-on coverage of the SonicOS April 2026 roll-up already covered 2026-05-01 (CVE-2026-0204 et al.). No material new info — flagged in case you missed yesterday's report.

**ConnectWise ScreenConnect KEV addition — reminder** — Federal remediation deadline already past (CVE-2024-1708, KEV addition 2026-04-29). Re-flagging because SC Media headlined it again 2026-05-02; if any unpatched ScreenConnect <23.9.8 remains in your fleet, treat as compromised.

**WordPress plugin batch — PT-2026-36577 (Gravity Forms 7.2), PT-2026-36588 (Widget Options 8.8), PT-2026-36617 (WCFM Frontend Manager 8.1), PT-2026-36681 (Nex-Forms Ultimate 7.2)** — Latest dbugs.ptsecurity advisories in the past 48h. Gravity Forms in particular is a high-deployment plugin (commercial, used widely on enterprise WordPress sites). Check the dbugs feed for fix versions.

**0xMarcio/cve repo activity — fresh PoCs landing for already-covered CVEs** — CVE-2026-31431 CopyFail (multiple new repos in last 24h, including detection scanners), CVE-2026-41940 cPanel (rfxn/cpanel-sessionscribe IR tool, Underh0st audit tool), CVE-2026-2991 KiviCare WordPress, CVE-2026-31802 npm tar — all already covered as findings or noted in prior reports. Mentioned for completeness; PoC volume on CopyFail continues to grow.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (403 — backfilled via THN/SecurityWeek/HelpNetSecurity) |
| Vendor advisories | msrc.microsoft.com/blog, fortinet.com/blog/threat-research, blog.cloudflare.com/tag/security, kb.cert.org/vuls | ⚠️ (msrc redirected, fortinet/cloudflare/cert no fresh posts) |
| Research / OSINT | schneier.com, rapid7.com/blog, seclists.org/fulldisclosure, openwall oss-security, dbugs.ptsecurity.com, github.com/0xMarcio/cve, github.com/search?q=CVE, opencve.io | ✅ |
| CVE databases | nvd.nist.gov, cve.org, cve.mitre.org, app.opencve.io | ⚠️ (nvd partially loaded; cve.org/cve.mitre.org JS-only) |
| Bug bounty / disclosure | hackerone.com/hacktivity, bugcrowd.com/disclosures, attackerkb.com, securitylab.github.com | ❌ (all 403/404/JS-only) |
| Project Zero / browser | projectzero.google | ✅ (no posts in window) |
| Russian-language community | habr.com/ru/companies/tomhunter, teletype.in/@cyberok, avleonov.com | ✅ (no posts in window) |
| Ukrainian govCERT | cert.gov.ua | ❌ (page empty) |
| Packetstorm | packetstorm.news | ⚠️ (front-page only; advisory section not loaded) |
| Supply-chain (additional) | socket.dev/blog (off-list, MEMORY-tracked) | ✅ |

**Errors:** CISA endpoints, attackerkb.com, hackerone.com/hacktivity, bugcrowd.com/disclosures, cve.org, cve.mitre.org, cert.gov.ua — unreachable via WebFetch (403/404/empty/JS-only). nvd.nist.gov, msrc.microsoft.com/blog, packetstorm.news, securitylab.github.com — degraded (loaded but no usable content for the window). Backfilled via openwall oss-security archive, BleepingComputer, The Hacker News, Help Net Security, Wiz, Snyk, Aikido.
**CISA KEV:** No new additions confirmed since CVE-2026-31431 (Linux CopyFail) added 2026-05-01. No KEV update visible in past 24 h via secondary sources.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-04/night | Next: 2026-05-05/night*
