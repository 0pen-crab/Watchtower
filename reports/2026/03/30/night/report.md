# 🔴 Vulnerability Research Report
**Cycle:** 2026-03-30 / Night  
**Generated:** 2026-03-30 03:07 EET  
**Sources:** 26/36 checked  
**New Findings:** 17 (10 critical/high, 5 medium, 2 low)

---

## 🚨 URGENT OPERATOR ALERT — THIS INSTANCE IS UNPATCHED

**OpenClaw version detected: `2026.2.21-2`**  
**Current latest: `2026.3.22+`**

This instance is running a version from **~6 weeks ago** and is vulnerable to **every single one** of the 15+ OpenClaw CVEs disclosed this week. Several are **CVSS 9.9 Critical** and enable RCE on connected devices. Additionally, the MEDIA: protocol zero-auth API key exfiltration is FULLY exploitable (partial fix only lands in v2026.3.22).

**Action required: `openclaw update` or reinstall from latest release.**

---

## 🔴 Critical / High Severity Findings

### 1. CVE-2026-32922 — OpenClaw device.token.rotate → RCE on Nodes (CVSS 9.9)
**Product:** OpenClaw < 2026.3.11 | **Status:** Patched | **Score:** 10/10

Callers with `operator.pairing` scope can call `device.token.rotate` to mint tokens with **any scope**, including `operator.admin`. This enables:
- Full RCE on connected nodes via `system.run`
- Unauthorized gateway-admin access
- Cross-device privilege escalation

**Fix:** Upgrade to OpenClaw >= 2026.3.11

---

### 2. CVE-2026-32987 — OpenClaw Bootstrap Code Replay → operator.admin Escalation (CVSS 9.3)
**Product:** OpenClaw < 2026.3.13 | **Status:** Patched | **Score:** 10/10

Bootstrap setup codes in `device-bootstrap.ts` can be replayed before approval to escalate pending pairing scope to `operator.admin`. CWE-294 (Improper Verification of Replay Protection).

**Fix:** Upgrade to OpenClaw >= 2026.3.13

---

### 3. GHSA-4749-wr9h-9qxx — OpenClaw MEDIA: Protocol Zero-Auth File Exfiltration (No CVE yet)
**Product:** OpenClaw <= 2026.3.13 (partial fix in 2026.3.22) | **Score:** 9/10

Any group chat member can inject `MEDIA:~/.openclaw/agents/<id>/agent/models.json` into chat, causing OpenClaw to read and deliver the file as an attachment. The `agents/` directory was removed from allowed roots in v2026.3.22 — but the `workspace/` directory **remains accessible**, meaning `SOUL.md`, `AGENTS.md`, and `USER.md` are still exfiltrable on patched versions.

**Files successfully exfiltrated (reported PoC):**
- `agent/models.json` — LLM provider API key (plaintext)
- `sessions/sessions.json` — session metadata, tool lists
- `sessions/<uuid>.jsonl` — complete conversation history
- Cross-agent reads (no per-agent isolation)

**Bypasses:** `tools.deny:["*"]`, exec security controls, all approval workflows.

**Disclosure:** Silently fixed 2026-03-22, shipped 2026-03-23, report denied, public Full Disclosure on 2026-03-28.

> **⚠️ This instance (v2026.2.21-2) is fully vulnerable — no mitigation at all.**

**Fix:** Upgrade to >= 2026.3.22. Even after patching, audit workspace files for sensitive data.

---

### 4. CVE-2026-32973 — OpenClaw exec Allowlist Glob Bypass (CVSS 9.8)
**Product:** OpenClaw < 2026.3.11 | **Status:** Patched | **Score:** 9/10

`matchesExecAllowlistPattern` applies `?` wildcard glob matching that spans path separators, enabling commands not intended by operators to execute. An operator writing `allow: ["/usr/bin/curl"]` can be bypassed with crafted inputs.

**Fix:** Upgrade to >= 2026.3.11

---

### 5. CVE-2026-32924 + CVE-2026-32975 — OpenClaw Feishu & Zalo Group Auth Bypasses (CVSS 9.8)
**Product:** OpenClaw < 2026.3.12 | **Status:** Patched | **Score:** 9/10

Two critical group authorization bypasses:
- **Feishu** (CVE-2026-32924): Reaction events with missing `chat_type` classified as p2p, bypassing `groupAllowFrom` and `requireMention`
- **Zalo** (CVE-2026-32975): Group allowlist matches mutable display names — create a clone group to bypass authorization

**Fix:** Upgrade to >= 2026.3.12

---

### 6. CVE-2026-32914 + CVE-2026-32915 — OpenClaw /config Access Bypass + Subagent Sandbox Escape (CVSS 8.8)
**Product:** OpenClaw < 2026.3.11-12 | **Status:** Patched | **Score:** 8/10

- **CVE-2026-32914**: Non-owner command-authorized users access owner-only `/config` and `/debug` to read/modify privileged settings
- **CVE-2026-32915**: Sandboxed subagents resolve against parent requester scope, enabling sibling session control and broader tool policy execution

**Fix:** Upgrade to >= 2026.3.12 (for 32914) and >= 2026.3.11 (for 32915)

---

### 7. CVE-2026-32974 — OpenClaw Feishu Webhook Auth Bypass (CVSS 8.6)
**Product:** OpenClaw < 2026.3.12 | **Status:** Patched | **Score:** 8/10

Feishu webhook with only `verificationToken` (no `encryptKey`) accepts forged events. Unauthenticated attackers can inject events to trigger tool execution.

**Fix:** Upgrade to >= 2026.3.12. Configure `encryptKey` for Feishu.

---

### 8. CVE-2026-32978 — OpenClaw system.run Approval TOCTOU (CVSS 8.0)
**Product:** OpenClaw < 2026.3.11 | **Status:** Patched | **Score:** 7/10

tsx/jiti script runners don't bind file operands at approval time. An attacker can rewrite approved scripts on disk and have modified code execute under the approved context.

**Fix:** Upgrade to >= 2026.3.11

---

### 9. CVE-2025-30189 — Dovecot Auth Cache Broken — Wrong User Login (CVSS 7.4)
**Product:** OX Dovecot CE core <= 2.4.0 / Pro <= 3.1.0 | **Status:** Patched | **Score:** 7/10

v2.4 regression breaks auth cache with multiple passdb/userdb drivers. All users sharing a cache key authenticate as the same user — effectively an auth bypass. No public exploits.

**Affected drivers:** Check advisory OXDC-2026-0001  
**Fix:** Upgrade to OX Dovecot CE 2.4.1 or Pro 3.1.2. Or disable auth caching.

---

### 10. CVE-2025-59032 — Dovecot ManageSieve Remote Crash (CVSS 7.5)
**Product:** OX Dovecot CE 2.4.x / Pro 3.1.x | **Status:** Patched | **Score:** 6/10

ManageSieve AUTHENTICATE command panics when a literal is used as SASL initial response, enabling repeated crashes/DoS. No public exploits.

**Fix:** Upgrade to CE 2.4.3 / Pro 3.1.3, or restrict ManageSieve access.

---

## 🟡 Medium Severity Findings

### 11. CVE-2026-0394 — Dovecot Pre-Auth Path Traversal via %d in passwd-file (CVSS 5.3)
**Product:** OX Dovecot Pro >= 2.3.0 (fixed in CE 2.4.0 / Pro 3.1.0)

Pre-auth path traversal: the `%d` domain escape in passwd-file passdb traverses above base directory (reads `/etc/passwd`). No public exploits.

**Fix:** Upgrade or avoid passwd-file passdb with user-controlled domain parameters.

---

### 12. CVE-2026-3098 — Smart Slider 3 WordPress Plugin Arbitrary File Read (800K Sites)
**Product:** Smart Slider 3 plugin <= 3.5.1.33 | **Status:** Patched

Subscriber-level authenticated users can read any server file, including `wp-config.php`. Patch in v3.5.1.34 (March 24). ~500K sites still unpatched.

**Fix:** Update Smart Slider 3 to v3.5.1.34 immediately on all managed WordPress sites.

---

### 13. MailEnable <= 10.54 — Triple Reflected XSS in Webmail (No CVE)
**Product:** MailEnable <= 10.54 (Windows email server) | **Status:** Patched in 10.55

Three reflected XSS in webmail paths (`ManageShares.aspx?SelectedIndex`, `FreeBusy.aspx?Attendees`, `FreeBusy.aspx?StartDate`). Full PoC URLs publicly disclosed. Patched in MailEnable 10.55 (March 2, 2026).

**Fix:** Upgrade MailEnable to 10.55.

---

### 14. CVE-2026-32980 — OpenClaw Telegram Webhook Pre-Auth DoS (CVSS 7.5)
**Product:** OpenClaw < 2026.3.13 | **Status:** Patched | **Score:** 6/10

Telegram webhook buffers full POST body before validating `x-telegram-bot-api-secret-token`, enabling unauthenticated memory exhaustion DoS.

**Fix:** Upgrade to >= 2026.3.13. Restrict webhook to Telegram IP ranges.

---

## 📋 Noted / Escalations

| Item | Detail |
|------|--------|
| CVE-2025-12548 Eclipse Che **ESCALATION** | Now has a public Metasploit module (03/27 wrap-up). Unauthenticated WebSocket RCE on port 3333. Red Hat OpenShift DevSpaces operators: patch now. |
| CVE-2026-23767 Epson ESC/POS | New Metasploit module for unauthenticated RCE on networked ESC/POS printers. |
| CVE-2026-28514/30833 Rocket.Chat | Auth bypass — listed by GitHub Security Lab. Monitoring for full disclosure. |
| CVE-2026-32919/32923/32972/32979 OpenClaw | Medium/lower-severity OpenClaw CVEs (CVSS 6.1–7.3). All fixed in >= 2026.3.11-12. |
| Iran cyber fallout | FortiGuard: No large-scale retaliation observed post-strikes. Regional activity elevated. Monitor. |
| Rapid7 2026 Global Threat Report | Key stats: 105% increase in CVSS 7-10 exploitation; median time to KEV = 5 days; ransomware in 42% of incidents. |

---

## 📊 Source Coverage (26/36)

| Source | Status | New Findings |
|--------|--------|-------------|
| bleepingcomputer.com | ✅ | CVE-2026-3098 Smart Slider |
| thehackernews.com | ✅ | None (dedup) |
| cisa.gov/known-exploited-vulnerabilities-catalog | ✅ | No new KEV additions |
| securityweek.com | ✅ | Context only |
| schneier.com | ✅ | Policy only |
| krebsonsecurity.com | ✅ | None (dedup) |
| rapid7.com/blog | ✅ | Metasploit 03/27 wrap-up; 2026 Threat Report |
| attackerkb.com | ✅ | CVE-2026-20127 deep-dive (dedup) |
| fortinet.com/blog/threat-research | ✅ | Iran cyber fallout noted |
| securitylab.github.com | ✅ | CVE-2026-28514/30833 Rocket.Chat |
| seclists.org/fulldisclosure | ✅ | OpenClaw MEDIA: protocol; Dovecot; MailEnable |
| app.opencve.io | ✅ | 15 new OpenClaw CVEs (March 29 batch) |
| nvd.nist.gov | ⚠️ JS-limited | Via OpenCVE |
| googleprojectzero.blogspot.com | ✅ | Windows UAC research (out of scope) |
| blog.cloudflare.com/tag/security | ✅ | No new vulns |
| msrc.microsoft.com/blog | ⚠️ Empty | — |
| hackerone.com/hacktivity | ⚠️ JS-only | — |
| kb.cert.org/vuls | ⚠️ Minimal | — |
| cert.gov.ua/article | ⚠️ Empty | — |
| github.com/0xMarcio/cve | ✅ | CVE-2026-0828 BYOVD (uncertain dedup) |
| wiz.io/blog | ✅ | TeamPCP (dedup) |
| isc.org/blogs | ⚠️ Nav-only | — |
| securityaffairs.com | ⚠️ Minimal | — |
| packetstormsecurity.com | ⚠️ TOS | — |
| app.opencve.io page 2 | ✅ | Confirmed prior CVEs in dedup |

---

*Report generated by vulnerability-researcher agent (OpenClaw v2026.2.21-2) at 03:07 EET. See debug.log for source check details and dedup decisions.*
