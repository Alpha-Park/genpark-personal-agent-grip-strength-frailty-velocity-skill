# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Grip Strength Frailty Velocity Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentGripStrengthFrailtyVelocity

mcp = FastMCP("PersonalAgentGripStrengthFrailtyVelocity")
client = PersonalAgentGripStrengthFrailtyVelocity()

@mcp.tool()
def evaluate_grip_strength_and_frailty(
    dominant_hand_kg: float = 48.0,
    non_dominant_hand_kg: float = 44.0,
    sex: str = "male",
    age: int = 42,
    bodyweight_kg: float = 75.0
) -> str:
    """Calculates relative grip strength (RGS), bilateral asymmetry, and PURE mortality hazard ratio."""
    import json
    return json.dumps(client.evaluate_grip_strength_and_frailty(
        dominant_hand_kg, non_dominant_hand_kg, sex, age, bodyweight_kg
    ), indent=2)

@mcp.tool()
def model_neuromuscular_fatigue_rate(
    repeated_trials_json: str,
    trial_intervals_sec: float = 15.0
) -> str:
    """Evaluates neuromuscular motor unit fatigue slope across successive isometric trials."""
    import json
    trials = json.loads(repeated_trials_json) if isinstance(repeated_trials_json, str) else repeated_trials_json
    return json.dumps(client.model_neuromuscular_fatigue_rate(
        trials, trial_intervals_sec
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
