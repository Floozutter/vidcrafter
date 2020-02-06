"""
Class definition of `IndexedPalette`.
"""

from color.metrics import squaredEuclideanDistance
from color.colortypes import Color, ColorMetric
from typing import Tuple, Dict


class IndexedPalette(Dict[Color, int]):
    """
    Associates color values to indices. Useful for creating image mosaics.

    Provides the method `nearest` to find the most similar color available in
    the palette to a given color argument (with a customizable metric).
    """

    def nearest(self,
                color: Color,
                metric: ColorMetric = squaredEuclideanDistance
    ) -> Tuple[Color, int]:
        """
        Get the color value and index of the nearest available palette color.

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
