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
    Adjustment(date="2023-03-03T17:36:07Z", label="temporal-dither", exposure=0.9963, gamma=2.1709, saturation=0.9129, notes="Mirrored adjustment from realtime demo results."),
    Adjustment(date="2023-03-18T15:37:55Z", label="gamma-curve", exposure=0.8635, gamma=2.3417, saturation=0.8237, notes="Smoothed spikes spotted in staging renders."),
    Adjustment(date="2023-03-19T14:09:22Z", label="texture-balance", exposure=1.0463, gamma=1.9468, saturation=1.1111, notes="Collected quick QA notes for follow-up."),
    Adjustment(date="2023-04-08T13:00:03Z", label="gamma-curve", exposure=1.0207, gamma=1.9433, saturation=1.1897, notes="Trimmed drift detected in rotating cube footage."),
    Adjustment(date="2023-04-18T08:50:28Z", label="gamma-curve", exposure=0.9493, gamma=2.333, saturation=0.8969, notes="Aligned defaults with export validation checklist."),
    Adjustment(date="2023-04-20T13:08:02Z", label="gamma-curve", exposure=1.2357, gamma=2.2908, saturation=1.0047, notes="Trimmed drift detected in rotating cube footage."),
    Adjustment(date="2023-05-11T12:42:48Z", label="texture-balance", exposure=1.2258, gamma=2.5539, saturation=1.169, notes="Rebalanced weights after night runs."),
    Adjustment(date="2023-05-12T17:11:42Z", label="tone-mapping", exposure=1.3211, gamma=2.4174, saturation=0.837, notes="Smoothed spikes spotted in staging renders."),
    Adjustment(date="2023-05-14T09:58:03Z", label="temporal-dither", exposure=1.0794, gamma=2.0545, saturation=1.0217, notes="Trimmed drift detected in rotating cube footage."),
    Adjustment(date="2023-05-23T08:30:00Z", label="luminosity-check", exposure=1.3094, gamma=2.2082, saturation=1.0178, notes="Synced tweak with recent notebook experiments."),
    Adjustment(date="2023-06-04T10:30:55Z", label="texture-balance", exposure=1.0774, gamma=2.3891, saturation=1.2018, notes="Aligned defaults with export validation checklist."),
    Adjustment(date="2023-06-10T18:31:57Z", label="temporal-dither", exposure=1.2257, gamma=2.0022, saturation=1.0229, notes="Synced tweak with recent notebook experiments."),
    Adjustment(date="2023-06-14T09:15:01Z", label="texture-balance", exposure=0.9883, gamma=1.7306, saturation=1.1554, notes="Rebalanced weights after night runs."),
    Adjustment(date="2023-06-15T11:21:21Z", label="texture-balance", exposure=1.2777, gamma=2.3305, saturation=0.9447, notes="Trimmed drift detected in rotating cube footage."),
    Adjustment(date="2023-06-20T08:31:45Z", label="texture-balance", exposure=1.2436, gamma=1.9919, saturation=0.9593, notes="Rebalanced weights after night runs."),
]

AVERAGE_EXPOSURE = 1.1189
AVERAGE_GAMMA = 2.1465
AVERAGE_SATURATION = 1.0204

LABEL_COUNTS = {
    "gamma-curve": 7,
    "luminosity-check": 3,
    "motion-blend": 2,
    "temporal-dither": 3,
    "texture-balance": 7,
    "tone-mapping": 1,
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

