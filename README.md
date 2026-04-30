# MyCaddy: Caddie-Style Golf Carry Distance Calculator

[![Live on Render](https://img.shields.io/badge/Render-Live%20Demo-46E3B7?logo=render\&logoColor=white)](https://mycaddy.onrender.com)
![GitHub last commit](https://img.shields.io/github/last-commit/CanyenPalmer/MyCaddy)
![GitHub repo size](https://img.shields.io/github/repo-size/CanyenPalmer/MyCaddy)
![Top language](https://img.shields.io/github/languages/top/CanyenPalmer/MyCaddy)
![Language count](https://img.shields.io/github/languages/count/CanyenPalmer/MyCaddy)

**Author:** Palmer Projects
**License:** © Palmer Projects. All rights reserved.

---

## 🧠 Overview

**MyCaddy** is a physics-informed, caddie-style golf calculator that determines the **true “plays-like” carry distance** for a shot based on real on-course conditions.

Rather than telling a player *what club to hit*, MyCaddy answers the more fundamental question:

> **“What carry yardage should this shot actually play as?”**

This mirrors how elite golfers and professional caddies build numbers during competition.

---

## 🎯 Project Purpose

MyCaddy addresses the variability in golf shot distances caused by environmental and lie conditions. Rather than relying solely on flat-yardage numbers, this tool adjusts shot carry predictions by incorporating real-world influences, offering practical assistance both on the course and during preparation.

---

## ⚙️ Core Features

### ✅ Caddie-Style Carry Calculation

* Outputs a **plays-like carry distance**
* Designed for fast, in-round decision making

---

### 🌬️ Advanced Wind Modeling

* Supports:

  * Headwind / Tailwind
  * Crosswind
  * Quartering wind (diagonal decomposition)

* Diagonal winds are scaled using:

  * **~70.7% effective component (cos 45°)**

---

### 🌱 Nonlinear Lie Penalty System

* Models realistic strike degradation:

  * First cut → minimal impact
  * Rough → moderate penalty
  * Deep rough → severe penalty

* Uses a **bounded, stable curve**

* Adapts across different course conditions

---

### ⛰️ Elevation Adjustment

* Uses standard golf conversion:

  * **3 feet ≈ 1 yard**

* Supports:

  * Uphill
  * Downhill
  * Flat (default)

---

### 🌡️ Temperature Scaling

* Adjusts distance based on air density:

  * ~**1% distance change per 10°F**

---

### 🎯 Flyer Logic (Context-Aware)

* User-controlled (not assumed)
* Behavior depends on lie:

| Lie Condition                | Output                             |
| ---------------------------- | ---------------------------------- |
| ≤ 50% (light/moderate rough) | Shows **flyer range (90–95%)**     |
| ≥ 75% (deep rough)           | Shows **warning instead of range** |

This prevents unrealistic precision in poor lies.

---

### 📊 Live Condition Summary

* Displays all user inputs in real time
* Ensures transparency and validation before shot execution

---

## ⚡ Performance Philosophy

MyCaddy is designed to be:

* **Fast** → usable mid-round
* **Accurate** → grounded in real golf principles
* **Simple** → no unnecessary inputs
* **Trustworthy** → no unstable or exaggerated outputs

---

## 🧰 Technology Stack

* **Python 3**
* **Flask (Web Application)**
* **HTML / CSS (Frontend UI)**
* **Custom Mathematical Functions**:

  * Wind decomposition
  * Elevation conversion
  * Temperature scaling
  * Lie penalty modeling

---

## 🎯 Target Users

* **Beginners** → learn how conditions affect distance
* **Amateurs** → improve course management
* **Competitive golfers** → refine decision-making
* **Advanced players** → simulate tournament-style conditions

---

## 🚀 Live Demo

👉 [**MyCaddy Live Application**](https://mycaddy.onrender.com)

---

## 🧪 Validation

The model has been tested across:

* Wind scenarios (head, tail, cross, diagonal)
* Temperature extremes
* Elevation changes
* Lie conditions (0% → 100%)
* Flyer and non-flyer scenarios

Typical carry accuracy:

> **±2–5 yards under realistic input conditions**

---

## 🔮 Future Roadmap

* Player-specific profiles (premium tier)
* Trajectory-aware adjustments
* Advanced environmental modeling (altitude, humidity)
* Shot dispersion modeling

---

## ⚠️ Disclaimer

MyCaddy calculates **carry distance only**.

It does not account for:

* Rollout
* Player-specific swing execution
* Club selection

Final shot decisions remain the responsibility of the player.

---

## 🏁 Summary

MyCaddy bridges the gap between:

> **simple yardage tools** and **professional-style shot calculation**

delivering a fast, realistic, and highly usable carry distance model for real-world golf.


