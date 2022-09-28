#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_module_docstring(self):
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_fun_docstring(self):
        f = __import__('6-max_integer').__doc__
        self.assertTrue(len(f) > 1)

    def test_empty_string(self):
        s = []
        self.assertIsNone(max_integer(s))

    def test_0_args(self):
        self.assertIsNone(max_integer())


    def test_non_int_arg(self):
        string = [1, 2, "You",4]
        with self.assertRaises(TypeError):
            max_integer(string)

    def test_positive(self):
        s = [ 1, 33, 78, 95, 3, 867]
        self.assertEqual(max_integer(s), 867)

    def test_negative(self):
        s = [-133, -33, -1, -78, -95, -3, -867]
        self.assertEqual(max_integer(s), -1)

    def test_none_arg(self):
        with self.assertRaises(TypeError):
            max_integer(None)

