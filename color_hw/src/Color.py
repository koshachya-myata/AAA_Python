"""Color class."""
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class ColorStrConstant:
    """Constants for string representation of a color."""

    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'


class ComputerColor(ABC):
    """Color base abscract class."""

    @abstractmethod
    def __mul__(self, other: float):
        """Multiply color by number from [0, 1]."""
        pass

    @abstractmethod
    def __rmul__(self, other):
        """Right operand multiply color by number from [0, 1]."""
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """Return printable representational string of self Color object."""
        pass


class Color(ComputerColor):
    """Class for representing color (RGB format)."""

    def __init__(self, red_level: int, green_level: int,
                 blue_level: int) -> None:
        """
        Init color.

        Args:
            red_level (int): red channel.
            green_level (int): green channel.
            blue_level (int): blue channel.
        """
        self.red_level = red_level
        self.green_level = green_level
        self.blue_level = blue_level

    def __str__(self) -> str:
        """
        Convert self to str.

        In format:
            f'{START};{red_level};{green_level};{blue_level}{MOD}●{END}{MOD}'
        """
        return f'{ColorStrConstant.START};{self.red_level};' + \
            f'{self.green_level};{self.blue_level}{ColorStrConstant.MOD}●' + \
            f'{ColorStrConstant.END}{ColorStrConstant.MOD}'

    def __get_rgb_tuple(self):
        """Get list of rgb channels."""
        return (self.red_level, self.green_level, self.blue_level)

    def __eq__(self, __value: object) -> bool:
        """Check if two colors are equal."""
        if not isinstance(__value, Color):
            return NotImplemented
        return str(self) == str(__value)

    def __add__(self, other: object) -> 'ComputerColor':
        """Adding of two Colors."""
        if not isinstance(other, Color):
            return NotImplemented
        rgb_self = self.__get_rgb_tuple()
        rgb_other = other.__get_rgb_tuple()
        rgb = list()
        for i in range(3):
            rgb.append(min(rgb_self[i] + rgb_other[i], 255))
        return type(self)(*rgb)

    def __hash__(self) -> int:
        """Get hash value for self."""
        return hash(self.__get_rgb_tuple())

    def __mul__(self, other: float) -> 'ComputerColor':
        """Multiply color by number from [0, 1] (reduces contrast)."""
        if not isinstance(other, float) or other < 0 or other > 1:
            raise ValueError('Multiplier must be a number in [0, 1]')
        cl = -256 * (1 - other)
        f = (259 * (cl + 255)) / (255 * (259 - cl))
        return type(self)(*map(lambda ch: int(f * (ch - 128) + 128),
                               self.__get_rgb_tuple()))

    def __rmul__(self, other: float) -> 'ComputerColor':
        """Right operand multiply color by number from [0, 1]."""
        return self.__mul__(other)

    def __repr__(self) -> str:
        """Return printable representational string of self Color object."""
        return f'Color({self.red_level},' + \
            f'{self.green_level}, {self.blue_level})'


def print_a(color: ComputerColor):
    """Print A in given color."""
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 +
        [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 +
        [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 +
        [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 +
        [bg_color] * 3,
        [bg_color] * 19,
    ]
    for row in a_matrix:
        print(''.join(str(ptr) for ptr in row))


if __name__ == '__main__':
    red = Color(255, 0, 0)
    print_a(red)
