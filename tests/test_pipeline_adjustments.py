import unittest
from collections import Counter
from statistics import fmean

import pipeline_adjustments as adjustments


class PipelineAdjustmentTests(unittest.TestCase):
    def test_adjustments_are_chronological(self) -> None:
        dates = [adjustment.date for adjustment in adjustments.ADJUSTMENTS]
        self.assertEqual(dates, sorted(dates))

    def test_summary_values_match_adjustments(self) -> None:
        self.assertEqual(
            adjustments.LABEL_COUNTS,
            dict(sorted(Counter(item.label for item in adjustments.ADJUSTMENTS).items())),
        )
        self.assertEqual(
            adjustments.AVERAGE_EXPOSURE,
            round(fmean(item.exposure for item in adjustments.ADJUSTMENTS), 4),
        )
        self.assertEqual(
            adjustments.AVERAGE_GAMMA,
            round(fmean(item.gamma for item in adjustments.ADJUSTMENTS), 4),
        )
        self.assertEqual(
            adjustments.AVERAGE_SATURATION,
            round(fmean(item.saturation for item in adjustments.ADJUSTMENTS), 4),
        )

    def test_latest_adjustment_returns_final_record(self) -> None:
        self.assertIs(adjustments.latest_adjustment(), adjustments.ADJUSTMENTS[-1])

    def test_find_adjustment_returns_latest_matching_record(self) -> None:
        expected = next(
            item for item in reversed(adjustments.ADJUSTMENTS) if item.label == "motion-blend"
        )
        self.assertIs(adjustments.find_adjustment("motion-blend"), expected)
        self.assertIsNone(adjustments.find_adjustment("unknown"))

    def test_recommended_settings_blend_with_latest_adjustment(self) -> None:
        latest = adjustments.latest_adjustment()
        recommended = adjustments.recommended_settings(1.25, 2.0, 0.8)

        self.assertEqual(recommended.date, latest.date)
        self.assertEqual(recommended.label, latest.label)
        self.assertEqual(recommended.exposure, round(1.25 * latest.exposure, 4))
        self.assertEqual(recommended.gamma, round(latest.gamma, 4))
        self.assertEqual(recommended.saturation, round(0.8 * latest.saturation, 4))


if __name__ == "__main__":
    unittest.main()
