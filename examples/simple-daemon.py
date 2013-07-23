# Need sys for exit status and argv
import sys

# Import Deiman
from deiman import Deiman


# Create a new instance of Deiman, passing in a PID file to use
# this only instantiates the class, nothing more.
d = Deiman("/tmp/deiman.pid")

# Check incoming argv values to see if we have start, stop or status
# command.
if len(sys.argv) == 1 or sys.argv[1] not in ('start', 'stop', 'status'):
    print("Usage: python simple-daemon.py [start, stop, status]")
    sys.exit(2)

# Set the incoming action to a shorter variable name, lazy.
act = sys.argv[1]
# Action is start, so tell Deiman to fork itself off in to the
# background.
if act == "start":
    d.start()
# Action is stop, this will take the existing PID file, get the
# current process ID and stop the running process.
elif act == "stop":
    d.stop()
    sys.exit(0)
# Action is status, this will get the current status information
# of the process from /proc. It'll tell you if it's running or not
# and also if it's a zombie process.
elif act == "status":
    d.status()
    sys.exit(0)
else:
    print("Unknown option!")
    sys.exit(2)

# Now we loop to keep the process a live until it's stopped.
while True:
    # do something here, it will only run if action is start
    print("Lalala")
