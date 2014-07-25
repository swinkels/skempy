# -*- coding: utf-8 -*-

import skempy

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_a(self):
        """Test that True holds."""
        assert True


if __name__ == '__main__':
    unittest.main()
