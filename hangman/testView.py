import unittest
from model import Model
from view import View

class TestView(unittest.TestCase):
    def setUp(self):
        self.model = Model()
        self.view = View(self.model)

    def tearDown(self):
        pass

    def testInputChar(self):
        for char in ['test', 'case', '', 'apple']:
            print("please input \""+char+"\"")
            self.assertEqual(char, self.view.inputChar())

if __name__ == '__main__':
    unittest.main()