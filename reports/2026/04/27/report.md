# Watchtower Night Report — 2026-04-27
**Cycle:** Night | **Generated:** 2026-04-27 03:30 UTC (2026-04-27T03:30:00Z)
**Sources checked:** 23/30 | **CISA KEV new additions:** 0 (no additions since 2026-04-24)

---

## 🟠 HIGH

### CVE-2026-34159 — llama.cpp RPC Server Unauthenticated 0-Click RCE (CVSS 9.8)
**Product:** ggml-org/llama.cpp RPC backend (`rpc-server`) — versions prior to b8492 | **CVE:** CVE-2026-34159 | **CVSS:** 9.8 | **First reported:** 2026-04-01 (publicly weaponised PoC circulated 2026-04-26)

The `deserialize_tensor()` function in llama.cpp's RPC backend skips all bounds validation when a tensor's `buffer` field is 0. An unauthenticated attacker with TCP access to the RPC port can craft a `GRAPH_COMPUTE` message that yields arbitrary process-memory read/write; chaining with pointer leaks from `ALLOC_BUFFER` and `BUFFER_GET_BASE` defeats ASLR and lands remote code execution as the inference-server user. The flaw was assigned and disclosed on 2026-04-01 (patched in b8492) but a working "0-click RCE" PoC against version b8487 has now been published on GitHub and X, and is being indexed under the CVE-2026 PoC trackers Watchtower monitors. We missed it on initial publication — flagging late.

**Timeline:** Vendor patch shipped in b8492 → CVE-2026-34159 published 2026-04-01 → public 0-click PoC referenced on social media and aggregator GitHub repos 2026-04-25/26 → no in-the-wild exploitation publicly reported yet.

**Why it matters:** Self-hosted `llama.cpp rpc-server` is the open-source pattern of choice for sharing GPU/CPU inference across machines, and the documented start-up flag binds it to `0.0.0.0` by default. Anyone running an internal LLM cluster on this stack — research, RAG agents, on-prem coding assistants — has an unauthenticated remote-memory primitive sitting one IP allow-list mistake from the internet, with PoC now in the wild. This is exactly the AI-platform / inference-infrastructure surface our scope explicitly covers.

**Discovered by:** Patrick Peng (retr0reg). Public PoC: `pwntricks.com` writeup + GitHub aggregators.

**Mitigation:**
- Upgrade `llama.cpp` to **b8492 or later** on every host running `rpc-server`. Builds older than that are exploitable as-is.
- Confirm the RPC port is bound only to a management interface or localhost; remove any public-internet exposure immediately. The default invocation listens on `0.0.0.0`.
- Place the inference cluster behind a network ACL or wireguard mesh; treat `rpc-server` as untrusted-input-handling code that should never face arbitrary clients.
- Hunt: review any `llama.cpp` host for unexpected child processes spawned by the RPC server, or anomalous outbound TCP from inference nodes.
- Where upgrade is delayed, drop traffic to the RPC port from anything but vetted inference clients.

**Sources:** [NVD — CVE-2026-34159](https://nvd.nist.gov/vuln/detail/CVE-2026-34159) | [TheHackerWire — llama.cpp Critical RCE via RPC Deserialization Bypass](https://www.thehackerwire.com/llama-cpp-critical-rce-via-rpc-deserialization-bypass/) | [Tenable — CVE-2026-34159](https://www.tenable.com/cve/CVE-2026-34159) | [GitHub — 0xMarcio/cve (PoC tracker entry)](https://github.com/0xMarcio/cve)

---

### CVE-2026-6951 — simple-git Unauthenticated RCE via `--config` Bypass (CVSS 9.8)
**Product:** `simple-git` npm package (versions < 3.36.0) | **CVE:** CVE-2026-6951 | **CVSS:** 9.8 | **First reported:** 2026-04-25

The `simple-git` Node.js library, an extremely common Git wrapper used inside CI/CD pipelines, build tools, and developer SDKs, ships an incomplete fix for the older CVE-2022-25912 option-injection RCE. The original patch blocked `-c` but missed the equivalent long form `--config`. An attacker who can reach the `options` argument of `simple-git` calls — typically via an untrusted repository URL or a controllable parameter in a build pipeline — can set `protocol.ext.allow=always` and pass an `ext::` clone source to execute arbitrary commands on the runner with no authentication. Public advisory and fixed release (3.36.0) landed on 2026-04-25.

**Mitigation:**
- Upgrade `simple-git` to **>= 3.36.0** across all repos and pinned-dependency build images. Re-bake CI/CD container layers — old versions get cached for months.
- Review every call site in your codebase: any path where untrusted input (issue body, package metadata, HTTP query, etc.) reaches the `options`, `clone`, `fetch`, or generic exec methods.
- For multi-tenant CI runners, treat this as an active sanitiser-bypass: assume a malicious PR could already have triggered RCE on shared runners.
- Audit `package-lock.json` / `pnpm-lock.yaml` for transitive `simple-git` pins — the package is heavily used as a sub-dependency of build-time tooling.

**Sources:** [Vulnerability-Lookup — CVE-2026-6951](https://vulnerability.circl.lu/vuln/cve-2026-6951) | [TheHackerWire — simple-git Critical RCE: Incomplete Fix Allows Code Execution](https://www.thehackerwire.com/simple-git-critical-rce-incomplete-fix-allows-code-execution/) | [OffSeq — CVE-2026-6951](https://radar.offseq.com/threat/cve-2026-6951-remote-code-execution-rce-in-simple--178a7d4e)

---

## 📋 Noted / Monitoring

**Itron breach disclosure (SEC 8-K, 2026-04-26)** — US smart-utility metering vendor disclosed that an unauthorised third party accessed "certain internal systems" in March 2026, blocked by 2026-04-13. No data-theft confirmation, no attribution, no follow-up activity, no customer-system impact claimed. Filing is deliberately thin; treat as an OT/ICS supply-chain signal worth tracking but not currently actionable.

**VU#748485 / CVE-2026-5756 — DRC INSIGHT Central Office Services unauth config modification (CERT/CC, 2026-04-23)** — Education-sector test-proctoring platform exposes `/v0/configuration` admin endpoint without authentication or origin checks; on-network attacker can change server config, redirect content, or harvest data. Niche to K-12 districts so out of our day-to-day surface, but flagging because the COS pattern (admin + content APIs sharing one router with no separation) recurs in other SaaS appliances we do run. Watch for vendor patch.

**CVE-2026-7037 — Totolink A8000RU OS command injection (CVSS 10.0, dbugs.ptsecurity, 2026-04-25)** — Critical pre-auth RCE in a consumer/SOHO router; researcher batch alongside multiple Tenda F456/Fh1202 buffer overflows (CVE-2026-7019 → 7036, mostly CVSS 9.0). Consumer hardware, no enterprise deployment expected, but volumes are large and Mirai operators routinely weaponise this class within days — relevant for ISP edge teams.

**CVE-2026-42255 — Technitium DNS Server (PT-2026-35197, CVSS 7.2)** — High-severity flaw in the open-source DNS server software disclosed 2026-04-25. Limited public detail so far; remote impact appears denial-of-service rather than RCE. Worth tracking if you run Technitium as a public-facing resolver.

**CVE-2026-30368 — Lightspeed Classroom client-side authorisation bypass (PoC published, 2026-04-26)** — Education-sector classroom-management product allows unauth attackers to forge client-generated authorisation tokens and impersonate users / control student devices. Out of our enterprise-perimeter scope, but PoC is now public.

**Tropic Trooper / Earth Centaur abuses trojanised SumatraPDF + GitHub for AdaptixC2 (Zscaler, 2026-04-24)** — APAC-focused (Taiwan, South Korea, Japan, Hong Kong) Chinese-speaker espionage cluster delivers a custom AdaptixC2 Beacon listener via military-themed lure ZIPs, then pivots to VS Code tunnels for stealthy remote access. Geographically narrow, but the "trojanised SumatraPDF + GitHub C2 + VS Code tunnels" tradecraft is portable — keep on the OSINT shelf.

**Pre-Stuxnet 'fast16' Lua sabotage malware (Kaspersky, 2026-04-25)** — Researchers documented Lua-based sabotage tooling from ~2005 designed to corrupt centrifuge calculations, predating Stuxnet. Historical / strategic-context piece, not a current threat. Useful background for ICS-defender briefings.

**Pack2TheRoot follow-up coverage (CVE-2026-41651)** — Bleeping/SecurityWeek continuing to publish on the Linux PackageKit local-priv-esc; we covered this previously and it remains LPE-only (out of scope for our remote-component criteria).

**MCP-server CVE batch (CVE-2026-7061 chatgpt-mcp-server, CVE-2026-7062 Intina47 context-sync, CVE-2026-7064 AgentDeskAI browser-tools-mcp)** — Three more MCP-server packages disclosed with classic OS command injection (CVSS 7.3 each) on 2026-04-25/26. Pattern continues from the Anthropic MCP SDK / OX Security / Endor Labs analyses already covered: user-controlled tool input reaching `child_process.exec` with no sanitisation. Individually low-impact, but worth watching for any of these MCP servers running in our agent stack.

---

## Source Coverage

| Category | Sources | Status |
|----------|---------|--------|
| Primary news | bleepingcomputer.com, thehackernews.com, securityweek.com, krebsonsecurity.com, schneier.com | ✅ |
| CISA / US Gov | cisa.gov, cisa.gov/known-exploited-vulnerabilities-catalog | ❌ (403 — used THN/BC for KEV mirror) |
| Vendor advisories | msrc.microsoft.com/blog, fortinet.com/blog/threat-research | ⚠️ (no recent posts) |
| Research / OSINT | securitylab.github.com, seclists.org/fulldisclosure, kb.cert.org/vuls, avleonov.com, projectzero.google | ✅ / ⚠️ |
| CVE databases | app.opencve.io, dbugs.ptsecurity.com, github.com/0xMarcio/cve, github.com/search | ✅ |
| Cloud / vendor blogs | blog.cloudflare.com/tag/security, rapid7.com | ✅ / ⚠️ |
| Bug bounty | hackerone.com/hacktivity, bugcrowd.com/disclosures, attackerkb.com | ❌ (JS / 404 / 403) |
| Russian / non-English | habr.com/ru/companies/tomhunter, teletype.in/@cyberok, cert.gov.ua | ⚠️ (no recent / empty extract) |
| Authoritative DBs | nvd.nist.gov, cve.org, cve.mitre.org | ⚠️ / ❌ (no Apr 26-27 entries / JS) |
| Research labs | googleprojectzero.blogspot.com (now projectzero.google), packetstormsecurity.com (now packetstorm.news) | ⚠️ |

**Errors:** cisa.gov + cisa.gov/known-exploited-vulnerabilities-catalog (403); attackerkb.com (403); bugcrowd.com/disclosures (404); hackerone.com/hacktivity (JS); cve.org, cve.mitre.org (JS); nvd.nist.gov (no extract for Apr 26-27); msrc.microsoft.com/blog (no extract — Microsoft now serves a JS shell).
**CISA KEV:** No new additions since 2026-04-24 (Samsung MagicINFO, SimpleHelp x2, D-Link DIR-823X). Today (2026-04-27) is the federal patch deadline for the previously-covered Adobe Acrobat CVE-2026-34621 KEV entry; CrowdStrike LogScale CVE-2026-40050 (covered yesterday) has no KEV entry yet.

---

*Watchtower vulnerability-researcher | Cycle: 2026-04-27/night | Next: 2026-04-28/night*
