# Watchtower Night Report — 2026-05-05
**Cycle:** Night | **Generated:** 2026-05-05 00:30 UTC (2026-05-05T00:30:00Z)
**Sources checked:** 22/30 | **CISA KEV total:** CVE-2026-31431 still the freshest add (2026-05-01 / due 2026-05-15) | **New KEV additions:** none observed today

---

## 🟠 HIGH

### 🔄 UPDATE — CVE-2026-31431 Linux Kernel "CopyFail": CISA Confirms Active Exploitation, Theori Publishes 100% Reliable Cross-Distro Exploit
**Product:** Linux kernel `algif_aead` cryptographic interface (kernels 2017→patch) | **CVE:** CVE-2026-31431 | **Status:** KEV / Active Exploitation Confirmed | **Previous score:** 7 → **Now:** 8

CISA on 2026-05-04 publicly confirmed active in-the-wild exploitation of the nine-year-old `algif_aead` LPE flaw and reiterated the 2026-05-15 federal patching deadline (added to KEV 2026-05-01). Microsoft observed "limited exploitation, mainly associated with PoC testing" but acknowledged active attacks are now underway. Materially, **Theori has published a 100%-reliable Python exploit demonstrated against Ubuntu 24.04 LTS, Amazon Linux 2023, RHEL 10.1, and SUSE 16** — i.e. essentially the entire 2024–2026 mainstream-cloud Linux fleet with kernels in the 2017→patch window. The technical primitive is unchanged from earlier coverage (write four controlled bytes to any readable file's page cache → root), but the cross-distro reliability of the public exploit moves this from "168 PoCs of varying quality" to a defender-must-assume mass-exploitation scenario.

**Timeline:** 2026-04-23 — Theori advisory → 2026-04-30 → 05-02 — first PoCs (LPE Noted) → 2026-05-01 — KEV addition (UPDATE score 4→7) → 2026-05-04 — CISA confirms in-the-wild exploitation + Theori cross-distro exploit (this UPDATE 7→8) → 2026-05-15 — KEV federal patching deadline.

**Why it matters:** Anything that already gets a foothold on a Linux host (web shell, leaked SSH key, a single supply-chain `.npmrc` exfil) now has a near-trivial, reliable, no-leak path to root across every hyperscale Linux base image. The window between "shell" and "kernel-level persistence" closed in the last 4 days.

**Mitigation:**
- Apply distro kernel updates immediately for any Ubuntu 24.04, RHEL 10/9, Amazon Linux 2023, SUSE 16, Debian, or AKS/EKS/GKE node images sitting on a 2017–pre-patch kernel.
- Until kernels can be replaced, lock `algif_aead` socket creation by AppArmor/SELinux profile, set `kernel.unprivileged_userns_clone=0`, or load a seccomp profile blocking `socket(AF_ALG, ...)`.
- Audit container images: any base image rebuilt before the distro fix carries the bug — gate the next image build on the patched-kernel CVE check, not just `apt upgrade`.
- Treat any local-only execution alert (web shell, suspicious process by `www-data`/app user) on Linux as potential root-already in the next 30 days.

**Sources:** [BleepingComputer — CISA says Copy Fail flaw now exploited to root Linux systems](https://www.bleepingcomputer.com/news/security/cisa-says-copy-fail-flaw-now-exploited-to-root-linux-systems/) | [SecurityWeek — Copy Fail Linux exploitation begins](https://www.securityweek.com) | [The Hacker News — Copy Fail KEV coverage](https://thehackernews.com)

---

### 📰 NEWS — Apache HTTP Server 9-CVE Patch Batch (CVE-2026-23918 HTTP/2 Double-Free RCE-Class + 8 Others)
**Product:** Apache HTTP Server (httpd) — versions 2.4.0 → 2.4.66 affected; fixed in 2.4.67 | **CVE:** CVE-2026-23918, CVE-2026-24072, CVE-2026-29169, CVE-2026-33006, CVE-2026-33007, CVE-2026-33523, CVE-2026-33857, CVE-2026-34032, CVE-2026-34059 | **CVSS:** Pending NVD scoring | **First reported:** 2026-05-04 (oss-security)

Apache shipped httpd 2.4.67 on 2026-05-04 fixing nine independent issues. The standout is **CVE-2026-23918 (Important severity) — a double-free in HTTP/2 early-reset handling with possible RCE**; this is the same general bug class as the 2023 HTTP/2 "Rapid Reset" and 2024's earlier double-free issues, and applies wherever httpd serves H2. The other batch items:

- **CVE-2026-33006 (Moderate)** — `mod_auth_digest` timing attack enables remote attacker to bypass Digest auth without valid creds.
- **CVE-2026-24072 (Moderate)** — `.htaccess` author can read files as the `httpd` user via `mod_rewrite` / `ap_expr` — local privilege expansion in shared-hosting / multi-tenant httpd.
- **CVE-2026-33523 (Low)** — HTTP response splitting when forwarding from untrusted backend (status-line injection across multiple modules).
- **CVE-2026-33857, 34032, 34059 (Low)** — three `mod_proxy_ajp` buffer over-reads / off-by-ones (memory disclosure).
- **CVE-2026-33007 (Low)** — `mod_authn_socache` NULL pointer dereference → child-process crash for caching forward-proxy configs.
- **CVE-2026-29169 (Low)** — `mod_dav_lock` NULL pointer crash (limited real-world surface — only used by very old SVN).

No public PoC for CVE-2026-23918 at time of writing, but the 2023 Rapid Reset cycle from disclosure → in-the-wild scanning was ~72 hours; expect similar tempo here.

**Why it matters:** Apache httpd is in our edge fleet, in dozens of internal services (Confluence/Jira reverse-proxies, internal apps), and bundled inside every Linux distro server image. CVE-2026-23918 (HTTP/2 + RCE-class) is the single highest-priority item; CVE-2026-33006 (mod_auth_digest auth bypass) is most immediately exploitable for credential-protected legacy admin pages.

**Discovered by:** Bartłomiej Dmitruk (striga.ai) and Stanisław Strzałkowski (isec.pl) — CVE-2026-23918; Pavel Kohout (Aisle Research), Elhanan Haenel, Tianshuo Han, Jérôme Djouder, Nitescu Lucian, Haruki Oyama (Waseda), Merih Mengisteab, Dawit Jeong, y7syeu — others.

**Mitigation:**
- Upgrade httpd to **2.4.67** across the fleet within the standard high-priority patch window (target ≤ 7 days for internet-facing, ≤ 14 days internal).
- For HTTP/2 specifically: if you cannot patch in 48h, disable H2 on internet-facing httpd vhosts (`Protocols http/1.1`) — degrades performance but eliminates the CVE-2026-23918 surface.
- For Digest auth (CVE-2026-33006): treat as a 0-day for any httpd instance fronting credential-protected admin pages with `AuthType Digest` — switch to Basic over TLS or front with an SSO proxy until patched.
- Multi-tenant httpd / shared hosting: rotate the `httpd` process user away from any sensitive on-disk material (OAuth keys, DB creds) — CVE-2026-24072 turns `.htaccess` write access into a file-read primitive on those.
- Inventory: confirm no `mod_dav_lock` enabled outside of WebDAV/SVN deployments (most installs have it disabled by default).

**Sources:** [Apache oss-security advisories — 2026-05-04](https://www.openwall.com/lists/oss-security/2026/05/04/) | [Apache HTTP Server 2.4.67 release notes](https://httpd.apache.org/security/vulnerabilities_24.html)

---

## 🟡 MEDIUM

### 📰 NEWS — DigiCert Code-Signing Compromise: 60 Certificates Revoked, 11 Used to Sign Zhong Stealer Malware
**Product:** DigiCert internal support portal / Code Signing certificate issuance | **CVE:** None assigned | **First reported:** 2026-05-04

On 2026-04-02 a malicious payload disguised as a screenshot was delivered through a customer chat channel and infected two DigiCert support analyst endpoints; one was caught 2026-04-03, the second went undetected until 2026-04-14 because the endpoint's security tooling was malfunctioning. Attackers pivoted from the analyst's machine into DigiCert's internal support portal and abused a legitimate "proxy into customer account" function intended for analysts. With that proxy access they captured **initialization codes for pending Code Signing orders** and combined them with already-approved orders to issue certificates fraudulently. By 2026-04-17 DigiCert had identified and revoked 60 certificates, including 27 directly attributed to the threat actor; **11 of those 60 were used to sign Zhong Stealer malware** (community-reported). DigiCert says the actor did not pivot beyond the support portal.

**Timeline:** 2026-04-02 — chat-channel malware payload → 2026-04-14 — second infected endpoint detected → 2026-04-17 — 60 certs revoked → 2026-05-04 — public disclosure.

**Why it matters:** Trust-chain incidents have cascading impact — 11 known-malicious certs already in the wild means EDR / AV reputation systems may have already whitelisted Zhong Stealer binaries on systems where AV uses CA reputation as a trust signal. Any internal binary still verifying against the revoked 60 will fail until cert chains are refreshed.

**Discovered by:** Internal DigiCert detection (April endpoint compromise); Zhong Stealer attribution via community / public AV vendor reporting.

**Mitigation:**
- Pull DigiCert's published serial-list of the 60 revoked certs and ingest into your code-signing-allowlist / EDR ruleset; alert/block on any binary signed by them.
- Verify your CRL/OCSP fetching is healthy on every endpoint and CI/CD signer that consumes Code Signing certs — any host with stale revocation data is still trusting these.
- For your own DigiCert-issued Code Signing certs: confirm with the vendor that none of your pending or recently-issued certs were affected by the lookup-leak, and rotate ones issued during the 2026-04-02 → 04-17 window if uncertain.
- Internal allowlists: if your application allowlists Zhong-Stealer-similar binaries by signature alone, switch to additional content-hash check before next deploy.

**Sources:** [SecurityWeek — DigiCert revokes certificates after support portal hack](https://www.securityweek.com/digicert-revokes-certificates-after-support-portal-hack/) | [BleepingComputer — DigiCert support portal compromise](https://www.bleepingcomputer.com)

---

### 📰 NEWS — VENOMOUS#HELPER: Phishing-Delivered SimpleHelp/ScreenConnect IAB Campaign Targeting 80+ U.S. Organizations
**Product:** SimpleHelp + ScreenConnect (legitimate RMM tools weaponised) | **CVE:** N/A — abuse of legitimate software | **First reported:** 2026-05-04 (The Hacker News / Securonix)

Securonix-tracked threat cluster **VENOMOUS#HELPER** is running an active, financially-motivated Initial Access Broker campaign that delivers customised SimpleHelp and ConnectWise ScreenConnect payloads via phishing. Targeting is "primarily U.S. organizations" — 80+ confirmed victims so far. The chain bypasses defences because the RMM agents are *legitimately* installed by the unsuspecting recipient (they appear as a normal IT remote-support tool); once installed, the actor has interactive remote access without needing to drop additional malware that EDR would catch.

**Timeline:** Activity ongoing; first publicly attributed and clustered by Securonix 2026-05-04.

**Why it matters:** The pattern (phishing → "your IT team needs to fix something" → user installs an MSI-signed RMM agent) is the bypass-of-choice in 2026 because the RMM binaries are legitimate vendor binaries with valid signatures — EDR allowlists, AV reputation, and many SOC playbooks treat them as benign. We currently have ScreenConnect, SimpleHelp, BeyondTrust RA, AnyDesk, and TeamViewer in the RMM bucket; any of them being installed by a non-IT user during a support pretext should be a high-fidelity alert.

**Mitigation:**
- Emit a SIEM alert on any **first-time install** of `SimpleHelpRemoteSupport.msi` / `ScreenConnect Client.msi` / `screenconnect.windowsclient.exe` on a non-IT user's endpoint.
- Email-gateway: add SPF/DKIM strict-fail rules for any external sender claiming to be IT/support; tag attachments with `.msi` or RMM-vendor-signed installers as high-risk.
- User awareness micro-training: emphasise "IT will never ask you to install a remote-control tool from an email link" — RMM-pretext is now the dominant social-engineering vector.
- AppLocker / WDAC: pre-block installation of all RMM tools your IT team doesn't sanction; allowlist only the RMM your own helpdesk uses.

**Sources:** [The Hacker News — VENOMOUS#HELPER phishing campaign](https://thehackernews.com) | [Securonix Threat Research](https://www.securonix.com)

---

### 📰 NEWS — CVE-2026-29200 Webpros Comet Backup — Cross-Tenant Account Impersonation IDOR (CVSS 9.9)
**Product:** Comet Backup (server / multi-tenant deployment) | **CVE:** CVE-2026-29200 | **CVSS:** 9.9 | **Status:** Patched — versions 26.1.1 / 26.2.1 | **First reported:** 2026-05-04

A vulnerable API call in Comet Backup (Webpros — same parent as cPanel) lets a tenant administrator on a multi-tenant Comet Backup server impersonate **any end-user account belonging to any other tenant on the same server**. Affects Comet Backup 20.11.0 → 26.1.0 / 26.2.0; fixed in 26.1.1 and 26.2.1. The flaw is a classic IDOR (CWE-639): the API call accepts a user identifier without validating tenant boundaries. CVSS 4.0 = 9.9 (network / no auth required from the attacker tenant's admin context).

**Why it matters:** Comet Backup is the white-label backup product widely used by hosting providers and MSPs (the same audience hit by cPanel CVE-2026-41940 over the past week). One compromised low-tier customer = read-write access to every other tenant's *backups* on the shared server. Backup data is the cleanest possible exfiltration target — historical credentials, full customer code/databases, and forensic traces.

**Discovered by:** Disclosed via Webpros advisory, picked up via dbugs.ptsecurity (PT-2026-36771).

**Mitigation:**
- MSPs / hosting providers running multi-tenant Comet Backup: upgrade to **26.1.1** or **26.2.1** within 48h.
- Until patched, disable the multi-tenant admin API or restrict it to a management VLAN with allowlisted source IPs.
- Audit Comet Backup access logs for cross-tenant API calls between 2026-04 and patch deployment.
- Hosting customers: ask your provider whether they run Comet Backup, what version, and when they're patching — this sits squarely on top of the cPanel-incident-class supply-chain risk.

**Sources:** [PT Security dbugs PT-2026-36771](https://dbugs.ptsecurity.com) | [NVD — CVE-2026-29200](https://nvd.nist.gov/vuln/detail/CVE-2026-29200) | [Comet Backup advisory](https://cometbackup.com)

---

### 📰 NEWS — Trellix Discloses Source-Code Repository Breach
**Product:** Trellix (security vendor — XDR / EDR / endpoint) | **CVE:** None assigned | **First reported:** 2026-05-04

Trellix disclosed unauthorized access to "a portion" of its source-code repository. The vendor states it found "no evidence that our source-code release or distribution process was affected, or that our source code has been exploited," engaged forensic experts and notified law enforcement. Attack vector and scope of code exposure were not disclosed. Trellix protects ~50,000 customers (200M+ endpoints).

**Timeline:** 2026-05-04 disclosure; window of unauthorized access not specified.

**Why it matters:** The 2026 string of security-vendor source-code breaches (Checkmarx, Cisco, now Trellix) means the bar to find new exploitable bugs in every defender's product is dropping — attackers are systematically pulling down tools they need to defeat. If your EDR is Trellix-based, plan for the possibility of bypass research being published in the next 30–60 days; treat any unusual EDR-behavior or signature-update interruption with elevated suspicion.

**Discovered by:** Internal Trellix detection.

**Mitigation:**
- If you're a Trellix customer: ask the vendor for confirmation that *your* tenant's customer-facing code (rules, signatures, custom modules you may have authored on their platform) was not exposed.
- Monitor for vendor-issued advisories about engine bypass / detection-evasion in the 30–90 days post-incident.
- Don't downgrade the EDR's role — but ensure you have a layered detection (network, identity, application logs) in case engine confidence drops.

**Sources:** [BleepingComputer — Trellix discloses data breach after source code repository hack](https://www.bleepingcomputer.com/news/security/trellix-discloses-data-breach-after-source-code-repository-hack/) | [SecurityWeek — Trellix breach](https://www.securityweek.com)

---

### 📰 NEWS — Apache Thrift Triple Advisory — Rust DoS, Java SSL Hostname Bypass, Node.js Multi-Vuln (CVE-2026-43868 / 43869 / 43870)
**Product:** Apache Thrift — Rust, Java, Node.js implementations | **CVE:** CVE-2026-43868, CVE-2026-43869, CVE-2026-43870 | **CVSS:** Pending | **First reported:** 2026-05-05 (oss-security)

Apache shipped a same-day triple advisory for Thrift across three language bindings on 2026-05-05:

- **CVE-2026-43868 (Rust)** — Rust impl is vulnerable to the same pattern as the 2020 CVE-2020-13949 (resource-exhaustion / unbounded read on malformed message headers). Java fix from 2020 was never carried into the Rust port.
- **CVE-2026-43869 (Java)** — `TSSLTransportFactory.java` does not perform hostname verification on the server certificate. Pure MITM enabler for any Thrift-over-TLS client built with this transport factory.
- **CVE-2026-43870 (Node.js)** — multiple vulnerabilities in `web_server.js` (specifics not yet detailed but flagged "multi" — likely auth + parser issues).

**Why it matters:** Thrift is the RPC framework behind many internal microservice meshes (especially in companies that pre-date gRPC adoption — Facebook, Pinterest, Evernote-style stacks). The Java SSL hostname-verification bypass (CVE-2026-43869) is the most directly exploitable in the field — anyone running Thrift-over-TLS Java clients on networks where an attacker can MITM the path (cloud transit, lateral inside K8s, BYOD) loses request integrity and credentials.

**Discovered by:** Jens Geyer / Apache Thrift project.

**Mitigation:**
- Inventory Thrift usage: Java IDL clients (most common), Rust services (rare but rising in newer codebases), Node.js web-server-mode (uncommon).
- Upgrade to the next Apache Thrift release containing the fixes (track Apache Thrift project release notes).
- Until upgraded, pin Thrift Java clients to mTLS with explicit certificate-pinning rather than relying on hostname verification.
- Audit any internal Thrift mesh for clients on a Thrift-over-plain-TCP (some legacy meshes only added TLS recently) — those weren't relying on hostname verification anyway, but they're now even higher priority to wrap in service-mesh mTLS.

**Sources:** [Apache oss-security advisories — 2026-05-05](https://www.openwall.com/lists/oss-security/2026/05/05/) | [Apache Thrift project security page](https://thrift.apache.org)

---

## 📋 Noted / Monitoring

**CVE-2026-41940 cPanel & WHM (ongoing)** — Mass-exploitation continues; The Hacker News reports the same auth-bypass weaponized against Southeast-Asian government, military, and MSP targets, and `rfxn/cpanel-sessionscribe` published a fleet-triage IOC scanner. No score change vs. 2026-05-03 ("Sorry" ransomware UPDATE, score 9) — flagging as still-active, no new tooling beyond yesterday's Watchtowr scanner.

**Amazon SES phishing abuse (operational pattern)** — Kaspersky reports a steep rise in attackers grabbing leaked AWS keys (TruffleHog scans of public GitHub / .env / Docker / S3) and using them to send DocuSign / BEC phishing through Amazon SES. SES has SPF/DKIM/DMARC pass by default and shares IP space with legitimate AWS outbound mail, so reputation-based filtering can't block it. Action item for our env: hunt our own GitHub orgs for AWS-key leaks and confirm IAM-credential-rotation cadence.

**Microsoft Windows April 2026 updates breaking 3rd-party backup software (`psmounterex.sys`)** — operational fault, not a vulnerability. Affects Veeam / Acronis / similar drivers binding the `psmounterex.sys` driver kernel structure. Microsoft confirmed; expect a vendor patch / out-of-band Microsoft fix in the next 7-14 days. Watch for any backup-job failures introduced after April Patch Tuesday.

**CVE-2026-29199 phpBB — Host Header Injection → Password-Reset Poisoning (CVSS 8.1)** — Patched. Pre-auth via the password-reset flow; attacker poisons the `Host:` header so the reset-link email points to attacker-controlled URL → captures reset token → account takeover. Affects any phpBB-hosted forum reachable via attacker-controllable Host. Monitor for next 30 days.

**CVE-2026-7723 Prefect — Missing Authentication on WebSocket Endpoint (CVSS 7.3)** — Fixed in 3.6.14. DevOps / workflow-orchestration platform; the WebSocket endpoint exposed runs/logs without auth. Anyone running self-hosted Prefect should patch.

**CVE-2026-37459 FRRouting — BGP UPDATE Integer Underflow → DoS (CVSS 7.5)** — BGP daemon DoS via crafted UPDATE message. Not RCE, but routing-disruption-class (anyone in our peering path could induce BGP daemon crash → session reset cascade). Patch when next maintenance window allows.

**CVE-2026-7776 HashiCorp Boundary — TLS Handshake DoS (CVSS 7.5)** — Workers can be locked up via crafted TLS handshakes. Affects any internet-reachable Boundary worker (rare deployment but high-impact when exposed).

**CVE-2026-22679 Weaver E-cology RCE (active since March)** — Unauthenticated RCE in the Weaver E-cology office-automation suite (predominantly Chinese-deployed). Patched 2026-03-12; mass exploitation observed 2026-03-17 → ~one week, with `whoami` / `ipconfig` / `tasklist` recon and Goby-linked C2 callbacks. Very limited Western footprint; included for completeness.

**Bluekit phishing kit (under development, AI assistant)** — New phishing-as-a-service kit under development, advertised as having an "AI assistant" for victim-conversation steering plus automated domain registration. Currently low-volume and not yet in active campaigns; flagging for the helpdesk-pretext class of attack we care about.

**Mutt 2.3.2 release** — release announcement on oss-security 2026-05-04; specific CVE details not yet broken out. Track for an MUA-side issue if it later gets a CVE assigned.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com, schneier.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog, kb.cert.org/vuls, cert.gov.ua | ❌ (KEV info via THN/BC relay; CISA + CERT-UA + KEV unreachable; kb.cert.org returned April-only) |
| Vendor advisories | msrc.microsoft.com/blog, blog.cloudflare.com/tag/security, fortinet.com/blog/threat-research, securitylab.github.com | ⚠️ (all stale; no May items) |
| Research / OSINT | rapid7.com, schneier.com, avleonov.com, googleprojectzero.blogspot.com, labs.watchtowr.com (off-list), socket.dev (off-list) | ⚠️ (Rapid7 Metasploit Wrap-Up only; the rest April or earlier; socket.dev/labs.watchtowr surfaced no May items) |
| Supply chain | github.com/0xMarcio/cve, github.com/search, seclists.org/fulldisclosure, openwall.com/lists/oss-security, socket.dev | ✅ |
| Threat intel | dbugs.ptsecurity.com, opencve.io, packetstorm.news, hackerone.com/hacktivity, bugcrowd.com/disclosures, attackerkb.com, habr.com/ru/companies/tomhunter, teletype.in/@cyberok, cve.org, cve.mitre.org, nvd.nist.gov | ⚠️ (dbugs + opencve productive; hackerone / bugcrowd / attackerkb / cve.org / cve.mitre.org / nvd full-listing all degraded or unreachable; Russian sources stale) |

**Errors:** cisa.gov 403 / cisa.gov/known-exploited-vulnerabilities-catalog 403 / attackerkb.com 403 / bugcrowd.com/disclosures 404 / hackerone.com/hacktivity JS-required / cve.org JS-required / cve.mitre.org redirects to cve.org / cert.gov.ua header-only.
**Degraded:** msrc.microsoft.com/blog (no content via WebFetch), nvd.nist.gov (change-timeline page only), packetstorm.news (feedback-loop only), googleprojectzero.blogspot.com / projectzero.google (no May posts).
**CISA KEV:** No new additions today beyond the 2026-05-01 add of CVE-2026-31431 (CopyFail, federal patch deadline 2026-05-15). Active confirmation of exploitation issued today.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-05/night | Next: 2026-05-06/night*
