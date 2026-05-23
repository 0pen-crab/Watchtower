# Watchtower Night Report — 2026-05-23
**Cycle:** Night | **Generated:** 2026-05-23 00:30 UTC
**Sources checked:** 21/30 | **CISA KEV new additions:** 2 (CVE-2025-34291 Langflow, CVE-2026-34926 Trend Micro Apex One)

---

## 🔴 CRITICAL

### Drupal SA-CORE-2026-004 CVE-2026-9082 — Highly Critical SQL Injection Actively Exploited Within 48 Hours of Patch (Internal 23/25)
**Product:** Drupal core 8.9 / 10.4 / 10.5 / 10.6 / 11.0 / 11.1 / 11.2 / 11.3 | **CVE:** CVE-2026-9082 | **Status:** Active Exploitation

Pre-announced via PSA on 2026-05-18, patched 2026-05-20 17:00–21:00 UTC; **BleepingComputer + SecurityWeek confirmed active exploitation on 2026-05-22** with mass scanning detected against thousands of sites within 48 hours of patch — matching the SA-CORE-2018-002 (Drupalgeddon 2) trajectory. Specially crafted requests trigger unauthenticated SQL injection through the database abstraction API on **PostgreSQL-backed sites** with confirmed RCE / privilege escalation / data disclosure impact. NIST has only assigned CVSS 6.5 but Drupal's internal score is 23/25 (the threshold for PSA pre-announcement is 20+/25 historically reserved for Drupalgeddon-class issues). Patched in 10.4.10 / 10.5.10 / 10.6.9 / 11.1.10 / 11.2.12 / 11.3.10; manual EOL patches shipped for 8.9.x / 9.5.x. Non-PostgreSQL sites still must update for upstream Symfony + Twig dependency fixes (CVE-2026-24425, CVE-2026-46633, CVE-2026-46639, CVE-2026-46640).

**Timeline:** 2026-05-18 PSA pre-announce → 2026-05-20 patches ship → 2026-05-22 confirmed active mass exploitation.

**Why it matters:** Drupal powers a long-tail of internet-facing government, education, NGO, and enterprise sites. Mass-exploitation tempo on Drupalgeddon-class bugs is historically 24-72h to fleet-wide compromise — the 48h-to-exploitation tempo on this one matches that exactly. PostgreSQL-backed Drupal is the high-risk subset (default for Acquia, Pantheon, many on-prem deployments). Patch SLAs for internet-facing Drupal fleet must be <12h from PSA, not <12h from patch.

**Discovered by:** Drupal Security Team coordinated disclosure (reporter not yet public).

**Mitigation:**
- Apply 10.4.10 / 10.5.10 / 10.6.9 / 11.1.10 / 11.2.12 / 11.3.10 immediately on any internet-facing Drupal site, regardless of database backend.
- For PostgreSQL-backed sites: assume web-shell drop happened during the 48h gap unless confirmed otherwise — run forensic sweeps against `sites/default/files/`, `sites/all/modules/`, and public upload paths.
- EOL 8.9.x / 9.5.x: apply the manual patches Drupal Security Team backported, then plan migration to supported branches (a PSA is the strongest signal that EOL coverage will not always be available).
- Deploy WAF rules blocking POSTs to `/node`, `/user`, `/admin/*` containing serialized PHP-object payloads or SQL keywords against PostgreSQL-syntax tells.
- Add EDR / runtime hunt rules for unexpected PHP child processes spawned by `httpd` / `nginx` worker users hosting Drupal sites.

**Sources:** [SecurityWeek](https://www.securityweek.com/drupal-vulnerability-in-hacker-crosshairs-shortly-after-disclosure/) | [BleepingComputer](https://www.bleepingcomputer.com/news/security/drupal-critical-sql-injection-flaw-now-targeted-in-attacks/)

---

## 🟠 HIGH

### Mini Shai-Hulud Wave 2 Expansion — TanStack PAT Theft → GitHub-Internal 3,800 Repo Breach + Megalodon 5,561-Repo CI/CD Campaign + Grafana TanStack-Linkage Confirmed
**Product:** GitHub-internal repos, GitHub Actions workflow ecosystem, Nx Console VSCode extension, TanStack-dependent npm packages | **CVE:** N/A | **CVSS:** N/A | **First reported:** 2026-05-13 (Wave 2 origin)

Three previously-discrete supply-chain incidents resolved into a single TeamPCP-linked cluster during 2026-05-21 → 2026-05-22 reporting: **(1) GitHub confirmed an employee installed a trojanized Nx Console VSCode extension** that exfiltrated 3,800 GitHub-internal repositories, with TeamPCP demanding ≥$50,000 on BreachForums; the same May 21 GitHub disclosure update **explicitly links the Nx Console compromise back to the TanStack npm Wave 2 supply-chain attack** (MEMORY 2026-05-13). **(2) Grafana Labs confirmed its 4-repo private-codebase theft (MEMORY 2026-05-18) was facilitated by a GitHub token compromised in the upstream TanStack incident** — closing the link between the pull_request_target → OIDC-token-theft Wave 2 primitive and the CoinbaseCartel extortion attempt. **(3) THN disclosed Megalodon**: a separate but TeamPCP-attributed campaign that pushed **5,718 malicious commits across 5,561 GitHub repositories in a 6-hour window on 2026-05-18** (11:36–17:48 UTC), forging author identities (`build-bot`, `auto-ci`, `ci-bot`, `pipeline-bot`), embedding base64 bash payloads in GitHub Actions workflows, and exfiltrating AWS / Google Cloud credentials, SSH keys, OIDC tokens, Vault tokens, Terraform creds, Docker / K8s configs, and GitHub tokens to **216.126.225[.]129:8443**. Wave 3 (2026-05-19 atool/@antv/timeago.js, MEMORY) already validated the Sigstore-provenance forgery primitive; this expansion validates the **TanStack OIDC-token theft as durable reentry vector** with at least three independent monetisation paths (Grafana extortion, GitHub-internal-repo theft, Megalodon mass-CI/CD harvest).

**Mitigation:**
- Immediately rotate any GitHub PATs / npm publish tokens / OIDC-trusted CI credentials touched by Nx Console / TanStack family dependencies between 2026-05-11 and now.
- Audit `pull_request_target` workflow misconfigurations across ALL public repos in the org — that is the Wave 2 primitive's entry point.
- Block egress from CI runners to `216.126.225.0/24` and add hunt rules for outbound port 8443 from any GitHub Actions runner.
- Hunt repository commit history for forged author identities matching `build-bot`, `auto-ci`, `ci-bot`, `pipeline-bot` published 2026-05-18 11:36–17:48 UTC (Megalodon window).
- Restrict VSCode Marketplace extensions for any employee with privileged GitHub access — enforce extension allow-list at the device-management tier; Nx Console (and any extension with cross-repo read scope) is the now-confirmed initial-access pattern.
- For TanStack-dependent npm projects: pin to known-good hashes published before 2026-05-13 OR after validated re-publish.

**Sources:** [BleepingComputer (GitHub breach)](https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/) | [BleepingComputer (Grafana TanStack link)](https://www.bleepingcomputer.com/news/security/github-links-repo-breach-to-tanstack-npm-supply-chain-attack/) | [SecurityWeek (Grafana)](https://www.securityweek.com/grafana-says-codebase-and-other-data-stolen-via-tanstack-supply-chain-attack/) | [THN (Megalodon)](https://thehackernews.com/2026/05/megalodon-github-attack-targets-5561.html)

---

### Trend Micro Apex One CVE-2026-34926 — Directory Traversal Zero-Day Actively Exploited, CISA KEV-Added With 2026-06-04 Federal Deadline
**Product:** Trend Micro Apex One (on-premise versions only) | **CVE:** CVE-2026-34926 | **CVSS:** 6.7 | **First reported:** 2026-05-22

Trend Micro disclosed and patched an actively-exploited directory traversal flaw in the on-premise Apex One management server allowing **an authenticated admin to modify a key table on the server and inject malicious code that is then deployed to every Apex One agent in the fleet**. CISA added the CVE to KEV on **2026-05-21 with federal deadline 2026-06-04** (14-day window). The admin-credential requirement constrains the attacker pool, but is the canonical APT initial-access primitive (Apex One admin creds are routinely harvested by ransomware affiliates via Teams-helpdesk-impersonation campaigns — MEMORY 2026-05-15 KongTuke pattern). Apex One joins the **EDR-equivalent multi-tenant pivot point** class (MEMORY 2026-05-14 Quest KACE SMA) — agent-push-malicious-code from a compromised management server compromises every endpoint downstream. CISA's catalog already lists 10 other Apex-related CVEs.

**Mitigation:**
- Apply Trend Micro's patches immediately on every on-prem Apex One management server.
- Audit agent-push job history for unexpected key-table modifications or unknown SHA-256s in deployed updates dating back 30+ days.
- Treat Apex One admin credentials as crown-jewel: enforce just-in-time elevation, FIDO2 MFA, hardware-keyed admin workstations.
- Hunt EDR / SIEM for unusual TrendMicro-process child-process launches or Apex agent updates outside normal patch windows.

**Sources:** [SecurityWeek](https://www.securityweek.com/trendai-patches-apex-one-zero-day-exploited-in-the-wild/) | [THN (KEV)](https://thehackernews.com/2026/05/cisa-adds-exploited-langflow-and-trend.html)

---

### Ubiquiti UniFi OS 5-CVE Maximum-Severity Batch — CVE-2026-34908 / 34909 / 34910 + 33000 + 34911 Affect 100,000+ Internet-Exposed Consoles
**Product:** Ubiquiti UniFi OS (UniFi Cloud Gateway, UniFi Dream Machine, Cloud Key) — powers UniFi Network / Protect / Access / Talk / Connect | **CVE:** CVE-2026-34908, CVE-2026-34909, CVE-2026-34910, CVE-2026-33000, CVE-2026-34911 | **CVSS:** Multiple max-severity | **First reported:** 2026-05-22

Five vulnerabilities patched in a single coordinated release via Ubiquiti's HackerOne bug bounty program: **CVE-2026-34908** improper access control (unauth changes to targeted system), **CVE-2026-34909** path traversal (file access on the underlying system + account-access manipulation), **CVE-2026-34910** command injection (post-network-access OS command execution), **CVE-2026-33000** critical command injection, **CVE-2026-34911** high-severity information disclosure. Low attack complexity, minimal attacker privileges required for several of these. **Censys tracks ~100,000 internet-exposed UniFi OS endpoints (50,000 in the US)** — UniFi consoles are deployed widely at small/medium business and prosumer home networks where they often act as the perimeter device. Historical Ubiquiti CVEs have been quickly enrolled into IoT botnets (Mirai variants, dnsmasq DNS hijacking campaigns); no confirmed active exploitation at disclosure but the at-risk fleet is large and patch tempo is historically slow.

**Mitigation:**
- Apply Ubiquiti's UniFi OS security updates on every console — particularly any internet-exposed device.
- Restrict UniFi OS management plane to VPN / management VLAN; do not expose port 443 / 22 / 8443 to the public internet.
- Hunt UniFi consoles for unexpected child processes, ssh authorized_keys additions, or outbound network connections to non-Ubiquiti destinations.
- Disable remote (non-LAN) admin access where not strictly required.

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/ubiquiti-patches-three-max-severity-unifi-os-vulnerabilities/)

---

### Langflow CVE-2025-34291 Promoted to CISA KEV With MuddyWater Attribution + 2026-06-04 Federal Deadline
**Product:** Langflow open-source LLM workflow IDE | **CVE:** CVE-2025-34291 | **CVSS:** 9.4 | **First reported:** 2025 (Langflow), KEV addition 2026-05-21

CISA added Langflow CVE-2025-34291 to KEV alongside the Apex One CVE on 2026-05-21 with federal deadline 2026-06-04. The bug chains three weaknesses — overly permissive CORS, missing CSRF protection, and an endpoint that allows code execution by design — for unauthenticated remote code execution on any internet-exposed Langflow instance. Critically, THN's KEV writeup confirms **Iranian state-sponsored MuddyWater leveraged CVE-2025-34291 as initial network access** per March 2026 analysis. Langflow is now the fourth AI-platform CVE on KEV in 2026 (after nginx-ui MCP path, Ivanti EPMM, LiteLLM CVE-2026-42208 — MEMORY 2026-05-12), confirming the **default-no-auth self-hosted AI infrastructure pattern as a state-actor initial-access surface** (MEMORY 2026-05-06 Intruder Labs 1M-instance scan; Pattern Library). Companion KEV add today (Apex One CVE-2026-34926) brings the KEV add count to 2 in a single day.

**Mitigation:**
- Apply Langflow security updates on every self-hosted instance; do not expose Langflow to the public internet.
- For internet-exposed Langflow instances, assume MuddyWater (or copycats) have reached the instance — incident response with full forensic clearance is the default posture, not patch-and-monitor.
- Treat every self-hosted AI workflow / LLM-IDE / model-serving platform (Langflow, Flowise, LangChain UI, n8n) as MuddyWater-class APT initial-access surface; segment from production estate.

**Sources:** [THN](https://thehackernews.com/2026/05/cisa-adds-exploited-langflow-and-trend.html)

---

### golang.org/x/crypto/ssh 5-CVE Batch — SignatureKey Revocation Bypass, FIDO/U2F Touch Bypass, Integer Overflow Infinite Write Loop
**Product:** golang.org/x/crypto/ssh (Go SSH library — used by Hashicorp Terraform / Vault / Consul / Boundary, K8s ssh agents, gitleaks, Caddy, every Go SSH client/server) | **CVE:** CVE-2026-39829, CVE-2026-39830, CVE-2026-39831, CVE-2026-39834, CVE-2026-42508 (also OpenSSH CVE-2026-39832, golang/x/crypto CVE-2026-39833 in same batch) | **CVSS:** 7.5–9.1 | **First reported:** 2026-05-22

Five-CVE coordinated drop in Go's `crypto/ssh` library spanning multiple high-impact failure modes: **CVE-2026-42508** — revoked SignatureKeys not properly checked, both key and SignatureKey now validated for revocation; **CVE-2026-39831** — FIDO/U2F security keys lacked user presence verification, enabling unattended use without physical touch; **CVE-2026-39830** — malicious SSH peers can block connection read loops with unsolicited responses (resource leak per connection); **CVE-2026-39834** — integer overflow in SSH channel writes >4GB causes the write loop to spin indefinitely sending empty packets (DoS amplification); **CVE-2026-39829** — RSA/DSA key parsers lacked size limits, crafted keys cause several minutes of CPU consumption during signature verification (DoS). Companion OpenSSH CVE-2026-39832 (CVSS 9.1) and golang/x/crypto CVE-2026-39833 (CVSS 9.1) ship in the same window. Go's SSH library is the back-end for nearly every Go-based DevOps / SRE / cloud-infra tool that does SSH (Terraform `remote-exec`, Consul Connect, Vault SSH secrets engine, Boundary, K8s kubelet ssh-jump, gitleaks, etc.).

**Mitigation:**
- Upgrade `golang.org/x/crypto` to the patched version across every Go-based service in the fleet — particularly anything that accepts inbound SSH or processes attacker-supplied SSH keys (Vault SSH secrets engine, Boundary SSH targets, Terraform Cloud agents, K8s ssh-jump providers).
- Audit FIDO/U2F SSH config for explicit `verify-required` flags; default `verify-discouraged` keys are exposed to CVE-2026-39831 unattended-use bypass.
- Revoke and rotate any SignatureKey-using SSH certificates issued before patch — the CVE-2026-42508 fix changes the revocation check semantics.
- For Go-based SSH servers exposing port 22 to attacker-controlled networks: rate-limit RSA/DSA key parsing to mitigate CVE-2026-39829 CPU-burn DoS until patched.

**Sources:** [OpenCVE](https://app.opencve.io) | [PT-Security dbugs](https://dbugs.ptsecurity.com)

---

## 🟡 MEDIUM

### Microsoft May 2026 Patch Tuesday Late-Disclosure Batch — 5× CVSS 10.0 Azure-Adjacent + CVE-2026-33117 Azure SDK for Java Key Vault Auth-Tag Bypass
**Product:** Microsoft Entra ID, Azure Resource Manager, Azure Local, Azure Orbital Space SDK, Planetary Computer Pro, Power Pages, Azure SDK for Java | **CVE:** CVE-2026-42901, CVE-2026-47280, CVE-2026-41104, CVE-2026-23652, CVE-2026-40412, CVE-2026-33117, CVE-2026-42822 | **Published:** 2026-05-21 / 2026-05-22

PT-Security dbugs surfaced a follow-on Microsoft disclosure cluster on 2026-05-21 / 22 — five **CVSS 10.0** Azure-adjacent bugs not in the original 2026-05-13 Patch Tuesday relayer summaries: **CVE-2026-42901 Entra ID origin validation error** (unauthorized privilege elevation over network), **CVE-2026-47280 Azure Resource Manager**, **CVE-2026-41104 Planetary Computer Pro deserialization** (information disclosure), **CVE-2026-23652 Power Pages**, **CVE-2026-40412 Azure Orbital Space SDK**, plus high-severity **CVE-2026-33117 Microsoft Azure SDK for Java Key Vault** (CVSS 9.1) incorrect authentication-tag comparison bypassing Key Vault integrity checks via specially-crafted encrypted input. CVE-2026-42822 Azure Local Disconnected Operations was previously noted (MEMORY 2026-05-19) with no patch available. This is the third instance in 60 days of the **Patch Tuesday relayer divergence pattern** (MEMORY 2026-05-14 MDASH disclosure pattern) — Microsoft drops CVSS 10.0 cloud-platform bugs in the Patch Tuesday tail that BleepingComputer / THN / SecurityWeek individual relayers don't enumerate. Treat MSRC / Microsoft Security Update Guide as the only authoritative Patch Tuesday source.

**Mitigation:** Cloud-side: Microsoft has patched server-side for Entra ID / Azure Resource Manager / Planetary Computer Pro / Power Pages — confirm tenant-level patch propagation via Microsoft Service Health. For Azure SDK for Java: upgrade affected versions across every JVM-based service that touches Azure Key Vault. For self-hosted Azure Local: still no public patch — apply MSRC mitigations only.

**Sources:** [OpenCVE](https://app.opencve.io) | [PT-Security dbugs](https://dbugs.ptsecurity.com)

---

### SonicWall Gen6 SSL-VPN CVE-2024-12802 — MFA Bypass via Incomplete Patch + Manual LDAP Reconfig Required
**Product:** SonicWall Gen6 SSL-VPN appliances (Gen7 / Gen8 less affected) | **CVE:** CVE-2024-12802 | **Published:** SNWLID-2025-0001

ReliaQuest disclosed on 2026-05-21 that the SonicWall MFA-enforcement bug fix shipped earlier in 2025 (SNWLID-2025-0001) **is not effective by default on Gen6 devices** — administrators must manually delete existing LDAP configurations that use `userPrincipalName`, remove cached LDAP users, remove SSL VPN User Domain settings, reboot, and recreate LDAP configuration. Devices that received the firmware patch appear remediated but remain exploitable. Active exploitation: attackers brute-force VPN credentials, exploit the still-present bypass to skip MFA, and pivot to internal recon + Cobalt Strike + BYOVD techniques within 30-60 minutes. ReliaQuest assesses the pattern is **initial-access broker selling VPN credentials to ransomware affiliates** based on deliberate logout/login patterns. Classic "incomplete patch" pattern matching the MEMORY 2026-05-06 Apache MINA incomplete-fix cluster — silent patching of one code path while leaving the operational config exposed.

**Mitigation:**
- For Gen6 SonicWall SSL-VPN appliances: follow SNWLID-2025-0001 *complete* mitigation steps (LDAP reconfig + cached-user clear + domain-setting removal + reboot + LDAP recreate) — firmware patch alone is insufficient.
- Audit VPN auth logs for the deliberate-rotation pattern (multiple short-duration logins from different accounts over hours) as an IAB tell.
- Rotate VPN account credentials suspected of compromise; enforce MFA via FIDO2 / TOTP not LDAP-side UPN.

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-bypass-sonicwall-vpn-mfa-due-to-incomplete-patching/) | [SonicWall PSIRT](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2025-0001)

---

## 📋 Noted / Monitoring

**Apache CXF 3-CVE batch (CVE-2026-44417 / 44618 / 44930)** — CVE-2026-44417 incomplete fix for CVE-2025-48913 JMS-untrusted-config-to-RCE; CVE-2026-44618 XXE in WS-Transfer; CVE-2026-44930 LDAP injection in XKMS LDAP Repository. Apache CXF widely embedded in Java SOAP / WS-* stacks — track per the MEMORY 2026-05-06 Apache MINA incomplete-fix recurrence pattern (this is now another Apache project shipping an incomplete-fix CVE on its prior fix).

**7-Zip multi-CVE memory corruption batch (CVE-2026-48095, 48092, 48101-104, 48111-112 — GHSL-2026-115/116/117/118/119/120/121/122/140)** — Jaroslav Lobačevski / GitHub Security Lab disclosed 9+ memory corruption issues in 7-Zip. Primarily client-side but 7-Zip is widely embedded in CI/CD (archive extraction in GitHub Actions, GitLab CI, Jenkins) — exposed surface if any CI step decompresses attacker-controlled archives.

**CVE-2026-46639 + CVE-2026-46640 Twig (continued)** — Two more Twig escape primitives shipped alongside yesterday's CVE-2026-24425 + CVE-2026-46633 batch: `_self.(<string>)` macro-reference compilation arbitrary PHP execution + object-destructuring assignment property/method bypass. Same Twig 3.26.0 upgrade addresses; Drupal SA-CORE-2026-004's upstream Twig coverage includes these.

**CVE-2026-46680 containerd `runAsNonRoot` bypass (GHSA-fqw6-gf59-qr4w)** — user ID handling bypass allows runAsNonRoot evasion in containerd; container-runtime security primitive break worth tracking for K8s shops relying on `runAsNonRoot` as a hardening control.

**CVE-2026-45401 Open WebUI SSRF (high-severity)** — fifth high-severity Open WebUI CVE in 45 days (after CVE-2026-44551 LDAP, 44549 XSS, 44566 path-traversal-RCE, 44567 authz). Confirms the MEMORY 2026-05-10 Open WebUI deprecation-candidate code-quality pattern — internal-resource access via redirect-bypass URL validation.

**CVE-2026-9256 NGINX ngx_http_rewrite_module buffer overflow** — Alan Coopersmith oss-security disclosure 2026-05-22; companion / follow-up to CVE-2026-42945 NGINX Rift (MEMORY 2026-05-15). Tracks the post-NGINX-Rift adjacent-code-path AI-finding recurrence pattern.

**CVE-2026-41076 / 41075 / 41074 Bestpractical RT batch** — LDAP/AD auth bypass (CVSS 8.1), authenticated SQL injection (8.8), CSRF (7.1). Bestpractical RT (Request Tracker) is internal IT ticketing — bypass yields any LDAP-backed user identity without password.

**CVE-2026-46670 yeswiki/yeswiki (Composer) unauth SQL injection** — GHSA-jwvv-qr7q-cv8j; niche but PHP-CMS class CVE.

**CVE-2026-46701 @network-ai/network-ai (npm) Empty Default Secret** — tool-invocation cross-origin access without authentication; another default-no-auth AI infra advisory in the MEMORY 2026-05-06 Intruder Labs ecosystem-pattern.

**CVE-2024-48019 Apache Doris arbitrary file read on REST API logging endpoint** — disclosed via GitHub Security Lab GHSL-2024-293; data-warehouse engine, internal-network surface.

**CVE-2026-29075 Mesa benchmarks.yml workflow RCE** — GHSL-2025-009; another GitHub Actions workflow misconfiguration (similar primitive class as the Mini Shai-Hulud Wave 2 pull_request_target chain) on a major open-source project.

**Chatwoot SQL injection (GHSL-2026-059)** — Man Yue Mo / GitHub Security Lab; customer support platform SQL injection.

**HPLIP Privilege Escalation + Arbitrary Code Execution (oss-security 2026-05-23)** — HP Linux Imaging and Printing system; relevant for Linux dev/admin workstations with HP printer drivers.

**CVE-2026-33642 / 33633 Kitty terminal heap buffer overflow (CVSS 9.8 / 8.8)** — image-loading and graphics-protocol bugs in Kitty GPU terminal; client-side only, OOS for normal scope but flagged for dev-workstation hardening.

**CVE-2024-9643 Four-Faith F3x36 industrial router mass exploitation (CrowdSec 2026-05-22)** — hardcoded credentials in industrial cellular routers; OT-adjacent, mass IoT-botnet enrollment.

**Showboat → JFMBackdoor Windows expansion (Calypso / Red Lamassu)** — Calypso China-aligned cluster (MEMORY 2026-05-22 Showboat) also ships Windows-side JFMBackdoor (DLL-sideload via `fltMC.exe` + `FLTLIB.dll`); minor expansion of yesterday's News item.

**Huawei enterprise router 0-day → Luxembourg national telecom 3-hour outage (July 2025)** — disclosed retroactively via SecurityWeek "In Other News" 2026-05-22; not actionable (incident historical) but a critical-infrastructure data point.

**Iranian hackers breach US gas station tank monitors** — ATG systems compromised via unauthenticated internet-exposed devices; display-only manipulation, no physical impact. CISA / FBI advisory framing only.

**CVE-2026-31635 Linux kernel rxgk DirtyDecrypt LPE** — page-cache LPE in rxgk; PoC released 2026-05-19. Per the MEMORY page-cache-LPE → K8s container-escape 14-day rule, expect K8s escape PoC by ~2026-06-02.

**Anthropic Mythos discovered macOS M5 kernel exploit + Cloudflare published Project Glasswing / Mythos comparison** (Schneier 2026-05-21, Cloudflare 2026-05-18) — companion data points to the MEMORY 2026-05-14 AI bug-finder labs pattern; Mythos extends the disclosure-class to mobile/macOS kernel.

**Anthropic + Cloudflare ship "Claude Managed Agents" + Claude Compliance API integration (2026-05-19 / 2026-05-21)** — Cloudflare CASB monitoring of Claude Enterprise activity. Calibration data point on the broader AI-control-plane integration trend.

**Microsoft DCU Fox Tempest follow-on** — implicit calibration: 90-day retroactive WDAC / ASR hunts on revoked-cert thumbprints from MEMORY 2026-05-19 takedown remain the canonical IR action; no new artifacts surfaced in this cycle.

**P2Pinfect K8s compromise (Fortinet 2026-05-20)** — unprotected Redis-via-misconfigured-GKE persistent enrollment into P2P botnet; reinforces the MEMORY 2026-05-06 self-hosted-default-no-auth posture pattern, here for Redis on K8s rather than AI-infra.

**VU#980487 Dirty Frag CERT/CC vu# issued 2026-05-20** — CERT/CC issuance for CVE-2026-43284 / 43500 Linux kernel page-cache write LPE (MEMORY 2026-05-09); upstream patch still pending. Track for K8s escape PoC arrival per the MEMORY page-cache → container-escape 14-day rule.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | BleepingComputer, The Hacker News, SecurityWeek, KrebsOnSecurity, Schneier | ✅ |
| CISA / US Gov | cisa.gov, KEV catalog, cert.gov.ua | ❌ (403 / sparse) |
| Vendor advisories | MSRC blog, projectzero.google, blog.cloudflare.com/tag/security, fortinet/threat-research, securitylab.github.com | ✅ (MSRC sparse) |
| Research / OSINT | Rapid7, github.com/0xMarcio/cve, avleonov.com, seclists/fulldisclosure, openwall oss-security, kb.cert.org/vuls, dbugs.ptsecurity, github.com/advisories | ✅ |
| CVE databases | OpenCVE, NVD | ✅ |
| Supply chain | (covered via Endor Labs / Socket / Aikido relayed via THN / SW) | ✅ |
| Threat intel | (covered via Hunt.io / Trend Micro / Cyera relayed via THN / SW) | ✅ |

**Errors:** cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403), attackerkb.com (403), cve.mitre.org (JS-only redirects to cve.org), cve.org (JS-only), msrc.microsoft.com/blog (redirects, sparse content), hackerone.com/hacktivity (JS-only), bugcrowd.com/disclosures (404), cert.gov.ua (sparse content via WebFetch). Degraded: packetstormsecurity.com (redirect to packetstorm.news, latest/files endpoint shows ToS only), habr.com/ru/companies/tomhunter (no posts since March 2026), teletype.in/@cyberok (no posts since February 2026), seclists.org/fulldisclosure (reachable but no posts in 2026-05-18→23 window).

**CISA KEV:** 2 new additions on 2026-05-21 (CVE-2025-34291 Langflow with MuddyWater attribution, CVE-2026-34926 Trend Micro Apex One). Federal deadline: 2026-06-04.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-23/night | Next: 2026-05-24/night*
