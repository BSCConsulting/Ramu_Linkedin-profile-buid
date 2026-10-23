"""
Outbound Assistant: Generates high-signal, peer-to-peer executive messages under 300 characters.
Includes dedicated channels for:
- UNDP & Multilateral Teams
- UKWDP (Uttarakhand Workforce / Watershed Development Project - World Bank)
- Uttarakhand Skill Development Mission (UKSDM) & State Directors
- TISS Mumbai Alumni in CSR & Foundations
- JNTU Engineering Alumni in Clean Energy
- Corporate CSR Heads & Executive Search
"""

def generate_connection_note(target_type: str, recipient_name: str, org_name: str = "") -> str:
    """
    Generates a personalized, peer-to-peer connection note (strictly under 300 characters).
    """
    fName = recipient_name.split()[0] if recipient_name else "there"
    t = target_type.lower()
    
    if t == "undp":
        # UNDP Leadership & Program Leads
        note = (
            f"Hi {fName}, following UNDP's livelihoods & climate resilience initiatives with great respect. "
            f"With 10+ yrs post-PG leadership across 50+ FPOs, clean-tech, and state skilling (TISS M.A. + B.Tech), "
            f"I frequently exchange notes on large field delivery. Glad to connect."
        )
    elif t == "ukwdp":
        # UKWDP (Uttarakhand Workforce / Watershed Project - World Bank)
        note = (
            f"Hi {fName}, following UKWDP's World Bank-supported workforce and watershed work. "
            f"Having managed ₹45Cr+ in state skilling ops and rural infrastructure across 59 districts (TISS + B.Tech), "
            f"I follow your project milestones with great interest. Would value staying connected."
        )
    elif t == "uksdm":
        # Uttarakhand Skill Development Mission / Department
        note = (
            f"Hi {fName}, following UKSDM's skilling initiatives in Uttarakhand. "
            f"As ex-State Head at NSDC (MoSDE) managing 33 District Committees and 45K+ certifications with clean CAG audits, "
            f"I always look to connect with state skilling leaders. Would be glad to connect."
        )
    elif t == "tiss":
        # Fellow TISS Alumni in CSR, Foundations, Multilaterals
        note = (
            f"Hi {fName}, great to connect with a fellow TISS alumnus! (M.A. Rural Development, 2016). "
            f"Over the last decade I've led state skilling under NSDC and federated 50+ FPOs across 59 districts. "
            f"Always inspiring to see alumni driving real impact across the sector. Let's stay in touch."
        )
    elif t == "jntu":
        # JNTU Engineering Alumni in Energy & Infrastructure
        note = (
            f"Hi {fName}, great to connect with a fellow JNTU engineer! "
            f"I've spent the last 15 years applying mechanical systems rigor to decentralized solar, micro-irrigation, and public governance. "
            f"Always glad to expand the alumni network with peers in energy and infrastructure."
        )
    elif t == "csr":
        # Corporate CSR Heads (Move B)
        note = (
            f"Hi {fName}, saw your recent work with {org_name or 'the foundation'}. "
            f"Over the last decade leading large skilling & rural programs (TISS Mumbai + B.Tech), "
            f"we've focused heavily on 4.8x verified SROI and field telemetry across 59 districts. "
            f"Would be great to stay connected as fellow sector practitioners."
        )
    elif t == "search":
        # Executive Search Partners (Move C)
        note = (
            f"Hi {fName}, noticed your executive search focus in social impact and energy. "
            f"I lead large-scale rural development, public policy, and clean-tech operations (ex-NSDC State Lead, TISS + B.Tech). "
            f"Glad to connect and keep in touch for senior leadership mandates."
        )
    elif t == "solar":
        # Solar & Clean Tech Executives
        note = (
            f"Hi {fName}, following {org_name or 'your team'}'s clean energy footprint. "
            f"As an engineer working on PM Surya Ghar and rural decentralized infrastructure, "
            f"I follow your updates with great interest. Would value connecting as peers."
        )
    else:
        # Default Peer
        note = (
            f"Hi {fName}, really respect the work you're driving at {org_name or 'your organization'}. "
            f"Having spent 15+ years managing large-scale livelihoods, FPO federations, and public policy delivery across 59 districts, "
            f"I always look to connect with solid operators. Glad to connect."
        )
        
    return note
