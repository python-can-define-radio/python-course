"""Demonstrates how to run a system command (specifically `ping`).
Based on https://stackoverflow.com/questions/2953462/pinging-servers-in-python"""


import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    procresult = subprocess.run(command, capture_output=True)
    
    return procresult.returncode == 0


for lastOctet in range(0, 256):
    fullIP = f"192.168.0.{lastOctet}"
    pingresult = ping(fullIP)
    print(f"{fullIP:17} {pingresult}")
