# Ramu Munugoti — LinkedIn Authority & Opportunity Agent

A specialized, self-contained AI Agent engineered to position **Ramu Munugoti** as a high-caliber **Program Director, Public Systems Executive, and Board Advisor** across:
1. **Rural Livelihoods & FPO Agribusiness**
2. **Corporate Social Responsibility (CSR) & 4.8x SROI Governance**
3. **Public Policy & Government Delivery (Ex-NSDC MoSDE, ₹45Cr+ PFMS Budget)**
4. **Clean Energy Transition (PM Surya Ghar / Solar) & Applied AI Telemetry**

---

## 🚀 Quick Start: How to Use Your Agent

### 1. View & 1-Click Copy Weekly Posts (Visual Dashboard)
To open your personal visual review desk:
```bash
python3 main.py dashboard
```
Then open [dashboard.html](file:///Users/johnyforever/Desktop/Antigravity/projects/Ramu%20Linkedin%20Agent/dashboard.html) in your browser.  
Click **"📋 1-Click Copy"** next to any post to paste directly into LinkedIn.

### 2. Generate a Fresh Weekly Batch of Posts
Generates 4 high-authority posts (one for each strategic pillar):
```bash
python3 main.py generate-week
```
Drafts are saved as Markdown in `drafts/` for easy reading and editing.

### 3. Generate a Personalized Executive Connection Note (< 300 Chars)
When reaching out to decision-makers, generate a tailored, non-spammy note:
```bash
# For CSR & Foundation Heads (Move B):
python3 main.py outbound-note --type csr --name "Full Name" --org "Company / Foundation"

# For Multilateral & USAID Proposal Leads (Move A):
python3 main.py outbound-note --type multilateral --name "Full Name" --org "USAID Prime / Org"

# For Executive Search Headhunters (Move C):
python3 main.py outbound-note --type headhunter --name "Full Name" --org "Search Firm"

# For Solar / Clean Energy CEOs:
python3 main.py outbound-note --type solarenergy --name "Full Name" --org "Energy Corp"
```

### 4. Generate High-Signal Comments for Target Posts
Drop authoritative comments on target leaders' feeds before sending connection requests:
```bash
python3 main.py comment --theme csr_sroi
python3 main.py comment --theme fpo_aggregation
python3 main.py comment --theme solar_grid
python3 main.py comment --theme public_policy
```

---

## 📂 Core Project Files

* [RAMU_MUNUGOTI_LINKEDIN_PROFILE.md](file:///Users/johnyforever/Desktop/Antigravity/projects/Ramu%20Linkedin%20Agent/RAMU_MUNUGOTI_LINKEDIN_PROFILE.md): Ready-to-paste master profile (Headlines, About, Experience, Skills, Certifications).
* [MASTER_ROADMAP_AND_OMNI_DOMAIN_STRATEGY.md](file:///Users/johnyforever/Desktop/Antigravity/projects/Ramu%20Linkedin%20Agent/MASTER_ROADMAP_AND_OMNI_DOMAIN_STRATEGY.md): Comprehensive strategic playbook covering all 5 hiring sectors and the Barbell recruitment strategy.
* [dashboard.html](file:///Users/johnyforever/Desktop/Antigravity/projects/Ramu%20Linkedin%20Agent/dashboard.html): Interactive visual command center for copying posts and connection notes.
* `agent_core/`:
  * `persona.py`: Verified dossier, proof points (₹45Cr, 45K livelihoods, 50 FPOs), and voice guidelines.
  * `pillars.py`: The 4 strategic content pillars and audience mapping.
  * `generator.py`: Content generation engine.
  * `outbound.py`: High-converting connection notes and comment generator.
