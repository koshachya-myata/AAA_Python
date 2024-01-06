"""Tests order functionality."""
from src.Color import Color

END = '\033[0'
START = '\033[1;38;2'
MOD = 'm'


def test_color():
    """Test that order status changes correctly."""
    clr = Color(255, 0, 0)
    assert str(clr) == f'{START};{255};{0};{0}{MOD}●{END}{MOD}'
    assert clr == Color(255, 0, 0)
    assert clr != Color(255, 255, 255)
    assert (clr + Color(100, 128, 0)) == Color(255, 128, 0)
    orange1 = Color(255, 165, 0)
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange2 = Color(255, 165, 0)
    color_list = [orange1, red, green, orange2]
    assert set(color_list) == set([orange1, red, green])
    assert set(color_list) != set([red])
