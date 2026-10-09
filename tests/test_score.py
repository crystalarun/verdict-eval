import unittest
from verdict_eval.score import score_case

class ScoreTests(unittest.TestCase):
    def test_requires_citation(self):
        case = {"id": "churn", "expect": "answer", "must_cite": "metric.churn_30d"}
        bad = {"decision": "answer", "citations": [{"doc_id": "other"}]}
        good = {"decision": "answer", "citations": [{"doc_id": "metric.churn_30d"}]}
        self.assertFalse(score_case(case, bad)["ok"])
        self.assertTrue(score_case(case, good)["ok"])

    def test_abstain(self):
        case = {"id": "nps", "expect": "abstain"}
        self.assertTrue(score_case(case, {"decision": "abstain", "citations": []})["ok"])

if __name__ == "__main__":
    unittest.main()
