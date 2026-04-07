# Vulnerability Research Report
**Date:** 2026-03-23 | **Cycle:** Night | **Analyst:** Watchtower / vulnerability-researcher
**Generated:** 2026-03-23T02:15:00+02:00 (Athens)
**Sources Checked:** 30/31 | **Unreachable:** bugcrowd.com/disclosures | **Degraded:** blog.cloudflare.com

---

## 🔴 CRITICAL FINDINGS

---

### 1. CVE-2026-33017 — Langflow Unauthenticated RCE Actively Exploited
**Threat Score:** 9/10 | **CVSS:** 9.3 | **Type:** news | **First Seen:** securityweek.com

**Affected:** Langflow AI Workflow Builder ≤ 1.8.1  
**Fixed In:** Langflow 1.9.0  
**CWE:** CWE-94 (Code Injection), CWE-95 (Eval Injection), CWE-306 (Missing Auth for Critical Function)

**Summary:**  
The `POST /api/v1/build_public_tmp/{flow_id}/flow` endpoint is intentionally unauthenticated for public flows, but incorrectly accepts an optional `data` parameter containing attacker-supplied flow definitions with arbitrary Python code. This code traverses through `build_graph_from_data()` → `Graph.from_payload()` → `instantiate_component()` → `exec(compiled_code, exec_globals)` with zero sandboxing.

**Exploitation Timeline:**
- Patch shipped with Langflow 1.9.0 (GitHub GHSA-vwmf-pq79-vjvx)
- ≤20 hours post-disclosure: Sysdig documented active exploitation in production environments (referenced by CISA-ADP in NVD)
- ~16 hours ago: 3 independent PoC repositories published (MaxMnMl, SimoesCTT, omer-efe-curkus)

**Attack Surface:**  
Langflow is deployed extensively in DevOps pipelines, data science workflows, and AI agent platforms. Any internet-exposed Langflow instance ≤ 1.8.1 is vulnerable. No authentication required.

**Remediation:**
- Upgrade to Langflow 1.9.0 immediately
- If immediate upgrade isn't possible, block public access to `/api/v1/build_public_tmp/` at the network/WAF layer
- Review server logs for unexpected POST requests to this endpoint

---

### 2. CVE-2026-20127 — Cisco Catalyst SD-WAN Auth Bypass Exploited by Chinese APT
**Threat Score:** 9/10 | **CVSS:** 10.0 | **Type:** news | **First Seen:** attackerkb.com

**Affected:** Cisco Catalyst SD-WAN Controller (vSmart)  
**Discovery Latency:** late (Cisco Talos disclosed Feb 25; not covered in prior cycles)

**Summary:**  
A flaw in the vdaemon service allows an unauthenticated remote attacker to bypass authentication and obtain administrative privileges on the SD-WAN Controller by sending a crafted request. Cisco Talos tracks active exploitation as UAT-8616 — assessed with high confidence as a sophisticated Chinese cyber threat actor.

**Attack Chain:**
1. CVE-2026-20127: Initial auth bypass → administrative access to vSmart Controller
2. CVE-2022-20775: Subsequent privilege escalation to root via software version downgrade
3. Actor restores original version to cover tracks (root persistence achieved)

**Scope of Damage:**
- Malicious activity traced back at least 3 years (since 2023) — actor has deep persistent access to SD-WAN deployments
- Targets: Critical Infrastructure, enterprise edge networks
- Australian Cyber Security Centre (ACSC) published joint hunt guide with Cisco

**Log IOC (Initial Access):**
```
%Viptela-vSmart-VDAEMON_0-5-NTCE-1000001: control-connection-state-change new-state:up peer-type:vmanage peer-system-ip:<UNEXPECTED_IP>
```

**Remediation:**
- Apply Cisco Security Advisory: cisco-sa-sdwan-rpa-EHchtZk immediately
- Audit all vManage peering events against known authorized IP ranges
- Cross-reference with ACSC Hunt Guide for IoC sweep
- Disable/restrict vdaemon service access where not operationally required

---

## 🟠 HIGH FINDINGS

---

### 3. CVE-2026-22200 — osTicket PHP Filter Chain → CNEXT RCE Chain (Horizon3.ai PoC)
**Threat Score:** 8/10 | **CVSS:** 9.1 | **Type:** news | **First Seen:** github.com/0xMarcio/cve

**Affected:** osTicket < 1.18.3 (v1.17.x < 1.17.7)  
**Also Requires:** CVE-2024-2961 (CNEXT glibc heap overflow) for RCE component  
**Patched:** osTicket 1.18.3 / 1.17.7

**Summary:**  
Horizon3.ai published a full exploit chain ("Ticket to Shell"). osTicket uses mPDF to export tickets as PDFs — mPDF fails to blacklist dangerous PHP filter URI schemes after normalization (`php:\\` bypasses the `php://` check). Any user with ticket view access (including unauthenticated guests if guest access is enabled — the **default**) can inject a PHP filter chain expression as `<img src="php:\\filter/chain...">` in a ticket, trigger PDF export, and exfiltrate arbitrary server files embedded as bitmap images in the PDF.

When CNEXT (CVE-2024-2961) is reachable (glibc ≤ 2.39 on the server), this file read is chainable to full RCE.

**Attack Surface:**
- Thousands of osTicket instances exposed to the internet
- Prevalent in SLED (State, Local, Education) and SMB sectors
- Guest access enabled by default = unauthenticated exploitation

**Remediation:**
- Upgrade to osTicket 1.18.3 or 1.17.7
- If not possible: disable guest ticket submission or restrict PDF export functionality
- Update glibc to ≥ 2.40 to remove the CNEXT RCE chain

---

### 4. Chrysalis Backdoor — Lotus Blossom APT (Chinese) via Notepad++ Infrastructure
**Threat Score:** 8/10 | **CVSS:** N/A | **Type:** news | **First Seen:** rapid7.com

**Affected:** Windows systems (targeted: government, telecom, aviation, CI, media in SE Asia / Central America)

**Summary:**  
Rapid7 Labs uncovered a sophisticated Lotus Blossom (active since 2009) campaign leveraging compromised Notepad++ update distribution infrastructure. The attack chain:

1. `notepad++.exe` → `GUP.exe` (updater) → malicious `update.exe` downloaded from 95.179.213.0
2. `update.exe` is an NSIS installer: drops `BluetoothService.exe` (legitimate renamed Bitdefender Submission Wizard) + malicious `log.dll` to `%AppData%\Bluetooth\` (hidden)
3. DLL sideload: `log.dll` exports `LogInit` (loads shellcode) + `LogWrite` (decrypts via LCG-based stream cipher with constants 0x19660D / 0x3C6EF35F)
4. Shellcode executes **Chrysalis** — a new undocumented C2 backdoor
5. One loader variant ("ConsoleApplication2.exe") uses Microsoft Warbird to protect shellcode execution

**Key IoCs:**
- `BluetoothService.exe` SHA-256: `2da00de67720f5f13b17e9d985fe70f10f153da60c9ab1086fe58f069a156924`
- `log.dll` SHA-256: `3bdc4c0637591533f1d4198a72a33426c01f69bd2e15ceee547866f65e26b7ad`
- `%AppData%\Bluetooth\` directory with HIDDEN attribute
- C2 staging: `95.179.213.0`

**Remediation:**
- Block `95.179.213.0` at perimeter
- Hunt for `%AppData%\Bluetooth\` hidden directories containing `BluetoothService.exe`
- Verify Notepad++ binary and GUP.exe integrity via official signatures
- Deploy detections for DLL sideloading patterns with Bitdefender legitimate binaries

---

## 🟡 MEDIUM FINDINGS

---

### 5. VoidStealer v2.0 — First In-the-Wild Chrome ABE Hardware Debugger Bypass
**Threat Score:** 7/10 | **CVSS:** N/A | **Type:** news | **First Seen:** bleepingcomputer.com

**Affected:** Google Chrome (post-ABE, v127+) and Microsoft Edge  
**Source:** Gen Digital (Norton/Avast parent)

**Summary:**  
VoidStealer MaaS (first advertised December 2025) introduced a novel Application-Bound Encryption (ABE) bypass in v2.0. The technique:
1. Spawns a **suspended, hidden** Chrome process and attaches as a debugger
2. Waits for `chrome.dll` to load; scans DLL for a specific string to locate the LEA instruction referencing the ABE decryption routine
3. Sets hardware breakpoints across all browser threads targeting this address
4. When Chrome decrypts ABE-protected cookies on startup, the breakpoint fires
5. Reads the register pointing to the plaintext `v20_master_key` via `ReadProcessMemory`

No privilege escalation or code injection required. Based on open-source **ElevationKatz** (from ChromeKatz project). First infostealer to adopt this technique in the wild.

**Impact:** Complete Chrome session hijacking (cookies, saved passwords, payment data) for any victim running the malware.

**Remediation:**
- No patch available for this technique at time of writing (Google contacted)
- Endpoint protection: monitor for hidden browser processes spawned by non-browser parents
- EDR rules: alert on `ReadProcessMemory` targeting browser DLLs from non-browser processes
- Hardware breakpoint (DR0-DR3 register) manipulation from external processes

---

### 6. CVE-2026-29058 — AVideo Encoder Unauthenticated OS Command Injection (Metasploit)
**Threat Score:** 7/10 | **CVSS:** 9.8 | **Type:** news | **First Seen:** rapid7.com

**Affected:** AVideo Encoder (getImage.php endpoint)  
**Metasploit Module:** Added in Rapid7 March 20 wrap-up

**Summary:**  
`getImage.php` in AVideo Encoder passes user-supplied input directly to a shell command without sanitization, enabling unauthenticated OS command injection. With a Metasploit module now publicly available, exploitation is trivial for script kiddies. AVideo is commonly deployed for self-hosted video streaming, often internet-exposed.

**Remediation:**
- Apply vendor patch
- If unpatched, block unauthenticated access to `getImage.php` via WAF/server config
- AVideo Encoder installs should not be internet-facing without authentication

---

## 🟢 LOW-MEDIUM FINDINGS

---

### 7. CVE-2026-23745 — node-tar < 7.5.3 Arbitrary File Overwrite via Unsanitized Hardlink Paths
**Threat Score:** 6/10 | **CVSS:** 7.5 | **Type:** news | **First Seen:** github.com/0xMarcio/cve

**Affected:** npm `tar` package < 7.5.3  
**Patched:** v7.5.3

**Summary:**  
`src/unpack.ts` calls `path.resolve(this.cwd, String(entry.linkpath))` on hardlink/symlink targets without stripping absolute paths. Since `path.resolve()` ignores the `cwd` argument when `linkpath` is absolute, a malicious tar archive can specify `/etc/passwd` or any other system path as a hardlink target, overwriting it during extraction even with `preservePaths: false` set. The fix in v7.5.3 adds `stripAbsolutePath()` before resolution.

**Impact:** Any Node.js application or build pipeline that extracts untrusted tar archives using the `tar` npm package is vulnerable. Common in CI/CD pipelines, build tools, and container image layers.

**Remediation:**
- Update `tar` npm package to ≥ 7.5.3
- Review CI/CD pipelines for untrusted tar extraction

---

## 📌 NOTED (Unverified / Pending Confirmation)

---

### CVE-2026-24516 — DigitalOcean Droplet Agent Pre-Auth Root RCE (UNVERIFIED)
**Product:** DigitalOcean Droplet Agent ≤ 1.3.2  
**Researcher:** Cortex Security Research (@pox_sky_01)

Claimed CVSS 10.0 pre-auth root RCE via command injection in `troubleshooting/actioner/actioner.go`. The agent allegedly processes metadata from 169.254.169.254 and executes unsanitized commands from `TroubleshootingAgent.Requesting`, triggered via a port-knocking TCP packet to port 22 (SeqNum: 68796879, AckNum: 848489). CVE is in RESERVED status on NVD; no DigitalOcean security advisory found at time of writing. **Treat as unverified pending vendor confirmation.**

---

## 📊 Intelligence Summary

| # | CVE | Product | CVSS | Threat Score | Status |
|---|-----|---------|------|-------------|--------|
| 1 | CVE-2026-33017 | Langflow ≤ 1.8.1 | 9.3 | 9/10 🔴 | Actively exploited |
| 2 | CVE-2026-20127 | Cisco SD-WAN vSmart | 10.0 | 9/10 🔴 | Actively exploited (APT) |
| 3 | CVE-2026-22200 | osTicket < 1.18.3 | 9.1 | 8/10 🟠 | PoC public |
| 4 | Chrysalis | Windows (Notepad++) | N/A | 8/10 🟠 | Active APT campaign |
| 5 | VoidStealer | Chrome/Edge | N/A | 7/10 🟡 | MaaS in-the-wild |
| 6 | CVE-2026-29058 | AVideo Encoder | 9.8 | 7/10 🟡 | Metasploit module live |
| 7 | CVE-2026-23745 | node-tar < 7.5.3 | 7.5 | 6/10 🟢 | PoC public |

---

## 🔍 Source Coverage

- **Total:** 31 | **Checked:** 30 | **With Findings:** 8
- **Unreachable:** bugcrowd.com/disclosures (persistent)
- **Degraded:** blog.cloudflare.com/tag/security (WAF timeout)

---

*Debug log: reports/2026/03/23/night/debug.log*
