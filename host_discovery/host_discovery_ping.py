from scapy.all import *
ip = IP()
icmp = ICMP()
pingPkg = ip/icmp
addr = "10.10.10."
ipList = []
for i in range(256):
	pingPkg[IP].dst = addr+str(i)
	#print(pingPkg[IP].dst)
	response = sr1(pingPkg, timeout = 0.5, verbose = False)
	#print(response)
	if(response):
		#print(pingPkg[IP].dst, "is up")
		ipList.append(pingPkg[IP].dst)
	else:
		pass	
print(ipList)		
