import unittest
from word import Word

class TestView(unittest.TestCase):
    def setUp(self):
        self.word = Word('words.txt')

    def tearDown(self):
        pass

    def testTest(self):
        self.assertEqual(self.word.test(), 'default')

    def testRandFromDB(self):
        word = self.word.randFromDB()
        print(word)
        self.assertEqual(type(word), str)

if __name__ == '__main__':
    unittest.main()