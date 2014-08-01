For developers
==============

In this section we describe how to install skempy as a developer.

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

The option -e that is passed to pip installs skempy in developer mode. If you
modify the skempy source code, the modification are immediately accessible.

The root of the repo contains a Makefile to help you develop skempy. That
Makefile has the following targets:

init
  Installs the development requirements listed in requirements.txt

tests
  Executes the unit tests in subdirectory tests/

docs
  Builds the HTML documentation in subdirectory tests/
