"""
Thematic Streams Engine for The Executive Desk.
Curates intelligence across 4 dedicated role-targeted streams:
1. Tuesday: CSR & Corporate Philanthropy (MCA, Tata Trusts, Azim Premji)
2. Wednesday: Agribusiness & Rural Livelihoods (NABARD, SFAC, UN FAO)
3. Thursday: Public Policy & State Systems (NITI Aayog, MoSDE, CPR)
4. Saturday: Clean Energy & Multilateral Transition (CEEW, ISA, World Bank, MNRE)
"""

import json
import os
from datetime import datetime

THEMATIC_STREAMS = [
    {
        "stream_id": "stream_tuesday_csr",
        "day_slot": "Tuesday 8:30 AM IST",
        "theme_title": "CSR, Philanthropy & ESG Governance",
        "institutions": ["Ministry of Corporate Affairs (MCA)", "Tata Trusts", "Azim Premji Foundation"],
        "target_audience": "Corporate Boards, CSR Committee Chairs, ESG Fund Trustees",
        "ground_friction": "Most corporate CSR boards evaluate success based on one-time disbursement and beneficiary headcount, rather than verified 12-month post-intervention economic retention.",
        "draft_post": """Whenever I review CSR impact presentations, I look for one specific slide:

What happened to the beneficiaries 12 months after the funding ended?

Most of the time, that slide doesn't exist. Instead, you get big numbers: "5,000 youth trained" or "2,000 women mobilised." 

That tells you money was spent. It doesn't tell you if anybody's life actually changed.

During my five years handling state operations at NSDC, we managed over ₹45 Crores in public skilling funds across 33 districts. The biggest lesson wasn't about mobilization; it was about follow-through.

We put three practical rules in place:

First, we stopped accepting paper attendance. If a student wasn't clocking in through biometric attendance, the training partner didn't get reimbursed. It sounded harsh to some providers, but it wiped out ghost candidates overnight.

Second, we stopped funding courses without pre-signed industry placement agreements. If local employers hadn't committed to hiring at least 70% of the batch, the batch didn't start.

Third, in our recent work with 50+ Farmer Producer Organizations in Telangana and Andhra, we measured social return on investment (SROI) by checking farmer price realization at the local mandi 12 months later. We saw an audited 24% price jump because we linked them directly to bulk buyers and decentralized cold rooms.

Real impact is unglamorous. It lives in attendance logs, cold storage maintenance, and bank transaction statements.

If your CSR reports don't track what happens 12 months post-intervention, you aren't measuring impact—you're just measuring disbursement.

Curious to hear from other CSR heads: how do you track candidate retention after year one?

#CSR #SocialImpact #SROI #CorporateGovernance #MCA #Section135 #RamuMunugoti""",
        "char_count": 1280,
        "read_time": "1.5 min read"
    },
    {
        "stream_id": "stream_wednesday_agri",
        "day_slot": "Wednesday 8:30 AM IST",
        "theme_title": "Agribusiness & Rural Livelihood Federations",
        "institutions": ["NABARD", "SFAC", "UN FAO", "Ministry of Agriculture (MoAFW)"],
        "target_audience": "Agribusiness CEOs, NABARD Leadership, Rural Livelihood Mission Directors",
        "ground_friction": "Smallholders sell at distressed mandi discounts because FPOs lack working capital liquidity during harvest week. Warehouse receipt lines and cold chain hardware are mandatory.",
        "draft_post": """A lot of people think farmer producer companies (FPOs) fail because farmers don't want to cooperate.

That hasn't been my experience on the ground.

Working across 50+ FPOs and 20,000+ farmers in Andhra Pradesh and Telangana, the single biggest reason an FPO stalls in its second year is simple: working capital timing.

A smallholder farmer with two acres cannot wait three weeks for an institutional buyer to reconcile an invoice and release NEFT payments. They have immediate diesel expenses, fertilizer dues, and household needs. If the FPO cannot pay on the day of harvest, the farmer will sell to the local mandi trader at a 15% discount just to get cash in hand.

To fix this, we stopped treating FPOs like social projects and started running them like supply chain businesses:

1. We clustered smallholder produce at the mandal level to build bulk volumes that large food processors couldn't ignore.
2. We sized decentralized solar cold rooms so farmers weren't forced to distress-sell perishable produce on day one.
3. We set up working capital credit lines with NABARD and regional banks backed by warehouse receipts, so the FPO could pay farmers within 48 hours.

The result was a verified 24% increase in what farmers actually took home.

An FPO is not a charity. It's a rural enterprise. If you don't solve the farmer's day-one cashflow, no amount of training workshops will keep the company alive.

Has anyone else working with producer companies found a reliable way to solve the harvest-week working capital gap?

#Agribusiness #RuralDevelopment #FPO #NABARD #Livelihoods #SupplyChain #RamuMunugoti""",
        "char_count": 1340,
        "read_time": "1.6 min read"
    },
    {
        "stream_id": "stream_thursday_policy",
        "day_slot": "Thursday 8:30 AM IST",
        "theme_title": "Public Policy & State Systems Convergence",
        "institutions": ["NITI Aayog", "MoSDE", "Centre for Policy Research (CPR)", "CAG"],
        "target_audience": "District Collectors, State Principal Secretaries, Multilateral Mission Directors",
        "ground_friction": "Public program execution stalls when statutory compliance is treated as a post-facto audit hurdle rather than a day-zero operational architecture.",
        "draft_post": """There's an old assumption in public administration that you have to choose between speed and audit compliance.

"If you follow every rule, work stalls. If you move fast, you'll get CAG audit queries."

I don't buy that.

Over 5 years heading state operations for central skilling schemes (PMKVY, DDU-GKY) under MoSDE, our office handled ₹45+ Crores across 33 districts. When the Comptroller & Auditor General (CAG) and statutory auditors conducted their reviews, we had zero adverse remarks or financial disallowances.

We didn't achieve that by slowing down. We certified over 45,000 candidates.

What made the difference was setting up clean systems early:

1. Daily PFMS Tracking: We treated the Public Financial Management System not as a year-end compliance headache, but as our daily operational compass. Every disbursement was mapped to verified milestones.
2. Field Telemetry: We replaced paper inspection sheets with geotagged mobile reports. You couldn't fake an inspection because the photos had embedded timestamps and coordinates.
3. Quick Action on Violations: When center inspections revealed proxy attendances, we didn't look away. Over five years, we terminated six non-compliant training centers. When word got out that standards were non-negotiable, compliance improved across the entire state.
4. Focus on Remote Blocks: We focused our mobilization on tribal and aspirational districts like Dungarpur and Baran, lifting female participation in technical courses by 13%.

Public systems don't fail because people don't care. They fail when reporting latency lets leakages compound over months.

Clean data and field discipline are the best protection any public program can have.

#PublicPolicy #Governance #SkillIndia #NITIAayog #PublicAdministration #CAG #RamuMunugoti""",
        "char_count": 1390,
        "read_time": "1.6 min read"
    },
    {
        "stream_id": "stream_saturday_energy",
        "day_slot": "Saturday 11:00 AM IST",
        "theme_title": "Clean Energy, Solar & Multilateral Transition",
        "institutions": ["CEEW", "International Solar Alliance (ISA)", "World Bank Energy", "MNRE"],
        "target_audience": "Solar EPCs, Cleantech Investors, International Federations, Chief of Party Leads",
        "ground_friction": "Rooftop solar expansion faces physical feeder bottlenecking at the distribution transformer level, while utility net-metering synchronization delays choke installer liquidity.",
        "draft_post": """With PM Surya Ghar (Muft Bijli Yojana), everyone is talking about rooftop acquisition and consumer subsidies.

Those are important, but they aren't where the project actually gets stuck.

As a mechanical engineer who has spent years on decentralized energy and rural systems, here is where solar installations actually stall on the ground:

1. Distribution Transformer Headroom:
You can sign up 50 homes on a residential street in a few days. But if the local 100 kVA or 250 kVA transformer is already running near peak load, injecting reverse solar power during afternoon hours can cause voltage fluctuations. Without transformer load mapping, the local feeder simply cannot take the capacity.

2. Net-Meter Inspection Queues:
The physical installation of solar panels takes about two days. But getting the DISCOM's junior engineer to inspect the site, swap the existing meter for a bi-directional meter, and sync it with utility billing can take weeks. That's cashflow sitting idle on the installer's books.

3. Sizing vs Water Table Reality (in Rural Ag Pumping):
On the farm side, I've seen multiple 3HP and 5HP solar micro-irrigation pumps underperform simply because they were installed without accounting for seasonal water table drop during March-May. Hardware sizing has to match the hydrologic reality, not just the tender document.

PM Surya Ghar is one of the most ambitious energy decentralization programs anywhere.

If we want to hit the one-crore rooftop goal smoothly, the focus needs to shift toward paperless utility interconnects and feeder-level telemetry.

To the solar installers and engineers here: what is your current turnaround time between physical panel mounting and net-meter commissioning?

#SolarEnergy #PMSuryaGhar #CleanEnergy #CEEW #EnergyTransition #WorldBank #RamuMunugoti""",
        "char_count": 1410,
        "read_time": "1.7 min read"
    }
]

def get_thematic_streams():
    return THEMATIC_STREAMS

def export_thematic_streams_json(output_path="drafts/thematic_streams.json"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(THEMATIC_STREAMS, f, indent=2, ensure_ascii=False)
    return output_path
