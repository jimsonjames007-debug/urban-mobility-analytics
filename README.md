# 🚍 Urban Mobility & Public Transport Performance Analytics

[![Tableau](https://img.shields.io/badge/Tableau-Dashboard-E97627?style=flat&logo=tableau&logoColor=white)](https://help.tableau.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An end-to-end data analytics and visual storytelling project analyzing urban transport dynamics, passenger demand patterns, operational delays, regional transit corridors, and carbon emissions across multi-modal transit networks (Bus, Metro, Tram, Rail, and Shared Cycling).

---

## 📌 Dashboard Overview

![Tableau Dashboard Preview](screenshots/DASHBOARD.png)

The interactive dashboard integrates multi-dimensional transit metrics to empower city planners, transit administrators, and municipal decision-makers with actionable operational intelligence.

---

## 📊 Key Visualizations & Analytical Modules

| Visualization | Type | Analytical Purpose | Key Insight |
| :--- | :--- | :--- | :--- |
| **Passenger Demand** | Bar Chart | Measures total passenger volume per transit mode | Metro and Rail networks handle the majority of commuter volumes. |
| **Usage Trend by Month** | Time-Series Line Chart | Identifies seasonality across transit modes throughout 2025 | Captures weather-related shifts (e.g. higher cycling in summer, increased metro traffic in winter). |
| **Delay Patterns by Route** | Scatter Plot | Examines passenger load vs. average delays per route | Identifies systemic delays in high-traffic rail corridors requiring signaling & junction reviews. |
| **Regional Performance** | Highlight Heat Map | Maps origin-to-destination district flows & average wait times | Highlights high-congestion bottlenecks between North District and City Center. |
| **Sustainability Indicator** | Dual-Axis Combo Chart | Compares aggregate distance traveled vs. CO₂ emissions | Highlights the urgency of bus fleet electrification relative to total distance traveled. |

---

## 🖼️ Visual Gallery

| Passenger Demand | Monthly Usage Trends |
| :---: | :---: |
| ![Passenger Demand](screenshots/PASSENGER%20DEMAND.png) | ![Usage Trend by Month](screenshots/USAGE%20TREND%20BY%20MONTH.png) |

| Delay Patterns | Regional Performance | Sustainability Impact |
| :---: | :---: | :---: |
| ![Delay Patterns](screenshots/DELAY%20PATTERNS.png) | ![Regional Performance](screenshots/REGINOAL%20PERFORMANCE.png) | ![Sustainability Indicator](screenshots/SUSTAINABILITY%20INDICATOR.png) |

---

## 📁 Repository Structure

```text
├── documentation/
│   ├── FINAL_REPORT_DRAFT.md                                      # Markdown report draft
│   ├── VSTT Practical Assignment Report.docx                      # Editable project report (Word)
│   ├── VSTT Practical Assignment Report.pdf                       # Comprehensive final report (PDF)
│   └── VSTT Practical Skills Oct25 G1 (1).pdf                     # Assignment brief / guidelines
├── screenshots/
│   ├── DASHBOARD.png                                              # Master dashboard screenshot
│   ├── DELAY PATTERNS.png                                         # Scatter plot screenshot
│   ├── PASSENGER DEMAND.png                                       # Passenger demand bar chart
│   ├── REGINOAL PERFORMANCE.png                                   # Regional flow heat map
│   ├── SUSTAINABILITY INDICATOR.png                               # Dual-axis emissions chart
│   └── USAGE TREND BY MONTH.png                                   # Monthly time-series chart
├── tableau_and_data/
│   ├── Urban Mobility & Public Transport Performance Dashboard.twbx # Tableau Packaged Workbook
│   └── urban_mobility_dataset.csv                                 # Processed 2,500-record dataset
├── .gitignore                                                     # Standard git ignore rules
├── generate_dataset.py                                            # Python simulation script for generating dataset
└── README.md                                                      # Project documentation & overview
```

---

## 🛠️ Tech Stack & Tools

- **Visual Analytics & BI:** Tableau Desktop (`.twbx`)
- **Data Engineering & Simulation:** Python 3 (`Pandas`, `NumPy`, `random`, `datetime`)
- **Reporting & Documentation:** Markdown, Microsoft Word, Adobe PDF

---

## 🚀 Getting Started

### 1. Re-generating the Dataset (Optional)
The repository includes a ready-to-use dataset (`tableau_and_data/urban_mobility_dataset.csv`), but you can generate a fresh distribution using:

```bash
# Install dependencies
pip install pandas numpy

# Generate 2,500 records across 11 variables (saved to tableau_and_data/)
python generate_dataset.py
```

### 2. Exploring the Tableau Workbook
1. Download or clone this repository.
2. Open `tableau_and_data/Urban Mobility & Public Transport Performance Dashboard.twbx` using **Tableau Desktop** or **Tableau Reader** (free).
3. Interact with dynamic filters, route selections, and cross-chart filtering.

---

## 💡 Key Strategic Recommendations
1. **Targeted Rail Infrastructure Upgrades:** Address junction bottlenecks on heavily delayed rail lines identified in the scatter plot.
2. **Dedicated Bus Lanes:** Deploy bus rapid transit (BRT) or dedicated bus lanes along the high-congestion *North District ➔ City Center* corridor.
3. **Fleet Electrification:** Prioritize low/zero-emission bus replacements to minimize the highest per-passenger CO₂ emission sources.
4. **Seasonal Scheduling Adjustments:** Adjust service frequencies during seasonal peaks according to monthly ridership data.

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).
