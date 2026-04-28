# Watchtower Night Report — 2026-04-28
**Cycle:** Night | **Generated:** 2026-04-28 03:30 UTC (2026-04-28T03:30:00Z)
**Sources checked:** 23/30 | **CISA KEV new additions:** 0 (no additions since 2026-04-24)

---

## 🔴 CRITICAL

### CVE-2026-35414 — OpenSSH 15-Year-Old Certificate Principal Parsing Bug Yields Root Shell (CVSS 8.1)
**Product:** OpenSSH all releases for ~15 years through 10.2 | **CVE:** CVE-2026-35414 | **Status:** Patched (10.3, early April 2026) — public technical write-up published 2026-04-27

A code-reuse error in OpenSSH's certificate-principal handling lets a comma in the principal name cross a parser boundary: one routine treats commas as list separators, another treats the principal as a single string. An attacker holding a valid certificate from a trusted CA can therefore present a principal like `deploy,root` and authenticate as `root` on a server that should only have allowed `deploy`. Because the bypass passes authentication cleanly, **no auth-failure entry appears in the logs** — log-based detection of the attack is essentially impossible. Cyera, who discovered the flaw, demonstrated end-to-end exploitation in roughly twenty minutes. No active in-the-wild exploitation reported yet, but the patch landed weeks ago and a clear technical write-up has now been published — weaponisation is a matter of time.

**Timeline:** Code path introduced ~2010 → reported by Cyera → patched in OpenSSH 10.3 early April 2026 → public technical disclosure 2026-04-27 → still no public PoC, but the bug pattern is simple enough that internal reproduction is straightforward.

**Why it matters:** OpenSSH is the universal management plane for Linux/BSD fleets — every SSH-cert-based deployment (Vault SSH CA, Smallstep, HashiCorp, Teleport, OpenSSH FIDO CAs, internal SSH-CA implementations) is at risk if any role/principal name in any signed cert can be set or influenced by a lower-privileged user. Worst case: a commit comment, ticket comment, automation parameter, or self-service request that flows into a principal name converts a routine SSH cert into a root login. This is the SSH equivalent of an SSRF in a token-issuing service, and our public-facing SSH bastion estate is exactly the surface the advisory targets.

**Discovered by:** Cyera (data security firm). Public technical write-up via SecurityWeek / Cyera blog 2026-04-27.

**Mitigation:**
- Upgrade every server (and bastion) running `sshd` to **OpenSSH 10.3 or later** immediately. Validate the `sshd -V` output post-upgrade.
- Audit your SSH certificate authority code paths: any principal value that comes from user-controllable input must be validated against a strict allow-list **and** rejected if it contains `,` or whitespace.
- Hunt for already-issued long-lived SSH certs whose principals contain commas — rotate the CA and re-issue cleanly if any are found.
- Treat the absence of failed-login telemetry around root as a signal during forensic review post-upgrade. Cross-reference SSH cert issuance logs (Vault, Smallstep, etc.) with `auth.log` for unexpected root sessions.
- Where upgrade is delayed, restrict SSH cert-based authentication to a short principal allow-list (`AuthorizedPrincipalsCommand` or `AuthorizedPrincipalsFile`) that explicitly disallows multi-principal certificates.

**Sources:** [SecurityWeek — OpenSSH Flaw Allowing Full Root Shell Access Lurked for 15 Years](https://www.securityweek.com/openssh-flaw-allowing-full-root-shell-access-lurked-for-15-years/) | [OpenSSH Release Notes — 10.3](https://www.openssh.com/releasenotes.html)

---

### CVE-2026-40976 — Spring Boot Default Web Security Bypass (CVSS 9.1)
**Product:** Spring Boot 4.0.0 – 4.0.5 (servlet web apps with `spring-boot-actuator-autoconfigure` and no `spring-boot-health`) | **CVE:** CVE-2026-40976 | **Status:** Patched (4.0.6, 2026-04-23)

Spring Boot's default-on web security degrades to allow-all when an application uses spring-boot-actuator-autoconfigure without a custom Spring Security configuration **and** does not pull in the spring-boot-health module. The result is unauthenticated access to **every endpoint in the application**, including actuator routes (`/actuator/env`, `/actuator/heapdump`, `/actuator/mappings`) that historically expose configuration, secrets, and request structure usable for further compromise. CVSS 9.1, Network/Low/None/None vector. Vendor advisory published 2026-04-23; OpenCVE picked it up 2026-04-27.

**Timeline:** Vulnerable since 4.0.0 → vendor advisory and 4.0.6 release 2026-04-23 → broader public coverage via OpenCVE 2026-04-27 → no public PoC observed, but `/actuator/env` exposure is one of the most heavily-scanned signatures in the wild and any Spring Boot 4.0.x app meeting the conditions will start failing internet-wide ZAP/Nuclei sweeps the moment scanners pick this up.

**Why it matters:** Spring Boot is one of the most widely deployed Java web frameworks. Although the preconditions are specific (servlet stack + actuator without health module + no custom security config), this is the configuration that ships in many bootstrapped projects, internal admin services, and microservices that "just need actuator for the platform team." The default-on actuator surface is exactly what attackers automate against — CVSS 9.1 unauthenticated access to all endpoints means RCE is plausible the moment a vulnerable app exposes anything writable or executes deserialised input.

**Mitigation:**
- Upgrade Spring Boot to **4.0.6** in every microservice. Re-bake container base images so old layers stop caching the vulnerable jars.
- Inventory Spring Boot 4.x services. For each, check whether actuator-autoconfigure is on the classpath and whether spring-boot-health is *not* — if the answer is "yes, no", that service was vulnerable until upgrade.
- Pending upgrade, add a temporary `SecurityFilterChain` bean restricting `/actuator/**` to authenticated/internal traffic, or remove `spring-boot-actuator-autoconfigure` from public-facing apps.
- Hunt: review egress-fronted reverse-proxy logs for unauthenticated 200s on `/actuator/env`, `/actuator/heapdump`, `/actuator/mappings`, `/actuator/configprops` against any Spring Boot 4.0.x app since 2026-04-23.

**Sources:** [Spring Security Advisory — CVE-2026-40976](https://spring.io/security/cve-2026-40976) | [OpenCVE — CVE-2026-40976](https://app.opencve.io/cve/CVE-2026-40976)

---

## 🟠 HIGH

### CVE-2026-32202 — Windows LNK Zero-Click NTLM Coercion (Incomplete Patch of CVE-2026-21510)
**Product:** Windows (all currently supported, Explorer LNK rendering) | **CVE:** CVE-2026-32202 | **CVSS:** Not yet publicly assigned | **First reported:** 2026-04-27

Akamai disclosed that Microsoft's February 2026 fix for CVE-2026-21510 (LNK-based RCE that APT28 used in December 2025 against Ukraine and EU targets) was incomplete: the victim machine still automatically authenticates to the attacker's SMB host when Windows Explorer renders the directory containing a malicious shortcut. The residual flaw, CVE-2026-32202, allows a zero-click NTLM-hash leak: an attacker drops a `.lnk` whose icon is referenced by UNC path, the moment a user (or background indexer) opens the containing folder, Explorer initiates an SMB connection, and Net-NTLMv2 hashes are sent to the attacker. Microsoft patched CVE-2026-32202 in the April 2026 cumulative updates that we previously covered.

**Timeline:** APT28 weaponised CVE-2026-21510 + CVE-2026-21513 in December 2025 → Microsoft patch shipped February 2026 → Akamai found the patch incomplete → Microsoft re-patched in April 2026 Patch Tuesday → public disclosure of the original-fix-was-incomplete story 2026-04-27.

**Why it matters:** Any Windows host that browses to an attacker-controlled SMB share, or unzips an attacker-supplied folder containing a `.lnk` whose icon is set to a UNC path on an attacker host, will leak NTLM hashes with no user interaction beyond the folder render itself. APT28 is already operating in this space; even though the latest fix is shipping in April Patch Tuesday, every host that did not yet apply April 2026 cumulative updates remains coercible. Cracked/relayed NTLM is still a bread-and-butter foothold-escalation primitive on internal networks.

**Mitigation:**
- Confirm April 2026 Patch Tuesday cumulative update is applied on every Windows server, workstation, and Citrix/RDS image. The earlier February patch is **not** sufficient.
- Block outbound SMB (TCP 445, 139) at the perimeter; enforce SMB signing and NTLMv2 only.
- Push the SMB client policy `EnableInsecureGuestLogons=0` and disable LM/NTLMv1.
- For high-value users, push the registry policy that restricts NTLM outbound traffic to an allow-list (`RestrictSendingNTLMTraffic = DenyAll` with explicit exceptions).
- Where impractical to fully block outbound SMB, deploy egress allow-listing on TCP 445 to internal subnets only.

**Sources:** [SecurityWeek — Incomplete Windows Patch Opens Door to Zero-Click Attacks](https://www.securityweek.com/incomplete-windows-patch-opens-door-to-zero-click-attacks/) | [Akamai — Coercive Authentication Resurrected: How an Incomplete Patch Brought Back NTLM Coercion](https://www.akamai.com/blog/security-research)

---

### GlassWorm v2 — 73 Sleeper Extensions on Open VSX (320+ Artifacts Since December 2025)
**Product:** Open VSX marketplace (extensions for VS Code, Cursor, Windsurf, VSCodium) | **CVE:** None | **CVSS:** N/A | **First reported:** 2026-04-27

Koi Security and Aikido Security identified 73 cloned VS Code extensions on Open VSX, six confirmed actively malicious and 67 dormant "sleeper" packages waiting to ship a malicious update once they accumulate developer trust. The campaign reuses the GlassWorm tradecraft from October 2025 (Unicode-hidden code, Solana-based C2) and now spans at least 320 artifacts across GitHub, npm, VS Code Marketplace, and Open VSX since 2025-12-21. The current loaders are thin — they pull a Zig-based dropper that fetches a secondary VSIX from GitHub at runtime, which lets the attackers swap the payload without re-publishing the extension. Confirmed-malicious extensions: `outsidestormcommand.monochromator-theme`, `keyacrosslaud.auto-loop-for-antigravity`, `krundoven.ironplc-fast-hub`, `boulderzitunnel.vscode-buddies`, `cubedivervolt.html-code-validate`, `winnerdomain17.version-lens-tool`. Payload objectives: SSH keys, git credentials, cloud credentials, browser session cookies, and crypto wallets.

**Mitigation:**
- Block / uninstall the six confirmed extensions across every developer workstation, CI runner, and Codespace image.
- Quarantine any extension installed from Open VSX between 2025-12-21 and now that originates from a publisher with no prior reputation; rotate developer credentials on suspicion.
- Pin Open VSX extensions to specific versions in shared developer images; do not auto-update extensions on shared/CI hosts.
- Hunt: review developer workstations for unexpected outbound HTTPS to GitHub raw / `githubusercontent` for `.vsix` blobs, anomalous spawn of `node` or `code` writing files under `~/.vscode/extensions/<publisher>/<extension>/`, and Solana RPC traffic from corp IDEs.
- For organisations using Cursor/Windsurf at scale, treat any `cursor-*` or `windsurf-*` extension installed in the past 4 months as untrusted until reverified.

**Sources:** [BleepingComputer — GlassWorm malware attacks return via 73 OpenVSX "sleeper" extensions](https://www.bleepingcomputer.com/news/security/glassworm-malware-attacks-return-via-73-openvsx-sleeper-extensions/) | [The Hacker News — Researchers Uncover 73 Fake VS Code Extensions](https://thehackernews.com/2026/04/researchers-uncover-73-fake-vs-code.html) | [Koi Security — GlassWorm v2 Analysis](https://koi.security/research)

---

### PyPI elementary-data 0.23.3 Supply Chain Compromise (1.1M Monthly Downloads)
**Product:** elementary-data PyPI package (dbt observability) | **CVE:** None assigned | **CVSS:** N/A | **First reported:** 2026-04-27

Attackers exploited a GitHub Actions script-injection flaw in the elementary-data project: malicious comments on pull requests exposed `GITHUB_TOKEN`, allowing them to push forged commits and tags that triggered the legitimate release pipeline. The result was a backdoored release **0.23.3** uploaded to PyPI and the corresponding Docker images published as `ghcr.io/elementary-data/elementary:0.23.3` and `:latest`. The injected `elementary.pth` file runs at Python interpreter startup and exfiltrates SSH keys, git credentials, cloud credentials (AWS/GCP/Azure), Kubernetes/Docker secrets, `.env` files, crypto wallets (BTC/LTC/XMR/ETH/SOL), `/etc/passwd`, and shell history. Community member `crisperik` flagged the upload, the package was yanked, and clean version **0.23.4** was published. Docker images tagged `:latest` re-pulled by automation between the upload and the takedown will have shipped the malicious build into customer pipelines.

**Mitigation:**
- Rotate every secret pulled from any environment that ran `elementary-data==0.23.3` or pulled `ghcr.io/elementary-data/elementary:0.23.3` or `:latest` between Saturday's compromise and Sunday's removal.
- Force-pin `elementary-data>=0.23.4` and `<0.24.0` in `requirements.txt` / `pyproject.toml` until the post-mortem stabilises.
- Audit GitHub Actions workflows across the org for the same anti-pattern: `${{ github.event.comment.body }}` (or `pull_request.body`/`issue.body`/`discussion.body`) flowing into `run:` blocks. This is the canonical script-injection sink — the elementary-data project lost its release pipeline because of it.
- Hunt: any host that ran the malicious release should be treated as compromised — assume credentials in `~/.aws`, `~/.config/gcloud`, `~/.kube/config`, `~/.ssh`, `.env` files, and crypto wallet files were exfiltrated.

**Sources:** [BleepingComputer — PyPI package with 1.1M monthly downloads hacked to push infostealer](https://www.bleepingcomputer.com/news/security/pypi-package-with-11m-monthly-downloads-hacked-to-push-infostealer/) | [elementary-data GitHub — Security Advisory](https://github.com/elementary-data/elementary)

---

### CVE-2026-27966 — Langflow Pre-Auth RCE via LangChain REPL Now Weaponised in Metasploit (CVSS not yet assigned)
**Product:** Langflow < 1.8.0 | **CVE:** CVE-2026-27966 | **CVSS:** Not yet assigned | **First reported:** 2026-04-25 (Metasploit module landed in Rapid7 wrap-up)

Langflow versions before 1.8.0 expose the LangChain REPL component by default; an attacker who can submit a "flow" can include arbitrary Python that the LangChain runtime executes server-side, yielding RCE without authentication. Rapid7 shipped a public Metasploit module on 2026-04-25 — the bar for exploitation has dropped from "researcher PoC" to "msfconsole one-liner". This continues the AI-tooling RCE pattern (LiteLLM, Marimo, n8n, llama.cpp) where flow/prompt/notebook entry points reach Python `exec()` paths.

**Mitigation:**
- Upgrade every Langflow deployment to **>= 1.8.0** and confirm the REPL component is disabled if not required.
- Network-isolate Langflow instances behind authenticated reverse proxies; treat the public Langflow endpoint as remote-shell-as-a-service until upgrade is confirmed.
- Search corporate networks (and any cloud account) for `langflow` containers or `langflow.exe` processes; correlate with internet-exposed hosts.
- Hunt: review Langflow logs for unexpected flow uploads or POSTs to `/api/v1/flows` from unknown IPs since 2026-04-01; a successful exploit will spawn a child Python process with non-Langflow command-line arguments.
- Where upgrade is delayed, drop inbound traffic to Langflow's listener at the firewall.

**Sources:** [Rapid7 — Metasploit Wrap-Up 04/25/2026](https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-04-25-2026/) | [Langflow GitHub — Security Advisory CVE-2026-27966](https://github.com/langflow-ai/langflow/security/advisories)

---

## 🔄 Update

### TeamPCP Campaign Update — Checkmarx GitHub Source Code, Employee Data, and Credentials Posted to Dark Web
**Product:** Checkmarx GitHub repository (initial vector: TeamPCP supply-chain compromise of 2026-03-23) | **CVE:** None | **Threat score:** 8 (previously 8) | **First reported:** 2026-04-27

Checkmarx confirmed on 2026-04-27 that data from the GitHub repository compromised in the 2026-03-23 TeamPCP supply-chain attack has now been published on a dark-web marketplace. The leak was claimed by an actor calling itself **LAPSUS$** but Checkmarx attributes the underlying compromise to TeamPCP (the same financially-motivated cluster that subsequently compromised the Bitwarden CLI npm package). Disclosed contents: source code, employee database, API keys, MongoDB and MySQL credentials. Checkmarx maintains the GitHub repo is separated from customer production data, but the API keys and DB credentials are exactly the kind of secret that downstream defenders need to rotate if any of them touched a Checkmarx-managed integration in the past 5 weeks.

**Why this is an update vs. last entry (2026-03-23 / 2026-04-23 KICS Docker compromise):** previous entries documented the compromise vector and the malicious KICS Docker images; today's development is the **publication of the stolen artefacts on the dark web**, raising the relay risk: any organisation whose API keys reside in the leaked Checkmarx repo data is now exposed to direct credential stuffing / lateral abuse, not just to the TeamPCP campaign.

**Mitigation:**
- If your organisation uses Checkmarx One or any Checkmarx-managed integration, confirm with Checkmarx whether your tenant credentials, API keys, or webhook secrets reside in the leaked repository — and rotate proactively if there is any uncertainty.
- Re-rotate any token or webhook value that was created or rotated in a Checkmarx-mediated workflow between 2026-02-23 and 2026-03-23.
- Block / monitor the published-on-darknet API keys against your auth and SaaS access logs (have Checkmarx provide hashes / prefixes if possible).
- Carry forward the remediation guidance from the 2026-04-23 KICS Docker advisory and the 2026-04-24 Bitwarden CLI advisory — the same actor cluster keeps monetising different artefacts of the same intrusion.

**Sources:** [The Hacker News — Checkmarx Confirms GitHub Repository Data Posted on Dark Web](https://thehackernews.com/2026/04/checkmarx-confirms-github-repository.html) | [Checkmarx Blog — Update on March 23 Supply Chain Incident](https://checkmarx.com/blog)

---

## 📋 Noted / Monitoring

**ADT Inc breach (5.5M individuals, 2026-04-27)** — ShinyHunters compromised an ADT employee Okta SSO via vishing, then exfiltrated 11GB of Salesforce data (names, addresses, phones; small subset DOB / partial SSN/Tax ID). Customer security systems and payment data unaffected. Out of our remote-vulnerability scope but worth flagging as another data point in the ShinyHunters / Okta-vishing pattern that continues to hit US enterprises.

**Medtronic confirms breach after ShinyHunters claim (9M records, 2026-04-27)** — Medical-device manufacturer confirmed unauthorised access to "certain corporate IT systems" while emphasising that product networks and manufacturing are segmented from corporate IT. ShinyHunters claimed 9M records and removed the listing post-confirmation (suggests payment / negotiation). Same MO as ADT. Track for healthcare-sector ripple effects.

**PhantomCore exploits TrueConf BDU:2025-10114 / 10115 / 10116 (CVSS 9.8 chain, Russian targets)** — Pro-Ukrainian hacktivists chained three TrueConf Server flaws (auth bypass on `/admin/*`, arbitrary file read, OS command injection) to land remote shells on Russian deployments since mid-September 2025. Vendor patch shipped 2025-08-27. **Distinct from the previously-covered TrueConf zero-day "Operation TrueChaos" (CVE-2026-3502)** — different actor, different bug class, but same underlying product. Anyone running TrueConf Server outside the latest LTS should patch yesterday.

**Robinhood account-creation flaw abused for phishing (BleepingComputer, 2026-04-27)** — Threat actors abused Robinhood's signup flow to inject phishing copy into legitimate Robinhood-from-Robinhood emails. App-specific abuse rather than a CVE — included as an OSINT signal: any service that lets unauthenticated input flow into transactional email templates is at risk of the same pattern.

**Microsoft Outlook.com sign-in outage (2026-04-27)** — Multi-hour outage preventing customer sign-ins. Operational rather than security; flag for SOC awareness because outages historically coincide with phishing campaigns that piggy-back on the helpdesk-ticket spike.

**CVE-2025-43449 — Apple iOS user tracking-between-installs (CVSS 7.5, 2026-04-27)** — Improper cache handling enables app-store-side tracking of users between reinstalls. Mobile / client-only, out of scope, but worth knowing exists if a CISO asks about Apple's April patch cycle.

**CVE-2026-27785 — Milesight AIOT camera firmware hard-coded credentials (CVSS 8.8, 2026-04-27)** — Embedded device hard-coded creds. Not a remote-services scope item, but Milesight cameras are deployed at scale across enterprise physical-security environments — flag for ops teams running this hardware to push the firmware update from Milesight.

**CVE-2026-34989 — CI4-CMS-ERP / CI4MS stored XSS (CVSS 9.0, 2026-04-27)** — Stored XSS in profile-name field, rendered unsafely across multiple views. Niche CMS, but the CVSS-9 rating reflects unauth-to-account-takeover via session theft. Patch (v31.0.0.0) available.

**CVE-2026-21510 / CVE-2026-21513** — Original LNK-RCE chain that APT28 used in Dec 2025 against Ukraine/EU. Already patched in February 2026; today's entry (CVE-2026-32202) is the incomplete-patch follow-up. Re-stating the originals so dedup later is cleaner.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com, schneier.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (403 — used THN/BC/SecurityWeek for KEV mirror) |
| Vendor advisories | msrc.microsoft.com/blog, fortinet.com/blog/threat-research, spring.io/security | ⚠️ (msrc serves JS shell; Spring advisories pulled directly) |
| Research / OSINT | securitylab.github.com (via github.blog/security), seclists.org/fulldisclosure, kb.cert.org/vuls, avleonov.com, projectzero.google | ✅ / ⚠️ (fulldisclosure has no posts since Apr 14) |
| CVE databases | app.opencve.io, dbugs.ptsecurity.com, github.com/0xMarcio/cve, github.com/search | ✅ |
| Cloud / vendor blogs | blog.cloudflare.com/tag/security, rapid7.com | ✅ / ⚠️ (Cloudflare last post Apr 14) |
| Bug bounty | hackerone.com/hacktivity, bugcrowd.com/disclosures, attackerkb.com | ❌ (JS / 404 / 403) |
| Russian / non-English | habr.com/ru/companies/tomhunter, teletype.in/@cyberok, cert.gov.ua | ⚠️ (no recent / empty extract) |
| Authoritative DBs | nvd.nist.gov, cve.org, cve.mitre.org | ⚠️ / ❌ (no extract for Apr 26-28 / JS) |
| Research labs | googleprojectzero.blogspot.com (now projectzero.google), packetstormsecurity.com (now packetstorm.news) | ⚠️ |

**Errors:** cisa.gov + cisa.gov/known-exploited-vulnerabilities-catalog (403); attackerkb.com (403); bugcrowd.com/disclosures (404); hackerone.com/hacktivity (JS); cve.org, cve.mitre.org (JS); nvd.nist.gov (no extract for Apr 26-28); msrc.microsoft.com/blog (JS shell).
**CISA KEV:** No new additions since 2026-04-24 (Samsung MagicINFO, SimpleHelp x2, D-Link DIR-823X). No federal patch deadlines elapsing 2026-04-28 in the watched set.

---

*Watchtower vulnerability-researcher | Cycle: 2026-04-28/night | Next: 2026-04-29/night*
