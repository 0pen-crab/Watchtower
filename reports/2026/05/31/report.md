# Watchtower Night Report — 2026-05-31
**Cycle:** Night | **Generated:** 2026-05-31 (Sunday)
**Sources checked:** 21/30 | **CISA KEV new addition tracked:** CVE-2026-0257 (added 2026-05-29)

---

## 🔴 CRITICAL

### PAN-OS GlobalProtect CVE-2026-0257 — Authentication-Override Cookie Forgery Actively Exploited, KEV-Added with 3-Day Federal Deadline (CVSS 7.8)
**Product:** Palo Alto Networks PAN-OS + Prisma Access GlobalProtect portal/gateway | **CVE:** CVE-2026-0257 | **Status:** Active Exploitation + KEV (federal deadline 2026-06-01)

GlobalProtect installations with the authentication-override-cookie feature enabled (typical SSO-bridging deployments) accept attacker-forged cookies that bypass authentication entirely, granting full VPN ingress to the internal network. Rapid7 MDR confirmed successful exploitation across multiple customer environments beginning 2026-05-17 (Vultr-sourced wave) with a follow-on wave 2026-05-21 from Dromatics Systems infrastructure; in two confirmed cases the attacker received an internal VPN IP assignment immediately after cookie authentication. Both waves attributed to the same operator. CVSS was initially scored as Medium but escalated to High after exploitation confirmed; CISA added to KEV 2026-05-29 with an unusually compressed 3-day federal deadline (2026-06-01) matching the tempo of CVE-2026-0300 (captive portal) and Ivanti EPMM CVE-2026-6973.

**Timeline:** Palo Alto advisory published 2026-05-13 → Rapid7 detected first exploitation wave 2026-05-17 → second wave 2026-05-21 → Palo Alto + Rapid7 + CISA KEV co-publication 2026-05-29 → mainstream coverage 2026-05-30.

**Why it matters:** Third PAN-OS perimeter CVE of 2026 (after CVE-2026-0265 GlobalProtect SignatureKey and CVE-2026-0300 captive-portal KEV) and the second confirmed-in-wild PAN-OS bug in two months. GlobalProtect is the canonical perimeter-VPN footprint across enterprises with 100k+ internet-facing assets; the auth-override-cookie pattern is common at SSO-bridged sites with no compensating MFA challenge after cookie acceptance. With a same-operator multi-wave pattern this looks like a single APT or IAB ramping up — expect ransomware-affiliate uptake within 14 days following the typical PAN-OS-CVE-to-affiliate-monetisation cycle.

**Discovered by:** Rapid7 MDR (Christiaan Beek's team)

**Mitigation:**
- Upgrade to the patched PAN-OS / Prisma Access build (per 2026-05-13 Palo Alto advisory)
- If patching is blocked, disable the authentication-override-cookie feature on every GlobalProtect portal + gateway
- Alternatively, generate dedicated certificates used exclusively for authentication-override and rotate any cert that has been used since the bug was introduced
- Hunt for cookie-based VPN authentications without a corresponding upstream SSO event in IdP logs for the 2026-05-17 → present window
- Pull internal-VPN IP assignment logs and correlate with EDR for unfamiliar process activity from those IPs

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/palo-alto-globalprotect-vpn-auth-bypass-flaw-now-exploited-in-attacks/) | [TheHackerNews](https://thehackernews.com/2026/05/pan-os-globalprotect-authentication.html)

---

## 🟠 HIGH

### Flowise CVE-2026-40933 — Pre-Import Code Execution via Malicious Chatflow + MCP Tool (CVSS 9.9, Public PoC)
**Product:** FlowiseAI Flowise (self-hosted, all versions < 3.1.0) | **CVE:** CVE-2026-40933 | **CVSS:** 9.9 | **First reported:** 2026-04 (Obsidian Security) — PoC published 2026-05-30

A malicious Flowise chatflow JSON containing a Custom MCP Tool configured with an attacker-controlled command will execute that command during the canvas-enumeration step that runs *automatically when the workflow is imported* — no operator approval required, the canvas-render trigger fires before any user interaction. Obsidian Security published technical details + a one-click PoC on 2026-05-30; Flowise Cloud is unaffected because stdio MCP support is disabled in the managed offering, but self-hosted Flowise deployments (which dominate this ecosystem) are vulnerable by default until upgraded to 3.1.0. This is the second high-CVSS MCP-server-class CVE in the 60-day window (after the Anthropic mcp-server-fetch + Microsoft playwright-mcp SSRF pair noted 2026-05-25) and the latest entry in the **self-hosted AI infrastructure default-no-auth / import-side trigger** pattern alongside nginx-ui (KEV), Open WebUI, FastGPT, OpenClaw, ChromaDB, SGLang, and FUXA SCADA.

**Mitigation:**
- Upgrade Flowise to 3.1.0 or later immediately
- Block chatflow import from any source other than internal repos for the patch window
- Audit for unexpected child processes spawned by the Flowise service user since 2026-04
- Disable stdio MCP tools entirely if the deployment does not require them

**Sources:** [SecurityWeek](https://www.securityweek.com/exploit-code-published-for-critical-flowise-rce-vulnerability/) | [Obsidian Security disclosure (relayed)](https://www.securityweek.com/exploit-code-published-for-critical-flowise-rce-vulnerability/)

---

### CIFSwitch — 19-Year-Old Linux Kernel LPE to Root via CIFS Auth-Key-Description Forge + NSS Module Hijack (Public PoC)
**Product:** Linux kernel (cifs-utils path) — Mint 21.3/22.3, CentOS Stream 9, Rocky 9, Alma 9, Kali 2021.4–2026.1, SLES 15 SP7 confirmed vulnerable; Ubuntu/Debian/Pop!_OS/openSUSE/Oracle/Amazon Linux potentially vulnerable if cifs-utils installed | **CVE:** Pending assignment | **CVSS:** Not yet scored | **First reported:** 2026-05-30 (BleepingComputer disclosure)

Local unprivileged user forges a CIFS authentication key description, triggering namespace-switching code that loads an attacker-controlled NSS (Name Service Switch) module and executes code as root. Bug introduced in the kernel ~2007 (19 years dormant). Fixed via upstream kernel commit `3da1fdf`; downstream kernel package versions vary by distro. Public PoC on GitHub. Disclosed by Asim Viladi Oglu Manizada (SpaceX security engineer). Modern long-term-support kernels (Ubuntu 26.04, Fedora 40-44, CentOS Stream 10, Rocky 10, Alma 10, SLES 16, openSUSE Leap 16, Amazon Linux 2) are not affected.

Defensively this joins the 2026-Q2 Linux kernel page-cache / namespace LPE cluster (Copy Fail CVE-2026-31431 → K8s container escape, Dirty Frag CVE-2026-43284/43500, Fragnesia CVE-2026-46300, ssh-keysign-pwn CVE-2026-46333) — every previous bug in this run gained a K8s container-escape PoC within 14 days of the kernel LPE PoC. Treat this as a presumptive container-escape primitive on unpatched nodes by 2026-06-14.

**Mitigation:**
- Apply the kernel patch (commit 3da1fdf) via distro security update channel
- Until patched, prevent unprivileged users from inserting custom NSS module entries (`/etc/nsswitch.conf` write-protect, audit `LD_PRELOAD`/NSS plugin paths)
- Set `kernel.yama.ptrace_scope=2` to block PoC variants relying on ptrace-adjacent primitives
- Hunt for unexpected `cifsd`/CIFS keyring activity in audit logs since 2026-05-30

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/new-cifswitch-linux-flaw-gives-root-on-multiple-distributions/)

---

### sshfs ≤ 3.7.5 — CVE-2026-47187 Symlink Escape (CVSS 9.3) + CVE-2026-48711 SSH Argument Injection (CVSS 7.0)
**Product:** sshfs (FUSE-based SFTP filesystem client) | **CVE:** CVE-2026-47187, CVE-2026-48711 | **CVSS:** 9.3 / 7.0 | **First reported:** 2026-05-30 (oss-security)

**CVE-2026-47187 (CVSS 9.3):** A malicious SFTP server returns symlink targets with relative escapes (containing `..`) that bypass sshfs's `transform_symlinks` containment. Any subsequent `cp` (or equivalent path-resolving op) across the mount point lets the SFTP-server side read arbitrary local files back to the server *or* overwrite arbitrary local files with server-controlled bytes. The mount client is the victim — i.e. any host mounting an attacker-controlled SFTP share is exposed even if the server is otherwise read-only.

**CVE-2026-48711 (CVSS 7.0):** Mount-source strings of the form `[-oProxyCommand=CMD]:/path` bypass bracket-normalisation and let the caller execute arbitrary commands as the sshfs user without any SSH authentication round-trip. Applies to any automation passing user-influenced strings into sshfs invocation (autofs, web-UI mounters, NAS gateways).

Both fixed in sshfs 3.7.6 (2026-05-29), which introduces a `contain_symlinks` option (default-on, rejects absolute paths + `..`) and rejects hostnames beginning with `-` after bracket processing. Discovered and reported by Abhinav Agarwal.

**Mitigation:**
- Upgrade sshfs to 3.7.6 on every workstation, NAS, automation host, and CI worker that mounts SFTP shares
- Audit any wrapper that exposes mount-source strings to user input — validate against an allowlist before invocation
- For build pipelines using sshfs to pull artifacts, treat the SFTP server as untrusted code-execution surface even with the patch

**Sources:** [oss-security 2026-05-30](https://www.openwall.com/lists/oss-security/2026/05/30/3)

---

## 🟡 MEDIUM

### Apache MINA SSHD CVE-2026-48827 — Path Traversal in `sshd-git` Component
**Product:** Apache MINA SSHD `org.apache.sshd:sshd-git` 2.0.0 → 2.17.1 + 3.0.0-M1 → M3 | **CVE:** CVE-2026-48827 | **Published:** 2026-05-30

Authenticated SSH users can traverse outside the configured repository root during `git-upload-pack` / `git-receive-pack` because the git-bundle layer lacks path validation. Reach is limited to filesystem paths readable by the sshd service user, but on shared self-hosted git hosting setups built on MINA SSHD this is an authenticated-user-to-cross-repo-source-read primitive. Fixed in 2.18.0 and 3.0.0-M4. Reported by `j0hndo`.

**Mitigation:** Upgrade to 2.18.0 / 3.0.0-M4. Add filesystem-level access controls outside the sshd-git service user since Apache explicitly recommends defense-in-depth here.

**Sources:** [oss-security 2026-05-30](https://www.openwall.com/lists/oss-security/2026/05/30/1)

---

## 📋 Noted / Monitoring

**CVE-2026-49361 Apache Fluss Netty frame decoder DoS** — Memory exhaustion via crafted oversized Netty frames (oss-security 2026-05-30); only relevant if a Fluss endpoint is reachable from untrusted networks.

**Vim < 9.2.565 out-of-bounds read in terminal screen snapshot** — Client-side dev-tool only (oss-security 2026-05-30); no infra impact but worth flagging for dev workstation fleet patch.

**CVE-2026-8594 Perl Text::LineFold output duplication ≤ 2019.001** — Behavioral bug with potential security adjacency where the duplicated output crosses trust boundaries (oss-security 2026-05-30); narrow surface.

**CVE-2025-12686 Synology BeeStation OS AdminCenter buffer overflow (CVSS 9.8)** — Synology consumer/SMB NAS appliance RCE published 2026-05-30 via opencve.io; OOS for the core Watchtower scope unless BeeStation appears on enterprise periphery, but flagged for SMB-tier asset inventories.

**CVE-2025-70103 libjxl heap buffer overflow processing PBM** — Image library memory corruption (oss-security 2026-05-30); deserves a watch if libjxl is in the request-handling path for any user-supplied image processing (CDN edge transforms, document-conversion services).

**CVE-2025-70116 GPAC/MP4Box NULL pointer dereference on truncated MP4** — DoS-class; relevant where MP4Box is used in media-processing pipelines exposed to user uploads.

**CVE-2026-10120/10121/10122/10123 Trendnet TEW-432BRP CVSS 9.0 batch** — Four critical router CVEs via PT-Security dbugs 2026-05-30; SOHO/legacy router scope, OOS for enterprise but track for Mirai variant enrollment over the next 14 days.

**CVE-2026-10124 Shibby Tomato firmware CVSS 9.0** — Same PT-Security dbugs 2026-05-30 cycle; Tomato custom firmware running on commodity routers.

**CVE-2026-46527 cpp-httplib CVSS 8.7** — Header-only C++ HTTP library defect (PT-Security 2026-05-29); embedded server libraries warrant downstream-vendor-relay tracking before patches propagate to compiled appliances.

**CVE-2026-48501 GitHub CLI CVSS 7.4** — Local CLI tool flaw (PT-Security 2026-05-29); developer-workstation impact, OOS for infra but worth a dev-fleet update push.

**CVE-2026-44489 npm Axios** — Low-CVSS HTTP-client issue (PT-Security 2026-05-29); routine npm patch.

**Apache Tomcat CVE-2026-34486 EncryptInterceptor — new exploitation tooling momentum** — GitHub PoC repo (`striga-ai`/`404-src`/`Vozec`) gaining stars (now 68+ per github.com/0xMarcio/cve aggregator); existing-CVE → exploit-tooling escalation but no new defensive action beyond confirming the April patch is applied on Tomcat clusters running 4000/tcp Tribes.

**Signal recovery-key SMS phishing campaign (SecurityAffairs 2026-05-30)** — Threat actors impersonate Signal support via SMS to harvest backup recovery keys → decrypt message archive; targeted at journalists + activists; novel platform-trust-abuse pattern joins the 2026-Q2 social-engineering tradecraft cluster (Tycoon2FA Trustifi, KongTuke Teams, ChatGPhish Markdown).

**OSV.dev withdraws 157 false-positive malware reports across npm + PyPI (Socket.dev 2026-05-27)** — Mass false-positive incident in the supply-chain malware-feed ecosystem; not a vulnerability but a signal that automated supply-chain reputation tooling needs human review before enforcing blocks. Defenders relying on OSV.dev feed for npm/PyPI install-time blocking should verify rule-base provenance.

**23andMe (Chrome Holding Co.) California AG lawsuit over 2023 breach (BleepingComputer 2026-05-29)** — Litigation milestone, not a new technical incident.

**Google security engineer charged with Polymarket insider trading (BleepingComputer 2026-05-29)** — Insider-threat data point; non-vulnerability.

**Trump Mobile customer data breach** — Roundup-mentioned in SecurityWeek 2026-05-29 'In Other News'; vendor not specified, OOS.

**FBI 2025 Internet Crime Report published (Schneier 2026-05-27)** — Annual report; calibration data, no new CVE.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com, securityaffairs.com, helpnetsecurity.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ⚠️ unreachable — KEV CVE-2026-0257 surfaced via THN/BC/Rapid7 relay |
| Vendor advisories | fortinet.com/blog/threat-research, dbugs.ptsecurity.com, msrc.microsoft.com/blog | ✅ / ⚠️ |
| Research / OSINT | rapid7.com, schneier.com, blog.cloudflare.com/tag/security, hunt.io, socket.dev/blog, avleonov.com, googleprojectzero.blogspot.com (→ projectzero.google), securitylab.github.com | ✅ |
| Supply chain | github.com/advisories, github.com/0xMarcio/cve, socket.dev/blog | ✅ |
| Threat intel | kb.cert.org/vuls, opencve.io, openwall.com/lists/oss-security, seclists.org/fulldisclosure | ✅ |

**Errors:** cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403), attackerkb.com (403), msrc.microsoft.com/blog (nav-only redirect), hackerone.com/hacktivity (JS-required), bugcrowd.com/disclosures (404), cve.org (JS-required), cve.mitre.org (redirect to cve.org), cert.gov.ua (empty).
**Degraded:** packetstormsecurity.com (homepage navigation only — redirects to packetstorm.news), habr.com/ru/companies/tomhunter/articles (stale, March 2026 latest), teletype.in/@cyberok (stale, February 2026 latest).
**CISA KEV:** CVE-2026-0257 PAN-OS GlobalProtect added 2026-05-29 (federal deadline 2026-06-01). No other new KEV additions surfaced via the THN/BC/SecurityWeek/SecurityAffairs relays in the 2026-05-30 → 31 window.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-31/night | Next: 2026-06-01/night*
