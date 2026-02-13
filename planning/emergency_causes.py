from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class EmergencyCause:
    id: str
    name: str
    description: str

    # modifiers
    housing_fee_multiplier: float = 1.0          # lower means cheaper housing switch
    job_stress_delta: float = 0.0                # negative reduces stress penalty
    happiness_delta_extra: float = 0.0           # extra happiness penalty/boost
    money_delta_extra: float = 0.0               # extra money (support) or loss


EMERGENCY_CAUSES: Dict[str, EmergencyCause] = {
    "roommate_conflict": EmergencyCause(
        id="roommate_conflict",
        name="Roommate conflict",
        description="You need to change your living situation quickly.",
        housing_fee_multiplier=0.4,  # housing change cheaper
    ),
    "job_hours_cut": EmergencyCause(
        id="job_hours_cut",
        name="Job hours cut",
        description="Your job reduced your hours unexpectedly; switching is stressful but less than normal.",
        job_stress_delta=-3.0,  # job change less stress
    ),
    "family_situation": EmergencyCause(
        id="family_situation",
        name="Family situation",
        description="A family issue forces a schedule change. Emotionally heavier, but some costs are covered.",
        happiness_delta_extra=-4.0,  # more happiness penalty
        money_delta_extra=120.0,     # less money pain (support)
    ),
}
