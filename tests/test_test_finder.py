# -*- coding: utf-8 -*-

import ast
import unittest

from skempy import test_finder


class TestTestFinder(unittest.TestCase):

    def test_a(self):
        test_path = test_finder.get_path("tests/source_code.py", 7)
        self.assertEqual("source_code.TestMe.test_a", test_path)

    def test_b(self):
        test_path = test_finder.get_path("tests/package/source_code.py", 7)
        self.assertEqual("package.source_code.TestMe.test_a", test_path)

class TestLineFinder(unittest.TestCase):

    def test_a(self):
        f = open("tests/source_code.py")
        source_code = f.read()
        f.close()

        tree = ast.parse(source_code)
        line_finder = test_finder.LineFinder(line_no=7)
        line_finder.visit(tree)

        self.assertEqual("TestMe.test_a", line_finder.path)

    def test_find_method_by_cursor_position_in_method_def(self):
        f = open("tests/source_code.py")
        source_code = f.read()
        f.close()

        tree = ast.parse(source_code)
        line_finder = test_finder.LineFinder(line_no=6)
        line_finder.visit(tree)

        self.assertEqual("TestMe.test_a", line_finder.path)
