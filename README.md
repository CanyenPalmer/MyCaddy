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

## Data Science & Analytics Overview

MyCaddy is an applied data science system that combines deterministic modeling, feature engineering, and rule-based decision systems to support both real-time decision-making and post-round performance analysis.

The system leverages:
- Feature engineering (wind, elevation, temperature, lie variables)
- Exploratory Data Analysis (EDA) and performance evaluation
- Statistical modeling and proportional scaling
- Rule-based decision systems for structured output generation

Model validation and evaluation are performed through:
- Iterative testing across environmental scenarios
- Performance benchmarking against expected outcomes
- Consistency checks to ensure stability and reproducibility

Outputs are designed to be:
- Fully interpretable (no black-box modeling)
- Deterministic and reproducible
- Aligned with real-world decision workflows

---

## Overview

MyCaddy is a structured golf performance system designed to support both **in-round decision making** and **post-round improvement**.

Rather than focusing on a single feature, the platform is built around two distinct tools that mirror how serious golfers actually operate:

> Make better decisions during the round.  
> Learn from the round afterward.

---

## MyCaddy Platform (v2.1.1)

MyCaddy has evolved into a two-system golf performance platform:

### MyCaddy (In-Round Tool)

A physics-informed carry distance engine designed for real-time decision making.

- Answers: *“What does this shot play like?”*
- Focus: speed, clarity, and trust during a round
- Produces a **plays-like carry distance**, not a club recommendation

---

### MyCoach (Post-Round Tool)

A structured coaching engine that analyzes round performance and produces targeted improvement plans.

- Answers: *“What did this round reveal about my game?”*
- Focus: development, pattern recognition, and practice direction
- Uses PGA Tour benchmarks and rule-based evaluation logic

---

### System Philosophy

The tools are intentionally separated:

- MyCaddy operates **during play**
- MyCoach operates **after the round**

This separation ensures:
- no cognitive overload during a round
- clear, focused improvement after the round

---

## Project Purpose

Golf performance depends on two things:

1. Making correct decisions under varying conditions  
2. Understanding what actually impacted your score  

MyCaddy addresses both.

---

## Core Calculation Model (MyCaddy)

The carry engine follows a deterministic adjustment pipeline:

1. **Base Distance**
   - User-provided yardage

2. **Lie Adjustment**
   - Nonlinear percentage penalty

3. **Elevation**
   - 3 feet ≈ 1 yard

4. **Wind**
   - Directional decomposition
   - Cosine scaling for diagonal wind

5. **Temperature**
   - ~1% carry change per 10°F

6. **Final Output**
   - Stock Target
   - Plays-Like Range
   - Caddy Insight

---

## Interface and Decision System

### Output Hierarchy

- **Stock Target** → primary number  
- **Plays-Like Range** → variability band  
- **Caddy Insight** → explanation  

### Visualization

- Distance progression bar  
- Scroll-triggered animations  
- Temperature-based color encoding  

### Interaction

- Typing-based insight delivery  
- Avatar feedback  
- Mobile-first design  

---

## MyCoach Engine (v2.1.1)

MyCoach is a rule-based performance analysis system.

### Inputs

- Score and par  
- Fairways hit  
- Greens in regulation  
- Putts and three-putts  
- Scrambling  
- Penalties  
- Miss patterns  
- Round issues  

---

### Output Structure

- **Round Tier** (performance classification)  
- **PGA Tour comparison metrics**  
- **Strengths**  
- **Ranked weaknesses**  
- **Primary focus (single or dual)**  
- **Practice plan with real drills**  

---

### Coaching Logic

- Uses **PGA Tour Top 10, Top 50, and Average benchmarks**
- Ranks weaknesses based on scoring impact
- Determines whether to assign:
  - single focus
  - dual focus
- Maps each weakness to a **specific drill**

---

### Design Principles

- No over-coaching  
- No fabricated weaknesses  
- Focus prioritization  
- Direct mapping:  
  **problem → drill → improvement path**

---

### Practice System

The practice engine assigns **real drills**, such as:

- Distance Ladder Approach Drill  
- Tee Shot Start-Line Gate Drill  
- Up-and-Down Challenge  
- Death Star Putting Drill  

Each drill includes:
- setup  
- execution  
- goal  
- purpose  

---

## Wind Modeling

- Headwind / tailwind → distance modifier  
- Crosswind → informational  
- Diagonal → cosine scaled  

---

## Lie Penalty System

- Fairway → none  
- First cut → minimal  
- Rough → moderate  
- Heavy rough → severe  

---

## Temperature Scaling

- Warmer → more carry  
- Colder → less carry  

Approximation:
- ~1% per 10°F  

---

## Flyer Logic

| Condition | Behavior |
|----------|----------|
| Light rough | Adjusted range |
| Heavy rough | Uncertainty warning |

---

## Performance Philosophy

The system is built on:

- **Speed**
- **Stability**
- **Clarity**
- **Trust**

---

## Technology Stack

- Python 3  
- Flask  
- HTML / CSS  
- Custom modeling logic  

---

## Target Users

- Developing golfers  
- Amateur players  
- Competitive players  
- Advanced players  

---

## Validation Status

Tested across:

- Wind scenarios  
- Elevation  
- Temperature  
- Lie conditions  
- Round performance profiles  

Expected accuracy:
> ±2–5 yards under realistic inputs  

---

## Roadmap

- Player-specific calibration  
- Shot dispersion modeling  
- Multi-round tracking (MyCoach expansion)  
- Additional environmental variables  

---

## Disclaimer

MyCaddy estimates:

- Carry distance only  
- Does not account for rollout  
- Does not select clubs  

Final decisions remain with the player.

---

## Summary

MyCaddy is a structured golf decision and coaching system that combines:

- Physics-based modeling  
- Data-driven evaluation  
- Real-world golf strategy  

It bridges the gap between:

- **in-round execution**
- **post-round improvement**

Version v2.1.1 represents a stable, production-ready implementation suitable for real-world use.
