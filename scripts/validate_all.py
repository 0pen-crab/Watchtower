#!/usr/bin/env python3
"""Validate all report.json files in the repo."""
import json, glob, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from validate_report import validate

total = 0
valid = 0
invalid = 0

for f in sorted(glob.glob("reports/**/report.json", recursive=True)):
    total += 1
    try:
        data = json.load(open(f))
    except json.JSONDecodeError as e:
        print(f"❌ {f}: JSON parse error: {e}")
        invalid += 1
        continue

    errors, warnings = validate(data, f)
    if errors:
        print(f"❌ {f}: {len(errors)} errors")
        for e in errors:
            print(f"     {e}")
        invalid += 1
    else:
        status = f"⚠️  {len(warnings)} warnings" if warnings else "✅"
        print(f"{status} {f}")
        valid += 1

print(f"\n{'='*60}")
print(f"Total: {total} | Valid: {valid} | Invalid: {invalid}")
if invalid > 0:
    sys.exit(1)
