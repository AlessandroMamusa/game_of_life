# !/usr/bin/env python
# -*- coding: utf-8 -*-


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

    def neighbors(self, cell):
        """
        return the list of ON cells around cell
        """
        neighbors = []
        x, y = cell
        for xpos in range(x-1, x+2):
            for ypos in range(y-1, y+2):
                if (xpos, ypos) == cell:
                    continue
                if (xpos, ypos) in self._active_cells:
                    neighbors.append((xpos, ypos))

        return neighbors

    def cellState(self, cell):
        return cell in self._active_cells

    def cicle(self):
        dead = []
        for cell in self._active_cells:
            # check rule one
            if len(self.neighbors(cell)) < 2:
                dead.append(cell)

        for cell in dead:
            self._active_cells.remove(cell)
        return

