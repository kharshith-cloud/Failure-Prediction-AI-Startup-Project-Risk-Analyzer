# Failure Prediction AI – Startup & Project Risk Analyzer

> Infosys Springboard Virtual Internship Project

![Project Preview](assets/project-preview.png)

## Overview

Failure Prediction AI is an AI-assisted project intelligence platform designed to evaluate startups and projects across multiple critical dimensions before significant resources are invested. By leveraging deterministic analysis combined with AI reasoning, the system evaluates market conditions, competitive landscapes, project risks, feasibility, and SWOT factors to produce actionable strategic recommendations and risk mitigation strategies. 

The application takes structured business inputs from the user and passes them through a sophisticated reasoning workflow, culminating in a consolidated project assessment dashboard and a downloadable report.

Developed as part of the Infosys Springboard Virtual Internship, this project demonstrates the integration of deterministic backend calculation engines with AI/LLM agent workflows to solve complex operational and strategic business problems.

## Problem Statement

Startup and project ideas often fail due to systemic factors such as:
- Fierce market competition
- Insufficient resources or capital
- Limited domain expertise
- Weak or unstructured market research
- Low practical feasibility
- Operational constraints
- Strategic gaps

Without a structured, data-driven way to assess these risk factors early on, organizations can waste significant time and capital. Failure Prediction AI provides structured, objective decision-support to analyze these vulnerabilities *before* irreversible investments are made.

## Objectives

The primary objectives of this system are to:
- Collect structured project information (budget, market, competition, etc.).
- Analyze market and competitor conditions systematically.
- Calculate objective project risk scores based on defined heuristics.
- Estimate success probabilities based on the calculated risk.
- Generate structured SWOT (Strengths, Weaknesses, Opportunities, Threats) analyses.
- Evaluate the practical feasibility of the project.
- Generate context-aware strategic recommendations.
- Generate targeted risk mitigation strategies.
- Run a structured LangGraph reasoning workflow to process and validate intelligence.
- Produce a unified, interactive final project intelligence report.
- Provide a downloadable artifact of the assessment.

## Key Features

### Project Information Collection
The system features a premium, interactive user interface to collect crucial project data, including:
- Project Name & Description
- Target Market
- Budget
- Competition
- Resources & Team Capabilities
- Primary Objectives

### Market & Competitor Intelligence
The system analyzes the structured inputs to assess the target market and the competitive landscape. Using rule-based heuristics and deterministic analysis, it evaluates the intensity of the competition and the viability of the market opportunity based on the provided parameters.

### Risk Assessment
The core risk engine calculates a comprehensive risk score (0-100) using defined project factors, including:
- Market Competition
- Team Expertise
- Resource Availability
- Innovation Level
- Market Research

Based on the score, the risk is categorized as:
- **0–39:** LOW RISK
- **40–69:** MEDIUM RISK
- **70–100:** HIGH RISK

The system also calculates the **Success Probability** using the formula:
`Success Probability = 100 − Risk Score`

### SWOT Analysis
The system automatically maps project characteristics to generate a comprehensive SWOT matrix:
- **Strengths:** Internal advantages (e.g., strong team, high budget).
- **Weaknesses:** Internal disadvantages (e.g., lack of resources).
- **Opportunities:** External chances for growth (e.g., low competition, high innovation).
- **Threats:** External risks (e.g., saturated market).

### Feasibility Assessment
Feasibility is evaluated across four distinct dimensions:
- Market Opportunity
- Team Capability
- Competitive Advantage
- Resource Availability

The final feasibility score is aggregated as the average of these four dimensions, providing a clear metric on how practical it is to execute the project.

### AI Recommendations
Based on the project's unique conditions and the calculated risk profile, the system generates targeted strategic recommendations to improve the project's chances of success.

### Risk Mitigation
The mitigation engine maps specific identified risk conditions (e.g., high competition combined with low budget) to concrete, actionable mitigation strategies to proactively protect the project.

### LangGraph AI Reasoning Workflow
The intelligence pipeline is orchestrated using a structured reasoning workflow consisting of five stages:
1. **Data Ingestion:** Structured extraction of user inputs.
2. **Risk Analysis:** Calculation of risk and feasibility metrics.
3. **Strategic Reasoning:** Generation of SWOT and mitigation strategies.
4. **Validation:** Checking data consistency and fallback handling.
5. **Report Generation:** Compiling the final dashboard data.

### Final Report
The output of the workflow is a beautifully rendered, interactive dashboard containing:
- Consolidated assessment metrics
- Risk score & success probability
- Feasibility breakdown
- Market & competitor analysis
- SWOT matrix
- Strategic recommendations
- Mitigation strategies
- The documented reasoning workflow

Users can also export this data as a downloadable final report.

## Technology Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Web Framework | Flask |
| Database | PostgreSQL |
| AI/LLM | Google Gemini |
| Agent Workflow | LangGraph |
| Data/Analysis | Python-based deterministic analysis |
| Frontend | HTML, CSS, JavaScript (Vanilla) |
| Testing | Python test suite |
| Deployment | WSGI-compatible deployment |

## System Architecture

The following diagram illustrates the complete data flow and system architecture:

```mermaid
flowchart TD
    A[Project Input] --> B[Flask Application]
    B --> C[PostgreSQL]
    C --> D[Market Analysis]
    C --> E[Competitor Analysis]
    D --> F[Risk Assessment]
    E --> F
    F --> G[SWOT Analysis]
    F --> H[Feasibility Assessment]
    G --> I[Recommendations]
    H --> I
    I --> J[Risk Mitigation]
    J --> K[LangGraph Workflow]
    K --> L[Final Assessment]
    L --> M[Dashboard & Report]
```

## Development Milestones

### Milestone 1: Environment Setup & Foundation
- Initialized the Python/Flask environment and configured the PostgreSQL database schema.
- Established the foundational project structure and basic routes.

### Milestone 2: Risk & Feasibility Engines
- Developed the deterministic risk calculation engine based on project inputs.
- Implemented the four-dimensional feasibility assessment system.

### Milestone 3: Intelligence & AI Integration
- Integrated Gemini AI and LangGraph workflows.
- Developed the SWOT analysis, competitor assessment, and risk mitigation strategies.

### Milestone 4: Frontend UI & Final Reporting
- Designed a premium, interactive frontend workspace.
- Implemented the final dashboard and downloadable report generation.
