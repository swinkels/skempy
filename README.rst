This repo contains the Python package skempy, which provides functionality to
facilitate Python development in Emacs. At the moment, skempy provides a single
script that returns the method at a given line in a given Python file. You can
call this script from Emacs to, for example, retrieve the test method at point
and execute that test as a compile command.

Installation
------------
 
First clone the skempy repo from Bitbucket::

  $> git clone https://swinkels@bitbucket.org/swinkels/skempy

If you have ssh access to that repo, you can also use the following command::
    
  $> git clone ssh://git@bitbucket.org/swinkels/skempy

Both commands create a copy of the repo in subdirectory skempy.

Then, to actually install skempy, execute the following command::

  $> cd skempy
  $> pip install -e .

When you pass option -e to pip, pip installs skempy in developer mode. This
means that if you modify the skempy source code, the modifications are
immediately accessible.

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

The oot of the repo contains the Emacs Lisp file skempy.el, which provides a
function to retrieve th test method at point and eecutes that test as a compile
command:

.. sourcecode:: lisp

  (defun sks-execute-python-test()
    (interactive)
    (let ((test-method (shell-command-to-string (format "skempy-find-test %s %d" (buffer-file-name) (line-number-at-pos)))))
      (compile (concat "python -m unittest " test-method)))
    )

If you bind it to a key then running the testat point is a single keystroke
away, e.g.:

.. sourcecode:: lisp

  (add-hook 'python-mode-hook
            '(lambda () (local-set-key [C-f7] 'sks-execute-python-test)))
