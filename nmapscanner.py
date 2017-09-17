import nmap
ns = nmap.PortScanner()
print (ns.nmap_version())
ip = input('Enter the IP address: ')
ns.scan(ip, '1-1024', '-v')
print (ns.scaninfo())

#print (ns.csv())
print (ns.scanstats())
print (ns[ip].state())
print (ns[ip].all_protocols())
print (ns[ip]['tcp'].keys())
port = int(input('\nEnter the port number to be scanned: '))
print (ns[ip].has_tcp(port))
