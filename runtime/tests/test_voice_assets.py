import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOICE = ROOT / "voice"


class VoiceAssetTests(unittest.TestCase):
    def test_delivery_profiles_are_valid_and_complete(self):
        data = json.loads((VOICE / "delivery_profiles.json").read_text(encoding="utf-8"))
        self.assertEqual(data["schema_version"], 1)
        profiles = data["profiles"]
        required = {
            "neutral",
            "analytical",
            "cerebro",
            "council",
            "ikonn",
            "watcher",
            "tva",
            "warning",
            "success",
            "failure",
            "dry_humour",
        }
        self.assertTrue(required.issubset(profiles))
        for name, profile in profiles.items():
            self.assertGreater(profile["pace"], 0)
            self.assertGreaterEqual(profile["energy"], 0)
            self.assertLessEqual(profile["energy"], 1)
            self.assertGreaterEqual(profile["pause_before_conclusion_ms"], 0)
            self.assertTrue(profile["notes"].strip(), name)

    def test_seed_corpus_has_unique_ids_and_valid_profiles(self):
        profiles = json.loads((VOICE / "delivery_profiles.json").read_text(encoding="utf-8"))["profiles"]
        rows = [
            json.loads(line)
            for line in (VOICE / "corpus_seed.jsonl").read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        self.assertGreaterEqual(len(rows), 50)
        ids = [row["id"] for row in rows]
        self.assertEqual(len(ids), len(set(ids)))
        for row in rows:
            self.assertIn(row["profile"], profiles)
            self.assertGreaterEqual(len(row["text"].split()), 4)

    def test_voice_policy_explicitly_blocks_celebrity_training_material(self):
        text = (VOICE / "README.md").read_text(encoding="utf-8").lower()
        self.assertIn("no celebrity audio", text)
        self.assertIn("consent", text)
        self.assertIn("original", text)


if __name__ == "__main__":
    unittest.main()
