#!/usr/bin/env python3
"""
Ramu Munugoti — LinkedIn Authority & Opportunity Agent
Main CLI and Orchestrator.
"""

import sys
import os
import argparse
from agent_core.generator import generate_weekly_batch
from agent_core.outbound import generate_connection_note, generate_high_signal_comment

def build_interactive_dashboard(output_file="dashboard.html"):
    """
    Synchronizes The Executive Desk master application (index.html)
    and ensures fresh weekly intelligence drafts exist.
    """
    import shutil
    base_dir = os.path.dirname(os.path.abspath(__file__))
    master_index = os.path.join(base_dir, "index.html")
    dest_path = os.path.join(base_dir, output_file)

    # Ensure weekly drafts exist
    generate_weekly_batch()

    if os.path.exists(master_index) and master_index != dest_path:
        shutil.copyfile(master_index, dest_path)
    return dest_path



def main():
    parser = argparse.ArgumentParser(description="Ramu Munugoti — LinkedIn Authority & Opportunity Agent")
    subparsers = parser.add_subparsers(dest="command", help="Available Commands")

    # Command: generate-week
    gen_parser = subparsers.add_parser("generate-week", help="Generate a fresh weekly batch of 4 authority posts")
    gen_parser.add_argument("--outdir", default="drafts", help="Output directory for drafts")

    # Command: dashboard
    dash_parser = subparsers.add_parser("dashboard", help="Generate and update the interactive HTML dashboard")
    dash_parser.add_argument("--output", default="dashboard.html", help="Dashboard HTML file path")

    # Command: outbound-note
    note_parser = subparsers.add_parser("outbound-note", help="Generate a personalized connection note")
    note_parser.add_argument("--type", choices=["csr", "multilateral", "headhunter", "solarenergy", "general"], default="csr")
    note_parser.add_argument("--name", default="Director", help="Recipient full name")
    note_parser.add_argument("--org", default="Organization", help="Recipient organization name")

    # Command: comment
    comm_parser = subparsers.add_parser("comment", help="Generate an authoritative comment for target posts")
    comm_parser.add_argument("--theme", choices=["csr_sroi", "fpo_aggregation", "solar_grid", "public_policy"], default="csr_sroi")

    # Command: storage-clean
    clean_parser = subparsers.add_parser("storage-clean", help="Auto-purge drafts, cache, and logs older than 20 days")
    clean_parser.add_argument("--days", type=int, default=20, help="Retention period in days (default: 20)")

    args = parser.parse_args()

    if args.command == "generate-week":
        md_path, json_path, posts = generate_weekly_batch(args.outdir)
        print(f"\n[SUCCESS] Weekly batch successfully generated!")
        print(f" -> Markdown: {md_path}")
        print(f" -> JSON:     {json_path}")
        print(f" -> Total Posts: {len(posts)}")
        print("\nTo open your visual review desk, run: python3 main.py dashboard\n")

    elif args.command == "dashboard":
        dash_file = build_interactive_dashboard(args.output)
        abs_path = os.path.abspath(dash_file)
        print(f"\n[SUCCESS] Interactive Dashboard generated at:")
        print(f" -> file://{abs_path}")
        print("\nYou can open this file in any web browser to review and 1-click copy your posts.\n")

    elif args.command == "outbound-note":
        note = generate_connection_note(args.type, args.name, args.org)
        print(f"\n--- Tailored LinkedIn Connection Note ({len(note)} chars / max 300) ---")
        print(note)
        print("--------------------------------------------------------------------\n")

    elif args.command == "comment":
        comment = generate_high_signal_comment(args.theme)
        print(f"\n--- High-Signal Thought Leadership Comment ---")
        print(comment)
        print("----------------------------------------------\n")

    elif args.command == "storage-clean":
        from agent_core.storage_manager import purge_stale_files
        res = purge_stale_files(max_age_days=args.days)
        print(f"\n[STORAGE CLEANUP] {args.days}-Day Retention Rule Enforced:")
        print(f" -> Files Purged: {res['purged_count']}")
        print(f" -> Space Freed: {res['freed_kb']} KB\n")

    else:
        # Default behavior: generate dashboard and summary
        dash_file = build_interactive_dashboard()
        abs_path = os.path.abspath(dash_file)
        print("\n=== Ramu Munugoti LinkedIn Agent CLI ===")
        print(f"[READY] Visual Authority Dashboard generated at: file://{abs_path}")
        print("Available subcommands:")
        print("  python3 main.py generate-week   (Generates 4 weekly authority posts)")
        print("  python3 main.py dashboard       (Builds interactive HTML review desk)")
        print("  python3 main.py outbound-note   (Generates 1-click tailored connection note)")
        print("  python3 main.py comment         (Generates authoritative comment for industry posts)")
        print("  python3 main.py storage-clean   (Auto-purges stale drafts & caches older than 20 days)\n")

if __name__ == "__main__":
    main()
