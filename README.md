# Nmap Port Scanner

This Python script provides a custom implementation of a port scanner using the `nmap` library. Ideal for web developers and students, it empowers you to:

- **Perform Network Scans:** Leverage Nmap's powerful features to scan target IP addresses and gather detailed information about open ports and running services.
- **Understand Network Security:** Gain practical experience with network scanning and security assessment tools, laying the groundwork for exploring more advanced network security topics.

## Features

- **Port Scanning:** Perform comprehensive scans on target IP addresses to identify open ports and the services running on them.
- **Service Version Detection:** Determine the version of services running on discovered ports.
- **Default Script Execution:** Utilize Nmap's default scripts to gather additional information about the target.

## Prerequisites

Before running the script, ensure you have the following:

- **Python 3:** Make sure Python 3 is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).
- **Nmap:** Install Nmap on your system. Download it from the [official Nmap website](https://nmap.org/download.html).
- **Python Nmap Library:** Install the `python-nmap` library using pip.

## Installation

1. **Install Nmap:**
   - Follow the instructions on the [Nmap download page](https://nmap.org/download.html) to install Nmap on your operating system.

2. **Install the Python Nmap Library:**
   
   ```pip install python-nmap```

## Explanation:
- Import the nmap module: This module provides the PortScanner class to perform network scans.
- Initialize the PortScanner object: An instance of PortScanner is created to perform the scan.
- Define the target IP address: The IP address to be scanned is specified.
- Define the scan options:
. sV probes open ports to determine service/version info.
. sC runs default scripts.
- Perform the scan: The scan method of the PortScanner object is called with the target and options.
- Iterate over all hosts found in the scan: The results are processed, printing the host's IP, hostname, state, and details of each detected protocol and port.
