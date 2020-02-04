"""
Functions for reducing a PIL.Image to a single average color.

Each function should be of type `ColorAverager`.
`ColorAverager` is defined in the `colortypes` submodule.
"""

from PIL import Image
from color.colortypes import Color


def arithmeticMean(img: Image.Image) -> Color:
    """
    Gets a color average using component-wise arithmetic means.
    """
    pixels = img.getdata()
    count = 0  # total number of pixels
    r_sum = 0  # total of each pixel's red component
    g_sum = 0  # total of each pixel's green component
    b_sum = 0  # total of each pixel's blue component
    for p in pixels:
        count += 1
        r_sum += p[0]
        g_sum += p[1]
        b_sum += p[2]
    return (
        round(r_sum/count),
        round(g_sum/count),
        round(b_sum/count)
    )

def clusterDominant(img: Image.Image) -> Color:
    return (0, 0, 0)
