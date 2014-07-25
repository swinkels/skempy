import os

class ModulePathFinder(object):

    def find_path(self, file_path):
        directory, file_name = os.path.split(file_path)
        module_name, _ = os.path.splitext(file_name)
        return '.'.join(self.find_packages(directory) + [module_name])

    def find_packages(self, directory):
        if not self._is_package(directory):
            return []
        parent_directory, package_name = os.path.split(directory)
        return self.find_packages(parent_directory) + [package_name]

    def _is_package(self, directory):
        return os.path.exists(os.path.join(directory, "__init__.py"))
