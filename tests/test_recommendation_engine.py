"""Smoke tests for recommendation_engine."""
import unittest

from signal_processing_recommender import recommendation_engine


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(recommendation_engine, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(recommendation_engine) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
