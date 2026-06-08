# Watchtower Night Report — 2026-06-08
**Cycle:** Night | **Generated:** 2026-06-08 02:30 UTC (2026-06-08T02:30:00Z)
**Sources checked:** 26/30 | **CISA KEV total:** ~1,540 | **New KEV additions:** 1 (CVE-2026-45247 Mirasvit, added 2026-06-03 — Watchtower missed it in 06/06)

---

## 🔴 CRITICAL

### Mirasvit Full Page Cache Warmer for Magento 2 — CVE-2026-45247 (CVSS 9.8) Unauthenticated PHP-Object-Deserialization RCE → CISA KEV + Active Imperva Exploitation Observed
**Product:** Mirasvit Full Page Cache Warmer extension for Magento 2 / Adobe Commerce (versions < 1.11.12) | **CVE:** CVE-2026-45247 | **Status:** Patched (1.11.12) | KEV (added 2026-06-03) | Active Exploitation Confirmed

The extension reads an attacker-controlled `CacheWarmer` cookie on ordinary storefront requests and passes it directly to PHP's native `unserialize()` without class allow-listing, classic CWE-502 PHP Object Injection. Existing gadget chains in Magento core and dependencies turn the deserialization primitive into unauthenticated RCE on the storefront PHP worker. No authentication, admin access, or special config required — the attack surface is every public Magento storefront with the extension installed and not yet upgraded to 1.11.12. Imperva confirmed in-the-wild exploitation attempts containing serialized-PHP payloads (cookie values base64-prefixed `Tz` / `Qz` / `YT`); they observed targeting primarily concentrated on gaming and business sites in the US, UK, France, and Australia.

**Timeline:** Sansec disclosed 2026-05 → vendor patch 1.11.12 released → SecurityWeek coverage 2026-06-04 (Watchtower NOTED 06/06 with no CVE assigned) → CISA KEV addition 2026-06-03 (Watchtower missed) → Imperva exploitation blog + IOCs published → THN republishes the KEV addition 2026-06-06.

**Why it matters:** Magento / Adobe Commerce is one of the largest e-commerce stacks on the public-facing internet (hundreds of thousands of storefronts), and Mirasvit Cache Warmer is a popular performance extension. The exploit primitive is a single cookie value on a normal storefront request — bot-friendly, CDN-friendly, scanner-friendly. KEV + active exploitation puts this in the "patch and hunt now" tier for any team running Magento.

**Discovered by:** Sansec (initial advisory); Imperva (in-the-wild exploitation telemetry + IOCs).

**Mitigation:**
- Upgrade Mirasvit Full Page Cache Warmer to 1.11.12 or later immediately on all Magento / Adobe Commerce instances.
- If patching is delayed, disable the Mirasvit Cache Warmer module and clear its cache pools.
- Hunt web-server / WAF logs for `CacheWarmer:(Tz|Qz|YT)` cookie values (base64-encoded serialized PHP object markers).
- Inspect Magento `var/`, `pub/media/`, and PHP-FPM worker process trees for unexpected child processes, web-shell artifacts, and outbound connections following first observation.
- Federal civilian agencies have a KEV deadline per the standard 21-day BOD 22-01 cadence.

**Sources:** [CISA KEV alert (2026-06-03)](https://www.cisa.gov/news-events/alerts/2026/06/03/cisa-adds-one-known-exploited-vulnerability-catalog) | [Imperva exploitation blog + IOCs](https://www.imperva.com/blog/imperva-customers-protected-against-cve-2026-45247-in-mirasvit-full-page-cache-warmer-for-magento/) | [Sansec advisory](https://sansec.io/research/mirasvit-cache-warmer-object-injection) | [THN KEV writeup](https://thehackernews.com/2026/06/cisa-adds-exploited-magento-rce-flaw.html) | [SecurityWeek](https://www.securityweek.com/mirasvit-vulnerability-exploited-to-execute-code-on-magento-servers/)

---

## 🟠 HIGH

### Microsoft 365 Copilot CVE-2026-45497 — Critical RCE via Command Injection in Cloud Service (Already Mitigated Server-Side, No Customer Action)
**Product:** Microsoft 365 Copilot (Microsoft cloud service) | **CVE:** CVE-2026-45497 | **CVSS:** 9.6 critical (Microsoft) / 3.1 retracted score in NVD reflecting "no customer action required" | **First reported:** 2026-06-04

Microsoft published CVE-2026-45497 on 2026-06-04 — a critical command-injection vulnerability in Microsoft 365 Copilot allowing an "authorized" attacker to execute code over the network, with scope change (S:C) indicating the issue could break out of the Copilot service container and impact other M365 components. Per Microsoft's update guide and confirmation by Tenable, the vulnerability has been fully mitigated in Microsoft's cloud service — no customer patch, no configuration change, no tenant action required, and no in-the-wild exploitation observed. This is the first publicly-acknowledged critical RCE in an enterprise AI assistant from a major cloud provider; it lands alongside CVE-2026-42824 (M365 Copilot Information Disclosure, 2026-06-04) and follows the May Patch Tuesday CVE-2026-26164 (M365 Copilot info disclosure, Watchtower 2026-05-13).

**Mitigation:**
- No customer action required (server-side fix already in production).
- Verify M365 Copilot threat-model entries in your AI-platform risk register reflect the demonstrated "container escape from Copilot into other M365 service plane" capability.
- Review which user identities have Copilot delegated permissions and what cross-service blast radius they imply — Copilot's authorization scope is the actual attack surface here.
- Track CVE-2026-42824 (Info Disclosure) in the same review cycle.

**Sources:** [MSRC advisory CVE-2026-45497](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45497) | [Tenable CVE record](https://www.tenable.com/cve/CVE-2026-45497) | [Windows News writeup](https://windowsnews.ai/article/cve-2026-45497-microsoft-365-copilot-critical-rceno-patch-needed-but-review-risk.422846)

---

## 🟡 MEDIUM

*(No standalone MEDIUM items today — see Noted for tracking-only entries.)*

---

## 📋 Noted / Monitoring

**C0XMO Gafgyt botnet — mainstream coverage expansion (BleepingComputer 2026-06-07)** — BleepingComputer republished the FortiGuard 2026-06-03 disclosure (Watchtower NOTED 06/04). Adds attribution detail (Japanese tech-company target, German source IP), confirms modular architecture, restates DD-WRT CVE-2021-27137 buffer-overflow as the propagation vector. IoT-botnet calibration only — DD-WRT is enthusiast / SOHO firmware, not enterprise-fleet relevant.

**Silent Ransom Group / Luna Moth / UNC3753 / Chatty Spider — law-firm IT-impersonation campaign continues (BleepingComputer 2026-06-07)** — Follow-up to the FBI FLASH from 2026-05-26 (Watchtower 05/28 OOS). Adds technical IOCs: phishing domains `<org>-itdesk[.]com` / `<org>-it[.]com`, abuse of Microsoft Teams / Zoom / Quick Assist / AnyDesk / Zoho Assist for initial access, WinSCP / Rclone for exfiltration, fast-flux DNS via residential proxies, leak site `business-data-leaks[.]com`. Largely social-engineering scope and law-firm-vertical-specific, but the remote-access tool fingerprint is useful detection input for any enterprise running those clients.

**CVE-2022-0492 (Linux cgroup auth bypass) + CVE-2025-48595 (Android Framework integer overflow) — CISA KEV adds 2026-06-02** — Linux cgroup-1 release_agent privilege bypass historically used for container-escape chains; Android integer overflow is mobile-only OOS. The CVE-2022-0492 KEV addition is the relevant one for any team running shared-tenant container infrastructure (cgroup-v1 escapes from inside a container). Patched in upstream kernels since 2022.

**CVE-2026-42824 — Microsoft 365 Copilot Information Disclosure (2026-06-04)** — Companion advisory to the CVE-2026-45497 RCE above. Already mitigated in Microsoft cloud, no customer action; tracked here as an additional AI-platform calibration data point.

**PT-Security DB June-7 batch — GL.iNet routers, JD Cloud Box AX6600 (CVE-2026-11413, CVSS 9.0), Jinher OA (CVE-2026-11435, CVSS 7.5), Clash-Verge-Service-IPC (CVE-2026-26422, CVSS 8.4)** — Most niche or SOHO / regional-vendor scope; not corporate-fleet-relevant. Clash-Verge is a Chinese-language VPN-tunnel client; flagged for review only if internal asset DB surfaces it on developer endpoints.

**WordPress-plugin micro-batch (PT-Security 06/07): Click To Chat – WA Widget (CVE-2026-7795, CVSS 6.4), EmbedPress (CVE-2026-7796, CVSS 6.4), LearnPress (CVE-2026-8502, CVSS 5.3)** — Standard WordPress-plugin CVSS-6/7 noise; auto-update channels should pick them up. No incident activity reported.

**CERT/CC VU#595768 Securly Chrome extension + VU#615987 Verizon VoLTE IPsec + VU#265691 Appsmiths XSS + VU#873170 Collibra agent (2026-06-02..06-03)** — All previously covered as noted in earlier Watchtower entries. No new public technical detail.

**Patch-Tuesday-prep reminder** — Microsoft's June 2026 Patch Tuesday is 2026-06-09 (tomorrow). Expect the usual ~100–130 CVE batch; flag for tomorrow's report.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (403 persistent — KEV add CVE-2026-45247 inferred from THN/Imperva/SecurityWeek relay) |
| Vendor advisories | msrc.microsoft.com/blog, fortinet.com/blog/threat-research, rapid7.com, securitylab.github.com | ⚠️ rapid7 / ⚠️ msrc (degraded) / ✅ fortinet, securitylab |
| Research / OSINT | schneier.com, krebsonsecurity.com, googleprojectzero.blogspot.com, blog.cloudflare.com/tag/security, avleonov.com, dbugs.ptsecurity.com, opencve.io | ✅ for most; ⚠️ opencve (homepage only); GPZ + Cloudflare returned only May 2026 posts |
| Supply chain | github.com/search?q=CVE, github.com/0xMarcio/cve | ✅ github search / ⚠️ 0xMarcio (page index only) |
| Threat intel | seclists.org/fulldisclosure, packetstormsecurity.com, kb.cert.org/vuls, attackerkb.com, hackerone.com/hacktivity, bugcrowd.com/disclosures, nvd.nist.gov, cve.mitre.org, cve.org, habr.com/ru/companies/tomhunter, teletype.in/@cyberok, cert.gov.ua | mixed — see Errors |

**Errors:**
- cisa.gov — 403 Forbidden (persistent per memory; KEV inferred via THN/Imperva/SecurityWeek relay)
- cisa.gov/known-exploited-vulnerabilities-catalog — 403 Forbidden (persistent)
- attackerkb.com — 403 Forbidden (recurrent)
- bugcrowd.com/disclosures — 404 Not Found (current page structure changed)
- Degraded (page reachable but only stale content or no June data): rapid7.com, seclists.org/fulldisclosure (only Revive SA-2026-002), packetstormsecurity.com (redirect & ToS page), opencve.io (homepage marketing only), cve.mitre.org (redirect to cve.org with no data), cve.org (no listing data), msrc.microsoft.com/blog (no post listing), hackerone.com/hacktivity (no public listing visible), github.com/0xMarcio/cve (year-folder index only), habr.com/ru/companies/tomhunter (latest post 2026-03), teletype.in/@cyberok (latest 2026-02), cert.gov.ua (no listing)

**CISA KEV:** ~1,540 entries total. New since Watchtower 2026-06-07: 1 — **CVE-2026-45247 (Mirasvit Full Page Cache Warmer, added 2026-06-03)** — promoted to CRITICAL above. Earlier-week KEV adds CVE-2022-0492 / CVE-2025-48595 (2026-06-02) noted above.

---

*Watchtower vulnerability-researcher | Cycle: 2026-06-08/night | Next: 2026-06-09/night*
