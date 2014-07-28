import ast

from module_path_finder import ModulePathFinder


class LineFinder(ast.NodeVisitor):

    def __init__(self, line_no):
        self.line_no = line_no
        self.path = ""

    def visit_ClassDef(self, node):
        self.class_name = node.name

        if node.lineno <= self.line_no:
            self.path = self.class_name

        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        # print ast.dump(node, include_attributes=True)

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
    with open(file_name) as f:
        source_code = f.read()

    module_path = ModulePathFinder().find_path(file_name)

    path_in_code = get_path_in_code(source_code, line_no)
    if path_in_code:
        module_path = module_path + "." + path_in_code

    return module_path
