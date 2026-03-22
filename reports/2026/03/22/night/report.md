# Vulnerability Intelligence Report — 2026-03-22 Night

**Cycle:** Night (00:00 UTC)
**Generated:** 2026-03-22T00:00:00Z

---

## 📰 React2Shell (CVE-2025-55182 / CVE-2025-66478) — Next.js / React Server Components Pre-Auth RCE — Original PoC Now Public

**Threat Score:** 9/10
**Affected Technology:** React.js (Server Components), Next.js (via vendored RSC)
**CVE:** CVE-2025-55182 / CVE-2025-66478
**CVSS:** 10.0

### Summary
CVE-2025-55182 ("React2Shell") is a CVSS 10.0 pre-authentication RCE vulnerability in React Server Components that allows arbitrary server-side code execution via a parser confusion attack on the RSC wire protocol (`$@x` chunk reference abuse → prototype chain manipulation → `_formData` gadget → shell). Originally disclosed to Meta and Vercel on November 29, 2025, and patched on December 3, 2025, the vulnerability has been in active exploitation by China-nexus threat actors since early December. Today (March 21-22, 2026), the original researcher (lachlan2k) published the full PoC including the `01-submitted-poc.js` that was originally filed with Meta — triggering a new wave of scanner releases, including a detection plugin in Google's Tsunami security scanner. Multiple independent PoC repositories now collectively exceed 3,000 GitHub stars. CVE-2025-66478 is a duplicate CVE assigned specifically for Next.js due to its vendored React bundling (standard dependency scanners do not flag it as vulnerable without the extra CVE). Exploitation requires that server functions be exposed via RSC; Next.js apps with Server Actions or RSC enabled are in scope. The exploit chain does NOT require the developer to have explicitly exposed dangerous functions — the genuine PoC bypasses this constraint.

### Why It Matters
Any of our Next.js or React Server Components workloads running pre-patch versions are exposed to unauthenticated shell access; the original researcher's PoC publication significantly lowers the bar for exploitation, and Google's Tsunami scanner means mass scanning for vulnerable instances is now trivial.

### Discovery
**First seen at:** github.com/0xMarcio/cve (trending PoC repos — 1000+ stars), corroborated via react2shell.com
**How found:** PoC repos trending on GitHub PoC tracker; cross-referenced react2shell.com for original researcher's disclosure; confirmed Google Tsunami scanner plugin active.

### Sources
- https://react2shell.com
- https://github.com/lachlan2k/React2Shell-CVE-2025-55182-original-poc
- https://github.com/facebook/react/security/advisories/GHSA-fv66-9v8q-g76r
- https://github.com/vercel/next.js/security/advisories/GHSA-9qr9-h5gf-34mp
- https://github.com/google/tsunami-security-scanner-plugins/commit/107447fda6ab86aa1ed703af9560a98d7c16f104

---

## 📰 TeamPCP CanisterWorm — Self-Propagating npm Supply Chain Attack Expands to 135 Malicious Artifacts

**Threat Score:** 9/10
**Affected Technology:** npm ecosystem (Node.js / JavaScript supply chain), GitHub Actions CI/CD
**CVE:** Not yet assigned
**CVSS:** N/A

### Summary
TeamPCP, the threat actor behind the earlier Aqua Security Trivy GitHub Actions tag compromise (March 19-21, 2026), has dramatically expanded their supply chain campaign into the npm ecosystem. As of March 21, 2026, the attack — dubbed "CanisterWorm" — has spread to 135 malicious package artifacts spanning 64+ unique packages, primarily under the `@emilgroup` and `@teale.io` publisher namespaces. The malware chain works as follows: a `postinstall` hook installs a Python dropper as a `systemd --user` service (`pgmon`), which polls an Internet Computer Protocol (ICP) blockchain canister as a dead-drop C2 channel, retrieves a follow-on binary URL, downloads it to `/tmp/pglog`, and executes it — the canister C2 architecture allows TeamPCP to swap second-stage payloads without touching the already-deployed implant. Critically, a worm component in `@teale.io/eslint-config` harvests npm publish tokens from `.npmrc`, environment variables, and npm config — then autonomously republishes the compromised payload to additional packages reachable by those credentials, creating a self-amplifying spread. The earlier Trivy GitHub Actions attack (force-updated 75/76 tags in the aquasecurity/trivy-action repo to deliver an infostealer) is confirmed as the same actor's initial salvo. CI/CD pipelines, developer workstations, and any system running `npm install` against these packages are at risk of credential theft (npm tokens, SSH keys, cloud API keys, environment secrets).

### Why It Matters
Any of our CI/CD pipelines or developer environments that install npm packages from compromised namespaces face live credential harvesting and persistent backdoor installation; the worm's self-propagating token-harvesting mechanism means secondary contamination of packages we publish is also possible.

### Discovery
**First seen at:** bleepingcomputer.com (Trivy initial vector), wiz.io/blog (attribution to TeamPCP), socket.dev/blog (CanisterWorm detailed analysis)
**How found:** BleepingComputer article on Trivy GitHub Actions compromise led to Wiz attribution to TeamPCP; cross-referencing Socket.dev revealed the full npm expansion scope confirmed as of March 21, 2026.

### Sources
- https://www.bleepingcomputer.com/news/security/trivy-vulnerability-scanner-breach-pushed-infostealer-via-github-actions/
- https://www.wiz.io/blog/trivy-compromised-teampcp-supply-chain-attack
- https://socket.dev/blog/canisterworm-npm-publisher-compromise-deploys-backdoor-across-29-packages
- https://socket.dev/supply-chain-attacks/canisterworm
- https://www.aikido.dev/blog/teampcp-deploys-worm-npm-trivy-compromise

---

## 📋 Noted

- **CVE-2025-32975** — Quest KACE Systems Management Appliance: Critical vulnerability reported as potentially exploited in attacks against education sector organizations; insufficient public technical detail available as of this cycle.

- **CVE-2026-33150 / CVE-2026-33179** — libfuse (io_uring): Use-after-free (CVE-2026-33150) and NULL dereference (CVE-2026-33179) in libfuse's io_uring I/O path, disclosed via oss-security on March 21, 2026; primarily a local privilege escalation vector in Linux systems running FUSE filesystems with io_uring, no remote vector confirmed.

- **CVE-2026-31381 / CVE-2026-31382** — Gainsight Assist (Chrome/Outlook plugin): Chained information disclosure (PII/email in base64 OAuth state parameter, CVSS 5.3) and reflected XSS via `error_description` parameter with Safari `onpagereveal` WAF bypass (CVSS 6.1), discovered and disclosed by Rapid7 Labs; patched by Gainsight server-side March 6 and plugin update March 9, 2026.

- **CVE-2026-27459** — pyOpenSSL 26.0.0: Buffer overflow in DTLS cookie callback when a callback returns a cookie exceeding DTLS1_COOKIE_LENGTH bytes; fixed in pyOpenSSL 26.0.0 released March 15, 2026.

- **CVE-2026-25757** — Spree Commerce: Insecure Direct Object Reference (IDOR) allowing unauthorized access to PII, discovered by GitHub Security Lab; patch status and CVSS not yet available.

- **[No CVE]** — Microsoft Azure Monitor Callback Phishing: Threat actors are creating Azure Monitor alerts with fake Microsoft billing warnings in the description field, causing legitimate emails from azure-noreply@microsoft.com (passing SPF/DKIM/DMARC) to be delivered to victims as callback phishing lures; a novel infrastructure-abuse technique with no patch available (platform design limitation).

---

## 📡 Source Coverage

**Sources checked:** 30/31
**Sources with findings:** 6

| Status | Source | Notes |
|--------|--------|-------|
| ✅ | bleepingcomputer.com | Trivy/CanisterWorm finding; Azure Monitor phishing (noted) |
| ✅ | thehackernews.com | Nothing new in scope |
| ✅ | cisa.gov/known-exploited-vulnerabilities-catalog | No new KEV additions since last cycle |
| ✅ | cisa.gov | No additional findings |
| ✅ | securityweek.com | CVE-2025-32975 Quest KACE (noted) |
| ⚠️ | github.com/search?q=CVE | JS-heavy; used github.com/0xMarcio/cve as effective proxy |
| ✅ | schneier.com | Nothing new in scope |
| ✅ | krebsonsecurity.com | Nothing new (prior cycles) |
| ✅ | rapid7.com | CVE-2026-31381/31382 Gainsight (noted); Teams phishing guidance |
| ✅ | attackerkb.com | CVE-2026-20127 Cisco SD-WAN (prior cycle) |
| ✅ | fortinet.com/blog/threat-research | Nothing new beyond prior Iran coverage |
| ✅ | securitylab.github.com | CVE-2026-25757 Spree IDOR (noted) |
| ✅ | seclists.org/fulldisclosure | CVE-2026-33150/33179 libfuse (noted); March 21 index checked |
| ✅ | packetstormsecurity.com | Nothing new in scope |
| ✅ | opencve.io | Platform UI only, no public feed without login |
| ✅ | nvd.nist.gov | No new critical CVEs surfaced via search |
| ✅ | cve.mitre.org | Redirects to cve.org; minimal content |
| ✅ | cve.org | Minimal content rendered |
| ✅ | googleprojectzero.blogspot.com | Windows UAC fuzzing research (LPE, out of scope) |
| ✅ | blog.cloudflare.com/tag/security | Product announcements only |
| ✅ | msrc.microsoft.com/blog | Minimal content rendered |
| ⚠️ | hackerone.com/hacktivity | JS-heavy; empty body rendered |
| ❌ | bugcrowd.com/disclosures | 404 Not Found |
| ✅ | seclists.org/fulldisclosure | Duplicate entry — already checked above |
| ✅ | kb.cert.org/vuls | Landing page only, no new advisories |
| ✅ | avleonov.com | n8n/DWM context only (prior cycles) |
| ✅ | github.com/0xMarcio/cve | React2Shell PoC trending (finding); other PoCs in dedup |
| ✅ | dbugs.ptsecurity.com | Minimal content rendered |
| ✅ | habr.com/ru/companies/tomhunter/articles | Feb 2026 digest only |
| ✅ | teletype.in/@cyberok | Dec 2025/Jan 2026 content only |
| ✅ | cert.gov.ua | Minimal content rendered |
