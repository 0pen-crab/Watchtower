# Watchtower Night Report — 2026-05-19
**Cycle:** Night | **Generated:** 2026-05-19 03:30 UTC (2026-05-19T03:30:00Z)
**Sources checked:** 19/30 | **CISA KEV total:** Not directly accessible (cisa.gov 403) | **New KEV additions:** None confirmed via secondary sources since Exchange CVE-2026-42897 (5/16)

---

## 🔴 CRITICAL

### ChromaDB CVE-2026-45829 — Pre-Auth Code Injection via Trust-Remote-Code in /collections Endpoint (CVSS 10.0)
**Product:** ChromaDB (open-source vector database) ≥1.0.0 | **CVE:** CVE-2026-45829 | **Status:** Patched (upgrade required) | **PoC:** HiddenLayer research publication

ChromaDB's `/api/v2/tenants/{tenant}/databases/{db}/collections` endpoint accepts a model repository reference plus a `trust_remote_code=true` flag from unauthenticated network clients and instantiates the model, executing attacker-controlled Python on the server. The flaw is CWE-94 (improper control of code generation); attack vector is AV:N/AC:L/PR:N/UI:N — no authentication, no user interaction. ChromaDB powers retrieval pipelines in many production LLM/RAG deployments, and self-hosted instances are routinely exposed on internal networks (and frequently on the public internet via misconfigured ingresses).

**Timeline:** Disclosure 2026-05-18 (PT-Security dbugs PT-2026-41683 + HiddenLayer writeup).

**Why it matters:** Pre-auth RCE on a vector-DB component that has become standard plumbing for enterprise AI deployments. Internet-facing exposure is common; identical primitive class to the Hugging Face / LeRobot pickle-deserialization pattern (CVE-2026-25874, 2026-04-29) — assume opportunistic scanning within days.

**Discovered by:** HiddenLayer (per PT-Security dbugs reference)

**Mitigation:**
- Upgrade ChromaDB to the patched release (consult vendor advisory for exact version on your install track)
- Set `chroma_server_authn_provider` to enforce auth on the `/api/v2` endpoints, and put ChromaDB behind a reverse proxy with mTLS or basic auth at minimum
- Block `/collections` POSTs containing `trust_remote_code` in WAF rules until patched
- Inventory ChromaDB deployments — confirm none are reachable from the public internet

**Sources:** [PT-Security PT-2026-41683](https://dbugs.ptsecurity.com/vulnerability/PT-2026-41683)

---

### Microsoft Azure Local Disconnected Operations CVE-2026-42822 — Unauthenticated Network Privilege Escalation, No Patch Available (CVSS 10.0)
**Product:** Microsoft Azure Local Disconnected Operations | **CVE:** CVE-2026-42822 | **Status:** No patch available yet | **PoC:** Not public; vendor advisory acknowledges severity

CWE-287 improper authentication enables an unauthenticated network-adjacent attacker to elevate privileges over the Azure Local Disconnected Operations control plane. CVSS vector is AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H — the changed scope tag indicates the privilege gain spans an authority boundary (i.e., from "no auth" to admin of the operations component, which manages on-prem Azure Local clusters running in disconnected mode for compliance, sovereignty, or sensitive workloads).

**Timeline:** Disclosed 2026-05-18 (PT-Security PT-2026-41709). Microsoft has not yet published a permanent patch.

**Why it matters:** Disconnected-mode Azure Local clusters are the deployment model for sensitive workloads where cloud connectivity is restricted (defense, regulated industries, sovereign cloud). Compromise of the disconnected operations layer hands an attacker administrative control of the entire on-prem control plane. Coming on the heels of the Microsoft Azure Backup-for-AKS Confused Deputy that Microsoft silently patched without a CVE (MEMORY 2026-05-17), the pattern of high-severity Microsoft cloud-management bugs lingering without patches is intensifying.

**Mitigation:**
- Restrict network access to Azure Local control-plane interfaces — only management subnets, never broader east-west or public exposure
- Monitor MSRC for the patch release; once available, apply during the next maintenance window with elevated priority
- Audit Azure Local Disconnected Operations identity assignments for unexpected role grants
- Until patched, treat any unexplained admin-level changes in disconnected clusters as suspicious

**Sources:** [PT-Security PT-2026-41709](https://dbugs.ptsecurity.com/vulnerability/PT-2026-41709)

---

## 🟠 HIGH

### SGLang LLM-Serving Framework — Two RCEs + Path Traversal, No Patch (VU#777338)
**Product:** SGLang (open-source framework for serving large language models) | **CVE:** CVE-2026-7301 (pickle RCE), CVE-2026-7302 (path traversal), CVE-2026-3304 (dill RCE) | **CVSS:** Not assigned in CERT/CC advisory | **First reported:** 2026-05-18

CMU CERT/CC published VU#777338 disclosing three vulnerabilities in SGLang's multimodal pipeline. CVE-2026-7301: the multimodal scheduler's ROUTER socket calls `pickle.loads()` on incoming messages and binds to 0.0.0.0 by default — any reachable network actor triggers RCE. CVE-2026-7302: unauthenticated path traversal via `../` sequences in upload filenames against the multimodal runtime, enabling arbitrary file write. CVE-2026-3304: when `--enable-custom-logit-processor` is set, the runtime deserializes Python objects via `dill.loads()` without validation, second RCE path. SGLang maintainers did not respond during the coordinated-disclosure window, so no fix is currently published; vendor status is "Unknown" in the advisory.

**Timeline:** Disclosure window opened with maintainers; no response received; CERT/CC published 2026-05-18.

**Why it matters:** SGLang is one of the small set of LLM-serving engines (alongside vLLM, TGI, TensorRT-LLM) used in production inference farms. Default 0.0.0.0 bind plus unauthenticated pickle deserialization is the AI-platform equivalent of an unauthenticated Redis instance — opportunistic mass scanning is the expected response. Maintainer silence increases the window during which exposed deployments remain unpatched.

**Discovered by:** Reported via CMU CERT/CC (researcher not named in public advisory)

**Mitigation:**
- Audit SGLang deployments and confirm they are not exposed on 0.0.0.0 — bind to localhost or internal-only interfaces, front with an authenticated reverse proxy
- Remove `--enable-custom-logit-processor` from production launch configs unless explicitly required
- Block inbound traffic to SGLang ports (default 30000) at the network edge
- Watch for vendor patches and apply immediately; if maintainers remain unresponsive, consider migrating to vLLM/TGI

**Sources:** [CMU CERT/CC VU#777338](https://kb.cert.org/vuls/id/777338)

---

### Palo Alto Networks PAN-OS CVE-2026-0265 — Authentication Bypass via Signature Verification Flaw (CVSS 7.2)
**Product:** PAN-OS on PA-Series, VM-Series firewalls and Panorama (virtual/M-Series) | **CVE:** CVE-2026-0265 | **CVSS:** 7.2 (vendor — disputed by researcher) | **First reported:** 2026-05-13 (Rapid7 ETR published 2026-05-18)

The Cloud Authentication Service (CAS) component performs signature verification incorrectly when CAS is attached to a login interface, allowing an attacker to bypass authentication. Vendor scope-limits the issue to deployments where CAS is enabled and bound to a login interface — common, though not default. Researcher Harsh Jaiswal (HacktronAI) publicly disputes the 7.2 rating, claiming successful exploitation against GlobalProtect portals and other internet-facing components; full technical details are expected the week of 2026-05-18. Patches shipped 2026-05-13 for most version streams; remaining patches expected 2026-05-28. Cloud NGFW and Prisma Access are not affected.

**Timeline:** Vendor advisory 2026-05-13 → Rapid7 ETR + researcher technical-detail tease 2026-05-18 → remaining patches expected 2026-05-28.

**Why it matters:** Second PAN-OS perimeter auth-bypass disclosure of 2026 (first was CVE-2026-0300 captive portal pre-auth RCE, MEMORY 2026-05-07, in KEV with 3-day federal deadline). PAN-OS is a perimeter-class target; the gap between vendor 7.2 and researcher claims of GlobalProtect exploitation is the part to watch — if Jaiswal's writeup materialises this week, expect rapid KEV addition. Cisco SD-WAN, Palo Alto, Fortinet, and Ivanti edges have all had at least one actively exploited critical/high in May 2026 — the perimeter has been the 2026 story.

**Discovered by:** Harsh Jaiswal (HacktronAI), reported via PSIRT

**Mitigation:**
- Apply 2026-05-13 patches immediately on PA-Series, VM-Series, and Panorama running affected PAN-OS versions
- Identify deployments where CAS is bound to a login interface — these are the in-scope configurations
- For GlobalProtect / internet-facing portals, do not delay patching past the 2026-05-28 follow-up release
- Monitor authentication logs for anomalous CAS handshakes; alert on signature-validation failures

**Sources:** [Rapid7 ETR CVE-2026-0265](https://www.rapid7.com/blog/post/etr-cve-2026-0265-authentication-bypass-in-palo-alto-networks-pan-os/)

---

### 🔄 OpenClaw "Claw Chain" Expansion — Cyera Publishes 4-CVE Chain (was 3); MCP Loopback CVE-2026-44118 Adds Privilege Elevation to Owner-Level
**Product:** OpenClaw AI assistant (60,000+ publicly accessible instances) | **CVE:** CVE-2026-44112, CVE-2026-44113, CVE-2026-44115, **CVE-2026-44118** (added) | **CVSS:** 9.6 (CVE-2026-44112) | **First reported:** 2026-05-16 (3-CVE batch); 2026-05-18 (Cyera 4-CVE Claw Chain writeup) | **Previous score:** 6 → **Now:** 7

The 2026-05-16 Watchtower entry covered the OpenClaw OpenShell sandbox race-condition chain (CVE-2026-44112/44113/44115). Cyera's 2026-05-18 "Claw Chain" publication adds **CVE-2026-44118** — an MCP loopback vulnerability that enables privilege elevation from sandbox-level to owner-level access on the host system, completing the disclosed chain from "sandbox code execution" to "credentials + API keys + tokens + config files + persistent backdoor." Each chain step looks like normal agent behavior to traditional EDR/CASB controls, which is the durable defensive problem. Patches deployed 2026-04-23 (one day after disclosure on 2026-04-22), but instance-update cadence remains the operational risk surface.

**Why this update:** Material change — the chain is now disclosed as 4 CVEs and the full primitive (sandbox → owner) is publicly documented by Cyera. Defenders previously seeing a "3-CVE race-condition cluster" should now treat this as a complete sandbox-to-host-takeover playbook against any OpenClaw instance not on the latest patch level.

**Why it matters:** Per MEMORY 2026-03-30, the OpenClaw fleet runs significantly behind latest — 6+ weeks lag is typical. With a fully documented sandbox-to-owner chain now public, mass-scan adversaries can fingerprint and exploit lagging instances at scale.

**Mitigation:**
- `openclaw update` on all instances — confirm version ≥ the 2026-04-23 release containing all four fixes
- Audit OpenClaw instance inventory: any internet-reachable instance is now an immediate exposure
- Validate MCP server configuration is not exposed beyond loopback where unnecessary; restrict MCP transport scope
- Review OpenClaw audit logs for unusual file-system reads, OpenShell invocations, and credential-bearing environment variables accessed by agent processes

**Sources:** [SecurityWeek — Claw Chain](https://www.securityweek.com/claw-chain-openclaw-flaws-allow-sandbox-escape-backdoor-delivery/)

---

### 📰 First Shai-Hulud Worm Clones in the Wild — Non-TeamPCP Actor Weaponizes Leaked Source in npm Campaign
**Product:** npm ecosystem (developer machines, CI runners, downstream package installs) | **CVE:** N/A (campaign / malware) | **First reported:** 2026-05-18

Within ~72 hours of TeamPCP publishing the Shai-Hulud worm source code on BreachForums (MEMORY 2026-05-16) and the $1,000 prize contest (MEMORY 2026-05-15), four malicious npm packages were observed in the wild from threat actor `_deadcode09284814_`: **chalk-tempalte** (Shai-Hulud clone, near-unmodified leaked source with no obfuscation), **@deadcode09284814/axios-util**, **axois-utils** (with HTTP/TCP/UDP DDoS botnet capability), and **color-style-utils** (crypto wallet + IP information stealer). Three of the four use Axios typosquatting. Combined downloads were limited (~2,678) at takedown, but the campaign represents the **first confirmed weaponization of the leaked Shai-Hulud primitive by a distinct actor from TeamPCP** — exactly the commoditization pattern predicted in the 2026-05-16 Watchtower entry (cited Mirai/Conti precedent for 3-7 distinct Wave-2-class compromises by 2026-06-15). OXsecurity attributes the actor as **distinct from TeamPCP** based on the lack of obfuscation; exfil to `87e0bbc636999[.]lhr[.]life`.

**Timeline:** TeamPCP source release 2026-05-16 → first clone in the wild observed 2026-05-17 → BleepingComputer/SecurityWeek/THN coverage 2026-05-18.

**Why it matters:** Commoditization of supply-chain worm tooling is the durable threat — the worm primitive (trusted-publisher self-propagation + GitHub Actions OIDC theft + provenance-attestation abuse) is now usable by actors who don't have TeamPCP's tradecraft. Expect a steady drip of clones over the next 30 days, with progressively lower technical sophistication and progressively higher noise. The defensive posture (rotate-on-detection, canary tokens in CI runner secret context, audit `pull_request_target` exposure) does not change but must be applied consistently across the entire 169+ confirmed Wave-2 package fan-out plus expected clone wave.

**Discovered by:** OXsecurity, with parallel coverage from BleepingComputer / SecurityWeek / The Hacker News

**Mitigation:**
- Block the four malicious packages explicitly in npm proxy / artifact registry policy: `chalk-tempalte`, `@deadcode09284814/axios-util`, `axois-utils`, `color-style-utils`
- Block outbound DNS / network traffic to `87e0bbc636999.lhr.life` and the `lhr.life` parent domain at the egress
- Audit recent `npm install` activity on developer laptops and CI runners for the four named packages
- Implement typosquatting detection for Axios family packages in your dependency-resolution pipeline (Socket, Snyk, Aikido, etc.)
- Continue the canary-token-in-CI-runner-secrets approach (per Grafana 2026-05-18 disclosure)

**Sources:** [SecurityWeek — Shai-Hulud Clones](https://www.securityweek.com/first-shai-hulud-worm-clones-emerge/) | [BleepingComputer](https://www.bleepingcomputer.com/news/security/leaked-shai-hulud-malware-fuels-new-npm-infostealer-campaign/) | [The Hacker News](https://thehackernews.com/2026/05/four-malicious-npm-packages-deliver.html)

---

### 7-Eleven Salesforce Breach — 600,000+ Records Stolen by ShinyHunters (CoinbaseCartel Cluster)
**Product:** Salesforce (third-party SaaS) at 7-Eleven | **CVE:** N/A | **First reported:** 2026-04-17 (leak-site listing); confirmed by 7-Eleven 2026-05-18

7-Eleven confirmed (2026-05-18) that intrusion was detected 2026-04-08; ShinyHunters listed the company on its leak site 2026-04-17 with a $250,000 ransom and 2026-04-21 deadline. Stolen data: 600,000+ Salesforce records including personal information from franchise applications and corporate data. Attack vector matches the broader ShinyHunters Salesforce-targeting campaign documented since mid-2025 — phishing, abuse of third-party Salesforce integrations, or instance misconfiguration. This is the same actor cluster (ShinyHunters / Scattered Spider / LAPSUS$ offshoots → CoinbaseCartel) credited with the **Grafana GitHub codebase theft (Watchtower 2026-05-18)** and the broader 2026-Q2 SaaS-extortion wave.

**Timeline:** Intrusion 2026-04-08 → leak-site listing 2026-04-17 → ransom deadline 2026-04-21 → public confirmation 2026-05-18 (Maine breach-notification disclosure).

**Why it matters:** Confirms the CoinbaseCartel-cluster Salesforce-pivot pattern is operational against retail/franchise targets in addition to observability/IaC vendors (Grafana). Two confirmed compromise vectors are now visible in the same actor cluster within a 7-day window: GitHub OAuth-token theft (Grafana) and Salesforce ecosystem abuse (7-Eleven). Companies running Salesforce with externally accessible AppExchange integrations or third-party connectors should treat themselves as priority targets.

**Mitigation:**
- Audit Salesforce connected-apps, third-party AppExchange integrations, and OAuth grants for unused / dormant / over-privileged entries
- Enable Salesforce Shield Event Monitoring with alerts on bulk export, anomalous report runs, and API calls from new IP/UA combinations
- Enforce IP allowlisting on Salesforce session restrictions for admin / data-export-privileged users
- Apply phishing-resistant MFA (FIDO2) on all Salesforce admin accounts and review IP login policies
- Map the same defensive ask back across other SaaS — same actor cluster has pivoted to Snowflake, GitHub, Workday in prior incidents

**Sources:** [SecurityWeek — 7-Eleven breach](https://www.securityweek.com/7-eleven-data-breach-confirmed-after-shinyhunters-ransom-demand/)

---

## 🟡 MEDIUM

### CISA Contractor Leaked AWS GovCloud Credentials via Public "Private-CISA" GitHub Repo
**Product:** CISA Landing Zone DevSecOps environment (AWS GovCloud) | **CVE:** N/A | **Published:** 2026-05-18

GitGuardian researcher Guillaume Valadon discovered a CISA-contractor-owned public repository named "Private-CISA" exposing privileged AWS GovCloud administrative credentials, internal-system passwords, and tokens for CISA's Landing Zone DevSecOps environment until 2026-05-15. The repository owner had explicitly disabled GitHub's push-protection (secrets-detection) feature. Security consultant Philippe Caturegli notes the exposed artifactory access could enable supply-chain backdoors in CISA-managed software packages.

**Mitigation:**
- For organizations using GitGuardian/Stack/TruffleHog/etc — extend monitoring beyond corporate accounts to contractor/employee personal repos via org-aware scanning
- Mandate that GitHub push-protection cannot be disabled at the org level for any repository under any GitHub username associated with corporate work
- For federal contractors with similar exposure surface, audit GitHub usernames and repos for the past 90 days; revoke any non-corporate-account-owned exposure
- Treat all credentials in the exposed repository as compromised — rotate without delay; assume access to artifactory means software-supply-chain implants are possible

**Sources:** [Krebs on Security](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/)

---

### AWS Amazon Redshift Python Connector CVE-2026-8838 — eval() on Server Data Enables MITM Code Execution in BI Clients (CVSS 9.8)
**Product:** amazon-redshift-python-driver < 2.1.14 | **CVE:** CVE-2026-8838 | **Published:** 2026-05-18

The `vector in()` function unsafely passes server-returned data to Python's `eval()`. An attacker with network position (or a MITM capability between BI tool and Redshift cluster — including ARP/DNS spoofing on lateral networks, compromised intermediate proxies, or stolen Redshift endpoints) can return crafted result data that executes arbitrary Python in the client process. Equivalent attack surface to last week's Amazon Redshift JDBC CVE-2026-8178 (MEMORY 2026-05-16), but in the Python driver instead of the JVM driver — and impacts every Airflow worker, dbt run, analyst notebook, and BI tool that connects to Redshift using this driver.

**Mitigation:** Upgrade `amazon-redshift-python-driver` to 2.1.14+ in every analyst notebook, Airflow image, dbt environment, and BI tool that uses the Python driver — rebuild containers, update lockfiles. Enforce TLS-with-cert-validation on every Redshift connection (no `sslmode=disable`). Network-level: ensure analyst → Redshift traffic is end-to-end-encrypted on private networking (PrivateLink, VPC peering) rather than across NAT/intermediate proxies that could be MITM'd.

**Sources:** [PT-Security PT-2026-41734](https://dbugs.ptsecurity.com/vulnerability/PT-2026-41734)

---

## 📋 Noted / Monitoring

**n8n CVE-2026-42231 + CVE-2026-42232 (full disclosure context)** — Thursday's THN multi-vendor wrap-up reveals the n8n batch is 5 CVEs total (not 3 as covered 2026-05-16); the additional two (xml2js prototype pollution + global prototype pollution via XML Node) were fixed in 1.123.32 — earlier than the 1.123.43 patches covered. No new defensive action; documentation alignment only.

**Ivanti Xtraction CVE-2026-8043 (CVSS 9.6)** — External file-name control allows an authenticated remote attacker to read sensitive files. Patched in 2026.2+. Authenticated-only, narrower than the recent Ivanti EPMM / Cloud SSA CVEs.

**Linux Kernel Copy Fail CVE-2026-31431 public multi-language PoC released (oss-security 2026-05-18)** — Andrei Berestov posted exploit code in C, Python, Perl, and x86_64 NASM. All stable kernels patched 2026-04-30. Item is already in KEV (MEMORY 2026-05-03 / 2026-05-05) and previously covered at score 8; mass-availability of working PoC raises operational urgency but does not warrant a new finding.

**lwIP CVE-2026-8836 (CVSS 10.0)** — Pre-auth stack overflow in SNMPv3 USM handler (`snmp_parse_inbound_frame()` via `msgAuthenticationParameters`). Affects lwIP < 2.2.2. Primarily an embedded/IoT firmware concern; restrict SNMPv3 USM exposure on any lwIP-based device.

**Dokploy CVE-2026-27130 (CVSS 9.9)** — Authenticated OS-command injection via the application-name parameter (shell metacharacters bypass `cleanAppName`). Patched in 0.26.7. Self-hosted deployment platform; small footprint but full host RCE post-auth.

**AutoGPT CVE-2026-30950 (CVSS 7.1)** — Authenticated IDOR enables session hijack and message access. AutoGPT deployments are usually internal but exposed instances exist.

**FacturaScripts CVE-2026-27891 (CVSS 7.2)** — Zip-slip via uploaded archive enables arbitrary file write → RCE. Companion CVE-2026-27964 (CVSS 3.9) reflected XSS via `fsNick` cookie. ERP software for SMBs.

**DumbAssets CVE-2026-45230 (CVSS 9.1)** — Pre-auth path-traversal enables arbitrary file deletion. Niche product but no-auth file delete is destructive.

**Bouncy Castle (BC-JAVA) CVE-2026-0636 (CVSS 6.5)** — LDAP injection in `LDAPStoreHelper` affecting 1.74 through 1.84. Bouncy Castle is bundled into a large number of Java enterprise stacks; impact depends on whether the application surfaces `LDAPStoreHelper` to untrusted input.

**Vim multiple vimscript / netrw / filetype-plugin code-injection CVEs (oss-security 2026-05-17)** — Pre-9.2.495 / 9.2.496. Client-side, OOS for Watchtower (no remote infrastructure component), logged for completeness.

**Net::Statsd::Lite / Tiny / Crypt::OpenSSL::PKCS12 Perl module CVEs (oss-security 2026-05-16 / 17 / 18)** — CVE-2026-46719, CVE-2026-46720, CVE-2026-8507, CVE-2026-8721, CVE-2026-8788. Metric-injection / OOB-write / password-truncation. Low-impact, client-only.

**Cloudflare Project Glasswing publication (2026-05-18)** — Cloudflare published its evaluation of "cyber frontier models" (Anthropic Mythos, OpenAI gpt-5.5-Cyber, GPT-5.5) against live infrastructure code. Joins the MDASH (Microsoft) / Daybreak (OpenAI) / Glasswing (Google + Cloudflare) cluster of AI vuln-finder disclosure programs. Calibration note rather than a finding.

**SHub macOS "Reaper" infostealer variant (BleepingComputer 2026-05-18)** — AppleScript-based fake Apple security-update lure, browser/wallet/iCloud/Telegram data theft. Client-side; OOS for Watchtower (no remote infrastructure component) but worth endpoint-team awareness.

**INTERPOL Operation Ramz (BleepingComputer 2026-05-18)** — 201 arrests across MENA targeting phishing-as-a-service infrastructure; 53 servers seized. Law-enforcement-only signal; not a vulnerability, but reduces the active phishing-kit operator pool short-term.

**Tycoon2FA + Trustifi device-code phishing (BleepingComputer 2026-05-17 → eSentire research)** — Already covered in MEMORY 2026-05-18 contextual log; THN/BC echo-coverage 2026-05-17. Device-code phishing up 37× year-over-year per Push Security; 10+ phishing-as-a-service platforms now support the tactic.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com, schneier.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (403 Forbidden via WebFetch — KEV data sourced via THN/Krebs/SecurityWeek) |
| Vendor / Researcher | rapid7.com, fortinet.com/blog/threat-research, securitylab.github.com, blog.cloudflare.com/tag/security, googleprojectzero.blogspot.com (→ projectzero.google), msrc.microsoft.com/blog | ⚠️ (msrc redirects to /blog homepage, no content) |
| Research / OSINT | seclists.org/fulldisclosure, attackerkb.com, packetstormsecurity.com (→ packetstorm.news), opencve.io, github.com/0xMarcio/cve, dbugs.ptsecurity.com, avleonov.com, kb.cert.org/vuls | ⚠️ (attackerkb 403, packetstorm content not accessible via WebFetch) |
| Reference DBs | nvd.nist.gov, cve.mitre.org, cve.org, hackerone.com/hacktivity, bugcrowd.com/disclosures, github.com/search?q=CVE | ⚠️ (cve.mitre/cve.org/hackerone/bugcrowd JS-only, github.com/search auth-required) |
| Russian-language | habr.com/ru/companies/tomhunter/articles, teletype.in/@cyberok | ⚠️ (returned stale content — newest visible posts pre-date May 14) |
| Other | cert.gov.ua | ⚠️ (page loaded but no advisory content returned via WebFetch) |

**Errors:** cisa.gov (403), cisa.gov/known-exploited-vulnerabilities-catalog (403), attackerkb.com (403), packetstormsecurity.com (content not accessible via WebFetch), cve.mitre.org (JS-only), cve.org (JS-only), msrc.microsoft.com/blog (redirects, no content), hackerone.com/hacktivity (JS-only), bugcrowd.com/disclosures (404), cert.gov.ua (no content), github.com/search?q=CVE (auth required).

**CISA KEV:** No new additions confirmed via secondary sources since CVE-2026-42897 Microsoft Exchange (2026-05-17, MEMORY) — 21-day federal deadline 2026-06-06.

---

*Watchtower vulnerability-researcher | Cycle: 2026-05-19/night | Next: 2026-05-20/night*
