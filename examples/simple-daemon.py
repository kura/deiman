import sys

from deiman.deiman import Deiman


d = Deiman("/tmp/deiman.pid")

if len(sys.argv) == 1 or sys.argv[1] not in ('start', 'stop', 'status'):
    print "Usage: simple-daemon.py [start, stop, status]"
    sys.exit(2)

act = sys.argv[1]
if act == "start":
    d.start()
elif act == "stop":
    d.stop()
    sys.exit(0)
elif act == "status":
    d.status()
    sys.exit(0)
else:
    print "Unknown option!"
    sys.exit(2)

while True:
    # do something here, it will only run if action is start
    print "Lalala"
