# -*- coding: utf-8 -*-

import os


def get_abs_path(rel_path_requested_file, abs_path_current_file):
    """Return the absolute path to the given requested file.

    The path to the given requested file is specified relative to the absolute
    path of the current file.

    """
    return os.path.join(os.path.dirname(abs_path_current_file),
                        rel_path_requested_file)
