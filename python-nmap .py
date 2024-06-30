# Import the nmap module, which provides functionalities for network scanning
import nmap

# Initialize the PortScanner object from nmap
nm = nmap.PortScanner()

# Define the target IP address to be scanned
target = "45.33.32.156"

# Define the scan options:
# -sV: Probe open ports to determine service/version info
# -sC: Run default scripts
options = "-sV -sC"

# Perform the scan on the target using the defined options
nm.scan(target, arguments=options)

# Iterate over all the hosts found in the scan
for host in nm.all_hosts():
    # Print the host's IP address and its hostname (if available)
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    # Print the state of the host (e.g., 'up' or 'down')
    print("State: %s" % nm[host].state())
    
    # Iterate over all the protocols (e.g., tcp, udp) detected on the host
    for protocol in nm[host].all_protocols():
        # Print the protocol type
        print("Protocol: %s" % protocol)
        # Get port information for the current protocol
        port_info = nm[host][protocol]
        
        # Iterate over each port and its state (e.g., open, closed)
        for port, state in port_info.items():
            # Print the port number and its state
            print("Port: %s\tState: %s" % (port, state))
            
''' This script demonstrates a basic port scanning operation using nmap in Python.
It scans a specified target IP for open ports, determines the services running on those ports, and prints out the results including hostnames and port states.'''
