#!/usr/bin/python3

"""Ufgfg rfgrgftr gtrgtrg trg)."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Dfvf fvfrvfr frfref refrefref..])."""

    def test_ordered_list(self):
        """Tefdgrt grtgtrgtrg rtgtrgtr trgtrs."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Tesgtrgtr gtrgtrg trgtr trgtrg trgtrg."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """Testgbrttr trgtrgtrg trgtrgtrgtr gtre."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """gtrgtrg trgtrgtr gtrgtrt."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Testrgrgr gtrgtrg trgtrelement."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Tetrgt gtrgtrg trgtrgs."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Testrrgtr gtrgtrg trgtrg ats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Tesgftrg trgtrg."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Ttrg trgtrgtr gtrgings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Tetrgtrg tgtrgtr gtrging."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
