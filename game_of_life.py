# !/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

MYPY = False
if MYPY:
    from typing import Tuple, List, DefaultDict


class Game(object):
    """
    rules:
    1 - If a cell is ON and has fewer than two neighbors that are ON, it
    turns OFF.
    2 - If a cell is ON and has either two or three neighbors that are ON,
    it remains ON.
    3 - If a cell is ON and has more than three neighbors that are ON, it
    turns OFF.
    4 - If a cell is OFF and has exactly three neighbors that are ON, it
    turns ON.
    """

    def __init__(self, size, starting_cells):
        # type: (Tuple[int, int], List[Tuple[int, int]]) -> None
        self.size = size
        self._starting_cells = list(starting_cells)  # type: List[Tuple[int, int]]
        self._active_cells = list(starting_cells)  # type: List[Tuple[int, int]]
        self.game_over = False

    def restart(self):
        self._active_cells = list(self._starting_cells)

    def _neighbors(self, cell):
        # type: (Tuple[int, int]) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]
        """
        return the list of ON and OFF cells around cell
        """
        on = []
        off = []
        x, y = cell
        for xpos in range(x-1, x+2):
            for ypos in range(y-1, y+2):
                if (xpos, ypos) == cell:
                    continue
                if (xpos, ypos) in self._active_cells:
                    on.append((xpos, ypos))
                else:
                    off.append((xpos, ypos))

        return on, off

    def activeNeighbors(self, cell):
        # type: (Tuple[int, int]) -> List[Tuple[int, int]]
        return self._neighbors(cell)[0]

    def cellState(self, cell):
        # type: (Tuple[int, int]) -> bool
        return cell in self._active_cells

    def cicle(self):
        # type: () -> None
        dead = []
        candidates = defaultdict(list)  # type: DefaultDict
        for cell in self._active_cells:
            on, off = self._neighbors(cell)
            # check rule one
            if len(on) < 2:
                dead.append(cell)
            # check rule three
            if len(on) > 3:
                dead.append(cell)

            for cell in off:
                candidates[cell].append(cell)

        # create new cells
        for cell, neighbors in candidates.items():
            # check rule four
            if len(neighbors) == 3:
                self._active_cells.append(cell)

        # remove dead cells
        for cell in dead:
            self._active_cells.remove(cell)

        if len(self._active_cells) == 0:
            self.game_over = True
        return

    def state(self):
        # type: () -> List[List[bool]]
        lines, cols = self.size
        matrix_state = [[True if self.cellState((x, y)) else False for x in range(lines)] for y in range(cols)]
        return matrix_state
