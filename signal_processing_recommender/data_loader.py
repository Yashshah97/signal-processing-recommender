"""
Module responsible for loading audio and sensor waveform data.

This module provides functions to load different types of waveform data. It
supports both numpy arrays and pandas DataFrames as output formats.
"""

import json
import os
from typing import List, Tuple, Union

def _load_file(path: str) -> bytes:
    """
    Load the contents of a file at the given path.

    Args:
        path (str): Path to the file to load.

    Returns:
        bytes: Contents of the file.
    """
    with open(path, 'rb') as f:
        return f.read()


def _load_json_file(path: str) -> List[dict]:
    """
    Load a JSON file at the given path and parse its contents.

    Args:
        path (str): Path to the JSON file to load.

    Returns:
        List[dict]: Parsed contents of the JSON file.
    """
    return json.loads(_load_file(path))


def _load_waveform_data(path: str, format: str) -> Union[List[float], Tuple[List[float], int]]:
    """
    Load waveform data from a file at the given path.

    Args:
        path (str): Path to the file containing the waveform data.
        format (str): Format of the waveform data. Currently only supports 'numpy' and 'pandas'.

    Returns:
        Union[List[float], Tuple[List[float], int]]: Loaded waveform data in the specified format.
    """
    if format == 'numpy':
        return _load_file(path)
    elif format == 'pandas':
        import pandas as pd
        df = pd.read_csv(path, header=None)
        return df[0].tolist(), len(df)
    else:
        raise ValueError(f"Unsupported format: {format}")


def load_audio_data(path: str) -> Tuple[List[float], int]:
    """
    Load audio waveform data from a file at the given path.

    Args:
        path (str): Path to the file containing the audio waveform data.

    Returns:
        Tuple[List[float], int]: Loaded audio waveform data.
    """
    return _load_waveform_data(path, 'numpy')


def load_sensor_data(path: str) -> Tuple[List[float], int]:
    """
    Load sensor waveform data from a file at the given path.

    Args:
        path (str): Path to the file containing the sensor waveform data.

    Returns:
        Tuple[List[float], int]: Loaded sensor waveform data.
    """
    return _load_waveform_data(path, 'numpy')


def load_audio_sensor_pairs(data_dir: str) -> List[Tuple[str, str]]:
    """
    Load pairs of audio and sensor waveform data from files in the given directory.

    Args:
        data_dir (str): Path to the directory containing the paired audio and sensor data.

    Returns:
        List[Tuple[str, str]]: Pairs of paths to loaded audio and sensor waveform data.
    """
    return [(os.path.join(data_dir, f), os.path.join(data_dir, f.replace('audio', 'sensor'))) for f in os.listdir(data_dir)]
