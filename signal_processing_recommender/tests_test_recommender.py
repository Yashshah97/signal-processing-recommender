"""
Unit tests for the signal processing recommender.

This module contains unit tests for the SignalProcessingRecommender class.
"""

import unittest
from dataclasses import FrozenInstanceError
from typing import List, Tuple

class TestSignalProcessingRecommender(unittest.TestCase):
    def test_empty_recommendations(self) -> None:
        """Test that an empty list is returned when no similar signals are found."""
        recommender = SignalProcessingRecommender()
        self.assertEqual(recommender.recommend([]), [])

    def test_single_recommendation(self) -> None:
        """Test that a single recommendation is made when there's only one similar signal."""
        recommender = SignalProcessingRecommender()
        similar_signals: List[Tuple[float, float]] = [(1.0, 2.0)]
        self.assertEqual(recommender.recommend(similar_signals), similar_signals)

    def test_multiple_recommendations(self) -> None:
        """Test that multiple recommendations are made when there are multiple similar signals."""
        recommender = SignalProcessingRecommender()
        similar_signals: List[Tuple[float, float]] = [(1.0, 2.0), (3.0, 4.0)]
        self.assertEqual(recommender.recommend(similar_signals), similar_signals)

    def test_no_similarity(self) -> None:
        """Test that an empty list is returned when there's no similarity between signals."""
        recommender = SignalProcessingRecommender()
        similar_signals: List[Tuple[float, float]] = [(1.0, 2.0)]
        self.assertEqual(recommender.recommend([similar_signals[1]]), [])

    def test_frozen_instance_error(self) -> None:
        """Test that a FrozenInstanceError is raised when trying to modify a frozen recommender."""
        recommender = SignalProcessingRecommender()
        with self.assertRaises(FrozenInstanceError):
            setattr(recommender, '_frozen', True)

class SignalProcessingRecommender:
    def __init__(self) -> None:
        """Initialize the recommender."""
        self._frozen: bool = False

    @property
    def frozen(self) -> bool:
        """Get whether the recommender is frozen."""
        return self._frozen

    def recommend(self, similar_signals: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
        """Recommend signals based on similarity.

        Args:
            similar_signals (List[Tuple[float, float]]): A list of similar signals.

        Returns:
            List[Tuple[float, float]]: The recommended signals.
        """
        if self.frozen:
            raise FrozenInstanceError('Cannot modify a frozen recommender')
        return similar_signals

if __name__ == '__main__':
    unittest.main()
