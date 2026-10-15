"""
Signal Processing Recommender core module.

This module contains the main domain logic and public entry points of the recommender system.
"""

import math
from typing import List, Dict, Tuple

def calculate_similarity(vector1: List[float], vector2: List[float]) -> float:
    """
    Calculate the cosine similarity between two vectors.

    Args:
        vector1 (List[float]): The first vector.
        vector2 (List[float]): The second vector.

    Returns:
        float: The cosine similarity between the two vectors.
    """
    dot_product = sum(x * y for x, y in zip(vector1, vector2))
    magnitude1 = math.sqrt(sum(x ** 2 for x in vector1))
    magnitude2 = math.sqrt(sum(x ** 2 for x in vector2))
    return dot_product / (magnitude1 * magnitude2)


def get_recommended_items(user_vector: List[float], item_vectors: Dict[str, List[float]]) -> Tuple[List[str], float]:
    """
    Get the recommended items for a user based on their vector.

    Args:
        user_vector (List[float]): The user's vector.
        item_vectors (Dict[str, List[float]]): A dictionary of item vectors.

    Returns:
        Tuple[List[str], float]: A list of recommended item IDs and the average similarity score.
    """
    similarities = {}
    for item_id, vector in item_vectors.items():
        similarity = calculate_similarity(user_vector, vector)
        similarities[item_id] = similarity

    recommended_items = sorted(similarities, key=similarities.get, reverse=True)[:3]
    avg_similarity = sum(similarities[item_id] for item_id in recommended_items) / len(recommended_items)

    return recommended_items, avg_similarity
