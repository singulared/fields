import unittest
from fields import Integer


class IntegerTest(unittest.TestCase):
    def setUp(self):
        Integer.prime = 9

    def test_addition(self):
        a = Integer(7)
        b = Integer(2)
        self.assertEqual((a + b).value, 0)
        self.assertEqual((a + 1).value, 8)
        self.assertEqual((a + 2).value, 0)
        self.assertEqual((a + 3).value, 1)
        self.assertEqual((a + Integer.prime).value, a.value)
        self.assertEqual((0 + b).value, b.value)
        self.assertEqual((3 + b).value, 5)
        self.assertEqual((8 + b).value, 1)

    def test_multiplication(self):
        a = Integer(7)
        b = Integer(2)
        self.assertEqual((a * b).value, 5)
        self.assertEqual((a * 1).value, a.value)
        self.assertEqual((a * 2).value, 5)
        self.assertEqual((a * 0).value, 0)
        self.assertEqual((0 * b).value, 0)
        self.assertEqual((3 * b).value, 6)
        self.assertEqual((8 * b).value, 7)

if __name__ == '__main__':
    unittest.main()
