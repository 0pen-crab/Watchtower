# Watchtower Night Report — 2026-04-30
**Cycle:** Night | **Generated:** 2026-04-30 02:30 UTC (2026-04-30T02:30:00Z)
**Sources checked:** 23/30 | **CISA KEV total:** unreachable (cisa.gov 403) | **New KEV additions:** unverified (relayed via THN/SecurityWeek)

---

## 🔴 CRITICAL

### CVE-2026-41940 — cPanel & WHM Authentication Bypass via CRLF Injection (CVSS 9.8)
**Product:** cPanel & WHM (all currently supported branches) + WP Squared 11.136.1 | **CVE:** CVE-2026-41940 | **Status:** 0-Day → Patched, Active In-the-Wild Exploitation

CRLF injection in the cPanel/WHM login flow lets an unauthenticated remote attacker insert raw `\r\n` characters into a basic-authorization header; the system writes the resulting session file without sanitisation, allowing the attacker to plant arbitrary properties (e.g. `user=root`) and immediately load a privileged session against TCP/2083 (cPanel) or TCP/2087 (WHM). watchTowr Labs' detonation showed reliable, single-request takeover with no preconditions beyond network reachability. Public reports confirm in-the-wild exploitation predating disclosure — the bug was used as a zero-day against the management plane of a meaningful fraction of the public web. cPanel shipped fixes 11.110.0.97, 11.118.0.63, 11.126.0.54, 11.132.0.29, 11.134.0.20, 11.136.0.5 and WP Squared 11.136.1.7 within 2–3 hours of advisory publication on 2026-04-29.

**Timeline:** Pre-advisory in-the-wild exploitation observed → 2026-04-28: Namecheap and other large hosters block 2083/2087 ingress as precaution → 2026-04-29: cPanel issues coordinated advisory + patches; watchTowr / Rapid7 / VulnCheck publish technical analyses → 2026-04-30: PoC scripts and session-validation tooling circulating on GitHub.

**Why it matters:** Every cPanel/WHM box is a multi-tenant hosting plane: a single unauthenticated request gives root-equivalent control of the management UI, all hosted domains, all FTP/email/database accounts, and all customer data on that node. This is the densest single-host blast radius defenders will see this year, and exploitation tooling is already public — every internet-facing 2083/2087 must be patched or firewalled today.

**Discovered by:** watchTowr Labs (publicly disclosed and analysed); credit also to cPanel L.L.C. internal response team for the rapid fix.

**Mitigation:**
- Upgrade immediately to 11.110.0.97 / 11.118.0.63 / 11.126.0.54 / 11.132.0.29 / 11.134.0.20 / 11.136.0.5 (or 11.136.1.7 WP Squared).
- Until patched, block inbound TCP 2083 and 2087 at the network edge (do not rely on workarounds — patch is the correct fix).
- Hunt: review session-store files for sessions whose user property does not match the authenticated identity; review cPanel access logs for basic-auth headers containing `\r` or `\n` byte values; assume compromise on any pre-patch externally-reachable instance.
- Rotate API tokens, contact-shell SSH keys, and any credentials stored under cPanel-managed accounts on a host with externally-reachable 2083/2087 prior to patch.

**Sources:** [watchTowr Labs — The Internet Is Falling Down](https://labs.watchtowr.com/the-internet-is-falling-down-falling-down-falling-down-cpanel-whm-authentication-bypass-cve-2026-41940/) | [Rapid7 ETR Brief](https://www.rapid7.com/blog/post/etr-cve-2026-41940-cpanel-whm-authentication-bypass/) | [VulnCheck Advisory](https://www.vulncheck.com/advisories/cpanel-and-whm-authentication-bypass-via-login-flow) | [Namecheap Status — pre-advisory firewall](https://www.namecheap.com/status-updates/ongoing-critical-security-vulnerability-in-cpanel-april-28-2026/)

---

### Mini Shai-Hulud — SAP CAP npm Supply Chain Compromise with AI-Agent Persistence
**Product:** npm packages `mbt@1.2.48`, `@cap-js/db-service@2.10.1`, `@cap-js/sqlite@2.2.2`, `@cap-js/postgres@2.2.2` | **CVE:** None assigned (campaign IDs only) | **Status:** Active campaign — packages unpublished, 1,000+ exfiltration repos already on GitHub

A new TeamPCP-attributed worm calling itself "Mini Shai-Hulud" published trojanised versions of four official SAP Cloud Application Programming (CAP) packages on 2026-04-29 between 09:55 and 12:14 UTC. Each compromised package adds a `preinstall` hook that runs `setup.mjs`, which downloads the Bun JavaScript runtime to execute the `execution.js` payload — a credential stealer that harvests local creds, GitHub/npm tokens, GitHub Actions secrets, and AWS/Azure/GCP/Kubernetes secrets, then exfiltrates an encrypted bundle to a public GitHub repo created on the victim's own account titled "A Mini Shai-Hulud has Appeared." More notably, the payload attempts to propagate by writing `.claude/settings.json` (abusing Claude Code's `SessionStart` hook to re-execute the stealer when a developer opens the repo) and `.vscode/tasks.json` into every accessible repository — making this one of the first documented supply-chain campaigns to weaponise AI-coding-assistant configuration files as a propagation vector. As of 2026-04-29 evening, GitHub search for the marker string returned 1,000+ victim repos.

**Timeline:** 2026-04-29 09:55–12:14 UTC: malicious versions published → ~2026-04-29 14:00: Wiz / safedep / aikido / Snyk / StepSecurity / Onapsis publish independent analyses → 2026-04-29 evening: SAP and npm yank versions; victim auto-created repos remain on GitHub but are being mass-detected.

**Why it matters:** SAP CAP packages are present in many enterprise CI pipelines that hold cloud admin tokens — same blast radius as the original Shai-Hulud worm of late 2025 / TeamPCP March campaign. The novel propagation via `.claude/settings.json` and `.vscode/tasks.json` is the more important signal: any organisation running developer machines with AI coding agents must now treat `.claude/`, `.vscode/`, and similar agent-config directories as code that runs implicitly when a repo is opened, and audit them in CI.

**Discovered by:** Wiz Research, StepSecurity, safedep, Snyk, Onapsis, and Aikido Security (parallel responsible disclosure to npm/SAP).

**Mitigation:**
- Immediately pin/upgrade away from `mbt@1.2.48`, `@cap-js/db-service@2.10.1`, `@cap-js/sqlite@2.2.2`, `@cap-js/postgres@2.2.2`; verify nothing in your lockfiles still resolves to these.
- Rotate every credential the malicious payload could have reached: GITHUB_TOKEN / npm tokens / Actions secrets / AWS/Azure/GCP/k8s secrets used on any host that ran `npm install` after 09:55 UTC on 2026-04-29.
- Search GitHub org-wide for `.claude/settings.json` and `.vscode/tasks.json` files mentioning Bun or remote loaders that you did not author; treat hits as compromised and rotate everything that branch had access to.
- Add CI guardrails for AI-agent config files: prohibit committed `.claude/settings.json` / `.cursor/settings.json` / `.vscode/tasks.json` containing `SessionStart`/`runOn` hooks unless code-reviewed.
- Search GitHub for the marker `"A Mini Shai-Hulud has Appeared"` in repo descriptions to find any affected accounts you operate.

**Sources:** [Wiz — Mini Shai-Hulud SAP CAP analysis](https://www.wiz.io/blog/mini-shai-hulud-supply-chain-sap-npm) | [The Hacker News coverage](https://thehackernews.com/2026/04/sap-npm-packages-compromised-by-mini.html) | [Snyk — Bun-Based Stealer Hits SAP CAP](https://snyk.io/blog/bun-based-stealer-hits-sap-cap-js-mbt-npm-packages/) | [Onapsis — Emerging supply chain attack](https://onapsis.com/blog/sap-cap-mini-shai-hulud-supply-chain-attack/) | [Aikido — Mini Shai-Hulud has Appeared](https://www.aikido.dev/blog/mini-shai-hulud-has-appeared)

---

## 🟠 HIGH

### OpenEMR — 38 AISLE-Disclosed CVEs Including Unauthenticated Patient Data Exfiltration
**Product:** OpenEMR (open-source electronic medical records platform — ~100,000 healthcare-provider deployments, ~200M patients) | **CVE:** 38 CVE-2026-* (incl. CVE-2026-24898) | **CVSS:** up to Critical | **First reported:** 2026-04-28

AISLE's autonomous code analyzer ran against OpenEMR in Q1 2026 and produced 39 GitHub Security Advisories, 38 of which received CVE designations. The two highest-severity findings together permit an unauthenticated remote attacker to access and rewrite patient/provider records, dump the database, and achieve RCE on the application server — i.e. complete ePHI exfiltration at scale. CVE-2026-24898 is the keystone: an unauthenticated patient-identity disclosure flaw exploitable against any internet-reachable OpenEMR instance with no login. The remaining 36 issues are mostly missing/incorrect authorisation, plus stored XSS, SQL injection, path traversal, and improper session expiration. All 38 are patched in current OpenEMR releases as part of the responsible-disclosure programme; AISLE published the announcement on 2026-04-28 and SecurityWeek/HIPAA Journal/GovInfoSecurity covered it 2026-04-29.

**Mitigation:**
- Inventory all OpenEMR instances (including community-clinic deployments operated outside of central IT) and upgrade to the current patched release; confirm patch level for each by hash, not by tag.
- For internet-exposed OpenEMR portals where patching cannot happen today: block external access at the WAF/edge until patched — the unauth identity-disclosure bug needs no preconditions.
- Audit web-server access logs for the period before patching for unauthenticated access to patient-record endpoints; this is an HHS/HIPAA breach-notification trigger if pre-patch exposure is shown.
- Establish or expand an OpenEMR upgrade cadence — AISLE/OpenEMR partnership is now ongoing, more CVEs are likely.

**Sources:** [SecurityWeek — 38 Vulnerabilities in OpenEMR](https://www.securityweek.com/38-vulnerabilities-found-in-openemr-medical-software/) | [AISLE blog — 38 CVEs in OpenEMR](https://aisle.com/blog/aisle-discovers-38-critical-security-vulnerabilities-in-healthcare-software-used-by-100000-providers) | [HIPAA Journal coverage](https://www.hipaajournal.com/ai-analysis-38-flaws-openemr-platform/) | [GovInfoSecurity coverage](https://www.govinfosecurity.com/researchers-find-38-flaws-in-openemr-theyve-been-fixed-a-31520)

---

## 🟡 MEDIUM

### Qinglong Task Scheduler — CVE-2026-3965 / CVE-2026-4047 Unauth RCE Mass-Exploited for Cryptomining
**Product:** Qinglong distributed task-scheduler panel | **CVE:** CVE-2026-3965, CVE-2026-4047 | **Published:** 2026-04-29 (rollup; in-the-wild since 2026-02)

Two pre-auth bypass + RCE chains in Qinglong's Express.js URL routing — one in the `/open/* → /api/$1` rewrite and a second in case-insensitive path canonicalisation reaching `/api/system/command-run`. Attackers used either chain to reset admin credentials and write a payload into `config.sh`, which then downloaded a Linux x86_64 / ARM64 / macOS cryptominer (`.fullgc`) from `file.551911.xyz`. Operators began surfacing 85–100% CPU saturation on 2026-02-07, but only with Snyk's 2026-04-29 write-up did the underlying chain become public. Patched in Qinglong 2.20.2; PoC public on GitHub.

**Mitigation:** upgrade Qinglong to 2.20.2; remove `.fullgc` and any cron entries pointing at `file.551911.xyz`; rotate any credentials cached on the host. Qinglong is most often used in self-hosted automation/scraping setups — niche enterprise footprint but increasing on developer side-project boxes.

**Sources:** [Snyk — Qinglong RCE Flaws Exploited for Cryptomining](https://snyk.io/blog/qinglong-task-scheduler-rce-vulnerabilities/) | [PoC repo](https://github.com/MaxMnMl/Qinglong-Auth-bypass-to-RCE-poc)

---

## 📋 Noted / Monitoring

**CVE-2026-27825 — mcp-atlassian Path Traversal via ZIP Extraction (CVSS 9.3)** — MCP server unzips attacker-supplied archives without normalising paths, enabling write-anywhere on the MCP host. Adds to the running list of MCP-server unauth-RCE patterns.

**CVE-2026-34940 — KubeAI Command Injection via Ollama Model URL (CVSS 8.7)** — Unsanitised model-URL input reaches `child_process.exec`. Same pattern as the FastGPT/Langflow/MCP cluster — the Ollama URL is now a recurring sink.

**CVE-2026-41653 — BentoPDF (≤2.8.1) Stored XSS to File Exfiltration** — Niche; relevant only to organisations self-hosting BentoPDF as a document portal.

**CVE-2026-35029 — LiteLLM Broken Access Control on Config Endpoint (separate from CVE-2026-42208 covered 2026-04-29)** — Authenticated config endpoint accepts unauthorised reads/writes; fixed in nightly. Patch in concert with the SQLi.

**CVE-2026-42523 — Jenkins GitHub Plugin ≤1.46.0 Stored XSS** — Auth-required (Overall/Read), low blast radius; bumped to 1.46.0.1.

**CVE-2026-34975 — Plunk Email Header Injection (CVSS 8.5)** — Email transactional service; risk for any deployer using Plunk for password-reset / OTP email.

**CVE-2026-34160 — Chamilo LMS Unauthenticated SSRF (CVSS 7.5)** — Internal-network pivot from any internet-exposed Chamilo instance.

**CVE-2026-0972 — GoAnywhere MFT HTML Injection in Email Templating (<7.10.0)** — Pre-auth, fixed; lower-impact than the historical GoAnywhere chains but still worth scheduling.

**SAP HANA Cockpit / Database Explorer — Private X.509 Key Exposure (<2.18.2)** — Embedded private TLS key in shipped artifacts; rotate any cert that depended on Cockpit-issued material.

**CVE-2026-31431 — Linux Kernel AF_ALG Local Privilege Escalation** — LPE only; out of remote-services scope, mention only because exploit code is on GitHub and CI/jump-host hardening teams should plan a kernel update window.

**CVE-2026-5166 / CVE-2026-5161 — Pardus Software Center & About (CVSS 9.6 / 8.8)** — Niche Turkish government Linux distro; no broad relevance.

**Roblox account hijacking — 610,000 accounts seized, three Ukrainian arrests** — Consumer-platform credential theft, no enterprise relevance, useful as a phishing-pattern data point.

**Quick Page/Post Redirect WordPress plugin (70K+ installs) — five-year dormant backdoor disclosure** — Reporting today appears to extend the EssentialPlugin / "Kris" supply-chain campaign covered 2026-04-17; awaiting confirmation whether it is genuinely separate or a coverage artefact. If separate, will promote next cycle with details.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer, thehackernews, securityweek, krebsonsecurity, schneier | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (403 — relayed via THN/SecurityWeek) |
| Vendor research | rapid7, fortinet/threat-research, securitylab.github.com, blog.cloudflare.com/tag/security, msrc.microsoft.com/blog | ✅ / ⚠️ msrc no listing |
| CVE feeds | opencve.io, app.opencve.io, nvd.nist.gov, cve.org, cve.mitre.org | ✅ / ❌ JS-only |
| Research / OSINT | securitylab.github.com, kb.cert.org/vuls, avleonov.com, dbugs.ptsecurity.com, github.com/0xMarcio/cve, seclists.org/fulldisclosure | ✅ |
| Bug bounty | hackerone.com/hacktivity, bugcrowd.com/disclosures, attackerkb.com | ❌ (JS / 404 / 403) |
| Aggregators | github.com/search, packetstormsecurity → packetstorm.news, googleprojectzero → projectzero.google | ✅ / ⚠️ |
| Russian / UA TI | habr.com/ru/companies/tomhunter, teletype.in/@cyberok, cert.gov.ua | ⚠️ (no recent posts surfaced) |

**Errors:** cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403), attackerkb.com (403), bugcrowd.com/disclosures (404), hackerone.com/hacktivity (JS-only), cve.org (JS-only), cve.mitre.org (JS-only redirect to cve.org).
**CISA KEV:** cisa.gov unreachable; relayed coverage indicates no notable additions overnight beyond CVE-2026-32202 (Windows Shell, 2026-04-22 add) covered 2026-04-29.

---

*Watchtower vulnerability-researcher | Cycle: 2026-04-30/night | Next: 2026-05-01/night*
