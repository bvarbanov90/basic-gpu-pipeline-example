"""Historical tuning adjustments for the GPU pipeline examples.

This module stores incremental tweaks applied while evolving the demo notebooks.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class Adjustment:
    date: str
    label: str
    exposure: float
    gamma: float
    saturation: float
    notes: str


ADJUSTMENTS: List[Adjustment] = [
    Adjustment(date="2023-01-01T10:40:30Z", label="gamma-curve", exposure=1.213, gamma=2.297, saturation=0.9126, notes="Trimmed drift detected in rotating cube footage."),
    Adjustment(date="2023-01-02T11:10:49Z", label="gamma-curve", exposure=1.0366, gamma=2.3762, saturation=1.097, notes="Synced tweak with recent notebook experiments."),
    Adjustment(date="2023-01-22T13:53:45Z", label="luminosity-check", exposure=0.9127, gamma=1.7906, saturation=1.0222, notes="Aligned defaults with export validation checklist."),
    Adjustment(date="2023-02-07T12:36:52Z", label="motion-blend", exposure=1.1101, gamma=1.8533, saturation=1.0895, notes="Collected quick QA notes for follow-up."),
    Adjustment(date="2023-02-11T18:52:02Z", label="texture-balance", exposure=0.9994, gamma=1.9683, saturation=0.8369, notes="Rebalanced weights after night runs."),
    Adjustment(date="2023-02-13T08:42:47Z", label="gamma-curve", exposure=1.1784, gamma=2.5079, saturation=1.2234, notes="Smoothed spikes spotted in staging renders."),
    Adjustment(date="2023-02-14T08:06:50Z", label="luminosity-check", exposure=1.1346, gamma=2.1171, saturation=0.9162, notes="Trimmed drift detected in rotating cube footage."),
    Adjustment(date="2023-02-22T16:04:13Z", label="motion-blend", exposure=1.2887, gamma=1.7548, saturation=1.1036, notes="Rebalanced weights after night runs."),
]

AVERAGE_EXPOSURE = 1.1092
AVERAGE_GAMMA = 2.0831
AVERAGE_SATURATION = 1.0252

LABEL_COUNTS = {
    "gamma-curve": 3,
    "luminosity-check": 2,
    "motion-blend": 2,
    "texture-balance": 1,
}

def latest_adjustment() -> Adjustment:
    """Return the most recent tuning adjustment."""
    return ADJUSTMENTS[-1]

def find_adjustment(label: str) -> Optional[Adjustment]:
    """Fetch the last adjustment recorded for a given label."""
    for adjustment in reversed(ADJUSTMENTS):
        if adjustment.label == label:
            return adjustment
    return None

def recommended_settings(base_exposure: float, base_gamma: float, base_saturation: float) -> Adjustment:
    """Blend the latest tuning values with supplied baseline settings."""
    latest = latest_adjustment()
    return Adjustment(
        date=latest.date,
        label=latest.label,
        exposure=round(base_exposure * latest.exposure, 4),
        gamma=round(base_gamma * latest.gamma / 2.0, 4),
        saturation=round(base_saturation * latest.saturation, 4),
        notes=f"Composed with {latest.label} guidance",
    )

