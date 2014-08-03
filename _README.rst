.. {{ d['_warning-auto-generated.txt']|indent(3) }}

This repo contains the Python package skempy, which provides functionality to
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

  {{ d['show-help.sh|shint']|indent(2) }}
  
Assume you have the Python file tests/source_code.py:

.. sourcecode:: python
  :linenos:
   
  {{ d['tests/source_code.py']|indent(2) }}
   
The following snippet shows the output of skempy-find-test::

  {{ d['find-test.sh|shint']|indent(2) }}

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
