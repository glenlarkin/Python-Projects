#!/bin/python

import sys
import socket
from datetime import datetime

# Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python 3 scanner.py <ip>")

# Print results
print("-" * 50)
print("Scanning target " + target)
t1 = datetime.now()
print("Time started: "+str(t1))
print("-"*50)

try:
    for port in range(1,1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) # Returns and error indicator
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit()

# Calculate time spent
t2 = datetime.now()

totalTime = t2 - t1
print("-"*50)
print("Time Elapsed: {}".format(totalTime))