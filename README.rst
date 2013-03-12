======
Deiman
======

Deiman is a Python utility class for daemonizing a process.
It has start and stop methods, as well as a method for retrieving running status information.

Linux/Unix-only.

Uses the Unix double fork method to fork your process to the background.


Installation
============

From PyPI
~~~~~~~~~

  pip install deiman

Or

  easy_install deiman


From GitHub
~~~~~~~~~~~

  pip install -e git+git://github.com/kura/deiman.git#egg=deiman

From source
~~~~~~~~~~~

Download the latest tarball from PyPI or GitHub. Unpack and run:

  python setup.py install

Usage
=====

To use Deiman, you simply need to import the main Deiman class, 
passing a path to where you want the pid to be stored and call 
the start and stop methods as required::

  from deiman import Deiman


  d = Deiman("/tmp/a.pid")
  d.start()
  
  while True:
      print "This print will be hidden because I am daemonized"

Examples
========

See the examples_ directory for usage examples on GitHub.

.. _examples: https://github.com/kura/deiman/tree/master/examples
