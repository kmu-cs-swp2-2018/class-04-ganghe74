import unittest
from model import Model
from view import View
from controller import Controller

class TestController(unittest.TestCase):
    def setUp(self):
        self.model = Model()
        self.view = View(self.model)
        self.controller = Controller(self.model, self.view)

    def tearDown(self):
        pass

    def testGuess(self):
        self.model.secretWord = 'testcase'
        self.model.currentStatus = '________'
        self.assertTrue(self.controller.guess('t'))
        self.assertEqual(self.model.currentStatus, 't__t____')
        
        self.assertFalse(self.controller.guess('t'))
        self.assertFalse(self.controller.guess('ab'))

        self.assertTrue(self.controller.guess('x'))
        self.assertTrue(self.controller.guess('y'))
        
        self.assertTrue(self.controller.guess('e'))
        self.assertTrue(self.controller.guess('s'))
        self.assertTrue(self.controller.guess('c'))
        self.assertTrue(self.controller.guess('a'))

        self.assertEqual(self.model.currentStatus, 'testcase')


if __name__ == '__main__':
    unittest.main()