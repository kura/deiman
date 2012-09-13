=====
Usage
=====

To use Deiman, you simply need to import the main Deiman class, 
passing a path to where you want the pid to be stored and call 
the start and stop methods as required::

  from deiman.deiman import Deiman


  d = Deiman("/tmp/a.pid")
  d.start()
  
  while True:
      print "This print will be hidden because I am daemonized"



