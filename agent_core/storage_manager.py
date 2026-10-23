#!/usr/bin/env python3
"""
Storage & Memory Hygiene Manager for The Executive Desk.
Enforces a strict 20-day Time-To-Live (TTL) retention policy across:
1. Generated weekly drafts (drafts/)
2. Log files and temporary artifacts
3. Bytecode cache directories (__pycache__)
"""

import os
import sys
import time
import argparse
from pathlib import Path

DEFAULT_MAX_AGE_DAYS = 20
SECONDS_PER_DAY = 86400

TARGET_DIRECTORIES = [
    "drafts",
    "logs",
    ".cache",
    "agent_core/__pycache__"
]

def purge_stale_files(max_age_days=DEFAULT_MAX_AGE_DAYS, base_dir=None):
    """
    Scans target directories and purges files older than max_age_days.
    Returns a summary dict of actions taken.
    """
    if base_dir is None:
        base_dir = Path(__file__).resolve().parent.parent
    else:
        base_dir = Path(base_dir).resolve()

    cutoff_timestamp = time.time() - (max_age_days * SECONDS_PER_DAY)
    purged_files = []
    freed_bytes = 0

    for rel_dir in TARGET_DIRECTORIES:
        target_path = base_dir / rel_dir
        if not target_path.exists():
            continue

        for item in target_path.rglob("*"):
            if item.is_file():
                try:
                    mtime = item.stat().st_mtime
                    if mtime < cutoff_timestamp:
                        file_size = item.stat().st_size
                        item.unlink()
                        purged_files.append(str(item.relative_to(base_dir)))
                        freed_bytes += file_size
                except OSError as err:
                    print(f"[WARN] Could not inspect/remove {item}: {err}")

    # Clean up empty directories inside target paths if any
    for rel_dir in TARGET_DIRECTORIES:
        target_path = base_dir / rel_dir
        if target_path.exists() and target_path.is_dir():
            for p in sorted(target_path.glob("**/*"), reverse=True):
                if p.is_dir() and not any(p.iterdir()):
                    try:
                        p.rmdir()
                    except OSError:
                        pass

    freed_kb = round(freed_bytes / 1024, 2)
    return {
        "max_age_days": max_age_days,
        "purged_count": len(purged_files),
        "freed_kb": freed_kb,
        "purged_files": purged_files
    }

def main():
    parser = argparse.ArgumentParser(description="Storage Hygiene & 20-Day Auto-Purge Manager")
    parser.add_argument("--days", type=int, default=DEFAULT_MAX_AGE_DAYS, help="Maximum age in days before auto-deletion (default: 20)")
    parser.add_argument("--dir", type=str, default=None, help="Base project directory")
    args = parser.parse_args()

    print(f"=== The Executive Desk: Storage & Memory Hygiene ===")
    print(f"Scanning for files older than {args.days} days...")
    result = purge_stale_files(max_age_days=args.days, base_dir=args.dir)

    print(f"[SUMMARY] Enforced {result['max_age_days']}-Day Retention:")
    print(f"  • Files Purged: {result['purged_count']}")
    print(f"  • Storage Freed: {result['freed_kb']} KB")
    if result["purged_files"]:
        print("  • Removed Items:")
        for f in result["purged_files"]:
            print(f"     - {f}")
    else:
        print("  • System Status: All storage pristine and within 20-day limit.")

if __name__ == "__main__":
    main()
