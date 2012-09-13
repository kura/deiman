======
Deiman
======

Deiman is a Python utility class for daemonizing a process.
It has start and stop methods, as well as a method for retrieving running status information.

Linux-only.


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

To use deiman, you simply need to import the main Deiman class and call the start and stop
methods as required::

  from deiman.deiman import Deiman


  d = Deiman("/tmp/a.pid")
  d.start()
  
  while True:
      print "This print will be hidden because I am daemonized"

Examples
========

See the examples directory for usage examples.
