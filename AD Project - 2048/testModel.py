import unittest

from model import Model

class TestPalindrome(unittest.TestCase):
    def setUp(self):
        self.m1 = Model()

    def tearDown(self):
        pass

    def testModel(self):
        self.assertFalse(self.m1.isFinished())
        self.m1.field = [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
        self.assertFalse(self.m1.isFinished())
        self.m1.field = [[2,4,2,4], [4,2,4,2], [2,4,2,4], [4,2,4,2]]
        self.assertTrue(self.m1.isFinished())
        self.m1.field = [[2, 4, 2, 4], [4, 2, 4, 2], [2, 4, 2, 4], [4, 2, 4, 0]]
        self.assertFalse(self.m1.isMovable("up"))
        self.assertTrue(self.m1.isMovable("down"))
        self.assertFalse(self.m1.isMovable("left"))
        self.assertTrue(self.m1.isMovable("right"))
        self.m1.generate(123)
        self.assertEqual(self.m1.field[3][3], 123)


if __name__ == '__main__':
    unittest.main()
