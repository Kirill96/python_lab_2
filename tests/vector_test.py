import unittest

from task4 import vector
from task4.vector import Vector

class Test_vector(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(1, 2, 3)
        self.v2 = Vector(2, 4, 6)
        self.v3 = Vector(1, 2, 3, 5)
        self.v4 = Vector(2, 4, 6)
    def test_add(self):
        self.assertEqual(self.v1 + self.v2, Vector(3, 6, 9))
    def test_sub(self):
        self.assertEqual(self.v4 - self.v1, Vector(1, 2, 3))
    def test_mul(self):
        self.assertEqual(self.v1 * self.v2, Vector(2, 8, 18))
        self.assertEqual(self.v1 * 'a', Vector('a', 'aa', 'aaa'))
    def test_length(self):
        self.assertEqual(round(self.v3.len()), 6.0)
    def test_eq(self):
        self.assertEqual(self.v2 == self.v4, True)
    def test_ne(self):
        self.assertEqual(self.v1 != self.v3, True)
    def test_get_item(self):
        self.assertEqual(self.v3[3], 5)

if __name__ == "__main__":
    unittest.main()