# 扫描开放端口，此脚本需改进，未能出结果
# -*- coding: UTF-8 -*-
import socket
import sys
from threading import Thread

# Easily changeable variables (you can extend the timeout length if necessary)
threads = []
timeout = 0.5

# Inputs & simple error handling
try:
    host = input("Enter Target Host Address: ")
    hostIP = socket.gethostbyname(host)
    startPort = int(input("Enter Starting Port to Scan: "))
    endPort = int(input("Enter Ending Port to Scan: "))

except KeyboardInterrupt:
    print("\n\n[*]User requested an interrupt[*]")
    sys.exit()

except socket.gaierror:
    print("\n\n[*]Hostname unresolvable[*]")
    sys.exit()

except socket.error:
    print("\n\n[*]Unable to connect to target[*]")
    sys.exit()

# Scanning Banner
print("-" * 50)
print("Scanning Target: ", hostIP)
print("-" * 50)


# Scanning and open port display
def scanner(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(timeout)
    result = sock.connect_ex((hostIP, port))
    if result == 0:
        print("[*] Port {}: Open".format(port))
    sock.close()

# Setup threading and calling the scan
for i in range(startPort, endPort+1):
    thread = Thread(target=scanner, args=(i,))
    threads.append(thread)
    thread.start()

[x.join() for x in threads]

# Completion Banner211.100.61.112
print("-" * 50)
print("Scanning completed!")
print("-" * 50)
