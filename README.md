# The Executive Desk — Ramu Munugoti
### Autonomous Executive Authority & Multi-Source Intelligence Engine

**Live Platform**: [ramulinkedin-profile-buid.vercel.app](https://ramulinkedin-profile-buid.vercel.app/)  
**GitHub Repository**: [BSCConsulting/Ramu_Linkedin-profile-buid](https://github.com/BSCConsulting/Ramu_Linkedin-profile-buid)

---

## 🏛️ Executive Summary

**The Executive Desk** is an autonomous web application and intelligence agent engineered for **Ramu Munugoti** (Founder, BSC Consulting; B.Tech Mechanical Engineering, JNTU; M.A. Rural Development & Governance, TISS Mumbai; ex-State Operations Lead, NSDC / MoSDE).

The platform serves two unified objectives:
1. **10x Public Trust & LinkedIn Authority**: Autonomous weekly dissemination of ground-tested thought leadership across 4 strategic pillars, eliminating generic AI clichés in favor of real field friction (distribution transformer headroom, net-metering synchronization delays, FPO working capital liquidity, AEBAS biometric attendance, and CAG audit compliance).
2. **Apex & Merit-Based Executive Recruitment**: Driving inbound mandates and proactive outreach for **Senior Executive Leadership, Board Director, Chief of Party, and Practice Lead** roles across Multilaterals (USAID, World Bank, UNDP), Corporate CSR Foundations, Clean Energy conglomerates, and State Missions.

---

## ⚡ Core Architecture & Features

### 1. The 4 Weekly Thematic Streams
Updated autonomously via GitHub Actions cron pipelines (`.github/workflows/weekly_radar_update.yml`):
* **Tuesday (08:30 AM IST)**: Corporate Social Responsibility (CSR), Philanthropy & ESG Governance (MCA Sec 135, Tata Trusts, Azim Premji Foundation).
* **Wednesday (08:30 AM IST)**: Agribusiness, Rural Livelihoods & FPO Federations (NABARD, SFAC, UN FAO).
* **Thursday (08:30 AM IST)**: Public Policy Formulation & State Systems Convergence (NITI Aayog, MoSDE, CAG).
* **Saturday (11:00 AM IST)**: Clean Energy Transition (PM Surya Ghar / Solar), DISCOMs & Telemetry (CEEW, ISA, World Bank).

### 2. Live In-Browser Inline Editing with Instant Auto-Save (`localStorage`)
* Every single post draft, LinkedIn headline, About section, and Executive Bio is directly editable inside the browser (`contenteditable="true"`).
* Changes auto-save instantly with debounced persistence (`execdesk_<id>`), with a 1-tap **"Reset to default"** control per section.

### 3. Spotless A4 Executive PDF Export Engine
* Tailored for Boardroom Reviews, Ministry panels, and Multilateral tender submissions.
* Strips all web application chrome, URLs, timestamps, page numbers, and web badges automatically (`@page { size: A4 portrait; margin: 0; }`).
* Dedicated export options for both the **Executive Bio One-Pager** and the **LinkedIn Profile Dossier**.

### 4. 20-Day Automated Storage & RAM Hygiene Policy
* **Browser Janitor**: Scans stored revisions on every session launch and auto-purges any items older than 20 days.
* **Backend Janitor (`agent_core/storage_manager.py`)**: Automatically cleans historical batch files and caches older than 20 days during scheduled CI runs.
* **Zero-RAM Edge**: Hosted on Vercel Serverless CDN with zero persistent server RAM overhead.

---

## 🛠️ CLI Commands & Local Usage

```bash
# 1. Sync & review dashboard locally
python3 main.py dashboard

# 2. Run local development server
python3 server.py

# 3. Generate weekly batch of 4 authority posts
python3 main.py generate-week

# 4. Generate high-converting peer connection notes (< 300 chars)
python3 main.py outbound-note --type undp --name "Amit" --org "UNDP India"
python3 main.py outbound-note --type ukwdp --name "Rajesh" --org "World Bank"
python3 main.py outbound-note --type solar --name "Priya" --org "Clean Energy Corp"
python3 main.py outbound-note --type csr --name "Suresh" --org "Tata Trusts"

# 5. Generate high-signal comments for industry posts
python3 main.py comment --theme csr_sroi
python3 main.py comment --theme fpo_aggregation
python3 main.py comment --theme solar_grid
python3 main.py comment --theme public_policy

# 6. Execute 20-day storage and cache cleanup
python3 main.py storage-clean --days 20
```

---

## 📂 Core Strategic Dossiers

* [RAMU_MUNUGOTI_LINKEDIN_PROFILE.md](file:///Users/johnyforever/Desktop/Antigravity/projects/Ramu%20Linkedin%20Agent/RAMU_MUNUGOTI_LINKEDIN_PROFILE.md): Master profile blueprint with availability statement.
* [EXECUTIVE_BIO_ONE_PAGER.md](file:///Users/johnyforever/Desktop/Antigravity/projects/Ramu%20Linkedin%20Agent/EXECUTIVE_BIO_ONE_PAGER.md): Boardroom and bilateral bid key personnel bio.
* [MASTER_ROADMAP_AND_OMNI_DOMAIN_STRATEGY.md](file:///Users/johnyforever/Desktop/Antigravity/projects/Ramu%20Linkedin%20Agent/MASTER_ROADMAP_AND_OMNI_DOMAIN_STRATEGY.md): The 90-day 3-Horizon Barbell recruitment strategy.

