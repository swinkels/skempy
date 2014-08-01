from argparse import ArgumentParser

import os
import sys

from skempy.test_finder import get_path

import skempy


def main():
    script_name = os.path.basename(sys.argv[0])
    parser = ArgumentParser(prog=script_name,
                            description="Retrieve the method in the given Python file and at the given line.")  # noqa
    parser.add_argument("file_path", help="Python file including path")
    parser.add_argument("line_no", help="line number", type=int)
    version = "{} {}".format(script_name, skempy.__version__)
    parser.add_argument("--version", action="version", version=version)
    args = parser.parse_args()
    print get_path(args.file_path, args.line_no)
