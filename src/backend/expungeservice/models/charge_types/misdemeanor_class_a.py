from dataclasses import dataclass

from expungeservice.models.charge import ChargeType
from expungeservice.models.charge import ChargeUtil
from expungeservice.models.expungement_result import TypeEligibility, EligibilityStatus


@dataclass(frozen=True)
class MisdemeanorClassA(ChargeType):
    type_name: str = "Misdemeanor Class A"
    expungement_rules: str = """Convictions for misdemeanors are generally eligible under ORS 137.225(1)(b).
Exceptions include convictions related to sex, child and elder abuse, and driving, including DUII.
Dismissals for misdemeanors are generally eligible under ORS 137.225(1)(d). Exceptions include cases dismissed due to successful completion of DUII diversion."""
    severity_level: str = "Misdemeanor Class A"

    def type_eligibility(self, disposition):
        if ChargeUtil.dismissed(disposition):
            raise ValueError("Dismissed criminal charges should have been caught by another class.")
        elif ChargeUtil.convicted(disposition):
            return TypeEligibility(EligibilityStatus.ELIGIBLE, reason="Eligible under 137.225(1)(b)")
        else:
            return TypeEligibility(
                EligibilityStatus.ELIGIBLE,
                reason="Always eligible under 137.225(1)(b) for convictions, or 137.225(1)(d) for dismissals",
            )
