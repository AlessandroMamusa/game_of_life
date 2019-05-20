# !/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict


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
        self.size = size
        self._starting_cells = list(starting_cells)
        self._active_cells = list(starting_cells)

    def restart(self):
        self._active_cells = list(self._starting_cells)

    def _neighbors(self, cell):
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
        return self._neighbors(cell)[0]

    def cellState(self, cell):
        return cell in self._active_cells

    def cicle(self):
        dead = []
        candidates = defaultdict(list)
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
        return
