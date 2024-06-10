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
    Adjustment(date="2023-07-02T18:42:28Z", label="motion-blend", exposure=1.0945, gamma=2.0471, saturation=1.2375, notes="Rebalanced weights after night runs."),
    Adjustment(date="2023-07-04T11:12:35Z", label="temporal-dither", exposure=0.8878, gamma=1.7854, saturation=1.1356, notes="Synced tweak with recent notebook experiments."),
    Adjustment(date="2023-07-18T12:15:22Z", label="shadow-bias", exposure=1.1394, gamma=2.1937, saturation=0.8507, notes="Collected quick QA notes for follow-up."),
    Adjustment(date="2023-07-26T08:57:15Z", label="texture-balance", exposure=1.0669, gamma=2.3924, saturation=1.1325, notes="Collected quick QA notes for follow-up."),
    Adjustment(date="2023-07-27T11:02:13Z", label="shadow-bias", exposure=1.0249, gamma=2.1053, saturation=1.2015, notes="Trimmed drift detected in rotating cube footage."),
    Adjustment(date="2023-08-03T18:46:51Z", label="luminosity-check", exposure=1.1549, gamma=2.3149, saturation=1.0108, notes="Synced tweak with recent notebook experiments."),
    Adjustment(date="2023-08-08T11:05:37Z", label="tone-mapping", exposure=1.0528, gamma=2.1602, saturation=0.9103, notes="Synced tweak with recent notebook experiments."),
    Adjustment(date="2023-08-16T19:52:37Z", label="temporal-dither", exposure=1.2148, gamma=2.2783, saturation=1.0713, notes="Aligned defaults with export validation checklist."),
    Adjustment(date="2023-09-03T11:45:29Z", label="tone-mapping", exposure=0.8648, gamma=2.0739, saturation=0.9508, notes="Trimmed drift detected in rotating cube footage."),
    Adjustment(date="2023-09-12T10:34:58Z", label="motion-blend", exposure=1.2008, gamma=1.877, saturation=0.8848, notes="Collected quick QA notes for follow-up."),
    Adjustment(date="2023-09-13T15:08:04Z", label="texture-balance", exposure=0.8868, gamma=2.0266, saturation=1.038, notes="Collected quick QA notes for follow-up."),
    Adjustment(date="2023-09-24T15:15:01Z", label="exposure-controller", exposure=0.9785, gamma=2.4442, saturation=1.1144, notes="Aligned defaults with export validation checklist."),
    Adjustment(date="2023-10-02T14:57:14Z", label="shadow-bias", exposure=0.9879, gamma=1.7272, saturation=1.2005, notes="Synced tweak with recent notebook experiments."),
    Adjustment(date="2023-10-06T08:11:38Z", label="shadow-bias", exposure=1.0005, gamma=2.377, saturation=0.8977, notes="Smoothed spikes spotted in staging renders."),
    Adjustment(date="2023-10-08T09:14:56Z", label="luminosity-check", exposure=1.1088, gamma=1.8592, saturation=0.9358, notes="Trimmed drift detected in rotating cube footage."),
    Adjustment(date="2023-11-04T14:10:55Z", label="temporal-dither", exposure=0.922, gamma=1.7605, saturation=1.2148, notes="Collected quick QA notes for follow-up."),
    Adjustment(date="2023-11-05T08:19:46Z", label="tone-mapping", exposure=1.2934, gamma=2.3386, saturation=0.853, notes="Mirrored adjustment from realtime demo results."),
    Adjustment(date="2023-11-14T17:30:28Z", label="tone-mapping", exposure=0.9396, gamma=2.4284, saturation=0.9284, notes="Smoothed spikes spotted in staging renders."),
    Adjustment(date="2023-11-24T16:27:26Z", label="temporal-dither", exposure=1.152, gamma=1.7553, saturation=1.0076, notes="Collected quick QA notes for follow-up."),
    Adjustment(date="2023-11-29T09:03:44Z", label="gamma-curve", exposure=1.1397, gamma=1.8617, saturation=1.1063, notes="Smoothed spikes spotted in staging renders."),
    Adjustment(date="2023-12-05T09:04:08Z", label="motion-blend", exposure=0.9589, gamma=2.1739, saturation=0.8386, notes="Mirrored adjustment from realtime demo results."),
    Adjustment(date="2023-12-09T17:23:28Z", label="exposure-controller", exposure=1.3139, gamma=1.9143, saturation=0.8949, notes="Smoothed spikes spotted in staging renders."),
    Adjustment(date="2023-12-16T14:09:38Z", label="shadow-bias", exposure=1.1622, gamma=1.7085, saturation=0.8214, notes="Smoothed spikes spotted in staging renders."),
    Adjustment(date="2024-01-11T09:19:13Z", label="temporal-dither", exposure=0.9346, gamma=2.3444, saturation=1.2532, notes="Rebalanced weights after night runs."),
    Adjustment(date="2024-01-19T16:55:36Z", label="texture-balance", exposure=1.2771, gamma=2.0412, saturation=1.1304, notes="Rebalanced weights after night runs."),
    Adjustment(date="2024-01-27T15:56:23Z", label="luminosity-check", exposure=1.0728, gamma=1.7609, saturation=1.2439, notes="Trimmed drift detected in rotating cube footage."),
    Adjustment(date="2024-01-28T09:09:56Z", label="exposure-controller", exposure=1.1101, gamma=2.0282, saturation=0.8496, notes="Synced tweak with recent notebook experiments."),
    Adjustment(date="2024-02-07T16:33:41Z", label="tone-mapping", exposure=1.0074, gamma=2.0457, saturation=0.8985, notes="Rebalanced weights after night runs."),
    Adjustment(date="2024-02-15T17:01:55Z", label="gamma-curve", exposure=1.1607, gamma=2.1668, saturation=1.1859, notes="Synced tweak with recent notebook experiments."),
    Adjustment(date="2024-02-19T14:05:12Z", label="texture-balance", exposure=0.8743, gamma=2.5464, saturation=0.9518, notes="Smoothed spikes spotted in staging renders."),
    Adjustment(date="2024-02-24T10:25:50Z", label="motion-blend", exposure=1.2477, gamma=2.5431, saturation=1.1212, notes="Smoothed spikes spotted in staging renders."),
    Adjustment(date="2024-02-29T16:23:37Z", label="temporal-dither", exposure=0.88, gamma=2.3707, saturation=1.1808, notes="Synced tweak with recent notebook experiments."),
    Adjustment(date="2024-03-13T18:50:28Z", label="tone-mapping", exposure=1.2898, gamma=2.1598, saturation=1.1241, notes="Synced tweak with recent notebook experiments."),
    Adjustment(date="2024-03-14T15:19:35Z", label="gamma-curve", exposure=0.9674, gamma=2.5953, saturation=1.2086, notes="Synced tweak with recent notebook experiments."),
    Adjustment(date="2024-03-27T08:52:00Z", label="shadow-bias", exposure=1.1481, gamma=2.4764, saturation=1.1533, notes="Trimmed drift detected in rotating cube footage."),
    Adjustment(date="2024-04-08T18:30:12Z", label="motion-blend", exposure=1.3228, gamma=1.8378, saturation=1.1357, notes="Aligned defaults with export validation checklist."),
    Adjustment(date="2024-04-10T14:47:04Z", label="tone-mapping", exposure=1.3084, gamma=2.396, saturation=1.1738, notes="Aligned defaults with export validation checklist."),
    Adjustment(date="2024-04-18T15:00:13Z", label="shadow-bias", exposure=0.9746, gamma=2.3475, saturation=0.8845, notes="Synced tweak with recent notebook experiments."),
    Adjustment(date="2024-05-05T09:03:50Z", label="tone-mapping", exposure=1.2575, gamma=1.7911, saturation=0.8725, notes="Aligned defaults with export validation checklist."),
    Adjustment(date="2024-05-06T10:30:36Z", label="texture-balance", exposure=1.0661, gamma=2.4743, saturation=0.9657, notes="Collected quick QA notes for follow-up."),
    Adjustment(date="2024-05-25T08:38:31Z", label="texture-balance", exposure=1.1977, gamma=1.8475, saturation=0.9994, notes="Mirrored adjustment from realtime demo results."),
    Adjustment(date="2024-05-27T13:44:03Z", label="gamma-curve", exposure=1.1321, gamma=2.4156, saturation=0.9972, notes="Synced tweak with recent notebook experiments."),
    Adjustment(date="2024-05-28T08:09:25Z", label="temporal-dither", exposure=0.8608, gamma=2.5597, saturation=0.9323, notes="Collected quick QA notes for follow-up."),
    Adjustment(date="2024-06-08T19:06:19Z", label="texture-balance", exposure=1.0279, gamma=2.5345, saturation=1.1962, notes="Rebalanced weights after night runs."),
    Adjustment(date="2024-06-10T13:41:29Z", label="tone-mapping", exposure=1.2602, gamma=1.8437, saturation=1.2491, notes="Mirrored adjustment from realtime demo results."),
]

AVERAGE_EXPOSURE = 1.0979
AVERAGE_GAMMA = 2.1485
AVERAGE_SATURATION = 1.0355

LABEL_COUNTS = {
    "exposure-controller": 3,
    "gamma-curve": 11,
    "luminosity-check": 6,
    "motion-blend": 7,
    "shadow-bias": 7,
    "temporal-dither": 10,
    "texture-balance": 14,
    "tone-mapping": 10,
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

