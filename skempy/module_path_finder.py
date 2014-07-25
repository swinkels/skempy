import os

class ModulePathFinder(object):

    def find_path(self, file_name):
        module_path, extension = os.path.splitext(os.path.basename(file_name))
        package_dir = os.path.dirname(file_name)
        packages = self.find_parent_packages(package_dir) + [module_path]
        return '.'.join(packages)

    def find_parent_packages(self, directory):
        parent_packages = []
        if self._is_package(directory):
            package_head, package_tail = os.path.split(directory)
            parent_packages = self.find_parent_packages(package_head) + [package_tail]
        return parent_packages

    def _is_package(self, directory):
        return os.path.exists(os.path.join(directory, "__init__.py"))
