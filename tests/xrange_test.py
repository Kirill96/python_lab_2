import random
import unittest

from task9.xrange import Myxrange

class Test_my_xrange(unittest.TestCase):
    def setUp(self):
        self.start = random.randint(-25, 50)
        self.stop = random.randint(-50, 100)
        self.step = random.choice([-10, -5, 10, 5, 2, 20, 50])

    def test_generation(self):
        self.assertEqual(list(Myxrange(self.start, self.stop, self.step)),
                         list(range(self.start, self.stop, self.step)))
        self.assertEqual(list(Myxrange(self.start, self.stop)),
                         list(range(self.start, self.stop)))
        self.assertEqual(list(Myxrange(self.stop)),
                         list(range(self.stop)))


if __name__ == "__main__":
    unittest.main()