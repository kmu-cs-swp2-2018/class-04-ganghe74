import unittest

from push import *

class TestPalindrome(unittest.TestCase):
    def tearDown(self):
        pass

    def testNormal(self):
        self.list = [[2, 2, 0, 2, 0, 4], [0, 2, 4, 2, 0, 4], [0, 0, 2, 2, 8, 0], [2, 0, 0, 2, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        self.assertEqual(down(self.list, len(self.list))[0], [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 4, 4, 0, 0], [4, 4, 2, 4, 8, 8]])
        self.assertEqual(up(self.list, len(self.list))[0], [[4, 4, 4, 8, 8, 8], [0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
        self.list = [[2, 2, 0, 2, 0, 4], [0, 2, 4, 2, 0, 4], [0, 0, 2, 2, 8, 0], [2, 0, 0, 2, 0, 0], [4, 0, 0, 8, 4, 0], [0, 0, 4, 0, 0, 0]]
        self.assertEqual(left(self.list, len(self.list))[0], [[4, 2, 4, 0, 0, 0], [2, 4, 2, 4, 0, 0], [4, 8, 0, 0, 0, 0], [4, 0, 0, 0, 0, 0], [4, 8, 4, 0, 0, 0], [4, 0, 0, 0, 0, 0]])
        self.assertEqual(right(self.list, len(self.list))[0], [[0, 0, 0, 4, 2, 4], [0, 0, 2, 4, 2, 4], [0, 0, 0, 0, 4, 8], [0, 0, 0, 0, 0, 4], [0, 0, 0, 4, 8, 4], [0, 0, 0, 0, 0, 4]])
        self.list = [[0 for i in range(6)] for j in range(6)]
        self.list[0][0] = 2
        self.list[0][1] = 2
        self.list, score = right(self.list, len(self.list))
        self.assertEqual(score, 4)