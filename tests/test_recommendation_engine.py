import unittest
from signal_processing_recommender import recommendation_engine

class TestRecommendationEngine(unittest.TestCase):
    def test_recommendation_engine_init(self):
        waveforms = [[1, 2, 3], [4, 5, 6]]
        engine = recommendation_engine.RecommendationEngine(waveforms)
        self.assertEqual(engine.waveforms, waveforms)

    def test_calculate_similarity(self):
        engine = recommendation_engine.RecommendationEngine([[1, 2, 3]])
        similarity = engine.calculate_similarity([4, 5, 6], [7, 8, 9])
        self.assertGreater(similarity, 0.0)

    def test_recommend(self):
        waveforms = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        engine = recommendation_engine.RecommendationEngine(waveforms)
        recommended_waveforms = engine.recommend([10, 20, 30])
        self.assertEqual(len(recommended_waveforms), 5)

if __name__ == "__main__":
    unittest.main()
