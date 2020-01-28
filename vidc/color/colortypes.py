"""
Types used in the `color` module.
"""

from PIL import Image
from typing import Tuple, Callable, Dict 

Color = Tuple[int, int, int]                    # RGB (red, green, blue)
ColorMetric = Callable[[Color, Color], float]   # measures color difference
ColorAverager = Callable[[Image.Image], Color]  # returns an average color
