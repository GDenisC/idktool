
from typing import Sequence

__all__ = [
    'ColorRGBA'
]

class ColorError(Exception):
    def __init__(self, colorname: str) -> None:
        super().__init__(f"Color `{colorname}` not in 0-255 (float) range")

class ColorRGBA:
    def __init__(self, red: float = 255, green: float = 255, blue: float = 255, alpha: float = 255, *, array: Sequence[float] = ...) -> None:
        if array:
            self.red = array[0]
            self.green = array[1]
            self.blue = array[2]
            try:
                self.alpha = array[3]
            except IndexError:
                self.alpha = 255
            return
        if red < 0 | red > 255:
            raise ColorError('red')
        if green < 0 | green > 255:
            raise ColorError('green')
        if blue < 0 | blue > 255:
            raise ColorError('blue')
        if alpha < 0 | alpha > 255:
            raise ColorError('alpha')

        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def toSequence(self) -> Sequence[float]:
        return [self.red, self.green, self.blue, self.alpha]
