"""Smoke tests for data_loader."""
import unittest

from signal_processing_recommender import data_loader


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(data_loader, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(data_loader) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
