import nmap
scan = nmap.PortScanner()
ip = "10.10.0.1/24"
scan.scan(ip_range,"0-100", '-sV','-sn')
print(scan.scaninfo())
print("host" ,scan[ip].state())
print("Protocols:" ,scan[ip].all_protocols)

print("Opened Ports" ,scanner[ip].keys())

for port in scan[ip]['tcp'].keys():
	name = scan[ip]['tcp][port]['name']
	product = scan[ip]['tcp][port]['product']
	version = scan[ip]['tcp][port]['version']
	print(port, name, product, version)
