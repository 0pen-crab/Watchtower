# Vulnerability Report — 2026-03-01 (Night Cycle)

## Executive Summary

Three findings and four noted items from scanning 72 of 90 sources. Quiet period (Saturday night into Sunday). The standout finding is ClawJacked, a high-severity WebSocket hijacking vulnerability in the OpenClaw AI agent gateway that could allow any malicious website to silently take over locally running AI agents. Two additional FortiOS vulnerabilities were identified that were not captured in the previous cycle.

---

## Findings

### 1. ClawJacked: OpenClaw WebSocket Hijacking Allows Full AI Agent Takeover (Threat Score: 8/10)

Oasis Security disclosed "ClawJacked," a high-severity vulnerability in the OpenClaw AI agent gateway. The attack exploits the fact that browsers don't block cross-origin WebSocket connections to localhost. A malicious website can:

1. Open a WebSocket connection to the local OpenClaw gateway port
2. Brute-force the gateway password (no rate limiting)
3. Silently register as a trusted device (auto-approved for localhost connections)
4. Gain complete control over the AI agent — including configuration access, node enumeration, and log reading

A separate log poisoning vulnerability was also disclosed, allowing attackers to embed indirect prompt injections into agent logs via WebSocket requests to publicly exposed instances.

OpenClaw patched both issues within 24 hours in version 2026.2.25 (released February 26, 2026). Users should update immediately, audit agent access, and ensure gateway ports are not exposed to the internet.

**Source:** The Hacker News, Oasis Security Blog, BleepingComputer

---

### 2. CVE-2025-25249: High-Severity Heap Buffer Overflow in FortiOS/FortiSwitchManager (Threat Score: 7/10)

Fortinet published PSIRT advisory FG-IR-25-084 for a heap-based buffer overflow (CWE-122) in the cw_acd daemon of FortiOS and FortiSwitchManager. Exploitation could allow arbitrary code execution. Fixes are included in FortiOS 7.6.3+ and FortiSwitchManager 7.2.6+.

**Source:** FortiGuard PSIRT

---

### 3. CVE-2026-22153: FortiOS LDAP Authentication Bypass in Agentless VPN/FSSO (Threat Score: 7/10)

Fortinet published PSIRT advisory FG-IR-25-1052 for an authentication bypass by primary weakness (CWE-305) in the FortiOS fnbamd component. The vulnerability affects Agentless VPN and FSSO authentication flows, potentially allowing LDAP authentication bypass. Fix included in FortiOS 7.6.4+. Published February 10 but identified in this cycle's scan.

**Source:** FortiGuard PSIRT

---

## Noted Items

| Product | CVE | Summary |
|---------|-----|---------|
| FortiOS SSL-VPN | CVE-2025-68686 | SSL-VPN symlink persistence patch bypass — medium severity |
| 1Phish Kit | — | Datadog Security Labs deep dive into sophisticated credential harvesting framework |
| Winos 4.0 / ValleyRat | — | FortiGuard Labs analysis of campaigns targeting Taiwan with DLL sideloading and BYOVD |
| Agent Tesla | — | FortiGuard Labs multi-stage campaign analysis with process hollowing and exfiltration |

---

## Dedup Exclusions

The following were seen but excluded as already reported:
- UNC2814 GRIDTIDE Chinese espionage (reported 2026-02-28)
- CVE-2026-2329 Grandstream GXP1600 (reported 2026-02-28)
- Malicious npm ambar-src (reported 2026-02-28)
- Lazarus + Medusa ransomware (reported 2026-02-28)
- CISA RESURGE on Ivanti (reported 2026-02-28)
- CVE-2025-15467 OpenSSL/Fortinet (reported 2026-02-28)
- CVE-2025-55018 FortiOS HTTP smuggling (noted 2026-02-28)
- CVE-2026-20127 Cisco SD-WAN (reported 2026-02-25)
- CVE-2026-1731 BeyondTrust (reported 2026-02-16)

---

## Source Coverage

- **Total sources:** 90
- **Checked:** 72
- **With findings:** 8
- **Unreachable (18):** x.com (all accounts), t.me, discord.gg, owasp.org/slack, 0day.today, threatpost.com, vulndb.cyberriskanalytics.com, cnvd.org.cn, cert.gov.ua, securityfocus.com, opencve.io, strobes.co, cybersecuritydispatch.com, dbugs.ptsecurity.com, habr.com, teletype.in, isc.sans.edu (522 timeout), reddit.com (content not rendering)
