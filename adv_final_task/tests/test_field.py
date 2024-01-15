"""Tictactoe fields."""

from src.tictactoe_utils import TicTacToeField
import pytest


def test_place_figure():
    """Test place figure functionality."""
    field = TicTacToeField(cross='1', zero='0', free_space='_')
    is_win = field.place_figure(pos=(1, 1))
    assert is_win is None
    is_win = field.place_figure(pos=(0, 0))
    assert is_win is None
    assert field._state[1][1] == '1'
    assert field._state[0][0] == '0'
    for i in range(3):
        for j in range(3):
            if i == j and i <= 1:
                continue
            assert field._state[i][j] == '_'


def test_check_win():
    """Test that check_win works correct."""
    field = TicTacToeField(cross='1', zero='0', free_space='_')
    for i in range(3):
        field._state[i][i] = '1'
    assert field.check_win() == '1'
    field = TicTacToeField(cross='1', zero='0', free_space='_')
    for i in range(3):
        field._state[1][i] = '0'
    assert field.check_win() == '0'

    field = TicTacToeField(cross='1', zero='0', free_space='_')
    field.place_figure((1, 1))
    field.place_figure((2, 2))
    for i in range(3):
        field._state[i][0] = '1'
    assert field.check_win() == '1'


def test_exceptions_raises():
    """Test that Exceptions raises correctly."""
    field = TicTacToeField(cross='1', zero='0', free_space='_')
    field._state[0][0] = '1'
    with pytest.raises(ValueError):
        field.place_figure(pos=(0, 0))
    with pytest.raises(ValueError):
        field.place_figure(pos=(3, 2))
