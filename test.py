# !/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from game_of_life import Game

"""
GAME OF LIFE TEST SUIT

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


class TestCell(unittest.TestCase):

    def setUp(self):
        self.adam = (10, 10)
        self.game = Game((20, 20), [self.adam])

    def tearDown(self):
        self.game.restart()

    def testRestart(self):
        self.assertEqual(len(self.game._active_cells), 1)
        self.assertEqual(self.game._active_cells[0], self.adam)
        # turn ON (0,0) and (1,1)
        self.game._active_cells.extend([(0, 0), (1, 1)])

        self.game.restart()

        self.assertEqual(len(self.game._active_cells), 1)
        self.assertEqual(self.game._active_cells[0], self.adam)

    def testNeighbors(self):
        self.assertEqual(len(self.game.neighbors(self.adam)), 0)

    def testCellState(self):
        self.assertTrue(self.game.cellState(self.adam))
        self.assertFalse(self.game.cellState((0, 0)))

    def testRuleOne(self):
        """
        1 - If a cell is ON and has fewer than two neighbors that are ON, it
        turns OFF.
        """
        self.assertTrue(self.game.cellState(self.adam))
        self.game.cicle()
        self.assertFalse(self.game.cellState(self.adam))

        # restart and add a neighbors to adam
        self.game.restart()
        eve = (10, 11)
        self.game._active_cells.append(eve)
        self.assertEqual(len(self.game._active_cells), 2)

        self.game.cicle()
        self.assertFalse(self.game.cellState(self.adam))
        self.assertFalse(self.game.cellState(eve))
        self.assertEqual(len(self.game._active_cells), 0)

    def testRuleTwo(self):
        """
        2 - If a cell is ON and has either two or three neighbors that are ON,
        it remains ON.
        """
        self.assertTrue(self.game.cellState(self.adam))

        # two neighbors
        pinco, panco = (10, 9), (10, 11)
        self.game._active_cells.extend([pinco, panco])
        self.game.cicle()
        self.assertTrue(self.game.cellState(self.adam))

        # three neighbors
        qui, quo, qua = (9, 9), (9, 10), (9, 11)
        self.game._active_cells.extend([qui, quo, qua])
        self.game.cicle()
        self.assertTrue(self.game.cellState(self.adam))


if __name__ == '__main__':
    unittest.main()
