# !/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from game_of_life import Game

"""
GAME OF LIFE TEST SUIT

rules:
- If a cell is ON and has fewer than two neighbors that are ON, it
turns OFF.
- If a cell is ON and has either two or three neighbors that are ON,
it remains ON.
- If a cell is ON and has more than three neighbors that are ON, it
turns OFF.
- If a cell is OFF and has exactly three neighbors that are ON, it
turns ON.
"""


class TestCell(unittest.TestCase):

    def setUp(self):
        self.adam = (10, 10)
        self.game = Game((20, 20), [self.adam])

    def testNeighbors(self):
        self.assertEqual(len(self.game.neighbors(self.adam)), 0)


if __name__ == '__main__':
    unittest.main()
