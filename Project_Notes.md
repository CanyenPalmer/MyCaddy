# MyCaddy: Golf Decision & Coaching System

[![Live on Render](https://img.shields.io/badge/Render-Live%20Demo-46E3B7?logo=render&logoColor=white)](https://mycaddy.onrender.com)
![GitHub last commit](https://img.shields.io/github/last-commit/CanyenPalmer/MyCaddy)
![GitHub repo size](https://img.shields.io/github/repo-size/CanyenPalmer/MyCaddy)
![Top language](https://img.shields.io/github/languages/top/CanyenPalmer/MyCaddy)
![Language count](https://img.shields.io/github/languages/count/CanyenPalmer/MyCaddy)

**Author:** Palmer Projects  
**Version:** v2.1.1  
**License:** © Palmer Projects. All rights reserved.

---

# Data Science & System Design Overview

Golf performance depends on both **accurate decision-making under variable conditions** and the ability to **analyze outcomes to improve future performance**. MyCaddy addresses both problems through a structured modeling and analytics system.

---

## Problem Context

Traditional golf decision-making relies on static yardage and intuition, which fails to account for:

- Environmental variability (wind, elevation, temperature)
- Lie-based strike degradation
- Round-to-round performance inconsistency
- Lack of structured post-round analysis

---

## System Design

The platform is built as a **dual-system architecture**:

- **MyCaddy:** Real-time deterministic modeling engine for carry distance  
- **MyCoach:** Post-round analytics and decision system for performance evaluation  

This separation ensures:
- low cognitive load during play  
- structured, high-signal feedback after play  

---

## Data Modeling & Feature Engineering

Key input variables were engineered to represent real-world golf conditions:

- Wind (directional vector decomposition)
- Elevation (continuous vertical scaling)
- Lie condition (nonlinear penalty modeling)
- Temperature (air density proxy)

The system applies a **deterministic transformation pipeline**:

Input Features → Adjustment Functions → Aggregated Output

---

## Mathematical Modeling

The system incorporates applied mathematical concepts including:

- Linear approximations  
  - Elevation: ~3 ft ≈ 1 yard  

- Trigonometric decomposition  
  - Wind direction resolved into components  
  - Diagonal wind scaled using cosine (~0.707)  

- Nonlinear scaling  
  - Lie penalties modeled as percentage-based degradation  

- Proportional modeling  
  - Temperature: ~1% carry change per 10°F  

- Constraint-based logic  
  - Prevents unrealistic or unstable outputs  

---

## Analytics & Evaluation Framework

A structured evaluation layer compares performance against external benchmarks:

- PGA Tour Top 10 averages  
- PGA Tour Top 50 averages  
- PGA Tour overall averages  

Each metric is classified using a **gap-based severity model**:

- Strength  
- Small Gap  
- Moderate Gap  
- Major Gap  

This enables:
- standardized performance interpretation  
- consistent cross-round comparisons  

---

## Decision System Logic

The MyCoach engine implements a rule-based decision system:

- Weaknesses are ranked by:
  - severity of gap  
  - scoring impact  
  - contextual inputs (miss patterns)  

- Focus selection logic determines:
  - single focus (primary issue)  
  - dual focus (multiple high-impact issues)  

- Constraint rules prevent:
  - over-coaching  
  - unnecessary recommendations  

---

## Output Engineering

The system is designed to produce **interpretable and actionable outputs**:

- Primary decision variable (Stock Target)  
- Contextual uncertainty band (Plays-Like Range)  
- Natural-language explanation layer (Caddy Insight)  
- Coaching outputs:
  - strengths  
  - ranked weaknesses  
  - targeted drills  

All outputs are:
- deterministic  
- interpretable  
- aligned with real-world decision workflows  

---

## Technology Stack

- Python 3  
- Flask  
- HTML / CSS (Mobile-First UI)  
- Custom modeling and analytics logic  

---

## Results & Performance

- Expected accuracy: **±2–5 yards** under realistic conditions  
- Stable outputs across environmental scenarios  
- Fully interpretable model (no black-box behavior)  
- Direct mapping from data → decision → action  

---

# Overview

MyCaddy is a structured golf performance system designed to support both:

- **In-round decision making**
- **Post-round improvement**

Rather than focusing on a single function, the system mirrors how competitive golfers operate:

> Make better decisions during the round.  
> Learn from the round afterward.

---

## MyCaddy Platform (v2.1.1)

### MyCaddy (In-Round Tool)

A physics-informed carry distance engine designed for real-time decision making.

- Answers: *“What does this shot play like?”*  
- Produces a **plays-like carry distance**, not a club recommendation  
- Optimized for speed, clarity, and trust  

---

### MyCoach (Post-Round Tool)

A structured coaching engine that analyzes performance and produces targeted improvement plans.

- Answers: *“What did this round reveal about my game?”*  
- Uses PGA benchmarks and decision logic  
- Outputs drills tied directly to weaknesses  

---

### System Philosophy

- MyCaddy operates **during play**  
- MyCoach operates **after play**  

This ensures:
- minimal cognitive load  
- focused decisions  
- structured improvement  

---

## Core Calculation Model (MyCaddy)

Pipeline:

1. Base Distance  
2. Lie Adjustment  
3. Elevation (3 ft ≈ 1 yd)  
4. Wind Decomposition  
5. Temperature Scaling  

Outputs:
- Stock Target  
- Plays-Like Range  
- Caddy Insight  

---

## MyCoach Engine

### Inputs
- Score / Par  
- Fairways  
- GIR  
- Putts / 3-putts  
- Scrambling  
- Penalties  
- Miss patterns  

---

### Outputs
- Round Tier  
- PGA comparisons  
- Strengths  
- Ranked weaknesses  
- Primary focus (single or dual)  
- Practice plan  

---

### Design Principles
- No over-coaching  
- No fabricated weaknesses  
- Direct mapping:
  - problem → drill  

---

## Target Users

- Amateur golfers  
- Competitive players  
- Data-driven athletes  

---

## Validation

Tested across:
- wind scenarios  
- elevation  
- lie conditions  
- scoring profiles  

Expected:
> ±2–5 yards accuracy  

---

## Roadmap

- Player-specific calibration  
- Multi-round tracking  
- Shot dispersion modeling  

---

## Disclaimer

- Carry distance only  
- No rollout modeling  
- No club selection  

---

## Summary

MyCaddy is a **decision + coaching system** that combines:

- physics-based modeling  
- structured analytics  
- real-world golf strategy  

It bridges:

> execution during the round  
> improvement after the round  
