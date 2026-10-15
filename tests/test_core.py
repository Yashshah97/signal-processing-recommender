import unittest
from signal_processing_recommender import core

class TestCoreModule(unittest.TestCase):

    def test_calculate_similarity(self):
        vector1 = [1, 2, 3]
        vector2 = [4, 5, 6]
        self.assertAlmostEqual(core.calculate_similarity(vector1, vector2), 0.8660254037844387)

    def test_get_recommended_items(self):
        user_vector = [1, 2, 3]
        item_vectors = {
            'item1': [4, 5, 6],
            'item2': [7, 8, 9],
            'item3': [10, 11, 12],
            'item4': [13, 14, 15]
        }
        recommended_items, avg_similarity = core.get_recommended_items(user_vector, item_vectors)
        self.assertEqual(recommended_items, ['item1', 'item2', 'item3'])
        self.assertAlmostEqual(avg_similarity, 0.8660254037844387)

if __name__ == '__main__':
    unittest.main()
