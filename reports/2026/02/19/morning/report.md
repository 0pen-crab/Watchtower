# Vulnerability Intelligence Report — 2026-02-19 Morning

---

## 📰 Grandstream VoIP Phones — Unauthenticated Root RCE with Eavesdropping (CVE-2026-2329)

**Threat Score:** 8
**Affected Technology:** Grandstream GXP1600 series VoIP phones
**CVE:** CVE-2026-2329
**CVSS:** Critical

### Summary
A critical vulnerability in Grandstream GXP1600 series VoIP phones allows remote, unauthenticated root-level access with silent eavesdropping capability. No patch available at disclosure.

### Why It Matters
VoIP phones are often reachable via SIP infrastructure. Root RCE with eavesdropping is ideal for espionage. Isolate GXP1600 series immediately.

### Discovery
**First seen at:** securityweek.com, bleepingcomputer.com
**How found:** Simultaneous multi-outlet coverage
**Latency:** On-time

### Sources
- https://www.securityweek.com/critical-grandstream-phone-vulnerability-exposes-calls-to-interception/
- https://www.bleepingcomputer.com/news/security/flaw-in-grandstream-voip-phones-allows-stealthy-eavesdropping/

---

## 📰 Microsoft Entra Accounts Targeted via Device Code + Vishing

**Threat Score:** 7
**Affected Technology:** Microsoft Entra ID (Azure AD), OAuth 2.0 Device Authorization
**CVE:** Not applicable (protocol abuse)
**CVSS:** N/A

### Summary
Threat actors combine device code phishing with vishing to abuse OAuth 2.0 Device Authorization flow and compromise Microsoft Entra accounts. Targets: technology, manufacturing, financial orgs. Bypasses MFA via legitimate OAuth flow.

### Why It Matters
Microsoft Entra ID is the identity backbone for enterprise Microsoft environments. Successful compromise gives persistent access to email, SharePoint, Teams, and Azure.

### Discovery
**First seen at:** bleepingcomputer.com
**How found:** BleepingComputer coverage of active campaigns
**Latency:** On-time

### Sources
- https://www.bleepingcomputer.com/news/security/hackers-target-microsoft-entra-accounts-in-device-code-vishing-attacks/

---

## 🔄 Update: Dell RecoverPoint — CISA Orders 3-Day Patch (CVE-2026-22769)

**Previous Threat Score:** 8 → **Updated Threat Score:** 9
**CVE:** CVE-2026-22769

### What Changed
CISA issued emergency directive with 3-day deadline (vs standard 21). Confirms Chinese state-backed exploitation since mid-2024 — an 18+ month zero-day campaign. The tight deadline signals active mass exploitation.

### Sources
- https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-dell-flaw-within-3-days/

---

## 📰 OpenSSL RCE Vulnerability Disclosed

**Threat Score:** 7
**Affected Technology:** OpenSSL
**CVE:** Details pending
**CVSS:** Critical (expected)

### Summary
New RCE vulnerability in OpenSSL disclosed. Details still emerging, but any RCE in OpenSSL is inherently high-impact given its ubiquity across all internet-facing encrypted services.

### Why It Matters
OpenSSL underpins TLS for web servers, email, VPN, and essentially every encrypted internet service.

### Discovery
**First seen at:** thehackernews.com (ThreatsDay Bulletin)
**How found:** Weekly security roundup
**Latency:** On-time

### Sources
- https://thehackernews.com/2026/02/threatsday-bulletin-openssl-rce-foxit-0.html

---

## 📋 Noted

- **No CVE** — PromptSpy Android malware: First to abuse Gemini AI at runtime. Mobile-only but notable AI trend.
- **No CVE** — Massiv Android banking trojan: Targeting south Europe via IPTV app. Mobile-only.
- **No CVE** — Texas sues TP-Link over firmware vulnerabilities. Regulatory action.

---

## 📡 Source Coverage

**Sources checked:** 90/90
**Sources with findings:** 7

| Status | Source | Notes |
|--------|--------|-------|
| ✅ | bleepingcomputer.com | Grandstream, Entra vishing, Dell update |
| ✅ | securityweek.com | Grandstream VoIP |
| ✅ | thehackernews.com | OpenSSL RCE, ThreatsDay bulletin |
| ✅ | cisa.gov | Dell emergency directive |
| ✅ | nvd.nist.gov | CVE lookups |
| ✅ | reddit.com/r/netsec | Grandstream, OpenSSL discussion |
| ✅ | attackerkb.com | Nothing new |
| ✅ | All remaining sources | Checked, nothing new in scope |
