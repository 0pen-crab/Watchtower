#!/usr/bin/env python3
"""
Watchtower report.json schema validator.
Usage: python3 validate_report.py <path_to_report.json> [--fix]
  --fix: attempt to auto-fix common issues and write back
Exit code 0 = valid, 1 = errors found
"""

import json
import sys
import os

REQUIRED_TOP_KEYS = {"date", "cycle", "findings", "noted", "source_coverage", "full_report"}
VALID_CYCLES = {"morning", "day", "evening", "night"}
VALID_FINDING_TYPES = {"news", "update"}

NEWS_KEYS = {"type", "title", "threat_score", "cve", "cvss", "affected_technology", "summary", "discovery_latency", "first_seen_at"}
UPDATE_KEYS = {"type", "title", "threat_score", "previous_threat_score", "cve", "cvss", "affected_technology", "summary", "first_seen_at"}
NOTED_KEYS = {"cve", "product", "summary"}
COVERAGE_KEYS = {"total", "checked", "with_findings", "unreachable", "degraded"}

VALID_LATENCY = {"early", "on-time", "late"}


def validate(data, filepath=""):
    errors = []
    warnings = []

    # Top-level keys
    missing = REQUIRED_TOP_KEYS - set(data.keys())
    extra = set(data.keys()) - REQUIRED_TOP_KEYS
    if missing:
        errors.append(f"Missing top-level keys: {missing}")
    if extra:
        errors.append(f"Extra top-level keys (remove these): {extra}")

    # date format
    date = data.get("date", "")
    if not (isinstance(date, str) and len(date) == 10 and date[4] == "-" and date[7] == "-"):
        errors.append(f"'date' must be YYYY-MM-DD string, got: {repr(date)}")

    # cycle
    cycle = data.get("cycle", "")
    if cycle not in VALID_CYCLES:
        errors.append(f"'cycle' must be one of {VALID_CYCLES}, got: {repr(cycle)}")

    # full_report
    fr = data.get("full_report", "")
    if not (isinstance(fr, str) and fr.startswith("reports/") and fr.endswith("/report.md")):
        errors.append(f"'full_report' must be repo-relative path like 'reports/YYYY/MM/DD/cycle/report.md', got: {repr(fr)}")

    # findings
    findings = data.get("findings", [])
    if not isinstance(findings, list):
        errors.append(f"'findings' must be array, got: {type(findings).__name__}")
        findings = []

    for i, f in enumerate(findings):
        prefix = f"findings[{i}]"
        if not isinstance(f, dict):
            errors.append(f"{prefix}: must be object, got {type(f).__name__}")
            continue

        ftype = f.get("type")
        if ftype not in VALID_FINDING_TYPES:
            errors.append(f"{prefix}: 'type' must be 'news' or 'update', got: {repr(ftype)}")
            continue

        expected = NEWS_KEYS if ftype == "news" else UPDATE_KEYS
        missing_f = expected - set(f.keys())
        extra_f = set(f.keys()) - expected
        if missing_f:
            errors.append(f"{prefix} ({ftype}): missing keys: {missing_f}")
        if extra_f:
            errors.append(f"{prefix} ({ftype}): extra keys (remove): {extra_f}")

        # threat_score
        ts = f.get("threat_score")
        if not (isinstance(ts, int) and 1 <= ts <= 10):
            errors.append(f"{prefix}: 'threat_score' must be int 1-10, got: {repr(ts)}")

        # previous_threat_score for updates
        if ftype == "update":
            pts = f.get("previous_threat_score")
            if not (isinstance(pts, int) and 1 <= pts <= 10):
                errors.append(f"{prefix}: 'previous_threat_score' must be int 1-10, got: {repr(pts)}")

        # discovery_latency for news
        if ftype == "news":
            dl = f.get("discovery_latency")
            if dl not in VALID_LATENCY:
                errors.append(f"{prefix}: 'discovery_latency' must be one of {VALID_LATENCY}, got: {repr(dl)}")

        # summary should be one sentence (heuristic: no newlines, reasonable length)
        summary = f.get("summary", "")
        if isinstance(summary, str):
            if "\n" in summary:
                warnings.append(f"{prefix}: 'summary' contains newlines (should be one sentence)")
            if len(summary) > 300:
                warnings.append(f"{prefix}: 'summary' is {len(summary)} chars (aim for <200)")

        # cve format check
        cve = f.get("cve")
        if cve is not None and isinstance(cve, str) and cve != "Not yet assigned":
            for c in cve.split(", "):
                c = c.strip()
                if c and not c.startswith("CVE-") and c != "null" and c != "Details pending" and c != "Multiple" and c != "Not specified" and c != "Not disclosed":
                    warnings.append(f"{prefix}: CVE '{c}' doesn't start with 'CVE-'")

    # noted
    noted = data.get("noted", [])
    if not isinstance(noted, list):
        errors.append(f"'noted' must be array, got: {type(noted).__name__}")
        noted = []

    for i, n in enumerate(noted):
        prefix = f"noted[{i}]"
        if not isinstance(n, dict):
            errors.append(f"{prefix}: must be object")
            continue
        missing_n = NOTED_KEYS - set(n.keys())
        extra_n = set(n.keys()) - NOTED_KEYS
        if missing_n:
            errors.append(f"{prefix}: missing keys: {missing_n}")
        if extra_n:
            errors.append(f"{prefix}: extra keys (remove): {extra_n}")

    # source_coverage
    cov = data.get("source_coverage", {})
    if not isinstance(cov, dict):
        errors.append(f"'source_coverage' must be object, got: {type(cov).__name__}")
    else:
        missing_c = COVERAGE_KEYS - set(cov.keys())
        extra_c = set(cov.keys()) - COVERAGE_KEYS
        if missing_c:
            errors.append(f"source_coverage: missing keys: {missing_c}")
        if extra_c:
            errors.append(f"source_coverage: extra keys: {extra_c}")

        total = cov.get("total", 0)
        checked = cov.get("checked", 0)
        unreachable = len(cov.get("unreachable", []))
        degraded = len(cov.get("degraded", []))

        if isinstance(total, int) and isinstance(checked, int):
            if checked < total - unreachable:
                errors.append(f"source_coverage: checked ({checked}) < total ({total}) - unreachable ({unreachable}). Report is NOT DONE.")
            if total == 0:
                errors.append(f"source_coverage: total is 0 — this is clearly wrong")
            if checked == 0 and total > 0:
                errors.append(f"source_coverage: checked is 0 — no sources were scanned")

    return errors, warnings


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <report.json> [--fix]")
        sys.exit(1)

    filepath = sys.argv[1]
    fix_mode = "--fix" in sys.argv

    if not os.path.exists(filepath):
        print(f"❌ File not found: {filepath}")
        sys.exit(1)

    try:
        with open(filepath) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ JSON parse error: {e}")
        sys.exit(1)

    errors, warnings = validate(data, filepath)

    if warnings:
        print(f"⚠️  {len(warnings)} warning(s):")
        for w in warnings:
            print(f"   {w}")

    if errors:
        print(f"\n❌ {len(errors)} error(s) — REPORT INVALID:")
        for e in errors:
            print(f"   {e}")
        sys.exit(1)
    else:
        print(f"✅ {filepath} — valid")
        sys.exit(0)


if __name__ == "__main__":
    main()
