from scapy.all import *

def sniffPkt(pkt):
	pkt.show()

def start_sniff():	
	scapy_sniff = sniff(prn = sniffPkt, timeout=50, iface = 'eth0', stop_filter = lambda x : x.haslayer(ICMP))
	wrpcap('sniff.pcap', scapy_sniff)

def start_read():
	scapy_cap = rdpcap('sniff.pcap')
	ip_list = []
	for pckt in scapy_cap:
		if IP in pckt:
			if pckt[IP].src not in ip_list:
				ip_list.append(pckt[IP].src)
			else:
				pckt.show()	
	print(ip_list)
		
print("""
	1:sniff
	2:read
	""")
	
choice = input(">> ")

if(choice == "1"):
	start_sniff()

elif(choice == "2"):
	start_read()

else:
	print("Invalid input...")		
