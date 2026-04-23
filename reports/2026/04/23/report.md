# Watchtower Night Report — 2026-04-23
**Cycle:** Night | **Generated:** 2026-04-23 06:00 UTC (2026-04-23T06:00:00Z)
**Sources checked:** 24/31 | **CISA KEV total:** N/A (403) | **New KEV additions:** N/A

---

## 🟠 HIGH

### CanisterSprawl — Self-Propagating npm Supply Chain Worm Steals Developer Tokens
**Product:** npm ecosystem (multiple packages) | **CVE:** Not yet assigned | **CVSS:** N/A | **First reported:** 2026-04-21

A self-replicating worm discovered by Socket and StepSecurity is spreading through the npm registry by stealing developer publish tokens via postinstall hooks, then injecting itself into every package the compromised token can publish. At least 16 packages from Namastex Labs are confirmed compromised, including @automagik/genie, pgserve, and @fairwords packages. The malware exfiltrates API keys, SSH keys, CI/CD credentials, cloud tokens, Kubernetes configs, browser data, and cryptocurrency wallets through ICP (Internet Computer Protocol) canisters for takedown resilience. First malicious version published April 21 at 22:14 UTC. Techniques resemble TeamPCP but attribution is unconfirmed.

**Discovery:** Socket and StepSecurity researchers. Cross-referenced npm publish timestamps with token exfiltration infrastructure on ICP.

**Mitigation:**
- Audit npm token scopes and rotate all publish tokens immediately
- Check for unexpected postinstall hooks in dependencies: `npm query ':attr(scripts, [postinstall])'`
- Pin package versions and enable npm provenance verification
- Review CI/CD pipeline credentials for exposure

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/new-npm-supply-chain-attack-self-spreads-to-steal-auth-tokens/) | [The Hacker News](https://thehackernews.com)

---

### CVE-2026-40372 — Microsoft ASP.NET Core Emergency Privilege Escalation (CVSS 9.1)
**Product:** Microsoft ASP.NET Core (Microsoft.AspNetCore.DataProtection 10.0.6) | **CVE:** CVE-2026-40372 | **CVSS:** 9.1 | **First reported:** 2026-04-22

Microsoft released an out-of-band emergency patch for a critical cryptographic signature verification flaw in ASP.NET Core's Data Protection component. Improper signature verification allows remote attackers to gain SYSTEM privileges, enabling file disclosure and data modification. The vulnerability affects applications using the specific DataProtection NuGet package version 10.0.6.

**Timeline:** Out-of-band patch released April 22, 2026 — outside normal Patch Tuesday cycle, indicating severity.

**Why it matters:** ASP.NET Core is ubiquitous in enterprise web applications. An out-of-band patch for a CVSS 9.1 privilege escalation to SYSTEM demands immediate attention for any .NET web stack.

**Mitigation:**
- Update Microsoft.AspNetCore.DataProtection NuGet package immediately
- Apply .NET runtime update from Microsoft Security Advisory
- Audit applications using Data Protection APIs for exposure

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com) | [The Hacker News](https://thehackernews.com)

---

### Malicious KICS Docker Images — Checkmarx Supply Chain Compromise
**Product:** Checkmarx KICS (Infrastructure-as-Code Scanner) | **CVE:** Not yet assigned | **CVSS:** N/A | **First reported:** 2026-04-22

Docker Hub repository for Checkmarx KICS was compromised with modified binaries containing data exfiltration capabilities. Poisoned tags include v2.1.20, alpine, and v2.1.21. The modified scanner generates normal-looking scan reports but encrypts and exfiltrates them to an external endpoint, exposing credentials found in scanned infrastructure-as-code files (Terraform, CloudFormation, Kubernetes manifests). This is a supply chain attack against security tooling itself — organizations running KICS in CI/CD pipelines are at highest risk.

**Mitigation:**
- Verify KICS Docker image digests against Checkmarx's official hashes
- Audit CI/CD pipelines that pull KICS images for unexpected tags
- Rotate any credentials present in scanned IaC files
- Pin Docker images by digest, not tag

**Sources:** [The Hacker News](https://thehackernews.com)

---

### CVE-2026-3844 — Breeze WordPress Cache Plugin Unauthenticated RCE (CVSS 9.8)
**Product:** Cloudways Breeze Cache Plugin (WordPress) | **CVE:** CVE-2026-3844 | **CVSS:** 9.8 | **First reported:** 2026-04-22

Unrestricted file upload vulnerability in the Gravatar caching feature of the Breeze cache plugin allows unauthenticated remote code execution when the Gravatar cache feature is enabled. Breeze is the default caching plugin for Cloudways-hosted WordPress installations, giving it significant deployment reach.

**Mitigation:**
- Update Breeze plugin immediately
- Disable Gravatar caching feature until patched
- Audit web shells in cache directories

**Sources:** [PT Security dbugs](https://dbugs.ptsecurity.com)

---

## 🟡 MEDIUM

### BRIDGE:BREAK — 22 Vulnerabilities in Lantronix and Silex Serial-to-IP Converters
**Product:** Lantronix EDS3000PS, Silex serial-to-Ethernet converters | **CVE:** Multiple (BRIDGE:BREAK family) | **Published:** 2026-04-21

Forescout researchers disclosed 22 vulnerabilities in legacy serial-to-IP device converters that bridge serial protocols to TCP/IP networks. Some flaws allow full device hijacking and data tampering in mission-critical industrial control systems. Approximately 20,000 converters are internet-exposed globally. These devices connect legacy serial equipment (medical devices, industrial controllers, POS terminals) to IP networks.

**Mitigation:** Segment serial-to-IP converters from the internet, apply vendor patches where available, monitor for unauthorized access to management interfaces.

**Sources:** [The Hacker News](https://thehackernews.com)

---

### CVE-2025-29635 — D-Link DIR-823X Mirai Botnet Exploitation
**Product:** D-Link DIR-823X routers (firmware 240126, 24082) | **CVE:** CVE-2025-29635 | **Published:** 2026-04-22

Active Mirai-based campaign exploiting a command injection flaw via the `/goform/set_prohibiting` endpoint on end-of-life D-Link routers. Discovered by Akamai SIRT in March 2026, the flaw was originally disclosed 13 months earlier by researchers Wang Jinshuai and Zhao Jiangting. The "tuxnokill" Mirai variant supports TCP SYN/ACK/STOMP, UDP floods, and HTTP null attacks. D-Link will not patch — these routers reached EOL November 2024.

**Mitigation:** Replace affected routers with supported models, disable remote administration, monitor for unusual outbound traffic.

**Sources:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/new-mirai-campaign-exploits-rce-flaw-in-eol-d-link-routers/)

---

## 📋 Noted / Monitoring

**Kyber Ransomware** — New ransomware operation using Kyber1024 post-quantum key encapsulation on Windows (Rust) and ChaCha8/RSA-4096 on ESXi. Compromised a US defense contractor. First post-quantum ransomware in the wild; monitoring for wider deployment.

**CVE-2026-41229, CVE-2026-41231, CVE-2026-41228, CVE-2026-41230 — Froxlor Server Admin** — Four critical flaws (CVSS 9.1–9.9) including PHP code injection and symlink attacks. Niche deployment limits immediate impact.

**CVE-2026-41679 — Paperclip AI Server** — Unauthenticated RCE (CVSS 10.0) and privilege escalation in AI platform. Low deployment footprint.

**VU#518910 — Ollama GGUF** — Remote memory leak in Ollama's GGUF quantization handling. Could expose model data or host memory.

**GoGra Linux Backdoor (Harvester APT)** — Linux variant using Microsoft Graph API/Outlook for C2, targeting South Asia. Sophisticated espionage but no vulnerability disclosure.

**CVE-2026-34415 — Xerte Online Toolkits** — Unauthenticated RCE (CVSS 9.8) via .php4 extension bypass in elFinder. Education sector deployment.

**CVE-2026-41196 — Luanti (Minetest fork)** — Lua sandbox escape enabling filesystem access (CVSS 9.0). Niche gaming platform.

**Lotus Wiper** — Novel data destruction malware targeting Venezuelan energy sector. Regional scope, not internet-facing vulnerability.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | BleepingComputer, The Hacker News, SecurityWeek, Krebs, Schneier | ✅ |
| CISA / US Gov | CISA KEV, CISA.gov | ❌ (403) |
| Vendor advisories | Rapid7, Fortinet, Cloudflare Blog, MSRC | ✅ / ⚠️ |
| Research / OSINT | GitHub CVE search, SecurityLab, Project Zero, KB CERT, Avleonov | ✅ |
| Exploit DBs | PacketStorm, SecLists, 0xMarcio/cve, dbugs.ptsecurity.com | ✅ / ⚠️ |
| NVD / CVE | NVD, CVE.org, OpenCVE, CVE MITRE | ⚠️ / ❌ |
| Regional / Niche | CERT-UA, Habr/TomHunter, CyberOK, HackerOne, Bugcrowd | ✅ / ❌ |

**Errors:**
- cisa.gov, cisa.gov/kev: 403 Forbidden (persistent)
- attackerkb.com: 403 Forbidden (persistent)
- bugcrowd.com/disclosures: 404 Not Found (persistent)
- hackerone.com/hacktivity: Requires JavaScript
- cve.org, cve.mitre.org: Require JavaScript / redirect loop
- packetstormsecurity.com: Redirect to packetstorm.news, returned ToS page
- opencve.io: Marketing page only, no vulnerability data
- nvd.nist.gov: Navigation shell only
- msrc.microsoft.com/blog: Empty after redirect
- cert.gov.ua: Empty content returned

**CISA KEV:** Unavailable (403). KEV additions covered via secondary sources (BleepingComputer, SecurityWeek).

---

*Watchtower vulnerability-researcher | Cycle: 2026-04-23/night | Next: 2026-04-24/night*
