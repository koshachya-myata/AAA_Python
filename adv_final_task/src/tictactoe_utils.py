"""Tictactoe utils."""
from typing import Union, Tuple, List
import random


class TicTacToeField:
    """Class for representing tictactoe game field."""

    def __init__(self, free_space: str = '.',
                 cross: str = 'X', zero: str = 'O') -> None:
        """
        Initiate class fields.

        Args:
            free_space (str, optional): Free space char. Defaults to '.'.
            corss (str, optional): 1st player char. Defaults to 'X'.
            zero (str, optional): 2nd player char. Defaults to 'O'.
        """
        self.free_space = free_space
        self.cross = cross
        self.zero = zero
        self._state: List[List[str]] = [[free_space for _ in range(3)]
                                        for _ in range(3)]
        self._free_cells = set()
        for i in range(3):
            for j in range(3):
                self._free_cells.update([(i, j)])
        self.current_turn = 0

    def get_state(self) -> List[List[str]]:
        """Get tictactoe current field state."""
        return self._state.copy()

    def check_win(self) -> Union[str, None]:
        """
        Check if crosses or zeros have won the game.

        Return None if no one won.
        If someone won, then return winner field character.
        """
        # horizontal
        for i in range(len(self._state)):
            if self._state[i][0] == self._state[i][1] == self._state[i][2]:
                if self._state[i][0] != self.free_space:
                    return self._state[i][0]

        # vertical
        for i in range(3):
            if self._state[0][i] == self._state[1][i] == self._state[2][i]:
                if self._state[0][i] != self.free_space:
                    return self._state[0][i]

        # diagonal
        if self._state[0][0] == self._state[1][1] == self._state[2][2] or \
                self._state[0][2] == self._state[1][1] == self._state[2][0]:
            if self._state[1][1] != self.free_space:
                return self._state[1][1]
        return None

    def is_draw(self) -> bool:
        """Check if there is a draw on a field."""
        return len(self._free_cells) == 0

    def place_figure(self, pos: Tuple[int, int]) -> Union[str, None]:
        """
        Place a players game symbol on a field in position pos.

        Args:
            pos (Tuple[int]): position to place a character.

        Raises:
            ValueError: if given args is bad.

        Returns:
            str: winner player game symbol or None
        """
        ch = self.cross if self.current_turn == 0 else self.zero
        if len(pos) != 2 or pos[0] < 0 or pos[0] > 2 \
                or pos[1] < 0 or pos[1] > 2:
            raise ValueError('Position must be in {0,1,2} × {0,1,2}.')
        if self._state[pos[0]][pos[1]] != self.free_space:
            raise ValueError('This position is already taken.')
        self._state[pos[0]][pos[1]] = ch
        self._free_cells.remove(pos)
        self.current_turn = (self.current_turn + 1) % 2
        return self.check_win()

    def ai_move(self) -> Union[str, None]:
        """
        Place a player symbol on a random free posotion.

        Returns:
            str: winner player game symbol or None
        """
        pos = random.sample(self._free_cells, 1)[0]
        return self.place_figure(pos)
