---
name: genpark-personal-agent-grip-strength-frailty-velocity-skill
version: "1.0.0"
description: "Zero-dependency isometric grip dynamometry modeler, PURE study mortality hazard quantifier, bilateral asymmetry indexer, and neuromuscular motor drive fatigue evaluator."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Grip Strength Frailty Velocity Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI assistants to evaluate isometric muscular capacity, compute Relative Grip Strength (RGS) normalized by bodyweight, quantify clinical sarcopenia risk, evaluate all-cause mortality hazard ratios from the prospective PURE Lancet trial, and track motor unit central fatigue rates across successive maximal contractions.

## Agent In-Context Capabilities

- **Clinical Sarcopenia Screening**: Compares dominant grip strength against age/sex-stratified European Working Group on Sarcopenia in Older People (EWGSOP2) cutoffs.
- **PURE Mortality Hazard Ratio**: Calculates the exponential hazard ratio associated with strength deficits below normative population references.
- **Bilateral Asymmetry Tracking**: Identifies lateral compensation patterns ($> 12\%$) signaling unilateral neuromuscular impairment.

## Tools Summary

1. `evaluate_grip_strength_and_frailty`: Computes RGS, bilateral asymmetry percentage, and PURE mortality hazard ratio.
2. `model_neuromuscular_fatigue_rate`: Calculates fatigue slope and motor drive retention across repeated isometric trials.
