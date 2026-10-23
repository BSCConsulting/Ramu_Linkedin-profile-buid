"""
Content generator for Ramu Munugoti's LinkedIn presence.
Supports both template-synthesized generation and optional LLM API calls.
"""

import os
import json
import random
from datetime import datetime
from agent_core.persona import RAMU_DOSSIER
from agent_core.pillars import PILLARS

TEMPLATES = {
    "pillar_1_csr_sroi": [
        """In the CSR and development sector, there is a dangerous vanity metric that too many boards still settle for:

"Number of beneficiaries reached."

Reaching a beneficiary is an input. It is not an outcome. And it certainly isn't impact.

Over the past decade managing public and corporate allocations exceeding ₹45 Crores, here is the framework we used to transition from superficial reach to an audited 4.8x Social Return on Investment (SROI):

1. The "Zero-Phantom" Rule:
If a beneficiary’s participation cannot be verified through Aadhaar-enabled telemetry or GPS-tagged field data (ODK/KoboToolbox), it does not enter our reporting dashboard. Paper attendance registers belong in the 1990s.

2. Economic Self-Sufficiency over One-Time Handouts:
Providing a subsidised asset (like a solar micro-irrigation pump or vocational certificate) is only stage one. True ROI is measured 12 months later: Did net household income rise? Did local mandi price realization improve?

3. Total Audit Transparency:
Public and corporate capital demands the same fiduciary precision as institutional equity. Across 5 years of central skilling operations across 33 districts, maintaining 100% clean Comptroller & Auditor General (CAG) clearance required treating every rupee as an investment with an auditable milestone.

Corporate boards don’t need more glossy brochures with smiling faces. They need rigorous, quantifiable, data-backed social impact.

How does your organization audit long-term social return on investment? Let's discuss in the comments.

#CSR #SocialImpact #SROI #PublicPolicy #Governance #RamuMunugoti""",

        """Most corporate CSR committees view compliance as a burden under Section 135.

High-impact leaders view it as patient capital for nation-building.

Having structured CSR and livelihood portfolios across 59 districts of Southern India, here are three things that separate transformative CSR from wasted budgets:

1. Theory of Change Must Include Market Realities:
Training 5,000 rural youth without pre-negotiating corporate placement MoUs is a waste of capital. In our MoSDE/NSDC programs, we never inaugurated a batch without locking in minimum 70% placement agreements with industry partners.

2. Infrastructure Sizing Requires Engineering Rigor:
If you are funding solar micro-irrigation or farm processing centers, mechanical sizing matters. A pump mismatched to seasonal water table depths chokes smallholder yields. Engineering precision is social responsibility.

3. Institutional Sustainability (Beyond the Grant):
The best CSR interventions make themselves obsolete within 36 months by turning rural collectives (FPOs and self-help federations) into bankable, profitable commercial entities.

If your CSR capital leaves when the funding cycle ends, you haven't built resilience. You’ve only built dependency.

What is the biggest operational roadblock in your CSR deployments?

#CSR #SocialResponsibility #ImpactInvesting #RuralDevelopment #PublicPolicy"""
    ],

    "pillar_2_fpo_livelihoods": [
        """Federating 50+ Farmer Producer Organizations (FPOs) across 59 districts taught me one brutal truth:

An FPO is not a charity. It is a commercial rural enterprise.

When government schemes or donor funds treat FPOs as passive subsidy recipients, they collapse the moment working capital support expires.

To deliver a sustained 24% increase in net farmer price realization across 20,000+ farm holdings, we enforced three non-negotiable operational principles:

1. Commodity Aggregation Before Market Entry:
Individual smallholders holding 1-2 acres have zero bargaining power with large institutional buyers. Clustered aggregation at the mandal and district level created bulk volumes that bypassed predatory middlemen.

2. Infrastructure Sizing (Hardware Reality):
You cannot scale horticultural value chains without cold-chain storage and primary grading assets. As a mechanical engineer, I worked directly on sizing decentralized solar cold rooms and micro-irrigation pumps to ensure the machinery matched local power availability and crop harvest cycles.

3. Institutional Credit Linkages:
FPOs need timely credit lines for harvest-season procurement. Building formal balance sheets and credit histories unlocked institutional financing from NABARD and regional commercial banks, replacing informal high-interest debt.

Rural development doesn't happen through theoretical workshops. It happens through cold-chain logistics, balance-sheet discipline, and fair market access.

What is the single biggest operational bottleneck your agribusiness teams face in field aggregation?

#RuralDevelopment #Agribusiness #FPO #Livelihoods #SupplyChain #Agriculture #RamuMunugoti""",

        """Why do 70% of Farmer Producer Organizations (FPOs) struggle to survive beyond Year 3?

It is rarely due to farmer unwillingness. It is almost always a failure of "working capital liquidity."

Smallholder farmers cannot wait 45 days for invoice reconciliation from urban buyers. They have immediate cash requirements for fertilizers, seeds, and household expenses.

When we scaled 50+ FPOs across Telangana and Andhra Pradesh, here is how we solved the cashflow crunch:

• Warehouse Receipt Financing:
Connecting local FPO godowns with institutional warehouse receipt systems allowed farmers to deposit produce, receive 70% immediate credit against pledge, and sell when mandi rates peaked.

• Digital Quality Grading at the Gate:
Eliminated quality disputes with buyers by introducing standardized moisture meters and digital grading at collection points. 

• Diversified Revenue Streams (Custom Hiring Centers):
Equipping FPOs with farm machinery and solar irrigation assets that generate leasing revenue during non-harvest seasons.

When you treat smallholders as equity partners in a business rather than recipients of aid, the entire rural economy shifts.

#Agribusiness #FarmerProducerCompany #FPO #Livelihoods #RuralEconomy #ImpactLeadership"""
    ],

    "pillar_3_public_policy": [
        """The anatomy of a ₹45 Crore public scheme:

What 5 years at NSDC and 33 District Committees taught me about executing without audit disallowances.

In government systems, good intentions mean nothing without statutory compliance. 

Stewarding multi-crore public budgets across Rajasthan and the Western corridor under MoSDE meant facing scrutiny from State Executive Committees, District Collectors, and the Comptroller & Auditor General (CAG).

Here is how we certified 45,000+ candidates while maintaining a 100% clean audit record with zero adverse remarks:

1. Reconciliation on Day Zero (PFMS Mastery):
The Public Financial Management System (PFMS) isn't just an accounting tool; it is an anti-leakage shield. Every rupee released to training partners was tied to verifiable Aadhaar-enabled biometric milestones (AEBAS).

2. District Skill Development Plans (DSDPs) Grounded in Industrial Data:
Instead of imposing top-down skilling targets, we convened District Skill Committees chaired by District Collectors. We mapped regional industrial corridors to ensure training matched actual employer vacancies.

3. Aggressive Fraud Elimination:
When field inspections uncovered non-compliance, we acted immediately. Over 5 years, we terminated 6 non-compliant training providers. Protecting public funds requires institutional courage.

4. Deliberate Affirmative Mobilization:
By targeting remote tribal blocks (Baran, Dungarpur, Banswara), we increased female technical training participation by 13 percentage points.

Public systems governance isn't about red tape. It's about designing delivery architectures that deliver honest value to the last citizen.

#PublicPolicy #Governance #SkillIndia #PublicAdministration #CAG #RamuMunugoti""",

        """There is a myth in public administration that speed and statutory compliance cannot co-exist.

"If you follow every rule, the scheme moves at a snail's pace. If you move fast, you risk audit queries."

This is a false trade-off.

Having operated 124+ continuous months in post-Master's governance roles across 59 districts, here is the secret to high-velocity, audit-proof execution:

• Standardized Digital Inspection Telemetry:
Replace multi-page subjective inspection reports with timestamped, geofenced mobile workflows (ODK / KoboToolbox). 

• Parallel Multi-Tier Approvals:
Run technical feasibility, financial vetting, and administrative sanction in synchronized parallel tracks rather than sequential serial handoffs.

• Transparent Partner Scorecards:
Publish monthly performance rankings of all operational partners publicly. Transparency is the single greatest deterrent to compliance slippage.

When public systems are built with engineering precision, they deliver speed AND integrity.

#PublicPolicy #Governance #GoodGovernance #SystemsThinking #Leadership"""
    ],

    "pillar_4_cleantech_ai": [
        """The biggest misconception about PM Surya Ghar (Muft Bijli Yojana) is that customer acquisition is the bottleneck.

It isn't. The bottleneck is the "last-mile grid friction."

Over the past decade working across public systems and clean-tech infrastructure, I’ve seen ambitious schemes encounter the same ground realities:

1. Feeder & Transformer Headroom:
Rooftops are ready to install, but local distribution transformers in semi-urban and rural feeders quickly hit saturation limits. Without real-time feeder telemetry, grid stability becomes a genuine risk.

2. Metering & DISCOM Interconnect Latency:
A 3kW or 5kW system gets physically installed in 48 hours. But the bi-directional net meter inspection, testing, and synchronization with the utility billing portal can take weeks without standardized digital workflows.

3. Working Capital Cycles for Regional EPCs:
Local solar installers operate on thin margins. When subsidy disbursement pipelines experience verification delays, installer cash flows choke, slowing down deployment velocity across the district.

India's target of 1 crore solar rooftops is one of the most visionary energy decentralization policies in the world.

To achieve it at population scale, we don't just need more solar panels; we need systems engineering:
→ Automated, paperless DISCOM grid-sync approvals
→ Predictive feeder load modeling
→ Standardized digital inspection telemetry

Scale isn’t built on enthusiasm. It is built on unglamorous, precision systems execution.

What is the biggest operational hurdle you are witnessing in the rooftop solar roll-out? Let's discuss in the comments.

#SolarEnergy #PMSuryaGhar #CleanEnergy #RenewableEnergy #EnergyTransition #PublicPolicy #RamuMunugoti""",

        """You cannot manage 59 districts with spreadsheets and WhatsApp groups.

Here is how we deployed practical AI and mobile data telemetry across 20,000+ agricultural and energy assets without Silicon Valley budgets:

1. The Problem:
Paper forms and delayed monthly reports meant that broken micro-irrigation pumps or stalling skilling batches were discovered 60 days too late.

2. The Architecture:
• Field Collection: Custom forms built on Open Data Kit (ODK) and KoboToolbox operating offline in remote villages.
• Ingestion & Warehousing: Automated Python pipelines feeding into a centralized SQL database upon reaching cellular connectivity.
• Automated Anomaly Detection: Scripted statistical checks flagging suspicious attendance clusters, GPS mismatches, or abnormal pump run-times.
• Executive Dashboarding: Power BI interfaces providing live operational heatmaps for district collectors and donors.

3. The Business Impact:
• Zero phantom beneficiaries.
• Asset downtime reduced by 35%.
• Reporting turnaround compressed from 30 days to 24 hours.

AI in the impact sector isn't about generative avatars. It's about data integrity, automated anomaly detection, and real-time operational truth.

#AI #DataAnalytics #Telemetry #Operations #CleanTech #Leadership"""
    ]
}


def generate_weekly_batch(output_dir="drafts"):
    """
    Generates a full week of 4 high-authority posts (one per pillar),
    saving them as Markdown and JSON files ready for review.
    """
    os.makedirs(output_dir, exist_ok=True)
    today = datetime.now()
    week_str = today.strftime("%Y_W%W")
    
    posts = []
    
    pillar_keys = [
        "pillar_1_csr_sroi",
        "pillar_2_fpo_livelihoods",
        "pillar_3_public_policy",
        "pillar_4_cleantech_ai"
    ]
    
    days = ["Tuesday 8:30 AM IST", "Wednesday 8:30 AM IST", "Thursday 8:30 AM IST", "Saturday 11:00 AM IST"]
    
    for idx, key in enumerate(pillar_keys):
        pillar_info = PILLARS[key]
        post_content = random.choice(TEMPLATES[key])
        
        post_obj = {
            "day_slot": days[idx],
            "pillar_id": key,
            "pillar_title": pillar_info["title"],
            "target_audience": pillar_info["audience"],
            "content": post_content,
            "status": "pending_approval"
        }
        posts.append(post_obj)
        
    # Write JSON
    json_path = os.path.join(output_dir, f"batch_{week_str}.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)
        
    # Write Markdown summary
    md_path = os.path.join(output_dir, f"batch_{week_str}.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# Ramu Munugoti — Weekly Authority Post Schedule ({week_str})\n\n")
        f.write("> **Weekly Target:** Build public trust across CSR, FPOs, Public Policy & Clean Tech.\n\n---\n\n")
        
        for i, p in enumerate(posts, start=1):
            f.write(f"## Post {i}: {p['pillar_title']}\n")
            f.write(f"**Recommended Time:** `{p['day_slot']}`  \n")
            f.write(f"**Target Audience:** *{p['target_audience']}*  \n\n")
            f.write("```text\n")
            f.write(p["content"])
            f.write("\n```\n\n---\n\n")
            
    return md_path, json_path, posts
