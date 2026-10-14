"""
Module containing signal processing functions and classes.

This module provides basic signal processing functionality for audio and sensor waveforms.
"""

import math
from typing import List, Tuple

class Signal:
    """Base class for signals."""
    def __init__(self, data: List[float]):
        self.data = data

class AudioSignal(Signal):
    """Class representing an audio signal."""
    pass

class SensorSignal(Signal):
    """Class representing a sensor signal."""
    pass

def calculate_magnitude(signal: Signal) -> float:
    """
    Calculate the magnitude of a signal.

    The magnitude is calculated as the square root of the sum of squares of all samples.

    Args:
        signal (Signal): The input signal.

    Returns:
        float: The magnitude of the signal.
    """
    return math.sqrt(sum(x**2 for x in signal.data))

def calculate_mean(signal: Signal) -> float:
    """
    Calculate the mean of a signal.

    Args:
        signal (Signal): The input signal.

    Returns:
        float: The mean of the signal.
    """
    return sum(signal.data) / len(signal.data)

def calculate_stddev(signal: Signal, mean: float = None) -> float:
    """
    Calculate the standard deviation of a signal.

    Args:
        signal (Signal): The input signal.
        mean (float, optional): The mean of the signal. Defaults to None.

    Returns:
        float: The standard deviation of the signal.
    """
    if mean is None:
        mean = calculate_mean(signal)
    return math.sqrt(sum((x - mean)**2 for x in signal.data) / len(signal.data))

def similarity(signal1: Signal, signal2: Signal) -> float:
    """
    Calculate the similarity between two signals.

    The similarity is calculated as 1 minus the ratio of the standard deviations.

    Args:
        signal1 (Signal): The first input signal.
        signal2 (Signal): The second input signal.

    Returns:
        float: The similarity between the two signals.
    """
    stddev1 = calculate_stddev(signal1)
    stddev2 = calculate_stddev(signal2)
    return 1 - abs(stddev1 / stddev2)

# Example usage
if __name__ == "__main__":
    signal1 = AudioSignal([1.0, 2.0, 3.0])
    signal2 = SensorSignal([4.0, 5.0, 6.0])

    print(calculate_magnitude(signal1))
    print(calculate_mean(signal1))
    print(calculate_stddev(signal1))

    print(similarity(signal1, signal2))
