# Watchtower Night Report — 2026-04-21
**Cycle:** Night | **Generated:** 2026-04-21 08:00 UTC (2026-04-21T08:00:00Z)
**Sources checked:** 21/29 | **CISA KEV total:** N/A (CISA blocked) | **New KEV additions:** N/A

---

## 🟠 HIGH

### 📰 CVE-2026-5760 — SGLang LLM Serving Framework RCE via Malicious GGUF Chat Template (CVSS 9.8)
**Product:** SGLang (open-source LLM serving framework) | **CVE:** CVE-2026-5760 | **Status:** 0-Day (Unpatched)

SGLang's `/v1/rerank` endpoint renders Jinja2 chat templates from GGUF model files using an unsandboxed `jinja2.Environment()`. An attacker who publishes a malicious GGUF model with a crafted `tokenizer.chat_template` field achieves arbitrary Python code execution in the context of the SGLang service when the model is loaded. CERT/CC published VU#915947 on April 20. No vendor patch exists — the recommended fix is switching to `ImmutableSandboxedEnvironment`.

**Timeline:** CERT/CC VU#915947 published April 20, 2026. No vendor response as of disclosure.

**Why it matters:** SGLang is widely deployed in production LLM inference pipelines. Organizations pulling models from Hugging Face or other public repositories are directly exposed. The attack vector mirrors the Marimo/Hugging Face supply chain pattern reported earlier this month — malicious model files as a vector into AI infrastructure.

**Discovered by:** CERT/CC Coordination Center

**Mitigation:**
- Do not load untrusted GGUF model files on SGLang instances
- Audit model sources and verify model integrity before deployment
- Monitor for upstream patch; apply immediately when available
- Consider sandboxing SGLang service containers with restricted network egress

**Sources:** [CERT/CC VU#915947](https://kb.cert.org/vuls/id/915947) | [The Hacker News](https://thehackernews.com) | [PT Security](https://dbugs.ptsecurity.com)

---

### 📰 MCP STDIO Transport Command Injection — OX Security Identifies Systemic RCE Across Major AI Frameworks (10 CVEs)
**Product:** Anthropic MCP SDK (Python, TypeScript, Java, Rust) + LiteLLM, LangChain, LangFlow, Flowise | **CVE:** Multiple (10 CVEs across downstream projects) | **CVSS:** 9.8 | **First reported:** 2026-04-17 (noted), promoted 2026-04-21

OX Security published detailed research demonstrating that Anthropic's MCP STDIO transport converts commands directly into server execution, allowing arbitrary OS command injection. The flaw affects all four official SDK implementations and manifests through four attack vectors: unauthenticated command injection via STDIO, hardening bypass, zero-click prompt injection, and network-based injection through MCP marketplaces. Ten CVEs were identified across downstream projects including LiteLLM, LangChain, LangFlow, Flowise, Bisheng, and DocsGPT. Some vendors have patched; Anthropic characterizes the behavior as "expected" and has declined to modify the protocol architecture.

**Why it matters:** With 7,000+ publicly accessible MCP servers and 150+ million package downloads, this is a systemic supply chain vulnerability affecting the rapidly growing AI agent ecosystem. Any organization deploying MCP-based tools is potentially exposed to command execution through poisoned configurations or prompt injection.

**Discovered by:** OX Security research team

**Mitigation:**
- Audit all MCP server configurations for untrusted command paths
- Update LiteLLM, Bisheng, DocsGPT, and other patched downstream projects immediately
- Restrict MCP STDIO server execution to explicitly allowlisted commands
- Monitor for prompt injection attempts targeting MCP tool invocations
- Do not install MCP servers from unverified marketplace sources

**Sources:** [The Hacker News](https://thehackernews.com/2026/04/anthropic-mcp-design-vulnerability.html) | [SecurityWeek](https://www.securityweek.com)

---

### 🔄 Vercel Breach Update — ShinyHunters Claims Data Sale, Unencrypted Environment Variables Confirmed (Score 7→8)
**Product:** Vercel (cloud development platform) | **CVE:** Not yet assigned | **CVSS:** N/A | **First reported:** 2026-04-20

Material update to the Vercel breach reported yesterday. BleepingComputer confirms: the breach originated from a compromised Context.ai tool's Google Workspace OAuth application used by a Vercel employee. Attackers escalated access to internal systems and exfiltrated customer environment variables that were stored unencrypted. ShinyHunters has claimed responsibility and posted data for sale, with a reported $2M ransom demand. Vercel CEO Guillermo Rauch confirmed that non-sensitive environment variables lacked encryption. 580 employee records reportedly exposed. BleepingComputer has not independently verified the authenticity of the claimed stolen data.

**Mitigation:**
- Rotate all API keys, tokens, and secrets stored as Vercel environment variables immediately
- Audit OAuth application permissions connected to development platforms
- Monitor for unauthorized access using any credentials previously stored in Vercel
- Enable encryption at rest for all environment variable stores

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/vercel-confirms-breach-as-hackers-claim-to-be-selling-stolen-data/) | [The Hacker News](https://thehackernews.com)

---

## 🟡 MEDIUM

### 📰 CVE-2025-7444 — LoginPress Pro WordPress Authentication Bypass (CVSS 9.8)
**Product:** LoginPress Pro (WordPress plugin) | **CVE:** CVE-2025-7444 | **Published:** 2026-04-21

Critical authentication bypass in the LoginPress Pro WordPress plugin allows unauthenticated attackers to log in as any existing user, including administrators. The vulnerability was disclosed via OpenCVE/NVD on April 21 with a CVSS 9.8 rating. LoginPress customizes WordPress login pages and is deployed across many WordPress installations.

**Mitigation:** Update LoginPress Pro to the latest patched version immediately. Audit WordPress admin accounts for unauthorized access.

**Sources:** [OpenCVE](https://app.opencve.io)

---

### 📰 CVE-2026-0740 — Ninja Forms WordPress Unauthenticated Arbitrary File Upload (PoC Public)
**Product:** Ninja Forms WordPress Plugin (versions ≤ 3.3.26) | **CVE:** CVE-2026-0740 | **Published:** 2026-04-20

Unauthenticated arbitrary file upload vulnerability in the Ninja Forms WordPress plugin (versions 3.3.26 and earlier). A public proof-of-concept exploit repository on GitHub has accumulated 17 stars, indicating growing awareness and potential exploitation. Ninja Forms is one of the most popular WordPress form builders with millions of installations.

**Mitigation:** Update Ninja Forms to version 3.3.27 or later. Audit web server upload directories for suspicious files. Implement WAF rules blocking file upload exploitation patterns.

**Sources:** [GitHub PoC](https://github.com/search?q=CVE-2026-0740) | [0xMarcio/cve](https://github.com/0xMarcio/cve)

---

### 📰 CVE-2026-32135 — NanoMQ MQTT Broker Remote Heap Buffer Overflow (CVSS 8.7)
**Product:** NanoMQ MQTT Broker (before v0.24.11) | **CVE:** CVE-2026-32135 | **Published:** 2026-04-20

Off-by-one memory allocation error in NanoMQ's REST API query parameter parsing enables remote heap buffer overflow via crafted HTTP requests without authentication. NanoMQ is an MQTT message broker used in IoT and edge computing deployments. While MQTT brokers are not typically directly internet-facing, misconfigured deployments with exposed REST APIs are at risk.

**Mitigation:** Update NanoMQ to v0.24.11 or later. Ensure REST API endpoints are not exposed to untrusted networks. Apply network segmentation for MQTT infrastructure.

**Sources:** [PT Security](https://dbugs.ptsecurity.com)

---

## 📋 Noted / Monitoring

**CVE-2026-39861 — Claude Code sandbox escape** — Symlink creation from sandboxed processes allows writes to arbitrary locations outside workspace (CVSS 7.7). Patched in Claude Code v2.1.64. Low risk for updated installations.

**CVE-2026-40497 — FreeScout CSS injection** — Mailbox signature field fails to strip style tags, enabling CSS attribute selectors to exfiltrate CSRF tokens and escalate agent-to-admin privileges (CVSS 8.1). Fixed in v1.8.213. Niche help desk platform limits blast radius.

**CVE-2025-7696, CVE-2025-7697 — WordPress CF7 Integration PHP Object Injection** — Integration plugins for Pipedrive and Google Sheets with Contact Form 7 vulnerable to PHP Object Injection (CVSS 9.8) potentially leading to RCE. Limited deployment of these specific integrations.

**CVE-2026-39377, CVE-2026-39378 — Jupyter nbconvert path traversal** — Unsanitized filenames in attachment and image references enable arbitrary file reads/writes outside intended directories (CVSS 6.5). Fixed in nbconvert v7.17.1.

**CVE-2026-28684 — python-dotenv symlink exploitation** — Symlink following during .env file rewriting enables local file overwrite (CVSS 6.6). Fixed in v1.2.2. Local-only vector limits immediate risk.

**Serial-to-IP converter flaws (Lantronix/Silex)** — Forescout researchers identified 20 new vulnerabilities in serial-to-IP converter devices used in OT and healthcare environments. Theoretical attack scenarios documented; no active exploitation. Monitoring for PoC or exploitation reports.

**Apple account notification phishing** — Threat actors inject phishing messages into Apple ID name fields to trigger legitimate account change notifications that pass SPF/DKIM/DMARC. Social engineering technique, not a software vulnerability. Active in the wild.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | BleepingComputer, The Hacker News, SecurityWeek, Krebs on Security, Schneier | ✅ |
| CISA / US Gov | CISA.gov, CISA KEV | ❌ (403 Forbidden) |
| Vendor advisories | Rapid7, Fortinet, Microsoft MSRC, Cloudflare Blog | ✅ / ⚠️ |
| Research / OSINT | CERT/CC, GitHub Security Lab, Google Project Zero, Full Disclosure | ✅ |
| CVE databases | OpenCVE, NVD, PT Security dbugs | ✅ / ⚠️ |
| Supply chain | GitHub CVE search, 0xMarcio/cve | ✅ |
| Threat intel | avleonov, Habr/T.Hunter, CyberOK, CERT-UA | ✅ / ⚠️ |

**Errors:** cisa.gov (403), cisa.gov/kev (403), attackerkb.com (403), hackerone.com/hacktivity (JS required), cve.org (JS required), bugcrowd.com/disclosures (404), cve.mitre.org (redirects to cve.org/JS), cert.gov.ua (empty content). Degraded: packetstorm.news (ToS only), nvd.nist.gov (navigation only), msrc.microsoft.com (empty after redirect).
**CISA KEV:** Unable to check directly (403); no new KEV additions detected via secondary sources this cycle.

---

*Watchtower vulnerability-researcher | Cycle: 2026-04-21/night | Next: 2026-04-22/night*
