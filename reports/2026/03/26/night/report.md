# Watchtower — Night Cycle Report
**Date:** 2026-03-26 | **Cycle:** Night | **Analyst:** vulnerability-researcher

---

## Summary

7 findings (5 new, 2 updates), 4 noted items. BIND 9 quad-CVE patch day and Node.js security releases are the major infrastructure alerts. TeamPCP supply-chain campaign now confirmed as 4+ distinct attack vectors (Trivy → KICS GitHub Action → Kubernetes cluster wiper → LiteLLM PyPI). Apple released iOS/macOS 26.4 with 30+ fixes. PolyShell Magento attacks now hitting >56% of vulnerable stores. CISA added Langflow RCE to KEV.

---

## Findings

### [NEW] TeamPCP Trojanizes LiteLLM on PyPI — Persistent .pth Backdoor in 36% of Cloud Envs
**Threat Score:** 10/10 | **CVE:** N/A | **Source:** wiz.io, oss-security

TeamPCP published malicious LiteLLM versions 1.82.7 and 1.82.8 to PyPI on March 24, 2026 at ~08:30 UTC. The packages were quarantined at 11:25 UTC after discovery by Wiz and disclosure to PyPI. Two payload delivery mechanisms were used:
- **1.82.7:** Drops double-base64 payload to disk, executes on `litellm --proxy` invocation
- **1.82.8:** Installs a `litellm_init.pth` file that triggers on *every* Python invocation — persistent execution across any Python process, not just LiteLLM imports

The payload collects: environment variables (API keys, tokens), SSH keys, cloud credentials (AWS/GCP/Azure), Kubernetes configs, CI/CD secrets, Docker configs, database credentials, and cryptocurrency wallets. Data is encrypted with AES-256, key encrypted with embedded RSA public key, exfiltrated to `checkmarx[.]zone` (1.82.7) and `models[.]litellm[.]cloud` (1.82.8).

LiteLLM is present in **36% of cloud environments**. Root cause: exposed PyPI API token from the prior Trivy compromise. 

TeamPCP confirmed attack chain: Aqua Trivy (PoC'd March 22) → Checkmarx KICS GitHub Action → Kubernetes cluster wiper (March 24 morning) → **LiteLLM PyPI backdoor** (March 24 afternoon).

**Mitigation:** Ensure LiteLLM is pinned to 1.82.9+ (clean version). Audit environments for `litellm_init.pth` presence. Rotate any credentials loaded by Python processes that used affected versions. LiteLLM security update at: `https://docs.litellm.ai/blog/security-update-march-2026`.

---

### [NEW] PolyShell Magento Mass Exploitation — 56.7% of Vulnerable Stores Attacked
**Threat Score:** 9/10 | **CVE:** N/A (PolyShell chain) | **Source:** bleepingcomputer.com

Active PolyShell exploitation is now affecting 56.7% of vulnerable Magento/Adobe Commerce instances. Attacks began March 19 with rapid escalation. A novel **WebRTC payment skimmer** variant has been discovered that exfiltrates payment card data via WebRTC data channels, making it harder to detect with conventional network monitoring. No official patch is available for stable Magento releases at time of writing. 

**Mitigation:** Immediately review Magento admin panels for unauthorized plugins/patches. Apply Content Security Policy headers blocking unexpected WebRTC connections. Segment payment forms behind WAF rules targeting the PolyShell exploit chain.

---

### [NEW] CVE-2026-33017 (Langflow RCE) Added to CISA KEV
**Threat Score:** 9/10 | **CVE:** CVE-2026-33017 | **CVSS:** 9.8 | **Source:** cisa.gov

CISA added CVE-2026-33017 (Langflow pre-authentication RCE) to the Known Exploited Vulnerabilities catalog on March 25, 2026, setting a mandatory federal remediation deadline. Previously reported as actively exploited. Federal agencies and contractors with exposed Langflow instances must now patch or disconnect. Patches are available — there is no valid reason to remain on a vulnerable version.

---

### [NEW] TP-Link Archer NX Critical Auth Bypass — Unauthenticated Firmware Upload
**Threat Score:** 8/10 | **CVE:** CVE-2025-15517, CVE-2025-15605, CVE-2025-15518, CVE-2025-15519 | **CVSS:** ~9.4 | **Source:** bleepingcomputer.com

TP-Link has disclosed a critical authentication bypass (CVE-2025-15517) in the Archer NX series routers enabling unauthenticated firmware upload and full device compromise. The advisory also includes:
- CVE-2025-15605: Hardcoded cryptographic key in firmware
- CVE-2025-15518, CVE-2025-15519: Command injection (post-auth, but chain-able with the bypass)

No public PoC or active exploitation reported yet. However, TP-Link routers are an extremely high-value mass-exploitation target given their ubiquitous deployment in home/SOHO environments and ISP supply chains.

**Mitigation:** Apply vendor firmware update immediately. Disable remote management interface if not needed. TP-Link advisory at tp-link.com/security.

---

### [NEW] BIND 9 Quad-CVE Patch Day — Remote DoS on DNS Resolvers
**Threat Score:** 8/10 | **CVE:** CVE-2026-1519, CVE-2026-3104, CVE-2026-3119, CVE-2026-3591 | **CVSS:** 7.5 | **Source:** openwall.com (oss-security), kb.isc.org

ISC publicly disclosed four BIND 9 vulnerabilities on March 25, 2026 (all were early-notified March 18):

- **CVE-2026-1519** (High, CVSS 7.5): Excessive NSEC3 iterations cause high CPU load in resolvers processing maliciously crafted zones — effective DoS. Affects BIND 9.11.0–9.21.x.
- **CVE-2026-3104** (High, CVSS 7.5): Memory leak during DNSSEC proof preparation via specially crafted domain query — causes unbounded RSS growth leading to OOM and named shutdown. Affects BIND 9.20.x–9.21.x.
- **CVE-2026-3119**: Details pending full ISC advisory; confirmed High severity.
- **CVE-2026-3591**: Details pending full ISC advisory; confirmed High severity.

All four are remotely exploitable with no authentication required on DNS resolvers. Authoritative-only servers are generally unaffected *unless* they make recursive queries.

**Patches:** BIND 9.18.47, 9.20.21, 9.21.20 (and S1 preview editions).

**Mitigation:** Update BIND immediately. If running 9.18.x, upgrade to 9.18.47. Note that disabling DNSSEC validation (as a workaround for CVE-2026-1519) is NOT recommended.

---

### [NEW] Node.js Multiple High-Severity CVEs — HTTP Server Crash, TLS DoS
**Threat Score:** 7/10 | **CVE:** CVE-2026-21637, CVE-2026-21710, CVE-2026-21711, CVE-2026-21712 | **Source:** openwall.com (oss-security), nodejs.org

Node.js patched 1 High, 5 Medium, 2 Low severity issues in a security release on March 24-25, 2026 affecting all supported lines (20.x, 22.x, 24.x, 25.x):

- **CVE-2026-21637** (High): TLS SNICallback exception bypasses all error handlers → uncaught exception crashes Node.js process. Incomplete fix for prior CVE-2026-21637 iteration. All TLS servers using SNICallback are affected.
- **CVE-2026-21710** (High): `__proto__` header in HTTP requests triggers uncatchable TypeError in `req.headersDistinct` accessor → process crash. Cannot be handled without wrapping every access in try/catch. Affects all HTTP servers on 20.x, 22.x, 24.x, 25.x.
- **CVE-2026-21711** (Medium): Unix Domain Socket server creation bypasses `--allow-net` permission model enforcement.
- **CVE-2026-21712** (Medium): Malformed IDN in url.format() triggers assertion failure, crashes process. Affects 24.x, 25.x.

**Mitigation:** Update Node.js to the latest security release for your line (see nodejs.org/en/blog/vulnerability/march-2026-security-releases). All HTTP servers are affected by CVE-2026-21710 and should be patched urgently.

---

### [NEW] Apple iOS/macOS 26.4 — 30+ CVEs Including WiFi MITM and WebKit UAF
**Threat Score:** 7/10 | **CVE:** CVE-2026-28865, CVE-2026-28879 (notable) | **Source:** isc.sans.edu, support.apple.com

Apple released iOS 26.4, iPadOS 26.4, macOS Tahoe 26.4, tvOS 26.4, watchOS 26.4 on **March 24, 2026** with patches for 30+ CVEs. Notable:

- **CVE-2026-28865**: Authentication issue in WiFi — attacker in privileged network position can intercept network traffic. Reported by Héloïse Gollier and Mathy Vanhoef (KU Leuven — the KRACK/Dragonblood researchers). This is a wireless protocol vulnerability.
- **CVE-2026-28879**: Use-after-free in WebKit — processing maliciously crafted web content leads to process crash. Reported by Justin Cohen of Google.
- **CVE-2026-28895**: Stolen Device Protection bypass — attacker with physical access can access biometrics-gated apps via passcode only.
- **CVE-2026-28866**: Symlink traversal for app → user data access.
- Also includes curl CVE-2025-14524 (connection leakage).

No in-the-wild exploitation reported. iOS 18.7.7 also released for older devices (iPhone XS/XR, iPad 7th gen).

**Mitigation:** Update all Apple devices immediately. Particularly prioritize CVE-2026-28865 for environments with high-sensitivity WiFi networks.

---

## Noted

### CVE-2026-33526, CVE-2026-32748, CVE-2026-33515 — Squid Cache ICP DoS Trio
Three DoS advisories (SQUID-2026:1, :2, :3) disclosed on March 25. Squid ICP (Internet Cache Protocol) request handling vulnerabilities — denial of service via malformed ICP packets. No auth required. Affects Squid installations using ICP (common in CDN/caching proxy deployments). Patches released.

### CVE-2026-31788 — Xen Linux privcmd Kernel Lockdown Bypass
Xen Security Advisory 482 (March 24): Linux privcmd driver allows Xen guests to circumvent kernel lockdown protections. Relevant to Xen hypervisor environments (virtualization infrastructure). Patch available.

### CVE-2026-33150, CVE-2026-33179 — libfuse io_uring Memory Safety
Two memory-safety issues in libfuse's io_uring interface disclosed via oss-security March 25: use-after-free (CVE-2026-33150) and NULL dereference (CVE-2026-33179). Affects Linux systems using FUSE file systems via io_uring. Patch available.

### CVE-2026-3608 — ISC Kea DHCP Server
ISC disclosed CVE-2026-3608 in Kea DHCP server on March 25. Limited technical details available; severity and exploitation path being assessed. Organizations running ISC Kea should apply the available patch proactively.

---

## Source Coverage

- **Total sources:** 31
- **Checked:** 30
- **With findings:** 9 (bleepingcomputer, thehackernews, cisa.gov/kev, securityweek, wiz.io, openwall.com, isc.sans.edu, 0xMarcio/cve, krebsonsecurity)
- **Unreachable (1):** darkreading.com (HTTP 403)
- **Degraded (7):** nvd.nist.gov (redirect/empty), msrc.microsoft.com/blog (no content), cve.mitre.org (redirect), packetstormsecurity.com (TOS redirect), crowdstrike.com (only 2021-22 archive posts), unit42.paloaltonetworks.com (2014 redirect), cert.gov.ua (blank response)
