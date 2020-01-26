"""
Functions for measuring color difference.

Each function should be of type `ColorMetric`.
`ColorMetric` is defined in the `colortypes` submodule.
"""

from color.colortypes import Color


def squaredEuclideanDistance(a: Color, b: Color) -> float:
    return (
            (a[0] - b[0])**2 +
            (a[1] - b[1])**2 +
            (a[2] - b[2])**2
    )

def squaredRec601LumaDistance(a: Color, b: Color) -> float:
    return (
            (0.299 * (a[0] - b[0]))**2 +
            (0.587 * (a[1] - b[1]))**2 +
            (0.114 * (a[2] - b[2]))**2
    )
