import unittest
import main
import operations

class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):
        testNumbers = [6, 5, 0.32, 0.82, 0, 65, 0.5, 32, 8, 0.506, 432, 456.2, 0]
        main.testCode(testNumbers)
    def test2(self):
        self.assertEqual(operations.multiply(9,2), 18)
    def test3(self):
        self.assertEqual(operations.divide(18,2), 9)

if __name__ == '__main__':
    unittest.main()
