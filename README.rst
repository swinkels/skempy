This repo contains the Python package skempy, bwhich provides functionality to
facilitate Python development in Emacs. At the moment, skempy provides a single
script that returns the method at a given line in a given Python file. You can
call this script from Emacs to, for example, retrieve the test method at point
and execute that test as a compile command.

Installation
------------

In this section we describe how to install skempy as an end-user. If you want
to easily fiddle around with the skempy source code, we refer to "For
developers" section of the skempy documentation.

The easiest way to install skempy, is to directly install it from its GitHub
repo. Execute the following command to install the bleeding-edge version from
the master branch:

  $> pip install https://swinkels@bitbucket.org/swinkels/skempy

Usage
-----

When you install skempy, the command line script skempy-find-test is
installed::

  $> skempy-find-test --help
  usage: skempy-find-test [-h] file_path line_no
   
  Retrieve the method in the given Python file and at the given line.
   
  positional arguments:
    file_path   Python file including path
    line_no     line number
   
  optional arguments:
    -h, --help  show this help message and exit
  
Assume you have the Python file source_code.py:

.. sourcecode:: python

  import unittest
   
  class TestMe(unittest.TestCase):
   
      def test_a(self):
          print"Hello World!"
          return

The following snippet shows the output of skempy-find-test::

  $> skempy-find-test tests/source_code.py 7
  source_code.TestMe.test_a

Example Emacs integration
-------------------------

The root of the repo contains the Emacs Lisp file skempy.el, which provides a
function to retrieve the test method at point and executes that test as a compile
command:

.. sourcecode:: common-lisp

  (defun sks-execute-python-test()
    (interactive)
    (let ((test-method (shell-command-to-string (format "skempy-find-test %s %d" (buffer-file-name) (line-number-at-pos)))))
      (compile (concat "python -m unittest " test-method)))
    )

If you bind it to a key then running the test at point is a single keystroke
away, e.g.:

.. sourcecode:: common-lisp

  (add-hook 'python-mode-hook
            '(lambda () (local-set-key [C-f7] 'sks-execute-python-test)))
