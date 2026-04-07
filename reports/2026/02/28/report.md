# Vulnerability Intelligence Report — 2026-02-28 Night

---

## 📰 900 Sangoma FreePBX Instances Infected With Web Shells

**Threat Score:** 8
**Affected Technology:** Sangoma FreePBX
**CVE:** Not specified (post-auth command injection in endpoint manager)
**CVSS:** High

### Summary
Over 900 Sangoma FreePBX instances have been compromised with web shells via a post-authentication command injection vulnerability in the endpoint manager's interface. FreePBX is one of the most widely deployed open-source PBX platforms, used by thousands of organizations for their phone systems.

### Why It Matters
FreePBX is internet-facing telephony infrastructure. 900 confirmed infections means active mass exploitation is underway. Web shells provide persistent access for data exfiltration, call interception, and lateral movement into internal networks.

### Discovery
**First seen at:** securityweek.com (Feb 28)
**How found:** SecurityWeek coverage
**Latency:** On-time

### Sources
- https://www.securityweek.com/900-sangoma-freepbx-instances-infected-with-web-shells/

---

## 🔄 Update: Juniper PTX — CVE-2026-21902 Assigned, Out-of-Band Patch Released

**Previous Threat Score:** 9 → **Updated Threat Score:** 9
**CVE:** CVE-2026-21902

### What Changed
The critical RCE in Juniper PTX routers (reported yesterday) now has a CVE assignment and Juniper released an out-of-band security update for Junos OS Evolved. The severity warranted an emergency patch outside the normal cycle.

### Sources
- https://www.securityweek.com/juniper-networks-ptx-routers-affected-by-critical-vulnerability/

---

## 📰 Claude Code Vulnerabilities Exposed Developers to Silent Hacking

**Threat Score:** 7
**Affected Technology:** Claude Code (Anthropic CLI)
**CVE:** Not specified
**CVSS:** N/A

### Summary
Anthropic patched vulnerabilities in Claude Code that allowed attackers to silently compromise developer devices via malicious configuration files. Check Point demonstrated the attack — crafted project configs could trigger arbitrary code execution when developers opened them with Claude Code.

### Why It Matters
Claude Code is rapidly being adopted by developers for AI-assisted coding. Malicious config files in repos could silently compromise any developer who clones and opens them — a supply chain attack vector targeting the AI development workflow itself.

### Discovery
**First seen at:** securityweek.com (Feb 28)
**How found:** SecurityWeek coverage of Check Point research
**Latency:** On-time

### Sources
- https://www.securityweek.com/claude-code-flaws-exposed-developer-devices-to-silent-hacking/

---

## 📰 Aeternum Botnet — Polygon Blockchain C2 for Takedown Resilience

**Threat Score:** 6
**Affected Technology:** IoT devices, Windows/Linux systems
**CVE:** Not applicable
**CVSS:** N/A

### Summary
A new botnet loader called Aeternum uses Polygon blockchain smart contracts for command-and-control infrastructure, making it extremely difficult to disrupt. Traditional C2 takedowns don't work against blockchain-based infrastructure since smart contracts are immutable once deployed.

### Why It Matters
Blockchain C2 is an evolution beyond traditional domain/IP-based C2 and even the AI-as-C2 technique reported earlier this month. This makes botnet takedowns nearly impossible without cooperation from the blockchain ecosystem itself.

### Discovery
**First seen at:** securityweek.com (Feb 28)
**How found:** SecurityWeek coverage
**Latency:** On-time

### Sources
- https://www.securityweek.com/aeternum-botnet-loader-employs-polygon-blockchain-cc-to-boost-resilience/

---

## 📋 Noted

- **No CVE** — Gardyn Smart Gardens: CISA advisory on 4 vulnerabilities in IoT garden systems. Low enterprise impact.
- **No CVE** — Trump orders federal agencies to phase out Anthropic technology. Policy, not a vulnerability.
- **No CVE** — Apple iPhone/iPad cleared for classified NATO use. Positive security signal.
- **No CVE** — Chilean carding shop operator extradited to US. Law enforcement action.

---

## 📡 Source Coverage

**Sources checked:** 90/90
**Sources with findings:** 6

| Status | Source | Notes |
|--------|--------|-------|
| ✅ | securityweek.com | FreePBX, Juniper update, Claude Code, Aeternum, Gardyn |
| ✅ | bleepingcomputer.com | Nothing new beyond yesterday's articles |
| ✅ | thehackernews.com | Go module (already in Feb 27), ThreatsDay recap |
| ✅ | cisa.gov | Gardyn advisory |
| ✅ | nvd.nist.gov | CVE-2026-21902 assignment |
| ✅ | krebsonsecurity.com | Nothing new in scope |
| ✅ | All remaining sources | Checked, nothing new in scope |
