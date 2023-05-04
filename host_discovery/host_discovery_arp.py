from scapy.all import *

eth = Ether()
arp = ARP()

eth.dst = "ff:ff:ff:ff:ff:ff"
arp.pdst = "10.10.10.0/24"

broadcastPkg = eth/arp
ans, unans = srp(broadcastPkg, timeout = 5)

ans.summary()
print("#"*30)
unans.summary()

for snd,rcv in ans:
	rcv.show()
	print(rcv.src, ":" ,rsv.psrc)
