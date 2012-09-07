======
Deiman
======

Deiman is a Python utility class for daemonizing a process.
It has start and stop methods, as well as a method for retrieving running status information.

Linux-only.


Installation
============

Install from GitHub using pip::

  pip install -e git+git://github.com/kura/deiman.git#egg=deiman

Install from source::

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

See the ``examples`` directory for usage examples.
