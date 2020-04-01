import nmap
import sys

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0]+ " "+ "ip ")
    sys.exit(1)

target = str(sys.argv[1])
ports = [80,8080]

nm = nmap.PortScanner()

print("\nScanning",target,"for",ports)

for port in ports:
    portscan = nm.scan(target,str(port))
    print("Port",port," is ",portscan['scan'][target]['tcp'][port]['state'])

print("\nHost",target," is ",portscan['scan'][target]['status']['state'])
