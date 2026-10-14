"""
Signal Processing Recommender - Recommendation Engine

This module implements a similarity-based recommendation engine for audio and sensor waveforms.

Classes:
    RecommendationEngine: The main class for the recommendation engine.
"""

class RecommendationEngine:
    """
    A similarity-based recommendation engine for audio and sensor waveforms.

    Attributes:
        waveforms (list): A list of waveforms to compare against.
    """

    def __init__(self, waveforms):
        """
        Initialize the recommendation engine with a list of waveforms.

        Args:
            waveforms (list): A list of waveforms to compare against.
        """
        self.waveforms = waveforms

    def calculate_similarity(self, waveform1, waveform2):
        """
        Calculate the similarity between two waveforms using the dot product method.

        Args:
            waveform1 (list): The first waveform to compare.
            waveform2 (list): The second waveform to compare.

        Returns:
            float: The similarity score between the two waveforms.
        """
        if len(waveform1) != len(waveform2):
            raise ValueError("Waveforms must be of equal length")

        dot_product = sum(x * y for x, y in zip(waveform1, waveform2))
        magnitude1 = sum(x ** 2 for x in waveform1) ** 0.5
        magnitude2 = sum(x ** 2 for x in waveform2) ** 0.5

        return dot_product / (magnitude1 * magnitude2)

    def recommend(self, waveform):
        """
        Recommend similar waveforms based on the input waveform.

        Args:
            waveform (list): The input waveform to compare against.

        Returns:
            list: A list of recommended waveforms.
        """
        similarities = [(self.calculate_similarity(waveform, wf), i) for i, wf in enumerate(self.waveforms)]
        similarities.sort(reverse=True)

        return [wf for _, i in similarities[:5]]

# Example usage
if __name__ == "__main__":
    waveforms = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    engine = RecommendationEngine(waveforms)
    waveform = [10, 20, 30]
    recommended_waveforms = engine.recommend(waveform)

    print("Recommended waveforms:", recommended_waveforms)
