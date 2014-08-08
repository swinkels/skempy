# -*- coding: utf-8 -*-

import ast
import unittest

from skempy import test_finder

from utils import get_abs_path


class TestTestFinder(unittest.TestCase):

    def test_find_method_in_python_file_in_non_package_directory(self):
        test_file_path = get_abs_path("source_code.py", __file__)
        test_path = test_finder.get_path(test_file_path, 7)
        self.assertEqual("source_code.TestMe.test_a", test_path)

    def test_find_method_in_python_file_in_package_directory(self):
        test_file_path = get_abs_path("package/source_code.py", __file__)
        test_path = test_finder.get_path(test_file_path, 7)
        self.assertEqual("package.source_code.TestMe.test_a", test_path)

    def test_find_module_in_python_file(self):
        test_file_path = get_abs_path("source_code.py", __file__)
        test_path = test_finder.get_path(test_file_path, 0)
        self.assertEqual("source_code", test_path)


class TestLineFinderBaseClass(unittest.TestCase):

    def retrieve_test(self, line_no):
        test_file_path = get_abs_path(self.test_file, __file__)
        with open(test_file_path) as f:
            source_code = f.read()

        tree = ast.parse(source_code)
        line_finder = test_finder.LineFinder(line_no=line_no)
        line_finder.visit(tree)

        return line_finder.path


class TestWithSingleTestCaseFile(TestLineFinderBaseClass):

    def __init__(self, *args, **kwargs):
        super(TestWithSingleTestCaseFile, self).__init__(*args, **kwargs)
        self.test_file = "source_code.py"

    def test_find_method_by_cursor_position_in_body(self):
        self.assertEqual("TestMe.test_a", self.retrieve_test(line_no=7))

    def test_find_method_by_cursor_position_in_method_def(self):
        self.assertEqual("TestMe.test_a", self.retrieve_test(line_no=6))

    def test_find_method_by_cursor_position_in_class_def(self):
        self.assertEqual("TestMe", self.retrieve_test(line_no=4))

    def test_find_method_by_cursor_position_in_class_body(self):
        self.assertEqual("TestMe", self.retrieve_test(line_no=5))


class TestWithMultipleTestCaseFile(TestWithSingleTestCaseFile):

    def __init__(self, *args, **kwargs):
        super(TestWithMultipleTestCaseFile, self).__init__(*args, **kwargs)
        self.test_file = "two_test_cases.py"

    def test_find_method_by_cursor_position_in_second_body(self):
        self.assertEqual("AnotherTestMe.test_b", self.retrieve_test(line_no=14))  # noqa

    def test_find_method_by_cursor_position_in_second_method_def(self):
        self.assertEqual("AnotherTestMe.test_b", self.retrieve_test(line_no=13))  # noqa

    def test_find_method_by_cursor_position_in_second_class_def(self):
        self.assertEqual("AnotherTestMe", self.retrieve_test(line_no=11))

    def test_find_method_by_cursor_position_in_second_class_body(self):
        self.assertEqual("AnotherTestMe", self.retrieve_test(line_no=12))
