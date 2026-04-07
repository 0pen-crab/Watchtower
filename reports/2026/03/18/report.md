# Watchtower — 2026-03-18 · Night Cycle

**Generated:** 2026-03-18 02:12 EET (00:12 UTC)
**Sources Checked:** 30 of 31 | Unreachable: 1 (attackerkb.com) | Degraded: 9 | With Findings: 8
**Findings:** 9 new | **Noted:** 6

---

## Findings

---

### 1. Veeam Backup & Replication — Five Critical/High CVEs Allow Authenticated RCE and Credential Theft
**CVEs:** CVE-2026-21669, CVE-2026-21671, CVE-2026-21708, CVE-2026-21672, CVE-2026-21670
**CVSS:** 9.9 / 9.1 / 9.9 / 8.8 / 7.7 | **Threat Score:** 8/10 | **Latency:** Late (6 days) | **First Seen:** 2026-03-12

On March 12, Veeam released patches for five vulnerabilities in Backup & Replication. The two most severe — CVE-2026-21669 (CVSS 9.9) and CVE-2026-21708 (CVSS 9.9) — allow RCE with minimal privilege: the first requires only a domain user account and targets the Backup Server process; the second requires only the Backup Viewer role (a read-only role many organizations grant broadly) and achieves RCE in high-availability deployments as the PostgreSQL user. CVE-2026-21671 (CVSS 9.1) targets HA environments and requires Backup Administrator access. CVE-2026-21672 (CVSS 8.8) enables local privilege escalation on Windows-based Veeam servers. CVE-2026-21670 (CVSS 7.7) allows extraction of saved SSH credentials.

No public proof-of-concept or active exploitation has been observed at time of writing. However, threat score is elevated because Veeam Backup & Replication is consistently one of the highest-value targets for ransomware operators: groups including Akira and Fog actively seek Veeam access as the first step after domain compromise to destroy backup chains, making recovery impossible before or after ransomware detonation. The authenticated-but-low-privilege bar for the worst CVEs means a single compromised domain account is sufficient to execute on the Backup Server.

**Action:** Upgrade to the latest fixed build immediately (see Veeam KB4831). Limit the Backup Viewer role to only users who absolutely require it. Ensure Veeam servers are not directly reachable from workstation subnets.

**References:**
- https://www.veeam.com/kb4831
- https://arcticwolf.com/resources/blog/multiple-authenticated-high-and-critical-vulnerabilities-veeam-backup-replication/

---

### 2. "Poisoned Typeface" — Font-Rendering Attack Hides Malicious Commands from All Major AI Assistants
**CVE:** Not yet assigned (rejected as out-of-scope by all vendors except Microsoft)
**Threat Score:** 7/10 | **Latency:** On-time | **First Seen:** 2026-03-17 | **PoC:** Public

LayerX Security published today a proof-of-concept technique — which they named "Poisoned Typeface" — demonstrating a fundamental disconnect between what AI assistants read and what browsers render. The attack works as follows: an attacker creates a webpage that uses custom web fonts with glyph substitution (character remapping) and CSS manipulation (near-zero opacity, tiny font size, or matching foreground/background colors). The DOM contains harmless text that an AI assistant's HTML parser sees. The browser's rendering engine, however, decodes the font substitution and displays a completely different, malicious instruction (such as a reverse shell command) to the human user. When the user asks their AI assistant "is this command safe to run?", the assistant sees only the benign DOM text and responds affirmatively.

In testing conducted in December 2025, LayerX successfully fooled 11 major AI assistants: ChatGPT, Claude, Copilot, Gemini, Leo, Grok, Perplexity, Sigma, Dia, Fellou, and Genspark. LayerX reported findings to all vendors on December 16, 2025. Microsoft was the only company to accept the report, escalate it to MSRC, and fully address it — Copilot has been patched. Google initially accepted it as high priority but later closed it, saying it could not cause "significant user harm" and was "overly reliant on social engineering." All other vendors declined.

A live PoC page demonstrating the attack remains accessible at layerxresearch.com/RaptureFuture (a fake Bioshock easter egg). This attack is in scope for our monitoring given our coverage of AI assistant security, prompt injection attacks, and OpenClaw-relevant vectors.

**Action:** AI assistant users should never rely solely on an AI tool to verify the safety of commands found on web pages. Organizations deploying AI coding or IT assistants should train staff on this class of attack. AI vendors should implement DOM/render comparison to detect font-based obfuscation.

**References:**
- https://www.bleepingcomputer.com/news/security/new-font-rendering-trick-hides-malicious-commands-from-ai-tools/
- https://layerxsecurity.com/blog/poisoned-typeface-a-simple-font-rendering-poisons-every-ai-assistant-and-only-microsoft-cares

---

### 3. LeakNet Ransomware Combines ClickFix Social Engineering with Deno Runtime Loader
**CVE:** N/A | **Threat Score:** 7/10 | **Latency:** On-time | **First Seen:** 2026-03-17 | **Actively Exploited**

BleepingComputer reported today that the LeakNet ransomware-as-a-service operation has adopted two novel techniques for initial access and EDR evasion. For initial access, LeakNet uses ClickFix: fake CAPTCHA pages, browser error dialogs, or IT support sites instruct users to open a Run dialog or PowerShell terminal and paste a command — which executes a malicious payload while appearing to be a legitimate fix. This technique has been gaining rapid adoption across threat actor groups (previously seen with Velvet Tempest and Termite ransomware, reported 2026-03-09). For the subsequent loader stage, LeakNet deploys malware built on the open-source Deno runtime — the modern JavaScript/TypeScript runtime that succeeds Node.js. Deno executables are signed with legitimate code-signing certificates, making them trusted by many EDR application allow-lists that whitelist common development runtimes.

The combination creates a fast path: ClickFix bypasses user security awareness by abusing trust in IT support workflows, and Deno bypasses endpoint detection by appearing as a trusted development tool. The approach is particularly dangerous in developer-heavy environments where Deno may already be installed.

**Action:** Restrict PowerShell execution policy to AllSigned or RemoteSigned on endpoints. Deploy application allowlisting that specifically controls Deno.exe execution by context (developer workstations may whitelist it; other endpoints should not). Train users to recognize ClickFix social engineering patterns: no legitimate website, CAPTCHA, or IT portal will ever ask you to paste a command into PowerShell.

**References:**
- https://www.bleepingcomputer.com/news/security/leaknet-ransomware-uses-clickfix-and-deno-runtime-for-stealthy-attacks/

---

### 4. Starkiller PhaaS Platform Uses Live AitM Headless-Chrome Reverse Proxy to Bypass MFA
**CVE:** N/A | **Threat Score:** 7/10 | **Latency:** On-time | **First Seen:** 2026-03-17 | **Actively Exploited**

Abnormal Security disclosed details of Starkiller, a phishing-as-a-service platform advertised by the "Jinkusu" group, which represents a significant evolution over template-based phishing kits. Instead of hosting a static copy of a target brand's login page, Starkiller runs a headless Chrome browser instance inside a Docker container that loads the real brand's website live and acts as a real-time adversary-in-the-middle reverse proxy between the victim and the legitimate site. The victim is served genuine, up-to-date page content through attacker-controlled infrastructure. Every keystroke, form submission, one-time password, and session token is captured and forwarded, with the attacker simultaneously replaying the session in real time to the legitimate site.

This architecture provides three key attacker advantages over traditional phishing kits: (1) pages are never out-of-date since they render directly from the real site; (2) there are no static HTML templates for security vendors to fingerprint or blocklist; (3) MFA is fully bypassed because the session token is captured mid-authentication and immediately used by the attacker. The dashboard allows selection of any brand to impersonate by entering a custom URL, choice of lure keywords, and integration with URL shorteners like TinyURL for delivery.

TOTP-based and SMS-based MFA are completely defeated by this architecture. Only hardware security keys implementing FIDO2/WebAuthn (which bind authentication to the origin domain) are resistant.

**Action:** Migrate to FIDO2/passkey-based authentication for all critical accounts. Implement Conditional Access policies requiring compliant/managed devices. Deploy anti-phishing URL scanning at the DNS and proxy layer. Monitor for session token reuse from unexpected geolocations or device fingerprints.

**References:**
- https://thehackernews.com/2026/03/starkiller-phishing-suite-uses-aitm.html
- https://abnormal.ai/blog/starkiller-phishing-kit

---

### 5. CVE-2026-0628 "Glic Jack" — Chrome Gemini Side Panel Lets Malicious Extensions Access Local Files, Camera, and Mic
**CVE:** CVE-2026-0628 | **CVSS:** 8.8 | **Threat Score:** 7/10 | **Latency:** On-time (full disclosure today; patched Jan 2026)

Unit 42 researcher Gal Weizman published full technical details today for CVE-2026-0628, which he named "Glic Jack" (Gemini Live in Chrome hijack). The vulnerability exists in Chrome's chrome://glic page — the Gemini AI side panel Google integrated into Chrome in September 2025 — which uses a WebView component to load gemini.google.com. Due to insufficient policy enforcement, a malicious browser extension with only basic permissions (not the elevated "manage" permission) can inject scripts or HTML into this high-privilege WebView context.

With this foothold, an attacker can: read local files from the filesystem, access the device camera and microphone without user consent prompts, and capture screenshots of any website the user visits. The issue was reported by Weizman to Google on November 23, 2025, and patched in Chrome 143.0.7499.192 in early January 2026. Weizman notes the broader implication: as browsers integrate AI agents with elevated access to the browsing environment for multi-step task automation (summarization, form filling, code execution), each new AI integration creates new attack surface. Malicious web content could also perform indirect prompt injection against the Gemini panel, potentially persisting malicious instructions in long-term memory across browser sessions.

**Action:** Ensure Chrome is updated to version 143.0.7499.192 or later. Audit all installed Chrome extensions — remove any that are not from trusted sources or that have broader permissions than necessary. Organizations running older locked-down Chrome builds should prioritize updating.

**References:**
- https://thehackernews.com/2026/03/new-chrome-vulnerability-let-malicious.html
- https://unit42.paloaltonetworks.com/gemini-live-in-chrome-hijacking/

---

### 6. CVE-2026-29000 — pac4j JWT Authentication Bypass via alg=none in JWE — Public PoC Exists
**CVE:** CVE-2026-29000 | **CVSS:** Critical (maximum severity per pac4j; NVD score pending) | **Threat Score:** 7/10 | **Latency:** Late (15 days) | **PoC:** Public

pac4j patched a maximum-severity authentication bypass in its pac4j-jwt component on March 3. The vulnerability is a classic algorithm confusion variant specific to JWE (encrypted JWT) flows. When JwtAuthenticator decrypts a JWE token, it attempts to parse the inner payload as a SignedJWT. If the inner payload is a PlainJWT (using the `alg: none` algorithm), the resulting SignedJWT object is null, and the code path that performs signature verification is silently skipped due to a logic error. The code then builds a full user profile from the unverified claims, allowing any user to be impersonated including administrators.

The critical element: the only input the attacker needs is the server's RSA public key. This is frequently published in the application's JWKS endpoint (standard OAuth/OIDC behavior) or embedded in the JWT header. A public proof-of-concept and detailed technical writeup are available at codeant.ai. Affected deployments are specifically those using RSA-based JWE together with JwtAuthenticator configured with both EncryptionConfiguration and SignatureConfiguration (both features together). pac4j is embedded in many Java-based frameworks including Apache Shiro and various Spring applications.

**Action:** Upgrade pac4j-jwt to version 4.5.9+, 5.7.9+, or 6.3.3+ immediately. Verify the upgrade applied by testing that PlainJWT (alg=none) tokens are rejected. Rotate any JWT secrets or RSA keys as a precautionary measure.

**References:**
- https://www.pac4j.org/blog/security-advisory-pac4j-jwt-jwtauthenticator.html
- https://www.codeant.ai/security-research/pac4j-jwt-authentication-bypass-public-key
- https://arcticwolf.com/resources/blog/cve-2026-29000/

---

### 7. Anthropic's Claude Opus 4.6 Autonomously Discovers 22 Firefox Vulnerabilities Including CVSS 9.8 JIT Bug CVE-2026-2796
**CVE:** CVE-2026-2796 (primary); 14 high + 7 moderate also patched in Firefox 148
**CVSS:** 9.8 (CVE-2026-2796) | **Threat Score:** 7/10 | **Latency:** Late (11 days) | **First Seen:** 2026-03-07

In a landmark disclosure published March 7 in partnership with Mozilla, Anthropic revealed that Claude Opus 4.6 autonomously identified 22 new security vulnerabilities in the Firefox codebase during a structured two-week engagement in January 2026. The model scanned nearly 6,000 C++ source files and submitted 112 unique vulnerability reports, of which 22 were confirmed (14 high, 7 moderate, 1 low severity). The most severe is CVE-2026-2796 (CVSS 9.8), a just-in-time miscompilation vulnerability in Firefox's JavaScript WebAssembly component — a use-after-free bug that the model detected after just 20 minutes of autonomous exploration of the codebase.

In a second phase, Anthropic tasked Claude with developing practical exploits for the confirmed vulnerabilities, spending approximately $4,000 in API credits across several hundred attempts. The model successfully generated working exploits for two vulnerabilities, including CVE-2026-2796, though only in a sandboxed environment with browser mitigations intentionally stripped. The significance here extends beyond Firefox: this disclosure demonstrates that the cost of AI-driven vulnerability discovery has fallen to four-digit dollar amounts, that LLMs can autonomously navigate large C++ codebases to find memory corruption bugs at a competitive rate relative to traditional fuzzing, and that the gap between discovery and weaponization is narrowing. All 22 issues were patched in Firefox 148. The disclosure also signals incoming risk from adversarial actors adopting the same methodology for products without Anthropic-style safety guardrails.

**Action:** Update Firefox to version 148 or later immediately. Organizations with Firefox pinned to older versions via enterprise policy should deploy 148 as an emergency update.

**References:**
- https://thehackernews.com/2026/03/anthropic-finds-22-firefox.html
- https://www.anthropic.com/news/mozilla-firefox-security
- https://www.mozilla.org/en-US/security/advisories/mfsa2026-13/

---

### 8. Pingora OSS HTTP/1 Request Smuggling — Three CVEs in Cloudflare's Open-Source Proxy (Fixed in 0.8.0)
**CVEs:** CVE-2026-2833, CVE-2026-2835, CVE-2026-2836
**CVSS:** N/A (pending) | **Threat Score:** 6/10 | **Latency:** Late (9 days) | **First Seen:** 2026-03-09

Cloudflare disclosed and patched three HTTP/1 request smuggling vulnerabilities in Pingora OSS — its widely-adopted open-source Rust-based HTTP proxy library — on March 9. The flaws allow an attacker who can send HTTP requests through a Pingora-based ingress proxy to poison the downstream cache, hijack other users' authenticated sessions, or bypass proxy-level security controls by inserting a smuggled request that the backend server processes as a separate, attacker-controlled request. Cloudflare's own production infrastructure uses an internal variant and is NOT affected; only organizations running standalone Pingora OSS as an internet-facing reverse proxy or CDN-edge replacement are at risk. A PoC was provided to Cloudflare during coordinated disclosure but has not been made public. Fixed in Pingora 0.8.0.

Pingora has become increasingly popular as a NGINX and HAProxy alternative since its open-source release, particularly in Rust-first infrastructure environments and among companies running high-throughput proxies at scale. Request smuggling vulnerabilities in edge proxies consistently carry high real-world impact when exploited, enabling cross-user account compromise and WAF/security-layer bypass.

**Action:** Upgrade to Pingora 0.8.0 or later. Review proxy keep-alive configuration. If immediate upgrade is not possible, consider disabling HTTP/1.1 keep-alive connections between the proxy and downstream servers as a temporary mitigation.

**References:**
- https://blog.cloudflare.com/pingora-oss-smuggling-vulnerabilities/

---

### 9. FortiGuard Warning: Elevated Cyber Risk from Iran/Israel Conflict — BadeSaba App Compromised, 149 Hacktivist DDoS Attacks in 48 Hours
**CVE:** N/A | **Threat Score:** 6/10 | **Latency:** On-time | **First Seen:** 2026-03-17 | **Geopolitical Threat Intel**

FortiGuard Labs published an urgent threat intelligence brief noting that while no large-scale, confirmed Iranian state-directed cyber retaliation has emerged following recent U.S.-Israeli kinetic strikes on Iranian targets, the threat landscape is meaningfully elevated. In the first 48 hours post-strike, FortiGuard observed: (1) compromise and defacement of Iranian applications and media properties, most notably the widely-used BadeSaba calendar app — whose push-notification system access implies pre-staged backend compromise achieved before the kinetic escalation; (2) broadcast and media intrusions distributing psychological messaging inside Iran; (3) disruption of Iranian internet connectivity; (4) 149 hacktivist DDoS attacks targeting 110 organizations across 16 countries (per corroborating THN data); (5) elevated Telegram chatter suggesting potential targeting of financial services and critical infrastructure in Jordan, Israel, Afghanistan, and other regional entities.

FortiGuard's key analytical warning: Iranian-linked threat actors have historically adopted a patient posture during geopolitical escalations, preferring to activate pre-staged access weeks or months after a triggering event when defensive attention has shifted. BadeSaba's pre-staged backend access is consistent with this pattern. Tradecraft to watch: wiper malware targeting government and energy sectors, DDoS against financial institutions, spoofed mobile app updates, fake software installers, and credential harvesting themed around conflict news.

**Action:** Organizations in defense, energy, finance, and government sectors — especially those with any perceived link to the conflict — should raise defensive posture immediately. Validate backup integrity, patch all internet-facing assets without delay, disable unnecessary remote access, ensure EDR/NDR alert review capacity is elevated, and train staff on conflict-themed phishing lures.

**References:**
- https://www.fortinet.com/blog/threat-research/cyber-fallout-after-the-strikes-signal-noise-and-what-comes-next
- https://thehackernews.com/2026/03/149-hacktivist-ddos-attacks-hit-110.html

---

## Noted (Watch List)

| # | CVE | Product | Note |
|---|-----|---------|------|
| 1 | CVE-2026-21994 | Oracle Edge Cloud Infrastructure Designer v0.3.0 | CVSS 9.8 unauthenticated network RCE via HTTP; niche product; monitor for PoC |
| 2 | CVE-2026-25937 | GLPI v11.0.0–11.0.5 | MFA bypass with valid credentials; fixed in GLPI 11.0.6; CVSS 6.5 |
| 3 | CVE-2026-22727 | Cloud Foundry CAPI Release ≤v1.226.0 | Unprotected internal endpoints allow droplet replacement; CVSS 7.5 |
| 4 | CVE-2026-27459, CVE-2026-27448 | pyOpenSSL prior to 26.0.0 | Buffer overflow (cookie >256B) and auth bypass on callback exception; fixed in 26.0.0 |
| 5 | N/A | OpenClaw AI — Admin Interface Exposure + ClawHub Supply Chain (Krebs/DVULN) | Hundreds of internet-exposed OpenClaw admin interfaces leaking all credentials; distinct from 2026-03-01 ClawJacked WebSocket finding; no CVE yet |
| 6 | N/A | GTIG AI Threat Tracker Q4 2025 (Google/Mandiant) | DPRK/Iran/PRC/Russia using LLMs for phishing/recon; HONESTCUE malware uses Gemini API for dynamic payload generation; Xanthorox jailbreak service; rising model extraction attacks |

---

## Source Coverage

| Status | Count | Sources |
|--------|-------|---------|
| ✅ OK | 21 | BleepingComputer, TheHackerNews, CISA KEV, Cloudflare blog, GitHub Security Lab, GitHub Advisory DB, SANS ISC, Schneier on Security, Google TI (Mandiant), Unit 42, KrebsOnSecurity, Fortinet blog, Arctic Wolf, SecLists FullDisclosure, OpenCVE, Google Project Zero, HackerOne, Packetstorm, MSRC blog, CVE.org, Exploit-DB |
| ⚠️ Degraded | 9 | SecurityWeek (403), NVD NIST (redirect loop), HackerOne/hacktivity (empty), NCSC alerts (404), Rapid7 blog (404), Exploit-DB (interface only), CISA alerts (404/funding lapse), MSRC blog (sparse), Talos blog (stale—last post Feb 26) |
| ❌ Unreachable | 1 | attackerkb.com (500) |

---

## Dedup Log

Items seen in current cycle but already reported in previous cycles (skipped):

- GlassWorm ForceMemo supply-chain attack → reported 2026-03-17
- Chrome CVE-2026-3909 (Skia) + CVE-2026-3910 (V8) → reported 2026-03-17
- NTLM Reflection CVE-2025-33073 → reported 2026-03-17
- Rocket.Chat CVE-2026-28514 + CVE-2026-30833 → reported 2026-03-17
- Wing FTP CVE-2025-47813 → reported 2026-03-17
- Stryker Wiper attack → reported 2026-03-11 through 2026-03-17 (multiple updates)
- DRILLAPP / Laundry Bear → reported 2026-03-17
- Zammad IDOR/SQLi (GHSL-2026-047/-049) → reported 2026-03-07
- Cisco FMC CVE-2026-20079 → reported 2026-03-08
- n8n CVE-2026-21858 and CVE-2025-68613 → reported 2026-03-07, 2026-03-11, 2026-03-12
- MS Patch Tuesday March 2026 → reported 2026-03-10
- APT28 BEARDSHELL/COVENANT → reported 2026-03-10
- FortiGate credential theft campaign → reported 2026-03-10
- Ivanti EPM CISA KEV → reported 2026-03-10
- HPE Aruba AOS-CX → reported 2026-03-10
- South Korean NTS crypto seed exposure → reported 2026-03-02
- ClawJacked WebSocket hijack → reported 2026-03-01
- APT28 CVE-2026-21513 MSHTML → subsumed under MS Patch Tuesday coverage 2026-03-10
