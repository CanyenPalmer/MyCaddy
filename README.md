# MyCaddy: Caddie-Style Golf Carry Distance Calculator

[![Live on Render](https://img.shields.io/badge/Render-Live%20Demo-46E3B7?logo=render&logoColor=white)](https://mycaddy.onrender.com)
![GitHub last commit](https://img.shields.io/github/last-commit/CanyenPalmer/MyCaddy)
![GitHub repo size](https://img.shields.io/github/repo-size/CanyenPalmer/MyCaddy)
![Top language](https://img.shields.io/github/languages/top/CanyenPalmer/MyCaddy)
![Language count](https://img.shields.io/github/languages/count/CanyenPalmer/MyCaddy)

**Author:** Palmer Projects  
**Version:** v2.1.1  
**License:** © Palmer Projects. All rights reserved.

---

## Overview

MyCaddy is a physics-informed golf carry distance calculator designed to estimate the true “plays-like” yardage of a shot under real on-course conditions.

Rather than recommending a club selection, the system focuses on a more fundamental question:

> What carry distance should this shot effectively play as?

This approach mirrors how competitive golfers and professional caddies construct numbers in tournament environments.

---

## Project Purpose

Carry distance in golf is highly sensitive to environmental and lie-based variables. Static yardage alone is insufficient for consistent decision-making.

MyCaddy introduces a structured adjustment framework that incorporates:

- Lie conditions
- Elevation change
- Wind speed and direction
- Temperature

The goal is to produce a **stable, interpretable carry estimate** that improves decision quality without increasing cognitive load.

---

## Core Calculation Model

The model follows a deterministic adjustment pipeline:

1. **Base Distance**
   - User-provided yardage to target

2. **Lie Adjustment**
   - Nonlinear percentage-based penalty
   - Reflects strike degradation and energy transfer loss

3. **Elevation Adjustment**
   - Converted using:
     - 3 feet ≈ 1 yard

4. **Wind Adjustment**
   - Directional decomposition:
     - Headwind / tailwind
     - Crosswind
     - Quartering wind (cosine-based scaling ~0.707)

5. **Temperature Adjustment**
   - Air density proxy:
     - ~1% carry change per 10°F deviation

6. **Final Output**
   - Stock Target (primary decision value)
   - Plays-Like Range (uncertainty band)
   - Caddy Insight (interpretable explanation)

---

## Interface and Decision System (v2.1.1)

The application has evolved from a pure calculation tool into a structured decision interface.

### Output Hierarchy

- **Stock Target**
  - Primary carry number
  - Intended to be trusted and acted upon

- **Plays-Like Range**
  - Secondary contextual band
  - Represents variability, not indecision

- **Caddy Insight**
  - Natural-language interpretation of conditions
  - Translates model adjustments into human-readable reasoning

### Visualization Layer

- Distance progression bar:
  - Displays base vs adjusted carry
  - Reinforces magnitude of adjustment

- Scroll-triggered animation:
  - Activates only when visible
  - Avoids wasted interaction on mobile

- Temperature color encoding:
  - Cold → neutral → hot spectrum
  - Provides quick environmental interpretation

### Interaction Design

- Typing-based insight delivery
- Subtle avatar feedback during output
- Mobile-first layout optimized for in-round use

---

## Wind Modeling

Wind effects are decomposed into directional components:

- Headwind / tailwind → primary distance modifier
- Crosswind → informational (non-distance altering)
- Diagonal wind → scaled using cosine decomposition

This ensures stability and avoids exaggerated wind effects.

---

## Lie Penalty System

The lie model applies a bounded nonlinear penalty:

- Fairway → no penalty
- First cut → minimal reduction
- Rough → moderate degradation
- Heavy rough → severe penalty

The system is designed to:
- Avoid unrealistic extremes
- Maintain consistency across varying conditions
- Reflect real strike variability rather than deterministic loss

---

## Elevation Adjustment

Elevation is converted using a standard approximation:

- 3 feet of elevation change ≈ 1 yard of carry adjustment

Supports:
- Uphill
- Downhill
- Flat

---

## Temperature Scaling

Temperature is treated as a proxy for air density:

- Warmer air → reduced resistance → increased carry
- Colder air → increased resistance → reduced carry

Approximation used:
- ~1% carry change per 10°F

---

## Flyer Logic

Flyer behavior is context-dependent and user-controlled.

| Lie Condition                | Behavior                          |
|----------------------------|----------------------------------|
| ≤ 50% rough severity        | Provides flyer-adjusted range     |
| ≥ 75% rough severity        | Displays uncertainty warning      |

This prevents false precision in poor lies while still offering actionable information.

---

## Performance Philosophy

The system is designed around four constraints:

- **Speed** — usable during play
- **Stability** — no volatile outputs
- **Clarity** — minimal interpretation required
- **Trust** — consistent directional behavior

---

## Technology Stack

- Python 3
- Flask
- HTML / CSS (mobile-first UI)
- Custom mathematical modeling functions

---

## Target Users

- Developing golfers learning environmental effects
- Amateur players improving course management
- Competitive players refining decision processes
- Advanced players simulating tournament conditions

---

## Validation Status

The model has been evaluated across:

- Wind scenarios (head, tail, cross, diagonal)
- Elevation changes
- Temperature ranges
- Lie conditions
- Flyer and non-flyer cases

Expected performance:

> Designed to fall within approximately ±2–5 yards under realistic inputs, pending real-course validation.

---

## Roadmap

Future development directions include:

- Player-specific calibration
- Shot dispersion modeling
- Expanded environmental variables (altitude, humidity)
- Decision-support extensions (club recommendation layer)

---

## Disclaimer

MyCaddy estimates carry distance only.

It does not account for:

- Rollout
- Individual swing variability
- Club selection

Final decisions remain the responsibility of the player.

---

## Summary

MyCaddy provides a structured method for translating raw yardage into a condition-adjusted carry value.

It operates at the intersection of:

- Applied physics
- Data modeling
- On-course decision systems

The current version (v2.1.1) represents a stable, test-ready implementation suitable for real-world validation.

