# Watchtower Night Report — 2026-05-06
**Cycle:** Night | **Generated:** 2026-05-06 00:30 UTC (2026-05-06T00:30:00Z)
**Sources checked:** 22/30 | **CISA KEV total:** ~1,440 | **New KEV additions:** none confirmed (cisa.gov 403 — see Update on CVE-2026-31431 from 2026-05-05)

---

## 🔴 CRITICAL

### Apache MINA Pre-Auth RCE Pair — CVE-2026-42778 / CVE-2026-42779 (CVSS 9.8 each) — Incomplete Fix of CVE-2026-41409 (CVSS 9.8)
**Product:** Apache MINA — versions 2.1.0–2.1.11 and 2.2.0–2.2.6 | **CVE:** CVE-2026-42778, CVE-2026-42779 | **Status:** Patched (2.1.12 / 2.2.7) — public technical detail; no confirmed in-the-wild yet

Apache published Apache MINA 2.1.12 / 2.2.7 to fix two distinct deserialization gadgets, both rated CVSS 9.8 (`AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`). CVE-2026-42778 is an *incomplete fix* of CVE-2026-41409 — the classname allowlist was applied too late, after a class's static initializer in `AbstractIoBuffer.getObject()` could already have run. CVE-2026-42779 is a parallel resolution-path bug in `AbstractIoBuffer.resolveClass()`: one branch handles primitive/static class lookups *without consulting the allowlist at all*, providing a clean bypass. Any application that calls `IoBuffer.getObject()` on attacker-controlled bytes is exploitable for full pre-auth RCE.

**Timeline:** CVE-2026-41409 disclosed and patched in earlier 2.1/2.2 release. Researcher identified that the prior fix was incomplete and that a second bypass path existed; both new CVEs published 2026-05-05 with patches in 2.1.12 / 2.2.7 the same day.

**Why it matters:** Apache MINA underpins a large slice of Java networking stacks — Apache Sshd, Apache Kafka client transports, Apache Asterix, Apache Karaf SSHD, and a long tail of internal RPC/messaging infrastructure. Anywhere `ObjectSerializationDecoder` accepts bytes from another tenant or the public internet, this is a one-shot RCE. This is the second incomplete-fix iteration on the same `getObject()` code path in 2026 — exploit researchers will already be reading the diff.

**Discovered by:** Independent researcher coordinated through Apache MINA security; patch authored by the Apache MINA maintainers.

**Mitigation:**
- Upgrade to Apache MINA 2.1.12 (2.1.x line) or 2.2.7 (2.2.x line) immediately — same-day patch availability.
- If immediate upgrade is impossible, audit application code for `IoBuffer.getObject()` calls and explicitly configure the `ObjectSerializationDecoder` classname allowlist to the minimum set required.
- Stop accepting Java-serialized payloads from untrusted sources entirely if practical — switch to JSON/Protobuf at the protocol boundary.
- Hunt: search `IoBuffer.getObject()` usage in your dependency tree (`mvn dependency:tree | grep mina`), and on the wire look for traffic patterns matching Java serialization magic bytes (`AC ED 00 05`) on internal RPC ports.

**Sources:** [Apache MINA security advisory (oss-security 2026-05-05)](https://www.openwall.com/lists/oss-security/2026/05/05) | [CVE-2026-42778 (OpenCVE)](https://app.opencve.io/cve/CVE-2026-42778) | [CVE-2026-42779 (OpenCVE)](https://app.opencve.io/cve/CVE-2026-42779) | [SecurityWeek — Critical, High-Severity Vulnerabilities Patched in Apache MINA, HTTP Server](https://www.securityweek.com)

---

## 🟠 HIGH

### CVE-2026-7482 "Bleeding Llama" — Ollama GGUF Loader Heap OOB Read → Pre-Auth Memory Disclosure (CVSS 9.1) Across ~300,000 Public Deployments
**Product:** Ollama < 0.17.1 | **CVE:** CVE-2026-7482 | **CVSS:** 9.1 | **First reported:** 2026-05-05

Ollama's `/api/create` endpoint accepts an attacker-supplied GGUF model file and quantises it. The GGUF loader trusts the per-tensor offset/length fields in the manifest; supplying offsets that exceed file length causes the server to read past the heap buffer during quantisation and emit the leaked bytes back inside the resulting model. Leaked memory has been demonstrated to include environment variables, API keys, and prior user conversation contents. The matching `/api/push` endpoint then exfiltrates the modified model to an attacker-controlled registry — both endpoints are unauthenticated by default. Intruder Labs concurrently scanned ~5,200 Ollama servers and found 31% reachable without authentication, while broader certificate-transparency analysis identified ~300,000 internet-exposed Ollama instances, predominantly self-hosted with `OLLAMA_HOST=0.0.0.0`.

**Timeline:** Vendor patched in Ollama 0.17.1; advisory published 2026-05-05 alongside SecurityWeek/THN coverage and the Intruder "1M exposed AI services" research.

**Why it matters:** Ollama has become the de facto self-hosted LLM substrate for engineering teams running internal coding assistants, RAG pipelines, and "ChatGPT-but-on-prem" deployments — the same systems that are routinely fed prompt histories containing AWS keys, ticket data, and customer PII. A single unauth GGUF push can stage a memory-disclosure attack against any of those workloads. The default-no-auth posture is the same operational pattern that drove the n8n CVE-2026-21858 mass exploitation in late March.

**Mitigation:**
- Upgrade Ollama to 0.17.1 immediately; treat anything older as compromised if `OLLAMA_HOST=0.0.0.0` was ever set on a publicly reachable interface.
- Place Ollama behind an authenticating reverse proxy (mTLS or OIDC); never expose `/api/create` or `/api/push` to the open internet.
- Hunt for GGUF uploads from external registries in the last 60 days; rotate any secrets that were present in the Ollama process environment during that window.
- Audit other self-hosted AI infrastructure (LangFlow, n8n, Flowise, Open WebUI) for the same default-no-auth pattern — Intruder reports widespread exposure.

**Sources:** [SecurityWeek — Heap OOB Read Flaw Leaves 300,000 Ollama Deployments Exposed](https://www.securityweek.com) | [The Hacker News — Critical Flaw in 300K Ollama Deployments](https://thehackernews.com) | [Intruder — We Scanned 1 Million Exposed AI Services](https://thehackernews.com) | [CVE-2026-7482 (OpenCVE)](https://app.opencve.io/cve/CVE-2026-7482)

---

### Quasar Linux (QLNX) — Trend Micro Discloses Stealth Linux Implant Targeting Developer & DevOps Workstations
**Product:** Linux developer/DevOps endpoints (npm, PyPI, GitHub, AWS, Docker, Kubernetes accounts) | **CVE:** None | **CVSS:** N/A | **First reported:** 2026-05-05

Trend Micro disclosed a previously-undocumented Linux implant they have named **Quasar Linux (QLNX)**. The malware *dynamically compiles* its own rootkit shared object and PAM backdoor on the target host using the system's `gcc`, then loads a dual-layer rootkit (LD_PRELOAD userland + eBPF kernel component) that hides its files, processes, and network sockets. A 58-command interactive RAT framework runs in-memory; the original dropper is unlinked, logs wiped, and the process renamed to blend in. Seven independent persistence mechanisms are deployed in parallel (LD_PRELOAD, systemd, crontab, init.d, XDG autostart, `.bashrc` injection, process injection). Detection is poor: only four AV products flagged the binary at publication time. The implant's apparent goal is supply-chain access — Trend Micro observed it harvesting credentials and tokens for npm, PyPI, GitHub, AWS, Docker, and Kubernetes accounts.

**Timeline:** Discovery analysis published 2026-05-05 by Trend Micro; no public attribution.

**Why it matters:** This is the first Linux-side implant in 2026 explicitly engineered around developer-machine compromise as a *route to* supply-chain attacks. Combined with the Mini Shai-Hulud (npm/PyPI) and BufferZoneCorp (Ruby/Go) campaigns of the last fortnight, this confirms that adversaries view dev workstations and CI runners as the cheapest path into downstream package ecosystems. Anyone whose engineers SSH into long-lived Linux hosts with publish credentials cached locally is exposed.

**Mitigation:**
- Pull Trend Micro's IOCs and run them across developer workstations, build runners, and bastion hosts; expect very low AV coverage and triage on behaviour rather than signatures.
- Audit `LD_PRELOAD` env, eBPF program enumeration (`bpftool prog list`), unfamiliar systemd units, `~/.bashrc` modifications, and unauthorised cron entries.
- Restrict where developer credentials live: use short-lived OIDC-issued tokens for npm/PyPI/GitHub publish, not long-lived `.npmrc` / `.pypirc` files on shared hosts.
- Treat any Linux host with a working `gcc` *and* publish credentials as a high-value target — consider removing one or both.

**Sources:** [BleepingComputer — New Stealthy Quasar Linux Malware Targets Software Developers](https://www.bleepingcomputer.com) | [Trend Micro Research (linked from BC)](https://www.trendmicro.com/en_us/research.html)

---

### CVE-2026-29014 — MetInfo CMS Unauthenticated PHP Code Injection Actively Exploited (CVSS 9.8)
**Product:** MetInfo CMS 7.9 / 8.0 / 8.1 | **CVE:** CVE-2026-29014 | **CVSS:** 9.8 | **First reported:** 2026-05-05

VulnCheck reported active exploitation of an unauthenticated PHP code-injection flaw in the WeChat-reply handler of MetInfo CMS. Insufficient input sanitisation lets attackers inject PHP that runs in the web-server context, achieving full pre-auth RCE on any internet-exposed instance. The vulnerable code paths exist in 7.9, 8.0, and 8.1 — i.e. every supported branch.

**Timeline:** CVE published with VulnCheck IOC reporting on 2026-05-05; vendor patch availability is unclear at time of writing.

**Why it matters:** MetInfo is heavily deployed across China-facing corporate sites and a non-trivial Western footprint among manufacturers and trading firms with PRC subsidiaries. The combination of pre-auth RCE + active exploitation + likely unmaintained installs places this in the same operational class as the Weaver E-cology CVE-2026-22679 campaign noted yesterday — expect mass-scanning within the week.

**Mitigation:**
- Inventory MetInfo installs across all subsidiary domains; the typical footprint is `<host>/admin/` plus a public site at the root.
- Block external requests to the WeChat-reply endpoint at the WAF layer until the vendor ships a fix.
- Hunt for `eval(`, `assert(`, or `preg_replace(... /e ...)` in recent file modifications under the MetInfo install path; suspicious POSTs to `/include/thumb.php` or `/app/system/` are common scanner targets.
- Treat any compromised install as full webserver RCE — rotate any DB / cloud credentials in the same VPC.

**Sources:** [The Hacker News — MetInfo CMS CVE-2026-29014 Exploited for RCE](https://thehackernews.com) | [VulnCheck advisory](https://vulncheck.com/advisories)

---

## 🟡 MEDIUM

### 🔄 Update — Apache HTTP Server 2.4.67 Patch Set Now 11 CVEs (was 9): mod_proxy_ajp Heap Overflow CVE-2026-28780 + mod_md OCSP CVE-2026-29168 Added
**Product:** Apache HTTP Server ≤ 2.4.66 | **CVE:** CVE-2026-28780 (new), CVE-2026-29168 (new) — joining the 9 published 2026-05-04 | **Threat score:** 7 (no change) | **First reported:** 2026-05-04

Two additional CVEs were published against the same 2.4.67 release. **CVE-2026-28780** is a heap-based buffer overflow in `mod_proxy_ajp::ajp_msg_check_header()` — a malicious AJP backend can write four attacker-controlled bytes past the heap buffer, enabling potential RCE on any httpd instance configured to proxy to AJP. **CVE-2026-29168** is in `mod_md` OCSP-response handling and allows unrestricted OCSP responses to be processed, weakening certificate-validation guarantees on ACME-managed deployments.

**Why the bump matters:** The 9-CVE coverage in yesterday's report missed the two most directly exploitable items: (a) `mod_proxy_ajp` is widely used in front of Tomcat/JBoss back-ends, and the 4-byte heap-write primitive lifts this from "DoS" into the same RCE-class as CVE-2026-23918; (b) `mod_md` OCSP handling weakens certificate-validation guarantees on ACME-managed deployments. Anyone who installed 2.4.67 yesterday is already covered; anyone still on 2.4.66 should now treat this as RCE-class.

**Mitigation:**
- Confirm Apache HTTP Server 2.4.67 is deployed everywhere — not 2.4.66.
- For deployments that cannot patch immediately: disable `mod_proxy_ajp` if unused (`a2dismod proxy_ajp` on Debian-family), and restrict AJP backend connections to trusted internal hosts only.
- For ACME / mod_md users: review issued certificate chains for any with anomalous OCSP responder behaviour observed since 2.4.66 deployment.

**Sources:** [oss-security 2026-05-05](https://www.openwall.com/lists/oss-security/2026/05/05) | [CVE-2026-28780 (OpenCVE)](https://app.opencve.io/cve/CVE-2026-28780) | [SecurityWeek — Apache MINA, HTTP Server patches](https://www.securityweek.com)

---

### DAEMON Tools Supply-Chain Compromise — Official Installers Trojanised Since 2026-04-08, Thousands Infected (Kaspersky)
**Product:** DAEMON Tools 12.5.0.2421 → 12.5.0.2434 | **CVE:** None | **CVSS:** N/A | **First reported:** 2026-05-05

Kaspersky disclosed that DAEMON Tools' official downloads — affecting versions 12.5.0.2421 through 12.5.0.2434 — were trojanised since 2026-04-08 by an unidentified, likely Chinese-speaking actor. The malicious installer drops first-stage info-stealer logic into `DTHelper.exe`, `DiscSoftBusServiceLite.exe`, and `DTShellHlp.exe`; a second-stage backdoor is selectively pushed to about a dozen targeted hosts; and at least one victim received a "QUIC RAT" with multi-protocol C2 and process-injection. Thousands of infections are spread across 100+ countries, with corroborated targeting of organisations in retail, scientific, government, and manufacturing sectors in Russia, Belarus, and Thailand.

**Why it matters:** Predominantly a consumer-grade software pivot, but the second-stage targeting pattern shows the actor is sifting infections to find enterprise networks — every IT/dev workstation in your fleet that ever installed DAEMON Tools (legacy ISO/disc-image utility) is in scope. Treat this as one more illustration of the "trust-the-download" supply-chain attack class that DigiCert (May 4) and Trellix (May 4) embodied for trust-infrastructure vendors.

**Mitigation:** Hunt for DAEMON Tools installs in software inventory across the fleet; isolate any host that received an installer between 2026-04-08 and 2026-05-05 and roll the host. Block outbound to QUIC-protocol C2 patterns Kaspersky published. Communicate to staff that direct-from-vendor downloads are not implicit safety guarantees — the trojanised installers were digitally signed.

**Sources:** [BleepingComputer — DAEMON Tools trojanized in supply-chain attack](https://www.bleepingcomputer.com) | [Kaspersky SecureList research (linked from BC)](https://securelist.com)

---

### Microsoft "Code-of-Conduct" AiTM Phishing Campaign — 35,000 Users / 13,000 Orgs / 26 Countries (92% U.S.) Targeted in 72-Hour Window
**Product:** Microsoft 365 / Entra ID — credential theft and MFA bypass | **CVE:** None | **First reported:** 2026-05-05

Microsoft Threat Intelligence detailed a credential-theft campaign observed 2026-04-14 → 04-16 that hit 35,000+ users at 13,000+ organisations across 26 countries (92% of the targeting in the U.S.; healthcare/life sciences 19%, financial services 18%, professional services 11%). The lure is an enterprise-style HTML email purportedly from "Internal Regulatory COC" warning of a code-of-conduct policy violation and demanding immediate review. The attack chain uses a PDF attachment that links through multiple CAPTCHA pages (designed to evade automated link-detonation) into an adversary-in-the-middle (AiTM) credential-and-token capture page; harvested tokens enable full MFA bypass. Inbound emails arrived from *legitimate* email-delivery service infrastructure, not spoofed-from addresses.

**Why it matters:** Same evasion playbook (PDF + AiTM + legitimate-relay sender + multi-stage CAPTCHA) as the BlackFile / SNOW / Cordial Spider chains we covered 2026-04-26 → 05-02 — confirms this is now the dominant Microsoft 365 credential-theft pattern of Q2 2026. Microsoft's parallel data shows QR-code phishing volume up 146% YoY (7.6M → 18.7M attacks).

**Mitigation:** Tune Defender / E5 phishing rules around the "code of conduct review" subject family and the legitimate-relay sender pattern. Force re-auth on suspicious sign-ins from new device IDs even when MFA was satisfied. Disable persistent-OAuth refresh tokens for high-risk roles. Train executive assistants and HR/Legal teams on this lure family — those are the recipients most likely to comply.

**Sources:** [BleepingComputer — Microsoft details phishing campaign targeting 35,000 users](https://www.bleepingcomputer.com) | [The Hacker News — Microsoft Phishing Campaign Targeting 35,000 Users](https://thehackernews.com) | [Microsoft Threat Intelligence blog (linked)](https://www.microsoft.com/security/blog)

---

## 📋 Noted / Monitoring

**CVE-2026-44007 — vm2 NodeVM Sandbox Escape (with nesting)** — vm2 is widely treated as deprecated/unsafe by upstream maintainers; this is the latest in a long line of sandbox-escape findings. If you still depend on vm2, migrate to `isolated-vm` or a real OS-level sandbox; treat any code that invokes vm2 nesting as RCE-equivalent.

**CVE-2026-43002 — OpenStack Horizon Unauthenticated Session Flood** — a public attacker can flood the login redirect store via Horizon's `next` parameter, leading to session-table exhaustion and Horizon DoS. Patched in OpenStack security advisory OSSA-2026-009.

**CVE-2026-42997 — OpenStack Ironic Credential Forwarding via iDrac Configuration** — a malicious iDrac BMC entry can coerce Ironic to forward Redfish credentials to attacker-controlled endpoints. Multi-tenant private clouds with mixed-trust hardware should patch promptly.

**CVE-2026-5766 / CVE-2026-35192 / CVE-2026-6907 — Django 6.0.5 / 5.2.14 Triple Advisory (all Low)** — ASGI `Content-Length` upload-limit bypass DoS, session fixation via cached pages when `SESSION_SAVE_EVERY_REQUEST` is on, and `UpdateCacheMiddleware` caching `Vary: *` responses leading to private-data exposure. All three are Low severity but Django is high-fanout; bundle into the next Django dependency-bump cycle.

**Apache MINA — `mod_md` OCSP CVE-2026-29168** — see HTTP Server update above; called out separately because ACME-managed certificate validation is the affected primitive, not the HTTP request path.

**Quasar Linux QLNX (developer-targeted Linux implant)** — see HIGH entry; flagged here because there is no CVE and no patchable surface, only IOCs and hunting work for DFIR teams.

**UAT-8302 China-nexus APT (Cisco Talos)** — South American + southeastern European government targeting using NetDraft (.NET FINALDRAFT variant), CloudSorcerer 3.0, SNOWLIGHT/SNOWRUST, Deed RAT, Zingdoor; tool overlap with Ink Dragon / Jewelbug / Earth Estries / LongNosedGoblin / Erudite Mogwai (Space Pirates). Track for Western critical-infrastructure pivots.

**Intruder Labs — "We Scanned 1 Million Exposed AI Services"** — research piece, not a single CVE: 31% of ~5,200 sampled Ollama servers reachable without authentication; 90+ exposed agent platforms (n8n, Flowise) leaking business logic and credentials; 518 instances wrapping frontier-model APIs (Anthropic / OpenAI / Google) without auth. Reinforces the "Ollama Bleeding Llama" finding above and the n8n exposure pattern from late March.

**CVE-2026-40280 — Gotenberg ≤8.30.1 Case-Sensitive Regex Bypass → Internal Network / Cloud Metadata Access** — server-side request-forgery class; affects PDF-generation services widely deployed behind internal APIs. Patch and review egress rules.

**CVE-2026-40331 — Masa CMS 7.2 → 7.5.2 Unauthenticated SQL Injection via altTable Parameter** — pre-auth SQLi exposing administrative credentials.

**CVE-2026-41950 — Dify <1.14.0 IDOR-Style File Access by Authenticated User (CVSS 6.5)** — authenticated tenant can read other tenants' files via arbitrary UUID submission; relevant for any Dify multi-tenant deployment.

**n8n Five-CVE Batch (credential exfiltration / project-access bypass / prototype pollution → RCE / SQL injection in DB nodes)** — disclosed via OpenCVE 2026-05-05; CVE numbers not yet broken out individually. Anyone running self-hosted n8n past March's CVE-2026-21858 should patch this batch as soon as detail and fix versions are published.

**ScarCruft (APT37) — BirdCall multi-platform backdoor delivered via trojanised sqgame[.]net Korean game platform** — Korea-region targeting (ethnic Koreans in China's Yanbian); included for situational awareness, not in-scope for a Western enterprise asset surface.

**iOS DarkSword 6-zero-day exploit chain (Schneier 2026-05-05)** — out of scope (mobile-only), but worth noting that the chain "leaked onto the internet" post-disclosure — mobile-device-management teams should ensure forced-update policies on iOS 18.4–18.7 fleets.

**Vimeo data breach (119,000 users) attributed to ShinyHunters** — already noted in 2026-04-29 cycle as part of the Anodot/Vimeo intrusion; updated victim count published 2026-05-05. Operational impact is consumer-only.

**Paramiko security audit completed; fixes scheduled for 5.0** — no CVEs assigned yet; pin the announcement and track for CVE batch when 5.0 ships.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, schneier.com, krebsonsecurity.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (403 Forbidden via WebFetch — 2nd day in a row) |
| Vendor advisories | rapid7.com/blog, fortinet.com/blog/threat-research, securitylab.github.com, blog.cloudflare.com/tag/security, msrc.microsoft.com/blog | ✅ / ⚠️ msrc degraded |
| Research / OSINT | seclists.org/fulldisclosure, openwall.com/lists/oss-security, kb.cert.org/vuls, avleonov.com, googleprojectzero.blogspot.com | ✅ / ⚠️ projectzero redirect |
| CVE databases | nvd.nist.gov, app.opencve.io, cve.org, cve.mitre.org | ⚠️ nvd degraded; cve.org / cve.mitre.org JS-only |
| Bug bounty / disclosure | hackerone.com/hacktivity, bugcrowd.com/disclosures, attackerkb.com | ❌ JS-only / 404 / 403 |
| Russian-language | habr.com/ru/companies/tomhunter/articles, teletype.in/@cyberok, dbugs.ptsecurity.com, cert.gov.ua | ✅ / ❌ cert.gov.ua empty |
| GitHub / PoC tracking | github.com/0xMarcio/cve, github.com/search?q=CVE | ✅ / ⚠️ github search 429 rate-limit |
| Packetstorm | packetstorm.news | ⚠️ landing-page only; degraded |

**Errors:** cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403), attackerkb.com (403), bugcrowd.com/disclosures (404), hackerone.com/hacktivity (JS), cve.org (JS), cve.mitre.org (JS redirect), cert.gov.ua (empty content)
**CISA KEV:** approx. 1,440 entries — no new additions confirmed today via mirrored sources; CVE-2026-31431 CopyFail KEV deadline 2026-05-15 still pending.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-06/night | Next: 2026-05-07/night*
