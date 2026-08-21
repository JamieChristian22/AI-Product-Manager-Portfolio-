# 🤖 AI E-Commerce Revenue Optimizer

### AI Product Management • Revenue Intelligence • Dynamic Pricing • Personalization • Experimentation • Responsible AI

![AI Product Management](https://img.shields.io/badge/AI-Product%20Management-6C63FF?style=for-the-badge)
![Revenue Optimization](https://img.shields.io/badge/Revenue-Optimization-16A34A?style=for-the-badge)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-F59E0B?style=for-the-badge)
![Responsible AI](https://img.shields.io/badge/Responsible-AI-059669?style=for-the-badge)
![AI Governance](https://img.shields.io/badge/AI-Governance-0F766E?style=for-the-badge)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square\&logo=python\&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-336791?style=flat-square\&logo=postgresql\&logoColor=white)
![Jira](https://img.shields.io/badge/Jira-0052CC?style=flat-square\&logo=jira\&logoColor=white)
![A/B Testing](https://img.shields.io/badge/A%2FB-Testing-EF4444?style=flat-square)
![Product Analytics](https://img.shields.io/badge/Product-Analytics-7C3AED?style=flat-square)
![Model Evaluation](https://img.shields.io/badge/Model-Evaluation-0891B2?style=flat-square)
![AI Risk Management](https://img.shields.io/badge/AI-Risk%20Management-DC2626?style=flat-square)
![Model Monitoring](https://img.shields.io/badge/Model-Monitoring-16A34A?style=flat-square)

> End-to-end AI Product Management case study demonstrating how machine learning, experimentation, product analytics, and Responsible AI can be combined to improve e-commerce revenue while protecting **customer trust, seller economics, model quality, and platform safety**.

> **Portfolio Disclosure:** This is a simulated AI Product Management case study using synthetic or modeled data. Business-impact and model-performance figures represent portfolio experiment outcomes and are not claims from a production deployment at a real company.

---

# 🧠 Executive Overview

The **AI E-Commerce Revenue Optimizer** is an AI-powered revenue intelligence platform designed around one core product question:

> **How might we increase revenue per active user without harming customer trust or seller margins?**

The solution combines:

* 💰 Dynamic pricing optimization
* 🎯 Personalized recommendation ranking
* 🛒 Cart-abandonment prediction
* 📊 Revenue and funnel analytics
* 🧪 Controlled A/B experimentation
* 🤖 Generative AI capabilities
* 🧠 AI model evaluation
* ⚖️ Responsible AI
* 🛡️ AI risk management
* 🔄 Model monitoring and lifecycle governance

The project demonstrates the complete AI product lifecycle:

**Business Problem → Product Strategy → AI Solution → Model Evaluation → Experimentation → Governance → Staged Launch → Monitoring → Iteration**

---

# 🎯 Business Problem

The simulated marketplace experienced four major problems:

### Static Pricing

Pricing did not adequately account for:

* Demand elasticity
* Inventory
* historical conversion
* timing
* competitive signals

### Weak Personalization

Customers frequently encountered products with limited relevance to their demonstrated interests.

### High Cart Abandonment

Potential purchases were lost because the platform lacked sufficient intelligence to identify high-risk sessions and intervene appropriately.

### Inefficient Promotional Targeting

Discounts and promotions could be distributed without sufficient understanding of customer intent or incremental value.

---

# 🚀 Product Vision

Build an AI-powered revenue intelligence platform that:

1. **Increases revenue per active user**
2. **Improves product discovery**
3. **Reduces avoidable cart abandonment**
4. **Protects seller margins**
5. **Maintains customer trust**
6. **Enables measurable experimentation**
7. **Operates within Responsible AI guardrails**

---

# 👥 Target Users

| Persona                     | Core Pain Point                 | Desired Outcome                  |
| --------------------------- | ------------------------------- | -------------------------------- |
| **Price-Sensitive Shopper** | Finds better deals elsewhere    | Competitive and fair pricing     |
| **Frequent Buyer**          | Irrelevant recommendations      | Faster product discovery         |
| **Marketplace Seller**      | Margin uncertainty              | Better pricing intelligence      |
| **Marketing Manager**       | Low campaign efficiency         | Higher-quality targeting         |
| **Product Manager**         | Limited experiment visibility   | Evidence-based product decisions |
| **Revenue Team**            | Fragmented monetization signals | Unified revenue intelligence     |

---

# ⭐ North Star Metric

## Revenue per Active User — RPAU

RPAU connects monetization performance with actual active-user behavior.

### Supporting Business KPIs

* Conversion Rate
* Average Order Value
* Cart Abandonment Rate
* Customer Lifetime Value
* Repeat Purchase Rate
* Revenue Lift
* Seller Margin

### AI/Product Guardrails

Revenue improvements are not considered successful if they materially damage:

* Customer trust
* Seller economics
* Recommendation quality
* Fairness
* Privacy
* Reliability
* User autonomy

---

# 📊 Simulated Business Impact

| Metric                      | Baseline | AI Experiment |       Lift |
| --------------------------- | -------: | ------------: | ---------: |
| **Conversion Rate**         |     3.4% |          3.9% | **+14.7%** |
| **Average Order Value**     |      $82 |           $91 |   **+11%** |
| **Revenue per Active User** |      $46 |           $54 |   **+17%** |
| **Cart Abandonment**        |      68% |           60% |   **-12%** |
| **Repeat Purchase Rate**    |      28% |           34% |   **+21%** |

### Modeled Business Outcome

**ROI-positive scenario within approximately four months**

Primary experiment designed around a **95% confidence threshold**.

---

# 🏗️ AI Solution Architecture

The product contains multiple AI components rather than relying on a single model.

```text
Customer / Session Signals
          ↓
    Data Validation
          ↓
     Feature Layer
          ↓
 ┌────────┼────────┐
 ↓        ↓        ↓
Pricing   Ranking  Abandonment
Model     Model    Predictor
 ↓        ↓        ↓
 └────────┼────────┘
          ↓
    Policy Guardrails
          ↓
  Product Experience
          ↓
 Experiment + Analytics
          ↓
 Monitoring / Governance
```

---

# 💰 1. Dynamic Pricing Engine

## Product Objective

Recommend prices that balance:

**Conversion + Revenue + Margin + Customer Trust**

### Model Inputs

* Demand elasticity
* Inventory levels
* Historical conversion
* Product velocity
* Time-based demand
* Pricing history
* Approved competitive signals

### Model Output

**Recommended price or pricing range**

### Product Constraints

The system should not simply maximize the highest possible price.

Pricing decisions must consider:

* Seller margin
* Customer experience
* price volatility
* business constraints
* fairness concerns
* model confidence

### Primary Metrics

* Revenue lift
* Conversion
* Gross margin
* Average order value
* Price acceptance

### Guardrails

* Refund rate
* customer complaints
* NPS/trust indicators
* excessive price volatility
* seller-margin degradation

---

# 🎯 2. AI Recommendation Engine

## Objective

Increase discovery, basket size, and repeat purchases by ranking products according to customer relevance.

### Modeling Approaches

* Collaborative filtering
* Behavioral clustering
* Purchase affinity modeling
* Candidate ranking

### Personalization Surfaces

* Homepage
* Product detail pages
* Product bundles
* Frequently Bought Together
* Cart recommendations
* Post-purchase cross-sell

### Simulated Business Impact

**+11% Average Order Value**

**+21% Repeat Purchase Rate**

### Recommendation Evaluation

The model is evaluated using more than revenue.

Example metrics include:

* Precision@K
* Recall@K
* NDCG@K
* CTR
* Conversion
* Catalog coverage
* Recommendation diversity
* Repeat-purchase behavior

---

# 🛒 3. Cart-Abandonment Predictor

## Product Objective

Estimate abandonment risk early enough for the platform to provide a useful intervention.

### Potential Signals

* Cart value
* Session duration
* repeated product views
* cart edits
* checkout progression
* historical purchase behavior
* discount affinity
* prior abandonment behavior

### Output

**Abandonment probability**

### Product Actions

Depending on model confidence and business rules:

* Surface useful checkout information
* Recommend related alternatives
* Provide eligible incentives
* Simplify the customer journey
* Trigger appropriate messaging

### Simulated Outcome

**Cart abandonment: 68% → 60%**

---

# 🤖 4. Generative AI Layer

Generative AI can support contextual commerce experiences such as:

* Product summaries
* Recommendation explanations
* Product comparisons
* Revenue insights
* Merchant-facing summaries

### GenAI Requirements

Responses should be:

* Grounded
* Relevant
* Non-deceptive
* Privacy-aware
* Traceable to approved information

### GenAI Guardrails

The system should prevent:

* Fabricated product claims
* Sensitive-trait inference
* Manipulative urgency
* unsupported pricing statements
* PII leakage
* prompt-injection attacks

---

# 🧠 AI Model Management

Every major AI component includes model documentation.

## Model Cards Cover

* Intended use
* Out-of-scope use
* Product objective
* Model inputs
* Model outputs
* Training/evaluation approach
* Performance metrics
* Limitations
* Failure modes
* Risk controls
* Monitoring
* Retirement criteria

---

# 📐 AI Model Evaluation

Model performance is evaluated at multiple levels.

## Recommendation Model

* Precision@K
* Recall@K
* NDCG
* Catalog coverage
* Diversity
* CTR
* Conversion

## Cart-Abandonment Model

* ROC-AUC
* Precision
* Recall
* F1
* Calibration
* False-positive rate

## Pricing Model

* Revenue lift
* Margin lift
* Conversion
* Elasticity error
* price acceptance
* price volatility

## Generative AI

* Groundedness
* hallucination rate
* helpfulness
* unsafe-output rate
* sensitive-inference violations

---

# ⚖️ Responsible AI Framework

Responsible AI is treated as a **product requirement**, not a final compliance exercise.

## ⚖️ Fairness

Evaluate whether model behavior or product outcomes create material differences across meaningful cohorts.

### Controls

* Cohort evaluation
* Feature-ablation testing
* Proxy-risk analysis
* exposure monitoring
* recommendation-quality comparisons

---

## 🔐 Privacy

The AI system follows data-minimization principles.

### Controls

* Pseudonymous identifiers
* Consent-aware personalization
* limited retention
* sensitive-feature restrictions
* PII filtering
* feature governance

---

## 👤 User Autonomy

The platform should not use AI to manipulate customers.

### Prohibited Patterns

* Fabricated scarcity
* false urgency
* deceptive discounts
* hidden personalization controls
* repeated recommendations after explicit rejection
* sensitive vulnerability targeting

---

## 🔍 Transparency

Model documentation includes:

* Intended purpose
* limitations
* assumptions
* model version
* evaluation results
* decision criteria
* monitoring thresholds

---

## 🛡️ Reliability

AI systems require:

* fallback experiences
* performance SLAs
* monitoring
* drift detection
* incident response
* rollback procedures

---

# 🚨 AI Risk Management

The project includes a structured AI Risk Register covering areas such as:

## Pricing Risk

* Excessive price volatility
* inaccurate elasticity
* unfair pricing outcomes
* seller-margin damage

## Recommendation Risk

* Popularity bias
* filter bubbles
* exposure concentration
* historical feedback loops
* cold-start degradation

## Predictive Model Risk

* Model drift
* calibration errors
* false positives
* overfitting
* data leakage

## Privacy Risk

* Sensitive inference
* consent bypass
* excessive retention
* PII exposure

## Security Risk

* Data poisoning
* model extraction
* prompt injection
* metadata manipulation

## Generative AI Risk

* Hallucinations
* fabricated product information
* unsafe responses
* sensitive-data disclosure

## Operational Risk

* Model outages
* data-quality failures
* feature-store failures
* latency
* failed fallback behavior

---

# 🛡️ AI Risk Register

Each risk includes:

| Field                | Purpose                |
| -------------------- | ---------------------- |
| **Risk ID**          | Traceability           |
| **Risk Description** | Failure scenario       |
| **Likelihood**       | Probability            |
| **Impact**           | Business/user severity |
| **Risk Score**       | Prioritization         |
| **Mitigation**       | Preventive controls    |
| **Residual Risk**    | Remaining exposure     |
| **Owner**            | Accountability         |
| **Trigger**          | Escalation threshold   |

This converts Responsible AI from general principles into **operational product management**.

---

# 🔐 AI Security & Threat Modeling

Threat scenarios evaluated include:

* Event poisoning
* Model extraction
* Product metadata manipulation
* Prompt injection
* Data exfiltration
* PII leakage
* reward manipulation
* compromised dependencies

### Security Controls

* Input validation
* rate limiting
* anomaly detection
* feature validation
* retrieval restrictions
* PII filtering
* model-version tracking
* logging
* dependency controls

---

# 🧪 Experimentation Framework

## Primary Experiment

### AI Pricing vs. Static Pricing

### Hypothesis

> AI-driven pricing will increase revenue and conversion without materially damaging customer trust or seller economics.

### Experiment Design

* **50/50 traffic split**
* **4-week test window**
* **95% confidence threshold**

### Primary Metric

**Revenue per Active User**

### Secondary Metrics

* Conversion
* AOV
* revenue
* margin
* cart abandonment

### Guardrails

* NPS
* return rate
* complaint rate
* seller margin
* price volatility

### Simulated Result

**Approximately +15% revenue lift with no modeled material degradation in trust guardrails.**

---

# 🧪 Experiment Decision Framework

```text
Hypothesis
    ↓
Control vs Treatment
    ↓
Collect Experiment Data
    ↓
Primary Metric Improved?
    ↓
Guardrails Healthy?
    ↓
Model Quality Acceptable?
    ↓
Cohort Results Acceptable?
    ↓
YES → Stage Rollout
NO  → Iterate / Stop / Rollback
```

---

# 🚦 AI Release Gates

An AI model cannot move directly from offline evaluation to full launch.

```text
Prototype
   ↓
Offline Validation
   ↓
Responsible AI Review
   ↓
Security / Privacy Review
   ↓
Experiment
   ↓
Release Checklist
   ↓
10% Traffic
   ↓
25%
   ↓
50%
   ↓
100%
```

Progression occurs only while business and safety guardrails remain healthy.

---

# 📡 Model Monitoring

Post-launch monitoring includes:

## Model Quality

* Precision
* Recall
* F1
* NDCG
* calibration

## Business

* RPAU
* revenue
* conversion
* AOV
* repeat purchase

## User Experience

* abandonment
* NPS
* complaints
* opt-out behavior

## Reliability

* latency
* error rate
* fallback rate
* availability

## Responsible AI

* cohort performance gaps
* exposure concentration
* privacy incidents
* unsafe GenAI outputs

---

# 📉 Drift Detection

The monitoring framework considers:

### Feature Drift

Changes in input distributions.

### Label Drift

Changes in outcome frequencies.

### Concept Drift

Changes in relationships between user behavior and outcomes.

### Seasonal Drift

Changes caused by:

* Holidays
* promotions
* economic conditions
* inventory
* changing customer behavior

Retraining is **not automatically equivalent to deployment**.

A retrained model must pass validation and governance gates before replacing the current champion.

---

# 🔄 Rollback Strategy

Rollback may be triggered by:

* Significant revenue degradation
* model-quality failure
* severe latency
* data-quality failure
* privacy incident
* unfair outcome
* unsafe GenAI behavior

### Rollback Flow

```text
Alert
  ↓
Validate Incident
  ↓
Disable AI Component
  ↓
Activate Safe Fallback
  ↓
Preserve Logs
  ↓
Root Cause Analysis
  ↓
Remediation
  ↓
Revalidation
  ↓
Controlled Relaunch
```

---

# 🚨 AI Incident Response

Incidents are classified according to severity.

### SEV-1

Examples:

* Sensitive-data exposure
* confirmed severe discriminatory behavior
* systemic unsafe GenAI output

### SEV-2

Examples:

* Significant model degradation
* material guardrail breach
* security exploit with limited exposure

### SEV-3

Examples:

* Localized model-quality problem
* non-critical drift
* temporary latency degradation

Every material incident results in:

* Containment
* investigation
* root-cause analysis
* corrective action
* ownership
* documented follow-up

---

# 📈 Data & Analytics Layer

### SQL

Used for:

* Revenue analysis
* cohort analysis
* funnel analysis
* experiment validation
* model-output validation

### Python

Used for:

* Data preparation
* pricing simulations
* elasticity modeling
* behavioral analysis
* model evaluation

### Excel

Used for:

* RICE prioritization
* experiment analysis
* financial modeling
* stakeholder reporting

### Power BI / Tableau

Used conceptually for:

* Revenue Lift Dashboard
* AI Feature Performance
* Funnel Drop-Off
* Cohort Retention
* NPS Sentiment
* Model Health

---

# 📋 Product Prioritization

## RICE Framework

| Feature                 | Reach | Impact | Confidence | Effort |  Score |
| ----------------------- | ----: | -----: | ---------: | -----: | -----: |
| **Dynamic Pricing**     |     8 |      9 |          8 |      6 | **96** |
| **Recommendations**     |     9 |      8 |          7 |      7 | **72** |
| **Abandonment Trigger** |     6 |      7 |          7 |      5 | **58** |

The roadmap prioritizes capabilities according to expected product value, evidence confidence, implementation effort, and risk.

---

# 🏃 Agile Delivery

Delivery is structured through Jira using:

* **3 major epics**
* **18 user stories**
* **2-week sprint cycles**
* sprint backlogs
* acceptance criteria
* subtasks
* stakeholder demos
* delivery tracking

### Cross-Functional Stakeholders

* Product
* Data Science
* Machine Learning
* Engineering
* Analytics
* UX
* Marketing
* Finance
* Security
* Privacy

---

# 👥 AI Governance RACI

Governance establishes clear ownership across:

| Responsibility            | Primary Functions      |
| ------------------------- | ---------------------- |
| **Product Strategy**      | AI Product Manager     |
| **Model Development**     | ML / Data Science      |
| **Data Quality**          | Data Engineering       |
| **Experiment Validation** | Product Analytics      |
| **Privacy**               | Privacy / Legal        |
| **Security**              | Security               |
| **UX / User Autonomy**    | Product Design         |
| **Model Operations**      | ML Engineering / MLOps |

This prevents AI governance from becoming an undefined shared responsibility.

---

# 🎨 UX & Design

Product-design artifacts include:

* User Journey Map
* AI Pricing Decision Flow
* Personalization Wireframes
* Information Architecture
* Funnel Optimization Model
* AI Revenue Dashboard

UX decisions are evaluated against both:

**Conversion performance AND customer trust**

---

# 🗺️ AI Product Lifecycle

```text
Business Opportunity
        ↓
Product Discovery
        ↓
AI Feasibility
        ↓
Data Readiness
        ↓
PRD / Requirements
        ↓
Model Prototype
        ↓
Offline Evaluation
        ↓
Responsible AI Review
        ↓
Experimentation
        ↓
Release Approval
        ↓
Staged Deployment
        ↓
Monitoring
        ↓
Drift / Risk Review
        ↓
Retrain • Recalibrate • Rollback • Retire
```

---

# 📂 AI Governance Artifacts

The project includes documentation across:

### 🧠 AI Model

* System Model Card
* Recommendation Model Card
* Cart-Abandonment Model Card
* Price-Response Model Card
* Generative AI Model Card
* Feature Inventory
* Data Dictionary
* Training & Evaluation Methodology
* Model Registry

### ⚖️ AI Risk Management

* AI Risk Register
* Responsible AI Framework
* Fairness Assessment
* Privacy Assessment
* AI Threat Model
* Red-Team Report

### 🛡️ Governance

* Governance RACI
* Release Checklist
* Decision Log
* Model Lifecycle Plan
* AI Incident Response

### 🧪 Experimentation

* Experiment Pre-Registration
* Experiment Results
* Launch Decision Memo
* Guardrail Framework

### 📡 Monitoring

* Model Monitoring Plan
* Drift Thresholds
* Rollback Runbook
* Performance Thresholds

---

# 🏆 AI Product Management Competencies Demonstrated

### Product

✔ AI Product Strategy
✔ Product Discovery
✔ PRDs
✔ Functional Requirements
✔ User Stories
✔ Acceptance Criteria
✔ Product Roadmapping
✔ RICE Prioritization
✔ Agile Delivery

### AI / ML

✔ Dynamic Pricing
✔ Recommendation Systems
✔ Propensity Modeling
✔ Behavioral Segmentation
✔ AI Model Evaluation
✔ Model Cards
✔ Generative AI

### Analytics

✔ SQL
✔ Python
✔ Revenue Analytics
✔ Funnel Analysis
✔ KPI Architecture
✔ Cohort Analysis

### Experimentation

✔ A/B Testing
✔ Hypothesis Development
✔ Primary & Secondary Metrics
✔ Guardrails
✔ Statistical Decision-Making
✔ Launch Decisions

### Responsible AI

✔ AI Risk Management
✔ Fairness Assessment
✔ Privacy & Consent
✔ AI Governance
✔ Threat Modeling
✔ Red-Team Testing
✔ User Autonomy

### AI Operations

✔ Model Monitoring
✔ Drift Detection
✔ Model Registry
✔ Versioning
✔ Incident Response
✔ Rollback Planning
✔ Model Lifecycle Management

---

# 🧰 Product & Technical Stack

| Area                   | Tools / Methods                               |
| ---------------------- | --------------------------------------------- |
| **Product Management** | PRDs, Roadmaps, RICE, User Stories            |
| **Agile**              | Jira, Sprint Planning, Backlog Management     |
| **Analytics**          | SQL, Excel, Product Analytics                 |
| **Programming**        | Python, Pandas                                |
| **AI/ML**              | Pricing, Ranking, Recommendations, Propensity |
| **Generative AI**      | Grounding, Evaluation, Safety Guardrails      |
| **Experimentation**    | A/B Testing, Statistical Evaluation           |
| **Responsible AI**     | Fairness, Privacy, Risk Registers             |
| **AI Governance**      | Model Cards, RACI, Release Gates              |
| **MLOps Concepts**     | Monitoring, Drift, Versioning, Rollback       |
| **Visualization**      | Power BI, Tableau                             |
| **UX**                 | User Journeys, Wireframes, Decision Flows     |

---

# 📁 Repository Structure

```text
AI_Ecommerce_Revenue_Optimizer/
│
├── Dashboard/
│
├── Data_Analytics/
│   ├── SQL
│   ├── Python
│   ├── Dataset
│   └── Experiment Analysis
│
├── Docs/
│   ├── PRD
│   ├── Roadmap
│   └── Product Documentation
│
├── Executive_Summary/
│
├── Jira/
│   ├── Backlog
│   ├── Sprint Board
│   ├── User Stories
│   └── Subtasks
│
├── Planning/
│
├── UX_Design/
│
├── AI_Model/
│   ├── Model Cards
│   ├── Feature Inventory
│   ├── Data Dictionary
│   └── Evaluation Methodology
│
├── AI_Risk_Management/
│   ├── AI Risk Register
│   ├── Fairness Assessment
│   ├── Privacy Assessment
│   ├── Threat Model
│   └── Red-Team Report
│
├── Governance/
│   ├── RACI
│   ├── Model Registry
│   ├── Release Checklist
│   ├── Decision Log
│   └── Incident Response
│
├── Experimentation/
│   ├── Pre-Registration
│   └── Launch Decision Memo
│
├── Monitoring/
│   ├── Monitoring Plan
│   ├── Drift Thresholds
│   └── Rollback Runbook
│
└── README.md
```

---

# 💼 What This Project Demonstrates

This case study demonstrates the ability to:

* Identify high-impact AI product opportunities
* Translate revenue problems into AI product requirements
* Connect model outputs to measurable business outcomes
* Define business, product, model, and guardrail metrics
* Evaluate recommendation and predictive models
* Design controlled experiments
* Prioritize an AI roadmap
* Coordinate cross-functional delivery
* Identify Responsible AI risks
* Establish AI governance
* Define model release criteria
* Monitor AI systems after launch
* Respond to model failures
* Make evidence-based launch and rollback decisions

> **The goal is not simply to build an AI feature. The goal is to build an AI product that creates measurable value while remaining trustworthy, governable, observable, and safe to operate.**

---

# 👤 About the Author

## Jamie Christian II

**AI Product Management • Product Strategy • Product Analytics • Responsible AI**

Portfolio focus:

* 🤖 AI-Powered Products
* 💰 Revenue Optimization
* 🎯 Personalization
* 📊 Product Analytics
* 🧪 Experimentation
* ⚖️ Responsible AI
* 🛡️ AI Governance

**GitHub:**
https://github.com/JamieChristian22

**LinkedIn:**
https://www.linkedin.com/in/jamiechristian2/

---

## ⭐ Project Focus

**AI Product Strategy • Revenue Optimization • Dynamic Pricing • Recommendation Systems • Experimentation • Responsible AI • AI Governance**

---

## 📄 License

This project is part of the **AI Product Manager Portfolio** and is available for portfolio and educational purposes under the repository's MIT License.
