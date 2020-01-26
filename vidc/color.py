from math import sqrt
from typing import Tuple, Callable, Dict 

Color = Tuple[int, int, int]                   # RGB (red, green, blue)
ColorMetric = Callable[[Color, Color], float]  # measures color difference


def euclideanDistance(a: Color, b: Color) -> float:
    return sqrt(
            (a[0] - b[0])**2 +
            (a[1] - b[1])**2 +
            (a[2] - b[2])**2
    )

def squaredEuclideanDistance(a: Color, b: Color) -> float:
    return (
            (a[0] - b[0])**2 +
            (a[1] - b[1])**2 +
            (a[2] - b[2])**2
    )

def rec601LumaDistance(a: Color, b: Color) -> float:
    return sqrt(
            (0.299 * (a[0] - b[0]))**2 +
            (0.587 * (a[1] - b[1]))**2 +
            (0.114 * (a[2] - b[2]))**2
    )

def squaredRec601LumaDistance(a: Color, b: Color) -> float:
    return (
            (0.299 * (a[0] - b[0]))**2 +
            (0.587 * (a[1] - b[1]))**2 +
            (0.114 * (a[2] - b[2]))**2
    )


class NamedPalette(Dict[Color, str]):
    """
    Associates color values to names.

    Useful for creating image mosaics by matching target image section colors
    to the colors of the library of available images (the palette).

    Provides the method `nearest` to find the most similar color available in
    the palette to a given color argument (using a customizable metric).
    """

    def nearest(self,
                color: Color,
                metric: ColorMetric = squaredEuclideanDistance
    ) -> Tuple[Color, str]:
        """
        Get the color value and name of the nearest available palette color.

        A custom definition of "nearest" can be used by passing a ColorMetric.
        By default, this method uses the metric of squared Euclidean distance.

        When multiple colors are nearest, the first encountered is returned.
        This adopts the behavior of Python's built-in min and max functions.
        """
        if color in self:  # exact same palette color already exists
            return color, self[color]

        # linear search through palette colors for nearest
        nearest_color = min(
                self.keys(),
                key = lambda palette_color: metric(color, palette_color)
        )
        return nearest_color, self[nearest_color]
