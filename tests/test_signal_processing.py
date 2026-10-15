"""Smoke tests for signal_processing."""
import unittest

from signal_processing_recommender import signal_processing


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(signal_processing, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(signal_processing) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
