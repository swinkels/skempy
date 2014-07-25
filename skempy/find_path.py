from argparse import ArgumentParser

from skempy.test_finder import get_path

def main():
    parser = ArgumentParser(description="Retrieve the method in the given Python file and at the given line.")  # noqa
    parser.add_argument("file_path", help="Python file including path")
    parser.add_argument("line_no", help="line number", type=int)
    args = parser.parse_args()
    print get_path(args.file_path, args.line_no)
