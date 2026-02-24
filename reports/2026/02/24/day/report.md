# Watchtower Report — 2026-02-24 (Day Cycle)

**Sources checked:** 89/89 | **New findings:** 20 | **Updates:** 2

---

## 🔴 CRITICAL

### Lazarus Group Linked to Medusa Ransomware — US Healthcare Targeted
North Korean state-backed Lazarus group is now directly operating Medusa ransomware against US healthcare organizations. This marks a significant escalation from espionage to ransomware extortion by DPRK actors, blurring lines between nation-state and cybercriminal activity.
**Sources:** BleepingComputer, The Record

### CVE-2026-1731 BeyondTrust RCE — Active Scanning Confirmed by GreyNoise
GreyNoise published detailed analysis of CVE-2026-1731 reconnaissance activity starting within 24 hours of PoC publication. Key findings: a single IP accounts for 86% of scanning, attackers are probing non-standard ports (security-through-obscurity evasion), JA4+ fingerprints reveal shared tooling across VPN tunnels, and scanning actors are also targeting other CVEs simultaneously. Exploitation is imminent or already occurring.
**CVE:** CVE-2026-1731 (CVSS 9.9) | **Sources:** GreyNoise, Cybersecurity Dive

---

## 🟠 HIGH

### ShinyHunters Claims Odido Breach — Millions of Dutch Telecom Users
The ShinyHunters extortion gang claims responsibility for breaching Odido (Dutch telecom), stealing millions of subscriber records including personal details.
**Sources:** BleepingComputer

### EnOcean SmartServer IoT — Two New Vulnerabilities
Claroty Team82 disclosed CVE-2026-22885 and CVE-2026-20761 in EnOcean SmartServer IoT devices used in building automation systems.
**CVEs:** CVE-2026-22885, CVE-2026-20761 | **Sources:** Claroty Team82

### Endor Labs Discloses Six New OpenClaw Vulnerabilities
Six new vulnerabilities found in the AI assistant platform OpenClaw, expanding the attack surface for AI agent infrastructure.
**Sources:** Infosecurity Magazine

### Bitdefender: OpenClaw Malicious Skill Trap Deep Dive
Bitdefender Labs analyzed how attackers create malicious OpenClaw skills that appear helpful but contain hidden payloads targeting AI agent users.
**Sources:** Bitdefender Labs

### Cisco: AI MCP Infrastructure Is 'Woefully Insecure'
Cisco warns that Model Context Protocol (MCP) — the "connective tissue" for AI agent communication — has fundamental security weaknesses creating broad attack surfaces as enterprises deploy AI agents.
**Sources:** Cybersecurity Dive

---

## 🟡 MEDIUM

### Optimizely Data Breach via Vishing Attack
Ad tech company Optimizely confirmed a data breach after threat actors compromised systems through voice phishing. Undisclosed number of customers notified.
**Sources:** BleepingComputer

### Android Mental Health Apps (14.7M Installs) Have Security Flaws
Multiple Google Play mental health apps with 14.7M combined downloads contain vulnerabilities that could expose sensitive medical information.
**Sources:** BleepingComputer

### Advantest (Semiconductor Testing) Hit by Ransomware
Japanese chip-testing giant Advantest deployed IR protocols after ransomware attack.
**Sources:** BleepingComputer, Infosecurity Magazine

### Air Côte d'Ivoire Ransomware Attack
West African airline hit by ransomware with data exfiltration claims.
**Sources:** The Record

### Cellebrite Linked to Unauthorized Phone Access of Kenyan Candidate
Citizen Lab links Cellebrite mobile forensics tools to unauthorized access of a Kenyan political candidate's device.
**Sources:** The Record

### Vanta Diagnostics Breach — 140K Affected
Medical diagnostics company breach exposing sensitive health and personal data of ~140,000 individuals.
**Sources:** The Record

### OysterLoader: Multi-Stage C++ Evasion Loader
Sekoia details OysterLoader (aka Broomstick/CleanUp), a multi-stage C++ loader with advanced evasion capabilities used in active campaigns.
**Sources:** Sekoia

### IClickFix: WordPress ClickFix Framework (Update)
Sekoia documents a widespread WordPress-targeting framework using the ClickFix social engineering tactic. Extends earlier ClickFix campaign reporting with WordPress-specific framework details.
**Sources:** Sekoia

### LummaStealer Revival with CastleLoader
LummaStealer infostealer getting a second life alongside new CastleLoader delivery mechanism, showing continued evolution of the infostealer ecosystem.
**Sources:** Bitdefender Labs

### Data-Only Extortion Growing vs Traditional Ransomware
Arctic Wolf report shows data-only extortion (no encryption) is rising as threat actors find it more profitable and lower risk.
**Sources:** Cybersecurity Dive

---

## 🔵 LOW / INFO

### Phobos Ransomware Affiliate Arrested in Poland
Continuing international law enforcement pressure on ransomware operators.
**Sources:** The Record

### Spain Arrests Anonymous Fenix Hacktivists
Four alleged hacktivists arrested for DDoS attacks on government ministries and political parties.
**Sources:** BleepingComputer

### CrowdStrike: Adversary Breakout Time Under 30 Minutes
CrowdStrike Global Threat Report warns adversaries leverage AI for faster, more efficient campaigns with breakout times often under 30 minutes.
**Sources:** CrowdStrike, Infosecurity Magazine

---

## Dedup Notes
Previously reported items confirmed still active but not re-listed: CVE-2026-2441 (Chrome), Ivanti EPMM/EPM, Dell RecoverPoint/Grimbolt, SmarterMail, Grandstream VoIP, OpenSSL AISLE, Roundcube KEV, LockBit 5.0 Proxmox, FortiGate AI breach (600+), Predator iOS, WPvivid, SANDWORM_MODE npm, MuddyWater Olalampo, Arkanix Stealer, MS Patch Tuesday, Starkiller PhaaS, Kimwolf I2P, PromptSpy, ShinyHunters SSO vishing, n8n/GIMP/Phoenix Contact CVEs.
