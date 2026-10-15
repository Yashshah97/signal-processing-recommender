import unittest
from signal_processing_recommender import tests_test_recommender

class TestTestRecommender(unittest.TestCase):
    def test_empty_recommendations(self) -> None:
        recommender = tests_test_recommender.TestSignalProcessingRecommender()
        self.assertEqual(recommender.test_empty_recommendations(), [])

    def test_single_recommendation(self) -> None:
        recommender = tests_test_recommender.TestSignalProcessingRecommender()
        similar_signals: List[Tuple[float, float]] = [(1.0, 2.0)]
        self.assertEqual(recommender.test_single_recommendation(similar_signals), similar_signals)

    def test_multiple_recommendations(self) -> None:
        recommender = tests_test_recommender.TestSignalProcessingRecommender()
        similar_signals: List[Tuple[float, float]] = [(1.0, 2.0), (3.0, 4.0)]
        self.assertEqual(recommender.test_multiple_recommendations(similar_signals), similar_signals)

    def test_no_similarity(self) -> None:
        recommender = tests_test_recommender.TestSignalProcessingRecommender()
        similar_signals: List[Tuple[float, float]] = [(1.0, 2.0)]
        self.assertEqual(recommender.test_no_similarity([similar_signals[1]]), [])

    def test_frozen_instance_error(self) -> None:
        recommender = tests_test_recommender.TestSignalProcessingRecommender()
        with self.assertRaises(FrozenInstanceError):
            recommender.test_frozen_instance_error()

if __name__ == '__main__':
    unittest.main()
