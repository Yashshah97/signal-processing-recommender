"""Demo for Signal Processing Recommender."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import signal_processing_recommender

print("Signal Processing Recommender", "v" + signal_processing_recommender.__version__)
print("modules:", [m for m in dir(signal_processing_recommender) if not m.startswith('_')])
