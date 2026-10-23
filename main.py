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
    Generates a standalone, beautiful HTML dashboard to view, edit,
    and 1-click copy weekly posts and outbound messages.
    """
    # Ensure drafts exist
    md_path, json_path, posts = generate_weekly_batch()
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ramu Munugoti — LinkedIn Executive Authority Desk</title>
    <style>
        :root {{
            --bg: #0b132b;
            --surface: #1c2541;
            --surface-hover: #263359;
            --primary: #3a86ff;
            --accent: #10b981;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --border: #334155;
            --card-radius: 12px;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
        body {{ background: var(--bg); color: var(--text-main); min-height: 100vh; padding: 32px 20px; }}
        .container {{ max-width: 1080px; margin: 0 auto; }}
        header {{ margin-bottom: 32px; border-bottom: 1px solid var(--border); padding-bottom: 24px; }}
        h1 {{ font-size: 26px; font-weight: 700; color: #fff; margin-bottom: 8px; }}
        .subtitle {{ font-size: 15px; color: var(--text-muted); }}
        .badge-row {{ display: flex; gap: 10px; margin-top: 14px; flex-wrap: wrap; }}
        .badge {{ background: rgba(58, 134, 255, 0.15); color: #60a5fa; border: 1px solid rgba(58, 134, 255, 0.3); padding: 4px 10px; border-radius: 6px; font-size: 12px; font-weight: 600; }}
        .badge.green {{ background: rgba(16, 185, 129, 0.15); color: #34d399; border-color: rgba(16, 185, 129, 0.3); }}
        
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(480px, 1fr)); gap: 24px; margin-top: 24px; }}
        .card {{ background: var(--surface); border: 1px solid var(--border); border-radius: var(--card-radius); padding: 22px; display: flex; flex-direction: column; justify-content: space-between; }}
        .card-header {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 14px; }}
        .card-title {{ font-size: 17px; font-weight: 600; color: #fff; }}
        .card-tag {{ font-size: 12px; color: var(--accent); font-weight: 600; }}
        .meta-info {{ font-size: 13px; color: var(--text-muted); margin-bottom: 14px; }}
        
        .post-body {{ background: #0f172a; border: 1px solid var(--border); border-radius: 8px; padding: 14px; color: #cbd5e1; font-size: 13.5px; line-height: 1.6; white-space: pre-wrap; margin-bottom: 16px; max-height: 280px; overflow-y: auto; }}
        .btn-copy {{ background: var(--primary); color: #fff; border: none; border-radius: 6px; padding: 10px 16px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s; align-self: flex-start; }}
        .btn-copy:hover {{ background: #2563eb; transform: translateY(-1px); }}
        .btn-copy:active {{ transform: translateY(0); }}

        .outbound-section {{ margin-top: 48px; background: var(--surface); border: 1px solid var(--border); border-radius: var(--card-radius); padding: 24px; }}
        .outbound-title {{ font-size: 18px; font-weight: 600; margin-bottom: 14px; }}
        .outbound-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin-top: 16px; }}
        .outbound-box {{ background: #0f172a; border: 1px solid var(--border); border-radius: 8px; padding: 14px; }}
        .outbound-box h4 {{ color: #60a5fa; font-size: 14px; margin-bottom: 8px; }}
        .outbound-text {{ font-size: 12.5px; color: #cbd5e1; line-height: 1.5; margin-bottom: 12px; }}
        .copied-toast {{ display: none; position: fixed; bottom: 20px; right: 20px; background: var(--accent); color: #042f2e; padding: 10px 18px; border-radius: 6px; font-weight: 700; font-size: 13px; }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Ramu Munugoti — LinkedIn Authority Desk</h1>
            <div class="subtitle">Omni-Sector Program Director & Public Systems Executive (Rural Livelihoods | CSR | Public Policy | Clean Tech)</div>
            <div class="badge-row">
                <span class="badge green">₹45Cr+ Public Budget (100% CAG Clearance)</span>
                <span class="badge">45,000+ Livelihoods Certified</span>
                <span class="badge">50+ FPOs & 20,000+ Farmers</span>
                <span class="badge green">4.8x Audited SROI</span>
                <span class="badge">TISS Mumbai (M.A.) + B.Tech Mechanical</span>
            </div>
        </header>

        <h2 style="font-size: 19px; font-weight: 600; color: #f1f5f9;">Weekly Post Queue (4 Strategic Pillars)</h2>
        <div class="grid">
"""
    for i, p in enumerate(posts, 1):
        content_escaped = p["content"].replace('`', '\\`').replace('"', '&quot;')
        html_content += f"""
            <div class="card">
                <div>
                    <div class="card-header">
                        <div class="card-title">Post {i}: {p['pillar_title']}</div>
                    </div>
                    <div class="meta-info">
                        <strong>Slot:</strong> {p['day_slot']} &nbsp;|&nbsp; <strong>Target:</strong> {p['target_audience']}
                    </div>
                    <div class="post-body" id="post-{i}">{p['content']}</div>
                </div>
                <button class="btn-copy" onclick="copyPost('post-{i}')">📋 1-Click Copy Post {i}</button>
            </div>
        """

    # Add Outbound Tools section
    sample_csr_note = generate_connection_note("csr", "Target Leader", "Tata Trusts / Adani Foundation")
    sample_multi_note = generate_connection_note("multilateral", "Mission Director", "USAID / World Bank")
    sample_solar_note = generate_connection_note("solarenergy", "Chief Executive", "Tata Power Solar / Clean Energy")

    html_content += f"""
        </div>

        <div class="outbound-section">
            <div class="outbound-title">Direct Outbound Pipeline (High-Converting Connection Notes)</div>
            <div class="subtitle">Use these tailored notes (under 300 characters) when connecting with target decision-makers:</div>
            
            <div class="outbound-grid">
                <div class="outbound-box">
                    <h4>Move B: Heads of CSR & Foundation Leaders</h4>
                    <div class="outbound-text" id="note-csr">{sample_csr_note}</div>
                    <button class="btn-copy" onclick="copyPost('note-csr')">Copy CSR Note</button>
                </div>
                
                <div class="outbound-box">
                    <h4>Move A: Multilateral & USAID Proposal Leads</h4>
                    <div class="outbound-text" id="note-multi">{sample_multi_note}</div>
                    <button class="btn-copy" onclick="copyPost('note-multi')">Copy Multilateral Note</button>
                </div>
                
                <div class="outbound-box">
                    <h4>Clean Tech & Solar Energy Executives</h4>
                    <div class="outbound-text" id="note-solar">{sample_solar_note}</div>
                    <button class="btn-copy" onclick="copyPost('note-solar')">Copy CleanTech Note</button>
                </div>
            </div>
        </div>
    </div>

    <div class="copied-toast" id="toast">Copied to Clipboard!</div>

    <script>
        function copyPost(elementId) {{
            const text = document.getElementById(elementId).innerText;
            navigator.clipboard.writeText(text).then(() => {{
                const toast = document.getElementById('toast');
                toast.style.display = 'block';
                setTimeout(() => {{ toast.style.display = 'none'; }}, 2200);
            }});
        }}
    </script>
</body>
</html>
"""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    return output_file


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
        print("  python3 main.py comment         (Generates authoritative comment for industry posts)\n")

if __name__ == "__main__":
    main()
