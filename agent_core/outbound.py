"""
Outbound Assistant: Generates high-signal executive comments and non-spammy connection notes.
Supports Move A (Multilateral/USAID), Move B (CSR Peers), Move C (Headhunters), and Tier 1 Operational Leads.
"""

def generate_connection_note(target_type: str, recipient_name: str, org_name: str) -> str:
    """
    Generates a high-converting, personalized LinkedIn connection note (under 300 characters).
    """
    recipient_first = recipient_name.split()[0] if recipient_name else "there"
    
    if target_type.lower() == "csr":
        # Move B: CSR & Social Impact Peer Exchange
        note = (
            f"Hi {recipient_first}, following your impact work at {org_name}. "
            f"Over the last decade managing ₹45Cr+ in public & CSR allocations (TISS M.A. + B.Tech), "
            f"we've focused on 4.8x verified SROI and telemetry across 59 districts. "
            f"Would value connecting with a fellow sector leader."
        )
    elif target_type.lower() == "multilateral":
        # Move A: USAID / World Bank / Bilateral RFP Partners (Named Key Personnel)
        note = (
            f"Hi {recipient_first}, appreciate your leadership on {org_name}'s development portfolio. "
            f"With 124+ months unbroken post-PG leadership (TISS Mumbai + B.Tech) across 50+ FPOs & 45K livelihoods, "
            f"I frequently advise on large-scale field delivery. Would value connecting."
        )
    elif target_type.lower() == "headhunter":
        # Move C: Executive Search Partner
        note = (
            f"Hi {recipient_first}, following your executive placements in the impact and energy space. "
            f"I lead large-scale rural development, public policy, and clean-tech programs (ex-NSDC State Lead, TISS + B.Tech). "
            f"Glad to connect and stay in touch for senior leadership opportunities."
        )
    elif target_type.lower() == "solarenergy":
        # Solar / PM Surya Ghar / Clean Energy Lead
        note = (
            f"Hi {recipient_first}, following {org_name}'s clean energy footprint. "
            f"As a mechanical engineer & public systems lead working on PM Surya Ghar and rural decentralized infrastructure, "
            f"I follow your updates with great interest. Would value connecting as peers."
        )
    else:
        # Default Tier 1 Operational Peer
        note = (
            f"Hi {recipient_first}, really respect your work at {org_name}. "
            f"Having spent 15+ years leading large-scale livelihoods, FPO federations, and public policy delivery across 59 districts, "
            f"I always look to connect with high-impact operators. Glad to connect."
        )
        
    return note


def generate_high_signal_comment(theme: str) -> str:
    """
    Generates an authoritative, value-add comment to drop on industry leaders' posts.
    """
    comments = {
        "csr_sroi": (
            "Spot on perspective. One critical observation we've seen on the ground across 59 districts: "
            "the moment an organization moves from measuring 'beneficiaries reached' to 'audited SROI (Social Return on Investment)', "
            "the entire intervention design sharpens. Fiduciary accountability and digital field telemetry "
            "are the true enablers of lasting social impact."
        ),
        "fpo_aggregation": (
            "Completely agree. An FPO cannot survive as a subsidized entity—it must be treated as a commercial enterprise. "
            "In our work federating 50+ FPOs and 20,000+ farmers, we found that combining pre-harvest commodity aggregation "
            "with localized cold-chain hardware delivered a verified 24% boost in net price realization. "
            "Market linkage and balance-sheet discipline are the real game changers."
        ),
        "solar_grid": (
            "Crucial insight. In PM Surya Ghar and decentralized solar, the core operational hurdle is rarely rooftop demand; "
            "it is distribution transformer headroom and DISCOM net-metering synchronization. "
            "Without predictive load telemetry and paperless utility interconnection, deployment velocity chokes. "
            "Systems engineering must meet ground-level policy execution."
        ),
        "public_policy": (
            "Couldn't agree more. Speed in public schemes doesn't require sacrificing statutory rigor. "
            "During my 5 years at NSDC managing ₹45Cr+ across 33 districts, maintaining 100% clean CAG audit clearance "
            "boiled down to one rule: zero-phantom telemetry (biometric/GPS verification) tied directly to PFMS fund releases. "
            "Integrity and scale can go hand in hand."
        )
    }
    return comments.get(theme, comments["csr_sroi"])
