import unittest

from main import window
from collections import OrderedDict

class TestSlidingWindow(unittest.TestCase):

    def test_list_empty(self):
        input = []
        self.assertEqual(window(input), [([], None)])

    def test_list_single_item(self):
        input = [1]
        self.assertEqual(window(input), [(1, None)])

    def test_list_multiple_items(self):
        input = [1, 2, 3, 4]
        self.assertEqual(window(input), [(1, 2), (2, 3), (3, 4), (4, None)])

    def test_set(self):  
        input = {1,2,3,4}
        self.assertEqual( window(input),  [(1, 2), (2, 3), (3, 4), (4, None)])
        
    def test_dictionary(self):
        input = {1: "a", 2: "b", 3: "c"}
        self.assertEqual( window(input), [(1,2), (2,3), (3,None)])
        
    def test_ordered_dictionary(self):
        input = OrderedDict({1: "a", 2: "b", 3: "c"})
        self.assertEqual(window(input), [(1, 2), (2, 3), (3, None)])

    def test_ordered_dictionary_interger_string_key_types(self):
        input = OrderedDict({"test": "a", 2: "b", 45: "c"})
        self.assertEqual(window(input), [('test', 2), (2, 45), (45, None)])

if __name__ == '__main__':
    unittest.main()
