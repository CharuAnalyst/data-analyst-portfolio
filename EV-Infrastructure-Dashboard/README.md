<div align="center">

# EV Infrastructure Gap Analysis 2026

### Python Forecasting + Power BI Dashboard for EV Charging Infrastructure Planning

![Python](https://img.shields.io/badge/Python-Data%20Analysis-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Decision%20Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Forecasting](https://img.shields.io/badge/Forecasting-2026%20Planning-174A7C?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-2E7D32?style=for-the-badge)

</div>

---

## Decision Brief

This project analyzes the expected gap between **EV adoption growth** and **public charging station availability** across Indian states by 2026.

The goal is to identify:

> **Which states may face the highest EV charging infrastructure pressure, how large the station gap could become, and where infrastructure planning should be prioritized first.**

This project combines **Python data preparation, forecasting, station gap calculation, visual analysis, and Power BI reporting** into one infrastructure planning case study.

---

## Executive Snapshot

| Planning Metric | Dashboard Result | Meaning |
| --- | ---: | --- |
| Forecasted EVs by 2026 | **3.22M** | Estimated EV volume from the analysis output |
| Charging Gap | **63K** | Approximate additional station gap shown in the dashboard |
| Stations Required | **64K** | Estimated public charging station requirement by 2026 |
| Active Stations | **1,372** | Current charging station base used in the analysis |
| Overall Gap Signal | **98%** | Large gap between current stations and required stations |

---

## Dashboard Preview

![EV Infrastructure Dashboard](Outputs/EV_Dashboard_Screenshot.png)

> The Power BI dashboard summarizes forecasted EV growth, station requirements, active stations, state-wise charging gap, and infrastructure recommendations for 2026 planning.

---

## Why This Project Matters

EV adoption can grow faster than charging infrastructure. If public charging availability does not expand in time, high-adoption states may face bottlenecks that affect customer confidence, city planning, and investment decisions.

This project frames EV infrastructure as a planning problem:

- Forecast future EV demand.
- Compare demand with current charging station availability.
- Estimate additional stations needed.
- Identify priority states for infrastructure expansion.
- Communicate findings through a dashboard and recommendations.

---

## Analytical Workflow

```text
Raw EV Sales Data
        |
        v
Data Cleaning and State-Level Aggregation
        |
        v
Charging Station Data Integration
        |
        v
Forecasting and 2026 Projection
        |
        v
Station Requirement and Gap Calculation
        |
        v
Power BI Dashboard and Recommendation Layer
```

---

## Core Analysis Questions

- Which Indian states are expected to have the highest EV demand by 2026?
- How many charging stations may be required to support forecasted EV adoption?
- Which states show the largest gap between current stations and required stations?
- Where should charging infrastructure expansion be prioritized first?
- How can forecast outputs be converted into a clear planning dashboard?

---

## Key Findings

### 1. Infrastructure Gap Is Severe

The dashboard shows a major gap between current active stations and estimated station requirement by 2026. The visible summary indicates **1,372 active stations** against around **64K required stations**.

### 2. Priority States Are Clearly Visible

The analysis highlights **Uttar Pradesh, Maharashtra, and Karnataka** as major priority states based on projected gap size.

### 3. EV Growth Requires Forward Planning

The forecast view shows EV adoption increasing from 2024 to 2026, making charging infrastructure a forward-looking planning issue rather than only a current-state reporting problem.

### 4. Forecasting Is Converted Into Action

The project does not stop at predicting EV growth. It converts forecasted EV demand into estimated station requirements, state-wise gap size, and practical planning recommendations.

---

## Priority State View

| Priority Signal | State Examples | Planning Meaning |
| --- | --- | --- |
| Highest gap pressure | Uttar Pradesh, Maharashtra, Karnataka | Requires urgent infrastructure planning |
| Strong growth visibility | UP, MH, KA and other top states | EV demand may outpace station availability |
| Investment focus | High-gap states | Better candidates for phased charging expansion |

---

## Business Recommendations

### 1. Prioritize High-Gap States First

Infrastructure planning should begin with states showing the largest projected gap, especially **Uttar Pradesh, Maharashtra, and Karnataka**.

### 2. Use A Phased Deployment Strategy

Charging expansion should not be distributed equally across all states. It should be phased based on forecasted EV demand, current station base, and gap severity.

### 3. Explore Public-Private Partnerships

Large infrastructure gaps may require collaboration between government bodies, charging companies, fuel stations, real estate owners, and fleet operators.

### 4. Track The Gap Yearly

The station gap should be recalculated each year as EV adoption, charging station rollout, and policy support change.

### 5. Improve Future Model Inputs

Future versions can become stronger by adding city-level EV adoption, vehicle category, charging speed, highway routes, population density, and station utilization data.

---

## Technical Implementation

| Layer | Work Completed |
| --- | --- |
| Data Cleaning | Cleaned EV sales, charging station, and supporting datasets using Python |
| Data Preparation | Created state-level master data and analysis-ready CSV outputs |
| Forecasting | Generated 2026 forecast outputs for state-wise EV planning |
| Gap Calculation | Estimated station requirement and additional charging gap |
| Visualization | Created Python charts and Power BI dashboard views |
| Reporting | Summarized findings, recommendations, and planning signals |

---

## Project Outputs

- [Power BI Dashboard](Outputs/EV_Dashboard.pbix)
- [Dashboard Screenshot](Outputs/EV_Dashboard_Screenshot.png)
- [EV Forecast Output](Outputs/EV_Forecast_2026.csv)
- [EV Gap Analysis Output](Outputs/EV_Gap_Analysis_2026.csv)
- [EV Master Data Output](Outputs/EV_Master_Data.csv)
- [Project Report](Project%20Report.pdf)

---

## Repository Structure

```text
EV-Infrastructure-Gap-Analysis-2026/
|
|-- Outputs/
|   |-- EV_Dashboard.pbix
|   |-- EV_Dashboard_Screenshot.png
|   |-- EV_Forecast_2026.csv
|   |-- EV_Gap_Analysis_2026.csv
|   |-- EV_Master_Data.csv
|   |-- Station_Gap_Analysis.png.png
|   |-- Top5_States_Forecast.png.png
|
|-- Scripts/
|   |-- day1.py
|   |-- day2.py
|   |-- day3.py
|
|-- Project Report.pdf
|-- README.md
```

---

## How To Review This Project

1. Open the Power BI dashboard file from the `Outputs` folder.
2. Review the dashboard screenshot for the executive summary view.
3. Check `EV_Gap_Analysis_2026.csv` for state-wise charging gap output.
4. Review the Python scripts in the `Scripts` folder to understand the analysis pipeline.
5. Read the project report for additional explanation of the analysis.

---

## Reproducibility Note

The repository includes processed outputs and dashboard files. The raw input datasets are not included, so a full rerun requires adding the original datasets under a `Data/` folder.

Recommended raw data structure:

```text
Data/
|-- EV_Dataset.csv
|-- ev-charging-stations-india.csv
|-- DailyDelhiClimate.csv
```

Recommended future cleanup:

- Add `requirements.txt`.
- Standardize all generated outputs into the `Outputs/` folder.
- Rename `.png.png` chart files to clean `.png` names.
- Update script paths so the full pipeline can run from the project root.

---

## Skills Demonstrated

**Python:** Data cleaning, aggregation, CSV output generation, and analysis workflow  
**Forecasting:** State-wise 2026 EV demand projection and forecast output preparation  
**Power BI:** Executive dashboard design, KPI cards, state-level visuals, and recommendation reporting  
**Business Analytics:** Infrastructure gap analysis, priority-state identification, and planning recommendations  
**Data Storytelling:** Turning technical outputs into a decision-ready infrastructure planning narrative  

---

## Final Takeaway

This project shows how analytics can support real infrastructure planning. By combining EV adoption trends, charging station availability, forecast outputs, and dashboard reporting, the analysis identifies where charging infrastructure pressure may become most urgent by 2026.

The strength of this project is that it connects technical analysis with a real planning question:

> **Where should EV charging infrastructure investment be prioritized first?**

---
