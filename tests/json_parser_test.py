import json
import unittest

from task3 import to_json

class Test_my_json(unittest.TestCase):
    def setUp(self):
        self.obj = {'one': 1, 'two': [1, 2, 3],
                    'three': True, 'four': None}
        self.obj1 = [1, 'aaa', {'python': 'cool'}]

    def test(self):
        self.assertEqual(to_json.to_json(self.obj), json.dumps(self.obj))
        self.assertEqual(to_json.to_json(self.obj1), json.dumps(self.obj1))
        self.assertRaises(to_json.MyException, to_json.to_json, {12: str})

if __name__ == "__main__":
    unittest.main()