import socket
import subprocess
import sys
from datetime import datetime

#Black screen
subprocess.call('clear', shell=True)

#User input
remoteServer = raw_input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

#Print banner with info on host
print("_" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("_" * 60)

#Check date and time
t1 = datetime.now

#Using range function to specify ports

try:
    for port in range(1,5000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP,port))
        if result == 0:
            print("Port {}:    Open").format(port)
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

#Check time again
t2 = datetime.now()

#Calculate the time the scan took
total = t2 - t1

#Print info on screen
print("Scanning Completed in: ", total)