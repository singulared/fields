import unittest
from fields import Field, euclid_extended


class IntegerTest(unittest.TestCase):
    def setUp(self):
        Field.prime = 9

    def test_add(self):
        a = Field(7)
        b = Field(2)
        self.assertEqual((a + b).value, 0)
        self.assertEqual((a + 1).value, 8)
        self.assertEqual((a + 2).value, 0)
        self.assertEqual((a + 3).value, 1)
        self.assertEqual((a + Field.prime).value, a.value)
        self.assertEqual((0 + b).value, b.value)
        self.assertEqual((3 + b).value, 5)
        self.assertEqual((8 + b).value, 1)

    def test_mul(self):
        a = Field(7)
        b = Field(2)
        self.assertEqual((a * b).value, 5)
        self.assertEqual((a * 1).value, a.value)
        self.assertEqual((a * 2).value, 5)
        self.assertEqual((a * 0).value, 0)
        self.assertEqual((0 * b).value, 0)
        self.assertEqual((3 * b).value, 6)
        self.assertEqual((8 * b).value, 7)

    def test_sub(self):
        a = Field(7)
        b = Field(2)
        self.assertEqual((a - b).value, 5)
        self.assertEqual((a - 0).value, a.value)
        self.assertEqual((a - 1).value, 6)
        self.assertEqual((a - 8).value, 8)
        self.assertEqual((0 - b).value, 7)
        self.assertEqual((3 - b).value, 1)
        self.assertEqual((8 - b).value, 6)

    def test_neg(self):
        a = Field(7)
        self.assertEqual((-a).value, 2)

    def test_abs(self):
        a = Field(-7)
        self.assertEqual(abs(a), 2)

    def test_eq(self):
        a = Field(7)
        b = Field(2)
        c = Field(5)
        self.assertEqual(a, b + c)
        self.assertEqual(a, a)
        self.assertNotEqual(a, b)
        self.assertNotEqual(a, 7)

    def test_euclid_extended(self):
        a = Field(20, 23)
        b = Field(8, 23)
        self.assertEqual(euclid_extended(a, b)[2].value, 4)
        self.assertEqual(euclid_extended(a, 0)[2], a)

    def test_inverse(self):
        a = Field(7, 23)
        self.assertEqual(a.inverse().value, 10)
        self.assertEqual((a.inverse() * 7).value, 1)


if __name__ == '__main__':
    unittest.main()
