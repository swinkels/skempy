# -*- coding: utf-8 -*-

import unittest

import skempy


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_a(self):
        """Test that a function from the package can be called."""
        skempy.hmm()


if __name__ == '__main__':
    unittest.main()
