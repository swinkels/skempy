import unittest

from skempy.module_path_finder import ModulePathFinder


class TestModulePathFinder(unittest.TestCase):

    def test_python_file_in_non_package_directory(self):
        module_path = ModulePathFinder().find_path("tests/source_code.py")
        self.assertEqual("source_code", module_path)

    def test_python_file_in_package_directory(self):
        module_path = ModulePathFinder().find_path("tests/package/source_code.py")
        self.assertEqual("package.source_code", module_path)

    def test_python_file_in_package_directory_tree(self):
        module_path = ModulePathFinder().find_path("tests/package/sub_package/source_code.py")
        self.assertEqual("package.sub_package.source_code", module_path)
