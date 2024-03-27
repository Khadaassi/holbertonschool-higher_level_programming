#!/usr/bin/python3

"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Define Unittests for max_integer """

    def test_empty_list(self):
        """ Test empty list """
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """ Test one element list """
        one = [42]
        self.assertEqual(max_integer(one), 42)

    def test_positive_list(self):
        """ Test positive list """
        positive = [10, 20, 30, 40, 50]
        self.assertEqual(max_integer(positive), 50)

    def test_negative_list(self):
        """ Test negative list """
        negative = [-1, -2, -3, -4, -5]
        self.assertEqual(max_integer(negative), -1)

    def test_mixed_list(self):
        """ Test mixed list """
        mixed = [1, -2, 3, -4, 5]
        self.assertEqual(max_integer(mixed), 5)

    def test_mixed_with_float(self):
        """ Test mixed list with float """
        mixed = [1.1, -2.2, 3.14, -4.0, 5.0]
        self.assertEqual(max_integer(mixed), 5.0)

    def test_duplicate_list(self):
        """ Test duplicate list """
        duplicate = [1, 3, 3, 3, 3]
        self.assertEqual(max_integer(duplicate), 3)

    def test_all_same_list(self):
        """ Test all same list """
        same = [1, 1, 1, 1, 1]
        self.assertEqual(max_integer(same), 1)

    def test_all_same_float(self):
        """ Test all same float """
        same = [1.1, 1.1, 1.1, 1.1, 1.1]
        self.assertEqual(max_integer(same), 1.1)

    def test_float_list(self):
        """ Test float list """
        float = [1.0, 2.2, 3.14, 4.0, 5.2]
        self.assertEqual(max_integer(float), 5.2)

    def test_float_and_int_list(self):
        """ Test float and int list """
        float_int = [1.3, 2, 3.14, 4, 5]
        self.assertEqual(max_integer(float_int), 5)

    def test_negative_float_list(self):
        """ Test negative float list """
        negative_float = [-1.3, -2, -3.14, -4, -5]
        self.assertEqual(max_integer(negative_float), -1.3)

    def test_string_list(self):
        """ Test string list """
        string = ["Hello", "World", "!"]
        self.assertEqual(max_integer(string), "World")

    def test_empty_string(self):
        """ Test empty string """
        empty = ""
        self.assertEqual(max_integer(empty), None)

    def test_max_at_beginning(self):
        """ Test max at beginning """
        beginning = [5, 4, 3, 2, 1]
        self.assertEqual(max_integer(beginning), 5)

    def test_max_in_middle(self):
        """ Test max in middle """
        middle = [1, 2, 10, 4, 5]
        self.assertEqual(max_integer(middle), 10)

    def test_max_reverse_order(self):
        """ Test max reverse order """
        reverse = [10, 9, 8, 7, 6]
        self.assertEqual(max_integer(reverse), 10)

    def test_string_max(self):
        """ Test string max """
        string = "Hello World!"
        self.assertEqual(max_integer(string), "r")

    def test_list_strings(self):
        """ Test list of strings """
        strings = ["Hello", "World", "C'est", "Valentine"]
        self.assertEqual(max_integer(strings), "World")

    def test_large_list(self):
        """ Test large list """
        large = [i for i in range(10000)]
        self.assertEqual(max_integer(large), 9999)

    def test_large_list_negative(self):
        """ Test large list with negative numbers """
        large = [-i for i in range(10000)]
        self.assertEqual(max_integer(large), 0)

    def test_special_characters(self):
        """ Test special characters """
        special = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
        self.assertEqual(max_integer(special), "^")


if __name__ == '__main__':
    unittest.main()
