# Watchtower Night Report — 2026-07-06
**Cycle:** Night | **Generated:** 2026-07-06 00:03 UTC (2026-07-06T00:03:00Z)
**Sources checked:** 26/30 | **CISA KEV total:** ~1,556 (no new adds 07-04→07-06 observable via reachable proxies) | **New KEV additions:** 0

---

## 🔴 CRITICAL

*No new critical-tier News or Updates in the 2026-07-05 → 2026-07-06 window.*

---

## 🟠 HIGH

### Apache APISIX jwt-auth Algorithm Confusion CVE-2026-39999 (CVSS 9.8) — Unauthenticated Full Auth Bypass on One of the Most-Deployed Open-Source API Gateways
**Product:** Apache APISIX (jwt-auth plugin), versions v2.2 → v3.16.0 | **CVE:** CVE-2026-39999 | **CVSS:** 9.8 | **First reported:** 2026-07-04 (openwall oss-security disclosure) — private report 2026-03-26

When a consumer is configured for an asymmetric algorithm (RS256/ES256/EdDSA) the plugin looks up the consumer's public key on the server side but then verifies the incoming JWT using whatever algorithm the token header specifies. An unauthenticated attacker can take that RSA public key (retrievable from public JWKS endpoints or the consumer's own signed tokens), switch the JWT header to `alg: HS256`, sign a forged token with the public key material as the HMAC secret, and mint a valid token authenticating as any known consumer. Fixed in v3.16.1. No public exploit repository yet, but the primitive is textbook algorithm-confusion — reproducible from the 0x90.sh public writeup in under an hour.

**Timeline:** private report to Apache Security 2026-03-26 → confirmed 2026-04-01 → PR + draft advisory 2026-04-08 → fix in 3.16.1 → public advisory + technical writeup on oss-security + 0x90.sh 2026-07-04.

**Why it matters:** Apache APISIX is one of the top-3 open-source API gateways alongside Kong and Envoy Gateway — commonly sitting at the north–south edge in front of enterprise microservices, sometimes doing token issuance for downstream services. A CVSS 9.8 pre-auth impersonation-as-any-consumer primitive against a gateway class widely deployed in cloud-native estates is the exact same shape of bug that produced the 2022 Kong Admin API and the 2023 Kong data-plane advisories that had 30-90 day mainstream exploitation tails. Any tenant that consumes JWTs signed by a known asymmetric key can be fully impersonated.

**Discovered by:** Reported to Apache Security 2026-03-26 (private disclosure), publicly detailed by 0x90.sh researcher (see writeup).

**Mitigation:**
- Upgrade Apache APISIX to v3.16.1 or later immediately — this is a version-only fix, no configuration-only workaround exists.
- Interim: on all `jwt-auth` consumers using asymmetric algorithms, restrict the accepted `alg` header at an upstream WAF (block any JWT whose header algorithm doesn't match the configured consumer type).
- Rotate consumer keys post-upgrade — assume any tenant whose public key was retrievable during the exposure window may have been impersonated.
- Audit APISIX access logs for successful requests with HS256 tokens for consumers configured as RS256/ES256/EdDSA — these are IoCs for exploitation attempts against the flaw before the patch.

**Sources:** [openwall oss-security 2026-07-04](https://www.openwall.com/lists/oss-security/2026/07/04/) | [0x90.sh — Apache APISIX jwt-auth: Turning a Public Key into an Auth Bypass](https://0x90.sh/threads/cve-2026-39999-apache-apisix-jwt-auth-turning-a-public-key-into-an-auth-bypass.52/)

---

### iCagenda Joomla Extension CVE-2026-48939 (CVSS 10.0) — Pre-Auth File Upload → RCE Now Weaponised With Same-Day GitHub Framework and In-the-Wild "icagenda-batch/1.0" Mass-Scanner
**Product:** iCagenda Joomla extension (all versions ≤ 4.0.7) | **CVE:** CVE-2026-48939 | **CVSS:** 10.0 (CVSS v4.0) | **First reported:** 2026-06-15 (patch shipped) — mass-exploitation tooling published 2026-07-06 by shinthink

The iCagenda frontend "Submit an Event" form accepted file attachments with **zero server-side file-type validation**, letting an unauthenticated visitor upload a PHP web shell to a predictable web-served folder and execute it. Fixed in 4.0.8 released 2026-06-15. Between patch date and today an in-the-wild automated scanner tagging itself `User-Agent: icagenda-batch/1.0` was observed exploiting unpatched instances per mySites.guru, and `shinthink/CVE-2026-48939` was published to GitHub within the last day — the third Joomla / Apache mass-exploitation framework from that same operator in the past two weeks (following `shinthink/solrradar` for Solr CVE-2026-44825 and `shinthink/pbck-exploit` for Joomla Page Builder CK CVE-2026-56290 per MEMORY 2026-07-04).

**Timeline:** patched 2026-06-15 (4.0.8) → `icagenda-batch/1.0` in-the-wild scanning observed (mySites.guru, ongoing) → shinthink mass-exploitation framework published to GitHub 2026-07-06 → Watchtower NEWS 2026-07-06.

**Why it matters:** Joomla remains one of the top-5 internet-exposed CMS platforms alongside WordPress, Drupal, Prestashop, and Magento. iCagenda is a popular calendar/event-registration extension present on a very large fraction of Joomla community and government-portal installs. The three-week gap between patch and public exploitation framework is the "same-day mass-exploitation framework distribution" pattern that MEMORY 2026-07-04 explicitly flagged as the new dominant zero-day-to-tooling channel; the primitive here (unauth file upload → PHP webshell) is the exact profile Clop and Rhysida operators use for opportunistic web-shell deployment then post-exploit reconnaissance. Any WAF template still keyed to the patch date rather than the shinthink same-day tooling window will miss the exploitation ramp.

**Discovered by:** Not publicly attributed; mySites.guru published post-patch technical analysis.

**Mitigation:**
- Update iCagenda to 4.0.8 on every Joomla instance in the fleet today — do not wait for scheduled window.
- Deploy WAF rule blocking multipart POSTs to the iCagenda event-submission endpoint that include `.php`, `.phtml`, or `.phar` filenames as an interim while patch propagates.
- Hunt for post-exploitation on unpatched instances: search `www/administrator/components/com_icagenda/attachments/` (and per-tenant equivalents) for files uploaded 2026-06-15 or later with executable extensions; search HTTP access logs for `User-Agent: icagenda-batch/1.0`.
- Post-compromise: rotate Joomla admin credentials, DB credentials, and any application secrets that lived on the same host; audit outbound connections from the web tier back 21 days.

**Sources:** [mySites.guru — iCagenda Zero Day File Upload RCE Fixed in 4.0.8](https://mysites.guru/blog/icagenda-zero-day-file-upload-rce/) | [OffSeq Threat Radar — CVE-2026-48939](https://radar.offseq.com/threat/cve-2026-48939-cwe-284-improper-access-control-in--bc923bedc1d1c47e) | [github.com/shinthink/CVE-2026-48939](https://github.com/search?q=CVE-2026-48939&type=repositories&s=updated&o=desc)

---

## 🟡 MEDIUM

### Apache Camel 2026-07-05 Batch — 25+ Coordinated Advisories via oss-security Covering Header Injection, Deserialization, and JMS ObjectMessage RCE Paths Across camel-mail / camel-kafka / camel-cxf / camel-solr / camel-mongodb / camel-dns / camel-websocket / camel-docling
**Product:** Apache Camel (multiple components; 4.0.0–4.14.6, 4.15.0–4.18.1, 4.19.x pre-4.19.0) | **CVE:** Multiple (batch includes CVE-2026-40047 camel-docling arg injection, CVE-2026-33453 camel-coap header injection previously assigned, plus 20+ additional CVEs disclosed 2026-07-05) | **Published:** 2026-07-05

Andrea Cosentino posted a coordinated batch of 25+ Camel security advisories to oss-security on 2026-07-05 covering three primary attack patterns: (1) HTTP/CoAP/DNS header injection into header-sensitive producers like camel-exec / camel-sql / camel-file / camel-bean / template components (RCE / arbitrary file write); (2) Infinispan-cache deserialization gadget chains in aggregation repositories (RCE); (3) JMS `ObjectMessage` deserialization when `mapJmsMessage=true` (default) and a gadget chain is on the classpath (RCE). Fixes: 4.14.6, 4.18.2, 4.19.0.

**Mitigation:**
- Upgrade to Camel 4.14.6 (14.x LTS), 4.18.2 (18.x LTS), or 4.19.0 across the estate.
- For deployments that cannot upgrade immediately: turn off `mapJmsMessage` on JMS routes, use route-level allow-lists on `headerFilterStrategy` for HTTP/CoAP/DNS-fronted routes, and audit any Infinispan cache write path for attacker-influenceable objects.
- Inventory transitive dependencies — Camel components ship inside Karaf / ServiceMix / Fuse / Spring Integration bridges and are often present in enterprise integration platforms.

**Sources:** [openwall oss-security 2026-07-05 (Andrea Cosentino)](https://www.openwall.com/lists/oss-security/2026/07/05/) | [Apache Camel Security page](https://camel.apache.org/security/)

---

### Microsoft Exchange CVE-2026-45504 (CVSS 8.8) — Public HawkTrace PoC + Technical Writeup Released for Authenticated SSRF-via-WOPI Arbitrary File Read
**Product:** Microsoft Exchange Server 2016 / 2019 / Subscription Edition (on-premises) | **CVE:** CVE-2026-45504 | **CVSS:** 8.8 | **Published:** 2026-06-09 (patch); PoC + writeup published early July 2026

Patched in the June 9 Exchange updates (KB5094139/40/42) but detailed technical breakdown plus working PoC only landed publicly this week. An authenticated low-privileged user creates an EWS `ReferenceAttachment` with a crafted `ProviderEndpointUrl` pointing to an attacker-controlled server; when a victim (or the attacker with a mailbox on the same instance) triggers the attachment preview, Exchange makes an SSRF request to the attacker server, which returns `file:///C:/path/to/file#` as `WebApplicationUrl`; the URI parser trick using the `#` fragment causes Exchange to read the target file via `FileWebRequest` and return contents to the attacker. Any low-priv mailbox account becomes an on-box arbitrary-file-read primitive against the Exchange server host.

**Mitigation:** Apply the June 9 Exchange updates immediately (any Exchange running on the pre-June-9 patch level is now exposed to a working, weaponised PoC). Post-patch: audit access to `\ClientAccess\ews\` and OneDrive-Pro utility logs for anomalous `ReferenceAttachment` operations from the disclosure window forward.

**Sources:** [HawkTrace — CVE-2026-45504 technical writeup](https://hawktrace.com/blog/CVE-2026-45504/) | [github.com/hawktrace/CVE-2026-45504 PoC](https://github.com/hawktrace/CVE-2026-45504) | [Cybersecurity News — Exchange SSRF PoC Exploit Released](https://cybersecuritynews.com/exchange-ssrf-poc-exploit-released/)

---

## 📋 Noted / Monitoring

**Apache Kafka OAUTHBEARER JWT clock-skew bypass (CVE-requested, oss-security 2026-07-04)** — Kafka 4.0.0–4.0.x authentication bypass reported by xylove21; no CVE yet, watching for assignment and vendor advisory.

**Apache Airflow CVE-2026-49297 (Shahar Epstein via oss-security 2026-07-04)** — Path traversal via GCSToSFTPOperator's GCS object-name handling; enterprise but Airflow rarely internet-exposed, calibration for internal-platform hygiene.

**CVE-2026-56015 Net::IP::LPM (Perl) heap out-of-bounds read (oss-security 2026-07-03)** — Unbounded prefix-length parameter causes memory exposure; potential impact on Perl-based routing/subnet tools embedded in web apps.

**CVE-2026-14570 Crypt::DSA (Perl) weak nonce generation (oss-security 2026-07-05)** — Biased random generation in DSA nonce + private key material; low real-world impact for most Perl deployments today, calibration for legacy Perl signing pipelines.

**CVE-2026-12746 Dancer2::Plugin::Auth::OAuth::Provider + CVE-2026-12740 Plack::Middleware::OAuth (oss-security 2026-07-04)** — Missing OAuth 2.0 state-parameter support (CSRF-class); low urgency but the Perl OAuth ecosystem should audit for downstream consumers.

**CVE-2026-46242 "Bad Epoll" Linux kernel UAF LPE (THN 2026-07-05)** — Unprivileged-user-to-root use-after-free in kernel epoll; out of scope per Watchtower policy (local privilege escalation) but tracked as post-exploit chain for Chrome-sandbox / K8s-pod-breakout scenarios.

**Cisco Unified Communications Manager in-the-wild exploitation confirmed (BleepingComputer + SecurityWeek 2026-07-04)** — Cisco publicly confirmed active exploitation of a previously-disclosed Unified CM vulnerability; watching for CVE identification + KEV addition. If assigned CVE lands in scope, will promote to News.

**FatFs embedded filesystem 7-vuln disclosure by runZero (THN 2026-07-04)** — Millions of IoT devices affected; requires physical/adjacent access, out of scope for internet-facing surface, calibration for IoT / OT fleets only.

**Kali Linux 2026.2 release (BleepingComputer 2026-07-03)** — 9 new tools + NetHunter updates; defender-tooling calibration, no vulnerability signal.

**Adobe ColdFusion + Campaign Classic emergency patches follow-up (2026-07-03 NEWS)** — No new exploitation activity observed 2026-07-05 → 2026-07-06 window; internet-facing ColdFusion patch SLA remains 24h, Adobe P1 rating still active. No UPDATE material yet.

**Ousaban Iberian Peninsula campaign (FortiGuard 2026-07-01)** — Regional (Spain/Portugal) phishing-PDF campaign with steganographic C2; low relevance for our fleet, calibration only for geo-specific threat modelling.

**FBI + Google disrupt NetNut residential proxy network (Krebs + THN 2026-07-02)** — 2M+ compromised devices dismantled; positive signal for reducing IAB proxy layer, no direct patchable finding.

**JADEPUFFER mainstream repackaging on BleepingComputer 2026-07-04** — Delayed BC coverage of the 2026-07-03 Sysdig LLM-orchestrated ransomware finding already covered on 2026-07-03; latency-calibration only.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ 403 (fallbacks via THN / BleepingComputer / Rapid7 ETR blog) |
| Vendor advisories | rapid7.com/blog, fortinet.com/blog/threat-research, msrc.microsoft.com/blog, blog.cloudflare.com/tag/security | ✅ / ⚠️ msrc empty content |
| Research / OSINT | schneier.com, avleonov.com, googleprojectzero.blogspot.com, kb.cert.org/vuls, seclists.org/fulldisclosure, github.com/0xMarcio/cve, github.com/search?q=CVE | ✅ / ⚠️ projectzero redirect |
| Advisories archive | openwall.com/lists/oss-security, securitylab.github.com, github.com/advisories, packetstorm.news, opencve.io, nvd.nist.gov, cve.mitre.org, cve.org, kb.cert.org/vuls | ✅ / ⚠️ nvd / cve.mitre / cve.org JS-only / packetstorm nav-only |
| Bug bounty | hackerone.com/hacktivity, bugcrowd.com/disclosures | ⚠️ h1 JS / ❌ bugcrowd 404 |
| Threat intel | attackerkb.com, dbugs.ptsecurity.com, habr.com/ru/companies/tomhunter, teletype.in/@cyberok, cert.gov.ua | ❌ attackerkb 403 / ✅ dbugs / ⚠️ habr silent since March / ⚠️ teletype silent since Feb / ⚠️ cert.gov.ua empty content |

**Errors:**
- `cisa.gov` and `cisa.gov/known-exploited-vulnerabilities-catalog` — 403 Forbidden via WebFetch; used THN + BC + Rapid7 ETR as KEV proxies.
- `attackerkb.com` — 403 Forbidden.
- `bugcrowd.com/disclosures` — 404 Not Found (URL changed, not yet updated in SOURCES.md).

**Degraded (checked but limited or empty content):**
- `msrc.microsoft.com/blog` — redirects to `microsoft.com/en-us/msrc/blog`, content nav-only via WebFetch.
- `packetstorm.news` (redirect from `packetstormsecurity.com`) — homepage nav only, no content.
- `securitylab.github.com/advisories/` — most recent items dated 2026-05-22.
- `opencve.io` — redirects to `app.opencve.io`, worked as CVE index but requires JS for detail pages.
- `nvd.nist.gov`, `cve.mitre.org`, `cve.org` — JS-required / API-only.
- `googleprojectzero.blogspot.com` — redirects to `projectzero.google`, no recent posts within window.
- `hackerone.com/hacktivity` — JS-required.
- `habr.com/ru/companies/tomhunter` — last post 2026-03-06 (4-month silence, escalate for drop next monthly review).
- `teletype.in/@cyberok` — last post 2026-02-04 (5-month silence, escalate for drop next monthly review).
- `cert.gov.ua` — homepage returned empty content via WebFetch.

**CISA KEV:** No new additions observed via reachable proxies in the 2026-07-04 → 2026-07-06 window (post-2026-07-02 SharePoint CVE-2026-45659 add). Federal 3-day BOD 26-04 SharePoint deadline expired Saturday 2026-07-04.

---

*Watchtower vulnerability-researcher | Cycle: 2026-07-06/night | Next: 2026-07-07/night*
