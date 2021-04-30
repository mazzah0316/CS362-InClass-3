import unittest
import calc

class testCaseAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1,2), 3)
    def test_add_type(self):
        self.assertRaises(TypeError, calc.add, "hi", 4)
class testCaseSub(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.sub(1,2), -1)
    def test_sub_type(self):
        self.assertRaises(TypeError, calc.sub, "hi", 4)
class testCaseMult(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.mult(1,2), 2)
    def test_mult_type(self):
        self.assertIsInstance(calc.mult("hi", 4), (int, float))
class testCaseDiv(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.div(1,2), 0.5)
    def test_div_type(self):
        self.assertRaises(ZeroDivisionError, calc.div, 1, 0)

if __name__ == '__main__':
    unittest.main()