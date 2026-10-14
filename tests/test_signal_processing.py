import unittest
from signal_processing_recommender import signal_processing

class TestSignalProcessing(unittest.TestCase):
    def test_calculate_magnitude(self):
        signal = signal_processing.Signal([1.0, 2.0, 3.0])
        self.assertAlmostEqual(signal_processing.calculate_magnitude(signal), 3.7416573867739413)

    def test_calculate_mean(self):
        signal = signal_processing.Signal([1.0, 2.0, 3.0])
        self.assertEqual(signal_processing.calculate_mean(signal), 2.0)

    def test_calculate_stddev(self):
        signal = signal_processing.Signal([1.0, 2.0, 3.0])
        self.assertAlmostEqual(signal_processing.calculate_stddev(signal), 1.0)

    def test_similarity(self):
        signal1 = signal_processing.Signal([1.0, 2.0, 3.0])
        signal2 = signal_processing.Signal([4.0, 5.0, 6.0])
        self.assertAlmostEqual(signal_processing.similarity(signal1, signal2), 0.0)

if __name__ == "__main__":
    unittest.main()
