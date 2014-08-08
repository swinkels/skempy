import unittest

from skempy.module_path_finder import ModulePathFinder

from utils import get_abs_path


class TestModulePathFinder(unittest.TestCase):

    def test_python_file_in_non_package_directory(self):
        test_file_path = get_abs_path("source_code.py", __file__)
        module_path = ModulePathFinder().find_path(test_file_path)
        self.assertEqual("source_code", module_path)

    def test_python_file_in_package_directory(self):
        test_file_path = get_abs_path("package/source_code.py", __file__)
        module_path = ModulePathFinder().find_path(test_file_path)
        self.assertEqual("package.source_code", module_path)

    def test_python_file_in_package_directory_tree(self):
        test_file_path = get_abs_path("package/sub_package/source_code.py",
                                      __file__)
        module_path = ModulePathFinder().find_path(test_file_path)
        self.assertEqual("package.sub_package.source_code", module_path)
