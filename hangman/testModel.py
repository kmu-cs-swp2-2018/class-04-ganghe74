import unittest
from model import Model

class TestGuess(unittest.TestCase):
    def setUp(self):
        self.model = Model()

    def tearDown(self):
        pass

    def testIncNumTries(self):
        self.model.numTries = 0
        for i in range(1,7):
            self.model.incNumTries()
            self.assertEqual(self.model.numTries, i)

    def testAddGuessedChar(self):
        self.model.addGuessedChar('a')
        self.assertEqual(self.model.guessedChars, 'a')
        self.model.addGuessedChar('b')
        self.assertEqual(self.model.guessedChars, 'ab')
        self.model.addGuessedChar('c')
        self.assertEqual(self.model.guessedChars, 'abc')

    def testFillBlank(self):
        self.model.secretWord = 'testcase'
        self.model.currentStatus = '________'
        self.model.fillBlank('t')
        self.assertEqual(self.model.currentStatus, 't__t____')
        self.model.fillBlank('e')
        self.assertEqual(self.model.currentStatus, 'te_t___e')
        self.model.fillBlank('s')
        self.assertEqual(self.model.currentStatus, 'test__se')
        self.model.fillBlank('c')
        self.assertEqual(self.model.currentStatus, 'testc_se')
        self.model.fillBlank('a')
        self.assertEqual(self.model.currentStatus, 'testcase')

    def testIsSuccess(self):
        self.model.secretWord = 'testcase'
        self.model.currentStatus = '________'
        self.assertFalse(self.model.isSuccess())
        self.model.currentStatus = 'testcase'
        self.assertTrue(self.model.isSuccess())

    def testIsFail(self):
        self.model.numTries = 0
        self.assertFalse(self.model.isFail())
        self.model.numTries = 6
        self.assertTrue(self.model.isFail())

    def testIsFinished(self):
        self.model.numTries = 0
        self.model.secretWord = 'testcase'
        self.model.currentStatus = '________'
        self.assertFalse(self.model.isFinished())
        self.model.numTries = 6
        self.assertTrue(self.model.isFinished())
        self.model.numTries = 0
        self.assertFalse(self.model.isFinished())
        self.model.currentStatus = 'testcase'
        self.assertTrue(self.model.isFinished())

if __name__ == '__main__':
    unittest.main()