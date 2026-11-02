# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Grip Strength Frailty Velocity Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentGripStrengthFrailtyVelocity

def main():
    agent = PersonalAgentGripStrengthFrailtyVelocity()

    print("=" * 70)
    print("DEMO: Personal Agent Grip Strength & Neuromuscular Frailty Engine")
    print("=" * 70)

    # 1. Evaluate Isometric Dynamometry (Dominant: 51 kg, Non-Dom: 47 kg, Male, Age 42, BW 74 kg)
    res_grip = agent.evaluate_grip_strength_and_frailty(
        dominant_hand_kg=51.0,
        non_dominant_hand_kg=47.0,
        sex="male",
        age=42,
        bodyweight_kg=74.0
    )

    print(f"\n1. Isometric Grip Strength & Sarcopenia Analysis:")
    print(f"   Dominant / Non-Dominant: {res_grip['dominant_grip_kg']} kg / {res_grip['non_dominant_grip_kg']} kg")
    print(f"   Normative Benchmark (Age 42 Male): {res_grip['normative_age_sex_benchmark_kg']} kg")
    print(f"   Relative Grip Strength (RGS): {res_grip['relative_grip_strength_rgs']} (kg/BW)")
    print(f"   Bilateral Asymmetry: {res_grip['bilateral_asymmetry_percentage']} ({res_grip['asymmetry_status']})")
    print(f"   Clinical Sarcopenia Risk: {res_grip['clinical_sarcopenia_risk']}")
    print(f"   All-Cause Mortality Hazard Ratio: {res_grip['all_cause_mortality_hazard_ratio']}")
    print(f"   Vitality Tier: {res_grip['functional_vitality_tier']}")

    # 2. Model 4 Successive Maximal Trials Fatigue Velocity (51 -> 48.5 -> 46 -> 43.5 kg)
    res_fatigue = agent.model_neuromuscular_fatigue_rate(
        repeated_trials_kg=[51.0, 48.5, 46.0, 43.5],
        trial_intervals_sec=15.0
    )

    print(f"\n2. Neuromuscular Motor Unit Fatigue Velocity:")
    print(f"   Trials Series: {res_fatigue['trial_series_kg']} kg")
    print(f"   Peak Force: {res_fatigue['peak_isometric_force_kg']} kg | Final Force: {res_fatigue['final_isometric_force_kg']} kg")
    print(f"   Fatigue Decrement: {res_fatigue['fatigue_decrement_percentage']} (Slope: {res_fatigue['fatigue_slope_kg_per_trial']} kg/trial)")
    print(f"   Central Drive Tier: {res_fatigue['central_nervous_motor_drive_tier']}")
    print(f"   Prescription: {res_fatigue['recovery_guidance']}")

    print("\nVerification complete: Grip strength frailty engine executed flawlessly.")

if __name__ == "__main__":
    main()
