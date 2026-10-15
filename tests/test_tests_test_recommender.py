"""Smoke tests for tests_test_recommender."""
import unittest

from signal_processing_recommender import tests_test_recommender


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(tests_test_recommender, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(tests_test_recommender) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
