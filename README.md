# PIROP — Enterprise Pricing Intelligence & Revenue Optimization Platform

**PIROP** (Pricing Intelligence & Revenue Optimization Platform) is a zero-dependency, standalone enterprise pricing and revenue optimization web application built for Mada Media's Out-Of-Home (OOH) media portfolio.

Live Web App: **[https://manasdevhub.github.io/pirop_pricing_tool/](https://manasdevhub.github.io/pirop_pricing_tool/)**

---

## Key Features & Capabilities

- **Executive Dashboard**: Realized revenue, portfolio occupancy (vs 55% target), win rate, avg selling price, and 4 interactive Chart.js visualizations (revenue by region, pipeline status, occupancy by asset class, 6-month revenue trend).
- **Market Insights Engine**: 6 auto-generated portfolio intelligence cards derived from live assets and occupancy.
- **Price Point Universe (PPU)**: Master benchmark repository with source classification (Investor Rate Card, Mystery Shopping, Contracts), filtering, and benchmark addition modal.
- **Asset Catalogue**: 12 seeded OOH assets across 4 regions and 5 asset classes with real-time occupancy indicators and RBAC asset management.
- **Pricing Workspace**: Benchmark-first pricing engine with explainable **Intelligent Fallback** (traffic, audience reach, occupancy model) and visual comparable constellation diagrams.
- **Scenario Planning**: Base Case, Aggressive Growth, and Premium Positioning strategic scenario modelling with comparative charts.
- **Financial Feasibility Engine**: ROI, IRR (bisection algorithm), NPV, payback period, and MAG (Minimum Guaranteed Take) vs. revenue share modeler with cash flow projection charts.
- **Approvals Queue**: Role-gated review workflow with Review Required flags for fallback-priced deals, rationale review, and decision audit logs.
- **Governance & Audit Trail**: Immutable append-only log, active policy cards, and one-click CSV audit export.
- **Commercial Intelligence Assistant**: Smart local NLP conversational engine with 8+ intent categories, typing animation, and grounded portfolio Q&A (100% offline, zero API keys required).
- **Platform Roadmap**: 4-phase evolution roadmap (P1 Foundation -> P4 Autonomous Optimization) and production architecture stack specification.

---

## How to Run Locally

1. Open `index.html` or `PIROP-Platform.html` in any web browser (Chrome, Edge, Firefox, Safari, MS Teams Webview).
2. No local web server, Node.js, or backend API required. All state persists automatically in `localStorage`.

---

## Rebuilding HTML Files (`build_pirop.py`)

To regenerate `index.html` and `PIROP-Platform.html` with bundled Chart.js and defensive rendering logic:

```bash
python build_pirop.py
```

This updates both files with 100% inlined scripts and styles so the app runs smoothly inside MS Teams, iframes, strict CSP environments, and offline networks.
