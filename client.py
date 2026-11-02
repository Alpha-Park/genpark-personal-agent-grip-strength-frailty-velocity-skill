# -*- coding: utf-8 -*-
"""Personal Agent Grip Strength Frailty Velocity Skill.

Zero-dependency isometric grip dynamometry modeler, PURE study mortality hazard quantifier,
bilateral asymmetry indexer, and neuromuscular motor drive fatigue evaluator.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentGripStrengthFrailtyVelocity:
    """Quantitative neuromuscular vitality and biological frailty engine based on
    the Prospective Urban Rural Epidemiology (PURE) trial and Fried frailty phenotype standards."""

    # Normative median grip strength benchmarks by sex and age bracket (kg)
    NORMATIVE_BENCHMARKS = {
        "male": {
            (18, 29): 47.0,
            (30, 39): 49.0,
            (40, 49): 46.5,
            (50, 59): 43.0,
            (60, 69): 38.0,
            (70, 99): 31.0
        },
        "female": {
            (18, 29): 28.5,
            (30, 39): 31.0,
            (40, 49): 29.5,
            (50, 59): 27.0,
            (60, 69): 24.0,
            (70, 99): 19.5
        }
    }

    def evaluate_grip_strength_and_frailty(
        self,
        dominant_hand_kg: float = 48.0,
        non_dominant_hand_kg: float = 44.0,
        sex: str = "male",
        age: int = 42,
        bodyweight_kg: float = 75.0
    ) -> Dict[str, Any]:
        """Calculates relative grip strength (RGS), bilateral asymmetry percentage,
        clinical sarcopenia threshold clearance, and all-cause mortality hazard ratio."""
        dom = max(5.0, float(dominant_hand_kg))
        non_dom = max(4.0, float(non_dominant_hand_kg))
        gender = "female" if sex.lower().startswith("f") else "male"
        a = max(18, int(age))
        bw = max(35.0, float(bodyweight_kg))

        # Lookup normative median
        norm_map = self.NORMATIVE_BENCHMARKS[gender]
        norm_ref = 45.0 if gender == "male" else 28.0
        for (low, high), val in norm_map.items():
            if low <= a <= high:
                norm_ref = val
                break

        # Relative Grip Strength (Normalized to body mass: RGS)
        rgs = round(dom / bw, 3)

        # Bilateral Asymmetry Index
        asymmetry_pct = round((abs(dom - non_dom) / dom) * 100.0, 1)

        # Fried Frailty / EWGSOP2 Sarcopenia Threshold: < 27 kg (males), < 16 kg (females)
        sarcopenia_cutoff = 27.0 if gender == "male" else 16.0
        sarcopenia_flag = dom < sarcopenia_cutoff

        # PURE Study Mortality Hazard Ratio (HR):
        # 16% increase in all-cause mortality per 5 kg decrement below normative reference
        # HR = exp(0.030 * max(0, norm_ref - dom))
        deficit = max(0.0, norm_ref - dom)
        hazard_ratio = round(math.exp(0.030 * deficit), 2)

        # Functional Neuromuscular Tier
        if dom >= norm_ref * 1.15:
            tier = "Superior Neuromuscular Capacity / High Robustness"
        elif dom >= norm_ref * 0.90:
            tier = "Normative Biological Age Vitality"
        elif dom >= sarcopenia_cutoff:
            tier = "Sub-Optimal Grip Strength / Pre-Sarcopenic Vulnerability"
        else:
            tier = "Clinical Sarcopenia & Elevated Frailty Risk"

        return {
            "dominant_grip_kg": dom,
            "non_dominant_grip_kg": non_dom,
            "normative_age_sex_benchmark_kg": norm_ref,
            "relative_grip_strength_rgs": rgs,
            "bilateral_asymmetry_percentage": f"{asymmetry_pct}%",
            "asymmetry_status": "Normative physiological dominance (< 12%)" if asymmetry_pct <= 12.0 else "Significant bilateral asymmetry (> 12% - assess cervical/shoulder motor chain)",
            "clinical_sarcopenia_risk": sarcopenia_flag,
            "all_cause_mortality_hazard_ratio": hazard_ratio,
            "functional_vitality_tier": tier,
            "strength_deficit_kg": round(deficit, 1)
        }

    def model_neuromuscular_fatigue_rate(
        self,
        repeated_trials_kg: List[float],
        trial_intervals_sec: float = 15.0
    ) -> Dict[str, Any]:
        """Evaluates neuromuscular motor unit fatigue slope across 3-5 successive isometric trials."""
        if not repeated_trials_kg or len(repeated_trials_kg) < 2:
            return {"error": "Minimum 2 trials required for fatigue velocity"}

        trials = [float(x) for x in repeated_trials_kg]
        peak_val = max(trials)
        final_val = trials[-1]

        # Fatigue decrement percentage
        decrement_pct = round(((peak_val - final_val) / peak_val) * 100.0, 1)

        # Linear fatigue slope (kg drop per trial)
        n = len(trials)
        slope = round((final_val - trials[0]) / (n - 1), 2)

        # Central Motor Drive vs Peripheral Fatigue Tier:
        # Rapid drop (> 20% in 3 trials) indicates central nervous motor fatigue
        if decrement_pct <= 10.0:
            recovery_tier = "High Neuromuscular Endurance / Stable Central Drive"
        elif decrement_pct <= 22.0:
            recovery_tier = "Normative High-Threshold Motor Unit Depletion"
        else:
            recovery_tier = "Acute Central Drive Attenuation / Elevated Neural Fatigue"

        return {
            "trial_series_kg": trials,
            "peak_isometric_force_kg": peak_val,
            "final_isometric_force_kg": final_val,
            "fatigue_decrement_percentage": f"{decrement_pct}%",
            "fatigue_slope_kg_per_trial": slope,
            "central_nervous_motor_drive_tier": recovery_tier,
            "recovery_guidance": (
                "Allow at least 90-120 seconds between maximal isometric efforts to replenish phosphocreatine (PCr) stores."
                if decrement_pct > 15.0 else
                "Neuromuscular recovery and peripheral motor pool recruitment are optimal."
            )
        }
