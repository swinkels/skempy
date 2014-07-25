import ast
import os

from module_path_finder import ModulePathFinder

class LineFinder(ast.NodeVisitor):

    def __init__(self, line_no):
        self.line_no = line_no
        self.path = ""

    def visit_ClassDef(self, node):
        self.class_name = node.name
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        print ast.dump(node, include_attributes=True)

        if node.lineno == self.line_no:
            self.path = "%s.%s" % (self.class_name, node.name)
        else:
            for statement_node in node.body:
                if statement_node.lineno == self.line_no:
                    self.path = "%s.%s" % (self.class_name, node.name)

        if not self.path:
            self.generic_visit(node)

def get_path_in_code(source_code, line_no):

    tree = ast.parse(source_code)
    line_finder = LineFinder(line_no)
    line_finder.visit(tree)

    return line_finder.path

def get_path(file_name, line_no):
    f = open(file_name)
    source_code = f.read()
    f.close()

    module_path = ModulePathFinder().find_path(file_name)
    return module_path + '.' + get_path_in_code(source_code, line_no)
