import importlib.util
import json
from pathlib import Path
import unittest

path = Path(__file__).resolve().parents[2] / ".agents/skills/vision/scripts/report.py"
spec = importlib.util.spec_from_file_location("vision_report", path)
vision = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vision)


def event(input_tokens=100, output_tokens=20):
    return json.dumps({"type": "turn.completed", "usage": {
        "input_tokens": input_tokens, "output_tokens": output_tokens,
        "cached_input_tokens": 80, "reasoning_output_tokens": 10}})


class VisionAccountingTests(unittest.TestCase):
    def test_cache_and_reasoning_are_not_double_counted(self):
        self.assertEqual(vision.usage(event())["tokens"], 120)

    def test_multiple_turns_and_separate_vision(self):
        result = vision.receipt(300, vision.usage(event() + "\n" + event()),
                                vision.usage(event(10, 5)))
        self.assertEqual((result["difference"], result["difference_percent"], result["combined"]),
                         (-60, -20, 255))

    def test_missing_is_not_zero(self):
        result = vision.receipt(100, vision.usage(""))
        self.assertIsNone(result["difference"])
        self.assertIsNone(result["combined"])
        self.assertIsNone(result["vision"])

    def test_failed_or_pending_is_partial(self):
        for suffix in ('{"type":"turn.failed"}', '{"type":"turn.started"}',
                       '{"type":"turn.completed"}', '{"type":"error"}'):
            result = vision.receipt(100, vision.usage(event() + "\n" + suffix))
            self.assertEqual(result["execution"]["tokens"], 120)
            self.assertFalse(result["execution"]["complete"])
            self.assertIsNone(result["difference"])

    def test_invalid_counts(self):
        for invalid in (True, -1, 1.5, "100"):
            self.assertIsNone(vision.usage(event(invalid))["tokens"])
        with self.assertRaises(ValueError):
            vision.receipt(-1, vision.usage(event()))

    def test_zero_estimate(self):
        result = vision.receipt(0, vision.usage(event(0, 0)))
        self.assertEqual(result["difference"], 0)
        self.assertIsNone(result["difference_percent"])

    def test_bad_json_rejected(self):
        with self.assertRaises(ValueError):
            vision.usage("not json")


if __name__ == "__main__":
    unittest.main()
