# MyCaddy: Golf Decision & Coaching System

[![Live on Render](https://img.shields.io/badge/Render-Live%20Demo-46E3B7?logo=render&logoColor=white)](https://mycaddy.onrender.com)

**Author:** Palmer Projects  
**Version:** v2.1.1  

---

## Case Study

MyCaddy is an applied data science and analytics system designed to model real-world golf conditions and translate them into interpretable, high-confidence decision outputs. The project was developed to address two fundamental gaps in golf performance: the lack of structured, data-driven decision-making during play, and the absence of a consistent analytical framework for evaluating performance after a round.

Traditional golf decision-making is largely heuristic. Players rely on static yardage, subjective adjustments, and incomplete environmental interpretation. This introduces variability that directly impacts scoring outcomes. At the same time, post-round evaluation is typically unstructured, preventing players from identifying statistically meaningful weaknesses or establishing a repeatable improvement process. MyCaddy approaches both problems through a unified data pipeline that supports real-time inference and post-hoc analysis within a single system.

---

## Methodology

The system is built on a deterministic modeling framework supported by structured feature engineering and applied statistical reasoning. Input variables were selected based on their influence on ball flight and scoring outcomes, including wind, elevation, temperature, and lie conditions. Each variable is transformed through engineered features designed to approximate real-world physics while maintaining computational efficiency and interpretability.

Wind is modeled using vector decomposition, allowing directional components such as headwind, tailwind, and diagonal wind to be represented independently. Elevation is approximated using a linear transformation, while temperature is incorporated through proportional scaling as a proxy for air density. Lie conditions are represented through nonlinear penalty functions to capture the variability in strike quality across different surfaces. These transformations form a consistent modeling pipeline in which raw inputs are converted into structured features and aggregated into a single output variable representing effective carry distance.

The system deliberately avoids black-box machine learning in favor of deterministic and interpretable modeling. This design choice ensures reproducibility, stability across edge cases, and alignment with real-world decision-making processes where transparency is critical.

---

## System Design and Analytics Framework

MyCaddy operates as a dual-system architecture composed of a real-time inference engine and a post-round analytics engine. The in-round component functions as a deterministic prediction system, converting engineered features into a “plays-like” carry distance. Outputs are structured hierarchically, with a primary decision variable supported by an uncertainty band and a contextual explanation layer. This output design reflects principles of human-centered analytics, where clarity and usability are prioritized alongside accuracy.

The post-round component extends the pipeline into a formal evaluation framework. Performance data is analyzed using comparative benchmarking against PGA Tour distributions, including top-tier and average performance levels. Metrics are evaluated using a gap-based classification system, allowing performance to be segmented into interpretable tiers such as strength, moderate gap, or major gap. This introduces standardization into what is typically a subjective evaluation process.

A rule-based decision system is then applied to transform analytical findings into actionable outputs. Weaknesses are ranked according to severity and scoring impact, and a constrained optimization approach is used to determine whether a single focus area or multiple areas should be prioritized. This ensures that recommendations remain targeted and avoids overfitting feedback to noise within a single round. The final outputs include structured insights, prioritized improvement areas, and mapped practice interventions, forming a closed-loop system from data ingestion to decision support.

---

## Results and Impact

The modeling system demonstrates an expected accuracy of approximately ±2–5 yards under realistic environmental conditions, with stable outputs observed across a wide range of input scenarios. More importantly, the system maintains full interpretability, allowing users to trace outputs back to their underlying feature transformations and modeling assumptions. This transparency is critical in establishing trust and enabling users to incorporate the system into real decision-making workflows.

From an analytics perspective, the project demonstrates the ability to design and implement an end-to-end data pipeline that integrates feature engineering, deterministic modeling, performance evaluation, and rule-based decision systems. It highlights how data science techniques can be applied outside traditional domains to solve domain-specific problems with measurable impact.

Ultimately, MyCaddy bridges the gap between real-time decision-making and long-term performance improvement. By combining modeling accuracy with structured analytics and interpretable outputs, the system provides both immediate utility during play and a scalable framework for continuous improvement over time.
