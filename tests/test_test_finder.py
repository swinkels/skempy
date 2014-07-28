# -*- coding: utf-8 -*-

import ast
import os
import unittest

from skempy import test_finder

def _get_file_path(file_name):
    """Return the file path of the given file

    The given file is specified relative to the current file.

    """
    return os.path.join(os.path.dirname(__file__), file_name)


class TestTestFinder(unittest.TestCase):

    def test_find_method_in_python_file_in_non_package_directory(self):
        test_file_path = _get_file_path("source_code.py")
        test_path = test_finder.get_path(test_file_path, 7)
        self.assertEqual("source_code.TestMe.test_a", test_path)

    def test_find_method_in_python_file_in_package_directory(self):
        test_file_path = _get_file_path("package/source_code.py")
        test_path = test_finder.get_path(test_file_path, 7)
        self.assertEqual("package.source_code.TestMe.test_a", test_path)

class TestLineFinder(unittest.TestCase):

    def setUp(self):
        test_file_path = _get_file_path("source_code.py")
        with open(test_file_path) as f:
            self.source_code = f.read()

    def test_find_method_by_cursor_position_in_body(self):
        tree = ast.parse(self.source_code)
        line_finder = test_finder.LineFinder(line_no=7)
        line_finder.visit(tree)

        self.assertEqual("TestMe.test_a", line_finder.path)

    def test_find_method_by_cursor_position_in_method_def(self):
        tree = ast.parse(self.source_code)
        line_finder = test_finder.LineFinder(line_no=6)
        line_finder.visit(tree)

        self.assertEqual("TestMe.test_a", line_finder.path)

    def test_find_method_by_cursor_position_in_class_def(self):
        tree = ast.parse(self.source_code)
        line_finder = test_finder.LineFinder(line_no=4)
        line_finder.visit(tree)

        self.assertEqual("TestMe", line_finder.path)

    def test_find_method_by_cursor_position_in_class_body(self):
        tree = ast.parse(self.source_code)
        line_finder = test_finder.LineFinder(line_no=5)
        line_finder.visit(tree)

        self.assertEqual("TestMe", line_finder.path)


class TestLineFinderForFileWithTwoTestCases(unittest.TestCase):

    def setUp(self):
        test_file_path = _get_file_path("two_test_cases.py")
        with open(test_file_path) as f:
            self.source_code = f.read()

    def test_find_method_by_cursor_position_in_body(self):
        tree = ast.parse(self.source_code)
        line_finder = test_finder.LineFinder(line_no=7)
        line_finder.visit(tree)

        self.assertEqual("TestMe.test_a", line_finder.path)

    def test_find_method_by_cursor_position_in_method_def(self):
        tree = ast.parse(self.source_code)
        line_finder = test_finder.LineFinder(line_no=6)
        line_finder.visit(tree)

        self.assertEqual("TestMe.test_a", line_finder.path)

    def test_find_method_by_cursor_position_in_class_def(self):
        tree = ast.parse(self.source_code)
        line_finder = test_finder.LineFinder(line_no=4)
        line_finder.visit(tree)

        self.assertEqual("TestMe", line_finder.path)

    def test_find_method_by_cursor_position_in_class_body(self):
        tree = ast.parse(self.source_code)
        line_finder = test_finder.LineFinder(line_no=5)
        line_finder.visit(tree)

        self.assertEqual("TestMe", line_finder.path)

    def test_find_method_by_cursor_position_in_second_body(self):
        tree = ast.parse(self.source_code)
        line_finder = test_finder.LineFinder(line_no=14)
        line_finder.visit(tree)

        self.assertEqual("AnotherTestMe.test_b", line_finder.path)

    def test_find_method_by_cursor_position_in_second_method_def(self):
        tree = ast.parse(self.source_code)
        line_finder = test_finder.LineFinder(line_no=13)
        line_finder.visit(tree)

        self.assertEqual("AnotherTestMe.test_b", line_finder.path)

    def test_find_method_by_cursor_position_in_second_class_def(self):
        tree = ast.parse(self.source_code)
        line_finder = test_finder.LineFinder(line_no=11)
        line_finder.visit(tree)

        self.assertEqual("AnotherTestMe", line_finder.path)

    def test_find_method_by_cursor_position_in_second_class_body(self):
        tree = ast.parse(self.source_code)
        line_finder = test_finder.LineFinder(line_no=12)
        line_finder.visit(tree)

        self.assertEqual("AnotherTestMe", line_finder.path)
