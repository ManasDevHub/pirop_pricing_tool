# PIROP — Enterprise Pricing Intelligence & Revenue Optimization Platform (Dubai OOH Edition)

**PIROP** (Pricing Intelligence & Revenue Optimization Platform) is a zero-dependency, standalone enterprise pricing and revenue optimization web application built specifically for Mada Media's Out-Of-Home (OOH) media portfolio in Dubai & the UAE.

Live Web App: **[https://manasdevhub.github.io/pirop_pricing_tool/](https://manasdevhub.github.io/pirop_pricing_tool/)**

---

## Key Features & Business Requirements Delivered

- **Dubai Currency & Portfolio Grounding**: 100% AED currency calculations across all modules with real Dubai OOH locations (Sheikh Zayed Road, Downtown Dubai, Dubai Marina, DIFC, Business Bay, Airport Road).
- **Executive Dashboard**: Realized AED revenue, portfolio occupancy (vs 55% target), win rate, avg selling price, executive PDF/CSV report exporter, and 4 interactive Chart.js visualizations.
- **Market Insights Engine**: 6 auto-generated portfolio intelligence cards derived from live assets and occupancy.
- **Price Point Universe (PPU) & Version Control**: Master Dubai benchmark repository with source classification, version tracking, version history modal, and rate updates.
- **Asset Catalogue & Impact Analysis**: 12 Dubai OOH assets across 5 asset classes, **Static-to-Digital Conversion Feasibility Analyzer**, and **New Asset Impact & Cannibalization Simulation**.
- **Pricing Workspace & Elasticity**: Benchmark-first pricing engine with explainable **Intelligent Fallback**, **Event & Seasonality Multipliers** (Gitex, DSF, F1), **Price Elasticity Coefficient Factor**, and **Commercial Guardrail Alert System**.
- **Scenario Planning & Revenue Modeling**: Low, Medium, and High occupancy sensitivity modeling with price adjustment forecasting.
- **Financial Feasibility & Profitability**: Complete PBT (Profit Before Tax), Net Profit, Net Margin %, Cost Breakdown (Land Lease, Utilities/O&M, Sales Commission), ROI, IRR (bisection algorithm), NPV, Payback period, and MAG Guarantee vs Revenue Share calculations.
- **Approvals Queue & Guardrail SLA**: Role-gated review workflow with Guardrail Violation flags (Discounts > 15%), approval rationale input, and decision history.
- **Governance & Policy Guardrails**: Configurable commercial guardrail threshold settings, immutable audit trail, and CSV audit exporter.
- **Commercial Intelligence Assistant**: Smart local NLP conversational engine with 8+ Dubai market intents, grounded portfolio Q&A (100% offline, zero API keys required).
- **Platform Roadmap & Enterprise Stack**: 4-phase evolution roadmap (P1 Foundation -> P4 Autonomous Optimization) and production architecture & integration specification.

---

## How to Run Locally

1. Open `index.html` or `PIROP-Platform.html` in any web browser (Chrome, Edge, Firefox, Safari, MS Teams Webview).
2. No local web server, Node.js, or backend API required. All state persists automatically in `localStorage`.

---

## Rebuilding HTML Files (`build_pirop.py`)

To regenerate `index.html` and `PIROP-Platform.html` with inlined Chart.js and defensive rendering:

```bash
python build_pirop.py
```
