import unittest

from task6 import defaultdict

class Test_default_dictionary(unittest.TestCase):
    def setUp(self):
        self.dct = defaultdict.DefaultDict()
        self.dct1 = defaultdict.DefaultDict()
        self.dct['one']['two'] = 10
        self.dct1['key'][1][10] = 100
        self.value = self.dct1['key'][1][10]
    def test(self):
        self.assertEqual(self.dct, {'one': {'two': 10}})
        self.assertEqual(self.value, 100)

if __name__ == "__main__":
    unittest.main() 