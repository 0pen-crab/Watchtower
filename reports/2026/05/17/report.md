# Watchtower Night Report — 2026-05-17
**Cycle:** Night | **Generated:** 2026-05-17 23:00 UTC (2026-05-17T23:00:00Z)
**Sources checked:** 16/30 | **CISA KEV total:** active (Exchange CVE-2026-42897 added 2026-05-16) | **New KEV additions:** 1

---

## 🔴 CRITICAL

### 🔄 Microsoft Exchange Server CVE-2026-42897 added to CISA KEV (CVSS 8.1)
**Product:** On-premises Microsoft Exchange Server 2019 / 2016 (OWA component) | **CVE:** CVE-2026-42897 | **Status:** KEV / Active Exploitation / Mitigations Only (no permanent patch yet)

CISA added Microsoft Exchange Server CVE-2026-42897 to the Known Exploited Vulnerabilities catalog on 2026-05-16, formalizing the active-exploitation determination Microsoft made on 2026-05-15. The bug is the OWA cross-site scripting flaw triggered by a crafted email body that executes arbitrary JavaScript in the recipient's Outlook Web Access context. Microsoft has still **not shipped a permanent code patch** — only the configuration-level mitigations issued mid-week — and Pwn2Own Berlin Day 2 produced an Exchange compromise on the same day, putting two independent in-the-wild Exchange compromise vectors on the table within 72 hours.

**Timeline:** Patch Tuesday 2026-05-13 (no Exchange Critical) → Microsoft confirms ITW exploitation 2026-05-15 with mitigations only → Pwn2Own Berlin Exchange compromise 2026-05-15 → CISA KEV add 2026-05-16 with the standard 21-day federal remediation deadline (2026-06-06).

**Why it matters:** On-prem Exchange remains the PRC-aligned initial-access vector active across 2026-Q2 (SHADOW-EARTH-053, FamousSparrow / UAT-9244). KEV listing without a permanent patch is the same operationally-painful pattern as ProxyNotShell (2022) and ProxyShell (2021) — defenders are forced to deploy interim mitigations correctly across every Exchange OWA endpoint while triaging for compromise indicators with no clear "patched" end-state. Any unpatched on-prem Exchange OWA reachable from the internet should be assumed-exploitable until permanent patches ship.

**Discovered by:** Microsoft Threat Intelligence (active-exploitation determination); ZDI / Pwn2Own contestants (Pwn2Own Berlin Exchange compromise, embargoed).

**Mitigation:**
- Apply Microsoft's interim configuration mitigations across every on-prem Exchange OWA frontend immediately (do not wait for a permanent patch).
- For internet-exposed Exchange OWA, restrict access to known VPN/IP allowlists where business-feasible until a permanent patch ships.
- Hunt for crafted-email indicators in OWA-rendered messages, particularly attacker-controlled JavaScript inline in HTML email bodies; pivot from any matching message to OWA session/token theft and inbox-rule manipulation.
- Federal agencies: 2026-06-06 KEV remediation deadline.
- Enable Exchange OWA detection for the second-stage post-XSS actions (mailbox-rule changes, OAuth token exchange, item exports) — patching alone will not retroactively detect prior intrusion.

**Sources:** [The Hacker News — CISA KEV addition](https://thehackernews.com/) | [SecurityAffairs — KEV addition](https://securityaffairs.com/) | [BleepingComputer — Microsoft warns of Exchange zero-day](https://www.bleepingcomputer.com/) | [SecurityWeek — Microsoft warns of Exchange zero-day exploited in the wild](https://www.securityweek.com/)

---

## 🟠 HIGH

### Microsoft Azure Backup for AKS — Confused Deputy escalation (Backup Contributor → cluster-admin), Microsoft refused CVE, silently patched
**Product:** Azure Backup for AKS (Azure Kubernetes Service) | **CVE:** None issued (Microsoft refused); CERT/CC VU#284781 | **CVSS:** Not assigned | **First reported:** 2026-03-17 (public disclosure 2026-05-16)

Justin O'Leary disclosed a confused-deputy vulnerability (CWE-441) in Azure Backup for AKS that allows a user holding only the **Backup Contributor** role (no Kubernetes RBAC permissions on the target cluster) to obtain cluster-admin equivalent access on any AKS cluster they can enable backup for. Enabling backup automatically establishes a Trusted Access relationship between the AKS cluster and the backup service, which the attacker then leverages to extract Kubernetes Secrets or schedule arbitrary workloads on the cluster. Microsoft rejected the report on 2026-04-13 as "expected behavior" requiring "pre-existing administrative privileges," and on 2026-05-04 explicitly blocked CVE assignment — but the original attack path stopped functioning between 2026-04-13 and 2026-05-16, with new permission checks and authentication requirements appearing during that window. CERT/CC assigned VU#284781 on 2026-04-16 over Microsoft's objection.

**Timeline:** Discovery 2026-03-17 → MSRC submission → MSRC rejection 2026-04-13 → CERT/CC validation + VU#284781 issuance 2026-04-16 → Microsoft blocks CVE assignment 2026-05-04 → silent patch deployed during May 2026 → public disclosure 2026-05-16.

**Why it matters:** Independent of the specific bug, the disclosure-pattern signal is meaningful: a cloud-platform vendor silently patched a confirmed privilege-escalation issue without issuing a CVE, leaving downstream defenders without an authoritative record of which deployments needed re-audit. For organizations granting Azure Backup Contributor roles broadly (a common operational pattern given Backup Contributor's "should be safe, only backups" framing), there is no clean way to determine retroactively whether the role was abused before Microsoft silently patched. Cross-reference any Backup Contributor role assignments and any AKS backup-enablement events between March and May 2026 against your audit logs.

**Mitigation:**
- Audit every Azure Backup Contributor role assignment scope and recipient — the role's documentation framing is misleading until Microsoft formally documents the scope tightening.
- Review AKS audit logs (kube-apiserver) for unexpected `backup-vault` / `azure-backup` service-account access between 2026-03 and 2026-05, particularly any retrieval of `kube-system` Secrets.
- Constrain the Backup Contributor role to specific resource groups; never grant subscription-scope.
- Apply Azure Policy to alert on new AKS Trusted Access relationships being established.
- For VU#284781 tracking, monitor the CERT/CC advisory page rather than waiting for a CVE that will not be issued.

**Sources:** [BleepingComputer — Microsoft rejects critical Azure vulnerability report, no CVE issued](https://www.bleepingcomputer.com/news/microsoft/microsoft-rejects-critical-azure-vulnerability-report-no-cve-issued/) | [CERT/CC VU#284781](https://www.kb.cert.org/vuls/id/284781) | Researcher: Justin O'Leary

---

## 🟡 MEDIUM

(None this cycle.)

---

## 📋 Noted / Monitoring

**vm2 CVE-2026-45411 — Sandbox Breakout Using Async Generator (npm, GHSA-248r-7h7q-cr24, 2026-05-16)** — yet another vm2 sandbox escape via async generator semantics; reinforces the structurally-broken pattern documented since 2026-05-06 (vm2 is unsalvageable, migrate to isolated-vm).

**electerm CVE-2026-45353 — Local code execution via single-instance socket (npm, GHSA-7p5m-v798-f8vv, 2026-05-16)** — second electerm CVE in 48h after CVE-2026-45058 yesterday; continues the deprecation-candidate cluster signal.

**WWBN/AVideo second-batch CVEs (Composer, GHSA 2026-05-17)** — CVE-2026-43884 incomplete-fix on `isSSRFSafeURL()`, CVE-2026-45610 missing CSRF on 2FA toggle, CVE-2026-45580 stored XSS via unescaped stream key, plus a no-CVE passwordless-login-via-filename-manipulation issue. Same project as yesterday's CVE-2026-45578 OS command injection.

**better-auth no-CVE OAuth callback PKCE issue (npm, GHSA-wxw3-q3m9-c3jr, 2026-05-17)** — accepts mismatched OAuth state without PKCE; second better-auth issue in a week after yesterday's IPv6 rate-limiter bypass (CVE-2026-45364).

**rkyv panic safety bugs (Rust, GHSA-vfvv-c25p-m7mm, 2026-05-17)** — panic-safety bugs in serialization library allowing arbitrary code execution under specific conditions; widely-used Rust zero-copy deserialization crate.

**arnika UDP/PQC/KMS issues (Go, GHSA-rc6v-5rmx-w5mv, 2026-05-17)** — multiple issues in UDP source-port rotation, PQC handling, and KMS TLS validation; post-quantum-VPN niche.

**TeamPCP FIRESCALE Python toolkit C2-resilience research (Hunt.io 2026-05-14)** — 31-minute research deep-dive on TeamPCP's post-takedown persistence playbook: legitimate GitHub repos as C2 fallback, victim-account-as-relay, FIRESCALE Python loader updated post-takedown within hours. IOC value for SOCs hunting TeamPCP residue from Mini Shai-Hulud Wave 1/Wave 2 incidents.

**Net::Statsd::Lite CVE-2026-46719 — metric injection (Perl, oss-security 2026-05-16)** — versions before 0.9.0 allow metric-name injection; niche Perl monitoring library.

**Shai-Hulud "ships signed malicious TanStack, Mistral npm packages" framing (BleepingComputer 2026-05-16)** — relayer follow-up on the SLSA-attested-yet-malicious Wave 2 pattern documented 2026-05-13/-16; no new mechanism, no escalation. Tracked here for completeness; does not alter the Wave 2 update from yesterday.

**Schneier 2026-05-15 "Bypassing On-Camera Age-Verification Checks"** — biometric/age-verification bypass research; out of scope for perimeter defense but tracked for awareness.

**Apple May 2026 patches** — already noted in prior cycle; no change.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | BleepingComputer, The Hacker News, SecurityWeek, KrebsOnSecurity | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/KEV, nvd.nist.gov, cve.mitre.org, cve.org | ❌ (all WebFetch-blocked) |
| Vendor advisories | Rapid7, Fortinet PSIRT, MSRC, Cloudflare, Schneier | ✅ (MSRC blocked) |
| Research / OSINT | securitylab.github.com, GitHub Advisories, opencve.io, dbugs.ptsecurity, kb.cert.org/vuls, avleonov.com | ✅ |
| Supply chain | Socket, Aikido, Wiz, watchtowr labs (extras) | ✅ |
| Threat intel | hunt.io, SecurityAffairs (extras) | ✅ |
| Russian / regional | habr/tomhunter, teletype/cyberok, cert.gov.ua | ⚠️ (no new content; cert.gov.ua blocked) |
| Mailing lists | seclists.org/fulldisclosure, packetstormsecurity, oss-security | ⚠️ (seclists/packetstorm blocked; oss-security ✅) |
| Bug bounty | hackerone.com/hacktivity, bugcrowd.com/disclosures, attackerkb.com | ❌ (all WebFetch-blocked) |

**Errors:** cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403), github.com/search?q=CVE (403 / JS-only), attackerkb.com (403), seclists.org/fulldisclosure (redirect / archive empty), packetstormsecurity.com (redirect to packetstorm.news, content-thin), nvd.nist.gov (JS-only), cve.mitre.org (redirect to cve.org, JS-only), cve.org (JS-only), googleprojectzero.blogspot.com (redirect to projectzero.google, no recent), msrc.microsoft.com/blog (redirect, nav-only), hackerone.com/hacktivity (JS-only), bugcrowd.com/disclosures (404), cert.gov.ua (English content unavailable via WebFetch).

**CISA KEV:** Microsoft Exchange CVE-2026-42897 added 2026-05-16 (21-day federal deadline 2026-06-06). No other additions surfaced during this cycle. Saturday cycle — overall disclosure volume materially lower than weekday.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-17/night | Next: 2026-05-18/night*
