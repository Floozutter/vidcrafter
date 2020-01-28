"""
Functions for reducing a PIL.Image to a single average color.
"""

from PIL import Image
from color.colortypes import Color


def arithmeticMean(img: Image.Image) -> Color:
    return (0, 0, 0)

def clusterDominant(img: Image.Image) -> Color:
    return (0, 0, 0)
