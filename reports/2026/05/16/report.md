# Watchtower Night Report — 2026-05-16
**Cycle:** Night | **Generated:** 2026-05-16 00:30 UTC
**Sources checked:** 14/30 | **CISA KEV total:** unchanged (gateway 403) | **New KEV additions:** none confirmed today (CVE-2026-20182 Cisco SD-WAN federal deadline still 2026-05-17)

---

## 🔴 CRITICAL

### Cisco Catalyst SD-WAN CVE-2026-20182 — Talos Attribution To UAT-8616, "Sixth Exploited Zero-Day of 2026" Per SecurityWeek; Federal Deadline Now <36 Hours *(Update on 2026-05-15 coverage)*
**Product:** Cisco Catalyst SD-WAN Controller and Cisco Catalyst SD-WAN Manager (on-prem + SD-WAN Cloud) | **CVE:** CVE-2026-20182 | **Status:** 0-Day (Active Exploitation / KEV)

Yesterday's News entry carried CVE-2026-20182 at threat_score 9 with attribution to threat actor UAT-8616 referenced as "previously exploited CVE-2026-20127." Today's developments materially extend the picture: (1) **Rapid7's full technical writeup** (2026-05-15) attributes the bug to a flaw in Cisco's peering authentication code that authenticates the *signature on a peer certificate* but skips validation of the certificate-subject field — an attacker presenting a self-signed cert with a `vmanage-admin` subject is logged in as that internal role; (2) **SecurityWeek framed CVE-2026-20182 as "the sixth exploited zero-day of 2026"** in Cisco-specific perimeter-class infrastructure, joining the cluster of CVE-2026-20127 (March SD-WAN), CVE-2026-20034/20035 (Cisco Unity Connection, May 8), and prior SD-WAN/IOS XE issues; (3) **CISA KEV federal deadline is 2026-05-17** — less than 36 hours from publication of this report. **Rapid7 published a Metasploit-ready exploitation primitive in their 2026-05-15 ETR post**.

**Timeline:** Zero-day exploitation observed by Cisco TALOS → patch shipped → public advisory 2026-05-14 → CISA KEV add 2026-05-14 (federal deadline 2026-05-17) → Rapid7 technical writeup + Talos UAT-8616 attribution 2026-05-15.

**Why it matters:** The Rapid7 writeup converts "Cisco confirms limited ITW exploitation" into a much higher exposure tempo — any environment with an internet-facing Catalyst SD-WAN Controller / Manager is presumptively compromised. The UAT-8616 attribution + "sixth exploited zero-day of 2026" framing reframes this as a sustained Cisco perimeter targeting campaign, not a single advisory event. Federal patch deadline is tomorrow.

**Discovered by:** Rapid7 (Jonah Burgess, Stephen Fewer) during follow-up research on CVE-2026-20127.

**Mitigation:**
- Confirm Cisco Catalyst SD-WAN Controller/Manager is on the patched release; no workaround exists.
- Audit `/var/log/auth.log` for `Accepted publickey for vmanage-admin` from non-corporate IP ranges since 2026-04-01.
- Treat any non-corporate IP that completed peering authentication in the audit window as compromised; rotate vManage admin credentials and TLS material.
- Remove internet exposure of SD-WAN management plane; require dedicated management VPN with MFA.
- Hunt for unexpected SD-WAN policy changes, rogue peer additions, configuration template pushes, and template versions originating from non-CICD user accounts since 2026-04-01.
- For SD-WAN Cloud: confirm Cisco managed-service IR has rotated tenant credentials.

**Sources:** [Rapid7 ETR — CVE-2026-20182 Critical Authentication Bypass in Cisco Catalyst SD-WAN Controller (FIXED)](https://www.rapid7.com/blog/post/2026/05/15/cve-2026-20182-critical-authentication-bypass-in-cisco-catalyst-sd-wan-controller/) | [SecurityWeek — Cisco SD-WAN Zero-Day (Sixth in 2026)](https://www.securityweek.com) | [BleepingComputer — Cisco SD-WAN flaw exploited in zero-day attacks](https://www.bleepingcomputer.com/news/security/)

---

### Mini Shai-Hulud Wave 2 — TeamPCP Publishes Full Worm Source Code, Removing Replication-Barrier For Copycat Actors *(Update on 2026-05-13 / 2026-05-15 coverage)*
**Product:** Mini Shai-Hulud npm worm primitive (Wave 2 affecting TanStack + UiPath + Mistral-published packages) | **CVE:** CVE-2026-45321 | **CVSS:** —

Three days after the Wave 2 wave broke (2026-05-12 → 169 packages), and one day after TeamPCP and BreachForums announced a $1,000 prize contest, **TeamPCP has now published the Wave 2 worm source code on BreachForums** (per SecurityWeek 2026-05-15). The release explicitly includes the `pull_request_target` workflow misconfiguration chain, GitHub Actions cache poisoning module, OIDC token theft from `Runner.Worker` memory, and the orphaned-commit-via-optional-dependency propagation primitive that Endor Labs documented as the novel Wave 2 mechanic. The source release converts a single-actor campaign primitive into a public toolkit: any actor with mid-tier npm/PyPI publishing access can now run the full Wave 2 chain without re-engineering the OIDC theft + SLSA-attested-yet-malicious payload mechanism.

**Why this is a material update vs. 2026-05-15 coverage:** Yesterday's update framed the $1,000 contest as an incentive escalation. Today's source release converts the worm primitive into commodity tooling — the same evolution as Mirai (2016 source release → 100+ Mirai variants within 12 months) and Conti (2022 source release → ContiLite + variants). Combined with the still-active contest, expect 3-7 distinct Wave-2-class supply-chain compromises by 2026-06-15. Adjust hunt rules and code-review policy on `pull_request_target` workflows, OIDC scopes, and optional-dependency content to assume Wave-2-class attempts are imminent against every public npm/PyPI publisher with a reasonable footprint.

**Mitigation:**
- Audit every public-package workflow for `pull_request_target` triggers; replace with `pull_request` + manual approval gate, or use a hardened orchestrator (e.g., `actions-permissions`).
- Restrict OIDC token scopes to absolute minimum; never grant write permissions to the `id-token` in PR-driven workflows.
- Add hunt rules for orphaned commits referenced via `optional dependencies` in `package.json` / `pyproject.toml`.
- Treat `SLSA attestation valid` as necessary-but-not-sufficient (per MEMORY pattern); pair with content review of optional dependencies and post-install scripts.
- For organisations with private npm registries: enable mirror-only mode (no transparent passthrough) for the next 60 days while copycat actors come online.

**Sources:** [SecurityWeek — TeamPCP Releases Shai-Hulud Worm Source Code](https://www.securityweek.com) | [Endor Labs — Mini Shai-Hulud Wave 2 Technical Analysis](https://www.endorlabs.com/blog) | [Socket — Shai-Hulud Worm Source Release](https://socket.dev/blog)

---

### Microsoft Exchange Server CVE-2026-42897 — Active Exploitation Confirmed By Microsoft, Mitigations Shipped, No Permanent Patch Yet *(Promotion of 2026-05-15 Noted item)*
**Product:** On-premises Microsoft Exchange Server (Exchange 2019 CU14/CU15, Exchange 2016 CU23 — Outlook Web Access / OWA component) | **CVE:** CVE-2026-42897 | **CVSS:** 8.1

Yesterday's report carried CVE-2026-42897 as a Noted item — a Microsoft May Patch Tuesday issue with limited public detail. On 2026-05-15 Microsoft confirmed **active exploitation in the wild** and re-issued the advisory with **mitigations only — no permanent patch yet**. The bug is a cross-site scripting / improper-neutralisation flaw in the OWA web-page generation path: a crafted email viewed in OWA (or in Outlook in some configurations) executes attacker-controlled JavaScript in the user's OWA session context, enabling spoofing, session theft, and chained execution. SecurityWeek and SecurityAffairs report Microsoft has shared "mitigations until a permanent patch can be released," strongly suggesting the patch sequencing was disrupted by the active-exploitation discovery between Patch Tuesday (2026-05-13) and 2026-05-15. No attribution surfaced yet.

**Why this is a material update vs. 2026-05-15 Noted:** Microsoft's own public statement of "exploitation in the wild" + "no permanent patch yet" elevates this from "track among Patch Tuesday batch" to active-incident class — on-prem Exchange remains the **PRC 2026-Q2 initial-access vector** (per MEMORY: SHADOW-EARTH-053 2026-05-02, FamousSparrow / UAT-9244 2026-05-14). A working OWA-side XSS that yields session compromise on Exchange would chain cleanly with the on-prem Exchange ProxyNotShell-class playbook these clusters already use.

**Mitigation:**
- Apply Microsoft's interim mitigations from the MSRC advisory immediately (likely IIS-side header / response filter; check MSRC for the canonical text).
- Restrict OWA exposure to corporate networks only (VPN / Zero Trust gateway); block direct OWA exposure from the public internet if practical.
- Enforce OWA session timeouts to the minimum operational value (15-30 min).
- Hunt OWA web logs for inbound emails followed by unusual outbound API calls / mailbox-rule changes within 5 minutes of message read.
- Coordinate with Microsoft for the permanent patch release; assume the patch is on the next out-of-band release cycle rather than the next Patch Tuesday.
- Track for KEV addition; the SD-WAN / PAN-OS tempo (KEV add within 1-3 days of disclosure) is plausible here.

**Sources:** [SecurityWeek — Microsoft Exchange Server CVE-2026-42897 Zero-Day Exploited](https://www.securityweek.com) | [TheHackerNews — Microsoft Exchange Server CVE-2026-42897 Under Active Exploitation](https://thehackernews.com) | [SecurityAffairs — CVE-2026-42897 Microsoft confirms active exploitation](https://securityaffairs.com)

---

### Linux Kernel Copy Fail CVE-2026-31431 — Kubernetes Container Escape PoC Published; LPE Now Demonstrably A Cross-Pod / Node-Compromise Primitive *(Update on prior coverage)*
**Product:** Linux kernel page-cache subsystem (CopyFail family — Ubuntu, RHEL, SUSE, Amazon Linux, Debian) — now demonstrably also affects containerised workloads | **CVE:** CVE-2026-31431 | **CVSS:** —

The 0xMarcio CVE feed (2026-05-15) surfaces a new public proof-of-concept repository, **Percivalll/Copy-Fail-CVE-2026-31431-Kubernetes-PoC**, that converts the previously LPE-only Copy Fail kernel page-cache write into a **container escape primitive on Kubernetes**: from a non-privileged pod (no CAP_SYS_ADMIN, no host filesystem mount, no privileged flag) the exploit writes attacker-controlled bytes to host-side page-cache entries of binaries shared by the cluster node (e.g., `/usr/bin/runc`, `/usr/sbin/kubelet`), achieving node-level code execution on the next container lifecycle event. Joins the existing Theori `copy-fail-CVE-2026-31431` and rootsecdev/iss4cf0ng/0xShe public exploits cited in MEMORY (2026-05-04 escalation).

**Why this is a material update:** Previously Copy Fail was classified LPE-only — within-scope only because KEV-added (2026-05-03). The Kubernetes-PoC moves it into **container-escape-class** privilege escalation, which is in-scope for any organization running multi-tenant K8s (managed K8s providers, build/CI runners running unprivileged pods, internal SaaS, agent-platform-as-a-service offerings). The same trajectory observed with Dirty Frag (kernel LPE → public ITW + container/escape implications) is repeating here within 14 days of public disclosure. Combine with the Mini Shai-Hulud Wave 2 supply-chain primitive (compromised package → unprivileged pod) and the chain ends in K8s node compromise.

**Mitigation:**
- Confirm all K8s nodes are on patched kernels (5.x with CopyFail fix backported; 6.x mainline with v6.13+).
- For unpatched cluster nodes: drain + reboot to patched kernel image; treat any unscheduled CopyFail-mitigation reboot as a forensic event.
- Add Falco / Tetragon / runtime-EDR rules for unexpected page-cache writes from unprivileged pods (telemetry primitive: writes to `/proc/self/mem` overlapping read-only file-backed mappings).
- Hunt cluster audit logs for unusual `runc`/`kubelet` binary modification timestamps; treat any non-package-manager binary change on cluster nodes since 2026-05-03 as suspicious.
- Patch backlog priority: K8s control-plane nodes ≥ K8s worker nodes ≥ traditional Linux servers.

**Sources:** [github.com/Percivalll/Copy-Fail-CVE-2026-31431-Kubernetes-PoC](https://github.com/Percivalll/Copy-Fail-CVE-2026-31431-Kubernetes-PoC) | [github.com/0xMarcio/cve](https://github.com/0xMarcio/cve) | [Theori — CopyFail Disclosure](https://theori.io/blog)

---

## 🟠 HIGH

### WordPress Funnel Builder Plugin — Unauthenticated Settings Modification → Persistent Payment-Card Skimmer; 40,000 Active Installs, Confirmed Active Exploitation (No CVE Assigned)
**Product:** Funnel Builder by FunnelKit WordPress plugin (versions ≤ 3.15.0.2) — 40,000+ active installs | **CVE:** Not yet assigned | **CVSS:** ~8.6 (estimated; not published by vendor) | **First reported:** 2026-05-14

A misconfigured WooCommerce checkout endpoint in Funnel Builder allows an unauthenticated attacker to call a non-protected admin handler that modifies the plugin's global settings — specifically the "External Scripts" setting. Attackers are using this to inject malicious JavaScript disguised as a fake Google Analytics tag (`googleanalytics-tracker.js` variants) that loads a payment-card skimmer at checkout. The payload exfiltrates card number, CVV, billing address, and customer PII to an attacker-controlled WebSocket server. Sansec confirmed active exploitation against multiple FunnelKit-driven WooCommerce stores. FunnelKit shipped version 3.15.0.3 on 2026-05-14.

**Why it matters:** This is the **second actively-exploited unauth WordPress plugin auth bypass in 5 days** (Burst Statistics CVE-2026-8181 on 2026-05-12 → 7,400 attempts in 24h; Funnel Builder on 2026-05-14 → Sansec confirmed mass deployment). The plugin runs on the WooCommerce checkout flow specifically, so injected JS executes on the payment page of every active site, making this the most direct skimmer monetisation vector active right now. Sansec history (Magecart, Polonium series) indicates a typical 4-6 week monetisation window before the skimmer is cycled out.

**Mitigation:**
- Update Funnel Builder to 3.15.0.3 (released 2026-05-14) immediately.
- Review `Settings → Checkout → External Scripts` for unauthorized entries; remove any non-canonical analytics/tracker scripts.
- Hunt WooCommerce admin audit logs for `wp_options` updates to `funnelbuilder_settings` from unauthenticated request contexts since 2026-04-01.
- Pull a full Content Security Policy report from the past 30 days; flag any external script load to an unfamiliar WebSocket / `wss://` endpoint on checkout pages.
- For affected sites: assume payment-card data has been exfiltrated since the date the malicious settings entry was created; trigger PCI-DSS incident response (notify card brands, isolate the site, full forensics).

**Sources:** [BleepingComputer — Funnel Builder WordPress plugin bug exploited to steal credit cards](https://www.bleepingcomputer.com/news/security/funnel-builder-wordpress-plugin-bug-exploited-to-steal-credit-cards/) | [Sansec — FunnelKit Magecart campaign](https://sansec.io) | [FunnelKit Security Advisory](https://funnelkit.com)

---

### WordPress Avada Builder CVE-2026-4798 (Unauth SQL Injection) + CVE-2026-4782 (Auth File Read) — 1 Million Active Installs; Full Site Takeover Via Database + wp-config.php Exfiltration
**Product:** Avada Builder WordPress plugin (versions ≤ 3.15.2) — ~1,000,000 active installs | **CVE:** CVE-2026-4798 (unauth SQLi), CVE-2026-4782 (auth file read) | **CVSS:** 9.4 (CVE-2026-4798), 6.5 (CVE-2026-4782) | **First reported:** 2026-05-14

CVE-2026-4798 is a time-based blind SQL injection in the `product_order` parameter — **unauthenticated** exploitation possible when WooCommerce has been installed and subsequently deactivated with intact database tables (a very common state after merchants migrate to alternative checkout solutions). CVE-2026-4782 is an authenticated (subscriber+) arbitrary file read via the `custom_svg` parameter in shortcode rendering, enabling exfiltration of `wp-config.php` and full site takeover. The Avada theme/builder bundle is one of the most-deployed commercial WordPress products with ~1M active installs and substantial e-commerce / corporate-site usage. Partial fix shipped 2026-04-13 (3.15.2); complete patch shipped 2026-05-12 (3.15.3) with the CVEs disclosed 2026-05-14.

**Why it matters:** The unauthenticated SQLi triggers on a configuration state ("WooCommerce installed then deactivated with intact DB tables") that is unusual but realistic, especially given the >1M install base. Time-based blind SQLi against the entire wp_options + wp_users tables yields admin password hashes, secret keys, and (via wp-config.php) database credentials and crypto keys — full site takeover. Avada is widely deployed by SMB / corporate marketing sites, and given the 3.15.3 patch was 2026-05-12 with disclosure 2026-05-14, the patch-window-to-exploitation tempo is 48 hours.

**Mitigation:**
- Update Avada Builder to 3.15.3 immediately.
- For any site where WooCommerce was previously installed and then deactivated, audit the database for residual WooCommerce tables (`wp_wc_*`); drop them if no longer needed.
- Audit WordPress admin user list for unauthorized additions since 2026-04-13 (partial-fix shipment).
- Hunt access logs for unusual GET requests with `product_order` parameter containing SQL syntax (`AND`, `SLEEP`, `BENCHMARK`, `ASCII`).
- Rotate WordPress secret keys (`AUTH_KEY`, `SECURE_AUTH_KEY`, etc.) on affected sites; force-logout all sessions.

**Sources:** [BleepingComputer — Avada Builder WordPress plugin flaws allow site credential theft](https://www.bleepingcomputer.com/news/security/avada-builder-wordpress-plugin-flaws-allow-site-credential-theft/) | [Wordfence — Avada Builder advisories](https://www.wordfence.com)

---

### n8n CVE-2026-44789 / CVE-2026-44790 / CVE-2026-44791 — 3-CVE Batch: HTTP Request Pagination Prototype-Pollution-To-RCE, Git Node Arbitrary File Read, XML Node Prototype Pollution Patch Bypass
**Product:** n8n self-hosted workflow automation (npm `n8n`) — versions before 1.x patched release | **CVE:** CVE-2026-44789 (HTTP Request RCE), CVE-2026-44790 (Git Node file read), CVE-2026-44791 (XML Node prototype-pollution patch bypass) | **CVSS:** 9.8 / 9.6 / 9.4 (all CRITICAL per GHSA) | **First reported:** 2026-05-15

GHSA published a 3-CVE batch on n8n on 2026-05-15. **CVE-2026-44789** is the most critical: a prototype-pollution vulnerability in the HTTP Request node's pagination handling that converts pollution into full RCE on the n8n host via Node.js prototype chain manipulation when a workflow is executed (authenticated workflow-execution context). **CVE-2026-44790** is an arbitrary file read in the Git Node via path manipulation in repository URLs — auth-required but the auth boundary in n8n is typically a single shared workflow operator. **CVE-2026-44791** is a patch-bypass on a prior n8n XML Node prototype-pollution issue (the patch added a key allowlist but missed a code path that processes XML attribute namespaces, allowing re-exploitation with attribute-namespace polluted keys).

This is the second n8n critical-RCE batch in 2026 after **CVE-2026-21858** (March 2026, CVSS 10.0) — the project shows the same code-quality recurrence pattern as nginx-ui (3 pre-auth RCEs in 2 months) and Open WebUI (5+ high-severity CVEs in 30 days).

**Why it matters:** n8n is widely deployed self-hosted automation platform (analogous to Zapier/Pipedream); per Intruder Labs scans previously cited in MEMORY, AI-automation platforms continue to demonstrate **default-no-auth** posture and frequent internet exposure. CVE-2026-44789 in particular is RCE on the host, which gives an attacker direct access to any credentials stored in n8n's credential vault (typically full read access to GitHub, AWS, Slack, Notion, customer databases). Treat any internet-facing n8n instance as a Tier-1 perimeter asset.

**Mitigation:**
- Update n8n to the GHSA-fixed release for all three CVEs.
- Audit n8n credential vault contents; rotate any high-privilege credentials (cloud, GitHub, IDP).
- Remove n8n's internet exposure; place behind dedicated VPN / Zero Trust gateway with auth.
- Hunt n8n workflow execution logs for unusual HTTP Request node configurations referencing `__proto__` / `constructor.prototype` / `Object.assign` in body templates.
- Add detection for unexpected child processes spawned by the n8n process tree.

**Sources:** [GitHub Security Advisories — n8n CVE-2026-44789](https://github.com/advisories/GHSA-c8xv-5998-g76h) | [GitHub Security Advisories — n8n CVE-2026-44790](https://github.com/advisories/GHSA-57g9-58c2-xjg3) | [GitHub Security Advisories — n8n CVE-2026-44791](https://github.com/advisories/GHSA-wrwr-h859-xh2r)

---

### Portainer CVE-2026-44848 (Missing Authz On Docker Plugin Endpoints → Host RCE) + CVE-2026-44849 (Swarm Service Endpoint Security Bypass)
**Product:** Portainer Community Edition + Business Edition (Go) — versions before 2.x patched release | **CVE:** CVE-2026-44848 (host RCE via Docker plugin authz), CVE-2026-44849 (Swarm endpoint security bypass) | **CVSS:** 9.9 / 9.4 (both CRITICAL per GHSA) | **First reported:** 2026-05-15

**CVE-2026-44848** is a missing-authorization issue on Portainer's Docker plugin management endpoints (`/api/endpoints/:id/docker/plugins/*`) — any authenticated Portainer user, regardless of role, can install / enable Docker plugins on the targeted Docker host. Docker plugins run with elevated privileges on the host (typical plugin types: volume drivers, network plugins, authz plugins); a maliciously crafted plugin yields **host-level RCE** on every Docker host managed by the Portainer instance. **CVE-2026-44849** is a parallel issue on Swarm service create/update endpoints: an attacker can bypass endpoint security boundaries (e.g., the "allow only standalone containers" enforcement) by routing the create/update through the Swarm-service path.

Portainer is **the dominant Docker management UI** with 1M+ pulls/week and is widely deployed in K8s + container homelabs, dev/test fleets, and SMB production. The combination of "any authenticated user → host RCE on every managed node" is a Tier-1 lateral-movement primitive in any environment running Portainer.

**Why it matters:** Portainer's typical deployment is a single privileged management container with credentials/agents to every Docker host in the environment — compromising Portainer is functionally equivalent to compromising every Docker host it manages. The fact that the authz check is missing for *any* authenticated user (not just admin-equivalent) means low-privilege Portainer users (or stolen API tokens at any tier) yield instant host RCE.

**Mitigation:**
- Update Portainer to the GHSA-fixed release immediately.
- Audit Portainer user list; revoke any non-essential accounts.
- Rotate all Portainer API tokens and force-logout all sessions.
- Hunt Docker daemon logs across all Portainer-managed hosts for unexpected plugin install / enable events since 2026-04-01.
- For high-trust Docker hosts (production): consider disconnecting Portainer agent until patched.
- Add Falco / Tetragon detection rules for new Docker plugin lifecycle events.

**Sources:** [GitHub Security Advisories — Portainer CVE-2026-44848](https://github.com/advisories/GHSA-rrmm-9v76-h3p4) | [GitHub Security Advisories — Portainer CVE-2026-44849](https://github.com/advisories/GHSA-5fxq-qcf3-244w)

---

### Amazon Redshift JDBC Driver CVE-2026-8178 — RCE Via Unsafe Class Loading In `redshift-jdbc42`
**Product:** Amazon Redshift JDBC Driver `com.amazon.redshift:redshift-jdbc42` (Maven) | **CVE:** CVE-2026-8178 | **CVSS:** 9.6 (CRITICAL per GHSA) | **First reported:** 2026-05-15

A deserialization / unsafe class-loading flaw in the Redshift JDBC driver allows a malicious JDBC connection string (or a connection-property override) to coerce the driver into loading attacker-controlled JVM classes, yielding **remote code execution in the JVM process loading the driver**. In typical deployment patterns this is the application server, the BI tool (Tableau / Superset / Looker), the data-pipeline runner (Airflow / Dagster / Prefect), or the analyst notebook host — all of which routinely hold high-privilege credentials to the data warehouse and adjacent IAM roles.

**Why it matters:** The Redshift JDBC driver is dependency-pinned in thousands of enterprise data pipelines and BI deployments; many use centrally-managed connection strings that *trust* the URL/parameter content because the URL is the connection target. An attacker who controls the connection-string supply path (CI runner with poisoned secrets, BI admin UI with insufficient input validation, malicious notebook shared in a team space) yields driver-host RCE without needing data-warehouse credentials. Affects the entire JVM ecosystem connecting to Redshift, not just Redshift itself.

**Mitigation:**
- Upgrade `redshift-jdbc42` to the GHSA-fixed release in all dependent products (BI tools, application servers, data pipeline runners, analyst notebooks).
- Audit all environments for the older driver version in Maven/Gradle dependency trees: `mvn dependency:tree | grep redshift-jdbc42` (or equivalent).
- Treat any system administrator who configures JDBC connection strings as a privileged-action role; restrict who can change them.
- Hunt JVM process logs for unusual `Class.forName` / `URLClassLoader` invocations from the Redshift driver thread.

**Sources:** [GitHub Security Advisories — Amazon Redshift JDBC CVE-2026-8178](https://github.com/advisories/GHSA-wmmv-vvg5-993q)

---

### OpenClaw CVE-2026-44112 / CVE-2026-44113 / CVE-2026-44115 — 3-CVE OpenShell Sandbox Race-Condition Chain Enables Data Theft And Privilege Escalation
**Product:** OpenClaw OpenShell sandbox (all versions ≤ 2026.3.x) | **CVE:** CVE-2026-44112 (CVSS 9.6/6.3 — primary race), CVE-2026-44113 (CVSS 7.7/6.3), CVE-2026-44115 (CVSS 8.8) | **First reported:** 2026-05-15

The Hacker News reports a 3-CVE chain in OpenClaw's OpenShell sandbox. CVE-2026-44112 is a **time-of-check / time-of-use race condition** in input validation that allows an attacker to bypass sandbox restrictions; CVE-2026-44113 chains incomplete input validation that surfaces sensitive data; CVE-2026-44115 establishes persistence post-bypass. The chain enables sandbox escape, data exfiltration, and persistence — joining the running stream of OpenClaw CVE disclosures (35+ CVEs published in 2026 already per MEMORY: VulnCheck 5/9 9-CVE batch, 5/12 16-CVE batch, plus this week's 5/15 4-CVE chain).

**Why it matters:** OpenClaw is the agent harness widely deployed for autonomous coding/CI workloads and is the canonical "AI agent runs shell commands" surface — sandbox escape moves the trust boundary inward to the OpenClaw process, which typically runs with credentials to the user's code repository, cloud account, and developer environment. Combined with the documented OpenClaw 2026.2.21-2 instance staleness across many environments (per MEMORY), this is exploitable in default deployments.

**Mitigation:**
- Update OpenClaw to the latest patched release immediately (`openclaw update`).
- Audit OpenClaw-host endpoints for unexpected process creation from the OpenShell sandbox process tree.
- Restrict OpenClaw credential exposure: never run with cloud-admin or repo-admin scope; use per-task least-privilege credentials.
- Hunt for the IoC pattern of sandbox escape: rapid sequential file-system operations on a path the sandbox was supposed to restrict, followed by unexpected subprocess invocation.

**Sources:** [TheHackerNews — Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence](https://thehackernews.com)

---

## 🟡 MEDIUM

### Pwn2Own Berlin 2026 Day 2 — 15 Additional Zero-Days Including Microsoft Exchange Compromise; $385,750 Awarded; Two-Day Total $908,750 / 39 Zero-Days *(Update on 2026-05-15 coverage)*
**Product:** Microsoft Exchange Server, Windows 11, additional virtualisation and enterprise targets | **CVE:** Multiple pending vendor advisory assignment | **Published:** 2026-05-15

Day 2 of Pwn2Own Berlin demonstrated **15 additional unique zero-days** including a **Microsoft Exchange Server compromise** (the most operationally significant of Day 2 given the same-day public confirmation of CVE-2026-42897 active exploitation — see Critical above), plus additional Windows 11 chains. Day-2 awards totalled $385,750; the two-day cumulative is $908,750 across 39 unique zero-days. The individual chains remain under ZDI embargo pending vendor coordination.

**Why this is an update vs. yesterday's Day 1 entry:** The Day 2 Exchange compromise lands in the same 24h window as Microsoft's confirmation of active CVE-2026-42897 exploitation — these may or may not be related, but the operational signal is identical: on-prem Exchange remains a top-tier 2026 target. Expect 30-50 CVEs landing in the next two Patch Tuesdays from the Pwn2Own Berlin batch (typical historical conversion rate).

**Mitigation:** Track ZDI's published advisories and the Microsoft / Broadcom / Mozilla vendor security feeds over the next 60-90 days. Apply the Patch Tuesday flow rigorously through Q2 2026.

**Sources:** [BleepingComputer — Microsoft Exchange, Windows 11 hacked on second day of Pwn2Own](https://www.bleepingcomputer.com/news/security/) | [SecurityAffairs — Pwn2Own Berlin 2026 Day Two](https://securityaffairs.com)

---

## 📋 Noted / Monitoring

**Linux kernel `__ptrace_may_access()` logic bug (Qualys advisory, oss-security 2026-05-15)** — Public PoC `_SiCk/ssh-keysign-pwn` already published; Qualys delayed full advisory to allow distros to patch. LPE-only with SSH-keysign exploitation primitive; the Qualys / `_SiCk` pattern suggests this will gain ITW exploitation within 7-14 days similar to the Dirty Frag and Copy Fail trajectories. Track for promotion if KEV-added.

**Apache Flink CVE-2026-35194 RCE via SQL injection in code generation (oss-security 2026-05-15/20)** — Stream-processing framework widely deployed in enterprise data pipelines; bug is RCE through Flink SQL Gateway's code-generation path. Limited technical detail at disclosure; track for vendor advisory escalation.

**libpng-apng CVE-2026-40930 push-mode APNG parser chunk smuggling (oss-security 2026-05-15/21)** — Image library issue with downstream distribution impact; client-side parsing path on widely-bundled library.

**netatalk 4.4.3 — 20-CVE security release (oss-security 2026-05-15/22)** — Apple Filing Protocol implementation; primarily affects NAS appliances and Time Machine targets; 18 additional issues deferred. Out of typical perimeter scope but track for NAS-vendor advisories.

**PostgreSQL 18.4 / 17.10 / 16.14 / 15.18 / 14.23 security release (oss-security 2026-05-15/23)** — Multi-CVE PostgreSQL update; specific CVE list pending oss-security thread propagation. Track and apply via OS package channels.

**sanitize-html CVE-2026-44990 default XSS via `xmp` raw-text passthrough (GHSA 2026-05-15)** — Critical default XSS in npm `sanitize-html` (~2M weekly downloads); affects any application using default config to sanitize untrusted HTML. Patch immediately and audit recent XSS reports for `<xmp>`-vector exploitation.

**Strapi CVE-2026-27886 sensitive-data leak via relational filtering (GHSA 2026-05-15)** — Companion to Strapi CVE-2026-22599 from 2026-05-13; lack of query sanitization on relational filters leaks data across permission boundaries.

**Apache Flink CVE-2026-35194 / Mapfish Print CVE-2026-44672 RCE (Maven, GHSA 2026-05-15)** — Mapfish Print is mapping-stack rendering library; RCE in dynamic table expressions; niche but in-scope where embedded in GIS web stacks.

**Goobi viewer-core CVE-2026-45083 unauthenticated Solr Streaming Expression proxy (Maven, GHSA 2026-05-15)** — Digital-library / museum-collection software; unauth Solr endpoint exposure → SSRF / data extraction.

**Obot CVE Authorization Bypass on `/mcp-connect/{id}` (Go, GHSA-vw82-7fv8-r6gp, 2026-05-15)** — MCP server: any authenticated user can connect to any registered MCP server; joins the 8+ MCP authz/authn issues documented in MEMORY pattern library.

**Flowise CVE-2026-46442 authenticated host RCE via NodeVM sandbox escape (npm, GHSA 2026-05-15)** — Flowise (AI workflow builder) RCE via `/api/v1/node-custom-function`; auth-required but Flowise's typical default-no-auth posture per MEMORY makes this exploitable in many deployments.

**frankenphp CVE-2026-45062 unsafe unicode handling in CGI path splitting (Go, GHSA 2026-05-15)** — Production-PHP server bug allowing execution of non-PHP files; sub-cluster of the Apache HTTP / PHP-FPM path-splitting class.

**@budibase/server 3-CVE batch (CVE-2026-45717 datasource authz, CVE-2026-45715 SSRF redirect bypass, CVE-2026-45548 SSRF in AI Extract File) (GHSA 2026-05-15)** — Budibase low-code platform; SSRF bypass class includes IP-blacklist bypass via redirect.

**WWBN/AVideo CVE-2026-45578 OS command injection in on_publish.php (Composer, GHSA 2026-05-15)** — Live-streaming platform; unauth command injection via unescaped m3u8 URL parameter.

**better-auth CVE-2026-45364 rate-limiter bypass via IPv6 prefix rotation (npm, GHSA 2026-05-15)** — Authentication library; rate limiter keys individual IPv6 addresses, bypassable via 2^64 prefix space.

**pipecat-ai CVE-2026-44716 path traversal in `/files` endpoint (pip, GHSA 2026-05-15)** — AI voice-agent framework arbitrary file read.

**code16/sharp CVE-2026-44692 cross-Storage download (Composer, GHSA 2026-05-15)** — Laravel admin panel; authenticated users can download unrelated Storage objects.

**electerm CVE-2026-45058 unsafe bookmark operation (npm, GHSA 2026-05-15)** — Fourth electerm CVE in 30 days after CVE-2026-43940 / 43944 / 45353; code-quality signal joining the deprecation-candidate cluster.

**simplesamlphp casserver CVE-2026-46491 path traversal → unserialize (Composer, GHSA 2026-05-15)** — Federated SSO server library; out-of-ticket-directory unserialize chain.

**Perl ecosystem oss-security batch (2026-05-15)** — CVE-2026-8612 (WWW::Mechanize::Cached deserialization), CVE-2026-8454/8669 (Imager::File::GIF heap OOB), CVE-2026-8503 (Apache::Session weak session ID generation), CVE-2026-46474 (Trog::TOTP weak random), CVE-2026-8700/8704 (Crypt::DSA weak seed / file write) — niche Perl modules.

**llama.cpp GGUF format parsers (oss-security 2026-05-15/19)** — Multiple vulnerabilities in llama.cpp's GGUF model-file parsers; AI inference engine widely deployed self-hosted. Track for CVE assignment and exploit publication.

**MOVEit Automation critical authentication bypass (Progress Software, 2026-05-15)** — Progress patched a critical auth-bypass in MOVEit Automation; no public exploit yet, but MOVEit's 2023 supply-chain incident history makes any auth-bypass an automatic high-priority patch.

**Ghostwriter / FrostyNeighbor Ukrainian government campaign (ESET, 2026-05-15)** — Belarus-aligned APT resumed campaigns active since March 2026 with geofenced PDF phishing delivering PicassoLoader + Cobalt Strike; out of direct enterprise perimeter scope but relevant for any org with Ukrainian government / NGO ties.

**Turla Kazuar P2P botnet (FSB-aligned, 2026-05-15)** — Russian APT upgraded Kazuar backdoor to peer-to-peer botnet for stealth + persistent network access; APT-tier IOC, not a vulnerability.

**Apache ActiveMQ CVE-2026-34197 follow-up (avleonov.com 2026-05-14)** — Deep-dive analysis confirms ~7,000 internet-exposed instances; covered originally 2026-05-14 noted; no new tempo signal.

**American Lending Center 123,000 customers (SecurityWeek 2026-05-15)** — Ransomware breach disclosed nearly a year after attack; financial-services data exposure; no novel TTP.

**OpenLoop Health 716,000 patients (BC 2026-05-15)** — January 2026 healthcare breach disclosure; standard healthcare PII exfiltration.

**Akamai acquires LayerX for $205M (2026-05-15)** — Industry consolidation; LayerX is the Claude-for-Chrome / ClaudeBleed disclosure org (per MEMORY 2026-05-09); track for any disclosure-policy change post-acquisition.

**G7 AI SBOM guidance (2026-05-15)** — Government policy release on AI-system supply-chain transparency; relevant for AI-platform vendors' future compliance requirements.

**Microsoft Edge backpedals on plaintext-password-in-memory (BC 2026-05-15)** — Microsoft will stop loading saved passwords into Edge memory at startup; operational hardening, not a vulnerability.

**OpenAI app-update deadline reminder (2026-06-12)** — Per yesterday's Mini Shai-Hulud Wave 2 OpenAI breach coverage; users of OpenAI macOS/Windows/iOS/Android apps must update by 2026-06-12 to maintain code-signing chain.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog, cert.gov.ua | ❌ (403 / empty) |
| Vendor advisories | fortinet.com/blog/threat-research, fortiguard.com/psirt (suppl.), msrc.microsoft.com/blog | ✅ / ❌ |
| Research / OSINT | schneier.com, krebsonsecurity.com, securitylab.github.com, kb.cert.org/vuls, openwall oss-security (suppl.), avleonov.com, github.com/advisories (suppl.) | ✅ |
| Supply chain | socket.dev/blog (suppl.), aikido.dev/blog (suppl.) | ✅ |
| Threat intel | rapid7.com, opencve.io, dbugs.ptsecurity.com, securityaffairs.com (suppl.), helpnetsecurity.com (suppl.) | ✅ |
| Reference DB | nvd.nist.gov, cve.org, cve.mitre.org, attackerkb.com, hackerone.com/hacktivity, bugcrowd.com/disclosures, github.com/0xMarcio/cve, packetstormsecurity.com, seclists.org/fulldisclosure | ⚠️ / ❌ |

**Errors:** `cisa.gov` (403), `cisa.gov/known-exploited-vulnerabilities-catalog` (403), `attackerkb.com` (403), `cve.mitre.org` → `cve.org` (JS-required), `cve.org` (JS-required), `googleprojectzero.blogspot.com` → `projectzero.google/` (JS-required), `msrc.microsoft.com/blog` (302 to JS-only site, no content), `hackerone.com/hacktivity` (JS-required), `bugcrowd.com/disclosures` (404), `cert.gov.ua` (empty content), `packetstormsecurity.com` (sparse / redirect), `github.com/search?q=CVE` (JS-required; used github.com/advisories as proxy), `seclists.org/fulldisclosure` (archive index stale through April), `teletype.in/@cyberok` (no recent posts), `habr.com/ru/companies/tomhunter/articles` (no recent posts), `nvd.nist.gov` (homepage shows only stale CVEs; no fresh data via WebFetch).

**CISA KEV:** No new additions confirmed today (gateway 403 via WebFetch; verified via BC/SA/SW relay). Yesterday's CVE-2026-20182 Cisco SD-WAN federal deadline remains 2026-05-17 — less than 36 hours from publication of this report.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-16/night | Next: 2026-05-17/night*
